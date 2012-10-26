#!/bin/bash  

module load python
. $HOME/software/pythonenv/bin/activate
export BOWTIE_DIR=$HOME/software/bowtie2/

export RUN=INDIA_bowtie-Marisa_miRNA-1_qseq.fq

air-run $RUN $BOWTIE_DIR/bin/bowtie2 --time -x $BOWTIE_DIR/data/ref/hg18/hg18 -U $BOWTIE_DIR/data/reads/Marisa_miRNA-1_qseq.fq -S result.sam 
