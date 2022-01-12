import matplotlib.pyplot as plt
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
from pyecharts.commons.utils import JsCode

data = pd.DataFrame(pd.read_csv('/home/hadoop/文档/JAVA可视化/gdp.csv', header=0, index_col=0))

def mix(data):  # 2019年末常住人口、人均GDP  柱状图+折线
    col_c = list(data.loc[:, '省份'])
    col_avg = list(data.loc[:, '人均GDP'])
    print(col_avg)
    col_pop = list(data.loc[:, '2019年末常住人口'])
    # 测试代码!!!!!!!!!!!!!!
    print(col_pop)
    from pyecharts import options as opts
    from pyecharts.charts import Bar, Grid, Line

    bar = (
        Bar()
            .add_xaxis(["{}省".format(i) for i in col_c])
            .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
            color="#d14a61",
        )
            .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color="#5793f3",
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="蒸发量",
                type_="value",
                min_=0,
                max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            )
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
            .set_global_opts(
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
            ],
            yaxis_opts=opts.AxisOpts(
                name="降水量",
                min_=0,
                max_=250,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            ),
            title_opts=opts.TitleOpts(title="Grid-Overlap-多 X/Y 轴示例"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="25%"),
        )
    )

    line = (
        Line()
            .add_xaxis(["{}省".format(i) for i in col_c])
            .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar1 = (
        Bar()
            .add_xaxis(["{}省".format(i) for i in col_c])
            .add_yaxis(
            "蒸发量 1",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            color="#d14a61",
            xaxis_index=1,
            yaxis_index=3,
        )
            .add_yaxis(
            "降水量 2",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            color="#5793f3",
            xaxis_index=1,
            yaxis_index=3,
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="蒸发量",
                type_="value",
                min_=0,
                max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            )
        )
            .extend_axis(

            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
            .set_global_opts(
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
            ],
            xaxis_opts=opts.AxisOpts(grid_index=1),
            yaxis_opts=opts.AxisOpts(
                name="降水量",
                min_=0,
                max_=250,
                position="right",
                offset=80,
                grid_index=1,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="65%"),
        )
    )

    line1 = (
        Line()
            .add_xaxis(["{}省".format(i) for i in col_c])
            .add_yaxis(
            "平均温度 1",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
            xaxis_index=1,
            yaxis_index=5,
        )
    )

    overlap_1 = bar.overlap(line)
    overlap_2 = bar1.overlap(line1)

    grid = (
        Grid(init_opts=opts.InitOpts(width="1800px", height="800px"))
            .add(
            overlap_1, grid_opts=opts.GridOpts(pos_right="58%"), is_control_axis_index=True
        )
        # .add(overlap_2, grid_opts=opts.GridOpts(pos_left="58%"), is_control_axis_index=True)

    )
    from pyecharts import options as opts
    from pyecharts.charts import Bar, Line
    from pyecharts.faker import Faker

    v1 = col_pop
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    v3 = col_avg

    bar = (
        Bar()
            .add_xaxis(col_c)
            .add_yaxis("2019年末常住人口数", v1)

            # .add_yaxis("降水量", v2)
            .extend_axis(
            yaxis=opts.AxisOpts(name='人口数(单位/万）',
                                axislabel_opts=opts.LabelOpts(formatter="{value} ")
                                )
        )
            # .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

            .set_series_opts(
                itemstyle_opts={
                    "normal": {
                        "color": JsCode(
                            """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(0, 244, 255, 1)'
                    }, {
                        offset: 1,
                        color: 'rgba(0, 77, 167, 1)'
                    }], false)"""
                        ),
                        "barBorderRadius": [30, 30, 30, 30],
                        "shadowColor": "rgb(0, 160, 221)",
                    }
                }
            )
            # .reversal_axis()
            .set_global_opts(
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
            ],
            yaxis_opts=opts.AxisOpts(
                # is_inverse=True,
                min_=0,
                max_=int(100000*0.25),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            title_opts=opts.TitleOpts(title="中国各省GDP人口折线直方图"),
            # yaxis_opts=opts.AxisOpts(name='金额(单位/元)',
            #                          axislabel_opts=opts.LabelOpts(formatter="{value} ")),
        )
    )

    line = Line().add_xaxis(col_c).add_yaxis("人均GDP", v3, yaxis_index=1) \
        .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            min_=-200000,
            max_=40000,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    bar.overlap(line)
    # bar.render("overlap_bar_line.html")
    return bar


# gdp
def render_gdp1(dateID):

    return mix(data)


if __name__ == "__main__":
    render_gdp1(202002).render('GDP人口图.html')

