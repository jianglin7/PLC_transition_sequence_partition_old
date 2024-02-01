def find_irrelev(causal_list, concr_list, Seq_list):
    irrelev_list = []
    # 将causal和concr中的元素放入一个集合中，以便进行高效的查找
    excluded_elements = set(causal_list + concr_list)
    # 遍历pairs中的元组，将不在excluded_elements中的元组添加到wuguan中
    for pair in Seq_list:
        if pair not in excluded_elements:
            irrelev_list.append(pair)
    return irrelev_list