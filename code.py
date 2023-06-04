import numpy as np
import matplotlib.pyplot as plt

def display_home_screen():
    print("            =========================================")
    print("               Welcome to A Slope Field Generator!        ")
    print("            =========================================")
    print("\n")
    print ("Below is the slope field for the differential equation cos(x)-sin(y).")

   
display_home_screen()


#Draws the slope field. Takes in a differential equation, the x and y Limits, and now many slopes are to be plotted in each direction.

def slope_field(dydx, xlim=(-5,5), ylim= (-5,5), num_arrows=20):

    #The built-in Linespace function creates an array of evenly spaced values between the lower and higher x-Limits.

    #In this case, it creates 20 evenly spaced values, which represent the x-coordinates of the slope lines.

    x_vals = np.linspace(xlim[0], xlim[1], num_arrows)

    #Represents the y-values of the slope lines.

    y_vals = np.linspace(ylim[0], ylim[1], num_arrows)

    #meshGrid creates a grid of coordinate points. This Line of code is providing a complete set of

    #coordinate points that cover the entire x-y plane by creating two 2D arrays, one for all the x values and the other for the y-values. (20 rows!)

    X, Y = np.meshgrid(x_vals, y_vals)

    #ensures that the lines all have a consistent Length of 1 by creating a 2D array thats the same size as the X and Y arrays.

    slopeSize = np.ones_like(X)

    #calculates derivative values at each XY point.

    deriValues = dydx(X, Y)

    #plots the slope Line. (Usually it is an arrow, but I made it so its a line.) 
    plt.quiver(X, Y, slopeSize, deriValues, angles= 'xy', headaxislength=0, headlength=0, headwidth=0)

# example differential equation. Any equation can be entered and its respective slope field will be produced. 
def dydx(x, y):
    return np.cos(x)-np.sin(y)

slope_field(dydx)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect('equal')  # Set aspect ratio to make axes equal
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis
plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis
plt.grid(True, linestyle='dotted')  # Add gridlines
