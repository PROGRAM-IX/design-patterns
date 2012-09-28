from i_observer import i_observer

class newspaper(i_observer):
    def __init__(self):
        """ Initialises the instance variable which stores the value of the subject """
        self.interest_rate = 0
    
    def update(self, sub):
        """ Gets the interest rate from the subject which calls this method """
        self.interest_rate = sub.get_interest_rate()
        print "Newspaper:", str(self.interest_rate)

