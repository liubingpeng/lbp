# homework1
import urllib.parse
str=urllib.parse.urlencode({'pw':'你好'})
print(str)
def.maopao(str1):
    strlist=str1.strip().split()
    numlist=[]
    for x in strlist:
        numlist.append(int(x))
    for i in range(len(numlist)-1):
        for i in range(len(numlist)-i-1):
            if numlist[j]>munlist[j+1]:
                numlist[j],numlist[j+1]=numlist[j+i],numlist[j]
                return numlist
response=urllib.request.urlopen(str1)
HTML=response.read().decode('utf8')
print(HTML)

# howework2
var app=angular.module('myApp',['ngRoute'])
app.config(['$routeProvider',funxtion($routeProvider){
    $routeProvider.when('/ali',{template:'<div>阿里在二楼!</div>',
    controller:'demoController'
    })
    .when('/baidu',{template:'<div>百度在一楼</div>'})
    }])
    
