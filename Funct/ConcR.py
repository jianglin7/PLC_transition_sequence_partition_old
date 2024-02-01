# # 判断并发规则1
def find_concr1(dual_direction_list, causal_list, prior_trasitions_dict):
    concr = []
    for a, b in dual_direction_list:
        if ((a, b) not in causal_list) and ((b, a) not in causal_list):
            if (len(prior_trasitions_dict[a])>1) and (len(prior_trasitions_dict[b])>1):
                concr.append((a, b))
    return concr

# # 判断并发规则2
def find_concr2(dual_direction_list, SI_list, prior_trasitions_dict, concr):
    for a, b in dual_direction_list:
        if (a, b) in SI_list:
            for key, values in prior_trasitions_dict.items():
                if (a!=key) and (b!=key) and (a in prior_trasitions_dict[key]) and (b in prior_trasitions_dict[key]) and ((a,b) not in concr):
                    concr.append((a,b))
    return concr

# # # 判断并发规则3
def find_concr3(dual_direction_list, SI_list, prior_trasitions_dict, Seq_list, concr):
    for a, b in dual_direction_list:
        if (a, b) in SI_list:
            for key, values in prior_trasitions_dict.items():
                if b==key:
                   for value in values:
                       if (value not in prior_trasitions_dict[a]) and ((a, value) in Seq_list) and ((a,b) not in concr):
                           concr.append((a,b))
    return concr

# # 判断并发规则4
def find_concr4(dual_direction_list, SI_list, prior_trasitions_dict, concr):
    for a, b in dual_direction_list:
        if (a, b) in SI_list:
            flag = 0
            for value in prior_trasitions_dict[a]:
                if (value, b) not in concr:
                    flag = 1
            if flag==0 and (a,b) not in concr:
                concr.append((a, b))
    return concr

# concr_list = []
# concr_list = find_concr1(dual_direction_list, causal_list, prior_trasitions_dict, concr_list)
# concr_list = find_concr2(dual_direction_list, SI_list, prior_trasitions_dict, concr_list)
# concr_list = find_concr3(dual_direction_list, SI_list, prior_trasitions_dict, Seq_list, concr_list)
# concr_list = find_concr4(dual_direction_list, SI_list, prior_trasitions_dict, concr_list)