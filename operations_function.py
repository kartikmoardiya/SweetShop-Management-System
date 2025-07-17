from sweet import Sweet

class SweetOperator:
    
    def __init__(self):
        self.sweets = []
        
    # Function to check if ID exists in the sweets list
    def id_exists(self, id):
        for sweet in self.sweets:
            if sweet.id == id:
                return True
        return False
    
    # Function to check if category is valid    
    def category_exists(self, category):
        valid_categories = ["chocolate", "candy", "pastry"]
        return category.strip().lower() in valid_categories
    
    def add_sweet(self, id = None, name = "", category= "", price = 0, quantity = -1):
        if id is None or self.id_exists(id) or id < 0:
            return "Invalid ID"
        
        if len(name) <= 0:
            return "Invalid Name"
        
        if not self.category_exists(category) or len(category) <= 0:
            return "Invalid Category"
        
        if price <= 0:
            return "Invalid Price"
        
        if quantity < 0:
            return "Invalid Quantity"
        
        sweet = Sweet(id, name, category, price, quantity)
        self.sweets.append(sweet)
        
        return "Sweet Added Successfully"
    
    # Function to get all sweets
    def get_sweets(self):
        return self.sweets
    
    # Delete function to remove a sweet by ID
    # If ID does not exist, return "Invalid ID"
    def delete_sweets(self, id = -1):
        if not self.id_exists(id):
            return "Invalid ID"
        self.sweets = [sweet for sweet in self.sweets if sweet.id != id]
        
        return "Sweet Deleted Successfully"

    def view_sweets(self):
        return list(self.sweets)
    
    def sweet_search(self, sort = "name"):
        sort = sort.strip().lower()
        if sort not in ["id","name", "category", "price", "quantity"]:
            return "Invalid Sort Parameter"
        sorted_sweets = sorted(self.sweets, key=lambda x: getattr(x, sort))
        return sorted_sweets
    
    def sweet_purchase(self, name, quantity_to_purchase = 1):
        # Check if sweets list is empty
        if not self.sweets or len(self.sweets) == 0:
            return "No Sweets Available"
        
        # Validate quantity to purchase
        if quantity_to_purchase <= 0:
            return "Invalid Purchase Quantity"
        
        # Find the sweet by name
        sweet_found = None
        for sweet in self.sweets:
            if sweet.name.lower() == name.lower():
                sweet_found = sweet
                break
        
        # If sweet not found
        if sweet_found is None:
            return "Sweet Not Found"
        
        # Check if enough stock is available
        if sweet_found.quantity < quantity_to_purchase:
            return "Insufficient Stock"
        
        # Decrease the quantity
        sweet_found.quantity -= quantity_to_purchase
        
        return f"Purchase Successful. {quantity_to_purchase} {name}(s) purchased. Remaining stock: {sweet_found.quantity}"
    
    def restock_sweets(self, name, quantity_to_restock):
        # Check if sweets list is empty
        if not self.sweets or len(self.sweets) == 0:
            return "No Sweets Available"
        
        # Validate restock quantity
        if quantity_to_restock <= 0:
            return "Invalid Restock Quantity"
        
        # Find the sweet by name
        sweet_found = None
        for sweet in self.sweets:
            if sweet.name.lower() == name.lower():
                sweet_found = sweet
                break
        
        # If sweet not found
        if sweet_found is None:
            return "Sweet Not Found"
        
        # Increase the quantity
        sweet_found.quantity += quantity_to_restock
        
        return f"Restock Successful. {quantity_to_restock} {name}(s) restocked. Current stock: {sweet_found.quantity}"