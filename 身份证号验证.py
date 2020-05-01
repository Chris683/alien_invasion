import tkinter as tk  # 使用Tkinter前需要先导入
import re

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('Chris')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('700x500')

# 第4步，在图形界面上设定标签
l = tk.Label(window, text='身份证号验证', font=('宋体', 30), width=40, height=2)
l1 = tk.Label(window, text='身份证号：', font=('Arial', 16), width=40, height=2)

# 第5步，放置标签
l.place(x=-80, y=0, anchor='nw')
l1.place(x=-100, y=80, anchor='nw')

# 第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show=None, font=('Arial', 20),)
e.place(x=200, y=90, anchor='nw')


# 第5步，定义两个触发事件时的函数check和delete
def check():        # 按钮‘检查’对应的函数
    t.delete(1.0, 'end')
    IDcard = e.get()
    if len(IDcard) != 18:
        var = '号码：' + IDcard + "\n身份证号码位数不对!\n错误的身份证号码.\n请重新输入！\n"
    else:
        IDcard_add = IDcard[0:6]     # 身份证前6位，对应归属地
        IDcard_birth = IDcard[6:14]  # 身份证中间8位，对应出生日期
        IDcard_sex = IDcard[14:17]   # 身份证15，,16,17位，对应性别

        area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁",
                "22": "吉林", "23": "黑龙江", "31": "上海", "32": "江苏", "33": "浙江", "34": "安徽",
                "35": "福建", "36": "江西", "37": "山东", "41": "河南", "42": "湖北","43": "湖南",
                "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州",
                "53": "云南", "54": "西藏", "61": "陕西", "62": "甘肃", "63": "青海", "64": "宁夏",
                "65": "新疆", "71": "台湾", "81": "香港", "82": "澳门", "91": "国外"}

        # 地区校验
        if IDcard[0:2] not in area.keys():
            var = '号码：' + IDcard + '\n身份证地区非法!\n错误的身份证号码\n'
        else:
            year = IDcard_birth[0:4]   # 出生年份
            month = IDcard_birth[4:6]  # 出生月份
            day = IDcard_birth[6:8]    # 出生日

            # 出生日期的合法性检查
            # 闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]
            # |[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
            # 平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]
            # |[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
            if (int(year) % 4 == 0 or (int(year) % 100 == 0 and int(year) % 4 == 0)):
                ereg = re.compile('[1-9][0-9]{5}((19[0-9]{2})|(20[0-1][0-8]))((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]'
                                  '|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))'
                                  '[0-9]{3}[0-9Xx]$')       # //闰年出生日期的合法性正则表达式
            else:
                ereg = re.compile('[1-9][0-9]{5}((19[0-9]{2})|(20[0-1][0-8]))((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]'
                                  '|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8])'
                                  ')[0-9]{3}[0-9Xx]$')      # //平年出生日期的合法性正则表达式
            # //测试出生日期的合法性
            if (re.match(ereg, IDcard)):
                IDcard_check = IDcard[17]  # 身份证最后一位
                W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]   # 逐位权数
                IDcard_CHECK = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']  # 身份证检验位
                IDcard_sum = 0                                              # 定义累加和
                for i in range(0, 17):
                    IDcard_sum = IDcard_sum + int(IDcard[i]) * W[i]         # 逐位加权求和
                IDcard_Check = IDcard_sum % 11  # 取余数
                if IDcard_check != IDcard_CHECK[IDcard_Check]:              # 和检验位对比
                    var = '号码：' + IDcard + '\n身份证号码校验错误!\n错误的身份证号码\n'
                else:
                    if int(IDcard_sex) % 2 == 0:
                        var = "正确的身份证号码! \n" + '号码：' + IDcard + '\n地区：' + area[IDcard[0: 2]] + \
                              '\n生日：' + year + '年' + month + '月' + day + '日' + "\n 性别：女\n"
                    else:

                        var = "正确的身份证号码! \n" + '号码：' + IDcard + '\n地区：' + area[IDcard[0: 2]] + \
                              "\n生日: " + year + '年' + month + '月' + day + '日' + "\n性别：男 \n"
            else:
                var = '号码：' + IDcard + '\n身份证号码出生日期超出范围或含有非法字符!\n错误的身份证号码\n'
    t.insert('insert', var)       # 显示输出
    e.delete(0, 'end')

# 第6步，创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text='检查', width=10, height=2, command = check)
b1.place(x=550, y=80, anchor='nw')

# 第7步，创建并放置一个多行文本框text用以显示
t = tk.Text(window, font=('宋体', 20), width=38, height=8)
t.place(x=100, y=210, anchor='nw')

# 第8步，主窗口循环显示
window.mainloop() 111111111111111111
