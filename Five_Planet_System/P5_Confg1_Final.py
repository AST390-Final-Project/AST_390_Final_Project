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
new_planet_mass = 0.00031 * mass_jupiter/solar_mass #[solar_mass]  #NEW PLANET 

#distance
#bas unit = distance from the sun of the system to the first planet which is planet e
b_planet_dist = 68.0  #[Au]
c_planet_dist = 42.9  #[Au]
d_planet_dist = 27.0  #[Au]
e_planet_dist = 16.4  #[Au]
new_planet_dist = 8.0 #[Au]  #NEW PLANET

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
    sim.add(m=new_planet_mass,a = new_planet_dist,e= 0.01)#x=new_planet_dist,y=0,vy=newplanet_time) #NEW PLANET
    #sim.add(m=e_planet_mass,a = e_planet_dist*1.5,e= 0.008)
    return sim
    
#time for the integration
for j in range(0,10000,1000):
    
    times = np.linspace(0.,2*j*np.pi,1000)
    print(len(times))
    print(j)
    #creating a list to save the positions in x and in y

    x = np.zeros((6,len(times)))
    y = np.zeros((6,len(times)))
    ecc = np.zeros((6,len(times)))

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
        x[5][i] = sim.particles[5].x
        y[5][i] = sim.particles[5].y
        ecc[5][i] = sim.particles[5].e
        
    for orbit in sim.calculate_orbits():
        print(orbit)
    
    fig = rebound.OrbitPlot(sim, unitlabel="[AU]")
    
# For eccentricity and orbit plots
times = np.linspace(0.,2*10000*np.pi,1000) 
print(len(times))
#creating a list to save the positions in x and in y

x = np.zeros((6,len(times)))
y = np.zeros((6,len(times)))
ecc = np.zeros((6,len(times)))

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
    x[5][i] = sim.particles[5].x
    y[5][i] = sim.particles[5].y
    ecc[5][i] = sim.particles[5].e

for orbit in sim.calculate_orbits():
    print(orbit)

for i in range(6):
    plt.plot(x[i],y[i])
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')


plt.plot(x[0],y[0])
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')


plt.plot(x[1],y[1],color = 'darkorange')
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')


plt.plot(x[2],y[2],color = 'green')
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')


plt.plot(x[3],y[3],color = 'red')
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')


plt.plot(x[4],y[4],color = 'mediumpurple')
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')


plt.plot(x[5],y[5], color = 'sienna')
plt.xlabel('Position in x [AU]')
plt.ylabel('Position in y [AU]')



#print all eccentricities vs time
for i in range(6):
    plt.plot(times,ecc[i])
plt.xlim(0,12500)
plt.ylim(0,0.6)
plt.xlabel('time [yr/4pi]')
plt.ylabel('eccentricity')



#print all eccentricities vs time
plt.plot(times,ecc[1], color = 'darkorange')
plt.xlabel('time [yr/4pi]')
plt.ylabel('eccentricity of {}')
plt.title('eccentricity vs time of planet {}'.format(1))

plt.plot(times,ecc[2],color = 'green')
plt.xlabel('time [yr/4pi]')
plt.ylabel('eccentricity of {}')
plt.title('eccentricity vs time of planet {}'.format(2))

plt.plot(times,ecc[3],color = 'red')
plt.xlabel('time [yr/4pi]')
plt.ylabel('eccentricity of {}')
plt.title('eccentricity vs time of planet {}'.format(3))


plt.plot(times,ecc[4],color = 'mediumpurple')
plt.xlabel('time [yr/4pi]')
plt.ylabel('eccentricity of {}')
plt.title('eccentricity vs time of planet {}'.format(4))

plt.plot(times,ecc[5],color = 'sienna')
plt.xlabel('time [yr/4pi]')
plt.ylabel('eccentricity of {}')
plt.title('eccentricity vs time of planet {}'.format(5))




