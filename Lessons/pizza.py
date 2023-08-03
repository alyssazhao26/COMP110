"""Define Pizza Class"""

class Pizza:

    # attributes
    size: str # 'small' or 'large'
    topping: int
    gluten_free: bool 

    def __init__(self, size_input: str, topping_input: int, gluten_input: bool): 
        self.size = size_input 
        self.topping = topping_input
        self.gluten_free = gluten_input
        # This function returns self

    def price(self) -> float:
        """price of pizza"""
        cost: float = 0.0
        if self.size == "Large":
            cost = 6.0
        else:
            cost = 5.0
        # 75 cents per topping
        cost += 0.75 * self.topping
        # add 1 if gluten free
        if self.gluten_free:
            cost += 1
        return cost
    
    def add_topping(self, num_toppings: int) -> None:
        """Add a certain number of toppings."""
        self.topping += num_toppings