import Algorithm2 as algo2
import Optimization as op
import data

partitions = algo2.partitions
l = data.partition_length
partitions_merge=op.partitions_modification(partitions, l)
print(f"partitions_merge: {partitions_merge}\n")

subsequence=op.remove_consecutive_str(partitions_merge)
print(f"subsequence: {subsequence}\n")