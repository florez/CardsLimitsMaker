# CardsLimitsMaker

## Installation

### extractBins
To run this code, the code in the `extractBins` folder must be compiled using the command:

```
make compile
```
Note that in order for the program to compile, ROOT and DELPHES must be installed in your system. Please see the `./extractBins/Makefile` file if you need to tweak the values for the delphes and exRootAnalysis folders. 

### Python 3

Additionally, python3 must be installed along with the libraries:

```
pandas
numpy
argparse
```

You can install them manually or in bulk with the `requirements.txt` file with the command `pip install -r requirements.txt`. A virtual environment with `pip` or `conda` is recommended.



## Usage

To run the program, type the following command in your terminal replacing `<your config.json>` with the path to your configuration file.

```
    python3 main.py -config <your config.json> 

```

### Configuration file

In order to run the program, you need to congfigure the configuration file in `JSON` format. 

```
{
     "channelPath" : <path to input data>,
     "sysUncertFile": <path to the systematic uncertanties file>,
     "studyType" : <type of study, for now, only "pheno" is supported>,
     "outputPath" : <output folder path>,
         "signals":[
				signal1.root,
				signal2.root>,
				.
				.
				.
     ],
         "backgrounds":[
				background1.root,
				background2.root,
				background3.root,
				.
				.
				.
     ],
     "histograms": [
		{
			"name" : <name of histogram 1>, 
			"binEdges" : <list of floats with histogram bins, for example: [0.0,40.0,60.0,80.0,100.0,120.0,140.0,160.0,300.0]>
		},
		{
			"name" : <name of histogram 2>, 
			"binEdges" : <list of floats with histogram bins for histogram 2>
		}
     ]
 }

```

With the configuration file defined, all that is left is to run the program.

Happy coding! 

