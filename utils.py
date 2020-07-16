import json
import argparse


def readConfig(path):
    """
        Read json file and return as a 
        dict
    """
    f = open(path) 
    data = json.load(f) 
    f.close()

    return data
    
def getArgs():
    """
        Get all the required arguments and return them in a dict
    """
    parser = argparse.ArgumentParser(
        description='Create the yields and cards to calculate the limits.')

    parser.add_argument('-config',
                        help='Path to the config.json file with the signal and bg lists',
                        required=True)
    
    args = parser.parse_args()
    return args
