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


data = [['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'h', 'b', 'k', 'j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'h', 'b', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'h', 'b', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'b', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'b', 'h', 'k', 'j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'b', 'h', 'k', 'j', 'd', 'h', 'b', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k', 'j', 'd', 'b', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k', 'j', 'd', 'b', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'b', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'h', 'b', 'k', 'j', 'b', 'd', 'h', 'k', 'j', 'd', 'b', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'b', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'b', 'h', 'k', 'j', 'b', 'd', 'h', 'k', 'j', 'd', 'b', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'h', 'b', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'h', 'b', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'b', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'h', 'b', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'd', 'h', 'b', 'k'], ['a', 'f', 'c', 'e', 'g', 'i'], ['j', 'b', 'd', 'h', 'k'], ['a', 'f', 'c', 'e', 'g', 'i']]

filename = "/extest/generate.csv"
generate_csv(data, filename)

def conver_xes(csv_path,xes_path):
    event_log = pm4py.format_dataframe(pandas.read_csv(csv_path, sep=','),case_id='case_id', activity_key='activity', timestamp_key='timestamp')
    pm4py.write_xes(event_log, xes_path)

csv_path = '/extest/generate.csv'
xes_path = '/extest/generate.xes'
conver_xes(csv_path, xes_path)

log = pm4py.read_xes(xes_path)
# net, im, fm = pm4py.discovery.discover_petri_net_alpha_plus(log)
net,im,fm=pm4py.discovery.discover_petri_net_alpha(log)
pm4py.view_petri_net(net, im, fm)