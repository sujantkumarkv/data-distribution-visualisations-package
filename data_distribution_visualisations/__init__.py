#from .GaussianDistribution import Gaussian

""" __init__.py file gets executed first.IT'S REQUIRED TO TELL THAT THE DIRECTORY 
    IS OFFICIALLY A PYTHON PACKAGE. It's required even if it's empty.
    So with the code above, I'm importing Gaussian to use it directly in code like, 

    from distributions import Gaussian

    but if __init__.py is empty then to use Gaussian, we gotta do:

    from distributions.GaussianDistribution import Gaussian

    I'm ok with the 2nd import notation so commenting the code above :)
    """