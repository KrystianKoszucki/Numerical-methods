#the computed function
def f(y):
	return y*y+1.0

#step
h=float(input("Enter h:"))
N=int(1.00001/h)
print("Adams-Bashforth second order:")
#the initial values
x0=0.0
y0=0.0
f0=f(y0)
print(f"x= {round(x0, 2)} " f"; y= {round(y0, 6)}")
#First point obtained by RK2=Runge-Kutta 2nd order
x1=x0+h
y1=y0+h*f(y0+(h/2.0)*f0)
f1=f(y1)
print(f"x= {round(x1, 2)} " f"; y= {round(y1)}")
#Next points obtained by AB2= Adams Bashforth 2nd order
i=2
while i < N:
    i+=1
    f1=f(y1)
    f0=f(y0)
    xNew=x1+h
    yNew=y1+(h/2.0)*(3.0*f1-f0)
    print(f"x= {round(xNew, 2)}" f"; y= {round(yNew, 6)}")
    if i<N:
        f0=f1
        f1=f(yNew)
        x1=xNew
        y1=yNew
print()
print("Adams-Bashforth fourth order:")
x0=0.0
y0=0.0
print(f"x= {round(x0, 2)}" f" ; y= {round(y0, 6)}")

#First point obtained by RK4
f0=f(y0)
f1=f(y0+(h/2.0)*f0)
f2=f(y0+(h/2.0)*f1)
f3=f(y0+h*f2)
x1=x0+h
y1=y0+(h/6.0)*(f0+2.0*f1+2.0*f2+f3)
print(f"x= {round(x1, 2)}" f"; y= {round(y1, 6)}")

#Second point obtained by RK4
f0=f(y1)
f1=f(y1+(h/2.0)*f0)
f2=f(y1+(h/2.0)*f1)
f3=f(y1+h*f2)
x2=x1+h
y2=y1+(h/6.0)*(f0+2.0*f1+2.0*f2+f3)
print(f"x= {round(x2, 2)}" f" ; y= {round(y2, 6)}")
#Third point obtained by RK4
f0=f(y2)
f1=f(y2+(h/2.0)*f0)
f2=f(y2+(h/2.0)*f1)
f3=f(y2+h*f2)
x3=x2+h
y3=y2+(h/6.0)*(f0+2.0*f1+2.0*f2+f3)
print(f"x= {round(x3, 2)}"f" ; y= {round(y3, 6)}")
	
#Initial f values
f0=f(y0)
f1=f(y1)
f2=f(y2)
f3=f(y3)

#Next points obtained by AB4
j=4
while j <N:
    j+=1
    xNew=x3+h
    yNew=y3+(h/24.0)*(55.0*f3-59.0*f2+37.0*f1-9.0*f0)
    print(f"x= {round(xNew, 2)}" f"; y= {round(yNew,6)}")
    if j<N:
        f0=f1
        f1=f2
        f2=f3
        f3=f(yNew)
        x3=xNew
        y3=yNew
