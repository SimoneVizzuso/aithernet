import pytest
from mesa import Model

from agents.NetAgent import NetAgent


# Create a dummy model that satisfies the registration requirement.
class DummyModel(Model):
    def register_agent(self, agent):
        pass


@pytest.fixture
def dummy_model():
    return DummyModel()


@pytest.fixture
def agent(dummy_model):
    return NetAgent(unique_id=0, model=dummy_model)


def test_initial_state(agent):
    # Verify the agent's initial state.
    state = agent.state
    assert state.health == 100
    assert state.hunger == 0
    assert state.energy == 100


def test_step_updates_state(agent):
    # Capture the initial state.
    init_health = agent.state.health
    init_hunger = agent.state.hunger
    init_energy = agent.state.energy

    # Call step to update the state.
    agent.step()

    # Expect hunger increased by 1 and energy decreased by 1.
    assert agent.state.hunger == init_hunger + 1
    assert agent.state.energy == init_energy - 1
    # Health should remain unchanged if hunger is below threshold.
    assert agent.state.health == init_health


def test_health_decreases_when_hunger_high(agent):
    # Manually set hunger above the threshold.
    agent.state.hunger = 51
    init_health = agent.state.health

    # Call the act() method.
    agent.act()

    # Expect health to decrease by 1.
    assert agent.state.health == init_health - 1
