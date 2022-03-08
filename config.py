'''
This script enables project wide variables to be defined and imported to other scripts as needed
'''

class Requirements:
    """
    Define the required settings for the project, including required packages for the projec to run
    """
    def __init__(self):
        # required packages need to be listed in a format that you would use for pip install
        # list all packages used as those which are already installed will be ignored and won't slow down the install
        # script
        self.required_packages = ['dash', 'plotly']

class Style:
    """
    Define style parameters for the project such as colours, font families
    """
    def __init__(self):
        self.jman_blue = '#32819F'
