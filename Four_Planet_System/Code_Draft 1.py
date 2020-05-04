#!/usr/bin/env python
# coding: utf-8

# In[85]:


import rebound
import numpy as np
import matplotlib.pyplot as plt
##using pylab might be better for analyzing the stats (Thats what was used in video)


# In[131]:


#unit masses in kg
mass_jupyter  = 1.898e+27    
solar_mass    = 1.989e+30    
#masses of the solar system HR 8799
mass_unit     = 2.924e+30
mass_star_HR  = 2.924e+30/solar_mass
b_planet_mass = 7.0 * mass_jupyter/mass_unit
c_planet_mass = 8.3 * mass_jupyter/mass_unit
d_planet_mass = 8.3 * mass_jupyter/mass_unit
e_planet_mass = 9.2 * mass_jupyter/mass_unit

base_unit     = 16.4 
b_planet_dist = 68.0 / base_unit
c_planet_dist = 42.9 / base_unit
d_planet_dist = 27.0 / base_unit
e_planet_dist = 16.4 / base_unit
#velocities
b_planet_time = 164250.0
c_planet_time = 82145.0
d_planet_time = 41054.0
e_planet_time = 18000.0


# In[158]:


#function to set up the simulation
def setup():
    sim = rebound.Simulation()
    sim.add(m=solar_mass)
    sim.add(m=b_planet_mass,a=b_planet_dist)
    sim.add(m=c_planet_mass,a=c_planet_dist)
    sim.add(m=d_planet_mass,a=d_planet_dist)
    sim.add(m=e_planet_mass,a=e_planet_dist)
    return sim


# In[159]:


times = np.linspace(0.,500.0,10)
eccsx  = np.zeros((len(times),4))
eccsy  = np.zeros((len(times),4))
eccs   = np.zeros((len(times),4))


# In[160]:


sim = setup()
for i, t in enumerate(times):
    sim.integrate(t)
    eccsy[i,0] = sim.particles[1].x
    eccsy[i,0] = sim.particles[1].y
    eccs[i,0] = sim.particles[1].e
    eccsx[i,1] = sim.particles[2].x
    eccsy[i,1] = sim.particles[2].y
    eccs[i,1] = sim.particles[2].e
    eccsx[i,2] = sim.particles[3].x
    eccsy[i,2] = sim.particles[3].y
    eccs[i,2] = sim.particles[3].e
    eccsx[i,3] = sim.particles[4].x
    eccsy[i,3] = sim.particles[4].y
    eccs[i,3] = sim.particles[4].e


# In[161]:


plt.plot(eccsx[0],eccsy[0])
plt.plot(eccsx[1],eccsy[1])
plt.plot(eccsx[2],eccsy[2])
plt.plot(eccsx[3],eccsy[3])


# In[176]:


#plt.plot(times, eccs)
eccs


# In[169]:


times


# In[ ]:




