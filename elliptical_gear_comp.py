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

    test_circle.changeGearAssembly([24,44],2)

    print(test_circle.R)
    print(test_circle.num)

    print(test_circle.getGear(2))

    test_circle.setGear(54,2)

    print(test_circle.R)

    test_circle.addGear(34)

    print(test_circle.R)
    print(test_circle.num)

    test_circle.removeGear(2)

    print(test_circle.R)
    print(test_circle.num)

    ### TEST ELLIPSE ###
    print("\nEllipse Test:")
    test_ellipse = Cassette([(56,52),(36,32)],2)

    print(test_ellipse.R)
    print(test_ellipse.num)

    test_ellipse.changeGearAssembly([(22,26),(42,46)],2)

    print(test_ellipse.R)
    print(test_ellipse.num)

    print(test_ellipse.getGear(2))

    test_ellipse.setGear((52,56),2)

    print(test_ellipse.R)

    test_ellipse.addGear((32,36))

    print(test_ellipse.R)
    print(test_ellipse.num)
    
    test_ellipse.removeGear(2)

    print(test_ellipse.R)
    print(test_ellipse.num)

def testCrankset():
    
    print("Circle Test:")

    test_circle = Crankset([54,34],2,'c')

    print(test_circle.R)
    print(test_circle.num)
    print(test_circle.shape)

    test_circle.changeGearAssembly([(22,26),(42,46)],2,'e')

    print(test_circle.R)
    print(test_circle.num)
    print(test_circle.shape)

    test_circle.changeGearAssembly([24,44],2,'c')

    print(test_circle.R)
    print(test_circle.num)
    print(test_circle.shape)

    print(test_circle.getGear(2))

    test_circle.setGear(54,2)

    print(test_circle.R)

    test_circle.addGear(34)

    print(test_circle.R)
    print(test_circle.num)

    test_circle.removeGear(2)

    print(test_circle.R)
    print(test_circle.num)

    print(test_circle.calcRadius(1,np.linspace(0,pi,10)))

    print("\nEllipse Test:")

    test_ellipse = Crankset([(52,56),(32,36)],2,'e')

    print(test_ellipse.R)
    print(test_ellipse.num)
    print(test_ellipse.shape)

    test_ellipse.changeGearAssembly([(22,26),(42,46)],2,'e')

    print(test_ellipse.R)
    print(test_ellipse.num)
    print(test_ellipse.shape)

    print(test_ellipse.getGear(2))

    test_ellipse.setGear((52,56),2)

    print(test_ellipse.R)

    test_ellipse.setGear(54,2)

    test_ellipse.addGear((32,36))

    print(test_ellipse.R)
    print(test_ellipse.num)

    test_ellipse.addGear(54)

    test_ellipse.removeGear(2)

    print(test_ellipse.R)
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
    changeGearAssembly(R: array, n:int): changes the entire cassette assembly to the new sprocket sizes defined in R with number of sprockets n
    getGear(i: int): returns the radius of the sprocket at index i in the list
    setGear(r: float, i: int): changes the radius of the sprocket at index i to radius r 
    addGear(r: float): adds a sprocket to the cassette assembly
    removeGear(i: int): removes the sprocket at index i from the cassette assembly
    """

    def __init__(self,R,n):
        self.R = R      #[mm]
        self.R.sort()
        self.num = n
    
    def changeGearAssembly(self,R,n):
        self.R = R
        self.num = n
    
    def getGear(self,i):
        return self.R[i-1]
    
    def setGear(self,r,i):
        self.R[i-1] = r

    def addGear(self,r):
        self.R.append(r)
        self.R.sort()
        self.num += 1

    def removeGear(self,i):
        self.R.pop(i-1)
        self.num -= 1

    def getNum(self):
        return self.num
    
class Crankset(Cassette):
    """
    Class defining a Crankset object

    Arguments:
    R: array of integers defining the radii of the crankset gears in mm in the case of a circular crankset in ascending order
    OR
    array of tuples defining the major and minor radii of the crankset gears in mm in the case of an elliptical crankset in ascending order
    n: integer number indicating the number of gears in the crankset asembly
    s: character indicating the shape type of the crankset --> 'c': circular, 'e': elliptical

    Methods:
    changeGearAssembly(R: array, n: int, s: char): changes the parameters of teh crankset assembly
    setGear(r: float, i: int): changes the crank gear at the specified index to a new radius value in mm
    addGear(r: float): adds a new crank gear with radius r in mm to the crankset assembly
    removeCrankGear(i:int): removes the crank gear at position i from the crankset assembly
    getCrankGear(i:int): returns the radius information for the specified gear. The return value is a float if the gear has shape 'c' and a tuple if the gear has shape 'e'
    calcRadius(i: int, t: float array): calculates the radius of teh crank gear. Returns a float radius in mm if the gear has shape 'c' and an array of radii in mm defining a rotation (t) of the crank gear if the shape is 'e'
    """

    def __init__(self,R,n,s):
        Cassette.__init__(self,R,n)
        self.shape = s
        
    def changeGearAssembly(self,R,n,s):
        # Overwrite cassette method
        self.num = n
        self.R = R
        self.shape = s

    def setGear(self,r,i):
        if type(self.R[i-1]) != type(r):
            print("error: cannot mix crank gear shapes")
            exit
        else: 
            self.R[i-1] = r
    
    def getShape(self):
        return self.shape

    def addGear(self,r):
        if type(self.R[0]) != type(r):
            print("error: cannot mix crank gear shapes")
            exit
        else: 
            self.R.append(r)
            self.R.sort()
            self.num += 1
    
    def calcRadius(self,i,t):
        if self.shape == 'c':
            return self.getGear(i)
        else:
            g = self.getGear(i)
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
    
class Bike:

    def __init__(self,crankshaft,crankset,cassette,person,w_radius,m_bike):
        self.crankshaft = crankshaft
        self.crankset = crankset
        self.cassette = cassette
        self.rider = person
        self.mass = m_bike
        self.wheelR = w_radius
        self.backgear = 1
        self.frontgear = 2

    def calcDriveTorque(self):
        return self.crankshaft.getRadiusShaft()*self.calcGearRatio(self.backgear,self.frontgear)*self.rider.F(self.crankshaft.getOffset())

    def calcDriveForce(self):
        return self.calcDriveTorque()/self.wheelR

    def calcGearRatio(self,b,f):
        return self.cassette.getGear(b)/self.crankset.calcRadius(f,THETA)

    def calcGearOverlap(self):
        i = 0
        g = []
        m = ['b','r','g','c']
        for c in (np.linspace(1,self.crankset.getNum(),self.crankset.getNum(),dtype=int)):
            for s in (np.linspace(1,self.cassette.getNum(),self.cassette.getNum(),dtype=int)):
                if self.crankset.getShape() == 'c':
                    g.append((1/self.calcGearRatio(s,c),m[i]))
                    big = max(g)[0]     # Not the best but I can't think of a better strategy at the moment
                else:
                    g.append(((1/min(self.calcGearRatio(s,c)),1/max(self.calcGearRatio(s,c))),m[i]))
                    big = max(g)[0][0]
            i +=1
        g.sort()
        
        # Plot the gear ratios
        x = 0
        if self.crankset.getShape() == 'c':
            for t in g:
                plt.plot(x,t[0],color=t[1],marker='o')
                x += 1
        else:
            for t in g:
                plt.errorbar(x,t[0][1]+(t[0][0]-t[0][1])/2,yerr=(t[0][0]-t[0][1])/2,color=t[1],marker='o')
                x += 1
        for n in (np.linspace(1,self.crankset.getNum(),self.crankset.getNum(),dtype=int)):
            plt.text(0,big-0.25*n,'Crank '+str(n),color=m[n-1])
        plt.xlabel('Gear Number')
        plt.ylabel('Gear Ratio')
        plt.title('Gear Ratio Overlap')
        plt.show()

    def changeGear(self,back,front):
        self.backgear = back
        self.frontgear = front

    def changeCassette(self,c):
        self.cassette = c

    def changeCrankshaft(self,c):
        self.crankshaft = c

    def changeCrankset(self,c):
        self.crankset = c

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

def main():

    # testCassette()
    # testCrankset()
    # testCrankshaft()

    # Initiate the cassette and crankshaft objects
    cassette = Cassette([11,12,13,14,15],5)
    crankshaft = Crankshaft(150,0)

    # Initiation the crankset objects with different shapes
    biopace = Crankset([(56,52),(36,32)],2,'e')
    qring = Crankset([(52,56),(32,36)],2,'e')
    circle = Crankset([54,34],2,'c')

    # Initiate the bike rider
    Manon = Rider(64,'Manon')

    # Create the different bike objects
    bike_circle = Bike(crankshaft,circle,cassette,Manon,500,3)
    bike_biopace = Bike(crankshaft,biopace,cassette,Manon,500,3)
    bike_qring = Bike(crankshaft,qring,cassette,Manon,500,3)

    # Look at gear ratio overlap for each bike type
    bike_circle.calcGearOverlap()
    bike_biopace.calcGearOverlap()
    bike_qring.calcGearOverlap()

    # Plot comparison between drive torque for different cranksets
    plt.plot(THETA,bike_circle.calcDriveTorque(),color="pink",label='T_circle')
    plt.plot(THETA,bike_biopace.calcDriveTorque(),color="cyan",label='T_biopace')
    plt.plot(THETA,bike_qring.calcDriveTorque(),color="lime",label='T_qring')
    plt.xlabel("Theta", fontsize = 10)
    plt.ylabel("Torque",fontsize=10)
    plt.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','pi/2','pi','3pi/2','2pi'])
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()