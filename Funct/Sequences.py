import re

#以t+数字为整体找相邻对 Seq (Seq_list)
def find_adjacent_pairs(sequence):
    pattern = r"t\d+"
    matches = re.findall(pattern, sequence)
    adjacent_pairs = [(matches[i], matches[i+1]) for i in range(len(matches) - 1)]
    unique_pairs = list(set(adjacent_pairs))
    def custom_sort(item):
        return (len(item[0]), item[0])
    Seq = sorted(unique_pairs, key=custom_sort)
    return Seq
# Seq_list转化为Seq_dict
def Seq_listtodict(Seq):
    Seq_dict = {}
    for item in Seq:
        key, value = item
        if key in Seq_dict:
            Seq_dict[key].append(value)
        else:
            Seq_dict[key] = [value]
    return Seq_dict

# 寻找变迁序列中所有的变迁 unique_elements_list
def find_unique_elements(sequence):
    # 使用split()函数将文本分割成一个列表
    S_list = sequence.split()
    # 将列表转换为集合以获取不同的元素
    unique_elements = set(S_list)
    # 转换为列表并返回
    unique_elements_list = sorted(list(unique_elements))
    return unique_elements_list

##寻找先行变迁 xianxing_dict = {}
def prior_trasitions(sequence):
    sequence = sequence.split()
    subsequences = []
    n = len(sequence)
    for start in range(n):
        for end in range(start + 1, n):
            if sequence[start] == sequence[end]:
                subsequence = sequence[start:end + 1]
                if subsequence not in subsequences:
                    subsequences.append(subsequence)
                break
    grouped_subsequences = {}
    for subsequence in subsequences:
        start_item = subsequence[0]
        if start_item in grouped_subsequences:
            grouped_subsequences[start_item].append(subsequence)
        else:
            grouped_subsequences[start_item] = [subsequence]
    xianxing_dict = {}
    for key, sequences in grouped_subsequences.items():
        # print(f"Key: {key}")
        common_elements = set(grouped_subsequences[key][0])
        for lst in grouped_subsequences[key][1:]:
            common_elements = common_elements.intersection(set(lst))
        # 将结果转换为列表
        common_elements_list = list(common_elements)
        xianxing_dict[key] = common_elements_list
    return xianxing_dict
# prior_trasitions dict转化为list
def prior_trasitions_dicttolist(prior_trasitions_dict):
    prior_trasitions_list = []
    for key, values in prior_trasitions_dict.items():
        for value in values:
            prior_trasitions_list.append((key, value))
    return prior_trasitions_list

#寻找逆先行集
def Inprior(prior_trasitions_dict):
    nixianxing = {}
    for key, values in prior_trasitions_dict.items():
        for value in values:
            if (value != key):
                if value in nixianxing:
                    nixianxing[value].append(key)
                else:
                    nixianxing[value] = [key]
    return nixianxing

# 寻找交错变迁集，存储格式[('t1', 't2'), ('t1', 't4')]
def find_TC(sequence):
    sequence = sequence.split()
    TC_list = []  # 用于存储双循环变迁的集合
    for i in range(len(sequence) - 2):
        if sequence[i] == sequence[i + 2]:
            TC_list.append((sequence[i], sequence[i + 1]))
    return TC_list

## 寻找双向变迁集 dual_direction = [('t4', 't14'), ('t4', 't10'), ('t10', 't4'), ('t14', 't4')]
def find_dual_direction(Seq_list):
    dual_direction = []
    for a, b in Seq_list:
        if (b, a) in Seq_list:
            dual_direction.append((a, b))
    return dual_direction

## 寻找序列独立 SI=[('t1', 't2'), ('t10', 't13'), ('t10', 't14')]
def find_SI_list(unique_elements, prior_trasitions_dict):
    indepence = []
    # 所有组合情况
    all_combinations = []
    # 使用嵌套循环生成两两组合
    for i in range(len(unique_elements)):
        for j in range(len(unique_elements)):
            all_combinations.append((unique_elements[i], unique_elements[j]))
    for a,b in all_combinations:
        if (b not in prior_trasitions_dict.get(a, [])) and (a not in prior_trasitions_dict.get(b, [])):
            indepence.append((a,b))
    return indepence

#
# sequence = "t1 t2 t3 t4 t1 t2 t4 t3 t5 t6 t7 t4 t1 t2 t3 t4 t5 t6 t7 t4 t1 t2 t3 t4 t1 t2 t3 t4 t5 t6 t7 t4 t5 t6 t7 t4 t1 t2 t3 t4 t5 t6 t7 t4 t5 t6 t7 t4 t5 t6 t7 t4 t5 t6 t7 t4 t5 t6 t7 t4 t1 t2 t4 t3 t1 t2 t3 t4 t1 t2 t3 t4 t1 t2 t4 t3 t1 t2 t3 t4 t1"
#
# ## 不同的变迁 unique_elements
# unique_elements = find_unique_elements(sequence)
# print(f"unique_elements: {unique_elements}")
#
# ## 寻找相邻变迁对 Seq的不同格式 Seq_list Seq_dict
# Seq = find_adjacent_pairs(sequence)
# Seq_list = Seq
# Seq_dict = Seq_listtodict(Seq)
# print(f"Seq_list: {Seq_list}")
# print(f"Seq_dict: {Seq_dict}")
#
# ## 先行集 prior_trasitions （prior_trasitions_list、prior_trasitions_dict）
# prior_trasitions_dict = prior_trasitions(sequence)
# prior_trasitions_list = prior_trasitions_dicttolist(prior_trasitions_dict)
# print(f"prior_trasitions_dict: {prior_trasitions_dict}")
# print(f"prior_trasitions_list: {prior_trasitions_list}")
#
# ## 逆先行集
# inprior_dict = Inprior(prior_trasitions_dict)
# print(f"inprior_dict: {inprior_dict}")
#
# ##寻找交错变迁集 TC_list
# TC_list = find_TC(sequence)
# print(f"TC_list: {TC_list}")
#
# ## 双向变迁dual_direction_list
# dual_direction_list = find_dual_direction(Seq_list)
# print(f"dual_direction_list: {dual_direction_list}")
#
# ##序列独立SI_list
# SI_list = find_SI_list(unique_elements, prior_trasitions_dict)
# print(f"SI_list: {SI_list}")