import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from numpy import trapz

# Global variables
GRAVITY = 9.81      # [m/s2]
THETA = np.linspace(0,2*pi,100)

### TO DO ###
# create bike class? rider class?
# more accurate force profile
# Find the correct gear diameters from my bike
# Implement class inheritance for the crankset/crankshaft classes?

def testCassette():

    # Don't know why you would ever have an elliptical cassette but I guess technically the class can also take an elliptical shape
    # Then this begs the question do we even need a different cassette and crankset class because they are essentially the same thing and should have all the same methods???

    ### TEST CIRCLE ###
    print("Circle Test:")
    test_circle = Cassette([54,34],2)

    print(test_circle.R)
    print(test_circle.num)

    test_circle.changeCassette([24,44],2)

    print(test_circle.R)
    print(test_circle.num)

    print(test_circle.getSprocket(2))

    test_circle.setSprocket(54,2)

    print(test_circle.R)

    test_circle.addSprocket(34)

    print(test_circle.R)
    print(test_circle.num)

    test_circle.removeSprocket(2)

    print(test_circle.R)
    print(test_circle.num)

    ### TEST ELLIPSE ###
    print("\nEllipse Test:")
    test_ellipse = Cassette([(56,52),(36,32)],2)

    print(test_ellipse.R)
    print(test_ellipse.num)

    test_ellipse.changeCassette([(22,26),(42,46)],2)

    print(test_ellipse.R)
    print(test_ellipse.num)

    print(test_ellipse.getSprocket(2))

    test_ellipse.setSprocket((52,56),2)

    print(test_ellipse.R)

    test_ellipse.addSprocket((32,36))

    print(test_ellipse.R)
    print(test_ellipse.num)
    
    test_ellipse.removeSprocket(2)

    print(test_ellipse.R)
    print(test_ellipse.num)

def testCrankset():
    
    print("Circle Test:")

    test_circle = Crankset([54,34],2,'c')

    print(test_circle.ab)
    print(test_circle.num)
    print(test_circle.shape)

    test_circle.changeCrankset([(22,26),(42,46)],2,'e')

    print(test_circle.ab)
    print(test_circle.num)
    print(test_circle.shape)

    test_circle.changeCrankset([24,44],2,'c')

    print(test_circle.ab)
    print(test_circle.num)
    print(test_circle.shape)

    print(test_circle.getCrankGear(2))

    test_circle.setCrankGear(54,2)

    print(test_circle.ab)

    test_circle.addCrankGear(34)

    print(test_circle.ab)
    print(test_circle.num)

    test_circle.removeCrankGear(2)

    print(test_circle.ab)
    print(test_circle.num)

    print(test_circle.calcRadius(1,np.linspace(0,pi,10)))

    print("\nEllipse Test:")

    test_ellipse = Crankset([(52,56),(32,36)],2,'e')

    print(test_ellipse.ab)
    print(test_ellipse.num)
    print(test_ellipse.shape)

    test_ellipse.changeCrankset([(22,26),(42,46)],2,'e')

    print(test_ellipse.ab)
    print(test_ellipse.num)
    print(test_ellipse.shape)

    print(test_ellipse.getCrankGear(2))

    test_ellipse.setCrankGear((52,56),2)

    print(test_ellipse.ab)

    test_ellipse.setCrankGear(54,2)

    test_ellipse.addCrankGear((32,36))

    print(test_ellipse.ab)
    print(test_ellipse.num)

    test_ellipse.addCrankGear(54)

    test_ellipse.removeCrankGear(2)

    print(test_ellipse.ab)
    print(test_ellipse.num)

    print(test_ellipse.calcRadius(1,np.linspace(0,pi,10)))

def testCrankshaft():

    test = Crankshaft(150,0)

    print(test.R)
    print(test.offset)

    test.setOffset(pi)

    print(test.offset)

    print(test.getOffset())

    test.setRadius(120)

    print(test.R)

    print(test.getRadius())


class Cassette:
    """
    Class defining a bike cassette object

    Arguments:
    R: array of the cassette sprocket radii in mm in ascending order
    n: integer number of the sprockets in the cassette

    Methods:
    changeCassette(R: array, n:int): changes the entire cassette assembly to the new sprocket sizes defined in R with number of sprockets n
    getSprocket(i: int): returns the radius of the sprocket at index i in the list
    setSprocket(r: float, i: int): changes the radius of the sprocket at index i to radius r 
    addSprocket(r: float): adds a sprocket to the cassette assembly
    removeSprocket(i: int): removes the sprocket at index i from the cassette assembly
    """

    def __init__(self,R,n):
        self.R_cassette = R      #[mm]
        self.R_cassette.sort()
        self.num_cassette = n
    
    def changeCassette(self,R,n):
        self.R_cassette = R
        self.num_cassette = n
    
    def getSprocket(self,i):
        return self.R_cassette[i-1]
    
    def setSprocket(self,r,i):
        self.R_cassette[i-1] = r

    def addSprocket(self,r):
        self.R_cassette.append(r)
        self.R_cassette.sort()
        self.num_cassette += 1

    def removeSprocket(self,i):
        self.R_cassette.pop(i-1)
        self.num_cassette -= 1
    
