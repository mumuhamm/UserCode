import FWCore.ParameterSet.Config as cms

def customize_L1TkMuonsGmt(process):
    process.L1TkMuonsGmt.trackingParticleInputTag = cms.InputTag("mix", "MergedTrackTruth")
    process.L1TkMuonsGmt.mcTruthTrackInputTag = cms.InputTag("TTTrackAssociatorFromPixelDigis", "Level1TTTracks")
    process.L1TkMuonsGmt.isolation.IsodumpForHLS = 0
    return process
