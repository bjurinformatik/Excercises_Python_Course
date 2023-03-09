from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("Testing if MPI works!!", rank)

# Run script with: mpirun -host localhost -n 4 python mpi_ranks.py 
