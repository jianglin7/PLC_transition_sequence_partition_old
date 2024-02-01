# import Sequences
###寻找因果集 causal=[('t1', 't6'), ('t3', 't4'), ('t4', 't5')]
def find_causal_list(Seq_list, prior_trasitions_list, TC_list):
    causal_list= []
    for a, b in Seq_list:
        if (a, b) in prior_trasitions_list or (b, a) in prior_trasitions_list or (a,b) in TC_list:
            causal_list.append((a, b))
    return causal_list
# print(causal_list)