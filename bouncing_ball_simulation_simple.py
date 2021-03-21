import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

h0 = 5         # m/s
v = 0          # m/s, current velocity
g = 10         # m/s/s
t = 0          # starting time
dt = 0.05     # time step
rho = 0.90     # coefficient of restitution
tau = 0.001     # contact time for bounce
hmax = h0      # keep track of the maximum height
h = h0
hstop = 0.001   # stop when bounce is less than 1 cm
freefall = True # state: freefall or in contact with the ground
t_last = -np.sqrt(2*h0/g) # time we would have launched to get to h0 at t=0
vmax = np.sqrt(2 * hmax * g)
H = [h]
T = [t]

def bouncing_ball(i):
    global hmax,hstop,freefall,v,dt,g,t_last,vmax,tau,rho,T,H,h,t
    if (hmax > hstop):
        if(freefall):
            hnew = h + v*dt - 0.5*g*dt*dt
            if(hnew<0):
                t = t_last + 2*np.sqrt(2*hmax/g)
                print(v,t,t_last,2*np.sqrt(2*hmax/g),hmax)
                freefall = False
                t_last = t + tau
                h = 0
            else:
                t = t + dt
                v = v - g*dt
                h = hnew
        else:
            t = t + tau
            vmax = vmax * rho
            v = vmax
            freefall = True
            h = 0
        hmax = 0.5*vmax*vmax/g
        H.append(h)
        T.append(t)

        plt.cla()

        plt.plot(T,H)
        plt.plot(T[-1],H[-1],'ro')
        plt.tight_layout()
        
    else:
        return
    
ani = FuncAnimation(plt.gcf() ,bouncing_ball , interval=1)
plt.show()

