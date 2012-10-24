#!/user/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

__author__    = "Ole Christian Weidner"
__copyright__ = "Copyright 2012, Ole Christian Weidner"
__license__   = "MIT"

import air
import sys

################################################################################
##
def main():
  global logger

  try:
    # check parameters
    if len(sys.argv) < 2:
      print "Usage: graph-gen.py appname"
      sys.exit(-1) 

    # conenct to AirStore server
    host='gw68.quarry.iu.teragrid.org'

	# try to connect to the air store (Redis) server
    store = air.AirStore(host=host,
	                     password='ILikeBigJob_wITH-REdIS',
	                     rootnamespace='airexample')
    store.connect()
    print "test" + sys.argv[0]

    app = store.get_application(sys.argv[1])
    #print ' Application: %s' % app
    for res_str in app.list_resources():
        res = app.get_resource(res_str)
        info = res.get_info("default_info")
        print info.get_data()

        sensor = res.get_sensor("default_sensor")
        print sensor.read()



    sys.exit(0)

  except KeyboardInterrupt, e:
    print "Ctrl-C caught... exiting..."
    sys.exit(-1)

  except air.AirException, aex:
    print "Air Exception caught: %s" % aex
    sys.exit(-1)



if __name__ == "__main__":
    sys.exit(main())