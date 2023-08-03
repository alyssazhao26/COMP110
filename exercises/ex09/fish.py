"""File to define Fish class."""
__author__ = "730615172"


class Fish:
    """Fish Class."""

    # Attributes
    age: int

    def __init__(self):
        """Class entry."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates for one day."""
        self.age += 1
        return None