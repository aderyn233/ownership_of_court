"""
11.20 周一 11、12、13
11.21 周二 1、2、3
11.22 周三 4、5、6
11.23 周四 7、8、9
11.24 周五 10、11、12

11.27 周一 13、1、2
11.28 周二 3、4、5
11.29 周三 6、7、8
11.30 周四 9、10、11
12.1 周五 12、13、1
......
"""

import datetime
from prettytable import PrettyTable

def get_weekday(date):  # 参数类型：string   e.g.2023-11-26
    """获取日期对应的星期几"""
    weekday = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return weekday

def get_owner(start_class):     # 参数类型：int，范围应当在[1,13]
    """获取从前往后的3个班级"""
    class_list = []
    for i in range(3):
        class_list.append(start_class)
        if start_class <= 12:
            start_class = start_class + 1
        elif start_class == 13:
            start_class = 1
    return class_list

def get_calender(today,start_class):
    """获取时间表"""
    start_date = today - datetime.timedelta(days=today.weekday())   #获取这周起始日期
    # print("起始日期",start_date)

    table = PrettyTable()
    table.field_names = ["日期", "星期", "归属班级"]

    for i in range(5):      # 获取这周每天的日期，星期，归属班级，并填入表中
        weekday = get_weekday(start_date.strftime("%Y-%m-%d")) + 1   #获取日期对应的星期几，由于周一对应的是0，周二对应的是1，周三对应的是2......所以在最后要加上1
        owner = get_owner(start_class)

        table.add_row([start_date,weekday,owner])   # 填表

        start_date = start_date + datetime.timedelta(days=1)  # 获取下一天的日期

        if start_class <= 10:   # 只有当start_class<=10的时候，start_class+3才不会超出13个班的界限
            start_class = start_class + 3
        else:   # 如果超出了13个班的界限
            start_class = start_class - 10

    return table

def get_next_owner(today):      # 参数为字符串，格式：2023-11-30
    """获取每周一的场地所属班级"""

    # 获取基准日期和基准日期当天的场地所属班级
    with open('standard_date.txt', 'r') as file:
        lines = file.readlines()
        standard_date = lines[0]    # 基准日期，这个取出来后会带一个换行，下一步把它去掉
        standard_date = standard_date[:10]  # 前十位是日期yyyy-mm-dd
        standard_court = lines[1]   # 基准日期当天的场地所属班级

    today = datetime.datetime.strptime(today,"%Y-%m-%d")    # 把字符串转换为datetime.datetime
    start_date = datetime.datetime.strptime(standard_date,"%Y-%m-%d")    # 基准日期
    # print(start_date)
    monday_of_this_week = today - datetime.timedelta(days=today.weekday())      # 获取该周第一天的日期
    # print(monday_of_this_week)
    duration = monday_of_this_week - start_date     #计算相差天数

    num_of_weeks = duration.days / 7     # 计算相隔周数
    next_owner = int(standard_court) + num_of_weeks * 2      # standard_court为基准日期当天的班级

    while next_owner > 13:
        next_owner = next_owner - 13

    return int(next_owner)

def get_this_and_next_week():
    """获取这周和下周的表格"""
    today = datetime.date.today()  # 当前日期，输出格式：2023-11-26，类型为datetime.date
    next_week = today + datetime.timedelta(days=7)  # 获取下一周某一天的日期

    print(get_calender(today, get_next_owner(today.strftime("%Y-%m-%d"))))
    print(get_calender(next_week, get_next_owner(next_week.strftime("%Y-%m-%d"))))
    return

if __name__ == '__main__':
    get_this_and_next_week()
    content = '''使用前请阅读README.md
查询格式为xxxx-xx-xx，例如2024-01-03
仅支持查询2023-11-20日后的时间表（查询2023-11-20之前的会出现负数班级，待完善）
请输入查询日期：'''
    query_date = input(content)
    try:
        query_date_datetime = datetime.datetime.strptime(query_date, "%Y-%m-%d").date()    # str转换为datetime.datetime，后面的date()是用来只保留年月日、去掉时分秒的方法
        print(get_calender(query_date_datetime, get_next_owner(query_date)))
    except ValueError:
        print("输入日期格式有误！")

