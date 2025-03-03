from agents.NetAgent import NetAgent
from world.DummyModel import DummyModel


class Environment:
    def __init__(self, model=None):
        """
        Initialize an empty simulation world.
        """
        if model is None:
            model = DummyModel()
        self.model = model
        self.agents = []

    def add_agent(self, unique_id=None):
        """
        Create and add a new agent to the world.

        Parameters:
          unique_id: Optional unique identifier for the new agent.
                     If not provided, it is set to the current number of agents.

        Returns:
          The newly created agent.
        """
        if unique_id is None:
            unique_id = len(self.agents)
        agent = NetAgent(unique_id=unique_id, model=self.model)
        self.agents.append(agent)
        return agent

    def step(self):
        """
        Execute one simulation step by calling each agent's step method.
        """
        for agent in self.agents:
            agent.step()

    def run(self, steps: int):
        """
        Run the simulation for a specified number of steps.
        """
        for _ in range(steps):
            self.step()
