import matplotlib.pyplot as plt
import pandas as pd
import math
## command to install all the packages
## pip3 install -r requirements.txt
## pip freeze > requirements.txt

from matplotlib.animation import FuncAnimation

from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from matplotlib import animation

data = pd.read_excel('data/sample.xlsx')
sensor_values=pd.DataFrame(data, columns=['s1','s2'])
df = pd.DataFrame(data, columns=['s1','s2']).to_numpy()



s1=sensor_values['s1'].to_numpy()
s2=sensor_values['s2'].to_numpy()
print('df',df)

print('s1',s1)
print('s2',s2)


# def plot(s1,s2,h_min_array):
#     print('plot-s1',s1,'plot-s2',s2,'plot-h_min',h_min_array)
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     X = s1
#     Y=s2
#     Z=h_min_array

#     ax.plot(X, Y, Z,color='blue',marker='o', alpha=1)

#     ax.set_xlabel('s1')
#     ax.set_ylabel('s2')
#     ax.set_zlabel('h_min')

#     plt.show()
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



def animationPlot(s1,h_min_array):

    fig = plt.figure(figsize=(12,8))
    axes = fig.add_subplot(1,1,1)
    # axes.set_ylim(230, 2500)
    # axes.set_xlim(0, 10)
    axes.set_title('Changes of h_min based on time', fontsize=20)

    y1= h_min_array
    # t= [0,1, 2, 3, 4, 5, 6,7] 
    t=np.arange(0,s1.size,1)
    print('t',t)
    x,y = [], []

    def animate(i):
        x.append(t[i])
        y.append((y1[i]))
        plt.plot(x,y, scaley=True, scalex=True, label='change of h_min',color="blue",marker='o')


    

    ani = FuncAnimation(fig=fig, func=animate, interval=700)

    plt.show()







# Eingangsgroesse sind wie folgt definiert:
theta1 = math.pi/4
theta2 = math.pi/4
# D in Einheit um
D=85000
# d in Einheit um
d=80000

# a1 und a2 sollen am Pruefstand gemessen werden, da nicht mehr moeglich ist, werden here jeweils 5000 um eingegeben.
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

    h_min_array=[]
    for sensor in df:
        h_min=getVariables(sensor[0],sensor[1])
        h_min_array.append(h_min)
        print('sensor',sensor)
    print('df',df)
    print('h_min',h_min_array)
        # plot(s1,s2,h_min_array)
    animationPlot(s1,h_min_array)
    






main()
