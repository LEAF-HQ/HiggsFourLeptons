# This script must be sourced from this exact folder before working in this folder.

export ANALYSISNAME=HiggsFourLeptons
export ANALYSISPATH=${LEAFPATH}/${ANALYSISNAME}
export ANALYSISPATHCONFIG=${ANALYSISPATH}/config
export ANALYSISPATHTUPLIZER=${ANALYSISPATH}/Tuplizer
export PYTHONPATH=$PYTHONPATH:${ANALYSISPATH}
export PYTHONPATH=$PYTHONPATH:${ANALYSISPATH}/python
export PYTHONPATH=$PYTHONPATH:${ANALYSISPATH}/DNN
