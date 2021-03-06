import FWCore.ParameterSet.Config as cms

muoObjects = cms.VPSet(
       cms.PSet(
           pathNAME = cms.string("HLT_L1SingleMu18"),
           moduleNAME = cms.string("hltL1fL1sMu18L1Filtered0"),
           label  = cms.string("L1 muon"),
           xTITLE = cms.string("L1 muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,50.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(False),
           displayInPrimary_pt_HEM17 = cms.bool(False),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(False),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_L2Mu10"),
           moduleNAME = cms.string("hltL2fL1sMu22or25L1f0L2Filtered10Q"),
           label  = cms.string("L2 muon"),
           xTITLE = cms.string("L2 muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,20.,30.,40.,50.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(False),
           displayInPrimary_pt_HEM17 = cms.bool(False),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(False),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_Mu27"),
           moduleNAME = cms.string("hltL3fL1sMu22Or25L1f0L2f10QL3Filtered27Q"),
           label  = cms.string("L3 muon"),
           xTITLE = cms.string("L3 muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,10.,20.,24.,25.,26.,27.,28.,29.,30.,31.,32.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(False),
           displayInPrimary_pt_HEM17 = cms.bool(False),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(False),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_IsoMu27"),
           moduleNAME = cms.string("hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07"),
           label  = cms.string("ISO muon"),
           xTITLE = cms.string("ISO muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,10.,20.,24.,25.,26.,27.,28.,29.,30.,31.,32.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_Mu20"),
           moduleNAME = cms.string("hltL3fL1sMu18L1f0L2f10QL3Filtered20Q"),
           label  = cms.string("L3 muon20"),
           xTITLE = cms.string("L3 muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(False),
           displayInPrimary_pt_HEM17 = cms.bool(False),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(False),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_IsoMu20"),
           moduleNAME = cms.string("hltL3crIsoL1sMu18L1f0L2f10QL3f20QL3trkIsoFiltered0p07"),
           label  = cms.string("ISO muon20"),
           xTITLE = cms.string("ISO muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL"),
           moduleNAME = cms.string("hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4"),
           label  = cms.string("ISO muon (double-muon)"),
           xTITLE = cms.string("ISO muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,5.,6.,7.,8.,9.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(True),
           displayInPrimary_dimass   = cms.bool(True),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(True),
           doPlotDiMass = cms.untracked.bool(True),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ"),
           moduleNAME = cms.string("hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4DzFiltered0p2"),
           label  = cms.string("ISO muon (double-muon dz)"),
           xTITLE = cms.string("ISO muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,5.,6.,7.,8.,9.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(True),
           displayInPrimary_dimass   = cms.bool(True),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(True),
           doPlotDiMass = cms.untracked.bool(True),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL"),
           moduleNAME = cms.string("hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4"),
           label  = cms.string("ISO muon (mu-tkmu)"),
           xTITLE = cms.string("ISO muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,5.,6.,7.,8.,9.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(True),
           displayInPrimary_dimass   = cms.bool(True),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(True),
           doPlotDiMass = cms.untracked.bool(True),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ"),
           moduleNAME = cms.string("hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4DzFiltered0p2"),
           label  = cms.string("ISO muon (mu-tkmu dz)"),
           xTITLE = cms.string("ISO muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,5.,6.,7.,8.,9.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(True),
           displayInPrimary_dimass   = cms.bool(True),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(True),
           doPlotDiMass = cms.untracked.bool(True),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL"),
           moduleNAME = cms.string("hltDiMuonTrk17Trk8RelTrkIsoFiltered0p4"),
           label  = cms.string("ISO muon (tkmu-tkmu)"),
           xTITLE = cms.string("ISO muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,5.,6.,7.,8.,9.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(True),
           displayInPrimary_dimass   = cms.bool(True),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(True),
           doPlotDiMass = cms.untracked.bool(True),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ"),
           moduleNAME = cms.string("hltDiMuonTrk17Trk8RelTrkIsoFiltered0p4DzFiltered0p2"),
           label  = cms.string("ISO muon (tkmu-tkmu dz)"),
           xTITLE = cms.string("ISO muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,5.,6.,7.,8.,9.,10.,15.,16.,17.,18.,19.,20.,21.,22.,23.,24.,25.,30.,40.,60.,80.,100.,150.,200.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(True),
           displayInPrimary_dimass   = cms.bool(True),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(True),
           doPlotDiMass = cms.untracked.bool(True),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_Mu50"),
           moduleNAME = cms.string("hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q"),
           label  = cms.string("L3 muon50"),
           xTITLE = cms.string("L3 muon"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,10.,20.,30.,40.,45.,46.,47.,48.,49.,50.,51.,52.,53.,54.,55.,60.,70.,80.,90.,100.,200.,300.,400.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(False),
           displayInPrimary_pt_HEM17 = cms.bool(False),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(False),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
)

