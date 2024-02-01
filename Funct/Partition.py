
def do_partition(irrelev_list, concr_list, causal_list, sequence, frequency):
    duandian = irrelev_list
    flag = []
    for a, b in irrelev_list:
        for c, d in concr_list:
            if a == c:
                flag.append((d, b))
            elif a == d:
                flag.append((c, b))
            elif b == c:
                flag.append((a, d))
            elif b == d:
                flag.append((a, c))
    if flag != []:
        for item in flag:
            if item not in duandian:
                duandian.append(item)
    S = sequence.split()
    # 计算每个causal项的频率
    causal_frequencies = {}
    for item in causal_list:
        pattern = list(item)
        count = 0
        for i in range(len(S) - 1):
            if [S[i], S[i + 1]] == pattern:
                count += 1
        causal_frequencies[item] = count
    for item, count in causal_frequencies.items():
        # if count < 0.005 * (len(S) - 1):
        if count < frequency:
            duandian.append(item)

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

    return partitions

