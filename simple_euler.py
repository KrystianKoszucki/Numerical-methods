#the computed function
def f(y):
    return y*y+1.0

h=float(input("Enter the step 'h': "))	
N=int(1.00001/h)
#initial values
x0=0.0
y0=0.0
print(f"x0= {round(x0, 2)}" f"; y0= {round(y0, 6)}")

i=0
while i < N:
    i=i+1
    f0=f(y0)
    x0=x0+h
    y0=y0+h*f0
    print(f"x0= {round(x0, 2)}" f"; y0= {round(y0, 6)}")
