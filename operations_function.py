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
            