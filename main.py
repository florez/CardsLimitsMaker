from utils import readConfig, getArgs
import os

if __name__ == "__main__":

    args = getArgs()
    configData = readConfig(args.config)
    
    # create and save global matrix
    print("Creating global matrix...")
    
    # hack to run python2 code 
    # python3 has compatibility issues with pyROOT
    os.system(""" 
	python getGlobalTable.py -config {} \
                   -outputPath {} \
                   -studyType {} \
                   -sysUncert {} \
                   -channelPath {} \
		   -histogram {}
	""".format(
			args.config,
			args.outputPath,
			args.studyType,
			args.sysUncert,
			args.channelPath,
			args.histogram))

    # create and save from matrix 

    # create and save from matrix