class Crankset:
    """
    Class defining a Crankset object

    Arguments:
    R: array of integers defining the radii of the crankset gears in mm in the case of a circular crankset in ascending order
    OR
    array of tuples defining the major and minor radii of the crankset gears in mm in the case of an elliptical crankset in ascending order
    n: integer number indicating the number of gears in the crankset asembly
    s: character indicating the shape type of the crankset --> 'c': circular, 'e': elliptical

    Methods:
    changeCrankset(R: array, n: int, s: char): changes the parameters of teh crankset assembly
    setCrankGear(r: float, i: int): changes the crank gear at the specified index to a new radius value in mm
    addCrankGear(r: float): adds a new crank gear with radius r in mm to the crankset assembly
    removeCrankGear(i:int): removes the crank gear at position i from the crankset assembly
    getCrankGear(i:int): returns the radius information for the specified gear. The return value is a float if the gear has shape 'c' and a tuple if the gear has shape 'e'
    calcRadius(i: int, t: float array): calculates the radius of teh crank gear. Returns a float radius in mm if the gear has shape 'c' and an array of radii in mm defining a rotation (t) of the crank gear if the shape is 'e'
    """

    def __init__(self,R,n,s):
        self.num_crank = n
        self.ab = R
        self.ab.sort()
        self.shape = s

        # remove these
        # self.theta = th
        # self.r = self.ellipse(R)
        
    def changeCrankset(self,R,n,s):
        self.num_crank = n
        self.ab = R
        self.shape = s

    def setCrankGear(self,r,i):
        if type(self.ab[i-1]) != type(r):
            print("error: cannot mix crank gear shapes")
            exit
        else: 
            self.ab[i-1] = r

    def addCrankGear(self,r):
        if type(self.ab[0]) != type(r):
            print("error: cannot mix crank gear shapes")
            exit
        else: 
            self.ab.append(r)
            self.ab.sort()
            self.num_crank += 1

    def removeCrankGear(self,i):
        self.ab.pop(i-1)
        self.num_crank -= 1

    def getCrankGear(self,i):
        return self.ab[i-1]
    
    def calcRadius(self,i,t):
        if self.shape == 'c':
            return self.getCrankGear(i)
        else:
            g = self.getCrankGear(i)
            return g[0]*g[1]/np.sqrt((g[0]*np.cos(t))**2+(g[1]*np.sin(t))**2)
    
class Crankshaft:

    """
    Class defining a crankshaft object

    Inputs:
    r: float defining  the radius of the cranshaft in mm
    o: float value defining the angle offset between the crankshaft position and the major axis of the ellipse in radians

    Methods:
    setOffset(o: float):    defines a new value for the crankshaft position offset in radians
    getOffset():            returns a float value of the crankshaft offset in radians
    setRadisu(r: float):    defines a new value for the crankshaft radius in mm
    getRadius():            returns a float value of the crankshaft radius in mm
    """

    def __init__(self,r,o):
        self.R_crankshaft = r          #[mm]
        self.offset = o     #[rad]

    def setOffset(self,o):
        self.offset = o

    def getOffset(self):
        return self.offset

    def setRadiusShaft(self,r):
        self.R_crankshaft = r

    def getRadiusShaft(self):
        return self.R_crankshaft
    
