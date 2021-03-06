import FWCore.ParameterSet.Config as cms

from EgammaAnalysis.ElectronTools.calibrationTablesRun2 import correctionType
from EgammaAnalysis.ElectronTools.calibrationTablesRun2 import files

calibratedElectrons = cms.EDProducer("CalibratedElectronProducerRun2",

                                     # input collections
                                     electrons = cms.InputTag('gedGsfElectrons'),
                                     gbrForestName = cms.vstring('electron_eb_ECALTRK_lowpt', 'electron_eb_ECALTRK',
                                                                 'electron_ee_ECALTRK_lowpt', 'electron_ee_ECALTRK',
                                                                 'electron_eb_ECALTRK_lowpt_var', 'electron_eb_ECALTRK_var',
                                                                 'electron_ee_ECALTRK_lowpt_var', 'electron_ee_ECALTRK_var'),

                                     # data or MC corrections
                                     # if isMC is false, data corrections are applied
                                     isMC = cms.bool(False),
    
                                     # set to True to get special "fake" smearing for synchronization. Use JUST in case of synchronization
                                     isSynchronization = cms.bool(False),
                                     
                                     correctionFile = cms.string(files[correctionType])
                                     )

