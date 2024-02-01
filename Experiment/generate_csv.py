import csv
import time
import pm4py
import pandas

# 把划分好的变迁序列写入到csv文件中去
def generate_csv(partitions, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['case_id', 'activity','timestamp'])

        case_id = 1
        k = 0
        for partition in partitions:
            for transition in partition:
                # 获取当前时间戳
                timestamp = time.time()+ k
                k = k + 1
                # 格式化时间
                time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
                writer.writerow([case_id, transition,time_str])
            case_id += 1


data = [['a', 'm', 'b', 'h', 'g', 'c'], ['k', 'd', 'e', 'i', 'l', 'm', 'h', 'b', 'g', 'c'], ['a', 'm', 'b', 'h', 'g', 'f'], ['k', 'e', 'i', 'd', 'l', 'm', 'h', 'b', 'g', 'c'], ['k', 'i', 'd', 'e', 'l', 'm', 'h', 'b', 'g', 'f'], ['k', 'd', 'i', 'e', 'l', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'h', 'b', 'g', 'c'], ['a', 'm', 'b', 'h', 'g', 'f'], ['k', 'e', 'i', 'd', 'l', 'm', 'b', 'h', 'g', 'f'], ['k', 'd', 'i', 'e', 'l', 'm', 'b', 'h', 'g', 'j'], ['a', 'm', 'b', 'h', 'g', 'j'], ['k', 'i', 'e', 'd', 'l', 'm', 'h', 'b', 'g', 'c'], ['k', 'i', 'd', 'e', 'l', 'm', 'b', 'h', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'f'], ['a', 'm', 'h', 'b', 'g', 'f'], ['k', 'e', 'd', 'i', 'l', 'm', 'b', 'h', 'g', 'j'], ['k', 'i', 'd', 'e', 'l', 'm', 'h', 'b', 'g', 'c'], ['a', 'm', 'h', 'b', 'g', 'f'], ['k', 'd', 'e', 'i', 'l', 'm', 'b', 'h', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'j'], ['k', 'e', 'd', 'i', 'l', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'b', 'h', 'g', 'c'], ['k', 'd', 'e', 'i', 'l', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'b', 'h', 'g', 'f'], ['a', 'm', 'h', 'b', 'g', 'c'], ['k', 'i', 'e', 'd', 'l', 'm', 'h', 'b', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'f'], ['a', 'm', 'h', 'b', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'b', 'h', 'g', 'f'], ['k', 'i', 'e', 'd', 'l', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'b', 'h', 'g', 'j'], ['a', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'h', 'b', 'g', 'c'], ['a', 'm', 'h', 'b', 'g', 'c'], ['k', 'e', 'i', 'd', 'l', 'm', 'h', 'b', 'g', 'j'], ['k', 'd', 'e', 'i', 'l', 'm', 'b', 'h', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'j'], ['k', 'i', 'e', 'd', 'l', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'j'], ['k', 'd', 'e', 'i', 'l', 'm', 'h', 'b', 'g', 'f'], ['k', 'e', 'i', 'd', 'l', 'm', 'h', 'b', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'j'], ['k', 'e', 'i', 'd', 'l', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'c'], ['k', 'i', 'd', 'e', 'l', 'm', 'b', 'h', 'g', 'j'], ['k', 'i', 'd', 'e', 'l', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'c'], ['k', 'e', 'd', 'i', 'l', 'm', 'h', 'b', 'g', 'j'], ['k', 'd', 'e', 'i', 'l', 'm', 'h', 'b', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'c'], ['k', 'd', 'i', 'e', 'l', 'm', 'h', 'b', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'j'], ['a', 'm', 'b', 'h', 'g', 'j'], ['k', 'd', 'e', 'i', 'l', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'b', 'h', 'g', 'f'], ['k', 'd', 'i', 'e', 'l', 'm', 'b', 'h', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'b', 'h', 'g', 'j'], ['k', 'i', 'd', 'e', 'l', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'b', 'h', 'g', 'c'], ['k', 'i', 'e', 'd', 'l', 'm', 'b', 'h', 'g', 'j'], ['a', 'm', 'b', 'h', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'c'], ['k', 'e', 'i', 'd', 'l', 'm', 'b', 'h', 'g', 'j'], ['k', 'd', 'e', 'i', 'l', 'm', 'b', 'h', 'g', 'f'], ['k', 'd', 'i', 'e', 'l', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'f'], ['a', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'f'], ['k', 'e', 'd', 'i', 'l', 'm', 'b', 'h', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'c'], ['a', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'j'], ['a', 'm', 'h', 'b', 'g', 'f'], ['k', 'e', 'd', 'i', 'l', 'm', 'h', 'b', 'g', 'f'], ['k', 'e', 'd', 'i', 'l', 'm', 'h', 'b', 'g', 'c'], ['k', 'd', 'i', 'e', 'l', 'm', 'h', 'b', 'g', 'c'], ['k', 'i', 'e', 'd', 'l', 'm', 'b', 'h', 'g', 'f'], ['a', 'm', 'b', 'h', 'g', 'c']]
filename = "D:/小七/app/py/code/Sequence_partition/Experiment/generate.csv"
generate_csv(data, filename)

def conver_xes(csv_path,xes_path):
    event_log = pm4py.format_dataframe(pandas.read_csv(csv_path, sep=','),case_id='case_id', activity_key='activity', timestamp_key='timestamp')
    pm4py.write_xes(event_log, xes_path)

csv_path = 'D:/小七/app/py/code/Sequence_partition/Experiment/generate.csv'
xes_path = 'D:/小七/app/py/code/Sequence_partition/Experiment/generate.xes'
conver_xes(csv_path, xes_path)

log = pm4py.read_xes(xes_path)
# net, im, fm = pm4py.discovery.discover_petri_net_alpha_plus(log)
net,im,fm=pm4py.discovery.discover_petri_net_alpha(log)
pm4py.view_petri_net(net, im, fm)