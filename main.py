from world.Environment import Environment


def main():
    env = Environment()

    env.add_agent()  # Adds an agent with unique_id 0

    env.run(1)

    for agent in env.agents:
        print(f"Agent {agent.unique_id}: Health = {agent.state.health}, "
              f"Hunger = {agent.state.hunger}, Energy = {agent.state.energy}")


if __name__ == "__main__":
    main()
