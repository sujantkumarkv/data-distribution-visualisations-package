"""This file is necessary for pip installing & pip would automatically look for it.
    It contains metadata :) """

from setuptools import setup
setup(name= 'data_distribution_visualisations',
    version= '0.1.3',
    packages= ['data_distribution_visualisations'],
    description= 'Data Distributions calculations and visualizations of Gaussian & Binomial Distributions with plots.',
    author= 'https://www.github.com/sujantkumarkv',
    zip_safe= False) #files can't be run directly from zipped state.