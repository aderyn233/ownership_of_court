# ownership_of_court
用于计算bj8z高二羽毛球场归属

## 开发环境
python3.8.8

prettytable==3.9.0

macOS12.5

IDE：PyCharm 2023.2.2 (Professional Edition)

## 使用
**运行前需要安装python3环境和prettytable**

安装好python之后，用如下命令安装prettytable：

```
# Windows
pip install prettytable==3.9.0
# macOS & linux
pip3 install prettytable==3.9.0
```

运行`mian.py`即可，程序会先输出最近两周的场地安排表格，然后可以查询任意基准时间以后的场地归属

查询基准时间以前的场地归属会出现负数班级，待完善

ps.程序名称叫`mian.py`，如有雷同，纯属搞笑。

## 校准
由于八监一贯以来举行活动占用场地不归还的作风，特设校准功能，使用方式如下：

编辑程序根目录下`standard_date.txt`，其中有两行内容，第一行为基准日期，第二行为基准日期当天4号场地所属班级

例如，2023-11-20当天的4号场是高二11班：
```text
2023-11-20
11
```
注意，第一行日期的格式为`yyyy-mm-dd`，例如2024-01-03，**“0”不能省略**

