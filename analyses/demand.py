# demand.py
class Demand:
    def __init__(self, nature, name, brand, price_limit, store, nutri_scores, quantity):
        # Validate demand_type
        if not isinstance(nature, str):
            raise ValueError("nature must be a string")
        self.nature = nature

        # Validate name
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self.name = name

        # Validate brand
        if not isinstance(brand, str):
            raise ValueError("brand must be a string")
        self.brand = brand

        # Validate price_limit
        if not isinstance(price_limit, (int, float)):
            raise ValueError("price_limit must be a number")
        if price_limit <= 0:
            raise ValueError("price_limit must be greater than 0")
        self.price_limit = price_limit

        # Validate store
        if not isinstance(store, str):
            raise ValueError("store must be a string")
        self.store = store

        # Validate nutri_scores
        if not isinstance(nutri_scores, str):
            raise ValueError("nutri_scores must be a string")
        self.nutri_scores = nutri_scores

        # Validate quantity
        if not isinstance(quantity, int):
            raise ValueError("quantity must be an integer")
        if quantity <= 0:
            raise ValueError("quantity must be greater than 0")
        self.quantity = quantity

    def get_type(self):
        """Get the demand type."""
        return self.type

    def get_name(self):
        """Get the name of the demand."""
        return self.name

    def get_brand(self):
        """Get the brand of the demand."""
        return self.brand

    def get_price_limit(self):
        """Get the price limit of the demand."""
        return self.price_limit

    def get_store(self):
        """Get the store of the demand."""
        return self.store

    def get_nutri_scores(self):
        """Get the nutritional scores of the demand."""
        return self.nutri_scores

    def get_quantity(self):
        """Get the quantity of the demand."""
        return self.quantity

    def price_per_unit(self):
        """Calculate the price per unit."""
        return self.price_limit / self.quantity
