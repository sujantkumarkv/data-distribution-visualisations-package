import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution

class Binomial(Distribution):

    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """   
        #       A binomial distribution is defined by two variables: 
        #           the probability of getting a positive outcome
        #           the number of trials
        
        #       If you know these two values, you can calculate the mean and the standard deviation
        #       
        #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
        #       You can then calculate the mean and standard deviation with the following formula:
        #           mean = p * n
        #           standard deviation = sqrt(n * p * (1 - p))
        
        #       

    def __init__(prob, n_times, self, mu = 0, stdev=1):
        Distribution.__init__(self, mu, stdev)
        self.p= prob
        self.n= n_times
        # TODO: Now that you know p and n, you can calculate the mean and standard deviation
        #       You can use the calculate_mean() and calculate_stdev() methods defined below along with the __init__ function from the Distribution class

#--------------------------------------------------------------------------------

    def calculate_mean(self):
        """Function to calculate the mean from p and n
        Args: 
            None
        Returns: 
            float: mean of the data set
        """
        self.mean= self.p * self.n
        return self.mean
            
#----------------------------------------------------------------------------------------

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        Args: 
            None
        Returns: 
            float: standard deviation of the data set
        """
        self.stdev= math.sqrt(n * p * (1 - p))
        return self.stdev

#---------------------------------------------------------------------------------------------

    def replace_stats_with_data():
        # Because the Binomaildistribution class inherits from the Generaldistribution class,
        # you don't need to re-write this method. However,  the method
        # doesn't update the mean or standard deviation of
        # a distribution. Hence you are going to write a method that calculates n, p, mean and
        # standard deviation from a data set and then updates the n, p, mean and stdev attributes.
        # Assume that the data is a list of zeros and ones like [0 1 0 1 1 0 1]. 
        #
        #       Write code that: 
        #           updates the n attribute of the binomial distribution
        #           updates the p value of the binomial distribution by calculating the
        #               number of positive trials divided by the total trials
        #           updates the mean attribute
        #           updates the standard deviation attribute
        #
        #       Hint: You can use the calculate_mean() and calculate_stdev() methods
        #           defined previously.

        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        Args: 
            None
        Returns: 
            float: the p value
            float: the n value
        """
        positive_trials= 0
        #data= self.data
        self.n= len(self.data)
        for value in self.data:
            if value==1: #when toss val is 1, then consider it & later add it to calc probability.
                positive_trials+= 1
        self.p= positive_trials / self.n #no.of positive trials/total trials :)

        self.mean= self.calculate_mean()
        self.stdev= self.calculate_stdev()

#------------------------------------------------------------------------------------------

    def plot_histogram(self): #histogram plot 
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        Args:
            None      
        Returns:
            None
        """
        plt.hist(self.data, facecolor='blue')
        plt.title('Binomial Distribution')
        plt.xlabel('data')
        plt.ylabel('binomial count')
        plt.show()

#-----------------------------------------------------------------------------------
    def binomial_pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        Args:
            k (float): point for calculating the probability density function     
            Simply like we do nCHOOSEk; so it's like how many +ve trials desired out of total trials.
        Returns:
            float: probability density function output

        Formula for Binomial Distribution: (n! / k!*(n-k)!) * (p^k)* (1-p)^(n-k)
            """             
        n= self.n
        p= self.p
        nCHOOSEk= math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
        other_term= math.pow(p, k) * (math.pow(1-p, n-k))
        binomial_pdf= nCHOOSEk * other_term

        return binomial_pdf
        
#-----------------------------------------------------------------------------------

    def plot_bar_pdf(self): 
        #A method to plot the probability density function of the binomial distribution
        """Function to bar plot the pdf of the binomial distribution
        Args:
            None
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        # Use a bar chart to plot the probability density function from
        # k = 0 to k = n
        """data = [23, 45, 56, 78, 213]
        plt.bar([1,2,3,4,5], data)
        plt.show()
        
        This is how code is & prints data[] on y-axis.
        """
        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.

        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists

        """W.R.T the points given & bar-chart, we need x[] as list of 0-n & y[] as list of it's pdf vals"""
        x= [], y= []
        n= self.n
        for k in range(n+1):
            x.append(k) #list of vals from 0-n attained where each is the no.of +ve trials req
        for each_x in x:
            y.append(bimomial_pdf(each_x)) #corresponding pdf vals :)
        
        #now plotting it.'
        plt.title('Binomial Probability Distributions')
        plt.xlabel('positive trials count')
        plt.ylabel('Probability distribution function values')
        plt.bar(x, y)
        plt.show()
        return (x, y) #returning as asked by the instructions :)

#---------------------------------------------------------------------------------------

    def __add__(self, other):
        # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
        """Function to add together two Binomial distributions with equal p
        Args:
            other (Binomial): Binomial instance       
        Returns:
            Binomial: Binomial distribution     
        """    
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise 

        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for 
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.

        # the try, except statement above will raise an exception if the p values are not equal

        """ Hint: When adding two binomial distributions, the p value remains the same
            The new n value is the sum of the n values of the two distributions. """
        result= Binomial()
        result.p= self.p
        result.n= self.n + other.n

        return result

#----------------------------------------------------------------------------------------

def __repr__(self):
    """Function to output the characteristics of the Binomial instance
    Args:
        None
    Returns:
        string: characteristics of the Binomial object
    """
    # TODO: Define the representation method so that the output looks like
    #       mean 5, standard deviation 4.5, p .8, n 20
    #       with the values replaced by whatever the actual distributions values are
    #       The method should return a string in the expected format

    return f'Mean: {self.mean}, Standard Deviation: {self.stdev}, p: {self.p}, n: {self.n}'

