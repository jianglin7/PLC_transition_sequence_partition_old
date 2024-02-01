import pm4py
from pm4py.visualization.petri_net import visualizer as vis_factory
from pm4py.objects.petri_net.utils import petri_utils as utils
from pm4py.objects.petri_net.obj import PetriNet, Marking


# petri网处理类
class PetrinetHandler:
    # 构造函数
    def __init__(self, fName=''):
        self.mPetrinet = PetriNet(fName)
        self.mInitialMarking = Marking()
        self.mFinalMarking = Marking()


    # 获取库所集合
    def get_place_list(self):
        places = []
        for place in self.mPetrinet.places:
            input_transitions = sorted([arc.source.label for arc in place.in_arcs])
            output_transitions = sorted([arc.target.label for arc in place.out_arcs])
            places.append((input_transitions, output_transitions))
        return sorted(places)


    def __hash__(self):
        return hash(str(self.get_place_list()))


    def get_signature(self):
        places = {}
        initials, finals = set(), set()
        for place in self.mPetrinet.places:
            input_transitions = '{' + ','.join(
                sorted([arc.source.label for arc in place.in_arcs if arc.source.label is not None])) + '}'
            output_transitions = '{' + ','.join(
                sorted([arc.target.label for arc in place.out_arcs if arc.target.label is not None])) + '}'
            places[place] = f'({input_transitions}->{output_transitions})'
            if place in self.mInitialMarking:
                initials.add(places[place])
            if place in self.mFinalMarking:
                finals.add(places[place])
        silents = []
        for transition in self.mPetrinet.transitions:
            if transition.label is None:
                if len(transition.in_arcs) != 1 or len(transition.out_arcs) != 1:
                    raise ValueError('Invalid, since silent transition is not connected to exactly 2 places.')
                in_place = list(transition.in_arcs)[0].source
                out_place = list(transition.out_arcs)[0].target
                silents.append((places[in_place], places[out_place]))
        return set(places.values()), silents, initials, finals


    def equals_other_petrinet(self, other):
        signature1 = self.get_signature()
        signature2 = other.get_signature()

        return signature1 == signature2


    # 添加库所
    def addPlace(self, fName=''):
        place = PetriNet.Place(fName)
        self.mPetrinet.places.add(place)
        return place


    # 添加变迁
    def addTransition(self, fName='', fLabel=''):
        if fLabel == '':
            fLabel = fName
        transition = PetriNet.Transition(fName, fLabel)
        self.mPetrinet.transitions.add(transition)
        return transition


    # 添加弧
    def addArc(self, fSource, fTarget, fWeight=1):
        return utils.add_arc_from_to(fSource, fTarget, self.mPetrinet, fWeight)


    # 可视化
    def visualize(self, fExport=''):
        parameters = {'debug': True,'format': 'png'}
        gviz = vis_factory.apply(*self.get(), parameters=parameters)
        if fExport != '':
            vis_factory.save(gviz, fExport)
        else:
            vis_factory.view(gviz)


    # 获取petri网，返回一个元组，包括petri网、初始标记、结束标记
    def get(self):
        elements = self.mPetrinet, self.mInitialMarking, self.mFinalMarking
        return elements



# 构造petri网
# 参数1：库所集合
# 参数2：变迁集合
# 参数3：弧集合
# 参数4：初始标记
# 参数5：petri网名称
# 参数6：是否可视化
def build_petri_net(places, transitions, arcs, initials=None, petriNetName='', visualize=False):
    # 创建petri网
    petrinet = PetrinetHandler(petriNetName)

    # 添加所有变迁
    places = {p : petrinet.addPlace(p) for p in places}

    # 添加所有库所
    transitions = {t : petrinet.addTransition(t) for t in transitions}

    # 添加所有弧
    for arc in arcs:
        place, direction, transition = arc
        if direction == "to":
            petrinet.addArc(places[place], transitions[transition])
        elif direction == "from":
            petrinet.addArc(transitions[transition], places[place])

    # 设置初始标记及其令牌数量，这里令牌数量默认为1
    if initials is not None:
        for initial in initials:
            petrinet.mInitialMarking[places[initial]] = 1

    # 是否可视化
    if visualize:
        petrinet.visualize()

    return petrinet.get()



# 从关联矩阵中提取所有的变迁、库所、所有的变迁和库所之间的关系
def extract_pt_and_relationships(incidence_matrix):
    places = []
    transitions = []
    arcs = []

    num_rows, num_cols = len(incidence_matrix), len(incidence_matrix[0])

    # 提取库所
    for row_index in range(num_rows):
        place_name = f"p{row_index + 1}"
        places.append(place_name)

    # 提取变迁
    for col_index in range(num_cols):
        transition_name = f"t{col_index + 1}"
        transitions.append(transition_name)

    # 提取变迁和库所之间的关系
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            # 获取到关联矩阵的一个值
            value = incidence_matrix[row_index][col_index]
            if value != 0:
                # 提取变迁和库所之间的关系
                place_name = f"p{row_index + 1}"
                transition_name = f"t{col_index + 1}"
                direction = ''
                if value == 1:
                    direction = 'from'
                elif value == -1:
                    direction = 'to'
                arcs.append((place_name, direction, transition_name))

    return places, transitions , arcs




if __name__ == '__main__':
    # tup = getTestPetriNet(fVisualize=True)
    # print(tup)

    # 根据关联矩阵获取库所、变迁及其之间的关系
    incidence_matrix = [

        [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [ 0, 0,-1, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0,-1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 1, 0, 0, 0, 0, 1,-1, 0, 0, 0,-1, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0,-1],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0],
        [ 1,-1, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      # [ 1, 2, 3, 4, 5, 6, 7, 8  9  10 11 12 13 14 15]
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 1, 0],
        [ 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 1,-1, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 1, 0, 0, 0,-1, 0, 0, 0,-1, 0],
        [ 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,-1, 0, 0, 0]
    ]
    p,t,a = extract_pt_and_relationships(incidence_matrix)
    print(p)
    print(t)
    print(a)
    print(len(a))

    net,init,final = build_petri_net(places=p,transitions=t,arcs=a,visualize=False)
    # net,init,final = build_petri_net(places=p, transitions=t, arcs=a, visualize=False)

    # 显示petri网
    pm4py.view_petri_net(net,init,final)

    ## 平均拟合度计算
    log = pm4py.read_xes('D:/小七/app/py/code/Sequence_partition/Discovery/data.xes')
    # net, im, fm = pm4py.discover_petri_net_alpha(log)
    # pm4py.view_petri_net(net, im, fm)
    tbr = pm4py.conformance_diagnostics_token_based_replay(log, net, init, final)

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
    tbr_precision = pm4py.precision_token_based_replay(log, net, init, final)
    print(f"av_precision: {tbr_precision}")

    f_measure = 2 * (av_firness * tbr_precision) / (av_firness + tbr_precision)
    print(f"F-measure: {f_measure}")




