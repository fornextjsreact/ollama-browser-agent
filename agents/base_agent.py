class BaseAgent:
    def __init__(self):
        pass

    def act(self):
        raise NotImplementedError("Subclasses should implement this method")

    def think(self):
        raise NotImplementedError("Subclasses should implement this method")

    def communicate(self):
        raise NotImplementedError("Subclasses should implement this method")

    # Add other methods that are common for all agents
