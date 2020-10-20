'''
This work by Alejandro Fernandez del Valle Herrea is licensed under CC BY 4.0 CC

This script creates all the information for the volcano, with and without drag.

Contains 2 different classes:

Rock -> a class that holds all the information of the rock\n
Plotter -> creates a list of rock class, with option to get special variables, and plot using matplotlib\n

in addition it holds special variables global for script:

delta_t = 0.02\n
rangeInTime = (0.0,100.0) \n

densityRho = 1.29\n
gravity = 9.8\n
dragCoeficient = 0.45\n

time = np.array(time,dtype=np.float)

globalArrayLength = time.shape[0]

To update this variables use:\n
updateBaseData()
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from random import randint
from random import uniform

class tcolour:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\u001b[0m'

# variables
delta_t = 0.02
rangeInTime = (0.0,100.0) 

densityRho = 1.29
gravity = 9.8
dragCoeficient = 0.45

densityOfRock = 2600

# get all delta t values, and create a function
time = [rangeInTime[0]]
while time[-1] <= rangeInTime[1]:
    time.append(time[-1] + delta_t)
time = np.array(time,dtype=np.float)

globalArrayLength = time.shape[0]

def updateBaseData(newDelta_t: float = 0.01, newRangeInTime: tuple = (0.0,20.0), newDensity: float = 1.29, newDragCoeficient: float = 0.45, newGravity : float = 9.8):
    '''
    changes al the base information of dataCreator.

    Special variables are:

    newRangeInTime -> 2 floats, start and end.

    all the other variables are float values
    '''
    global delta_t, rangeInTime, densityRho, gravity, dragCoeficient, time, globalArrayLength
    # variables
    delta_t = newDelta_t
    rangeInTime = newRangeInTime

    densityRho = newDensity
    gravity = newGravity
    dragCoeficient = newDragCoeficient

    # get all delta t values, and create a function
    time2 = [rangeInTime[0]]
    while time2[-1] <= rangeInTime[1]:
        time2.append(time2[-1] + delta_t)

    time = np.array(time2,dtype=np.float)

    print(time)

    globalArrayLength = time.shape[0]

class rock:
    def __init__(self, mass, area, initialVelocity : tuple, initialYpos = 1000, calculateWithoutDrag: bool = False):
        '''
        A class that holds all the information for each rock simulated

        mass -> the mass of the rock
        area -> area exposed to air to calculate air resistance
        initial Velocity -> the start velocity as (x,y,z) components
        initial Y Pos -> the starting height over normal ground of launch of the volcano
        calculateWithoutDrag -> calculate or not the drag, to draw later
        '''
        global globalArrayLength

        self.withDrag = calculateWithoutDrag

        self.x = np.zeros(globalArrayLength, dtype=np.float)
        self.y = np.zeros(globalArrayLength, dtype=np.float)
        self.z = np.zeros(globalArrayLength, dtype=np.float)

        self.weight = gravity * mass

        self.x_dragForce = np.zeros(globalArrayLength, dtype=np.float)
        self.y_dragForce = np.zeros(globalArrayLength, dtype=np.float)
        self.z_dragForce = np.zeros(globalArrayLength, dtype=np.float)

        self.x_velocity = np.zeros(globalArrayLength, dtype=np.float)
        self.y_velocity = np.zeros(globalArrayLength, dtype=np.float)
        self.z_velocity = np.zeros(globalArrayLength, dtype=np.float)

        self.x_acceleration = np.zeros(globalArrayLength, dtype=np.float)
        self.y_acceleration = np.zeros(globalArrayLength, dtype=np.float)
        self.z_acceleration = np.zeros(globalArrayLength, dtype=np.float)

        self.area = area
        self.mass = mass

        self.dragForceCoeficient = (densityRho * self.area * dragCoeficient)/2

        self.y[0] = initialYpos

        self.x_velocity[0] = initialVelocity[0]
        self.y_velocity[0] = initialVelocity[1]
        self.z_velocity[0] = initialVelocity[2]
        
        if calculateWithoutDrag:
            # calculate the parabola of the launch
            self.x_withoutDrag = time * initialVelocity[0]
            self.z_withoutDrag = time * initialVelocity[2]
            self.y_withoutDrag = 0.5*-gravity* time ** 2 + initialVelocity[1] * time + initialYpos

            for i in range(globalArrayLength):
                if self.y_withoutDrag[i] < 0:
                    self.x_withoutDrag[i] = 0
                    self.z_withoutDrag[i] = 0
                    self.y_withoutDrag[i] = 0

                    

    def calculateNext(self):
        '''
        calculate the rock values. Thats practically all
        '''
        for i in range(1,globalArrayLength):
            self.x_acceleration[i] = - (self.dragForceCoeficient/self.mass) * np.sqrt(self.x_velocity[i-1] ** 2 + self.y_velocity[i-1] ** 2 + self.z_velocity[i-1] ** 2) * self.x_velocity[i-1]
            self.x_velocity[i] = self.x_velocity[i-1] + self.x_acceleration[i-1] * delta_t
            self.x[i] = self.x[i-1] + self.x_velocity[i] * delta_t + 0.5 * self.x_acceleration[i] * delta_t ** 2 

            self.z_acceleration[i] = - (self.dragForceCoeficient/self.mass) * np.sqrt(self.x_velocity[i-1] ** 2 + self.y_velocity[i-1] ** 2 + self.z_velocity[i-1] ** 2) * self.z_velocity[i-1]
            self.z_velocity[i] = self.z_velocity[i-1] + self.z_acceleration[i-1] * delta_t
            self.z[i] = self.z[i-1] + self.z_velocity[i] * delta_t + 0.5 * self.z_acceleration[i] * delta_t ** 2 

            self.y_acceleration[i] = - gravity - (self.dragForceCoeficient/self.mass) * np.sqrt(self.x_velocity[i-1] ** 2 + self.y_velocity[i-1] ** 2 + self.z_velocity[i-1] ** 2) * self.y_velocity[i-1]
            self.y_velocity[i] = self.y_velocity[i-1] + self.y_acceleration[i-1] * delta_t
            self.y[i] = self.y[i-1] + self.y_velocity[i] * delta_t + 0.5 * self.y_acceleration[i] * delta_t ** 2 

            if self.y[i] < 0:
                break


class plotter:
    def __init__(self, amount:int = 50, doParabolicLines:bool = False, maxForceRange : tuple = (50,500,50), minForceRange : tuple = (50,500,50), areaRange:tuple = (1,10), initialHeight: int = 3200):
        '''
        A plotting method. At start, it creates all the rocks, use plot() to plot them, or getSpecialPoints() to get special points of self

        inputs:

        amount -> the amount of lines to input

        doParabolicLines -> if you also calculate the lines without airdrag (default False)

        maxForceRange -> the maximum range of force it chooses from, given as: (x,y,z) HAS TO BE INT

        maxForceRange -> the minimum range of force it chooses from, given as: (x,y,z) HAS TO BE INT

        areaRange -> the range of radious of figures. given as: (min, max) CAN BE FLOAT
        '''
        self.lines = []

        self.amount = amount

        print('creating lines')
        for i in range(self.amount):
            radious = uniform(areaRange[0],areaRange[1])
            area = radious ** 2 * np.pi # calculates the area that will be in contact with air
            mass = np.pi * radious ** 3 * densityOfRock # density of andesite is 2600 kg/m^3, so to get mass, multiply area times density

            # crate rock
            self.lines.append(rock(mass,area,(randint(minForceRange[0],maxForceRange[0]),randint(minForceRange[1],maxForceRange[1]),randint(minForceRange[2],maxForceRange[2])),initialHeight,doParabolicLines))

        print('calculating lines')
        for i in range(amount):
            self.lines[i].calculateNext()

    def plot(self):
        self.ax = plt.gca(projection='3d')
        for i in range(self.amount):
            self.ax.plot(xs = self.lines[i].x ,ys = self.lines[i].z, zs =  self.lines[i].y, label = 'with drag ' + str(i))

            if self.lines[i].withDrag:
                self.ax.plot(xs = self.lines[i].x_withoutDrag ,ys = self.lines[i].z_withoutDrag, zs =  self.lines[i].y_withoutDrag, label = 'without drag ' + str(i))

        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.show()

    def plotWithWeb(self):
        import streamlit as st 
        plotThingy = st.pyplot(plt)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for i in range(self.amount):
            xs = self.lines[i].x
            ys = self.lines[i].z
            zs = self.lines[i].y
            ax.plot(xs, ys, zs, label=f"line {i} with drag")

            if self.lines[i].withDrag:
                xs = self.lines[i].x_withoutDrag
                ys = self.lines[i].z_withoutDrag
                zs = self.lines[i].y_withoutDrag
                ax.plot(xs, ys, zs, label=f"line {i} without drag")

        ax.set_xlabel('X ')
        ax.set_ylabel('Z ')
        ax.set_ylabel('Y ')
        ax.legend()

        plotThingy.pyplot(plt)

    def plot2D(self):
        import streamlit as st 
        plotThingy = st.pyplot(plt)

        fig = plt.figure()
        ax = fig.add_subplot()

        for i in range(self.amount):
            xs = self.lines[i].x
            ys = self.lines[i].y
            ax.plot(xs, ys, label=f"line {i}")
            if self.lines[i].withDrag:
                xs = self.lines[i].x_withoutDrag
                ys = self.lines[i].y_withoutDrag
                ax.plot(xs, ys, label=f"line {i} without drag")

        ax.set_xlabel('X ')
        ax.set_ylabel('Y ')
        ax.legend()

        plotThingy.pyplot(plt)

    def getSpecialPoints(self, rangeOfSelection: tuple = (0,1)):
        self.maxPoints = []
        self.minPoints = []
        self.totalAirtime = []
        self.airtimeToMaxHeight = []
        self.lastPos = []
        self.distancesTravelled = []
        self.velocitiesWhenChrashed = []
        
        for i in range(rangeOfSelection[0], rangeOfSelection[1]):
            self.maxPoints.append(np.max(self.lines[i].y))
            self.minPoints.append(np.min(self.lines[i].y))

            self.lastPos.append(np.where(self.lines[i].y == self.minPoints[i]))

            self.totalAirtime = np.append(self.totalAirtime,time[self.lastPos[i]])
            self.airtimeToMaxHeight = np.append(self.airtimeToMaxHeight ,time[np.where(self.lines[i].y == self.maxPoints[i])])

            self.distancesTravelled = np.append(self.distancesTravelled, np.sqrt(self.lines[i].x[self.lastPos[i]] ** 2 + self.lines[i].z[self.lastPos[i]] ** 2))

            self.velocitiesWhenChrashed = np.append(self.velocitiesWhenChrashed, self.lines[i].y_acceleration[self.lastPos[i]])
        
        print(tcolour.GREEN + 'special points:')

        print(tcolour.YELLOW + 'max y values (m):' + tcolour.BLUE)
        print(self.maxPoints)

        print(tcolour.YELLOW + 'time untill max y values (max height in s):' + tcolour.BLUE)
        print(self.airtimeToMaxHeight)

        print(tcolour.YELLOW + 'time untill crash (s):' + tcolour.BLUE)
        print(self.totalAirtime)

        print(tcolour.YELLOW + 'distance travelled untill crash (m):' + tcolour.BLUE)
        print(self.distancesTravelled)

        print(tcolour.YELLOW + 'velocity when crashed (m/s):' + tcolour.BLUE)
        print(self.velocitiesWhenChrashed)
        print(tcolour.RESET)