from string import ascii_letters as alphabet

class Automaton(object):
    def __init__(self,q,sigma,delta,initial,final):
        self.q = q
        self.sigma = sigma
        self.delta = delta
        self.initial = initial
        self.final = final


q = ['q1','q2','q3']
sigma = alphabet + '0123456789'



print(sigma)

