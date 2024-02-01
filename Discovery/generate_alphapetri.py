import pandas
import pm4py

# xes 启发式挖掘算法
def heuristics_net(file):
    log = pm4py.read_xes(file)
    map = pm4py.discover_heuristics_net(log)
    pm4py.view_heuristics_net(map)

# xes alpha算法
def alpha_net(file):
    log = pm4py.read_xes(file)
    net, im, fm = pm4py.discover_petri_net_alpha(log)
    pm4py.view_petri_net(net, im, fm)

def bpmn(file):
    log = pm4py.read_xes(file)
    process_tree = pm4py.discover_process_tree_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)

if __name__ == "__main__":

    # 将csv数据转为xes数据
    csv_path = 'D:/小七/app/py/code/Sequence_partition/Discovery/data.csv'
    xes_path = 'D:/小七/app/py/code/Sequence_partition/Discovery/data.xes'
    # conver_xes(csv_path, xes_path)

    # #读取xes数据
    # log = pm4py.read_xes(xes_path)

    # #启发式挖掘算法
    # heuristics_net(xes_path)

    #alpha算法
    alpha_net(xes_path)

    # # bpmn模型
    # bpmn(xes_path)

    ## 平均拟合度计算
    log = pm4py.read_xes(xes_path)
    net, im, fm = pm4py.discover_petri_net_alpha(log)
    # pm4py.view_petri_net(net, im, fm)
    tbr = pm4py.conformance_diagnostics_token_based_replay(log, net, im, fm)

    # print(len(tbr))
    count = len(tbr)
    sum = 0.0
    for item in tbr:
        # print(item['trace_fitness'])
        sum = sum + item['trace_fitness']
    # print(count)
    # print(sum)
    av_firness = (sum / count)
    print(f"av_firness: {av_firness}")

    ##精确度计算
    tbr_precision = pm4py.precision_token_based_replay(log, net, im, fm)
    print(f"av_precision: {tbr_precision}")

    f_measure = 2 * (av_firness * tbr_precision) / (av_firness + tbr_precision)
    print(f"F-measure: {f_measure}")
