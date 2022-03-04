import matplotlib.pyplot as plt


dict01 = {'2': '2'}
dict02 = {'06': '2', '07': "7"}
def draw(mydict01, mydict02, path):
    def GetData(mydict):
        ColumnX = []
        ColumnY = []
        for i, j  in zip(mydict.keys(), mydict.values()):
            ColumnX.append(int(i))
            ColumnY.append(int(j))
        print(ColumnX, ColumnY)
        return ColumnX, ColumnY

    def auto_text(rects):
        for rect in rects:
            ax.text(rect.get_x() + 0.35, rect.get_height()+0.5, rect.get_height())

    # # 柱状图
    ColumnX, ColumnY = GetData(mydict01)
    fig, ax = plt.subplots()
    rect = plt.bar(range(len(ColumnY)), ColumnY, tick_label = ColumnX)
    plt.title("各鸟类数量分析")
    plt.xlabel("鸟类")
    plt.ylabel("数量")
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False
    auto_text(rect)
    plt.save(path)
    plt.show()

    # 折线图
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False
    ColumnX, ColumnY = GetData(mydict02)
    plt.figure(figsize=(20,5),dpi=90)
    plt.plot(ColumnX, ColumnY)
    plt.xticks(rotation=45)
    plt.title("活动量分析")
    plt.xlabel("日期")
    plt.ylabel("鸟类活动总数")
    plt.save(path)
    plt.show()

draw(dict01, dict02)