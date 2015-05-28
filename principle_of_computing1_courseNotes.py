#######Quiz One######
#Q5 Which of the following expressions returns the last character in the non-empty string my_string?

mystring = 'abc'
print mystring[len(mystring)-1]

#Q7 Consider the following snippet of Python code. What is the value of val2[1] after executing this code?
val1 = [1, 2, 3]
val2 = val1[1:]
val1[2]  = 4
print val2[1]

#Q9 Write a function in Python that takes a list as input and repeatedly appends the sum of 
#the last three elements of the list to the end of the list. Your function should loop for 25 times.
def appendsums(lst):
	"""
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
	for i in range(25):
		lst.append(sum(lst[(len(lst)-3):(len(lst))]))
	return lst
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[10]
print sum_three [20]
#!!!list[1:3] takes elements 1 and 2

#Q10 The deposit and withdraw methods each change the account balance. The withdraw method also 
#deducts a fee of 5 dollars from the balance if the withdrawal (before any fees) results in a 
#negative balance. Since we also have the method get_fees, you will need to have a variable to 
#keep track of the fees paid.
class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fee = 0
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance = self.balance + amount
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance = self.balance - amount
        if self.balance < 0:
        	self.balance = self.balance -5
        	self.fee = self.fee +5
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee







