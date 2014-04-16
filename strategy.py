class Strategy:

    def __init__(self, counters = []):
        self.counter = None

class Simple(Strategy):

    def __init__(self, counters = []):
        Strategy.__init__(self, counters)

    def betAmount(self):
        return 1

    def chooseAction(self, hand, dealer_hand):
        if hand.getScore() < 17:
            return 'P' 
        return 'L' 

class Base(Strategy):

    def __init__(self, counters = []):
        Strategy.__init__(self, counters)

    def betAmount(self):
        return 1

    def chooseAction(self, hand, dealer_hand):
        player_index = {
                '2': '2', 
                '3': '3', 
                '4': '4', 
                '5': '5', 
                '6': '6', 
                '7': '7', 
                '8': '8', 
                '9': '9', 
                '10': '10', 
                'valet': '10', 
                'dame': '10', 
                'roi': '10', 
                'as': 'A', 
                }

        dealer_index = {
                '2': 0, 
                '3': 1, 
                '4': 2, 
                '5': 3, 
                '6': 4, 
                '7': 5, 
                '8': 6, 
                '9': 7, 
                '10': 8, 
                'valet': 8, 
                'dame': 8, 
                'roi': 8, 
                'as': 9, 
                }

        actions_score = {
                '21' : ['L','L','L','L','L','L','L','L','L','L'],
                '20' : ['L','L','L','L','L','L','L','L','L','L'],
                '19' : ['L','L','L','L','L','L','L','L','L','L'],
                '18' : ['L','L','L','L','L','L','L','L','L','L'],
                '17' : ['L','L','L','L','L','L','L','L','L','A'],
                '16' : ['L','L','L','L','L','P','P','A','A','A'],
                '15' : ['L','L','L','L','L','P','P','P','A','A'],
                '14' : ['L','L','L','L','L','P','P','P','A','A'],
                '13' : ['L','L','L','L','L','P','P','P','P','A'],
                '12' : ['P','P','L','L','L','P','P','P','P','A'],
                '11' : ['D','D','D','D','D','D','D','D','P','P'],
                '10' : ['D','D','D','D','D','D','D','D','P','P'],
                '9'  : ['P','D','D','D','D','P','P','P','P','P'],
                '8'  : ['P','P','P','P','P','P','P','P','P','P'],
                '7'  : ['P','P','P','P','P','P','P','P','P','P'],
                '6'  : ['P','P','P','P','P','P','P','P','P','P'],
                '5'  : ['P','P','P','P','P','P','P','P','P','P']
                }

        actions_pair = {
                'A' : ['S','S','S','S','S','S','S','S','S','L'],
                '10' : ['L','L','L','L','L','L','L','L','L','L'],
                '9' : ['S','S','S','S','S','L','S','S','L','L'],
                '8' : ['S','S','S','S','S','S','S','S','A','A'],
                '7' : ['S','S','S','S','S','S','P','P','A','A'],
                '6' : ['S','S','S','S','S','P','P','P','P','A'],
                '5' : ['D','D','D','D','D','D','D','D','P','P'],
                '4' : ['P','P','P','S','S','P','P','P','P','P'],
                '3' : ['S','S','S','S','S','S','P','P','P','A'],
                '2' : ['S','S','S','S','S','S','P','P','P','P'],
                }

        actions_ace = {
                '10' : ['L','L','L','L','L','L','L','L','L','L'],
                '9' : ['L','L','L','L','L','L','L','L','L','L'],
                '8' : ['L','L','L','L','L','L','L','L','L','L'],
                '7' : ['L','D','D','D','D','L','L','P','P','P'],
                '6' : ['P','D','D','D','D','P','P','P','P','P'],
                '5' : ['P','P','D','D','D','P','P','P','P','P'],
                '4' : ['P','P','D','D','D','P','P','P','P','P'],
                '3' : ['P','P','P','D','D','P','P','P','P','P'],
                '2' : ['P','P','P','D','D','P','P','P','P','P'],
                }
        x_index = dealer_index[dealer_hand._cards[0]._high]
        
        if hand.hasPair():
            table = actions_pair
            y_index = player_index[hand._cards[0]._high]
        elif hand.hasAce():
            table = actions_ace
            no_ace = hand._cards[0]._high
            if (no_ace == 'as'):
                no_ace = hand._cards[1]._high
            y_index = player_index[no_ace]
        else:
            table = actions_score
            y_index = str(hand.getScore())

        return table[y_index][x_index]
