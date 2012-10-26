#!/bin/bash  

module load python
. $HOME/software/pythonenv/bin/activate
export BFAST_DIR=$HOME/software/bfast/

export RUN=HOTEL_bfast_fewwd_bj128_ref3G_read170M

air-run $RUN $BFAST_DIR/bin/bfast match -A 1 -r $BFAST_DIR/data/reads/read.170M.fastq -f $BFAST_DIR/data/reference/hg2122/hg_2122.fa > /dev/null
