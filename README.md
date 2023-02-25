# PHSX815_Week6

This week explored Numerical Integation.

**Riemann Sums**

Riemamn sums use rectangles to 

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
>Left Riemann Sum: 0.6315706623750237
>Right Riemann Sum: 0.6252864292852441
>Trapzoid Sum: 0.628428545830134
>analytical solution: 0.6321205588285577

This program also creates two graphs that analyze the Error of the Quadrature Integration vs Order of Integration and the Error of the Trapezoidal Integration vs Number of Subintervals and are seen in the files **

![Coin Toss Graph.png](https://github.com/DJDdawg/PHSX815_Week2/blob/master/python/Coin%20Toss%20Graph.png)


![Dice Roll Graph](https://github.com/DJDdawg/PHSX815_Week2/blob/master/python/Dice%20Roll%20Graph.png)
