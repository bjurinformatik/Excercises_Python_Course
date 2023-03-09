import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

proc_value = np.zeros(1)
total = np.zeros(1)

#Perform local computation on each process
proc_value = np.random.random_sample(1)
print("Value from process", rank, "is %s" % proc_value )

#Set up the communication between processes and send output to root
comm.Reduce(proc_value, total, op=MPI.SUM, root=0)

#Print out result from process 0
if comm.rank == 0:
    print("The sum of values from all processes: %s" % total)
