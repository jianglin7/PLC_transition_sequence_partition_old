import csv
import time
import pm4py
import pandas
import Algorithm3 as algo3

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


data = algo3.subsequence
csv_path = "D:/小七/app/py/code/Sequence_partition/Discovery/data.csv"
generate_csv(data, csv_path)

def conver_xes(csv_path,xes_path):
    event_log = pm4py.format_dataframe(pandas.read_csv(csv_path, sep=','),case_id='case_id', activity_key='activity', timestamp_key='timestamp')
    pm4py.write_xes(event_log, xes_path)

xes_path = 'D:/小七/app/py/code/Sequence_partition/Discovery/data.xes'
conver_xes(csv_path, xes_path)