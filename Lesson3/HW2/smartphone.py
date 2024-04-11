class Smartphone:
    def __init__(self, model, brand, phone):
        self.model = model
        self.brand = brand
        self. phone = phone
    
    def say_phone(self):
        print(f"{self.model}, {self.brand}, {self.phone}")