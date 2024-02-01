import Algorithm1 as algo1
import Partition as par
import data

irrelev_list = algo1.irrelev
concr_list = algo1.concr_list
causal_list = algo1.causal_list
sequence = algo1.sequence
frequency = data.causal_frequency
partitions = par.do_partition(irrelev_list, concr_list, causal_list, sequence, frequency)
print(f"sequence: {sequence}\n")
print(f"partitions: {partitions}\n")