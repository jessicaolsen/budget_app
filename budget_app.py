class Category():

    def __init__(self, category_name) : 
        self.category_name = category_name
    
    
    ledger = list()

    #Defining Deposit
    def deposit(self, amount, description) : 
        if bool(description) == False : 
            description = ''
        self.amount = amount
        self.description = description
        

    ledger.append(amount)

def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(1000, "initial deposit")