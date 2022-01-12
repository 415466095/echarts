var worldCloud = echarts.init(document.getElementById('worldCloud'), 'white', {renderer: 'canvas'});
var slider2 = document.getElementById('slider2');
// var test = "q"
$(
    function () {
        // fetchchinaMapData(chinamap);
        // fetchchinaMapData1(chinamap1);
        fetchWord(worldCloud);
    }
);


worldCloud.on('click', function(params) {
    // console.log(params.name);
    // // window.open(params.data.url);
    // window.open('https://www.baidu.com/s?wd=' + encodeURIComponent(params.value));
    $.ajax({
        type:"GET",
        url:"/my_function",
        dataType:"json",
        data:"index="+params.name,
        success:function (data) {
            // alert("ok")
            // alert(data.new1)
            // alert(data.i)
            // console.log('name', name_);
            // var age = data.name;
            // alert(data.j)
            $("#121").html(data.index)
            $("#100").html(data.i)
            var obj = document.getElementById("aaa");
            obj.src = data.j;
            $("#122").html(data.new1)
            $("#101").html(data.i1)
            var obj1 = document.getElementById("bbb");
            obj1.src = data.j1;
            $("#123").html(data.new2)
            $("#102").html(data.i2)
            var obj2 = document.getElementById("ccc");
            obj2.src = data.j2;
            $("#124").html(data.new3)
            $("#103").html(data.i3)
            var obj3 = document.getElementById("ddd");
            obj3.src = data.j3;
        },
        error:function (re) {
            alert("暂无推荐！")
        }
    })

});

