import os

nl = os.linesep

class Hand:
   def __init__(self):
      self._cards = []
      self._scores = [0]
      self._is_abandonned = False

   def isBlackJack(self):
      return self.getScore() == 21 and len(self._cards) == 2

   def isOver(self):
       return self.getScore() == -1

   def hasPair(self):
      if (len(self._cards) != 2):
          return False
      return self._cards[0]._high == self._cards[1]._high

   def hasAce(self):
      if (len(self._cards) != 2):
          return False
      return (self._cards[0]._high == 'as' or \
              self._cards[1]._high == 'as')

   def getScore(self):
      valid_scores = [x for x in self._scores if x <= 21]
      if valid_scores:
         return max(valid_scores)
      else:
         return -1

   def addCard(self, card):
      # update scores
      new_scores = []
      for card_score in card._scores:
         for hand_score in self._scores:
            new_scores.append(hand_score + card_score)
      self._scores = new_scores;
      # add the new card
      self._cards.append(card);

   def compare(self, other):
      if self._is_abandonned:
         return 'abandonned'

      if self.isBlackJack() and not other.isBlackJack():
         return 'blackjack'

      if self.getScore() > other.getScore():
         return 'victory'

      if self.getScore() == other.getScore() \
          and not self.isOver():
         return 'tie'

      return 'loose'

   def __str__(self):
      res = ''
      for card in self._cards:
         res += str(card) + nl
      res += '[score = '+str(self.getScore())+']' + nl
      return res
