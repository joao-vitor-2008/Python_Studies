#!/bin/zsh

cd /home/joao-vitor/Faculdade/IC/git/Python_Studies/listaDomino/

for counter in $(seq 6 16); do cat P$counter.py >>bloco_II.py; done
