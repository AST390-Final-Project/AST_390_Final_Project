#!/usr/bin/env python
# coding: utf-8

# In[232]:


import rebound
import numpy as np
import matplotlib.pyplot as plt


# In[281]:


#unit masses
mass_jupiter  = 1.898e+27 #[kg]
solar_mass    = 1.989e+30 #[kg]
#masses of the solar system HR 8799

#this is the mass of the new solar system and we take it as mass units
mass_unit     = 2.924e+30 #[kg]
mass_star_HR  = 2.924e+30/solar_mass #[solar_mass]

#mass of the planets in [mass_unit] 
b_planet_mass = 7.0 * mass_jupiter/solar_mass #[solar_mass]
c_planet_mass = 8.3 * mass_jupiter/solar_mass #[solar_mass]
d_planet_mass = 8.3 * mass_jupiter/solar_mass #[solar_mass]
e_planet_mass = 9.2 * mass_jupiter/solar_mass #[solar_mass]

#distance
#bas unit = distance from the sun of the system to the first planet which is planet e
b_planet_dist = 68.0  #[Au]
c_planet_dist = 42.9  #[Au]
d_planet_dist = 27.0  #[Au]
e_planet_dist = 16.4  #[Au]

#velocities
b_planet_time = 2*np.pi*b_planet_dist/(164250.0/365.25) #[AU/years]
c_planet_time = 2*np.pi*b_planet_dist/(82145.0/365.25)  #[AU/years]
d_planet_time = 2*np.pi*b_planet_dist/(41054.0/365.25)  #[AU/years]
e_planet_time = 2*np.pi*b_planet_dist/(18000.0/365.25)  #[AU/years]


# In[282]:


#function to set up the simulation
def setup():
    #this is the main simulation
    sim = rebound.Simulation()
    #adding the star and the planets
    
    #cartisian coordinates
    sim.add(m=mass_star_HR)
    sim.add(m=b_planet_mass,x=b_planet_dist,y=0,vy=b_planet_time)
    sim.add(m=c_planet_mass,x=c_planet_dist,y=0,vy=c_planet_time)
    sim.add(m=d_planet_mass,x=d_planet_dist,y=0,vy=d_planet_time)
    sim.add(m=e_planet_mass,x=e_planet_dist,y=0,vy=e_planet_time)
    return sim


# In[283]:


#time for the integration
times = np.linspace(0.,200.0,100)
print(len(times))
#creating a list to save the positions in x and in y

#star
zerox = []
zeroy = []
#first planet
firstx = []
firsty = []
#second planet
secondx = []
secondy = []
#third planet
thirdx = []
thirdy = []

#fourth planet
fourthx = []
fourthy = []

#fifth planet
fifthx = []
fifthy = []

#creating a list to save the eccentricities for the fourth planets
eccs_1   = []
eccs_2   = []
eccs_3   = []
eccs_4   = []


# In[284]:


#we start the simulation
sim = setup()
for i, t in enumerate(times):
    #we run for the timein times
    sim.integrate(t)
    #saving in the list for position in x and position in y
    #saving in the list for eccentricity
    zerox.append(sim.particles[0].x)
    zeroy.append(sim.particles[0].y)
    firstx.append(sim.particles[1].x)
    firsty.append(sim.particles[1].y)
    eccs_1.append(sim.particles[1].e)
    secondx.append(sim.particles[2].x)
    secondy.append(sim.particles[2].y)
    eccs_2.append(sim.particles[2].e)
    thirdx.append(sim.particles[3].x)
    thirdy.append(sim.particles[3].y)
    eccs_3.append(sim.particles[3].e)
    fourthx.append(sim.particles[4].x)
    fourthy.append(sim.particles[4].y)
    eccs_4.append(sim.particles[4].e)
    


# In[285]:


for orbit in sim.calculate_orbits():
    print(orbit)


# In[286]:


fig = rebound.OrbitPlot(sim, unitlabel="[AU]")


# In[287]:


plt.plot(zerox,zeroy)
plt.plot(firstx,firsty)
plt.plot(secondx,secondy)
plt.plot(thirdx,thirdy)
plt.plot(fourthx,fourthy)


# In[ ]:




