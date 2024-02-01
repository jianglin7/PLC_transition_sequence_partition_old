import random
from collections import Counter
from prettytable import PrettyTable

import matplotlib.pyplot as plt
# 输入的字母序列
# letters = "ambhgf ambhgf ambhgf ambhgf ambhgf ambhgf ambhgf ambhgf ambhgf kdeilmbhgf ambhgc ambhgc ambhgc ambhgc ambhgc ambhgc ambhgc ambhgc ambhgc amhbgf amhbgf amhbgf amhbgf amhbgf amhbgf amhbgf amhbgf keidlmbhgf amhbgj amhbgj amhbgj amhbgj amhbgj amhbgj amhbgj kedilmhbgj amhbgc amhbgc amhbgc amhbgc amhbgc amhbgc amhbgc kdielmhbgc kiedlmhbgf keidlmhbgc kidelmbhgf keidlmbhgj kedilmbhgj kiedlmhbgj kiedlmhbgc kdeilmhbgj keidlmhbgf ambhgj ambhgj ambhgj ambhgj ambhgj ambhgj ambhgj kdeilmhbgf kiedlmbhgj kidelmhbgf kidelmhbgf kdeilmhbgc kedilmbhgf kdeilmbhgc kidelmhbgj kidelmhbgj kedilmhbgc kiedlmbhgc keidlmhbgj keidlmhbgj kdielmhbgf kdeilmbhgj kdeilmbhgj kedilmbhgc kdielmbhgf kdielmbhgj kidelmbhgj kiedlmbhgf kdielmbhgc kdielmhbgj keidlmbhgc kedilmhbgf kidelmbhgc kidelmhbgc"
letters = "afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi afcegi jdhbk jdhbk jdhbk jdhbk jdhbk jdhbk jdhbk jdhbk jdhbk jdhbk jdhbk jdbhk jdbhk jdbhk jdbhk jdbhk jdbhk jdbhk jdbhk jdbhk jdbhk jdbhk jdbhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk jbdhk "
# 将字母序列分割成单词
words = letters.split()
# print(words)
# 随机打乱单词的顺序
random.shuffle(words)
# print(words)
# 组合
combined_words = ' '.join(words)
# print(combined_words)
# 去除空格
combined_words_without_spaces = combined_words.replace(" ", "")
# print(combined_words_without_spaces)
# 使用空格将单词重新连接起来
shuffled_letters = ' '.join(combined_words_without_spaces)
# print(shuffled_letters)

sequence = shuffled_letters
print(f"sequence_len: {len(sequence)}")

def find_adjacent_pairs(sequence):
    adjacent_pairs = [(sequence[i], sequence[i+1]) for i in range(len(sequence) - 1)]
    return adjacent_pairs
#去除重复的相邻对
def find_unique_adjacent_pairs(pairs):
    unique_pairs = list(set(pairs))
    return unique_pairs
#无重复相邻对排序
def sort_unique_adjacent_pairs(pairs):
    def custom_sort(item):
        return (len(item[0]), item[0])
    sorted_tuples = sorted(pairs, key=custom_sort)
    return sorted_tuples

###sequence寻找变迁
def find_unique_elements(S):
    # 使用split()函数将文本分割成一个列表
    S_list = S.split()
    # 将列表转换为集合以获取不同的元素
    unique_elements = set(S_list)
    # 转换为列表并返回
    unique_elements_list = sorted(list(unique_elements))
    return unique_elements_list

adjacent_pairs=find_adjacent_pairs(combined_words_without_spaces)
pairs = find_unique_adjacent_pairs(adjacent_pairs)
Seq = sort_unique_adjacent_pairs(pairs)
# print(Seq)

Seq_list = Seq
Seq_dict = {}
for item in Seq:
    key, value = item
    if key in Seq_dict:
        Seq_dict[key].append(value)
    else:
        Seq_dict[key] = [value]
# print(Seq_list)
# print(Seq_dict)
# 打印结果
# for key, value in Seq_dict.items():
#     print(f"'{key}': {value}")

#序列中所有的变迁元素，如['t1', 't10', 't11', 't12', 't13', 't14', 't15', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9']
unique_elements = find_unique_elements(sequence)
# print(unique_elements)

##寻找先行变迁
def find_same_start_end_no_repeated_middle_subsequences(sequence):
    subsequences = []
    n = len(sequence)
    for start in range(n):
        for end in range(start + 1, n):
            if sequence[start] == sequence[end]:
                subsequence = sequence[start:end + 1]
                if subsequence not in subsequences:
                    subsequences.append(subsequence)
                break
    return subsequences

def group_subsequences_by_start(subsequences):
    grouped_subsequences = {}
    for subsequence in subsequences:
        start_item = subsequence[0]
        if start_item in grouped_subsequences:
            grouped_subsequences[start_item].append(subsequence)
        else:
            grouped_subsequences[start_item] = [subsequence]
    return grouped_subsequences

