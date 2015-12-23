#encoding:utf-8
import requests
import os,sys
import config
reload(sys)
sys.setdefaultencoding("utf-8")
import requests
import json
poiCache = {}
nameCache = []

htmlStr = '''

<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>%(title)s</title>
</head>
<body>

    <div id="main" style="height:600px;width:900px;margin:20px auto;"></div>
    <script src="http://echarts.baidu.com/build/dist/echarts-all.js"></script>
    <script type="text/javascript">
        var myChart = echarts.init(document.getElementById('main'));
        var option = {
            backgroundColor: '#1b1b1b',
            color: ['gold', 'aqua', 'lime'],
            title: {
                text: '%(title)s',
                subtext: '%(subtitle)s',
                x: 'center',
                textStyle: {
                    color: '#fff'
                }
            },
            tooltip: {
                trigger: 'item',
                formatter: '{b}'
            },

            series: [{
                name: '全国',
                type: 'map',
                hoverable: false,
                mapType: 'china',
                itemStyle: {
                    normal: {
                        borderColor: 'rgba(100,149,237,1)',
                        borderWidth: 0.5,
                        areaStyle: {
                            color: '#1b1b1b'
                        }
                    }
                },
                data: [],

                geoCoord: %(alldata)s
            }, {
                name: '足迹',
                type: 'map',
                mapType: 'china',
                data: [],
                markLine: {
                    smooth: true,
                    effect: {
                        show: true,
                        scaleSize: 1,
                        period: 30,
                        color: '#fff',
                        shadowBlur: 10
                    },
                    itemStyle: {
                        normal: {
                            borderWidth: 1,
                            lineStyle: {
                                type: 'solid',
                                shadowBlur: 10
                            }
                        }
                    },
                    data: %(linedata)s
                },
                markPoint: {
                    symbol: 'emptyCircle',
                    symbolSize: function(v) {
                        return 10 + v / 10
                    },
                    effect: {
                        show: true,
                        shadowBlur: 0
                    },
                    itemStyle: {
                        normal: {
                            label: {
                                show: false
                            }
                        },
                        emphasis: {
                            label: {
                                position: 'top'
                            }
                        }
                    },
                    data: %(pointdata)s
                }
            }]
        };
        myChart.setOption(option);
    </script>
</body>

</html>

'''

def getPoint(name):
    key = 'q5mTrTGzCSVq5QmGpI9y18Bo'
    url = 'http://api.map.baidu.com/geocoder/v2/?output=json&ak=%s&address=%s'%(key,name)
    try:
        r = requests.get(url)
        res = r.json()

        if res.get('result',None):
            loc = res['result']['location']
            poiCache[name] = [loc['lng'],loc['lat']]
    except:
        print '获取不到%s的经纬度信息'%(name)

def gen(config):
    title = config['title']
    subtitle = config['subtitle']
    footTmp = []
    for foot in config['foot']:
        tmp = foot.split()
        for i in range(len(tmp)-1):
            footTmp.append([{'name':tmp[i]},{"name":tmp[i+1]}])
        for f in foot.split():
            if f not in poiCache:
                getPoint(f)
    for name in poiCache:
        nameCache.append({'name':name})

    obj = {
        'title':title,
        'subtitle':subtitle,
        'alldata':json.dumps(poiCache),
        'linedata':json.dumps(footTmp),
        'pointdata':json.dumps(nameCache)
    }

    with open('output.html','w') as f:
        f.write(htmlStr % obj)       
if __name__ =="__main__":
    gen(config.config)
