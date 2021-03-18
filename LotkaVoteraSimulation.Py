import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class LotkaVolterraSim():
    def __init__(self,b,p,d,r,t0,dt,t_interval):
        '''
        params : 
        b - birth rate of prey
        p - predation rate 'of' prey(rate at which prey are being eaten by predator)
        d - death rate of predators
        r - predation rate 'on' prey(rate at which predator is eating prey)
        X - array containing prey and predator population to be used 
        t0 - initial time
        dt - timestep
        t_interval - timestep to use for plots
        '''
        
        self.b = float(b)
        self.p = float(p)
        self.d = float(d)
        self.r = float(r)
        self.t0 = t0
        self.dt = dt
        self.t_interval = t_interval
        
        
    def LotkaVolterra(self,X,b,p,d,r):
        return np.array([b*X[0] - p*X[0]*X[1] , r*X[0]*X[1]-d*X[1]])
    
    def runge(self,i):
        
        f1 = self.dt * self.f(self.time_[i],self.y_list[i])
        f2 = self.dt * self.f(self.time_[i] + self.dt/2 , self.y_list[i]+f1/2)
        f3 = self.dt * self.f(self.time_[i] + self.dt/2 , self.y_list[i]+f2/2)
        f4 = self.dt * self.f(self.time_[i] + self.dt , f3)

        y = self.y_list[i] + (f1 + 2*f2 + 2*f3 +f4)/6
        
        self.prey_list.append(y[0])
        self.pred_list.append(y[1])
        
        self.time_.append(self.time_[i] + self.dt)
        self.y_list.append(y)
        
        plt.cla()

        plt.plot(self.time_,self.prey_list, label = "Prey")
        plt.plot(self.time_,self.pred_list , label = "Predator")
        plt.legend(loc='upper left')
        plt.title("b: "+str(self.b)+", p: "+str(self.p)+", d: "+str(self.d)+", r: "+str(self.r))

        


    def simulation_execution(self,prey0,pred0):
        self.f = lambda t,x : self.LotkaVolterra(x,self.b,self.p,self.d,self.r)

        y = np.array([prey0,pred0])
        self.time_ =  [self.t0] # store/hold time values after each time step but start with the initial
        self.y_list = [y] # store/hold prey-predator array values after each time step but start with the initial
        self.prey_list = [y[0]] # store/hold prey values
        self.pred_list = [y[1]] # store/hold predator values

        self.anime = FuncAnimation(plt.gcf(), self.runge , interval= self.t_interval)
        
        plt.show()
    

prey_predator  = LotkaVolterraSim(1, 1, 1, 1, 0, 0.1, 1)
prey_predator.simulation_execution(0.5,0.5) # for this case 0.5 is the population density per unit area