document.getElementById('slider2').onchange =  function changeDate(){
    // fetchworldMapData(worldmap);
    fetchWord(worldCloud);
}
function fetchWord(chart) {
    var colorList = [[
    '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
    '#ff69b4', '#ba55d3', '#cd5c5c', '#a6ff00', '#40e0d0',
    '#1e90ff', '#ff6347', '#7b68ee', '#d0648a', '#ffd700',
    '#6b8e23', '#4ea397', '#3cb371', '#b8860b', '#7bd9a5'
    ],
    [
    '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
    '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
    '#1e90ff', '#ff6347', '#7b68ee', '#00fa9a', '#ffd700',
    '#6b8e23', '#ff00ff', '#3cb371', '#b8860b', '#30e0e0'
    ],
    [
    '#929fff', '#9de0ff', '#ffa897', '#af87fe', '#7dc3fe',
    '#bb60b2', '#433e7c', '#f47a75', '#009db2', '#024b51',
    '#0780cf', '#765005', '#e75840', '#26ccd8', '#3685fe',
    '#9977ef', '#f5616f', '#f7b13f', '#f9e264', '#50c48f'
    ]][2];


option = {
    // 图表标题
    title: {
        show:true,//显示策略，默认值true,可选为：true（显示） | false（隐藏）
        text: '旅游美食超话',//主标题文本，'\n'指定换行
        x: 'center',        // 水平安放位置，默认为左对齐，可选为：
                          // 'center' ¦ 'left' ¦ 'right'
                          // ¦ {number}（x坐标，单位px）
        y: 'bottom',             // 垂直安放位置，默认为全图顶端，可选为：
                          // 'top' ¦ 'bottom' ¦ 'center'
                          // ¦ {number}（y坐标，单位px）
        //textAlign: null          // 水平对齐方式，默认根据x设置自动调整
        backgroundColor: 'rgba(255,255,255,255)',
        borderColor: '#ccc',    // 标题边框颜色
        borderWidth: 0,         // 标题边框线宽，单位px，默认为0（无边框）
        padding: 5,             // 标题内边距，单位px，默认各方向内边距为5，
                                // 接受数组分别设定上右下左边距，同css
        itemGap: 10,            // 主副标题纵向间隔，单位px，默认为10，
        textStyle: {
            fontSize: 18,
            fontWeight: 'bolder',
            color: '#003366'        // 主标题文字颜色
        },
        subtextStyle: {
            color: '#aaa'        // 副标题文字颜色
        }
    },
    backgroundColor: '#f1f1f1',
    tooltip: {},
    animationDurationUpdate: function(idx) {
        // 越往后的数据延迟越大
        return idx * 100;
    },
    animationEasingUpdate: 'bounceIn',
    color: ['#fff', '#fff', '#fff'],
    series: [{
        type: 'graph',
        layout: 'force',
        force: {
            repulsion: 250,
            edgeLength: 10
        },
        roam: true,
        label: {
            normal: {
                show: true
            }
        },
        data: [
          {"name": "凉皮", "value": 2058124, "symbolSize": 143, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[1], "color": colorList[1] } } },
{"name": "肉夹馍", "value": 1751491, "symbolSize": 132, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[2], "color": colorList[2] } } },
{"name": "平遥牛肉", "value": 1642587, "symbolSize": 128, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[3], "color": colorList[3] } } },
{"name": "冰峰", "value": 1524287, "symbolSize": 123, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[4], "color": colorList[4] } } },
{"name": "泡馍", "value": 1435649, "symbolSize": 119, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[5], "color": colorList[5] } } },
{"name": "大唐芙蓉园", "value": 1301903, "symbolSize": 114, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[6], "color": colorList[6] } } },
{"name": "华山", "value": 1150224, "symbolSize": 107, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[7], "color": colorList[7] } } },
{"name": "大碗", "value": 1008954, "symbolSize": 100, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[8], "color": colorList[8] } } },
{"name": "炸酱面", "value": 966638, "symbolSize": 98, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[9], "color": colorList[9] } } },
{"name": "烤鸭", "value": 942399, "symbolSize": 97, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[10], "color": colorList[10] } } },
{"name": "狗不理", "value": 777198, "symbolSize": 88, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[11], "color": colorList[11] } } },
{"name": "葱油煎饼", "value": 726378, "symbolSize": 85, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[12], "color": colorList[12] } } },
{"name": "牛肉干", "value": 624773, "symbolSize": 79, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[13], "color": colorList[13] } } },
{"name": "羊杂", "value": 620858, "symbolSize": 78, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[14], "color": colorList[14] } } },
{"name": "烤全羊", "value": 565363, "symbolSize": 75, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[15], "color": colorList[15] } } },
{"name": "大盘鸡", "value": 534676, "symbolSize": 73, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[16], "color": colorList[16] } } },
{"name": "杀猪菜", "value": 504716, "symbolSize": 71, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[17], "color": colorList[17] } } },
{"name": "红肠", "value": 494101, "symbolSize": 70, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[18], "color": colorList[18] } } },
{"name": "麻婆豆腐", "value": 440445, "symbolSize": 66, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[19], "color": colorList[19] } } },
{"name": "火锅", "value": 403092, "symbolSize": 63, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[0], "color": colorList[0] } } },
{"name": "石锅鸡", "value": 399236, "symbolSize": 63, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[1], "color": colorList[1] } } },
{"name": "酥油茶", "value": 390904, "symbolSize": 62, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[2], "color": colorList[2] } } },
{"name": "生煎包", "value": 368912, "symbolSize": 60, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[3], "color": colorList[3] } } },
{"name": "葱油拌面", "value": 368366, "symbolSize": 60, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[4], "color": colorList[4] } } },
{"name": "西红柿鸡蛋汤", "value": 368296, "symbolSize": 60, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[5], "color": colorList[5] } } },
{"name": "五台山", "value": 359468, "symbolSize": 59, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[6], "color": colorList[6] } } },
{"name": "云冈石窟", "value": 295436, "symbolSize": 54, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[7], "color": colorList[7] } } },
{"name": "天安门", "value": 284210, "symbolSize": 53, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[8], "color": colorList[8] } } },
{"name": "颐和园", "value": 283813, "symbolSize": 53, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[9], "color": colorList[9] } } },
{"name": "天津之眼", "value": 283766, "symbolSize": 53, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[10], "color": colorList[10] } } },
{"name": "北海", "value": 256506, "symbolSize": 50, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[11], "color": colorList[11] } } },
{"name": "宝成奇石园", "value": 250184, "symbolSize": 50, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[12], "color": colorList[12] } } },
{"name": "响沙湾", "value": 247223, "symbolSize": 49, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[13], "color": colorList[13] } } },
{"name": "呼伦贝尔", "value": 237377, "symbolSize": 48, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[14], "color": colorList[14] } } },
{"name": "喀什噶尔老城", "value": 220219, "symbolSize": 46, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[15], "color": colorList[15] } } },
{"name": "喀纳斯", "value": 209512, "symbolSize": 45, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[16], "color": colorList[16] } } },
{"name": "冰雪大世界", "value": 192396, "symbolSize": 43, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[17], "color": colorList[17] } } },
{"name": "翠华山", "value": 184315, "symbolSize": 42, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[18], "color": colorList[18] } } },
{"name": "九寨沟", "value": 174247, "symbolSize": 41, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[19], "color": colorList[19] } } },
{"name": "乐山大佛", "value": 171994, "symbolSize": 41, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[0], "color": colorList[0] } } },
{"name": "布达拉宫", "value": 164751, "symbolSize": 40, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[1], "color": colorList[1] } } },
{"name": "珠穆朗玛峰", "value": 155213, "symbolSize": 39, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[2], "color": colorList[2] } } },
{"name": "东方明珠", "value": 153323, "symbolSize": 39, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[3], "color": colorList[3] } } },
{"name": "黄浦江", "value": 152564, "symbolSize": 39, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[4], "color": colorList[4] } } },
{"name": "兵马俑", "value": 147858, "symbolSize": 38, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[5], "color": colorList[5] } } },
{"name": "武侯祠", "value": 138773, "symbolSize": 37, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[6], "color": colorList[6] } } },
{"name": "金沙滩", "value": 134038, "symbolSize": 36, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[7], "color": colorList[7] } } },
{"name": "泰山", "value": 131590, "symbolSize": 36, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[8], "color": colorList[8] } } },
{"name": "崂山", "value": 115787, "symbolSize": 34, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[9], "color": colorList[9] } } },
{"name": "亚龙湾", "value": 100309, "symbolSize": 31, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 10, "shadowColor": colorList[10], "color": colorList[10] } } },
            ]
    }]
}
chart.setOption(option);
}