# PHSX815_Week6

This week explored Numerical Integation.

**Riemann Sums**

Riemamn sums use  the area of a rectangle to approximate the area underneath a curve. 

The area of a rectangle is given by $A_{rec} = height * width $, where the width of each rectangle is determined by the amount of sub-intervals N used to evaluate the interval, $\Delta x = \frac{b - a}{N}$ and the height of the rectangle is the function evaluated at each $x_{i}$. 

A left Riemann sum utilized the left edge of the rectangles, and runs from $x_{0} = a$ to $x_{f} = a + (N-1) * \Delta x$.

A right Riemann sum utilized the right edge of each rectangle, with $x_{0} = a + \Delta x$ to $x_{f} = a + N * \Delta * X$.

**Trapezoidal Sums**

A trapezoidal sum is simply the average of the left and right Riemann sums. This tends to be a more accurate approximation of the integrals true value than either of the individual Riemann sums. 

**Integration by Quadtratures** 

I won't pretend to understand Quadrature Integration, but there is a scipy package that does it for you. All you need to do is specify the function, lower and upper bounds of the interval, and the order of Quadrature integration you want to use. 

This week's code is in **Integrate.py** where the above 4 methods have been implemented to integrate the function $y = e^{-x}$ on the interval [0, 1]. 

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


