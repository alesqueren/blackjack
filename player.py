import os, random
from hand import Hand

nl = os.linesep

class Player:

   def __init__(self, pot, is_dealer, strategy, name = 'un joueur'):
      self._pot = pot
      self._is_dealer = is_dealer
      self._strategy = strategy
      self._name = name
      self._chairs = []

   def getMainHand(self):
      if len(self._chairs) == 0:
         self._chairs.append({ 'hand': Hand(), 'bet': 0 })
      return self._chairs[0]['hand']

   def bet(self):
      bet = self._strategy.betAmount()

      self._pot -= bet
      self._chairs.append({ 'hand': Hand(), 'bet': bet })

      return True

   def play(self, deck, dealer_hand = None):

      # play all hands once
      i = 0
      while i < len(self._chairs):
         chair = self._chairs[i]
         i+=1

         while not chair['hand'].isOver():
            action = self._strategy.chooseAction(chair['hand'], dealer_hand)

            if action == 'P':
               chair['hand'].addCard(deck.pick())
            if action == 'L':
               break;
            if action == 'D':
               self._pot -= chair['bet']
               chair['bet'] *= 2
               chair['hand'].addCard(deck.pick())
               break;
            if action == 'A':
               chair['hand']._is_abandonned = True
               break;
            if action == 'S':
               # append 2 new hands
               for l in [0, 1]:
                  # take one of the 2 cards 
                  hand = Hand()
                  hand.addCard(chair['hand']._cards[l])
                  hand.addCard(deck.pick())
                  # bet 
                  bet = chair['bet']
                  self._pot -= bet
                  # will be played later
                  new_chair = { 'hand': hand, 'bet': bet }
                  self._chairs.append(new_chair)
               # remove splited hand 
               self._pot += chair['bet']
               self._chairs.remove(chair)
               i-=1
               break;

   def getGains(self, dealer_hand):

      gainCoefficient = {
         'blackjack' : 2.5,
         'victory' : 2,
         'tie' : 1,
         'abandonned' : 0.5,
         'loose' : 0,
      }
      
      for chair in self._chairs:
         result = chair['hand'].compare(dealer_hand);
         self._pot += gainCoefficient[result] * chair['bet']

      self._chairs = []

   def __str__(self):
      res = ''
      res += '--- ' + self._name + ' ---' + nl
      for chair in self._chairs:
         if not self._is_dealer:
            res += '[mise = ' + str(chair['bet']) + ']' + nl
         res += str(chair['hand']) + nl
      return res
