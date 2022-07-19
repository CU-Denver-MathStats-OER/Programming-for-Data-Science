import matplotlib.pyplot as plt
import numpy as np

class FunctionTemplate(object):
    '''
    Templates the typical methods inherited by specific function subclasses
    
    Attributes
    ----------
    
    Methods
    -------
    evaluate(x)
        
    plot(x_min, x_max, fignum=0, N=100, c='b', ls=':')
        Makes a plot of the function
    '''
    def __init__(self):
        '''
        Nothing to see here.
        '''
        return
    
    def evaluate(self, x):
        '''
        This is overwritten by the evaluate method of the sub-class.
        '''
        return
    
    def plot(self, x_min, x_max, fignum=0, N=100, c='b', ls=':'):
        '''
        Each function has the ability to plot itself.
        '''
        x_plot = np.linspace(x_min, x_max, N)
        
        plt.figure(fignum)
        plt.plot(x_plot, self.evaluate(x_plot), c=c, ls=ls)
        
        return
    
class Polynomial(FunctionTemplate):
    '''
    Create a polynomial from coefficients assumed to be given in increasing order.
    
    Subclass of :class: FunctionTemplate that overrides the evaluate method.
    
    Attributes
    ----------
    coeffs : list or numpy.array
        coeffs[0] is constant term and coeffs[-1] is the coefficient of x**(len(coeffs)) term
    
    Methods
    -------
    evaluate(x)
        Returns the function values at points x.
    '''
    def __init__(self, coeffs):
        '''
        Parmaeters
        ----------
        coeffs : list or numpy.array
            coeffs[0] is constant term and coeffs[-1] is the coefficient of x**(len(coeffs)-1) term
        '''
        self.coeffs = coeffs
        
        return
        
    def evaluate(self, x):
        '''
        Returns the function values at points x.
        
        Parameters
        ----------
        x : int, float, or numpy.array
            The points in the domain.
            
        Returns
        -------
        v : float or numpy.array
            The values of the polynomial at the points x
        '''
        v = 0  # v is for value
        
        for order, coeff in enumerate(self.coeffs):
            v += coeff * x**order
        
        return v
    

class Sine(FunctionTemplate):
    '''
    Create a sine function of the form $a\sin(\omega x)$ where $a$ is an amplitude
    that is defaulted to 1 and $\omega$ is a frequency that is also defaulted to 1.
    
    Subclass of :class: FunctionTemplate that overrides the evaluate method.
    
    Attributes
    ----------
    a : int or float
        The amplitude of the sine function
    omega : int or float
        The frequency of the sine function
    
    Methods
    -------
    evaluate(x)
        Returns the function values at points x.
    '''
    def __init__(self, omega=1, a=1):
        '''
        Parmaeters
        ----------
        a : int or float
            The amplitude
        omega : int or float
            The frequency
        '''
        self.a = a
        self.omega = omega
        
        return
        
    def evaluate(self, x):
        '''
        Evaluates the function at points x.
        
        Parameters
        ----------
        x : int, float, or numpy.array
            The points in the domain of the function.
            
        Returns
        -------
        Returns the function values at points x.
        '''
        
        return self.a * np.sin( self.omega*x )
    
class Cosine(FunctionTemplate):
    '''
    Create a cosine function of the form $a\cos(\omega x)$ where $a$ is an amplitude
    that is defaulted to 1 and $\omega$ is a frequency that is also defaulted to 1.
    
    Subclass of :class: FunctionTemplate that overrides the evaluate method.
    
    Attributes
    ----------
    a : int or float
        The amplitude
    omega : int or float
        The frequency
    
    Methods
    -------
    evaluate(x)
        Returns the function values at points x.
    '''
    def __init__(self, a, omega):
        '''
        Parmaeters
        ----------
        a : int or float
            The amplitude of the cosine function.
        omega : int or float
            The frequency of the cosine function.
        '''
        self.a = a
        self.omega = omega
        
        return
        
    def evaluate(self, x):
        '''
        Evaluates the function at points x.
        
        Parameters
        ----------
        x : int, float, or numpy.array
            The points in the domain of the function.
            
        Returns
        -------
        Returns the function values at points x.
        '''
        
        return self.a * np.cos( self.omega*x )
    
class Logarithm(FunctionTemplate):
    '''
    Create a logarithm function of the form $a \log_b(x)$ where $b$ is the 
    base of the logarithm function defaulted to $e$ (to give the natural 
    logarithm) and $a$ is a multiplicative scaling of the function that is 
    defaulted to 1.
    
    Subclass of :class: FunctionTemplate that overrides the evaluate method.
    
    Attributes
    ----------
    b : int or float
        The base of the logarithm.
    a : int or float
        The scaling of the logarithm.
        
    Methods
    -------
    evaluate(x)
        Returns the function values at points x.
    '''
    def __init__(self, b=np.e, a=1):
        '''
        Parmaeters
        ----------
        b : int or float
            The base of the logarithm
        a : int or float
            The scaling of the logarithm
        '''
        self.b = b
        self.a = a
        
        return
        
    def evaluate(self, x):
        '''
        Evaluates the function at points x.
        
        Parameters
        ----------
        x : int, float, or numpy.array
            The points in the domain of the function.
            
        Returns
        -------
        Returns the function values at points x.
        '''
        
        return self.a * np.log(x)/np.log(self.b)
    
class Exponential(FunctionTemplate):
    '''
    Create an exponential function of the form $a b^(x)$ where $b$ is the 
    base of the exponential function defaulted to $e$ and $a$ is a 
    multiplicative scaling of the function that is defaulted to 1.
    
    Subclass of :class: FunctionTemplate that overrides the evaluate method.
    
    Attributes
    ----------
    b : int or float
        The base of the exponential.
    a : int or float
        The scaling of the exponential.
        
    Methods
    -------
    evaluate(x)
        Returns the function values at points x.
    '''
    def __init__(self, b=np.e, a=1):
        '''
        Parmaeters
        ----------
        b : int or float
            The base of the exponential
        a : int or float
            The scaling of the exponential
        '''
        self.b = b
        self.a = a
        
        return
        
    def evaluate(self, x):
        '''
        Evaluates the function at points x.
        
        Parameters
        ----------
        x : int, float, or numpy.array
            The points in the domain of the function.
            
        Returns
        -------
        Returns the function values at points x.
        '''
        
        return self.a * np.power(self.b, x)