from abc import ABC, abstractmethod

# Abstract Product (Generic Pizza)
class Pizza(ABC):
    
    @abstractmethod
    def prepare(self):
        """Prepare the pizza"""
        pass
    
    @abstractmethod
    def get_name(self):
        """Get the name of the pizza"""
        pass

# Abstract Creator (Generic Pizza Creator)
class PizzaCreator(ABC):
    
    def order_pizza(self):
        pizza = self.create_pizza()
        
        if pizza:
            print(pizza.prepare())
            print(f"{pizza.get_name()} coming right up!\n")
            return pizza
        else:
            print("Unable to create pizza.\n")
            return None
    
    @abstractmethod
    # Factory Method
    def create_pizza(self):
        """Create a specific type of pizza"""
        pass

# Concrete Creators (Different Pizza Types)
class CheesePizzaCreator(PizzaCreator):
    
    def create_pizza(self):
        return CheesePizza()

class PepperoniPizzaCreator(PizzaCreator):
    
    def create_pizza(self):
        return PepperoniPizza()

class SupremePizzaCreator(PizzaCreator):
    
    def create_pizza(self):
        return SupremePizza()

# Concrete Products
class CheesePizza(Pizza):
    
    def prepare(self):
        return "Preparing Cheese Pizza with mozzarella and tomato sauce..."
    
    def get_name(self):
        return "Cheese Pizza"

class PepperoniPizza(Pizza):
    
    def prepare(self):
        return "Preparing Pepperoni Pizza with pepperoni, mozzarella, and tomato sauce..."
    
    def get_name(self):
        return "Pepperoni Pizza"

class SupremePizza(Pizza):
    
    def prepare(self):
        return "Preparing Supreme Pizza with pepperoni, sausage, peppers, onions, and olives..."
    
    def get_name(self):
        return "Supreme Pizza"

# Client Code
def main():
    print("Welcome to Mansoor's Pizzeria!\n")
    
    # Map user choices to concrete creators
    pizza_creators = {
        "1": CheesePizzaCreator(),
        "2": PepperoniPizzaCreator(),
        "3": SupremePizzaCreator()
    }
    
    user_input = ""
    while user_input != "Exit":
        print("Please order from the options below.\n")
        print("1. Cheese Pizza\n")
        print("2. Pepperoni Pizza\n")
        print("3. Supreme Pizza\n")
        print("Type 'Exit' to leave.\n")
        
        user_input = input("Enter the order number: ")
        
        if user_input == "Exit":
            print("Goodbye! Thanks for visiting Mansoor's Pizzeria.\n")
        elif user_input in pizza_creators:
            pizza_creators[user_input].order_pizza()
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()