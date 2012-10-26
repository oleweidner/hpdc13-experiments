#!/bin/bash  

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "Usage: air-run... APPKEY"

export RUN=RANGER_BFAST_$1
echo "Registering application run as: $RUN"

module load python
. $SCRATCH/software/pythonenv/bin/activate
export BFAST_DIR=$SCRATCH/software/bfast/

air-run $RUN $BFAST_DIR/bin/bfast match -A 1 -r $BFAST_DIR/data/reads/read.170M.fastq -f $BFAST_DIR/data/reference/hg2122/hg_2122.fa > /dev/null
