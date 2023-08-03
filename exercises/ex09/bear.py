"""File to define Bear class."""
__author__ = "730615172"


class Bear:
    """Bear Class."""
    
    # Attributes
    age: int
    hunger_score: int

    def __init__(self):
        """Class entry."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulates for one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Update bears hunger score."""
        self.hunger_score += num_fish
        return None