import pytest
from world.Environment import Environment


# Create a dummy model to use in tests.
class DummyModel:
    def register_agent(self, agent):
        pass


@pytest.fixture
def world_instance():
    return Environment(model=DummyModel())


def test_add_agent(world_instance):
    # Initially, the world has no agents.
    initial_count = len(world_instance.agents)
    agent = world_instance.add_agent()
    # If no unique_id is provided, it should be set to the current count.
    assert agent.unique_id == initial_count
    # The agent count should have increased by one.
    assert len(world_instance.agents) == initial_count + 1


def test_run_steps(world_instance):
    # Add two agents.
    world_instance.add_agent()  # Agent with id 0.
    world_instance.add_agent()  # Agent with id 1.

    # Capture initial states.
    initial_states = [(agent.state.health, agent.state.hunger, agent.state.energy)
                      for agent in world_instance.agents]

    # Run one simulation step.
    world_instance.run(1)

    # Verify that each agent's state has updated.
    for (health, hunger, energy), agent in zip(initial_states, world_instance.agents):
        expected_hunger = hunger + 1
        expected_energy = energy - 1
        # If hunger was already high, health should decrease.
        expected_health = health - 1 if hunger >= 50 else health
        assert agent.state.hunger == expected_hunger
        assert agent.state.energy == expected_energy
        assert agent.state.health == expected_health
