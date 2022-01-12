import matplotlib.pyplot as plt
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
from pyecharts import options as opts
from pyecharts.charts import Bar

data = pd.DataFrame(pd.read_csv('/home/hadoop/文档/JAVA可视化/gdp.csv', header=0, index_col=0))

def gdp3(datt):
    col_c = list(data.loc[:, '省份'])
    col_2019 = list(data.loc[:, '2019年GDP'])
    col_2020 = list(data.loc[:, '2020年GDP'])
    print(col_2020)
    print(col_2019)
    f = 1.5
    w = 1200 * f
    h = 500 * f
    c = (
        Bar(init_opts=opts.InitOpts(width="%dpx"%w, height="%dpx"%h))
            .add_xaxis(col_c)
            .add_yaxis("2019年GDP", col_2019)
            .add_yaxis("2020年GDP", col_2020)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各省2019与2020GDP柱状对比图(单位/万亿)"),
            datazoom_opts=opts.DataZoomOpts(),
        )
            # .render("bar_datazoom_slider.html")
    )
    bar = (
        Bar(init_opts=opts.InitOpts(width="7000px", height="4000px"))
            .add_xaxis(col_c)
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                # 选坐标轴
                type_='category',
                min_=0,
                max_=50,


                # splitline_opts=opts.SplitLineOpts(is_show=True)
            )
        )
            .add_yaxis("l2", col_2019)
            .add_yaxis("l3", col_2020)
            .set_global_opts(title_opts=opts.TitleOpts(title="各省2019与2020GDP柱状对比图", subtitle="我是副标题"),
                             toolbox_opts=opts.BrushOpts(), )
    )
    return c


def render_gdp3(dateID):
        return gdp3(data)

if __name__ == "__main__":
    render_gdp3(202002).render('1920年gdp对比柱状图.html')