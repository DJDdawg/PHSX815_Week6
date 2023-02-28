# PHSX815_Week6

This week explored Numerical Integation.

**Riemann Sums**

Riemamn sums use  the area of a rectangle to approximate the area underneath a curve. 

The area of a rectangle is given by $A_{rec} = height * width $, where the width of each rectangle is determined by the amount of sub-intervals N used to evaluate the interval, $\Delta x = \frac{b - a}{N}$, and the height of the rectangle is the function evaluated at each $x_{i}$, $f(x_{i})$. 

A left Riemann sum utilized the left edge of the rectangles, and runs from $x_{0} = a$ to $x_{f} = a + (N-1) \Delta x$.

A right Riemann sum utilized the right edge of each rectangle, with $x_{0} = a + \Delta x$ to $x_{f} = a + N \Delta x$.

The total area is given by adding up the area of all of the rectangles you use. Generally, using more rectangles (larger N or smaller $\Delta x$) gives more accurate results. 

**Trapezoidal Sums**

A trapezoidal sum is simply the average of the left and right Riemann sums. This tends to be a more accurate approximation of the integrals true value than either of the individual Riemann sums. 

**Integration by Quadtratures** 

I won't pretend to understand Quadrature Integration, but there is a scipy package that does it for you. All you need to do is specify the function, lower and upper bounds of the interval, and the order of Quadrature integration you want to use. 

This week's code is in **Integrate.py** where the above 4 methods have been implemented to integrate the function $y = e^{-x}$ on the interval [0, 1]. 


**Running the Code and Results**

The code can be run with the following terminal command:

>$ python3 Integration.py -Nint 100 -Nord 5 -Lowerbound 0 -Upperbound 1

Where the number of intervals for the Riemann and Trapezoidal sums is specified with `-Nint xxx`, the order of quadrature integration is specified with `-Nord xxx`, and the Upper and Lower bound of the interval are specified obviously. 

The output is given in the terminal as the following: 

>method by quadratures: 0.6321205588283172
>
>Left Riemann Sum: 0.6315706623750237
>
>Right Riemann Sum: 0.6252864292852441
>
>Trapzoid Sum: 0.628428545830134
>
>analytical solution: 0.6321205588285577

This program also creates two graphs that analyze the Error of the Quadrature Integration vs Order of Integration and the Error of the Trapezoidal Integration vs Number of Subintervals and are seen in the files **QuadratureError.png** and **TrapezoidError.png**

![QuadratureError.png](https://github.com/DJDdawg/PHSX815_Week6/blob/main/QuadratureError.png)


![TrapezoidError.png](https://github.com/DJDdawg/PHSX815_Week6/blob/main/TrapezoidError.png)


**~~Monte Python and the Holy Grail~~ Monte Carlo Integration**

'Tis but a flesh wound. 

Anyways... We're back, and this time we are integrating more *stochastically*. 

Building upon the above code, I copied the contents from **Integration.py** into **MontePython.py** and simply added a function to do Monte Carlo Integration using the following approximation: 

$I = \int_{a}^{b} f(x) dx \approx \frac{b-a}{N} \Sum_{n=1}^{N} f(x_{i})$ given that a random uniform distribution on the interval $[a, b)$ was used to obtain each $x_{i}$, making the weights $w_{i} = 1$.

The program can be run in the terminal with the following:
>$ python3 MontePython.py -Nint 1000 -Nord 50 -Npoints 2000  -Lowerbound 0 -Upperbound 1

Where the commands are the same as above, and '-Npoints xxx' is the only new command that you must specify. This is the number of function evaluations that will be performed during the Monte Carlo integration. 

The output for the above is the following: 

>analytical solution: 0.6321205588285577
>
>method by quadratures: 0.6321205588285574
>
>Left Riemann Sum: 0.6320684242800702
>
>Right Riemann Sum: 0.6314366717846835
>
>Trapzoid Sum: 0.6317525480323769
>
>Monte Carlo Integration: 0.633629250035489

And a new Graph, **MonteCarloError.png** is created and can be seen below. 

![MonteCarloError.png](https://github.com/DJDdawg/PHSX815_Week6/blob/main/MonteCarloError.png)

The error for this graph is much more random than the others, and while adding more function evaluations does seem to generally decrease the error, this type of integration seems to require more points than the other types above (this could perhaps just be because of the function I have chosen). 

Let's go gamble on **red** in Morocco. 10 Bucks on the big one.
