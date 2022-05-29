#the computed function
def f(y):
    return y*y+1.0	
h=float(input("Enter the step 'h': "))	
N=int(1.00/h)
#Modified Euler
print("Modified Euler:")
x0=0.0
y0=0.0
print(f"x0= {x0}" f"; y0= {y0}")
i=0
while i < N:
    i=i+1
    f0=f(y0)
    yMid=y0+(h/2.0)*f0
    fMid=f(yMid)
    y0=y0+h*fMid
    x0=x0+h
    print(f"x0= {round(x0,2)}" f"; y0= {round(y0, 6)}")
print()

#Improved Euler
print("Improved Euler:")
x0=0.0
y0=0.0
print(f"x0= {x0}" f"; y0= {y0}")
j=0
while j< N:
    j+=1
    f0=f(y0)
    y0=y0+(h/2.0)*(f0+f(y0+h*f0))
    x0=x0+h
    print(f"x0= {round(x0,2)}" f"; y0= {round(y0, 6)}")
print()
#Fourth-order Runge-Kutta
print("Fourth-order Runge-Kutta:")
x0=0.0
y0=0.0
print(f"x0= {round(x0,2)}" f"; y0= {round(y0, 6)}")
k=0
while k<N:
    k+=1
    f0=f(y0)
    f1=f(y0+(h/2.0)*f0)
    f2=f(y0+(h/2.0)*f1)
    f3=f(y0+h*f2)
    y0=y0+(h/6.0)*(f0+2.0*f1+2.0*f2+f3)
    x0=x0+h
    print(f"x0= {round(x0,2)}" f"; y0= {round(y0, 6)}")
