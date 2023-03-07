from math import *
from numpy import real, imag
'''
A library created to make circuits easier to deal with :)
should work with complex numbers, input them as a+bj
'''

# below are methods commonly used throughout circuit calculations

def series(*Z_list):
    '''calculates series impedances'''
    z_tot = 0
    for z in Z_list:
        z_tot += z
    return z_tot

def parallel(*Z_list):
    '''calculates parallel impedances'''
    z_tot = 0
    for z in Z_list:
        z_tot += 1/z
    return 1/z_tot

def magnitude(a,b):
    '''returns magnitude of a+bj'''
    return sqrt(a**2 + b**2)

def phase(a,b, deg=0):
    '''returns angle of a+bj in Rad by default, for deg use deg=1'''
    if deg != 0:
        return degrees(atan(b/a))
    else:
        return atan(b/a)

def toPhasor(cmplx=0, a=0,b=0, deg=0):
    '''returns a tuple with (magn,phase) for a+bj, use deg=1 for phase in deg, use cmplx= for complex obj, or a=, b='''
    isRect = a !=0 and b !=0
    isCmplx = cmplx != 0
    if deg == 0 and isRect:
        return (magnitude(a,b), phase(a,b))
    elif deg == 1 and isRect:
        return (magnitude(a,b), phase(a,b,deg=1))
    elif deg == 0 and isCmplx:
        return (magnitude(real(cmplx), imag(cmplx)), phase(real(cmplx), imag(cmplx)) )
    elif deg == 1 and isCmplx:
        return (magnitude(real(cmplx), imag(cmplx)) , degrees(phase(real(cmplx), imag(cmplx))) )

def vdiv(src, z_load, *z_list):
    '''returns voltage division of v=src upon impedance z_load with all other series impedances in z_list'''
    z_tot = series(*z_list) + z_load
    return src*(z_load/z_tot)

def idiv(src, z_load, *z_list):
    '''returns current division of I=src upon branch with impedancez_load with other branch impedances in z_list'''
    z_else = parallel(*z_list)
    z_tot = z_else + z_load
    return src*(z_else/z_tot)

def freq(f=0, T=0):
    '''returns angular frequency when you input temporal frequency Hz -> rad/sec, to use period enter T=0'''
    if f != 0:
        return 2*pi*f
    if T != 0:
        return 2*pi/T

def L(w,H):
    '''returns impedance of an Inductor given angular freq and inductance'''
    return 1j*w*H

def C(w,c):
    '''returns impedance of a Capacitor given angular freq and capacitance'''
    return -1j/(w*c)

class Amplifier():
    '''A class to define an STC amplifier.'''
    def __init__(self, Ri, amp_factor, Ro, type="voltage", src:tuple=None):
        '''creates an equivalent voltage amplifier of some following type: 'voltage', 'current', 'transresistance', or 'transconductance' with given constructor args'''
        self.src = src
        self.Ri = Ri
        self.Ro = Ro
        self.type = type
        if type == "voltage":
            self.A = amp_factor
        if type == "current":
            self.A = amp_factor*(self.Ro/self.Ri)
        if type == "transresistance":
            self.A = amp_factor/self.Ri
        if type == "transconductance":
            self.A = amp_factor*self.Ro
        
    def output(self) -> tuple:
        '''Returns the amplifier's output as a tuple representing a thevenin equivalent.''' 
        Vs = self.src[0]
        Rs = self.src[1]
        Vi = vdiv(Vs, self.Ri, Rs)
        return (self.A*Vi, self.Ro)