""" Example application demonstrating how to submit a jobs with PilotJob.  """

import os
import time
import sys
from pilot import PilotComputeService, ComputeDataService, State
	
if __name__ == "__main__":

    # check parameters
    if len(sys.argv) < 3:
        print "Usage: run-many-bowties-LONESTAR.py name processes"
        sys.exit(-1) 

    run_name = sys.argv[1]
    num_proc = int(sys.argv[2])

    start_time=time.time()
    pilot_compute_service = PilotComputeService("redis://ILikeBigJob_wITH-REdIS@gw68.quarry.iu.teragrid.org:6379")
    pilot_compute_description=[]

    pilot_compute_description.append({ "service_url": "sge+ssh://localhost",
                                       "number_of_processes": num_proc*2, 
	                               "queue": "development",
                                       #"processes_per_node":4,
                                       "working_directory": "%s/agent" % os.getenv('WORK'),
                                       "walltime":30,
                                     })

    print pilot_compute_description

    for pcd in pilot_compute_description:
        pilot_compute_service.create_pilot(pilot_compute_description=pcd)

    compute_data_service = ComputeDataService()
    compute_data_service.add_pilot_compute_service(pilot_compute_service)

    print ("Finished Pilot-Job setup. Submitting compute units")

    # submit compute units
    for i in range(num_proc):
        compute_unit_description = {
                "executable": "%s/hpdc13-experiments/scripts/air-run-bowtie-LONESTAR.sh" % os.getenv('WORK'),
                "arguments": ["%s-%s-procs" % (run_name, num_proc)],
                "total_cpu_count": 2,            
                "output": "bowtie-stdout.txt",
                "error" : "bowtie-stderr.txt",
        } 
        compute_unit = compute_data_service.submit_compute_unit(compute_unit_description)

    print ("Waiting for compute units to complete")
    compute_data_service.wait()

    print ("Terminate Pilot Jobs")
    compute_data_service.cancel()    
    pilot_compute_service.cancel()
    end_time=time.time()

    print "Total time to solution-" + str(round(end_time-start_time,2))

