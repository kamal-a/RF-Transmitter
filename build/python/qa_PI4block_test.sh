#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/root/gr-OOT/python
export PATH=/root/gr-OOT/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/root/gr-OOT/build/swig:$PYTHONPATH
/usr/bin/python2 /root/gr-OOT/python/qa_PI4block.py 
