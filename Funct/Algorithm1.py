import Sequences as ss
import CausalR as ca
import ConcR as co
import  IrrelevR as ir
import data



sequence = data.sequence
## 不同的变迁 unique_elements
unique_elements = ss.find_unique_elements(sequence)
print(f"unique_elements: {unique_elements}\n")

## 寻找相邻变迁对 Seq的不同格式 Seq_list Seq_dict
Seq = ss.find_adjacent_pairs(sequence)
Seq_list = Seq
Seq_dict = ss.Seq_listtodict(Seq)
print(f"Seq_list: {Seq_list}")
print(f"Seq_dict: {Seq_dict}\n")

## 先行集 prior_trasitions （prior_trasitions_list、prior_trasitions_dict）
prior_trasitions_dict = ss.prior_trasitions(sequence)
prior_trasitions_list = ss.prior_trasitions_dicttolist(prior_trasitions_dict)
print(f"prior_trasitions_dict: {prior_trasitions_dict}")
print(f"prior_trasitions_list: {prior_trasitions_list}\n")

## 逆先行集
inprior_dict = ss.Inprior(prior_trasitions_dict)
print(f"inprior_dict: {inprior_dict}\n")

##寻找交错变迁集 TC_list
TC_list = ss.find_TC(sequence)
print(f"TC_list: {TC_list}\n")

## 双向变迁dual_direction_list
dual_direction_list = ss.find_dual_direction(Seq_list)
print(f"dual_direction_list: {dual_direction_list}\n")

##序列独立SI_list
SI_list = ss.find_SI_list(unique_elements, prior_trasitions_dict)
print(f"SI_list: {SI_list}\n")

causal_list = ca.find_causal_list(Seq_list, prior_trasitions_list, TC_list)
print(f"causal_list: {causal_list}\n")


concr_list = co.find_concr1(dual_direction_list, causal_list, prior_trasitions_dict)
concr_list = co.find_concr2(dual_direction_list, SI_list, prior_trasitions_dict, concr_list)
concr_list = co.find_concr3(dual_direction_list, SI_list, prior_trasitions_dict, Seq_list, concr_list)
concr_list = co.find_concr4(dual_direction_list, SI_list, prior_trasitions_dict, concr_list)
print(f"concr_list: {concr_list}\n")


irrelev = ir.find_irrelev(causal_list, concr_list, Seq_list)
print(f"irrelev: {irrelev}\n")