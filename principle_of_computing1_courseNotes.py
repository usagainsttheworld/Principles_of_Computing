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

#########Quiz 4#########
"""
Q3.
Probability for sequences of trials.
Consider a sequence of trials in which a fair four-sided die (with faces 
numbered 1-4) is rolled twice. What is the expected value of the product 
of the two die rolls? Enter the answer as a floating point number below.
"""
def gen_all_sequences(outcomes, length):
    """
    Functions to enumerate sequences of outcomes
    Repetition of outcomes is allowed;
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """   
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

def get_expected_value(outcomes, length):
    """
    to get expected value for a die roll in a sequence trail
    """
    seq_outcomes = gen_all_sequences(outcomes, length)
    #print "Computed", len(seq_outcomes), "sequences of", str(length), "outcomes"
    #print "Sequences were", seq_outcomes
    sum = 0
    for dummy_idx in seq_outcomes:
        sum = sum + dummy_idx[0] + dummy_idx[1]
    expected_value = sum/len(seq_outcomes)
    return expected_value

print get_expected_value(set([1,2,3,4]), 2)

#Q4
"""
Given a trial in which a decimal digit is selected from the list ["0", "1", "2", "3",
"4", "5", "6", "7", "8", "9"] with equal probability 0.1, consider a five-digit 
string created by a sequence of such trials (leading zeros and repeated digits 
are allowed). What is the probability that this five-digit string consists of 
five consecutive digits in either ascending or descending order (e.g; "34567" or "43210")?
"""
def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """   
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

def get_asc_des_possibility(outcomes, length):
    """
    to get probability that the length from the outcomes is in either 
    ascending or descending order
    """
    seq_outcomes = gen_all_sequences(outcomes, length)
    #print "Computed", len(seq_outcomes), "sequences of", str(length), "outcomes"
    #print "Sequences were", seq_outcomes
    asc_list = []
    for dummy_seq in seq_outcomes:
        if dummy_seq[0] + len(dummy_seq)-1 == dummy_seq[len(dummy_seq)-1]:
            asc_found = True
            for dummy_index in range(len(dummy_seq)-1):
                if dummy_seq[dummy_index] + 1 != dummy_seq[dummy_index + 1]:
                    asc_found = False
                    break
            if asc_found:
                asc_list.append(dummy_seq)
    asc_des_count = len(asc_list)*2
    possibility = float(asc_des_count)/float(len(seq_outcomes))
    return possibility

#print get_asc_des_possibility(set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]), 5)
print get_asc_des_possibility(set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)

#Q5
"""
Permutations
Consider a trial in which five digit strings are formed as permutations of the 
digits ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]. (In this case, 
repetition of digits is not allowed.) If the probability of each permutation 
is the same, what is the probability that this five digits string consists of 
consecutive digits in either ascending or descending order (e.g; "34567" or "43210")?
"""
def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                if item not in seq:
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans

def get_asc_des_possibility(outcomes, length):
    """
    to get probability that the length from the outcomes is in either 
    ascending or descending order
    """
    permutaion_outcomes = gen_permutations(outcomes, length)
    asc_list = []
    for dummy_seq in permutaion_outcomes:
        if dummy_seq[0] + len(dummy_seq)-1 == dummy_seq[len(dummy_seq)-1]:
            asc_found = True
            for dummy_index in range(len(dummy_seq)-1):
                if dummy_seq[dummy_index] + 1 != dummy_seq[dummy_index + 1]:
                    asc_found = False
                    break
            if asc_found:
                asc_list.append(dummy_seq)
    asc_des_count = len(asc_list)*2
    possibility = float(asc_des_count)/float(len(permutaion_outcomes))
    return possibility

#print get_asc_des_possibility(set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]), 5)
print get_asc_des_possibility(set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)



#Q6
"""
In this week's lectures, we discussed an iterative approach to generating all 
sequences of outcomes where repeated outcomes were allowed. Starting from this 
program template, implement a function gen_permutations(outcomes, num_trials) 
that takes a list of outcomes and a number of trials and returns a list of all 
possible permutations of length num_trials from this set of outcomes.
"""

def gen_permutations(outcomes, length):
    """
    Function to generate permutations of outcomes
    Repetition of outcomes not allowed.
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                if item not in seq:
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans

## Final example for homework problem
outcome = set(["a", "b", "c", "d", "e", "f"])
permutations = gen_permutations(outcome, 4)
permutation_list = list(permutations)
permutation_list.sort()
print
print "Answer is", permutation_list[100]

#Q9
"""
Given a standard 52 card deck of playing cards, what is the probability of being 
dealt a five card hand where all five cards are of the same suit?
"""
#################
#Part2####
#Quiz1#
#Q9 implement a Stack class. Once your implementation is complete, 
#uncomment the test code at the end of the template and enter the number printed out by this template.
"""
Queue class
"""

class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """ 
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)
    
    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        """
        Add item to the queue.
        """        
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []
        
"""
Stack class
"""
class Stack:
    """
    A simple implementation of a FILO stack.
    """

    def __init__(self):
        """ 
        Initialize the stack.
        """
        self._items=[]

    def __len__(self):
        """
        Return number of items in the stack.
        """
        return len(self._items)

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        return str(self._items)

    def push(self, item):
        """
        Push item onto the stack.
        """        
        self._items.append(item)

    def pop(self):
        """
        Pop an item off of the stack
        """
        return self._items.pop()

    def clear(self):
        """
        Remove all items from the stack.
        """
        self._items=[]

############################
# test code for the stack

my_stack = Stack()
my_stack.push(72)
my_stack.push(59)
my_stack.push(33)
my_stack.pop()
my_stack.push(77)
my_stack.push(13)
my_stack.push(22)
my_stack.push(45)
my_stack.pop()
my_stack.pop()
my_stack.push(22)
my_stack.push(72)
my_stack.pop()
my_stack.push(90)
my_stack.push(67)
while len(my_stack) > 4:
   my_stack.pop()
my_stack.push(32)
my_stack.push(14)
my_stack.pop()
my_stack.push(65)
my_stack.push(87)
my_stack.pop()
my_stack.pop()
my_stack.push(34)
my_stack.push(38)
my_stack.push(29)
my_stack.push(87)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print my_stack.pop()

#Recursion
def is_palindrome(word):
	if len(word)<2:
		return True
	else:
		if word[0]!=word[-1]:
			return False
		else:
			return is_palindrome(word[1:-1])
#Quiz 2
#Q4
counter = 0
def fib(num):
    global counter
    counter += 1
    print counter
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
fib(3)

#Q5
counter = 0
def memoized_fib(num, memo_dict):
    global counter
    counter += 1
    print counter
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2
memoized_fib(6,{0:0,1:1})




