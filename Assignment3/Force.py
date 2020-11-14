import numpy as np 
import time

def force_per_particle_sort(xs):
    F = np.zeros(len(xs))    
    sortedIndices = np.argsort(xs)    
    for  newIndex,originalIndex in enumerate(sortedIndices):
        
        F[originalIndex] = (len(xs) - newIndex -1) - (newIndex)
        
    return F


N = 10001
t = 200
dt = 0.0005



xs = np.linspace(-np.pi/2,np.pi/2,N)

As = force_per_particle_sort(xs)

vs = -0.001 * np.sin(xs)



ts = np.arange(t/dt)


run = True

if run:
    start = time.time()
    x_ = []
    v_ = []
    for t in ts:
        
        print(t/ts[-1]*100," complete")
        
        xs = xs + vs * dt + .5 * As * dt **2

        As_new = force_per_particle_sort(xs)

        vs = vs + .5 * (As + As_new) * dt

        As = As_new

        #if np.isin(t,[0,18,25,40,132,200]):

        x_.append(xs)

        v_.append(vs)
            
    np.savetxt(f"x_N{N}_t{t}_dt{dt}.txt",x_)
    np.savetxt(f"v_N{N}_t{t}_dt{dt}.txt",v_)

    print(f"Time {time.time() - start}")    