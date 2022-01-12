import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts

n = "/home/hadoop/文档/JAVA可视化/tmall_order_report1.csv"
def datarush(FILE):
    # 清洗数据
    col = ('总金额', '买家实际支付金额', '收货地址',
           '订单付款时间', '退款金额')
    data = pd.read_csv(FILE, usecols=col)
    newdata = data.dropna(axis=0, how='any')
    newdata = pd.DataFrame(newdata)
    newdata['总金额'] = newdata['总金额'].astype(float)
    newdata['买家实际支付金额'] = newdata['买家实际支付金额'].astype(float)
    newdata['退款金额'] = newdata['退款金额'].astype(float)
    return newdata


def render_mapcountChina_current(dateId):
    data = datarush(n)
    col_s = list(data.loc[:, '收货地址'])
    col_p = list(data.loc[:, '总金额'])
    col_d = list(data.loc[:, '订单付款时间'])
    col_b=[]
    for j in range(len(col_d)):
         col_b.append(int(col_d[j][0:10].replace('-', '')))
    # print(col_b)

    set_col = set(col_s)
    dict_cap = {}
    for i in set_col:
        if i[-1] == "省":
            i = i[:-1]
        elif i == "宁夏回族自治区":
            i = "宁夏"
        elif i == "内蒙古自治区":
            i = "内蒙古"
        elif i == "西藏自治区":
            i = "西藏"
        elif i == "广西壮族自治区":
            i = "广西"
        elif i == "新疆维吾尔自治区":
            i = "新疆"

        dict_cap[i] = 0

    for i in dict_cap:
        for j in range(0, len(col_s)):
            k = col_s[j]

            if k[-1] == "省":
                k = k[:-1]
            elif k=="宁夏回族自治区":
                k="宁夏"
            elif k == "内蒙古自治区":
                k = "内蒙古"
            elif k == "西藏自治区":
                k = "西藏"
            elif k == "广西壮族自治区":
                k = "广西"
            elif k == "新疆维吾尔自治区":
                k = "新疆"

            # if (i == k or i[0:2]==k):
            if (i == k ):
                if(col_b[j]==dateId):
                    dict_cap[i] += col_p[j]
                    dict_cap[i] = round(dict_cap[i], 2)
                # print(dict_cap)
    # # [('湖北', 48206), ('广东', 1241), ('河南', 1169), ('浙江', 1145), ..., ('澳门', 10), ('西藏', 1)]
    list_data = dict_cap.items()
    list_data = [z for z in list_data]
    print(list_data)
    # print(list_data)
    c = (
        Map()
            .add('', list_data, 'china')
            .set_global_opts(
            title_opts=opts.TitleOpts(title='中国2月网购化妆品价格分布图' + str(dateId)),
            visualmap_opts=opts.VisualMapOpts(
                                              is_show=True,
                                              split_number=6,
                                              is_piecewise=True,  # 是否为分段型
                                              pos_top='center',
                                              pieces=[
                                                  {'min': 10000, 'color': '#7f1818'},  # 不指定 max
                                                  {'min': 1000, 'max':9999},
                                                  {'min': 500, 'max': 1000},
                                                  {'min': 400, 'max': 500},
                                                  {'min': 300, 'max': 400},
                                                  {'min': 200, 'max': 300},
                                                  {'min': 100, 'max': 200},
                                                  {'min': 50, 'max': 100},
                                                  {'min': 0, 'max': 50}
                                              ]
                                              ),
        )
    )
    return c


def render_mapcountChina(dateId):
    print('sssssssssssss')
    return render_mapcountChina_current(dateId)


if __name__ == "__main__":
    render_mapcountChina(202002).render('中国地图.html')
