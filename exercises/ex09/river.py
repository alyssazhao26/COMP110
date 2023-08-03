"""File to define River class."""
__author__ = "730615172"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River Class."""
    
    # attributes
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
    
    def remove_fish(self, amount: int):
        """Remove fish from river."""
        exist_fish: list[Fish] = []
        for i in range(amount, len(self.fish)):
            exist_fish.append(self.fish[i])
        self.fish = exist_fish
        return None

    def bears_eating(self):
        """Determine the amount of fish bears will eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Checks bear's hunger score."""
        exist_bear: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                exist_bear.append(bear)
        self.bears = exist_bear
        return None

    def check_ages(self):
        """Create lists of surviving bears and fish."""
        survive_bears: list[Bear] = []
        survive_fish: list[Fish] = []
        for bear in self.bears:
            if bear.age <= 5:
                survive_bears.append(bear)
        for fish in self.fish:
            if fish.age <= 3:
                survive_fish.append(fish)
        self.bears = survive_bears
        self.fish = survive_fish
        return None

    def repopulate_fish(self):
        """Recalulate bears' population."""
        num_new: int = len(self.fish) // 2
        new_fish: list[Fish] = self.fish
        for i in range(0, num_new):
            for fish in range(0, 4):
                new_fish.append(Fish())
        self.fish = new_fish
        return None
    
    def repopulate_bears(self):
        """Recalculate fish population."""
        new_bears: list[Bear] = self.bears
        num_new: int = len(self.bears) // 2
        for i in range(0, num_new):
            new_bears.append(Bear())
        self.bears = new_bears
        return None
    
    def view_river(self):
        """Print out the river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulation for 1 day."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulation for 1 week."""
        for i in range(1, 8):
            self.one_river_day()
        return None