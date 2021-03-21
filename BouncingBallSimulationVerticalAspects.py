import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

h0 = 5         # m/s
v = 12.4          # m/s, current velocity
# for velocity:
    # use -ve velocity if the ball is thrown down
    # use +ve velocity if the ball is thrown up
    # use 0 if ball is just dropped 

g = 9.8         # m/s/s --- gravity 10 or 9.8
t = 0          # starting time
dt = 0.05     # time step
rho = 0.70     # coefficient of restitution
tau = 0.001     # contact time for bounce
theta = 90      # angle between projectile vector and ground, in our case it is 90    
hmax = h0 + (v**2)*np.sin(np.radians(theta)) / (2*g) # track the maximum height
# np.radians(90) , since 90 is in degrees , 
# we convert it to radians since np.sin takes assumes input is in radians
vmax = np.sqrt(2 * hmax * g)

h = h0
hstop = 0.001   # stop when bounce is less than certain centimeters 
freefall = True # state: freefall or in contact with the ground

if v<0 or v>0 :
    # Using the equations of motion here we use this because inital velocity is not zero
    t_last = -(vmax - v)/g 
else:    
    # here because initial velocity is zero we can set ut to zero
    t_last = -np.sqrt(2*hmax/g) # time we would have launched to get to h0 at t=0


H = [h]
T = [t]

def bouncing_ball(i):
    global hmax,hstop,freefall,v,dt,g,vmax,tau,rho,T,H,h,t,t_last
    if (hmax > hstop):
        if(freefall):            
            hnew = h + v*dt - 0.5*g*dt*dt
            if (hnew<0):
                t = t_last + 2*np.sqrt(2*hmax/g)
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

