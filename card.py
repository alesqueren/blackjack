import random

class Card:
   
   def __init__(self, siut, high):
      self._siut = siut
      self._high = high
      if high == 'as':
         self._scores = [1, 11]
      elif high in ['10', 'valet', 'dame', 'roi']:
         self._scores = [10]
      else:
         self._scores = [int(high)]

   def __str__(self):
      return self._high + " de " + self._siut

class Deck:

   def __init__(self, deck_nb):
      self._deck_nb = deck_nb
      self._threshold = 52 * 2
      self._cards = []
      self.initCards()

   def initCards(self):
      siuts = ['coeur', 'carreau', 'pique', 'trefle']
      highs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi', 'as']
      for i in range(self._deck_nb):
         for siut in siuts:
            for high in highs:
               self._cards.append(Card(siut, high))
      random.shuffle(self._cards)

   def isFinished(self):
       return len(self._cards) < self._threshold

   def pick(self):
      return self._cards.pop()
