# import the definition of the steps and input files:
from  Configuration.PyReleaseValidation.relval_steps import *

# here only define the workflows as a combination of the steps defined above:
workflows = Matrix()

# each workflow defines a name and a list of steps to be done. 
# if no explicit name/label given for the workflow (first arg),
# the name of step1 will be used


## re-miniAOD of the production tests
workflows[1601301] = ['', ['ProdMinBias_13_MINIAOD','REMINIAODPROD','HARVESTREMINIAODPROD']]
workflows[1601302] = ['', ['ProdTTbar_13_MINIAOD','REMINIAODPROD','HARVESTREMINIAODPROD']]
workflows[1601303] = ['', ['ProdQCD_Pt_3000_3500_13_MINIAOD','REMINIAODPROD','HARVESTREMINIAODPROD']]

## re-miniAOD workflows -- fullSim noPU
workflows[1601329] = ['', ['ZEE_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601331] = ['', ['ZTT_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601330] = ['', ['ZMM_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

## re-miniAOD workflows -- fullSim PU
workflows[16050200]=['',['ZEE_13_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]
workflows[16025200]=['',['ZEE_13_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]

## re-miniAOD workflows -- data 2015b
workflows[160134.702] = ['',['RunDoubleEG2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]

## re-miniAOD workflows -- data 2015c
workflows[160134.802] = ['',['RunDoubleEG2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]

## re-miniAOD workflows -- data 2015d
workflows[160134.902] = ['',['RunDoubleEG2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]

