from utils import readConfig, getArgs
import os
import pandas as pd

def createOutputFolders(config):

    channel = config['channelPath'][:-1].split('/')[-1]
    outputPath = config['outputPath'] + channel + '/'

    for histo in config['histograms']:
        histoName = histo['name']
        for subfolder in ['yields','cards','rawHistogramInfo']:
            
            os.system('mkdir -p {}'.format(outputPath + histoName + '/' + subfolder))

    return outputPath    

def getIndHistogramsInfo(config, outputPath):
	
	for sample in config['signals'] + config['backgrounds']:
		fileName = config['channelPath'] + sample + '.root'
		for histo in config['histograms']:
			histoName = histo['name']
			binEdges = histo['binEdges']
			indHistoOutputPath = outputPath + histoName + '/rawHistogramInfo/' + sample + '.csv'
			
			commandToRun = './extractBins/main {} {} {} {}'.format(fileName,histoName,indHistoOutputPath,' '.join([str(x) for x in binEdges])) 
			print(commandToRun)
			os.system(commandToRun)

def createGlobalMatrix(configData):
	pass

if __name__ == "__main__":
    args = getArgs()
    configData = readConfig(args.config)
    
    print('Creating output folders...')
    outputPath = createOutputFolders(configData)

    # create and save global matrix
    print('Retrieving individual histogram data...')
    getIndHistogramsInfo(configData,outputPath)

    print("Creating global matrix...")
	createGlobalMatrix(configData)
    # create and save from matrix 

    # create and save from matrix
