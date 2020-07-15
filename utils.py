import yaml
import argparse


def readYaml(path):
    """
        Read yaml file and return as a 
        dict
    """
    with open(path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def getArgs():
    """
        Get all the required arguments and return them in a dict
    """
    parser = argparse.ArgumentParser(
        description='Create the yields and cards to calculate the limits.')

    parser.add_argument('-config',
                        help='Path to the config.yml file with the signal and bg lists',
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

    return parser.parse_args()
