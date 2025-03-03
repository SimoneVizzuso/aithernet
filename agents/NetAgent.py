from mesa import Agent
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    health: int = Field(default=100, ge=0)
    hunger: int = Field(default=0, ge=0)
    energy: int = Field(default=100, ge=0)


class NetAgent(Agent):
    def __init__(self, unique_id, model, state: AgentState = None, *args, **kwargs):
        """
        Initialize a new agent with a unique ID, a reference to the model,
        and a validated state.

        Parameters:
          unique_id: A unique identifier for the agent.
          model: The simulation model in which the agent operates.
          state: A validated state for the agent (default values are provided if None).
        """
        super().__init__(model, *args, **kwargs)
        self.unique_id = unique_id
        self.model = model
        # Register the agent with the model if available
        if hasattr(model, 'register_agent'):
            model.register_agent(self)
        self.state = state or AgentState()

    def step(self):
        """
        Called at each iteration of the simulation.
        """
        self.act()

    def act(self):
        """
        Basic logic for the agent:
          - Increase hunger level.
          - Decrease energy level.
          - If hunger exceeds a threshold (e.g., 50), decrease health.
        """
        self.state.hunger += 1
        self.state.energy -= 1

        if self.state.hunger > 50:
            self.state.health -= 1

        # Additional logic (e.g., movement, interactions) will be added here
