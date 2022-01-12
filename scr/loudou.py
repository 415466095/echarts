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
        # col_s = list(newdata.loc[:, '收货地址'])
    col_p = list(data.loc[:, '总金额'])
    # set_col = set(col_s)
    # dict_cap = {}
    list1 = []
    count = [0, 0, 0, 0, 0]
    for j in range(len(col_p)):

        # for j in range(0,len(col_p)):
        #     if i==col_s[j]:
        if col_p[j] > 0 and col_p[j] <= 50:
            count[0] += 1

        elif col_p[j] > 50 and col_p[j] <= 100:
            count[1] = count[1] + 1
        elif col_p[j] > 100 and col_p[j] <= 500:
            count[2] = count[2] + 1
        elif col_p[j] > 500 and col_p[j] <= 1000:
            count[3] = count[3] + 1
        else:
            count[4] = count[4] + 1
    list1 = count


    list_data = [z for z in list1]
    # print(list_data)
    from pyecharts.charts import Bar, Page, Line
    from pyecharts import options as opts
    from pyecharts.charts import Funnel
    from pyecharts import options as opts
    cate = ['50元及以下', '50到100元', '100到500元', '500-1000元', '1000元以上']
    data = list_data
    funnel = (Funnel()
              .add("用户数", [list(z) for z in zip(cate, data)],
                   sort_='ascending',
                   label_opts=opts.LabelOpts(position="inside"))
              .set_global_opts(title_opts=opts.TitleOpts(title="2月化妆品价格销量", subtitle="单/(单位)"))
              )
    return funnel


def render_applicationloudou(dateId, type=2):     #漏斗图代码

    if (type == 2):
        return render_daysale_current(dateId)


if __name__ == "__main__":
    # render_applicationloudou(20200201)
    render_applicationloudou(20200201).render('中国淘宝2月订单价格区域漏斗图.html')