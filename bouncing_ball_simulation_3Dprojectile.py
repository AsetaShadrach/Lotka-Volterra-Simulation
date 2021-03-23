import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.axes3d import Axes3D as p3

h0  = 5 # initial height
v = 5.0 # velocity
angle = 70
vel = np.cos(np.radians(angle))*v # horizontal velocity
g = 9.8
dt = 0.01
t = 0
rho = 0.90
hstop=0.001
hmax = h0 + (v**2)*np.sin(np.radians(angle)) / (2*g)
x = vel*t # horizontal displacement
t_ =[]
x_ = []
y_ =[]
vmax = np.sqrt(2 * hmax * g)

def bouncing_ball(i):
  global hmax, hstop, v, dt, g, rho, t, vel, h0, angle, t_, x_, y_, vmax
  if (hmax > hstop):
    x = round(vel*t,5) # horizontal distance round it just incase x is too small : approaches zero
    y = h0 + x*np.tan(np.radians(angle)) - (g*x**2 )/(2 * (v**2) * np.cos(np.radians(angle))**2)

    if angle == 90: # when angle is 90
      y = h0 + v*dt - 0.5*g*dt*dt
      v = v - g*dt
      h0 = y
    
    if y<0.0:
      h0 = 0
      vmax = vmax * rho
      v= vmax
      t = 0
      y = 0
      
      if abs(vel)/abs(v)<1:
        angle = 90 - np.degrees(np.arcsin(abs(vel)/abs(v)))
      vel = np.cos(np.radians(angle))*v
      

    if len(t_)<1:
      t_.append(t)
      x_.append(x)
    else:
      t_.append(t_[-1]+dt)
      x_.append(x_[-1]+x)    
    
    y_.append(y)
    t = t+dt
    hmax = (vmax**2)*np.sin(np.radians(angle)) / (2*g)
    

    plt.cla()
    plot_fig.plot(x_,t_,y_)
    plot_fig.set_xlabel('Horizontal Distance')
    plot_fig.set_ylabel('Time')
    plot_fig.set_zlabel('Height')
    plot_fig.plot(x_[-1:],t_[-1:],y_[-1:],'ro') # use list range not singular points to avoid 
                                                # 'numpy.float64' has no len()'  error
    #plt.tight_layout()
    
  else:
    return
    
plot_fig = p3(plt.figure())

ani = FuncAnimation(plt.gcf() ,bouncing_ball , interval=1)
plt.show()

 