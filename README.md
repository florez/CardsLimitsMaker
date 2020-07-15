# CardsLimitsMaker

```
    python main.py -config ./config.json \
                   -outputPath ./output/ \
                   -studyType pheno \
                   -sysUncert ./input/syst_uncertainties.dat \
                   -channelPath ./input/single_mu_met_bjets_vbf_pt15 \
		   -histogram Mjj
```

The pyROOT part needs to be run with python2 because of compatibility issues. 

The pandas part needs to be run with python3 as python2 has numpy compatibility issues. 
