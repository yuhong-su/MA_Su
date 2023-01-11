# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation


# # First set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 10), ylim=(0, 1000))
# line, = ax.plot([], [], lw=2)


# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,

# # animation function.  This is called sequentially
# def animate(i):
#     x = np.linspace(0, 2, 1000)
#     print('x',x)
#     # x=[0,1,2,3,4,5,6,7]
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     print('y',y)
#     line.set_data(x, y)
#     return line,

# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)



# plt.show()




# x_data=[]
# y_data=[]
# fig, ax  =plt.subplot()
# ax.set_xlim(0,105)
# ax.set_ylim(0,12)

# line,=ax.plot(0,0)

# def animation_frame(i):
#     x_data.append(i*10)
#     y_data.append(i)

#     line.set_xdata(x_data)
#     line.set_ydata(y_data)

# animation = FuncAnimation(fig, func=animation_frame,frames=np.arange(0,10,0.01),interval=10)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# fig, ax = plt.subplots()

# x = []
# y=[]
# line, = ax.plot(x,y)


# def animate(i):
#     # x = [0,1,2,3,4,5,6,7]
#     # y=[930,930,906,670,2494,1445,1541,238]
#     x.append(i*10)
#     y.append(i)
#     line.set_xdata(x)
#     line.set_ydata(y)  # update the data.
#     return line,


# ani = animation.FuncAnimation(
#     fig, animate, interval=200, blit=True)



# plt.show()




from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



fig = plt.figure(figsize=(12,8))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(230, 2500)
axes.set_xlim(0, 10)
y1= [930,930,906,670,2494,1445,1541,238] 
t= [0,1, 2, 3, 4, 5, 6,7] 
x,y = [], []


def animate(i):
    x.append(t[i])
    y.append((y1[i]))
    plt.plot(x,y, scaley=True, scalex=True, color="blue")

ani = FuncAnimation(fig=fig, func=animate, interval=1000)

plt.show()