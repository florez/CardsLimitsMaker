from utils import getArgs, readConfig
import ROOT as rt

if __name__ == "__main__":
	args = getArgs()
 	config = readConfig(args.config)
	
	for channel in config['signals']+config['backgrounds']:
		print(channel)	
		print('getting file {}...'.format(args.channelPath + channel  + '.root'))	
		rootFile = rt.TFile(args.channelPath + channel  + '.root','READ')
		print('Getting histogram...')
		rootFile.Get('Mjj')
