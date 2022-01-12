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

def backmoney(newdata):
    col_bm = list(newdata.loc[:, '退款金额'])
    col_s = list(newdata.loc[:, '收货地址'])
    sum = 0
    for i in col_bm:
        sum += i
    set_s = set(col_s)
    dict_cap1=[]
    for i in set_s:
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
        dict_cap1.append(i)
    dict_backmoney = {}
    count =0
    for i in dict_cap1:
        dict_backmoney[i] = 0
    for j in col_s:
        if j [-1] == "省":
            j = j [:-1]
        elif j == "宁夏回族自治区":
            j = "宁夏"
        elif j == "内蒙古自治区":
            j = "内蒙古"
        elif j == "西藏自治区":
            j = "西藏"
        elif j == "广西壮族自治区":
            j = "广西"
        elif j == "新疆维吾尔自治区":
            j = "新疆"
        dict_backmoney[j] = dict_backmoney[j] + col_bm[count] / sum
        count = count + 1
    for j in dict_cap1:
        dict_backmoney[j] = round(dict_backmoney[j],3)
    sum = 0
    for i in dict_cap1:
        sum += dict_backmoney[i]
    # print(sum)
    return dict_backmoney

def paybak(money):
    data=datarush(n)
    col_a=list(data.loc[:,'总金额'])
    col_s = list(data.loc[:, '收货地址'])
    col_t = list(data.loc[:, '退款金额'])
    set_col = set(col_s)
    dict_cap=[]
    # data1=backmoney(data)
    # print(set_col)
    dict_cap1 = {}
    dict_cap2 = {}
    dict_cap3 = {}
    dict_cap4 = {}
    # print((set_col))
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
        dict_cap.append(i)
    date2=backmoney(data)
    listForN = ["黑龙江" , "吉林" , "北京" , "天津" , "河北" , "山东" , "辽宁" , "山西" , "河南"]
    listForS = ["江苏" , "浙江" , "上海" , "湖北" , "湖南" , "江西" , "福建" , "贵州" , "重庆" , "广东" , "广西" , "海南" , "云南" , "贵州" , "安徽"]
    listForw = ["陕西" , "内蒙古","甘肃","宁夏","新疆"]
    listForx = ["青海" ,"西藏" , "四川"]
    dateall=date2.items()
    dateall=[z for z in dateall]
    count=0
    for i in listForN:
        for j in range(len(dateall)):
            if(i==dateall[j][0]):
                dict_cap1[i]=0
                dict_cap1[i]+=dateall[j][1]
    # print(dict_cap1)
    for i in listForS:
        for j in range(len(dateall)):
            if(i==dateall[j][0]):
                dict_cap2[i]=0
                dict_cap2[i]+=dateall[j][1]
    # print(dict_cap2)
    for i in listForw:
        for j in range(len(dateall)):
            if(i==dateall[j][0]):
                dict_cap3[i]=0
                dict_cap3[i]+=dateall[j][1]
    # print(dict_cap3)
    for i in listForx:
        for j in range(len(dateall)):
            if(i==dateall[j][0]):
                dict_cap4[i]=0
                dict_cap4[i]+=dateall[j][1]
    print(dict_cap1)
    c=(
        Pie()
    .add(
    "",
        [list(z) for z in dict_cap1.items()],
        center=["20%", "30%"],   # 位置
        radius=[60, 80],   # 每个饼图内外圈的大小
    )
        #     .set_global_opts(
        #     title_opts=opts.TitleOpts(title="退货比例环状(北方地区)"),
        #     legend_opts=opts.LegendOpts(
        #         type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        #     ),
        # )
    .add(
    "",
        [list(z) for z in dict_cap2.items()],
        center=["55%", "30%"],
        radius=[60, 80],
    )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="退货比例环状图(1排左:北方地区 1排右:南方地区 2排左:西北地区 2排右:川藏地区)"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="60%", pos_left="80%", orient="vertical"
            ),

        )
    .add(
    "",
        [list(z) for z in dict_cap3.items()],
        center=["20%", "70%"],
        radius=[60, 80],
    )
    .add(
    "",
        [list(z) for z in dict_cap4.items()],
        center=["55%", "70%"],
        radius=[60, 80],
    )


    )
    return c



def render_paybackchina(money,type=2):
    if (type == 2):
          return paybak(money)


if __name__ == "__main__":
    render_paybackchina(202002).render('退款比例图.html')
    # .render('各地区退款比例扇形图.html')