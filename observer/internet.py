from i_observer import i_observer

class internet(i_observer):
    def __init__(self):
        """ Initialises the instance variable which stores the value of the subject """
        self.interest_rate = 0
        
    def update(self, sub):
        """ Gets the interest rate from the subject which calls this method - parameter is of type i_subject """
        self.interest_rate = sub.get_interest_rate()
        print "Internet:", str(self.interest_rate)
        

