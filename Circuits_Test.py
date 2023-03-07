from Circuits import *

signal = (0.030, 50_000)

a1 = Amplifier(750_000, 0.006, 1_000, type="transconductance", src=signal)
a2 = Amplifier(6_000, 900, 1_000, type="current", src=a1.output())

Vth = a1.output()[0]
Rth = a1.output()[1]
Rl = 6_000

print(Vth/(Rth + Rl))

Vth = a2.output()[0]
Rth = a2.output()[1]
Rl = 6_000

print(f'i_o = {Vth/(Rth + Rl)}')
print(f'v_o = {vdiv(Vth, Rl, Rth)}')

Vin = 0.030
Iin = 0.030/(750_000 + 50_000)
Pin = Vin*Iin

Vout = vdiv(Vth, Rl, Rth)
Iout = Vth/(Rth + Rl)
Pout = Vout*Iout

Gi = gain_vi(Iin, Iout, db=True)
Gv = gain_vi(Vin, Vout, db=True)
Gp = gain_power(Pin, Pout, db=True)

print(Gv)
print(Gi)
print(Gp)

