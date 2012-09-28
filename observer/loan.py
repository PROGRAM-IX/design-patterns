from i_subject import i_subject

class loan(i_subject):
    
    def __init__(self):
        """ Initialise instance variables """
        self.interest_rate = 0.35
        self.observers = []        
    
    def attach(self, ob):
        """ Override for the subject attach method """
        self.observers.append(ob)
        ob.update(self)
        
    def detach(self, ob):
        """ Override for the subject detach method """
        self.observers.remove(ob)
    
    def notify(self):
        """ Override for the notify method """
        for o in self.observers:
            o.update(self)
    
    def get_interest_rate(self):
        """ Return the current interest rate """
        return self.interest_rate
        
    def set_interest_rate(self, new_rate):
        """ Set the interest rate """
        self.interest_rate = new_rate
        self.notify() 
