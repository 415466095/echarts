 // function show(){
 //     alert("nmsl");
 // }
 // 基于准备好的dom，初始化echarts实例

 //
 // // 使用刚指定的配置项和数据显示图表。
 // myChart.setOption(option);
 // }
 // function show() {
 //     var myChart = echarts.init(document.getElementById('main'));
 //
 //     // 指定图表的配置项和数据
 //     var option = {
 //         title: {
 //             text: '第一个 ECharts 实例'
 //         },
 //         tooltip: {},
 //         legend: {
 //             data:['销量']
 //         },
 //         xAxis: {
 //             data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
 //         },
 //         yAxis: {},
 //         series: [{
 //             name: '销量',
 //             type: 'bar',
 //             data: [5, 20, 36, 10, 10, 20]
 //         }]
 //     };
 //
 //     // 使用刚指定的配置项和数据显示图表。
 //     myChart.setOption(option);
 // }
 function show() {
     var chartDom = document.getElementById('main');

     var myChart = echarts.init(chartDom);
     var option;

     // Generate data
     var category = [];
     var dottedBase = +new Date();
     var lineData = [];
     var barData = [];

     for (var i = 0; i < 20; i++) {
         var date = new Date(dottedBase += 3600 * 24 * 1000);
         category.push([
             date.getFullYear(),
             date.getMonth() + 1,
             date.getDate()
         ].join('-'));
         var b = Math.random() * 200;
         var d = Math.random() * 200;
         barData.push(b)
         lineData.push(d + b);
     }


     // option
     option = {
         backgroundColor: '#0f375f',
         tooltip: {
             trigger: 'axis',
             axisPointer: {
                 type: 'shadow'
             }
         },
         legend: {
             data: ['line', 'bar'],
             textStyle: {
                 color: '#ccc'
             }
         },
         xAxis: {
             data: category,
             axisLine: {
                 lineStyle: {
                     color: '#ccc'
                 }
             }
         },
         yAxis: {
             splitLine: {show: false},
             axisLine: {
                 lineStyle: {
                     color: '#ccc'
                 }
             }
         },
         series: [
             {
             name: 'line',
             type: 'line',
             smooth: true,
             showAllSymbol: true,
             symbol: 'emptyCircle',
             symbolSize: 15,
             data: lineData
         }, {
             name: 'bar',
             type: 'bar',
             barWidth: 10,
             itemStyle: {
                 barBorderRadius: 5,
                 color: new echarts.graphic.LinearGradient(
                     0, 0, 0, 1,
                     [
                         {offset: 0, color: '#14c8d4'},
                         {offset: 1, color: '#43eec6'}
                     ]
                 )
             },
             data: barData
         }, {
             name: 'line',
             type: 'bar',
             barGap: '-100%',
             barWidth: 10,
             itemStyle: {
                 color: new echarts.graphic.LinearGradient(
                     0, 0, 0, 1,
                     [
                         {offset: 0, color: 'rgba(20,200,212,0.5)'},
                         {offset: 0.2, color: 'rgba(20,200,212,0.2)'},
                         {offset: 1, color: 'rgba(20,200,212,0)'}
                     ]
                 )
             },
             z: -12,
             data: lineData
         }, {
             name: 'dotted',
             type: 'pictorialBar',
             symbol: 'rect',
             itemStyle: {
                 color: '#0f375f'
             },
             symbolRepeat: true,
             symbolSize: [12, 4],
             symbolMargin: 1,
             z: -10,
             data: lineData
         }]
     };

     myChart.setOption(option);
 }

