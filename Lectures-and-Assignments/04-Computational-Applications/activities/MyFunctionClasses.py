import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon 
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from scipy.integrate import quad

class MyFunctions(object):
    '''
    A class that provides useful plots/information involving the root of a
    function. 
    '''
    def __init__(self, f, root=None):
        '''
        If a root is given, then it should be given as a float. 
        '''
        self.f = f
        # The following data attributes may not be known at the time of 
        # initialization. 
        self.root = root  
        return
    
    def set_root(self, root):
        '''
        Used to set the self.root attribute as a new root value. Give as a float.
        '''
        self.root = root
        return
        
    def plot(self, x_min, x_max, fignum=0, N=100, c='b', ls='-', lw=2, 
             show_root = False, annotate = True, clf = True):
        '''
        Used to visualize the function and potentially its root.
        '''
        self.fig = plt.figure(fignum)
        if clf is True:
            self.fig.clf()
        
        # Let's add x-axis to the plot but not the y-axis because the interval
        # for plotting may be far away from x=0 which is where the typical 
        # y-axis is plotted.
        plt.axhline(0, linewidth=1, linestyle=':', c='k')  # plot typical x-axis
        
        x_plot = np.linspace(x_min, x_max, N)
        
        plt.plot(x_plot, self.f(x_plot), c=c, ls=ls, lw=lw)
        
        if self.root is not None and show_root:
            self.plot_root(annotate)
        
        plt.show();
        return
        
    def plot_root(self, annotate=True):
        '''
        Used to plot the root if it has been found/estimated
        '''
        # plot approximate root
        plt.scatter(self.root, self.f(self.root), s=70, c='r', marker='s') 

        # Create a text string for the title that formats certain floating point
        # numbers that are relevant in our plot.
        title_str = 'Approx. root at c=' + '{:.3}'.format(self.root) + \
                    r' with f(c)$\approx$' + '{:.2e}'.format(self.f(self.root))
        plt.title(title_str, fontsize=14)
        
        if annotate:
            self.plot_annotate()       
        return
    
    def plot_annotate(self):    
        '''
        Used to annotate the root plot with text and arrows in a two-step process
        '''
        # First, we define the dict (dictionary) of properties of the text and arrows used in the annotation
        bbox = dict(boxstyle="round", fc='b', color='r', alpha=0.5, linewidth=2)  # properties for bounding box of text
        arrowprops = dict(arrowstyle='->', color='k', alpha=0.5, linewidth=2)  # properties for the arrow

        # Now annotate the plot
        y_min, y_max = plt.ylim() #get min and max y-values from plot to offset annotations
        y_range = y_max - y_min
        x_min, x_max = plt.xlim()
        x_range = x_max - x_min

        plt.annotate('Approx. root', fontsize=12, xy=(self.root,self.f(self.root)), 
                     xytext=(self.root-0.35*x_range,0.1*y_range), 
                     color='w', bbox = bbox, arrowprops = arrowprops);           
        return
    
class MyFunctionsEnhanced(MyFunctions):
    '''
    A subclass that provides useful plots/information involving the root of a
    function, which may be found via the bisection algorithm in an interval
    [a, b]
    '''
    def __init__(self, f, root=None, a=None, b=None, 
                 n=None, tol_interval=1e-5, tol_f=1e-8):
        '''
        If a root is given, then it should be given as a float. 
        '''
        super().__init__(f, root)  
        self.a = a
        self.b = b
        self.n = n
        self.tol_interval = tol_interval
        self.tol_f = tol_f
        # If all of the parameters necessary for the evaluation of the bisec. 
        # alg. are set, then run the alg.
        if all((a, b, n, tol_interval, tol_f)):
            self.compute_bisection()
        return

    def set_bisection_parameters(self, a=None, b=None, n=None, 
                                 tol_interval=None, tol_f=None):
        '''
        Useful for setting any or all of the parameters in the bisection alg.
        '''      
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if n is not None:
            self.n = n
        if tol_interval is not None:
            self.tol_interval = tol_interval
        if tol_f is not None:
            self.tol_f = tol_f           
        return
            
    def compute_bisection(self):
        '''
        This simple function applies up to n iterations of the 
        bisection algorithm. 
        
        It sets new data attributes based on the outputs of the previously 
        defined compute_bisection standalone function.
        '''
        
        if (self.a is None) or (self.b is None) or (self.n is None):
            raise AttributeError('Check that all bisection parameters are set. \n' +\
                   'Use set_bisection_parameters to set: a, b, and/or n.')

        # Let us first check the conditions to apply the bisection
        # algorithm are satisfied
        if self.a >= self.b:
            raise ValueError('The bisec. alg. requires a')
        if self.f(self.a)*self.f(self.b) > 0:
            raise ValueError('The bisec. alg. requires f(a) and f(b)' +\
                             'are different signs')

        a_n = self.a
        b_n = self.b
        # Now, perform the bisection algorithm
        current_iter = 0
        while current_iter < self.n:
            current_iter += 1

            # bisect the interval [a,b], i.e., compute mid-point
            c = (b_n + a_n)/2 

            # Check if c is an (approx.) root
            if np.abs(self.f(c)) < self.tol_f:
                break

            # Determine if a or b should be replaced with c
            if self.f(a_n)*self.f(c) < 0:
                b_n = c
            else:
                a_n = c

            # Check if dividing [a,b] in half made the interval 
            # too small to continue
            if (b_n - a_n) < self.tol_interval:
                break
                
        # New data attributes are set based on the completion of the above algorithm        
        self.a_n = a_n 
        self.b_n = b_n
        self.set_root(c)  # Useful for plotting!
        return
    
