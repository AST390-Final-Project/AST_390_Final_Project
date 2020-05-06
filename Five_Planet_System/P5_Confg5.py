#!/usr/bin/env python
# coding: utf-8

# In[15]:


import rebound
import numpy as np
import matplotlib.pyplot as plt


# In[16]:


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
new_planet_mass = 0.211 * mass_jupiter/solar_mass #[solar_mass]  #NEW PLANET 

#distance
#bas unit = distance from the sun of the system to the first planet which is planet e
b_planet_dist = 68.0  #[Au]
c_planet_dist = 42.9  #[Au]
d_planet_dist = 27.0  #[Au]
e_planet_dist = 16.4  #[Au]
new_planet_dist = 410.0 #[Au]  #NEW PLANET


# In[17]:


def setup():
    #this is the main simulation
    sim = rebound.Simulation()
    #adding the star and the planets
    
    #cartisian coordinates
    sim.add(m=mass_star_HR)
    sim.add(m=b_planet_mass,a = b_planet_dist,e= 0.008)#x=b_planet_dist,y=0,vy=b_planet_time)
    sim.add(m=c_planet_mass,a = c_planet_dist,e= 0.012)#x=c_planet_dist,y=0,vy=c_planet_time)
    sim.add(m=d_planet_mass,a = d_planet_dist,e= 0.1)#x=d_planet_dist,y=0,vy=d_planet_time)
    sim.add(m=e_planet_mass,a = e_planet_dist,e= 0.008)#x=e_planet_dist,y=0,vy=e_planet_time)
    sim.add(m=new_planet_mass,a = new_planet_dist,e= 0.4)#x=new_planet_dist,y=0,vy=newplanet_time) #NEW PLANET
    #sim.add(m=e_planet_mass,a = e_planet_dist*1.5,e= 0.008)
    return sim


# In[27]:


#time for the integration
times = np.linspace(0.,2*3000*np.pi,1000)
print(len(times))
#creating a list to save the positions in x and in y


# In[28]:


x = np.zeros((len(times),6))
y = np.zeros((len(times),6))
ecc = np.zeros((len(times),6))


# In[63]:


#we start the simulation
sim = setup()
sim.integrator = "ias15"
sim.move_to_com()
for i, t in enumerate(times):
    #we run for the timein times
    sim.integrate(t)
    
    
    x[i,0] = sim.particles[0].x
    y[i,0] = sim.particles[0].y

    x[i,1] = sim.particles[1].x
    y[i,1] = sim.particles[1].y    
    ecc[i,1] = sim.particles[1].e
    x[i,2] = sim.particles[2].x
    y[i,2] = sim.particles[2].y
    ecc[i,2] = sim.particles[2].e
    x[i,3] = sim.particles[3].x
    y[i,3] = sim.particles[3].y
    ecc[i,3] = sim.particles[3].e
    x[i,4] = sim.particles[4].x
    y[i,4] = sim.particles[4].y
    ecc[i,4] = sim.particles[4].e
    x[i,5] = sim.particles[5].x
    y[i,5] = sim.particles[5].y
    ecc[i,5] = sim.particles[5].e


# In[64]:


for orbit in sim.calculate_orbits():
    print(orbit)
    
fig = rebound.OrbitPlot(sim, unitlabel="[AU]")


# In[89]:


#plot all orbits
plt.plot(x,y)
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')


# In[105]:


#print an individual orbit

list_x = []
list_y = []
n = 1
for i, t in enumerate(times):
    list_x.append(x[i][n])
    list_y.append(y[i][n])
plt.plot(list_x,list_y)
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')
plt.title('eccentricity of {}'.format(n))


# In[106]:


#print all eccentricities vs time
ecc_1 = []
n = 1
for i, t in enumerate(times):
    ecc_1.append(ecc[i][n])
plt.plot(times,ecc_1)
plt.xlabel('time [yr/4pi]')
plt.ylabel('eccentricity of {}')
plt.title('eccentricity vs time of planet {}'.format(n))


# In[107]:


#print all eccentricities vs time
plt.plot(times,ecc)
plt.xlim(0,12500)
plt.ylim(0,0.6)
plt.xlabel('time [yr/4pi]')
plt.ylabel('eccentricity')


# In[ ]:




