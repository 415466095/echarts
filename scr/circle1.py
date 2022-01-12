import pandas as pd
from pyecharts.charts import Map, Pie
import pyecharts.options as opts
from pyecharts.faker import Faker

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

def revenuechina(money):
    data=datarush(n)
    col_a=list(data.loc[:,'总金额'])
    col_s = list(data.loc[:, '收货地址'])
    set_col = set(col_s)
    # print(set_col)
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
        for j in range(len(col_a)):
            k=col_s[j]
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

            if(i==k):
                dict_cap[i]+=col_a[j]
                dict_cap[i] = round(dict_cap[i], 2)
    # print(dict_cap)
    list_data = dict_cap.items()
    list_data = [z for z in list_data]
    x=[]
    y=[]
    for i in range(len(list_data)):
        x.append(list_data[i][0])
        y.append(list_data[i][1])
###测试代码！！！！！！！！！
    # c=(
    #         Pie(init_opts=opts.InitOpts(width="1600px",height="1000px"))#图形的大小设置
    #         .add(
    #                 series_name="访问来源",
    #                 data_pair=[list(z)  for z in zip(x,y)],
    #                 radius=["15%","50%"],#饼图内圈和外圈的大小比例
    #                 center=["30%","40%"],#饼图的位置：左边距和上边距
    #                 label_opts=opts.LabelOpts(is_show=True),#显示数据和百分比
    #         )
    #         .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left",orient="vertical"))#图例在左边和垂直显示
    #         .set_series_opts(
    #         tooltip_opts=opts.TooltipOpts(
    #                 trigger="item",formatter="{a}<br/>{b}:{c}({d}%)"
    #         ),
    #     )
    # )
    def key(x):
        return x[1]
    v=Faker.choose()
    list1 = [list(z)  for z in zip(x, y)]
    list1.sort(key=lambda x: x[1])
    print(list1)
    c=(
        Pie()
    .add(
    "",
    [ list(z) for z in zip(x, y)],   # 两个值
        radius=["50%", "100%"],   # 大小
        center=["25%", "55%"],   # 位置
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),   # 不在图形上显示数据
    )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='各省2月化妆品销售饼状图',
                title_link=None,
                title_target=None,

                pos_left="50%",
                pos_right="80%",
                pos_top=260,

                pos_bottom=None,

                padding=[5, 10, 5, 10],
                item_gap=30,
                title_textstyle_opts=opts.TextStyleOpts(color="#535332"),
                # subtitle_textstyle_opts=opts.TextStyleOpts(color="blue"),
        )
        )
    )

    return c

def render_reveuechina(money,type=2):
    if (type == 2):
          return revenuechina(money)


if __name__ == "__main__":
    render_reveuechina(202002).render('中国化妆品2月销售饼状图.html')