# 序列 sequence转换成列表数据S存储,使用split()函数将文本分割成一个列表,S = ['t1', 't2', 't3', 't4',……]
S = sequence.split()
# print(S)
# 调用函数查找子序列
subsequences = find_same_start_end_no_repeated_middle_subsequences(S)
# print(subsequences)
# 根据首项分组子序列
grouped_subsequences = group_subsequences_by_start(subsequences)
# print(grouped_subsequences)
# 输出结果
# for start_item, sequences in grouped_subsequences.items():
#     print(f"Start Item: {start_item}")
#     for subsequence in sequences:
#         print(' '.join(subsequence))
#     print()

# 先行 xianxing_dic={'t1': ['t1', 't2', 't3', 't4']} xianxing_list=[('t1', 't1'), ('t1', 't5'), ('t1', 't4')]
xianxing_dict= {}
for key, sequences in grouped_subsequences.items():
    # print(f"Key: {key}")
    common_elements = set(grouped_subsequences[key][0])
    for lst in grouped_subsequences[key][1:]:
        common_elements = common_elements.intersection(set(lst))
    # 将结果转换为列表
    common_elements_list = list(common_elements)
    xianxing_dict[key]=common_elements_list
    # 打印公共元素
    # print(key,xianxing_dict[key])
xianxing_list = []
for key, values in xianxing_dict.items():
    for value in values:
        xianxing_list.append((key, value))
# print(xianxing_dict)
# print(xianxing_list)

#逆先行 nixianxing={'t5': ['t1', 't3', 't4', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15']}
nixianxing = {}
for key, values in xianxing_dict.items():
    for value in values:
        if (value != key) :
            if value in nixianxing:
                nixianxing[value].append(key)
            else:
                nixianxing[value] = [key]
# print(nixianxing)

###寻找双循环变迁集，存储格式[('t1', 't2'), ('t1', 't4')]
def find_double_loops(S):
    double_loops = []  # 用于存储双循环变迁的集合
    for i in range(len(S) - 2):
        if S[i] == S[i + 2]:
            double_loops.append((S[i], S[i + 1]))
    return double_loops
TC = find_double_loops(S)
# print(TC)

###寻找因果集 causal=[('t1', 't6'), ('t3', 't4'), ('t4', 't5')]
causal_list= []
for a, b in Seq_list:
    if (a, b) in xianxing_list or (b, a) in xianxing_list or (a,b) in TC:
        causal_list.append((a, b))
# print(causal_list)

### 寻找并发集 concr=[('t4', 't14'), ('t4', 't10'), ('t10', 't4'), ('t14', 't4')]
concr = []
## 双向变迁集 dual_direction = [('t4', 't14'), ('t4', 't10'), ('t10', 't4'), ('t14', 't4')]
dual_direction = []
for a, b in Seq_list:
    if (b, a) in Seq_list:
        dual_direction.append((a, b))
# print(dual_direction)

## 序列独立 indepence=[('t1', 't2'), ('t10', 't13'), ('t10', 't14')]
indepence = []
# 所有组合情况
all_combinations = []
# 使用嵌套循环生成两两组合
for i in range(len(unique_elements)):
    for j in range(len(unique_elements)):
        all_combinations.append((unique_elements[i], unique_elements[j]))
# print(all_combinations)
for a,b in all_combinations:
    if (b not in xianxing_dict.get(a, [])) and (a not in xianxing_dict.get(b, [])):
        indepence.append((a,b))
# print(indepence)

# # 判断并发规则1
for a, b in dual_direction:
    if ((a, b) not in causal_list) and ((b, a) not in causal_list):
        if (len(xianxing_dict[a])>1) and (len(xianxing_dict[b])>1):
            concr.append((a, b))
# # 判断并发规则2
for a, b in dual_direction:
    if (a, b) in indepence:
        for key, values in xianxing_dict.items():
            if (a!=key) and (b!=key) and (a in xianxing_dict[key]) and (b in xianxing_dict[key]) and ((a,b) not in concr):
                concr.append((a,b))
# # # 判断并发规则3
for a, b in dual_direction:
    if (a, b) in indepence:
        for key, values in xianxing_dict.items():
            if b==key:
               for value in values:
                   if (value not in xianxing_dict[a]) and ((a, value) in Seq_list) and ((a,b) not in concr):
                       concr.append((a,b))
# # 判断并发规则4
for a, b in dual_direction:
    if (a, b) in indepence:
        flag = 0
        for value in xianxing_dict[a]:
            if (value, b) not in concr:
                flag = 1
        if flag==0 and (a,b) not in concr:
            concr.append((a, b))
# print(concr)

###寻找无关 wuguan=[('t1', 't2'), ('t2', 't3'), ('t3', 't13'), ('t3', 't9'), ('t8', 't13'), ('t8', 't9')]
wuguan = []
# 将causal和concr中的元素放入一个集合中，以便进行高效的查找
excluded_elements = set(causal_list + concr)
# 遍历pairs中的元组，将不在excluded_elements中的元组添加到wuguan中
for pair in Seq_list:
    if pair not in excluded_elements:
        wuguan.append(pair)
# print(wuguan)

