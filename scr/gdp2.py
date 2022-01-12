import ssl

import pyecharts.options as opts
from pyecharts.charts import Map
from pyecharts.datasets import register_url
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context
register_url("https://echarts-maps.github.io/echarts-china-cities-js")




data = pd.DataFrame(pd.read_csv('/home/hadoop/文档/JAVA可视化/gdp.csv', header=0, index_col=0))

col_c = list(data.loc[:, '省份'])
col_2020 = list(data.loc[:, '2020年GDP'])
# col_pop = list(data.loc[:, '2019年末常住人口'])
list_data = [z for z in zip(col_c, col_2020)]
print(list_data)
c = (
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
        .add(
        series_name="中国2020年GDP热力分布图",
        maptype='china',

        data_pair=list_data,
        # name_map=NAME_MAP_DATA,
        is_map_symbol_show=False,
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="",
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}<br/>{c} 万亿"
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=min(col_2020),
            max_=max(col_2020),
            range_text=["High", "Low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
        .render("中国2020年GDP热力分布图.html")
)
