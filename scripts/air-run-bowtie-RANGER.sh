#!/bin/bash  

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "Usage: air-run... APPKEY"

export RUN=RANGER_BOWTIE_$1
echo "Registering application run as: $RUN"

module load python
. $SCRATCH/software/pythonenv/bin/activate
export BOWTIE_DIR=$SCRATCH/software/bowtie2/

air-run $RUN $BOWTIE_DIR/bin/bowtie2 --time -x $BOWTIE_DIR/data/ref/hg18/hg18 -U $BOWTIE_DIR/data/reads/Marisa_miRNA-1_qseq.fq -S result.sam 
