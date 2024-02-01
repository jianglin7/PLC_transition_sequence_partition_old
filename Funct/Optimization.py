def remove_consecutive_str(partitions):
    final_result = []
    for input_str in partitions:
        current_str = []
        final_str = []
        i = 0
        while i < len(input_str):
            if i == 0:  # 当到达字符串的开始或者当前字符与前一个字符不同时
                current_str.append(input_str[i])
                final_str.append(input_str[i])
                i = i + 1
            else:  # 当当前字符与前一个字符相同时
                k = i
                falg = 0
                for j in range(len(current_str)):
                    if (current_str[j] == input_str[k]):
                        k = k + 1
                        falg = 1
                    else:
                        k = i
                        falg = 0
                    if (k == len(input_str) and j != len(current_str) - 1):
                        falg = 0
                        break
                if (falg != 1):
                    current_str.append(input_str[i])
                    final_str.append(input_str[i])
                    i = i + 1
                else:
                    m = k - i  # 记录相差的位置个数
                    final_strlen = len(final_str)
                    list1 = final_str[final_strlen - m:final_strlen + 1]
                    list2 = final_str[final_strlen - 2 * m:final_strlen - m]
                    if (list1 == list2):  # 已经存了两个连续的
                        i = k
                    else:
                        for n in range(len(list1)):
                            final_str.append(list1[n])
                        i = k
        final_result.append(final_str)
    return final_result

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