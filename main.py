'''
This work by Alejandro Fernandez del Valle Herrea is licensed under CC BY 4.0 CC

Volcano sim, a code to just have fun, and maybe educate yourself a little bit!
gl hf
'''
import dataCreator

class tcolour:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'
    YELLOW = '\033[93m'
    GRAY = '\033[90m'
    PURPLE = '\033[95m'
    LIGHTBLUE = '\033[96m'
    RESET = '\u001b[0m'

# dataCreator.updateBaseData(newRangeInTime=(0.0,60.0), newDragCoeficient=1) # activar para cambiar variables y jugar con ellas

print(tcolour.LIGHTBLUE + 'creando tiro base' + tcolour.GRAY)
line1 = dataCreator.plotter(amount= 1 , doParabolicLines= True,maxForceRange=(100,100,0),minForceRange=(100,100,0), areaRange=(10,10))

line1.getSpecialPoints()
line1.plot()

print(tcolour.LIGHTBLUE + 'creando serie de tiros aleatorios 2D' + tcolour.GRAY)
data2 = dataCreator.plotter(amount= 10 , doParabolicLines= True,maxForceRange=(200,200,0),minForceRange=(50,50,0), areaRange=(0.01,50))

data2.getSpecialPoints((0,10))
data2.plot()

print(tcolour.LIGHTBLUE + 'creando volcan explotando con 50 tiros' + tcolour.GRAY)
data3 = dataCreator.plotter(amount= 50 , doParabolicLines= False,maxForceRange=(50,200,50),minForceRange=(-50,50,-50), areaRange=(0.01,20))

data3.getSpecialPoints((0,50))
data3.plot()
