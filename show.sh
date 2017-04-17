#!/bin/bash
if [ "$#" -ne 1 ]
then
  python ./Visualization/fullvis.py
else
  python ./Visualization/categorized.py "$1"
fi
python ./Visualization/orderedprops.py
