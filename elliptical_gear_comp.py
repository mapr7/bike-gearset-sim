import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from numpy import trapz

class Cassette:

    def __init__(self,R,n):
        self.R = R
        self.n = n
    
    def easy(self):
        return self.R[self.n-1]
    
    def hard(self):
        return self.R[0]
    
    def getSprocket(self,n):
        return self.R[n-1]
    
class Crankset:

    def __init__(self,R,n,th):
        self.n = n
        self.ab = R
        self.theta = th
        self.r = self.ellipse(R)
        

    # Actually change this so it is not calculating the ellipse for each set but only when you call get set
    def ellipse(self,R):

        r = np.zeros((self.n,len(self.theta)))
        i = 0
        for g in R:
            r[i] = g[0]*g[1]/np.sqrt((g[0]*np.cos(self.theta))**2+(g[1]*np.sin(self.theta))**2)
            i = i+1
        
        return r
        
    # def easy(self):
    #     self.a = self.ab[self.n-1][0]
    #     self.b = self.ab[self.n-1][1]
    #     return self.r[self.n-1]
    
    # def hard(self):
    #     self.a = self.ab[0][0]
    #     self.b = self.ab[0][1]
    #     return self.r[0]
    
    def getSet(self,n):
        return self.r[n-1]
    
    def setSet(self,n):
        self.a = self.ab[n-1][0]
        self.b = self.ab[n-1][1]
    
    def getTangent(self,crankshaft,theta):
        return self.b**2/(self.a**2*np.tan(theta+crankshaft.offset))
    
class Crankshaft:
    def __init__(self,r,o):
        self.R = r
        self.offset = o

class Force:
    def __init__(self,mg,th,crankshaft,crankset):
        self.W = mg
        self.theta = th
        self.F = self.calcF(crankshaft,crankset)

    def calcF(self,crankshaft,crankset):
        return self.W*np.sin(self.theta+crankshaft.offset)#crankset.getTangent(crankshaft,self.theta) 

def main():

    # Add a bycicle class which can be built up of the cassette class and the crankset class and a rider class?

    theta = np.linspace(0,2*pi,100)

    cassette = Cassette([11,12,13,14,15],5)
    biopace = Crankset([(56,52),(36,32)],2,theta)
    qring = Crankset([(52,56),(32,56)],2,theta)
    circle = Crankset([(54,54),(34,34)],2,theta)
    crankshaft = Crankshaft(150,0)

    set = 1
    sprocket = 5

    biopace.setSet(set)
    qring.setSet(set)
    circle.setSet(set)

    # Should change these forces to go inside the crankset class definition
    P_circle = Force(64*9.81,theta,crankshaft,circle)
    P_biopace = Force(64*9.81,theta,crankshaft,biopace)
    P_qring = Force(64*9.81,theta,crankshaft,qring)

    # print(P_circle.F)

    plt.plot(theta,circle.getSet(set),color="red",label='r_circle')
    plt.plot(theta,biopace.getSet(set),color="blue",label='r_bio')
    plt.plot(theta,qring.getSet(set),color="green",label='r_q')
    plt.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','pi/2','pi','3pi/2','2pi'])
    plt.grid(True,axis='x')
    plt.legend()
    plt.show()

    T_circle = crankshaft.R*cassette.getSprocket(sprocket)*P_circle.F/circle.getSet(set)
    T_biopace = crankshaft.R*cassette.getSprocket(sprocket)*P_biopace.F/biopace.getSet(set)
    T_qring = crankshaft.R*cassette.getSprocket(sprocket)*P_qring.F/qring.getSet(set)

    # plt.plot(theta,P_circle.F*crankshaft.R,color='yellow',label="P_circle")
    plt.plot(theta,T_circle,color="red",label='T_circle')
    plt.plot(theta,T_biopace,color="blue",label='T_biopace')
    plt.plot(theta,T_qring,color="green",label='T_qring')
    plt.xlabel("Theta", fontsize = 10)
    plt.ylabel("Torque",fontsize=10)
    plt.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','pi/2','pi','3pi/2','2pi'])
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()