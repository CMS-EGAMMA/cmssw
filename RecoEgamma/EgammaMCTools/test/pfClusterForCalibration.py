# EGM skimmer
# Author: Rafael Lopes de Sa

import FWCore.ParameterSet.Config as cms

# Run with the 2017 detector
from Configuration.StandardSequences.Eras import eras
process = cms.Process('SKIM',eras.Run2_2017)

# Import the standard packages for reconstruction and digitization
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('RecoEgamma.EgammaMCTools.pfClusterMatchedToPhotonsSelector_cfi')

# Global Tag configuration ... just using the same as in the RelVal
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '90X_upgrade2017_realistic_ExtendedZeroMaterial_EGM_PFCalib', '')

process.MessageLogger.cerr.threshold = 'ERROR'
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

# This is where users have some control.
# Define which collections to save and which dataformat we are using
savedCollections = cms.untracked.vstring('drop *',
# The commented ones are large collections that can be kept for debug
#                                         'keep EcalRecHitsSorted_*_*_*',
#                                         'keep recoPFClusters_*_*_*',
#                                         'keep recoCaloClusters_*_*_*',
#                                         'keep recoSuperClusters_*_*_*', 
#                                         'keep recoGsfElectron*_*_*_*',
#                                         'keep recoPhoton*_*_*_*',
#                                         'keep *_mix_MergedTrackTruth_*',
                                         'keep *_reducedEcalRecHits*_*_*',
                                         'keep double_fixedGridRho*_*_*',
                                         'keep recoGenParticles_*_*_*',
                                         'keep GenEventInfoProduct_*_*_*',
                                         'keep PileupSummaryInfos_*_*_*',
                                         'keep *_ecalDigis_*_*',
                                         'keep *_offlinePrimaryVertices_*_*',
                                         'keep *_particleFlowCluster*_*_*')

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10000))

process.source = cms.Source("PoolSource",                 
                            fileNames = cms.untracked.vstring(
        'file:/eos/user/r/rcoelhol/TestingPFClusters/AOD/00AFAD91-1635-E711-A988-5065F382A241.root',
        ),
                            secondaryFileNames = cms.untracked.vstring(
         'file:/eos/user/r/rcoelhol/TestingPFClusters/RAW/0C033EC9-8A34-E711-B54B-5065F382C201.root',
         'file:/eos/user/r/rcoelhol/TestingPFClusters/RAW/46D7847E-BC34-E711-A409-0242AC130005.root',
        'file:/eos/user/r/rcoelhol/TestingPFClusters/RAW/7050DE06-B534-E711-BCF0-141877410ACD.root',
        'file:/eos/user/r/rcoelhol/TestingPFClusters/RAW/88081134-BC34-E711-BC69-0242AC130002.root',
        'file:/eos/user/r/rcoelhol/TestingPFClusters/RAW/AE82A641-CF33-E711-A457-5065F3818281.root',
        'file:/eos/user/r/rcoelhol/TestingPFClusters/RAW/FAF39EC6-D533-E711-95E6-24BE05C48831.root'
)
                            )
process.PFCLUSTERoutput = cms.OutputModule("PoolOutputModule",
                                           dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO'),
                                                                        filterName = cms.untracked.string('')
                                                                        ),
                                           eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                           fileName = cms.untracked.string('skimEGMobjects_fromRAW.root'),
                                           outputCommands = savedCollections,
                                           splitLevel = cms.untracked.int32(0)
                                           )

# Run the digitizer to make the trackingparticles
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
process.trackingtruth_step = cms.Path(process.pdigi_valid)

# Remake the PFClusters
process.pfclusters_step = cms.Path(process.bunchSpacingProducer *
                                   process.ecalDigis * 
                                   process.ecalPreshowerDigis * 
                                   process.ecalPreshowerRecHit *
                                   process.ecalMultiFitUncalibRecHit *
                                   process.ecalDetIdToBeRecovered *
                                   process.ecalRecHit *
                                   process.particleFlowRecHitPS * 
                                   process.particleFlowRecHitECAL * 
                                   process.particleFlowClusterECALUncorrected * 
                                   process.particleFlowClusterPS *
                                   process.particleFlowClusterECAL)

# Select the PFClusters we want to calibrate
process.particleFlowClusterECALMatchedToPhotons = process.pfClusterMatchedToPhotonsSelector.clone()
process.selection_step = cms.Path(process.particleFlowClusterECALMatchedToPhotons)

# Ends job and writes our output
process.endjob_step = cms.EndPath(process.endOfProcess)
process.output_step = cms.EndPath(process.PFCLUSTERoutput)

# Schedule definition, rebuilding rechits
process.schedule = cms.Schedule(process.trackingtruth_step,process.pfclusters_step,process.selection_step,process.endjob_step,process.output_step)


