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

def render_daysale_current(dateId):
    data = datarush(n)
#     # col_a = list(newdata.loc[:, '订单付款时间'])
    col_d = list(data.loc[:, '订单付款时间'])
    col_b = []
    for j in range(len(col_d)):
        col_b.append(int(col_d[j][0:10].replace('-', '')))
    # print(col_b)
    # print('okok')
    # print(dateId)
    hours=[]
    days=[]
    for i in col_d:
        hours.append(int(i[11:13]))
        days.append(int(i[8:10]))
    set_hours = set(hours)
    set_days=set(days)
    dict_hours={}
    for i in set_hours:
        dict_hours[i]=0
    # for j in hours:
    #     dict_hours[j]=dict_hours[j]+1
        for j in range(len(col_d)):
            if(i==int(col_d[j][11:13])):
                # print(int(int(col_b[j][11:13])))
                # print(col_b[j])
                if(int(col_b[j])==dateId):
                    dict_hours[i]=dict_hours[i]+1
    list_data = dict_hours.items()
    list_data = [z for z in list_data]
    # print(list_data)
    # print(list_data)
    # print(list_data)
    from pyecharts.charts import Bar, Page, Line
    from pyecharts import options as opts

    x = []
    y = []
    j=0
    for i in list_data:
        x.append(list_data[j][0])
        y.append(list_data[j][1])
        j+=1

    c =(
        Line()
        # 设置x轴
        .add_xaxis(xaxis_data=x)
        # 设置y轴
        .add_yaxis(series_name='淘宝销量曲线', y_axis=y)
        # .add_yaxis(series_name='平台B2', y_axis=y2)
        # 数据项设置
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(name="单位(小时）"),
            yaxis_opts=opts.AxisOpts(name="销售量(个)"),
            title_opts=opts.TitleOpts(title='淘宝化妆品的销售情况'),
            legend_opts=opts.LegendOpts(is_show=True),
            tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross')
        )
    )

    return c
    # return dict_hours

def render_allday():
    data = datarush(n)
    col_b = list(data.loc[:, '订单付款时间'])
    days=[]
    tay=[]
    new=[]
    # print(col_b[0:10])
    for i in col_b:
        days.append(i[0:10])

    tay=set(days)
    for i in tay:
        new.append(i.replace('-', ''))
    # print(new)
    return new

def render_applicationsale(dateId, type=2):
    if (type == 2):
        return render_daysale_current(dateId)


if __name__ == "__main__":
    # render_applicationsale(20200201)
    # print(render_allday())
    render_applicationsale(202002).render('中国淘宝日每时销售.html')