#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from Tuplizer.TuplizeRunner import *

from Samples_H4l import *


# make a new workarea for each eventcontent present in the NTuples, for example "Workarea_standard" for "standard" saved in NTuples, another one "Workarea_pfcands" for ntuplizing samples with the content "pfcands" stored. Each sample will have the same name, just a different 'contents' and xml file name
workarea = os.path.join(os.environ['ANALYSISPATHTUPLIZER'], 'Workarea_standard')
username = os.environ['USER']

AllSamples = SampleContainer()
# Add_Data(AllSamples)
# Add_Background(AllSamples)
# Add_Signals_LQ(AllSamples)
Add_Samples_H4L(AllSamples)

config_per_year = {
    'UL16preVFP': {
        'arch_tag': 'slc7_amd64_gcc700',
        'cmsswtag': 'CMSSW_10_6_28'
    },
    'UL16postVFP': {
        'arch_tag': 'slc7_amd64_gcc700',
        'cmsswtag': 'CMSSW_10_6_28'
    },
    'UL17': {
        'arch_tag': 'slc7_amd64_gcc700',
        'cmsswtag': 'CMSSW_10_6_28'
    },
    'UL18': {
        'arch_tag': 'slc7_amd64_gcc700',
        'cmsswtag': 'CMSSW_10_6_28'
    }
}


years = []
years.append('UL16preVFP')
years.append('UL16postVFP')
years.append('UL17')
years.append('UL18')
stage = 'mini'
submit = True
submit = False
nevt_per_job = 100000


def main():
    for year in years:
        for samplename, sample in AllSamples.items():
            print(green('--> Working on sample: \'%s\'' % (samplename)))
            if not sample.minipaths.has_year(year):
                print(yellow('   --> skipping sample for '+year))
                continue
            Tuplizer = TuplizeRunner(sample=sample, stage=stage, year=year, config=config_per_year[year], workarea=workarea, submit=submit)
            Tuplizer.CountEvents(check_missing=True)
            # Tuplizer.SubmitTuplize(ncores=1, runtime=(01,00,00), nevt_per_job=nevt_per_job, mode='new')
            # Tuplizer.SubmitTuplize(ncores=1, runtime=(01,00,00), nevt_per_job=nevt_per_job, mode='resubmit', update_missing=False)
            # Tuplizer.SubmitTuplize(ncores=1, runtime=(01,00,00), nevt_per_job=nevt_per_job, mode='resubmit', update_missing=True)
            # Tuplizer.CreateDatasetXMLFile(force_counting=True, count_weights=(sample.type=="MC"), ncores=8)



if __name__ == '__main__':
    main()
