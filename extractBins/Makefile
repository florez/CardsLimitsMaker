ROOTCFLAGS=$(shell root-config --cflags)

ROOTLIBS=$(shell root-config --libs)  
ROOTGLIBS=$(shell root-config --glibs)  

# Directory of Exrootanalysis
EXROOTDIR=/usr/local/HEP/ExRootAnalysis
EXROOTLIB=$(EXROOTDIR)/lib
EXROOTINC=$(EXROOTDIR)/ExRootAnalysis


# Directory of Delphes
DELPHESDIR=/usr/local/HEP/Delphes-3.4.1
DELPHESLIB=${DELPHESDIR}
DELPHESINC=${DELPHESDIR}


#compile:  main.cc 
#	g++ -o main main.cc -Wall $(ROOTCFLAGS) 	\
#	-I$(DELPHESINC) -I$(EXROOTINC)	\
#	-L$(DELPHESLIB) -lDelphes -L$(EXROOTLIB) -lExRootAnalysis $(ROOTLIBS)

compile:  main.cc 
	g++ -o main main.cc `root-config --cflags --glibs`
