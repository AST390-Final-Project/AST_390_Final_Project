import rebound
import numpy as np
import matplotlib.pyplot as plt

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
    #sim.add(m=e_planet_mass,a = e_planet_dist*1.5,e= 0.008)
    return sim
    
times = np.linspace(0.,2*np.pi*3000000,4000)
print(len(times))

#creating a list to save the positions in x and in y

x = np.zeros((5,len(times)))
y = np.zeros((5,len(times)))
ecc = np.zeros((5,len(times)))

sim = setup()
sim.integrator = "ias15"
sim.move_to_com()
for i, t in enumerate(times):
    #we run for the timein times
    sim.integrate(t)
    
    x[0][i] = sim.particles[0].x
    y[0][i] = sim.particles[0].y

    x[1][i] = sim.particles[1].x
    y[1][i] = sim.particles[1].y    
    ecc[1][i] = sim.particles[1].e
    x[2][i] = sim.particles[2].x
    y[2][i] = sim.particles[2].y
    ecc[2][i] = sim.particles[2].e
    x[3][i] = sim.particles[3].x
    y[3][i] = sim.particles[3].y
    ecc[3][i] = sim.particles[3].e
    x[4][i] = sim.particles[4].x
    y[4][i] = sim.particles[4].y
    ecc[4][i] = sim.particles[4].e
        
for orbit in sim.calculate_orbits():
    print(orbit)
    
    
plt.ylim(-1500, 1500)
plt.xlim(-1500, 1500)
plt.plot(x[0],y[0])
plt.plot(x[1],y[1])
plt.plot(x[2],y[2])
plt.plot(x[3],y[3])
plt.plot(x[4],y[4])
plt.plot(x[5],y[5])
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')


plt.plot(times,y[0])
plt.plot(times,y[1])
plt.plot(times,y[2])
plt.plot(times,y[3])
plt.plot(times,y[4])
plt.plot(times,y[5])

plt.xlabel('time [yr*2pi]')
plt.ylabel('y postion of planet [AU]')