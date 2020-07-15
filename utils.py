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

    parser.add_argument('-sysUncert',
                        help='Path to the systematic uncertainties',
                        required=True)

    parser.add_argument('-channelPath',
                        help='Path to the channel folder that contains all of the histograms',
                        required=True)

    parser.add_argument('-outputPath',
                        help='Path to the output folder',
                        required=True)

    parser.add_argument('-studyType',
                        help='Type of analysis',
                        choices=['exp', 'pheno'],
                        required=True)

    args = parser.parse_args()

    # make sure paths have a slash at the end
    if args.channelPath[-1] != '/':
        args.channelPath += '/'

    if args.outputPath[-1] != '/':
        args.outputPath += '/'

    return args
