import math as m

# the computed function
def f(v):
	return 9.8-(0.0001/0.01)*v*v

#initial values	
t=0.0
v=0.0
#h- step
h=0.2
#if you want to change the computed function, you will have to change the value of Eps
Eps=0.00001
print("Runge-Kutta Fehlberg method")
print()
print(f"t= {t}"f"; v= {v}")
while t<10.0:
    f0=f(v)
    f1=f(v+(h/4.0)*f0)
    f2=f(v+(3.0*h/32.0)*f0+(9.0*h/32.0)*f1)
    f3=f(v+(1932.0*h/2197.0)*f0-(7200.0*h/2197.0)*f1+(7296*h/2197.0)*f2)
    f4=f(v+(439.0*h/216.0)*f0-8.0*h*f1+(3680.0*h/513.0)*f2-(845.0*h/4104.0)*f3)
    f5=f(v-(8.0*h/27.0)*f0+2.0*h*f1-(3544.0*h/2565.0)*f2+(1859.0*h/4104.0)*f3-(11.0*h/40.0)*f4)
    Error=m.fabs(h*((f0/360.0)-(128.0*f2/4275.0)-(2197.0*f3/75240.0)+(f4/50.0)+(2.0*f5/55.0)))
    hnew=0.9*h*pow(h*Eps/Error,0.25)
    if Error>(h*Eps):
        print(f"t= {round(t,6 )}" f"; v= {round(v, 6)}" f"; h= {round(h,6)} " " Step is rejected, because h is too large")
    else:
        t=t+h
        v=v+h*((16.0*f0/135.0)+(6656.0*f2/12825.0)+(28561.0*f3/56430.0)-(9.0*f4/50.0)+(2.0*f5/55.0))
        print(f"t= {round(t,6 )}" f"; v= {round(v, 6)}" f"; h= {round(h,6)} ")
    h=hnew
