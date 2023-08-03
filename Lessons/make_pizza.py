"""Instantiating Pizza class"""

from Lessons.pizza import Pizza

my_pizza: Pizza = Pizza("Large", 1, True)
sals_pizza: Pizza = Pizza("Small", 2, False)

a = my_pizza
my_pizza.add_topping(2)
print(my_pizza.topping)
print(a.topping)
# def price(pizza_order: Pizza) -> float:
#     """Calculate and return the cost of ordered pizza."""
#     cost: float = 0.0
#     if pizza_order.size == "Large":
#         cost = 6.0
#     else:
#         cost = 5.0
#     # 75 cents per topping
#     cost += 0.75 * pizza_order.topping
#     # add 1 if gluten free
#     if pizza_order.gluten_free:
#         cost += 1
#     return cost