class Bike(Crankshaft,Crankset,Cassette):

    def __init__(self,R_crankshaft,o,R_crankset,n_crankset,s,R_cassette,n_cassette,person,w_radius,m_bike):
        Crankshaft.__init__(self,R_crankshaft,o)
        Crankset.__init__(self,R_crankset,n_crankset,s)
        Cassette.__init__(self,R_cassette,n_cassette)
        self.rider = person
        self.mass = m_bike
        self.wheelR = w_radius
        self.backgear = 1
        self.frontgear = 2

    def calcDriveTorque(self):
        return self.getRadiusShaft()*self.calcGearRatio(self.backgear,self.frontgear)*self.rider.F(self.offset)

    def calcDriveForce(self):
        return self.calcDriveTorque()/self.wheelR

    def calcGearRatio(self,b,f):
        return self.getSprocket(b)/self.calcRadius(f,THETA)

    def calcGearOverlap(self):
        i = 0
        g = []
        m = ['b','r','g','c']
        for c in (np.linspace(1,self.num_crank,self.num_crank,dtype=int)):
            for s in (np.linspace(1,self.num_cassette,self.num_cassette,dtype=int)):
                if self.shape == 'c':
                    g.append((1/self.calcGearRatio(s,c),m[i]))
                    big = max(g)[0]     # Not the best but I can't think of a better strategy at the moment
                else:
                    g.append(((1/min(self.calcGearRatio(s,c)),1/max(self.calcGearRatio(s,c))),m[i]))
                    big = max(g)[0][0]
            i +=1
        g.sort()
        
        # Plot the gear ratios
        x = 0
        if self.shape == 'c':
            for t in g:
                plt.plot(x,t[0],color=t[1],marker='o')
                x += 1
        else:
            for t in g:
                plt.errorbar(x,t[0][1]+(t[0][0]-t[0][1])/2,yerr=(t[0][0]-t[0][1])/2,color=t[1],marker='o')
                x += 1
        for n in (np.linspace(1,self.num_crank,self.num_crank,dtype=int)):
            plt.text(0,big-0.25*n,'Crank '+str(n),color=m[n-1])
        plt.xlabel('Gear Number')
        plt.ylabel('Gear Ratio')
        plt.title('Gear Ratio Overlap')
        plt.show()

    def changeGear(self,back,front):
        self.backgear = back
        self.frontgear = front

    def simRide(self):
        pass

class Rider:
    # Class to define a rider on the bike
    # Maybe linkage mechanism simulation for the leg mechanics and joint torques?
    def __init__(self,m,n):
        self.mass = m
        self.name = n
    
    def F(self,o):
        return self.mass*GRAVITY*np.sin(THETA+o)
    
    def getMass(self):
        return self.mass
    
    def setMass(self,m):
        self.mass = m

    def getName(self):
        return self.name
    
    def setName(self,n):
        self.name = n

class Force:
    def __init__(self,mg,th,crankshaft):
        self.W = mg
        self.theta = th
        self.F = self.calcF(crankshaft)

    def calcF(self,crankshaft):
        return self.W*np.sin(self.theta+crankshaft.offset)

def main():

    # testCassette()
    # testCrankset()
    # testCrankshaft()

    # Add a bycicle class which can be built up of the cassette class and the crankset class and a rider class?

    theta = np.linspace(0,2*pi,100)

    cassette = Cassette([11,12,13,14,15],5)
    biopace = Crankset([(56,52),(36,32)],2,'e')
    qring = Crankset([(52,56),(32,36)],2,'e')
    circle = Crankset([54,34],2,'c')
    crankshaft = Crankshaft(150,0)

    set = 2
    sprocket = 1

    Manon = Rider(64,'Manon')
    bike_circle = Bike(150,0,[44,34],2,'c',[11,12,13,14,15],5,Manon,500,3)
    bike_biopace = Bike(150,0,[(46,42),(36,32)],2,'e',[11,12,13,14,15],5,Manon,500,3)
    bike_qring = Bike(150,0,[(52,56),(32,36)],2,'e',[11,12,13,14,15],5,Manon,500,3)

    bike_circle.calcGearOverlap()

    # # Should change these forces and torques to go inside the crankset class definition
    # P = Force(64*9.81,theta,crankshaft)

    # T_circle = crankshaft.R_crankshaft*cassette.getSprocket(sprocket)*P.F/circle.calcRadius(set,theta)
    # T_biopace = crankshaft.R_crankshaft*cassette.getSprocket(sprocket)*P.F/biopace.calcRadius(set,theta)
    # T_qring = crankshaft.R_crankshaft*cassette.getSprocket(sprocket)*P.F/qring.calcRadius(set,theta)

    # # plt.plot(theta,P_circle.F*crankshaft.R,color='yellow',label="P_circle")
    # # plt.plot(theta,T_circle,color="red",label='T_circle')
    # plt.plot(THETA,bike_circle.calcDriveTorque(),color="pink",label='T_circle')
    # # plt.plot(theta,T_biopace,color="blue",label='T_biopace')
    # plt.plot(THETA,bike_biopace.calcDriveTorque(),color="cyan",label='T_biopace')
    # plt.plot(THETA,bike_qring.calcDriveTorque(),color="cyan",label='T_biopace')
    # # plt.plot(theta,T_qring,color="green",label='T_qring')
    # plt.xlabel("Theta", fontsize = 10)
    # plt.ylabel("Torque",fontsize=10)
    # plt.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','pi/2','pi','3pi/2','2pi'])
    # plt.grid(True)
    # plt.legend()
    # plt.show()


if __name__ == '__main__':
    main()