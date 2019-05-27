import numpy as np
import pylab as plt
from PyAstronomy.pyasl import foldAt


def Msun2kg(m):
    return m*1.9891e30
def Mjup2kg(m):
    return m*1.898e27
def Mearth2Mjup(m):
    return m*5.972e24/1.898e27
def day2sec(t):
    return t*24*60*60.

def semi_amp(P,Ms,Mp,inc,e):
    G=6.67e-11
    P=day2sec(P)
    return (2*np.pi*G/(P*Msun2kg(Ms)**2))**(1./3)*Mjup2kg(Mearth2Mjup(Mp))*np.sin(inc)/np.sqrt(1-e*e) # m/s

def ecc_anom(t,omega,ecc):
    '''t (BJD), omega (rad)'''
    omega=np.deg2rad(450.)-omega # translate by 1.25 circles; get rid of negative values)
    e0=np.arctan2(np.sqrt(1-ecc*ecc)*np.sin(omega),ecc+np.cos(omega))
    fma0=e0-ecc*np.sin(e0)
    E=np.zeros(len(t))
    for i in range(len(t)):
        phase=2*np.pi*t[i]
        fma=phase+fma0
        ee=fma+ecc*np.sin(fma)
        for j in range(15):
            denom=1.-ecc*np.cos(ee)
            disc=fma - ee + ecc*np.sin(ee)
            ee+=disc/denom
            if (np.abs(disc) < 2e-15):
                break
        E[i]=ee
    return E

def true_anom(ecc,E):
    return 2.*np.arctan(np.sqrt((1.+ecc)/(1.-ecc))*np.tan(E/2.))

def RV(t,theta):
    '''P (days), T0 (BJD), V (m/s), K (m/s), 
    h=sqrt(ecc)cos(omega), k=sqrt(ecc)sin(omega)'''
    P,T0,V,K,h,k=theta
    # Compute phase
    t=(t-T0)/P
    # Sanity check
    if np.any(np.isinf(t)):
	return np.zeros(t.size)
    # Compute eccentricity and argument of periapsis
    ecc=h*h+k*k
    omega=np.arctan2(k,h)
    # Solve Kepler's equation
    E=ecc_anom(t,omega,ecc)
    # Compute true anomaly
    nu=true_anom(ecc,E)
    # Return RV timeseries
    return nu, V+K*(ecc*np.cos(omega)+np.cos(nu+omega)) # m/s


if __name__ == '__main__':
    T0=2459234.4
    P=8.159
    V=0.
    ecc=0.1
    omega=np.deg2rad(45.)
    h=np.sqrt(ecc)*np.cos(omega)
    k=np.sqrt(ecc)*np.sin(omega)
    K=1.5
    theta=(P,T0,V,K,h,k)

    N=50
    t=np.linspace(T0,T0+200,N)*np.random.normal(1,1e-3,N)
    t=np.sort(t)

    rv=RV(t,theta)

    phase=foldAt(t,P,T0=T0)

    plt.plot(phase,rv,'ko')
    plt.show()
