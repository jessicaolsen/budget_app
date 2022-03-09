class Category():

    def __init__(self, category_name) : 
        self.category_name = category_name
        self.ledger = []
        self.balance = 0.0
    
    #formating Output
    def __repr__(self):
        header_length= len(self.category_name)
        if header_length &2 == 0: 
            number_stars1 = number_stars2 = int((30 - header_length) / 2)
        else : 
            number_stars1 = int((30 - header_length) / 2) + 1
            number_stars2 = int((30 - header_length) / 2) 
        header = "*" * number_stars1 + self.category_name + "*" * number_stars2
        ledger = ""
        for item in self.ledger : 
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:7.2f}".format(item["amount"])
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.balance)
        return header + "\n" + ledger + total

    #Defining Check Funds
    def check_funds(self, amount) : 
        if amount > self.balance : 
            return False
        else : 
            return True

    #Defining Deposit
    def deposit(self, amount, description = False) : 
        if description == False : 
            description = ""
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
    
    #Defining Withdraw
    def withdraw(self, amount, description = "") :
        if description == False : 
            description = ""
        if bool(self.check_funds(amount)) == False : 
            return False
        else : 
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
    
    #Defining Get Balance
    def get_balance(self) :
        return self.balance
    
    #Defining Transfer
    def transfer(self, amount, category_other): 
         if bool(self.check_funds(amount)) == False : 
            return False
         else: 
            self.withdraw(amount, "Transfer to {}".format(category_other.category_name))
            category_other.deposit(amount,"Transfer from {}".format(self.category_name))
            return True 
    
#
def create_spend_chart(categories):
    pass



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)