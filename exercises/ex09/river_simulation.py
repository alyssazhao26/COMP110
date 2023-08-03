"""Ex09 River Simulation."""
__author__ = "730615172"

from exercises.ex09.river import River

my_river: River = River(10, 2)


"""my_river.view_river()
my_river.one_river_week()
print(len(my_river.fish))"""
my_river.repopulate_fish()
print(len(my_river.fish))

my_river.repopulate_bears()
print(len(my_river.bears))