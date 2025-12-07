from abc import ABC, abstractmethod

# Abstract Product class for all pizzas
class Pizza(ABC):
    
    @abstractmethod
    def prepare(self):
        """Prepare the pizza"""
        pass
    
    @abstractmethod
    def get_name(self):
        """Get the name of the pizza"""
        pass

# Concrete Products
class CheesePizza(Pizza):
    """Concrete product: Cheese Pizza"""
    
    def prepare(self):
        return "Preparing Cheese Pizza with mozzarella and tomato sauce..."
    
    def get_name(self):
        return "Cheese Pizza"

class PepperoniPizza(Pizza):
    """Concrete product: Pepperoni Pizza"""
    
    def prepare(self):
        return "Preparing Pepperoni Pizza with pepperoni, mozzarella, and tomato sauce..."
    
    def get_name(self):
        return "Pepperoni Pizza"

class SupremePizza(Pizza):
    """Concrete product: Supreme Pizza"""
    
    def prepare(self):
        return "Preparing Supreme Pizza with pepperoni, sausage, peppers, onions, and olives..."
    
    def get_name(self):
        return "Supreme Pizza"

# Creator (Abstract)
class Pizzeria(ABC):
    """Abstract creator class for pizzeria"""
    
    def order_pizza(self, pizza_type):
        """Template method for ordering pizza"""
        pizza = self.create_pizza(pizza_type)
        
        if pizza:
            print(pizza.prepare())
            print(f"{pizza.get_name()} coming right up!\n")
            return pizza
        else:
            print("Invalid option, please try again.\n")
            return None
    
    @abstractmethod
    def create_pizza(self, pizza_type):
        """Factory method to be implemented by concrete creators"""
        pass

# Concrete Creator
class MansoorsPizzeria(Pizzeria):
    """Concrete creator: Mansoor's Pizzeria implementation"""
    
    def create_pizza(self, pizza_type):
        """Factory method implementation"""
        if pizza_type == "1":
            return CheesePizza()
        elif pizza_type == "2":
            return PepperoniPizza()
        elif pizza_type == "3":
            return SupremePizza()
        else:
            return None

# Client Code
def main():
    pizzeria = MansoorsPizzeria()
    print("Welcome to Mansoor's Pizzeria!\n")
    
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
        else:
            pizzeria.order_pizza(user_input)

if __name__ == "__main__":
    main()