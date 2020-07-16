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
    
    # make sure the paths end with a /
    if data['channelPath'][-1] != '/':
        data['channelPath'] += '/'

    if data['outputPath'][-1] != '/':
        data['outputPath'] += '/'

    print('Using configuration:')
    print(json.dumps(data, indent=4))
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
