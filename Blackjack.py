'''
*************************************************************************************************************
* 											Created By Aminu Bishir                                         *	
*     											1st Oct. 2018                                               *
* This simple game was created with OOP at heart, and hence can serve as a learning tool for Python newbies *
* It aslo uses some other features such as Exception handling, random, list manipulation etc.               *
*************************************************************************************************************
'''

import random
class Blackjack(object):
		
		p = []
		d = []
		cards = [2,3,4,5,6,7,8,9,'A','J','K','Q']
		balance = 100
		h1 = [random.sample(cards,2)]
		for x in h1:
			p.append(x)
		h2 = [random.sample(cards,2)]
		for y in h2:
			d.append(y)
		
		def __init__(self):
				self.cards = [2,3,4,5,6,7,8,9,'A','J','K','Q']
				self.balance = 100
				
					
				'''self.p.append([random.choice(self.cards)])'''
				'''self.d = [random.sample(self.cards,2)]'''
				'''self.d.append([random.choice(self.cards)])'''
				self.bet = 0
				self.doubleMark = 0
		

		def play(self):
				
				print 'Welcome to the BackJack Game! \n Your starting balance is: N',self.getBalance()
				while(self.getBalance() >0):
					
					repeat = True
					while(repeat):
						print 'These are the cards at your hand: ',self.p[0]
						print "Open card at the dealer's hand: ",self.d[0][0]
						print 'Balance: ',self.getBalance()
						try:
							bet_amount = int(raw_input('Enter the bet amount: '))
							repeat = False
							if(bet_amount > self.getBalance()):
									print 'Bet amount exceeds your current balance!'
									repeat = False
							else:
								self.setBet(bet_amount)
								self.setBalance((-bet_amount))
						except:
							print 'Invalid input'
					
					while(True):
						input = raw_input('Press H, to hit, S, to stand, D to Double-Down: ')
						if(input =='H' or input =='h'):

							self.p[0].append(self.hit())
							self.d[0].append(self.hit())
							self.alert()
							break
						elif(input =='S' or input == 's'):
							print self.p[0]
							self.d[0].append(self.hit())
							self.alert()
							break
						elif(input == 'd' or input == 'D'):
							print self.p[0]
							self.doubleMark = self.doubleDown(self.p)
							self.d[0].append(self.hit())
							self.alert()
							break
						else:
							print 'Invalid Choice!'
						continue	
					if(self.getBalance() > 0):
						cont = raw_input('Press Y to continue or Any key to stop')
						
						if(cont.upper() =='Y'):
							self.player()
							self.dealer()
							continue
						else:
							break
					else:
						print 'You run out of Money!'
						cont = raw_input('Press Y to restart or Any key to stop')
						
						if(cont.upper() =='Y'):
							self.resetBalance()
							
							break
							self.start()
						else:
							break
				
						
							
		def alert(self):
				mark = 0
				if(self.doubleMark == 0):
					player = self.mark(self.p)
					dealer = self.mark(self.d)
					if((player > dealer) and (player <= 21)):
						print 'You Won! \nYou got N', 2*(self.getBet())
						self.setBalance(2*(self.getBet()))
						print 'Your new balance: N', self.getBalance()
					elif((player < dealer) and (dealer <= 21)):
						print 'You Lost! \nYou got nothing'
						
						print 'Your new balance: N', self.getBalance()
					elif(player == dealer):
						print 'Push! \nYou got your N',self.getBet(),'back'
						self.setBalance(self.getBet())
						print 'Your new balance: N', self.getBalance()
				else:
				
					dealer = self.mark(self.d)
					if((self.doubleMark > dealer) and (self.doubleMark <= 21)):
						print 'You Won! \n you got N', 2*(self.getBet())
						setBalance(2*(self.bet()))
						print 'Your new balance: N',self.getBalance()
					elif((self.doubleMark < dealer) and (dealer <= 21)):
						print 'You Lost! \nYou got nothing'
						
						print 'Your new balance: N',self.getBalance()
					elif(self.doubleMark == dealer):
						print 'Push! \nYou got N',self.getBet()
						setBalance(self.getBet())
						print 'Your new balance: N',self.getBalance()					
					
						
		def setBet(self,b):
				self.bet = b
		def getBet(self):
				return self.bet
					
		def setBalance(self,b):
				self.balance += b
		
		def doubleDown(self,h):
				h[0].append(self.hit())
				return int(self.mark(h)/2)	
		def hit(self):
				hand = [random.choice(self.cards)]
				x = ''
				for a in hand:
					x += str(a)
				return x
		def stand(self):
				pass
		def mark(self,h):
				mark1 = 0;
				ace = False
				for i in h[0]:
					try:
						mark1 += int(i)
					except:
						if(i != 'A'):
							mark1 += 10
						else:
							ace = True
					finally:
						if(ace):
							if(mark1 <= 10):
								mark1 += 11
							else:
								mark1 += 1
				return mark1
				
		
		def resetBalanace(self):
				 self.balance = 100
				
		
		def dealer(self):
				hand = [random.sample(self.cards,2)]
				global d
				temp =[]
				for y in hand:
					temp.append(y)
				self.d = temp
				
		def player(self):
				hand = [random.sample(self.cards,2)]
				global p
				temp =[]
				for y in hand:
					temp.append(y)
				self.p = temp
				
		def getBalance(self):
				return self.balance
		