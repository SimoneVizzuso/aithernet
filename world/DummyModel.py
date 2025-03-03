from mesa import Model


class DummyModel(Model):
    # DummyModel to satisfy the model requirement for testing

    def register_agent(self, agent):
        pass