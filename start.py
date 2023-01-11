import matplotlib.pyplot as plt
import pandas as pd
import math
## command to install all the packages
## pip3 install -r requirements.txt
## pip freeze > requirements.txt

## run the project 
## python start.py

# importing libraries
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
# C:\Users\lenovo\Desktop\yuhong_thesis\data\sample.xlsx

data = pd.read_excel('data/sample.xlsx')
sensor_values=pd.DataFrame(data, columns=['s1','s2'])
df = pd.DataFrame(data, columns=['s1','s2']).to_numpy()



s1=sensor_values['s1'].to_numpy()
s2=sensor_values['s2'].to_numpy()
print('df',df)

# sensors =df.to_dict('sensor')
print('s1',s1)
print('s2',s2)
# print('sensors',sensors)


def plot(s1,s2,h_min_array):
    print('plot-s1',s1,'plot-s2',s2,'plot-h_min',h_min_array)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = s1
    Y=s2
    Z=h_min_array

    ax.plot(X, Y, Z,color='blue',marker='o', alpha=1)

    ax.set_xlabel('s1')
    ax.set_ylabel('s2')
    ax.set_zlabel('h_min')

    plt.show()
    # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # print('plot',s1,s2,h_min_array)
    # # Make data.
    # X =s1
    # Y =s2
    # X, Y = np.meshgrid(X, Y)
    # h_min= np.array(h_min_array)
    #Z =   np.reshape(h_min,(1, h_min.size))

    # # Plot the surface.
    # # surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
    # #                     linewidth=0, antialiased=False)


    # # Customize the z axis.
    # ax.set_zlim(1,5)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # # A StrMethodFormatter is used automatically

    # ax.zaxis.set_major_formatter('{x:.02f}')

    # # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    # ax.set_xlabel('s1', fontsize=15, rotation=60)
    # ax.set_ylabel('s2', fontsize=15, rotation=60)
    # ax.set_zlabel('hmin', fontsize=15, rotation=60)
    # print('h_min',s1,s2,h_min_array)
    # plt.show()


theta1 = math.pi/4
theta2 = math.pi/4
D=85000
d=80000
a1=5000
a2=5000

def getVariables(s1,s2):
    X_Q = (D/2-(s2-a2))*math.sin(theta2)
    print('X_Q',X_Q)
    X_P = -(D/2-(s1-a1))*math.sin(theta1)
    print('X_P',X_P)
    Y_Q = -X_Q*math.tan(math.pi/2-theta2)
    print('Y_Q',Y_Q)
    Y_P =X_P*math.tan(math.pi/2-theta1)
    print('Y_P',Y_P)
    fi = math.atan((Y_P-Y_Q)/(X_Q-X_P))
    print('fi',fi)
    b= math.sqrt(math.pow((X_P-X_Q),2)+math.pow((Y_P-Y_Q),2)) / 2
    print('b',b)
    # x − This must be a numeric value in the range -1 to 1. If x is greater than 1 then it will generate an error.
    # beta= math.acos(2b/d)
    beta=math.acos(2*b/d)
    print('beta',beta)
    alpha= math.pi/2-fi-beta
    print('alpha',alpha)
    X_O1=X_Q-(d/2)*math.sin(alpha)
    print('X_O1',X_O1)
    Y_O1=Y_Q+(d/2)*math.cos(alpha)
    print('Y_O1',Y_O1)
    h_min=D/2- (math.sqrt(math.pow((X_O1),2)+math.pow((Y_O1),2)))-d/2
    print('h_min',h_min)
    return h_min

def main():
    # variable_s1 = int(input("Enter value for S1: "))
    # variable_s2 = int(input("Enter value for S2: "))

    # print("Hello World!","S1:", s1,"S2",s2)
    h_min_array=[]
    for sensor in df:
        h_min=getVariables(sensor[0],sensor[1])
        h_min_array.append(h_min)
        print('sensor',sensor)
    print('df',df)
    print('h_min',h_min_array)
    plot(s1,s2,h_min_array)








main()
