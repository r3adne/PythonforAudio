# Object-Oriented Programming in Python
#### Zachary Lewis-Towbes; BerkleeMakes; May 2019


### Goals

* Understand why Object-Oriented programming is useful.
* Implement classes in Python


### OOP, an Introduction

**Object-Oriented Programming** is a complicated-sounding term for a very simple idea: Programming that represents the way we look at the world. To flesh out the need for Object-Oriented Programming, let's look at a program that keeps track of a user's bank account balance:

	# the first character of each variable is the identity of the user. 

	a_balance = 1000
	a_inDebt = False
	a_memos = ["this is the first memo"]
	
	def a_withdraw(amount, memo):
		a_balance -= amount
		
		if a_balance < 0:
			print('a in debt')
			a_inDebt = True
		else:
			a_inDebt = False
			
		a_memos.append(memo)
		print('withdrew from a')
	
	def a_deposit(amount, memo):
		a_balance += amount
		print('a added to their balance')
		

Now, let's add another client to our accounts list:

	# the first character of each variable is the identity of the user. 

	a_balance = 1000
	a_inDebt = False
	a_memos = ["this is the first memo"]
	
	b_balance = 1000
	b_inDebt = False
	b_memos = ["this is the first memo"]
	
	
	def a_withdraw(amount, memo):
		a_balance -= amount
		
		if a_balance < 0:
			print('a in debt')
			a_inDebt = True
		else:
			a_inDebt = False
			
		a_memos.append(memo)
		print('withdrew from a')
	
	def a_deposit(amount, memo):
		a_balance += amount
		print('a added to their balance')
		
	def b_withdraw(amount, memo):
		b_balance -= amount
		
		if b_balance < 0:
			print('b in debt')
			b_inDebt = True
		else:
			b_inDebt = False
			
		b_memos.append(memo)
		print('withdrew from b')
	
	def b_deposit(amount, memo):
		b_balance += amount
		print('b added to their balance')
	
We can see that continuing to add clients would prove difficult. Now, in reality, we wouldn't actually write a program like this. A more refined example might be: 

	accountNumbers = [] # a list of all active account numbers
	balances = {} # account number : balance
	inDebt = {} # account number : Debt Status (Boolean)
	
	def withdraw(accountNumber, amount):
		# withdraws amount from accountNumber
		balances[accountNumber] -= amount
		
		if balances[accountNumber] < 0: # is accountNumber in debt? 
			print('%d in debt'%(accountNumber))
			inDebt[accountNumber] = True
	
	def deposit(accountNumber, amount):
		# deposits amount into accountNumber
		balances[accountNumber] += amount
		
		if balances[accountNumber] >= 0:
			inDebt[accountNumber] = False
			
	
	def addAccount(accountNumber, initialAmount):
		accountNumbers.append(accountNumber)
		balances[accountNumber] = initialAmount
		inDebt[accountNumber] = False
		
	
	
Essentially, what we're trying to do here is reframe the program around the account holders. This makes sense to us because in the real world we consider each thing we experience as an object. In this case, each account could be a virtual "object" which has certain properties -- **attributes**. It also has certain functions that are only needed within the context of the object itself -- **methods**.

In Python, defining classes is much like defining functions. Let's look at a hypothetical program which serves the same functionality as above using classes:

	class Account:
	    def __init__(self, accountNumber, initialAmount):
	        self.accountNumber = accountNumber
	        self.balance = initialAmount 
	        self.inDebt = False
	    
	    def debtupdate(self):
	        """ Updates debt status """
	        if self.balance < 0:
	            self.inDebt = True
	        else:
	            self.inDebt = False
	
	    def withdraw(self, amount):
	        """ withdraws amount from account """
	        self.balance -= amount
	        self.debtupdate()
	    
	    def deposit(self, amount):
	        """ deposits amount into account """
	        self.balance += amount
	        self.debtupdate()
 
	
Now we can make accounts like this:

	DwightsAccount = Account(12345, 100) # makes a new account with number 12345 and balance $100.
	
	print("Dwight has ${} in his account".format(DwightsAccount.balance))
	print("Dwight's debt status is {}".format(DwightsAccount.inDebt))
	
	DwightsAccount.deposit(100)
	
	print("We have added $100 to Dwight's account. His balance is now ${}".format(DwightsAccount.balance))
	
	DwightsAccount.withdraw(1000)
	
	print("Dwight spent $1000 on renewing his crane operating license. His balance is now ${}".format(DwightsAccount.balance))
	print("Dwight's debt status is now {}".format(DwightsAccount.inDebt))
	
Let's try to run `L3-0.py` in the `PythonFiles` directory.
	

### \_\_init__()

The \_\_init__() method **initializes** the class. It must have a few characteristics:

* Its first argument should be `self`. When in a class, we refer to the class itself as `self`.

* It must be titled exactly `__init__()`, with exactly two underscores on each side. We'll discuss why later.

* It can take any number of additional arguments that are used to initialize the class. See the example above. 


### Methods and Attributes

\_\_init__() is a special kind of function called a **method**. Methods are functions belonging to the class. They must take the instance of the class itself as the first argument, using `self`. 

**attributes** are variables that belong to the class. In the above example, `Account.accoutnNumber`, `Account.balance`, and `Account.inDebt` are each attributes. 

To use methods and access attributes, we use the `.` operator.

### The Membership Operator

One thing to keep in mind regarding classes is that each instance of a class may have different attribute values. For instance, if we continued our previous class `Account` below:

	a = Account(14023, 100)
	b = Account(41202, 200)

We notice that accounts `a` and `b` have different balances. `a` should have $100 in it and `b` should have $200. 

So, to access the balance of each, we must use the membership operator. 

This operator asks for an object's attribute or method. So in this case, to get `a`'s balance, we would use:

	a.balance

and to get `b`'s balance we would use:
	
	b.balance
	
The `.` being used here is the membership operator. It is used as such:

	n.m

where `n` is an object (user-defined class or built-in object) and `m` is an attribute of that object; or:


	n.m()
	
where `n` is an object and `m()` is a method of that object.

In short, when you're trying to access the methods or attributes of a class, use `.`.


### Why should we learn this?

Classes might seem very complicated, and they are. You won't need to use them all too often in your own work unless you plan on working on large-scale projects. 

We must learn about them in order to use other, open-source Python libraries that are made entirely of classes. 