class MyFunctionsAmazing(MyFunctionsEnhanced):
    '''
    
    '''
    def __init__(self, f, a=None, b=None):
        '''
        
        '''
        super().__init__(f, None, a, b)        
        return
    
    def set_integral_limits(self, a, b):
        '''
        
        '''
        self.a = a
        self.b = b
        return
    
    
    def evaluate_integral(self, a=None, b=None):
        '''
        
        '''
        if (a is not None) and (b is not None):
            self.set_integral_limits(a, b)
            
        self.integral = quad(self.f, self.a, self.b)[0]
        return self.integral
    
    def plot_integral(self, x_min=None, x_max=None, N=101, fignum=0, figsize=(10,6)):
        '''
        
        '''
        if x_min is None:
            x_min = self.a
        
        if x_max is None:
            x_max = self.b
            
        x = np.linspace(x_min, x_max, N)
        y = self.f(x)

        plt.figure(num=fignum, figsize=figsize)
        plt.clf()
        fig, ax = plt.subplots(num=fignum)
        ax.plot(x, y, 'r', linewidth=2)

        plt.axhline(0, linewidth=1, linestyle=':', c='k')  # plot typical x-axis

        # Make the shaded region
        ix = np.linspace(self.a, self.b, N)
        iy = self.f(ix)
        # A * before the zip will "unpack" the tuples in the 
        # list of tuples created by zip
        verts = [(self.a, 0), *zip(ix, iy), (self.b, 0)]
        poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
        ax.add_patch(poly)

        ax.set_title(r"$\int_a^b f(x)\mathrm{d}x \approx $ %3.2f" %self.integral, 
                     fontsize=16)
            
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xticks((self.a, self.b))
        ax.set_xticklabels(('$a$', '$b$'))
        plt.show() 
        return
        
    def evaluate_and_plot_integral(self, a=None, b=None, x_min=None, x_max=None, 
                                   fignum=0):
        '''
        
        '''
        self.evaluate_integral(a=a, b=b)
        
        self.plot_integral(x_min=x_min, x_max=x_max, fignum=fignum)
        return
    
class MyFunctionsRule(MyFunctionsAmazing):
    '''
    
    '''
    def __init__(self, f, a=None, b=None, n=None, rule='Left'):
        '''
        
        '''
        super().__init__(f=f, a=a, b=b)
        self.n = n
        self.rule = rule
        return
        
    def change_rectangles(self, n=None, rule=None):
        '''
        
        '''
        if n is not None:
            self.n = n
        if rule is not None:
            self.rule = rule
            
        return
    
    def compute_integral_approx(self):
        '''
        
        '''
        self.ix = np.linspace(self.a, self.b, self.n+1)  # create the x-values to create the base of each rectangle 
        self.Delta_x = self.ix[1]-self.ix[0]  # compute the length of the base of each rectangle

        # Now determine the height of the rectangle by evaluating the
        # function f at some point along its base.
        if self.rule == 'left':
            self.iy = self.f(self.ix[0:-1])  # evaluate function at left-hand side of its base
        elif self.rule == 'right':
            self.iy = self.f(self.ix[1:])  # evaluate the function at right-hand side of its base
        else:
            self.iy = self.f(self.ix[0:-1]+0.5*self.Delta_x)  # evaluate the function at midpoint of its base

        # Now compute the approximate integral by adding up all 
        # the areas of the rectangles
        self.integral_approx = np.sum(self.iy)*self.Delta_x

        return self.integral_approx
    
    
    def plot_rectangle_approx(self, x_min=0, x_max=1, N=101, fignum=0,
                              figsize=(10, 6)):
        
        # Get a more accurate approximate for comparison sake using method
        # inherited from the super class and plot.
        self.evaluate_integral()

        ################# EVERYTHING BELOW IS JUST FOR PLOTTING
        x = np.linspace(x_min, x_max, N)
        y = self.f(x)

        plt.figure(num=fignum, figsize=figsize)
        plt.clf()
        fig, ax = plt.subplots(num=fignum)
        ax.plot(x, y, 'r', linewidth=2)
        
        plt.axhline(0, linewidth=1, linestyle=':', c='k')  # plot typical x-axis

        rects = []
        for i in range(self.n):
            rects.append(Rectangle((self.ix[i],0), self.Delta_x, self.iy[i]))    
        # Create patch collection with specified colour/alpha
        pc = PatchCollection(rects, facecolor='0.9', alpha=0.5,
                             edgecolor='0.5')
        ax.add_collection(pc)

        ax.set_title(r"$\int_a^b f(x)\mathrm{d}x = %3.2f \approx $ Sum of Rect. Areas = %3.2f" 
                     %(self.integral, self.integral_approx), fontsize=20)

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xticks((self.a, self.b))
        ax.set_xticklabels(('$a$', '$b$'))
        plt.show()
        
        return
    
    def evaluate_and_plot_rectangle_approx(self, a, b, n, rule, x_min, x_max, N=101, fignum=0):
        '''
        
        '''
        self.change_rectangles(n=n, rule=rule)
        
        self.set_integral_limits(a=a, b=b)
        
        self.compute_integral_approx()
        
        self.plot_rectangle_approx(x_min=x_min, x_max=x_max, N=N, fignum=fignum)
        
        return