print(f"S: {S}")
print(f"Seq: {Seq_list}")
print(f"causal: {causal_list}")
print(f"concr: {concr}")
print(f"irrelv: {wuguan}")
print()

duandian = wuguan
flag = []
for a, b in wuguan:
    for c, d in concr:
        if a == c:
            flag.append((d, b))
        elif a == d:
            flag.append((c, b))
        elif b == c:
            flag.append((a, d))
        elif b == d:
            flag.append((a, c))
# print(flag)
if flag != []:
    for item in flag:
        if item not in duandian:
            duandian.append(item)
# print(duandian)

# 计算每个causal项的频率
causal_frequencies = {}

for item in causal_list:
    pattern = list(item)
    # print(pattern)
    count = 0
    for i in range(len(S) - 1):
        if [S[i], S[i + 1]] == pattern:
            count += 1
    causal_frequencies[item] = count
# print(causal_frequencies)
# 打印causal每一项在S中的频率
for item, count in causal_frequencies.items():
    if count < 0.005 * (len(S) - 1):
        # print(f"{item}: {count}次")
        duandian.append(item)
# print(duandian)

# 初始化一个列表用于存储划分后的部分
partitions = []
current_partition = []

# 遍历S列表，并根据duandian划分
for item in range(len(S)):
    current_partition.append(S[item])
    if item != len(S) - 1 and ((S[item], S[item + 1]) in duandian):
        partitions.append(current_partition)
        current_partition = []

# 如果最后一个部分不为空，将其添加到结果中
if current_partition:
    partitions.append(current_partition)

# print(partitions)


# for item in partitions:
#     print(item)

def partitions_modification(partitions, l):
    result = []
    i = 0
    while i < len(partitions):
        current_merge = []
        current_list = partitions[i]
        flag = 0
        if len(current_list) >= l:
            # 如果当前列表长度大于l，直接添加到结果
            result.append(current_list)
        else:
            current_merge += current_list
            if i == 0:
                # 第一个数据直接往后添加
                while len(current_merge) < l and i < len(partitions) - 1:
                    current_merge += partitions[i + 1]
                    i += 1
                result.append(current_merge)
            elif i == len(partitions) - 1:
                # 最后一个数据
                result[-1] = result[-1] + current_merge
            else:
                # 否则，与前后相邻的列表中长度较小的那一个合并
                while len(current_merge) < l:
                    left_list = result[-1]
                    right_list = partitions[i + 1]
                    # 选择与当前列表合并的方向
                    if len(left_list) <= len(right_list):
                        current_merge = left_list + current_merge
                        result[-1] = current_merge
                        break
                    else:
                        current_merge += right_list
                        i += 1
                        if i == len(partitions) - 1 and len(current_merge) < l:
                            # 如果i已经是最后一个了 并且当前的current_merge长度还是小于l则直接合并
                            current_merge = left_list + current_merge
                            result[-1] = current_merge
                            break
                        else:
                            flag = 1
                if flag == 1:
                    result.append(current_merge)
        i += 1
    return result

partitions=partitions_modification(partitions,1)

def remove_consecutive_str_list(list_of_lists):
    result_list = []
    for input_str in list_of_lists:
        current_str = []
        i = 0
        while i < len(input_str):
            if i == 0:
                current_str.append(input_str[i])
                i = i + 1
            else:
                k = i
                flag = 0
                for j in range(len(current_str)):
                    if current_str[j] == input_str[k]:
                        k = k + 1
                        flag = 1
                    else:
                        k = i
                        flag = 0
                    if k == len(input_str) and j != len(current_str) - 1:
                        flag = 0
                        break
                if flag != 1:
                    current_str.append(input_str[i])
                    i = i + 1
                else:
                    i = k
        result_list.append(current_str)
    return result_list

# 对每个子列表使用方法
result_list = remove_consecutive_str_list(partitions)

# 打印结果
print(result_list)
# for item in result_list:
#     print(item)

print(len(result_list))


# Flatten the nested lists and convert to tuples for hashing
flattened_data = [tuple(sublist) for sublist in result_list]

# Use Counter to count the frequency of each unique list
list_frequencies = Counter(flattened_data)

# Print the results
# for unique_list, frequency in list_frequencies.items():
#     print(f"List: {list(unique_list)} - Frequency: {frequency}")


# # Flatten the nested lists and convert to tuples for hashing
# flattened_data = [tuple(sublist) for sublist in result_list]
#
# # Use Counter to count the frequency of each unique list
# list_frequencies = Counter(flattened_data)
#
# # Create a PrettyTable
# table = PrettyTable()
# table.field_names = ["List", "Frequency"]
#
# # Add data to the table
# for unique_list, frequency in list_frequencies.items():
#     table.add_row([list(unique_list), frequency])
#
# # Print the table
# print(table)
#
# # Plot the table and save it as an image
# fig, ax = plt.subplots(figsize=(15, 8))
# ax.axis('off')
# ax.table(cellText=table._rows, colLabels=table.field_names, cellLoc='center', loc='center')
# plt.savefig('frequency_table.png')
# plt.show()


