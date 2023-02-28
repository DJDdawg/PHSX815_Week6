#import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sys

#Create Numerical Integration Functions
def leftriemann(f, a, b, N):
    AtotL = 0 #initialize area under curve
    a = float(a) #lower bound of interval
    b = float(b) #upper bound of interval
    N = float(N) #number of rectangles used in approximation
    dx = (b-a)/N #equal step size (width) for each rectangle
    
    #set bounds
    xoL = a #First rectangle has left edge at x = a
    xfL = a + (N-1) * dx #Final rectangle has edge at x = b - dx = a + (n-1) * dx
    
    #Initialize xi for left riemann
    xiL = a
 
    #Left Riemann Sum
    while xoL <= xiL <= xfL:
        ArecL = f(xiL) * dx #area of individual rectangle
        AtotL += ArecL #add area of each rectangle together to get total area under curve
        xiL += dx #increment to next rectangle's left edge

    return AtotL

def rightriemann(f, a, b, N):
    AtotR = 0 #initialize area under curve
    a = float(a) #lower bound of interval
    b = float(b) #upper bound of interval
    N = float(N) #number of rectangles used in approximation
    dx = (b-a)/N #equal step size (width) for each rectangle
    
    #set bounds
    xoR = a + dx #First rectangle has right edge at x = a + dx
    xfR = b #Final rectangle has right edge at x = b = a + N * dx
    
    #Initialize xi for right riemann sum
    xiR = a + dx  

    #Right Riemann Sum
    while xoR <= xiR <= xfR:
    	ArecR = f(xiR) * dx #area of individual rectangle
    	AtotR += ArecR #add area of each rectangle together to get total area under curve
    	xiR += dx #increment to next rectangle's left edge

    return AtotR
    
def trapezoidsum(f, a, b, N): 
    #initialize areas under curve
    AtotL = 0
    AtotR = 0
    AtotT = 0
    
    #bounds and step size
    a = float(a) #lower bound of interval
    b = float(b) #upper bound of interval
    N = float(N) #number of rectangles used in approximation
    dx = (b-a)/N #equal step size (width) for each rectangle
    
    #set bounds for left and right sums
    xoL = a #First rectangle has left edge at x = a
    xfL = a + (N-1) * dx #Final rectangle has edge at x = b - dx = a + (n-1) * dx
    
    xoR = a + dx #First rectangle has right edge at x = a + dx
    xfR = b #Final rectangle has right edge at x = b = a + N * dx
    
    #Initialize xi for left and right riemann sum
    xiL = a
    xiR = a + dx  
    
    #Left Riemann Sum
    while xoL <= xiL <= xfL:
    	ArecL = f(xiL) * dx #area of individual rectangle
    	AtotL += ArecL #add area of each rectangle together to get total area under curve
    	xiL += dx #increment to next rectangle's left edge

    #Right Riemann Sum
    while xoR <= xiR <= xfR:
    	ArecR = f(xiR) * dx #area of individual rectangle
    	AtotR += ArecR #add area of each rectangle together to get total area under curve
    	xiR += dx #increment to next rectangle's left edge

    AtotT = 1/2 * (AtotL + AtotR) #Trapzoid rule is average of left and right riemann sums
    
    return AtotT

def mcint(f, a, b, N): #Monte Carlo Integration
    #Initialize 
    a = float(a) #lower bound of interval
    b = float(b) #upper bound of interval
    Npoints = float(N) #number of function evaluations used in approximation
    
    Amc = np.zeros(N) 
    
    for x in range(len(Amc)):
    	Amc[x] = np.random.uniform(a,b) #Random number between upper and lower bound.

    Fsum = 0

    for x in Amc: #Evaluate Function at each point 
    	Fsum += f(x)
    	
    I = (b-a)/float(Npoints) * Fsum #Monte Carlo Integration Formula. I = (b-a)/N * Sum F(xi)
    return I
	
#Function of interest
def f(x):
    return np.exp(-x)

#Analytical integral
def intf(x, a, b):
    return -1 * np.exp(-1 * b) + np.exp(-1 * a)

