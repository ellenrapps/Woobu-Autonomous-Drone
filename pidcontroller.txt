'''
Source: https://github.com/shivaay1/Equsant-Self-Balancing-Robot-Python/blob/master/pidcontroller.py
'''

'''HARIOMHARIBOLJAIMATAJIPITAJIKIJAIJAI'''
#Developed by Mark Tomczak (fixermark@gmail.com)
#Python class to calculate PID values


class PIDController:
    def __init__(self, P, I, D):
        self.KP = P
        self.KI = I
        self.KD = D
        self.target = 0

        self.lastError = 0
        self.integrator = 0

    def setTarget(self, newTarget):
        self.target = newTarget
        self.integrator = 0

    def step(self, currentValue):
        error = currentValue - self.target

        output = (self.KP * error + self.KI * self.integrator + self.KD * (error - self.lastError))

        self.lastError = error
        self.integrator += error

        return output

