// #include <bits/stdc++.h>
#include "TH1.h"
#include "TFile.h"
#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char const *argv[])
{
    /*
 	The command line arguments are:
		pathToRootFile histoName outputFile edgeOfBin1 edgeOfBin2 ... edgeOfBinN
    */

    TFile *rootFile = new TFile(argv[1], "READ");
    TH1F *histo = (TH1F *)rootFile->Get(argv[2]);
    ofstream outputfile;
    outputfile.open(argv[3]);

    const Int_t NBINS = argc - 5;
    Double_t edges[NBINS + 1];

    for(int i = 0; i < NBINS+1; i++){
	edges[i] = atof(argv[i + 4]);
    } 
    
    histo = (TH1F*)histo->Rebin(NBINS,"",edges);  //creates a new variable bin size histogram hnew
    cout << "number of bins: " << histo->GetNbinsX() << endl;

    outputfile << "BinNumber,BinStart,BinEnd,BinCount" << endl; 

    for(int i = 0; i<NBINS ; i++){
	cout << i << " " << edges[i] << " " << edges[i+1] << " "  <<  histo->GetBinContent(i) << endl;
	outputfile << i << "," << edges[i] << "," << edges[i+1] << ","  <<  histo->GetBinContent(i) << endl;
    }

    outputfile.close();

    return 0;
}
