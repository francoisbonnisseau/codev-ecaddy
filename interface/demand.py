import numpy as np 

class Demand:
    last_id = 0  # Class variable to track the last assigned ID

    def __init__(self, name, brand='', budget_limit=np.inf, store='', quantity=1, price_min=0):
        """
        Initializes a Demand object.

        Args:
            name (str): The name of the demand.
            brand (str, optional): The brand of the demand. Defaults to ''.
            budget_limit (float, optional): The budget limit of the demand. Defaults to np.inf.
            store (str, optional): The store of the demand. Defaults to ''.
            quantity (int, optional): The quantity of the demand. Defaults to 1.
            price_min (float, optional): The minimum price of the demand. Defaults to 0.

        Raises:
            ValueError: If any input type is invalid or if budget_limit, quantity, or price_min is invalid.
        """
        # Validate name
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self.name = name

        # Validate brand
        if not isinstance(brand, str):
            raise ValueError("brand must be a string")
        self.brand = brand

        # Validate budget_limit
        if not isinstance(budget_limit, (int, float)):
            raise ValueError("budget_limit must be a number")
        if budget_limit <= 0:
            raise ValueError("budget_limit must be greater than 0")
        self.budget_limit = budget_limit

        # Validate price_min
        if not isinstance(price_min, (int, float)):
            raise ValueError("price_min must be a number")
        if price_min < 0:
            raise ValueError("bprice_min must be greater than 0")
        self.price_min = price_min
        
        # Validate store
        if not isinstance(store, str):
            raise ValueError("store must be a string")
        self.store = store

        # Validate quantity
        if not isinstance(quantity, int):
            raise ValueError("quantity must be an integer")
        if quantity <= 0:
            raise ValueError("quantity must be greater than 0")
        self.quantity = quantity

        # Increment the last ID when a new instance is created
        Demand.last_id += 1
        self.id = Demand.last_id

    def get_id(self):
        """Get the ID of the demand."""
        return self.id

    def get_name(self):
        """Get the name of the demand."""
        return self.name

    def get_brand(self):
        """Get the brand of the demand."""
        return self.brand

    def get_budget_limit(self):
        """Get the budget limit of the demand."""
        return self.budget_limit

    def get_store(self):
        """Get the store of the demand."""
        return self.store

    def get_quantity(self):
        """Get the quantity of the demand."""
        return self.quantity
    def get_price_min(self):
        return self.price_min
    
    

if __name__ == "__main__":
    # Test cases for Demand class
    demand1 = Demand(name="Chair", brand="BrandX", budget_limit=50.0, store="Store A")
    # Test case 1: Valid input
    try:
        demand1 = Demand(name="Chair", brand="BrandX", budget_limit=50.0, store="Store A", quantity=2)
        print("Test case 1 passed: Valid input")
    except ValueError:
        print("Test case 1 failed: Valid input")

    # Test case 2: Invalid input - name should be a string
    try:
        Demand(name=123, brand="BrandX", budget_limit=50.0, store="Store A", quantity=2)
        print("Test case 2 failed: Invalid input - name should be a string")
    except ValueError:
        print("Test case 2 passed: Invalid input - name should be a string")

    # Test case 3: Invalid input - brand should be a string
    try:
        Demand(name="Chair", brand=123, budget_limit=50.0, store="Store A", quantity=2)
        print("Test case 3 failed: Invalid input - brand should be a string")
    except ValueError:
        print("Test case 3 passed: Invalid input - brand should be a string")

    # Test case 4: Invalid input - budget_limit should be a positive number
    try:
        Demand(name="Chair", brand="BrandX", budget_limit="50.0", store="Store A", quantity=2)
        print("Test case 4 failed: Invalid input - budget_limit should be a number")
    except ValueError:
        print("Test case 4 passed: Invalid input - budget_limit should be a number")
    try:
        Demand(name="Chair", brand="BrandX", budget_limit=-50.0, store="Store A", quantity=2)
        print("Test case 4 failed: Invalid input - budget_limit should be a positive number")
    except ValueError:
        print("Test case 4 passed: Invalid input - budget_limit should be a positive number")
    # Test case 5: Invalid input - budget_limit should be greater than 0
    try:
        Demand(name="Chair", brand="BrandX", budget_limit=-50.0, store="Store A", quantity=2)
        print("Test case 5 failed: Invalid input - budget_limit should be greater than 0")
    except ValueError:
        print("Test case 5 passed: Invalid input - budget_limit should be greater than 0")

    # Test case 6: Invalid input - store should be a string
    try:
        Demand(name="Chair", brand="BrandX", budget_limit=50.0, store=123, quantity=2)
        print("Test case 6 failed: Invalid input - store should be a string")
    except ValueError:
        print("Test case 6 passed: Invalid input - store should be a string")

    # Test case 7: Invalid input - quantity should be an integer
    try:
        Demand(name="Chair", brand="BrandX", budget_limit=50.0, store="Store A", quantity="2")
        print("Test case 7 failed: Invalid input - quantity should be an integer")
    except ValueError:
        print("Test case 7 passed: Invalid input - quantity should be an integer")
    try:
        Demand(name="Chair", brand="BrandX", budget_limit=50.0, store="Store A", quantity=-2)
        print("Test case 7 failed: Invalid input - quantity should be a positive integer")
    except ValueError:
        print("Test case 7 passed: Invalid input - quantity should be a positive integer")
        

    # Test case 8: Invalid input - quantity should be greater than 0
    try:
        Demand(name="Chair", brand="BrandX", budget_limit=50.0, store="Store A", quantity=0)
        print("Test case 8 failed: Invalid input - quantity should be greater than 0")
    except ValueError:
        print("Test case 8 passed: Invalid input - quantity should be greater than 0")
    # Test case 9: Verify uniqueness and incrementation of ID with 10 demands
    try:
        demands = []
        for i in range(10):
            demands.append(Demand(name=f"Chair{i+1}", brand="BrandX", budget_limit=50.0, store="Store A", quantity=2))
        
        for i in range(1, len(demands)):
            assert demands[i].get_id() == demands[i-1].get_id() + 1  # IDs should increment by 1
        print("Test case 9 passed: ID uniqueness and incrementation with 10 demands")
    except AssertionError:
        print("Test case 9 failed: ID uniqueness and incrementation with 10 demands")
