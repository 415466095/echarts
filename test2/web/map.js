// function map1() {
//     var chartDom = document.getElementById('main1');
//     var myChart = echarts.init(chartDom);
//     var option;
//     var base = +new Date(1968, 9, 3);
//     var oneDay = 24 * 3600 * 1000;
//     var date = [];
//
//     var data = [Math.random() * 300];
//
//     for (var i = 1; i < 20000; i++) {
//         var now = new Date(base += oneDay);
//         date.push([now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'));
//         data.push(Math.round((Math.random() - 0.5) * 20 + data[i - 1]));
//     }
//
//     option = {
//         tooltip: {
//             trigger: 'axis',
//             position: function (pt) {
//                 return [pt[0], '10%'];
//             }
//         },
//         title: {
//             left: 'center',
//             text: '大数据量面积图',
//         },
//         toolbox: {
//             feature: {
//                 dataZoom: {
//                     yAxisIndex: 'none'
//                 },
//                 restore: {},
//                 saveAsImage: {}
//             }
//         },
//         xAxis: {
//             type: 'category',
//             boundaryGap: false,
//             data: date
//         },
//         yAxis: {
//             type: 'value',
//             boundaryGap: [0, '100%']
//         },
//         dataZoom: [{
//             type: 'inside',
//             start: 0,
//             end: 10
//         }, {
//             start: 0,
//             end: 10
//         }],
//         series: [
//             {
//                 name: '模拟数据',
//                 type: 'line',
//                 symbol: 'none',
//                 sampling: 'lttb',
//                 itemStyle: {
//                     color: 'rgb(255, 70, 131)'
//                 },
//                 areaStyle: {
//                     color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
//                         offset: 0,
//                         color: 'rgb(255, 158, 68)'
//                     }, {
//                         offset: 1,
//                         color: 'rgb(255, 70, 131)'
//                     }])
//                 },
//                 data: data
//             }
//         ]
//     };
//
//     myChart.setOption(option);
// }
// function map2()
// {
//     var chartDom = document.getElementById('main2');
//     var myChart = echarts.init(chartDom);
//     var option;
//
//     option = {
//         xAxis: {
//             type: 'category',
//             data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
//         },
//         yAxis: {
//             type: 'value'
//         },
//         series: [{
//             data: [120, 200, 150, 80, 70, 110, 130],
//             type: 'bar',
//             showBackground: true,
//             backgroundStyle: {
//                 color: 'rgba(180, 180, 180, 0.2)'
//             }
//         }]
//     };
//
//     myChart.setOption(option);
// }