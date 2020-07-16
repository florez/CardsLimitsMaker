from utils import readConfig, getArgs
import os
import pandas as pd
import numpy as np

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

def createGlobalMatrix(config, outputPath):
	for histo in config['histograms']:
		
		histoName = histo['name']
		folderToProcess = outputPath + histoName + '/' 

		globalMatrix = pd.DataFrame()

		for sample in config['signals'] + config['backgrounds']:
			
			tempDf = pd.read_csv(folderToProcess + 'rawHistogramInfo/' + sample + '.csv')
			globalMatrix[sample] = tempDf['BinCount'] 
		
		globalMatrix['Data'] = 0
		for bg in config['backgrounds']:
			globalMatrix['Data'] = globalMatrix['Data'] + globalMatrix[bg] 
		
		globalMatrix['data'] = np.ceil(globalMatrix['Data'])
		globalMatrix['bin'] = tempDf.index + 1

		#change order of bin and data in the df
		cols = ['bin', 'data'] + list(globalMatrix.columns[:-2])
		globalMatrix = globalMatrix[cols]

		globalMatrix.to_csv(folderToProcess + 'globalMatrix.csv', index = False) 	
		

def createYields(config, outputPath):

	for histo in config['histograms']:
		histoName = histo['name']
		folderToProcess = outputPath + histoName + '/' 
		globalMatrix = pd.read_csv(folderToProcess + 'globalMatrix.csv')

		for sample in config['signals'] + config['backgrounds'] + ['data']:
		
			globalMatrix[sample].to_csv(folderToProcess + 'yields/' + sample + '.dat' ,header=False, index = False)			

def createCards(config, outputPath):

	for histo in config['histograms']:
		histoName = histo['name']
		folderToProcess = outputPath + histoName + '/' 
		globalMatrix = pd.read_csv(folderToProcess + 'globalMatrix.csv')
		
		uncertFile = open(config['sysUncertFile'], "r")
		uncertFileNumLines = len(uncertFile.readlines(  ))
		uncertFile.close()

		
		for signal in config['signals']:
			for binNum in globalMatrix['bin']:
				
							
				uncertFile = open(config['sysUncertFile'], "r")
				
				outFile = open(folderToProcess + 'cards/' + signal + '_' + str(binNum) + '.txt','w')
				
				outFile.write('imax 1  number of channels\n')
				outFile.write('jmax {}  number of backgrounds\n'.format(len(config['backgrounds'])))
				outFile.write('kmax {}  number of nuisance parameters (sources of systematic uncertainties)\n'.format(uncertFileNumLines))
				
				outFile.write('bin {}\n'.format(binNum))
				outFile.write('observation {}\n'.format(int(globalMatrix['data'].values[binNum-1])))

				outFile.write('bin {}\n'.format(' '.join([str(binNum)]*(len(config['backgrounds'])+1))))
				outFile.write('process SIG {} \n'.format(' '.join(config['backgrounds'])))
				outFile.write('process {}\n'.format( ' '.join([str(x) for x in range(len(config['backgrounds'])+1)]) ))
				outFile.write('rate {} {}\n'.format(globalMatrix[signal].values[binNum-1],' '.join( [str(x) for x in  globalMatrix[config['backgrounds']].iloc[binNum-1].values]  )))
		
					
				outFile.write(uncertFile.read())
				outFile.close()

		
				uncertFile.close()

	
	
if __name__ == "__main__":
	args = getArgs()
	configData = readConfig(args.config)
    
	print('Creating output folders...')
	outputPath = createOutputFolders(configData)

    # create and save global matrix
	print('Retrieving individual histogram data...')
	getIndHistogramsInfo(configData,outputPath)
	
	print("Creating global matrix...")
	createGlobalMatrix(configData, outputPath)
	
	print("Creating yields...")
    # create and save yields from matrix 
	createYields(configData, outputPath)

	print("Creating cards...")
    # create and save from matrix
	createCards(configData,outputPath)
