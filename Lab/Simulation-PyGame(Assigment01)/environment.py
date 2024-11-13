class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def limit_position(self, position):
        """Ensure the agent's position wraps around the environment boundaries."""
        x, y = position
        x = x % self.width  
        y = y % self.height
        return [x, y]
