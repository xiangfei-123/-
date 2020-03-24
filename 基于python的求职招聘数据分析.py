# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:51:41 2020

@author: lenovo
"""

import requests
import re
from pylab import mpl
import matplotlib.pyplot as plt

def getHTMLText(url):  #爬取网页
    try :
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text  #返回网页内容
    except:
        return ""

def getCity(html): #获取城市信息 
    city = re.findall(r'工作城市：<span>.*?<',html)
    return city 

def getNumber(html): #获取人数信息
    number = re.findall(r'招聘人数：<span>.*?<',html)
    return number

def getClassify(html): #获取职位类别信息
    classify = re.findall(r'类别：<span>.*?<',html)
    return classify

def getNumberSum(numberList): #对人数进行求和
    numberl = [] #存放获得的人数
    for i in numberList:
        num = re.findall(r'\d+',str(i))
        numberl.append(num)
    
    sum = 0
    
    for i in numberl:#对人数进行求和
        if type(i) is list:
            for j in i:
                sum = sum + int(j)
        else :
            continue
    return sum

def nmgNumber(cityList,numberList): #内蒙古各盟市招聘人数图
    hl_number = []
    
    xa_number = []
    
    tl_number = []
    
    cf_number = []
    
    xl_number = []
    
    wl_number = []
    
    hh_number = []
    
    bt_number = []
    
    by_number = []
    
    er_number = []
    
    wh_number = []
    
    al_number = []  #存放各盟市的人数
    
    for i in range(6500): #对获取到的信息进行按盟市分类获得各盟市的人数
        b = str(cityList[i])
        if b == "['工作城市：<span>内蒙古 - 呼伦贝尔市<']":
            hl_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 兴安盟<']":
            xa_number.append(numberList[i]) 
            
        elif b == "['工作城市：<span>内蒙古 - 通辽市<']":
            tl_number.append(numberList[i]) 
            
        elif b == "['工作城市：<span>内蒙古 - 赤峰市<']":
            cf_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 锡林郭勒盟<']":
            xl_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 乌兰察布市<']":
            wl_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 呼和浩特市<']":
            hh_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 包头市<']":
            bt_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 巴彦淖尔市<']":
            by_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 鄂尔多斯市<']":
            er_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 乌海市<']":
            wh_number.append(numberList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 阿拉善盟<']":
            al_number.append(numberList[i])
        else :
             continue
    
    #对各盟市的人数进行求和
    
    hlNumSum = getNumberSum(hl_number)
    
    xaNumSum = getNumberSum(xa_number)
    
    tlNumSum = getNumberSum(tl_number)
    
    cfNumSum = getNumberSum(cf_number)
    
    xlNumSum = getNumberSum(xl_number)
    
    wlNumSum = getNumberSum(wl_number)
    
    hhNumSum = getNumberSum(hh_number)
    
    btNumSum = getNumberSum(bt_number)
    
    byNumSum = getNumberSum(by_number)
    
    erNumSum = getNumberSum(er_number)
    
    whNumSum = getNumberSum(wh_number)
    
    alNumSum = getNumberSum(al_number)
    
     #显示中文
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
    
 
    name_list = ["呼伦贝尔市","兴安盟","通辽市","赤峰市","锡林郭勒盟",
                 "乌兰察布市","呼和浩特市","包头市","巴彦淖尔市","鄂尔多斯市",
                 "乌海市","阿拉善盟"]
    num_list = [hlNumSum,xaNumSum,tlNumSum,cfNumSum,xlNumSum,wlNumSum,hhNumSum,
                btNumSum,byNumSum,erNumSum,whNumSum,alNumSum]
    plt.bar(range(len(num_list)),num_list,color='gb',tick_label=name_list)
    plt.title("内蒙古各盟市招聘人数")
    plt.show()
            
def  nmgNewsSum(cityList): #内蒙古各盟市招聘信息数图
    
    hl_city = []
    
    xa_city = []

    tl_city = []

    cf_city = []

    xl_city = []

    wl_city = []

    hh_city = []

    bt_city = []

    by_city = []

    er_city = []

    wh_city = []

    al_city = [] #存放各盟市的招聘信息
    
    for i in range(6500):#对招聘信息按盟市分类
        b = str(cityList[i])
        if b == "['工作城市：<span>内蒙古 - 呼伦贝尔市<']":
            hl_city.append(cityList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 兴安盟<']":
            xa_city.append(cityList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 通辽市<']":
            tl_city.append(cityList[i])
             
        elif b == "['工作城市：<span>内蒙古 - 赤峰市<']":
            cf_city.append(cityList[i])
          
        elif b == "['工作城市：<span>内蒙古 - 锡林郭勒盟<']":
            xl_city.append(cityList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 乌兰察布市<']":
            wl_city.append(cityList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 呼和浩特市<']":
            hh_city.append(cityList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 包头市<']":
            bt_city.append(cityList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 巴彦淖尔市<']":
            by_city.append(cityList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 鄂尔多斯市<']":
            er_city.append(cityList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 乌海市<']":
            wh_city.append(cityList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 阿拉善盟<']":
            al_city.append(cityList[i])
           
        else :
             continue
         
        #对各盟市的招聘信息数进行统计    
            
    hlSum = len(hl_city)
         
    xaSum = len(xa_city)
         
    tlSum = len(tl_city)
         
    cfSum = len(cf_city)
         
    xlSum = len(xl_city)
         
    wlSum = len(wl_city)
         
    hhSum = len(hh_city)
         
    btSum = len(bt_city)
         
    bySum = len(by_city)
         
    erSum = len(er_city)
         
    whSum = len(wh_city)
         
    alSum = len(al_city)
    
     #显示中文
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
 
    name_list = ["呼伦贝尔市","兴安盟","通辽市","赤峰市","锡林郭勒盟",
                 "乌兰察布市","呼和浩特市","包头市","巴彦淖尔市","鄂尔多斯市",
                 "乌海市","阿拉善盟"]
    num_list = [hlSum,xaSum,tlSum,cfSum,xlSum,wlSum,hhSum,
                btSum,bySum,erSum,whSum,alSum]
    plt.bar(range(len(num_list)),num_list,color='gb',tick_label=name_list)
    plt.title("内蒙古各盟市招聘信息数")
    plt.show()
    
    
    
def classify(classify,cityname): #生成各行业招聘信息数图

    sc_class = []
    
    rl_class = []
    
    nl_class = []
    
    cc_class = []
    
    xs_class = []
    
    jt_class = []
    
    sj_class = []
    
    dq_class = []
    
    yl_class = []
    
    jd_class = []
    
    jy_class = []
    
    ms_class = []
  
    wl_class = []
    
    jr_class= []
    
    jz_class = []
    
    bj_class = []
    
    jg_class = []
    
    qt_class = []
#存放各行业的招聘信息
    
    for i in range(len(classify)):#对招聘信息按行业分类
        b = str(classify[i])
        if b == "['类别：<span>市场/公关类<']" :
            sc_class.append(classify[i])
            
        elif b == "['类别：<span>人力资源/行政/后勤/经营管理类<']" :
            rl_class.append(classify[i])
            
        elif b == "['类别：<span>农/林/牧/渔业类<']" :
            nl_class.append(classify[i])
            
        elif b == "['类别：<span>仓储/物流/运输类<']" :
            cc_class.append(classify[i])

        elif b == "['类别：<span>销售/零售/客户服务类<']" :
            xs_class.append(classify[i])

        elif b == "['类别：<span>建筑/交通/房地产/装修/物业服务类<']":
            jt_class.append(classify[i])

        elif b == "['类别：<span>财务/审计/统计类<']":
            sj_class.append(classify[i])

        elif b == "['类别：<span>电气/电子/电器/仪器/仪表类<']":
            dq_class.append(classify[i])

        elif b == "['类别：<span>医疗/卫生/制药/生物类<']":
            yl_class.append(classify[i])

        elif b == "['类别：<span>酒店/餐饮/旅游/社会服务类<']":
            jd_class.append(classify[i])

        elif b == "['类别：<span>教育/科研/咨询/法律类<']" :
            jy_class.append(classify[i])

        elif b == "['类别：<span>美术/设计/创意类<']" :
            ms_class.append(classify[i])

        elif b == "['类别：<span>计算机/互联网/通信类<']" :
            wl_class.append(classify[i])

        elif b == "['类别：<span>金融/保险类<']" :
            jr_class.append(classify[i])

        elif b == "['类别：<span>兼职/临时/培训生/储备干部<']":
            jz_class.append(classify[i])

        elif b == "['类别：<span>编辑/文案/翻译/传媒类<']":
            bj_class.append(classify[i])

        elif b == "['类别：<span>技工类<']" :
            jg_class.append(classify[i])

        else :
            qt_class.append(classify[i])

    #对各行业的招聘数统计
    sc = len(sc_class)
    rl = len(rl_class)
    nl = len(nl_class)
    cc = len(cc_class)
    xs = len(xs_class)
    jt = len(jt_class)
    sj = len(sj_class)
    dq = len(dq_class)
    yl = len(yl_class)
    jd = len(jd_class)
    jy = len(jy_class)
    ms = len(ms_class)
    wl = len(wl_class)
    jr = len(jr_class)
    jz = len(jz_class)
    bj = len(bj_class)
    jg = len(jg_class)
    qt = len(qt_class)
    
    #显示中文
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
    
    name_list = ["市场/公关","人力/行政","农牧业","仓储/物流","销售类",
                 "建筑/交通","财务/审计","电气类","医疗类","酒店餐饮",
                 "美术/设计","教育/法律","计算机/网络","金融类",
                 "兼职/培训","编辑/文案","技工类","其他"]
    num_list = [sc,rl,nl,cc,xs,jt,sj,dq,yl,jd,jy,ms,wl,jr,jz,bj,jg,qt]
    plt.bar(range(len(num_list)),num_list,color='gb',tick_label=name_list)
    plt.title(cityname + "各行业招聘信息数")
    plt.show()
    
    
def classifyNum(classify,number,cityname):#绘制各行业招聘人数图

    #存放各行业的招聘人数
    sc_num = []
    
    rl_num = []
    
    nl_num = []
    
    cc_num = []
    
    xs_num = []
    
    jt_num = []
    
    sj_num = []
    
    dq_num = []
    
    yl_num = []
    
    jd_num = []
    
    jy_num = []
    
    ms_num = []
    
    wl_num = []
    
    jr_num = []
    
    jz_num = []
    
    bj_num = []
    
    jg_num = []
    
    qt_num = []
    
    for i in range(len(classify)):#获取各行业的人数
        b = str(classify[i])
        if b == "['类别：<span>市场/公关类<']" :
            sc_num.append(number[i])
            
        elif b == "['类别：<span>人力资源/行政/后勤/经营管理类<']" :
            rl_num.append(number[i])
            
        elif b == "['类别：<span>农/林/牧/渔业类<']" :
            nl_num.append(number[i])
            
        elif b == "['类别：<span>仓储/物流/运输类<']" :
            cc_num.append(number[i])
            
        elif b == "['类别：<span>销售/零售/客户服务类<']" :
            xs_num.append(number[i])
            
        elif b == "['类别：<span>建筑/交通/房地产/装修/物业服务类<']":
            jt_num.append(number[i])
            
        elif b == "['类别：<span>财务/审计/统计类<']":
            sj_num.append(number[i])
            
        elif b == "['类别：<span>电气/电子/电器/仪器/仪表类<']":
            dq_num.append(number[i])
            
        elif b == "['类别：<span>医疗/卫生/制药/生物类<']":
            yl_num.append(number[i])
            
        elif b == "['类别：<span>酒店/餐饮/旅游/社会服务类<']":
            jd_num.append(number[i])
            
        elif b == "['类别：<span>教育/科研/咨询/法律类<']" :
            jy_num.append(number[i])
            
        elif b == "['类别：<span>美术/设计/创意类<']" :
            ms_num.append(number[i])
            
        elif b == "['类别：<span>计算机/互联网/通信类<']" :
            wl_num.append(number[i])
            
        elif b == "['类别：<span>金融/保险类<']" :
            jr_num.append(number[i])
            
        elif b == "['类别：<span>兼职/临时/培训生/储备干部<']":
            jz_num.append(number[i])
            
        elif b == "['类别：<span>编辑/文案/翻译/传媒类<']":
            bj_num.append(number[i])
            
        elif b == "['类别：<span>技工类<']" :
            jg_num.append(number[i])
            
        else :
            qt_num.append(number[i])
        
   #对各行业人数求和     
    scNum = getNumberSum(sc_num)
    rlNum = getNumberSum(rl_num)
    nlNum = getNumberSum(nl_num)
    ccNum = getNumberSum(cc_num)
    xsNum = getNumberSum(xs_num)
    jtNum = getNumberSum(jt_num)
    sjNum = getNumberSum(sj_num)
    dqNum = getNumberSum(dq_num)
    ylNum = getNumberSum(yl_num)
    jdNum = getNumberSum(jd_num)
    jyNum = getNumberSum(jy_num)
    msNum = getNumberSum(ms_num)
    wlNum = getNumberSum(wl_num)
    jrNum = getNumberSum(jr_num)
    jzNum = getNumberSum(jz_num)
    bjNum = getNumberSum(bj_num)
    jgNum = getNumberSum(jg_num)
    qtNum = getNumberSum(qt_num)
    
    
     #显示中文
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
    
    
    name_list = ["市场/公关","人力/行政","农牧业","仓储/物流","销售类",
                 "建筑/交通","财务/审计","电气类","医疗类","酒店餐饮",
                 "美术/设计","教育/法律","计算机/网络","金融类",
                 "兼职/培训","编辑/文案","技工类","其他"]
    num_list = [scNum,rlNum,nlNum,ccNum,xsNum,jtNum,sjNum,dqNum,ylNum,
                jdNum,jyNum,msNum,wlNum,jrNum,jzNum,bjNum,jgNum,qtNum]
    plt.bar(range(len(num_list)),num_list,color='gb',tick_label=name_list)
    plt.title(cityname + "各行业招聘人数")
    plt.show()
    
    
    
def nmgClass(cityList,classifyList):  #内蒙古各行业招聘数图
    
    nmg_class = [] #存放内蒙古的招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取属于内蒙古的招聘类别
        if b == "['工作城市：<span>内蒙古 - 呼伦贝尔市<']":
            nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 兴安盟<']":
             nmg_class.append(classifyList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 通辽市<']":
             nmg_class.append(classifyList[i])
             
        elif b == "['工作城市：<span>内蒙古 - 赤峰市<']":
             nmg_class.append(classifyList[i])
          
        elif b == "['工作城市：<span>内蒙古 - 锡林郭勒盟<']":
             nmg_class.append(classifyList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 乌兰察布市<']":
             nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 呼和浩特市<']":
             nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 包头市<']":
             nmg_class.append(classifyList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 巴彦淖尔市<']":
             nmg_class.append(classifyList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 鄂尔多斯市<']":
             nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 乌海市<']":
             nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 阿拉善盟<']":
             nmg_class.append(classifyList[i])
  
        else :
            continue
    cityname = "内蒙古"
    classify(nmg_class,cityname)

    
            
def nmgClassNum(cityList,classifyList,numberList):#内蒙古各行业招聘人数图 
    
    nmg_num = []
    nmg_class = []#存放属于内蒙古的招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取属于内蒙古的招聘信息、人数
        if b == "['工作城市：<span>内蒙古 - 呼伦贝尔市<']":
            nmg_num.append(numberList[i])
            nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 兴安盟<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 通辽市<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
             
        elif b == "['工作城市：<span>内蒙古 - 赤峰市<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
          
        elif b == "['工作城市：<span>内蒙古 - 锡林郭勒盟<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 乌兰察布市<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 呼和浩特市<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 包头市<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 巴彦淖尔市<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
           
        elif b == "['工作城市：<span>内蒙古 - 鄂尔多斯市<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 乌海市<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
            
        elif b == "['工作城市：<span>内蒙古 - 阿拉善盟<']":
             nmg_num.append(numberList[i])
             nmg_class.append(classifyList[i])
  
        else :
            continue
    cityname = "内蒙古"
    classifyNum(nmg_class,nmg_num,cityname)
    

    
        
def hlbrClass(cityList,classifyList):  #呼伦贝尔市各行业招聘数图
    
    hlbr_class = [] #存放呼伦贝尔市的招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取属于呼伦贝尔市的招聘类别
        if b == "['工作城市：<span>内蒙古 - 呼伦贝尔市<']":
            hlbr_class.append(classifyList[i])
        else :
            continue
    cityname = "呼伦贝尔市"
    classify(hlbr_class,cityname)
    
            
def hlbrClassNum(cityList,classifyList,numberList):#呼伦贝尔市各行业招聘人数图 
    
    hlbr_num = []
    hlbr_class = []#存放属于呼伦贝尔市的招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取属于呼伦贝尔市的招聘信息、人数
        if b == "['工作城市：<span>内蒙古 - 呼伦贝尔市<']":
            hlbr_num.append(numberList[i])
            hlbr_class.append(classifyList[i])
  
        else :
            continue

    cityname = "呼伦贝尔市"
    classifyNum(hlbr_class,hlbr_num,cityname)           


def xamClass(cityList,classifyList):  #兴安盟各行业招聘数图
    
    xam_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别
        if b == "['工作城市：<span>内蒙古 - 兴安盟<']":
             xam_class.append(classifyList[i])
        else :
            continue
    cityname = "兴安盟"
    classify(xam_class,cityname)
    
            
def xamClassNum(cityList,classifyList,numberList):#兴安盟各行业招聘人数图 
    
    xam_num = []
    xam_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
      
        if b == "['工作城市：<span>内蒙古 - 兴安盟<']":
             xam_num.append(numberList[i])
             xam_class.append(classifyList[i])
        else :
            continue

    cityname = "兴安盟"
    classifyNum(xam_class,xam_num,cityname)


def tlsClass(cityList,classifyList):  #通辽市各行业招聘数图
    
    tls_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别   
        if b == "['工作城市：<span>内蒙古 - 通辽市<']":
             tls_class.append(classifyList[i])
        else :
            continue
    cityname = "通辽市"
    classify(tls_class,cityname)
    
            
def tlsClassNum(cityList,classifyList,numberList):#通辽市各行业招聘人数图 
    
    tls_num = []
    tls_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
       
        if b == "['工作城市：<span>内蒙古 - 通辽市<']":
             tls_num.append(numberList[i])
             tls_class.append(classifyList[i])
        else :
            continue


    cityname = "通辽市"
    classifyNum(tls_class,tls_num,cityname)
        
  



def cfsClass(cityList,classifyList):  #赤峰市各行业招聘数图
    
    cfs_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别
        if b == "['工作城市：<span>内蒙古 - 赤峰市<']":
             cfs_class.append(classifyList[i])
        else :
            continue
    cityname = "赤峰市"
    classify(cfs_class,cityname)
    
            
def cfsClassNum(cityList,classifyList,numberList):#赤峰市各行业招聘人数图 
    
    cfs_num = []
    cfs_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
        
        if b == "['工作城市：<span>内蒙古 - 赤峰市<']":
             cfs_num.append(numberList[i])
             cfs_class.append(classifyList[i])
        else :
            continue

    cityname = "赤峰市"
    classifyNum(cfs_class,cfs_num,cityname)




def xlglClass(cityList,classifyList):  #锡林郭勒盟各行业招聘数图
    
    xlgl_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别
        if b == "['工作城市：<span>内蒙古 - 锡林郭勒盟<']":
             xlgl_class.append(classifyList[i])
        else :
            continue
    cityname = "锡林郭勒盟"
    classify(xlgl_class,cityname)
    
            
def xlglClassNum(cityList,classifyList,numberList):#锡林郭勒盟各行业招聘人数图 
    
    xlgl_num = []
    xlgl_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
        
        if b == "['工作城市：<span>内蒙古 - 锡林郭勒盟<']":
             xlgl_num.append(numberList[i])
             xlgl_class.append(classifyList[i])
        else :
            continue

    cityname = "锡林郭勒盟"
    classifyNum(xlgl_class,xlgl_num,cityname)




def wlcbClass(cityList,classifyList):  #乌兰察布市各行业招聘数图
    wlcb_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别
        if b == "['工作城市：<span>内蒙古 - 乌兰察布市<']":
             wlcb_class.append(classifyList[i])
        else :
            continue
    cityname = "乌兰察布市"
    classify(wlcb_class,cityname)
    
            
def wlcbClassNum(cityList,classifyList,numberList):#乌兰察布市各行业招聘人数图 
    
    wlcb_num = []
    wlcb_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
        
        if b == "['工作城市：<span>内蒙古 - 乌兰察布市<']":
             wlcb_num.append(numberList[i])
             wlcb_class.append(classifyList[i])
        else :
            continue

    cityname = "乌兰察布市"
    classifyNum(wlcb_class,wlcb_num,cityname)



def hhhtClass(cityList,classifyList):  #呼和浩特市各行业招聘数图
    
    hhht_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别   
        if b == "['工作城市：<span>内蒙古 - 呼和浩特市<']":
             hhht_class.append(classifyList[i])
        else :
            continue
    cityname = "呼和浩特市"
    classify(hhht_class,cityname)
    
            
def hhhtClassNum(cityList,classifyList,numberList):#呼和浩特市各行业招聘人数图 
    
    hhht_num = []
    hhht_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
        if b == "['工作城市：<span>内蒙古 - 呼和浩特市<']":
             hhht_num.append(numberList[i])
             hhht_class.append(classifyList[i])   
        else :
            continue

    cityname = "呼和浩特市"
    classifyNum(hhht_class,hhht_num,cityname)



def btsClass(cityList,classifyList):  #包头市各行业招聘数图
    
    bts_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别
        if b == "['工作城市：<span>内蒙古 - 包头市<']":
             bts_class.append(classifyList[i])
        else :
            continue
    cityname = "包头市"
    classify(bts_class,cityname)
    
            
def btsClassNum(cityList,classifyList,numberList):#包头市各行业招聘人数图 
    
    bts_num = []
    bts_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
       
        if b == "['工作城市：<span>内蒙古 - 包头市<']":
             bts_num.append(numberList[i])
             bts_class.append(classifyList[i])
        else :
             continue

    cityname = "包头市"
    classifyNum(bts_class,bts_num,cityname)




def byneClass(cityList,classifyList):  #巴彦淖尔市各行业招聘数图
    
    byne_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别
       
        if b == "['工作城市：<span>内蒙古 - 巴彦淖尔市<']":
             byne_class.append(classifyList[i])
        else :
            continue
    cityname = "巴彦淖尔市"
    classify(byne_class,cityname)
    
            
def byneClassNum(cityList,classifyList,numberList):#巴彦淖尔市各行业招聘人数图 
    
    byne_num = []
    byne_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
        
        if b == "['工作城市：<span>内蒙古 - 巴彦淖尔市<']":
             byne_num.append(numberList[i])
             byne_class.append(classifyList[i])
        else :
            continue

    cityname = "巴彦淖尔市"
    classifyNum(byne_class,byne_num,cityname)




def eedsClass(cityList,classifyList):  #鄂尔多斯市各行业招聘数图
    eeds_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别
       
        if b == "['工作城市：<span>内蒙古 - 鄂尔多斯市<']":
             eeds_class.append(classifyList[i])
        else :
            continue
    cityname = "鄂尔多斯市"
    classify(eeds_class,cityname)
    
            
def eedsClassNum(cityList,classifyList,numberList):#鄂尔多斯市各行业招聘人数图 
    
    eeds_num = []
    eeds_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
       
        if b == "['工作城市：<span>内蒙古 - 鄂尔多斯市<']":
             eeds_num.append(numberList[i])
             eeds_class.append(classifyList[i])
        else :
            continue

    cityname = "鄂尔多斯市"
    classifyNum(eeds_class,eeds_num,cityname)




def whsClass(cityList,classifyList):  #乌海市各行业招聘数图   
    whs_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别
       
        if b == "['工作城市：<span>内蒙古 - 乌海市<']":
             whs_class.append(classifyList[i])
        else :
            continue
    cityname = "乌海市"
    classify(whs_class,cityname)
    
            
def whsClassNum(cityList,classifyList,numberList):#乌海市各行业招聘人数图 
    
    whs_num = []
    whs_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
     
        if b == "['工作城市：<span>内蒙古 - 乌海市<']":
             whs_num.append(numberList[i])
             whs_class.append(classifyList[i])
        else :
            continue

    cityname = "乌海市"
    classifyNum(whs_class,whs_num,cityname)




def alsmClass(cityList,classifyList):  #阿拉善盟各行业招聘数图
    
    alsm_class = [] #存放招聘类别
    for i in range(6500):
        b = str(cityList[i])#获取招聘类别 
        if b == "['工作城市：<span>内蒙古 - 阿拉善盟<']":
             alsm_class.append(classifyList[i])
  
        else :
            continue
    cityname = "阿拉善盟"
    classify(alsm_class,cityname)
    
            
def alsmClassNum(cityList,classifyList,numberList):#阿拉善盟各行业招聘人数图 
    
    alsm_num = []
    alsm_class = []#存放招聘信息、人数
    for i in range(6500):
        b = str(cityList[i])#获取招聘信息、人数
           
        if b == "['工作城市：<span>内蒙古 - 阿拉善盟<']":
             alsm_num.append(numberList[i])
             alsm_class.append(classifyList[i])
        else :
            continue

    cityname = "阿拉善盟"
    classifyNum(alsm_class,alsm_num,cityname)



def main():
    start_url = 'https://job.nmbys.cn/job/view/id/'
    cityD = {}
    numberD = {}
    classifyD= {}
    for i in range(6500):
        try :
            url = start_url + str(int('608831') + i)
            html = getHTMLText(url)
            
            cityD[i] = getCity(html)
            cityList = list(cityD.values())
            
            numberD[i] = getNumber(html)
            numberList = list(numberD.values())

            classifyD[i] = getClassify(html)
            classifyList = list(classifyD.values())
            
        except:
            continue
    nmgNumber(cityList,numberList)
    nmgNewsSum(cityList)
    
    nmgClass(cityList,classifyList)
    nmgClassNum(cityList,classifyList,numberList)
    
    hlbrClass(cityList,classifyList)
    hlbrClassNum(cityList,classifyList,numberList)
    
    xamClass(cityList,classifyList)
    xamClassNum(cityList,classifyList,numberList)
    
    tlsClass(cityList,classifyList)
    tlsClassNum(cityList,classifyList,numberList)
    
    cfsClass(cityList,classifyList)
    cfsClassNum(cityList,classifyList,numberList)

    xlglClass(cityList,classifyList)
    xlglClassNum(cityList,classifyList,numberList)
    
    wlcbClass(cityList,classifyList)
    wlcbClassNum(cityList,classifyList,numberList)
    
    hhhtClass(cityList,classifyList)
    hhhtClassNum(cityList,classifyList,numberList)
    
    btsClass(cityList,classifyList)
    btsClassNum(cityList,classifyList,numberList)
    
    byneClass(cityList,classifyList)
    byneClassNum(cityList,classifyList,numberList)
    
    eedsClass(cityList,classifyList)
    eedsClassNum(cityList,classifyList,numberList)
    
    whsClass(cityList,classifyList)
    whsClassNum(cityList,classifyList,numberList)
    
    alsmClass(cityList,classifyList)
    alsmClassNum(cityList,classifyList,numberList)
   #1111111111111111111111111111  
main()