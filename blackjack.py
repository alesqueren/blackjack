#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import optparse
from game import Game

def process_cmd_line():
   # parse command line options
   parser = optparse.OptionParser(
         usage='Usage: %prog [options] initial_pot', 
         description='Play blackjack and become a milionar !')
   (opts, args) = parser.parse_args()

   # set initial pot
   if len(args) == 1:
      return args[0]
   else:
      print "Wrong argument number :"
      parser.print_help()
      exit(-1)

def main():
   pot = process_cmd_line()

   game = Game()
   game.play()

if __name__ == "__main__":
   main()
