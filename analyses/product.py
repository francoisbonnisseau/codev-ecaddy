class Product:
    last_id = 0  # Class variable to track the last assigned ID
    def __init__(self, name, brand, price, description, url, image_url, store, nature):
            # Validate input values
            if not isinstance(name, str) or not isinstance(brand, str) or not isinstance(description, str) or not isinstance(url, str) or not isinstance(image_url, str) or not isinstance(store, str) or not isinstance(nature, str):
                raise ValueError("Invalid input type for string attributes")
            if not isinstance(price, (int, float)) or price < 0:
                raise ValueError("Price must be a non-negative number")
            
            # Increment the last ID when a new instance is created
            Product.last_id += 1
            # Assign the incremented ID to the current instance
            self.id = Product.last_id
            self.name = name
            self.brand = brand
            self.price = price
            self.description = description
            self.url = url
            self.image_url = image_url
            self.store = store
            self.nature=nature
    def get_id(self):
        """Method to get the ID of the product."""
        return self.id

    def get_name(self):
        """Method to get the name of the product."""
        return self.name

    def get_brand(self):
        """Method to get the brand of the product."""
        return self.brand

    def get_price(self):
        """Method to get the price of the product."""
        return self.price

    def get_description(self):
        """Method to get the description of the product."""
        return self.description

    def get_url(self):
        """Method to get the URL of the product."""
        return self.url

    def get_image_url(self):
        """Method to get the image URL of the product."""
        return self.image_url

    def get_store(self):
        """Method to get the store of the product."""
        return self.store
    def get_nature(self):
        return self.nature

# Creating a product
product1 = Product(name="Laptop", brand="Lenovo", price=899.99, description="Powerful laptop with Intel Core i7 processor.", url="http://example.com/product1", image_url="http://example.com/image1.jpg", store="Store A", nature="eletroménager")

# Using the methods to get the product attributes
print(product1.get_id())
print(product1.get_name())
print(product1.get_brand())
print(product1.get_price())
print(product1.get_description())
print(product1.get_url())
print(product1.get_image_url())
print(product1.get_store())
print(product1.get_nature())
