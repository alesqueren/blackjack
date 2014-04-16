#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from player import Player
from card import Deck
from strategy import Simple, Base
import os

nl = os.linesep

class Game:

   def __init__(self):
      self._players_nb = None
      self._blend = None
      self._max_game = 100000
      self._deck = Deck(6)

      strat_simple = Simple()
      strat_base = Base()

      self._dealer = Player(10000, 1, strat_simple, 'dealer')

      self._players = []
      self._players.append(Player(0, 0, strat_base, 'guest'))

   def play(self):
      game_nb = 1

      while game_nb <= self._max_game:

         # Get a new deck if needed
         if self._deck.isFinished():
            self._deck.initCards()

         # Players bet
         beters = []
         for player in self._players:
            if player.bet():
               beters.append(player)

         # Dealer picks one card
         self._dealer.getMainHand().addCard(self._deck.pick())

         # Players pick 2 cards
         for i in [1, 2]:
            for player in self._players:
               player.getMainHand().addCard(self._deck.pick())

         # Players play
         for player in self._players:
            player.play(self._deck, self._dealer.getMainHand())

         # Dealer plays
         self._dealer.getMainHand().addCard(self._deck.pick())
         self._dealer.play(self._deck)

         # Money transferts
         for player in self._players:
            player.getGains(self._dealer.getMainHand())
         self._dealer._chairs = []

         game_nb += 1

      print "FINAL : {0:.2f}€ in {1:.0f} hours. [{2:.2f}% benefit, {3:.2f} €/h]"\
              .format(self._players[0]._pot, game_nb / 50, self._players[0]._pot / game_nb, self._players[0]._pot / (game_nb / 50))
