import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='class', charset='utf8')
cursor = db.cursor()


def load_data_set(pat):
    try:
        lists = []
        for i in range(1, pat):
            sql = " select 条目 from eat where 关联度=%d" % i
            cursor.execute(sql)
            label_set = list(cursor.fetchall())
            list_for_row = [i[0] for i in label_set]
            lists.append(list_for_row)
    except:
        # 发生错误时回滚
        db.rollback()
    return lists

def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1  # 候选1项集


def has_infrequent_subset(Ck_item, Lksub1):
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True


def apriori_gen(Lksub1, k):  # 候选产生算法
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k - 2] == l2[0:k - 2]:  # 只有最后一项不同时，生成下一候选项
                Ck_item = list_Lksub1[i] | list_Lksub1[j]  # 并集
                if has_infrequent_subset(Ck_item, Lksub1):  # 检查该候选项的子集是否都在Lk-1中
                    Ck.add(Ck_item)
    return Ck


def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):
    Lk = set()  # 频繁K项集
    item_count = {}  # 项集：项集频数
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    for item in item_count:
        if (item_count[item]) >= min_support:  # 判断支持度是否大于最小支持度，支持度=事务频数/总事务
            Lk.add(item)
            support_data[item] = item_count[item]
    return Lk


def generate_L(data_set, k, min_support):
    support_data = {}  # 保存键值对，频繁项集：支持度
    C1 = create_C1(data_set)  # 创建候选1项集  {frozenset({'凉皮'}), frozenset({'可乐'}), frozenset({'冰峰'}), frozenset({'肉夹馍'}), frozenset({'果啤'}), frozenset({'米线'}), frozenset({'菜夹馍'})}
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)  # 频繁1项集
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k + 1):
        Ci = apriori_gen(Lksub1, i)  # Lk-1生成候选k项集
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)  # 候选k项集生成频繁k项集
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data


def generate_big_rules(L, support_data, min_conf):
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in big_rule_list:
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list


# def big_rule():
#     data_set = load_data_set(15)
#     L, support_data = generate_L(data_set, k=2, min_support=3)  # 求频繁项集，k为最大频繁项的最大容纳，返回频繁项集和支持度数据集
#     big_rules_list = generate_big_rules(L, support_data, min_conf=0.5)  # 求强关联规则
#     # 输出
#     for Lk in L:
#         print("=" * 50)
#         print("频繁" + str(len(list(Lk)[0])) + "-项集\t\t\t\tsupport")
#         for freq_set in Lk:
#             print(freq_set, '\t', support_data[freq_set])
#     print("=" * 50)
#     print("关联规则：")
#     BIG = []
#     for item in big_rules_list:
#         BIG.append([str(list(item[0])[0]), str(list(item[1])[0]), item[2]])
#     big_rules_list = BIG
#
#     # 获取列表的第二个元素
#     def takeSecond(elem):
#         return -elem[2]
#
#     print(type(big_rules_list[0][2]))
#     # 指定第二个元素排序
#     big_rules_list.sort(key=takeSecond)
#     print(big_rules_list[0:3])
#     for item in big_rules_list:
#         print("rules:", item[0], "=>", item[1], '\t', "conf: ", item[2])

def takeThird(elem):
    return -elem[2]

def big_rule(goods):
        sql = "select 关联度 from eat"
        cursor.execute(sql)
        data = cursor.fetchall()
        data = len(set(data)) + 1
        data_set = load_data_set(data)  # 加载数据集
        L, support_data = generate_L(data_set, k=2, min_support=1)  # 求频繁项集，k为最大频繁项的最大容纳，返回频繁项集和支持度数据集
        big_rules_list = generate_big_rules(L, support_data, min_conf=0.3)  # 求强关联规则
        # 输出
        returnString1 = \
            """
        """
        returnString1 += "=" * 22
        returnString1 += "<PRE></PRE>%s<PRE></PRE>" % "购买成功"
        returnString1 += "=" * 22
        returnString1 += "<PRE></PRE>买过%s的人还买了：<PRE></PRE>" % goods
        # 指定第三个元素排序
        BIG = []
        SAVE = []
        for item in big_rules_list:
            BIG.append([str(list(item[0])[0]), str(list(item[1])[0]), item[2]])
        big_rules_list = BIG
        big_rules_list.sort(key=takeThird)
        for item in big_rules_list:
            if goods in item[0]:
                SAVE.append(item[1])
                # returnString1 += "%s---推荐指数%d<br/>" % (item[1], int(float(item[2]) * 5))
                # returnString1 += "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;conf: %s</td></tr>" % item[2]

        if len(SAVE) > 3:
            SAVE = SAVE[0:3]

        print(SAVE)
        return SAVE