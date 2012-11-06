#!/user/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__copyright__ = "Copyright 2012, Ole Christian Weidner"
__license__   = "MIT"

import air
import sys

# This code requires numpy (pip install numpy) 
# and matplotlib (pip install matplotlib)
#import numpy as np
#import matplotlib.pyplot as plt


################################################################################
##
def main():
  global logger

  try:
    # check parameters
    if len(sys.argv) < 2:
      print "Usage: avg-ttc.py appname"
      sys.exit(-1) 

    # conenct to AirStore server
    host='gw68.quarry.iu.teragrid.org'

	# try to connect to the air store (Redis) server
    store = air.AirStore(host=host,
	                     password='ILikeBigJob_wITH-REdIS',
	                     rootnamespace='airexample')
    store.connect()

    p = list()

    app = store.get_application(sys.argv[1])

    sum = 0
    sum_iter = 0

    earlies_start_time = 10000000000.0
    latest_start_time  = 0.0


    for proc_str in app.list_processes():
        proc = app.get_process(proc_str)
        info = proc.get_info("default_info")
        data = info.get_data()

        termination_time = float(data['termination_time'])
        create_time = float(data['create_time'])
        if create_time < earlies_start_time:
            earlies_start_time = create_time
        if create_time > latest_start_time:
            latest_start_time = create_time

        delta_t =  termination_time - create_time 
        sum += delta_t
        sum_iter += 1
        print "%s" % (delta_t)

    print "Average: %s" % (sum / sum_iter)
    print "Earliest start time: %s " % earlies_start_time
    print "Latest start time: %s " % latest_start_time

    sys.exit(0)

  except KeyboardInterrupt, e:
    print "Ctrl-C caught... exiting..."
    sys.exit(-1)

  except air.AirException, aex:
    print "Air Exception caught: %s" % aex
    sys.exit(-1)



if __name__ == "__main__":
    sys.exit(main())
