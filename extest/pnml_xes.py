import pm4py

# 读取pnml文件，生成事件日志
# net, im, fm = pm4py.read_pnml('D:/小七/app/py/code/blackbox2/shiyan/pnml/1_1.pnml')
# net, im, fm = pm4py.read_pnml('D:/小七/app/py/code/blackbox2/shiyan/pnml/1_n.pnml')
# net, im, fm = pm4py.read_pnml('D:/小七/app/py/code/blackbox2/shiyan/pnml/n_1.pnml')
net, im, fm = pm4py.read_pnml('/extest/0587.pnml')
# net, im, fm = pm4py.read_pnml('D:/小七/app/py/code/blackbox2/shiyan/pnml/0041.pnml')
# pm4py.view_petri_net(net, im, fm)
log = pm4py.play_out(net, im, fm)

# 把petri网模型生成的事件日志输出为xes文件
# pm4py.write_xes(log, "D:/小七/app/py/code/blackbox2/shiyan/csv_xes/1_1.xes")
# pm4py.write_xes(log, "D:/小七/app/py/code/blackbox2/shiyan/csv_xes/1_n.xes")
# pm4py.write_xes(log, "D:/小七/app/py/code/blackbox2/shiyan/csv_xes/n_1.xes")
pm4py.write_xes(log, "/extest/0587.xes")
# pm4py.write_xes(log, "D:/小七/app/py/code/blackbox2/shiyan/csv_xes/0041.xes")

# 读取.xes文件
# log = pm4py.read_xes("0060.xes")
# net, im, fm = pm4py.discover_petri_net_alpha(log)
# pm4py.view_petri_net(net, im, fm)

# 提取所有轨迹
traces = [trace for trace in log]

# # 重放前 100 条轨迹
# for i in range(100):
#     trace = traces[i]
#     places = pm4py.algo.simulation.playout.apply(net, im, fm, trace)
#     print(f"Replayed Trace {i + 1}: {places}")

import xml.etree.ElementTree as ET

# 读取.xes文件
# tree = ET.parse('D:/小七/app/py/code/blackbox2/shiyan/csv_xes/1_1.xes')
# tree = ET.parse('D:/小七/app/py/code/blackbox2/shiyan/csv_xes/1_n.xes')
# tree = ET.parse('D:/小七/app/py/code/blackbox2/shiyan/csv_xes/n_1.xes')
tree = ET.parse('D:/小七/app/py/code/Sequence_partition/extest/0587.xes')
# tree = ET.parse('D:/小七/app/py/code/blackbox2/shiyan/csv_xes/0041.xes')
root = tree.getroot()

# 添加命名空间前缀，用于XPath查询
namespace = {'xes': 'http://www.xes-standard.org/'}

# 用于跟踪已输出轨迹的字典
output_count = {}

# 用于存储连接的轨迹字符串
all_event_values = []

# 统计轨迹总数
num = 0

# 遍历每个轨迹(trace)
for trace in root.findall('.//xes:trace', namespace):
    # 初始化一个空字符串来保存事件的"value"
    event_values = []
    num = num + 1
    # 遍历轨迹中的每个事件
    for event in trace.findall('.//xes:event', namespace):
        # 获取事件的"value"属性值
        event_value = event.find('.//xes:string[@key="concept:name"]', namespace).get('value')
        event_values.append(event_value)

    # 将事件的"value"合并
    combined_event_value = ''.join(event_values)

    # 检查轨迹是否已经输出
    if combined_event_value not in output_count:
        # 更新轨迹的输出计数
        output_count[combined_event_value] = 1
    else:
        # 增加轨迹的输出计数
        output_count[combined_event_value] += 1

    # 连续输出轨迹
    # for _ in range(output_count[combined_event_value]):
    #     all_event_values.append(combined_event_value)

# 输出每个轨迹的最终输出次数，按频率高低输出
for combined_event_value, count in sorted(output_count.items(), key=lambda x: x[1], reverse=True):
    print(f"轨迹 '{combined_event_value}' 输出了 {count} 次")

# 将连接的轨迹字符串写入文件，不换行D:/小七/app/py/code/blackbox2
# with open('D:/小七/app/py/code/blackbox2/shiyan/csv_xes/1_1.txt', 'w') as file:
# with open('D:/小七/app/py/code/blackbox2/shiyan/csv_xes/1_n.txt', 'w') as file:
# with open('D:/小七/app/py/code/blackbox2/shiyan/csv_xes/n_1.txt', 'w') as file:
# with open('D:/小七/app/py/code/blackbox2/shiyan/csv_xes/n_n.txt', 'w') as file:
sum=0
flag=0
with open('/extest/0587.txt', 'w') as file:
    for combined_event_value, count in output_count.items():
        # if count > 10:
        #     file.write(combined_event_value )
        # if count > (num//100):
        #     # 输出多次的轨迹多遍写入文件
        #     file.write((combined_event_value+ ' ') * (count//5))
        if count > 5:
            file.write((combined_event_value + ' ')* (count//5) )
            sum=sum+(count//5)
            flag=flag+1
        else:
            file.write(combined_event_value + ' ')
            sum=sum+1
            flag = flag + 1
print(sum)
print(flag)