if __name__ == "__main__":

    # default number of rectangles
    Nint = 100

    # default order of quadrature integration
    Nord = 1

    #default number of points for Monte Carlo Integration
    Npoints = 1000
    
    # bounds
    a = 0
    b = 1
    
    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
	
    if '-Nint' in sys.argv: 
        p = sys.argv.index('-Nint')
        Nint = int(sys.argv[p+1])
        
    if '-Nord' in sys.argv:
        p = sys.argv.index('-Nord')
        Nord = int(sys.argv[p+1]) 
        
    if '-Npoints' in sys.argv:
        p = sys.argv.index('-Npoints')
        Npoints = int(sys.argv[p+1]) 
        
    if '-Lowerbound' in sys.argv:
        p = sys.argv.index('-Lowerbound')
        a = int(sys.argv[p+1]) 
        
    if '-Upperbound' in sys.argv:
        p = sys.argv.index('-Upperbound')
        b = int(sys.argv[p+1])
  
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-Nint] number of intervals" % sys.argv[0])
        print
        sys.exit(1)  


    #Analytical Solution
    actualval = intf(f, a, b) 

    print(f"analytical solution: {actualval}")
    
    
    #integrate by quadratures w/ Scipy Package
    quadval, quaderr = integrate.fixed_quad(f, a, b, n = Nord) 

    print(f"method by quadratures: {quadval}")


    #numerical integration with Riemann sums and Trapezoidal Sums
    LeftRiemann = leftriemann(f, a, b, Nint) 
    RightRiemann = rightriemann(f, a, b, Nint) 
    TrapezoidRule = trapezoidsum(f, a, b, Nint) 

    print(f"Left Riemann Sum: {LeftRiemann}")
    print(f"Right Riemann Sum: {RightRiemann}")
    print(f"Trapzoid Sum: {TrapezoidRule}")


    #Monte Carlo Integration
    MCInt = mcint(f, a, b, Npoints)
    print(f"Monte Carlo Integration: {MCInt}")
    

    #Error in each order of Quadrature Integration
    Quaderrors = []

    orders = np.arange(1, Nord, 1)

    for i in orders:
        quadval, quaderr = integrate.fixed_quad(f, a, b, n=i)
        quaderror = (quadval - actualval)/actualval
        Quaderrors.append(quaderror)

    #Graph of Quadrature Error vs Order of Quadrature Integration
    plt.figure()
    plt.scatter(orders, Quaderrors)
    plt.xlim([0, max(orders)])
    plt.xlabel("Order of Quadrature Integration", fontsize = 15)
    plt.ylabel("Error", fontsize = 15)
    plt.title("Quadrature Integration compared to Analytical Solution", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.show()
   
   
    #Error for number of sub-intervals in Trapzoidal Integration 
    Trapezoiderrors = []

    intervals = np.arange(1, Nint, 10)
    
    for i in intervals:
        TrapezoidRule = trapezoidsum(f, a, b, i) 
        trapezoiderror = (TrapezoidRule - actualval)/actualval
        Trapezoiderrors.append(trapezoiderror)

    #Graph of Trapezoidal Sum Error vs Number of Sub-Intervals
    plt.figure()
    plt.scatter(intervals, Trapezoiderrors)
    plt.xlim([0, max(intervals)])
    plt.xlabel("Number of Sub-Intervals", fontsize = 15)
    plt.ylabel("Error", fontsize = 15)
    plt.title("Trapezoid Rule compared to Analytical Solution", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.show()
    

    #Error in Monte Carlo Integration.
    MCInterrors = []

    MCintervals = np.arange(1, Npoints, 10)
    
    for i in MCintervals:
        MCInt = mcint(f, a, b, i) 
        MCInterror = (MCInt - actualval)/actualval
        MCInterrors.append(MCInterror)

    #Graph of Monte Carlo Integration Error vs Number of Function Evaluations
    plt.figure()
    plt.scatter(MCintervals, MCInterrors)
    plt.xlim([0, max(MCintervals)])
    plt.xlabel("Number of Function Evaluations", fontsize = 15)
    plt.ylabel("Error", fontsize = 15)
    plt.title("Monte Carlo Integration compared to Analytical Solution", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.show()
