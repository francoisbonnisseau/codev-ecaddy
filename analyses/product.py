class Product:
    last_id = 0  # Class variable to track the last assigned ID
    def __init__(self, name, brand, price, description, url, image_url, store, nature=''):
            """
        Initializes a Product object.

        Args:
            name (str): The name of the product.
            brand (str): The brand of the product.
            price (float): The price of the product.
            description (str): The description of the product.
            url (str): The URL of the product.
            image_url (str): The image URL of the product.
            store (str): The store of the product.
            nature (str, optional): The nature of the product. Defaults to ''.

        Raises:
            ValueError: If any input type is invalid or if price is negative.
        """
            # Validate input values
            if not isinstance(name, str) or not isinstance(brand, str) or not isinstance(description, str) or not isinstance(url, str) or not isinstance(image_url, str) or not isinstance(store, str) or not isinstance(nature, str) :
                raise ValueError("Invalid input type for string attributes")
            if not isinstance(price, (int, float)):
                print("this is the price ",price)
                raise ValueError("Price must be an integer or float")
            if price < 0:
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
if __name__ == "__main__":
# Test case 1: Valid input
    try:
        product1 = Product(name="Laptop", brand="Lenovo", price=899.99, description="Powerful laptop with Intel Core i7 processor.", 
                           url="http://example.com/product1", image_url="http://example.com/image1.jpg", store="Store A", nature="Electronics")
        assert product1.get_name() == "Laptop"
        assert product1.get_brand() == "Lenovo"
        assert product1.get_price() == 899.99
        assert product1.get_description() == "Powerful laptop with Intel Core i7 processor."
        assert product1.get_url() == "http://example.com/product1"
        assert product1.get_image_url() == "http://example.com/image1.jpg"
        assert product1.get_store() == "Store A"
        assert product1.get_nature() == "Electronics"
        print("Test case 1 passed: Valid input")
    except AssertionError:
        print("Test case 1 failed: Valid input")

    # Test case 2: Invalid input - name should be a string
    try:
        Product(name=123, brand="Lenovo", price=899.99, description="Powerful laptop with Intel Core i7 processor.",
                 url="http://example.com/product1", image_url="http://example.com/image1.jpg", store="Store A", nature="Electronics")
        print("Test case 2 failed: Invalid input - name should be a string")
    except ValueError:
        print("Test case 2 passed: Invalid input - name should be a string")

    # Test case 3: Invalid input - brand should be a string
    try:
        Product(name="Laptop", brand=123, price=899.99, description="Powerful laptop with Intel Core i7 processor.", url="http://example.com/product1", image_url="http://example.com/image1.jpg", store="Store A", nature="Electronics")
        print("Test case 3 failed: Invalid input - brand should be a string")
    except ValueError:
        print("Test case 3 passed: Invalid input - brand should be a string")

    # Test case 4: Invalid input - price should be a positive number
    try:
        Product(name="Laptop", brand="Lenovo", price="invalid", description="Powerful laptop with Intel Core i7 processor.", url="http://example.com/product1", image_url="http://example.com/image1.jpg", store="Store A", nature="Electronics")
        print("Test case 4 failed: Invalid input - price should be a number")
    except ValueError:
        print("Test case 4 passed: Invalid input - price should be a number")
    try:
        Product(name="Laptop", brand="Lenovo", price=-899.99, description="Powerful laptop with Intel Core i7 processor.", url="http://example.com/product1", image_url="http://example.com/image1.jpg", store="Store A", nature="Electronics")
        print("Test case 4 failed: Invalid input - price should be a positive number")
    except ValueError:
        print("Test case 4 passed: Invalid input - price should be a positive number")
    # Test case 5: Invalid input - description should be a string
    try:
        Product(name="Laptop", brand="Lenovo", price=899.99, description=123, url="http://example.com/product1", image_url="http://example.com/image1.jpg", store="Store A", nature="Electronics")
        print("Test case 5 failed: Invalid input - description should be a string")
    except ValueError:
        print("Test case 5 passed: Invalid input - description should be a string")

    # Test case 6: Invalid input - url should be a string
    try:
        Product(name="Laptop", brand="Lenovo", price=899.99, description="Powerful laptop with Intel Core i7 processor.", url=123, image_url="http://example.com/image1.jpg", store="Store A", nature="Electronics")
        print("Test case 6 failed: Invalid input - url should be a string")
    except ValueError:
        print("Test case 6 passed: Invalid input - url should be a string")

    # Test case 7: Invalid input - image_url should be a string
    try:
        Product(name="Laptop", brand="Lenovo", price=899.99, description="Powerful laptop with Intel Core i7 processor.", url="http://example.com/product1", image_url=123, store="Store A", nature="Electronics")
        print("Test case 7 failed: Invalid input - image_url should be a string")
    except ValueError:
        print("Test case 7 passed: Invalid input - image_url should be a string")

    # Test case 8: Invalid input - store should be a string
    try:
        Product(name="Laptop", brand="Lenovo", price=899.99, description="Powerful laptop with Intel Core i7 processor.", url="http://example.com/product1", image_url="http://example.com/image1.jpg", store=123, nature="Electronics")
        print("Test case 8 failed: Invalid input - store should be a string")
    except ValueError:
        print("Test case 8 passed: Invalid input - store should be a string")

    # Test case 9: Invalid input - nature should be a string
    try:
        Product(name="Laptop", brand="Lenovo", price=899.99, description="Powerful laptop with Intel Core i7 processor.", url="http://example.com/product1", image_url="http://example.com/image1.jpg", store="Store A", nature=123)
        print("Test case 9 failed: Invalid input - nature should be a string")
    except ValueError:
        print("Test case 9 passed: Invalid input - nature should be a string")
    # Test case 10: Valid id - ID generation and increment
    try:
        products = []
        for i in range(5):
            products.append(Product(name=f"Product {i+1}", brand=f"Brand {i+1}", price=100 + i * 10, description=f"Description {i+1}", url=f"http://example.com/product{i+1}", image_url=f"http://example.com/image{i+1}.jpg", store=f"Store {i+1}", nature=f"Nature {i+1}"))
        
        for i in range(1, len(products)):
            assert products[i].get_id() == products[i-1].get_id() + 1  # IDs should increment by 1
        
        print("Test case 10 passed: ID generation and increment")
    except AssertionError:
        print("Test case 10 failed: ID generation and increment")