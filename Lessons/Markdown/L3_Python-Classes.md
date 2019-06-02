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
		
	
	
Essentially, what we're trying to do here is reframe the program around the account holders. This makes sense to us because in the real world we consider each thing we experience as an object. 
