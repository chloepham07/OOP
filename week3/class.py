# Dog class
class Dog:
    """Represents a dog with physical attributes and behaviors."""
    
    def __init__(self, name: str, color: str, breed: str, emotion: str):
        self.name = name
        self.color = color
        self.breed = breed
        self.emotion = emotion
    
    def __str__(self) -> str:
        return f"Name: {self.name.title()}| Color: {self.color}| Breed: {self.breed}| Mood: {self.emotion}"
    
    def bark(self) -> str:
        self.emotion = "angry"
        return f"Woof woof! {self.name.title()} is barking at you!"
    
    def wag_tail(self) -> str:
        self.emotion = "happy"
        return f"{self.name.title()} is wagging its tail. So cute <3"
    
    def eat(self) -> str:
        self.emotion = "satisfied"
        return f"{self.name.title()} is eating and looks satisfied."
    
    def run(self) -> str:
        self.emotion = "excited"
        return f"{self.name.title()} is running around excitedly!"


#  Car class
class Car:
    """Represents a car with basic behaviors."""
    
    def __init__(self, brand: str, size: str, color: str, price: str):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.is_moving = False

    def __str__(self):
        return f"{self.brand}| Color: {self.color}| Size: {self.size}| Price: {self.price}"
    
    def speed_up(self):
        self.is_moving = True
        return f"{self.brand} is speeding up"
    
    def slow_down(self):
        self.is_moving = False
        return f"{self.brand} is slowing down"
    
    def collide(self):
        self.is_moving = False
        return f"{self.brand} has crashed!"


# Bank Account class
class BankAccount:
    """Represents a bank account with basic operations."""
    
    def __init__(self, account_number, owner_name, bank, balance: float):
        self.account_number = account_number
        self.owner_name = owner_name
        self.bank = bank
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}. New balance: {self.__balance}"
        return "Error: amount must be greater than zero"
    
    def withdraw(self, amount: float):
        if amount <= 0:
            return "Error: amount must be greater than zero"
        if amount > self.__balance:
            return "Error: do not have enough money"
        
        self.__balance -= amount
        return f"Withdrew: {amount}. Remaining balance: {self.__balance}"
        
    def __str__(self):
        return (f"{self.owner_name} | Account: {self.account_number} | "
                f"Bank: {self.bank} | Balance: {self.__balance}")



dog1 = Dog('lucy', 'yellow', 'bull terrier', 'happy')
print("--- Dog Info ---")
print(dog1)
print("--- Interacting with the Dog ---")
print(dog1.eat())
print(dog1.wag_tail())
print(dog1.run())
print(dog1.bark())

print("\n")

# Car
car = Car('Ferrari', 'coupe', 'red', '$600,000')
print("--- Car Info ---")
print(car)
print(car.speed_up())
print(car.slow_down())
print(car.collide())

print("\n")

# Bank Account
my_account = BankAccount('123456', 'Duyen', 'MB Bank', 200000)
print("--- Bank Account ---")
print(my_account)
print(my_account.deposit(300000))
print(my_account.withdraw(100000))
print("Current balance:", my_account.get_balance())
