import codecs
import jieba
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import imageio

def get_words(txt):
    #进行分词
    list = jieba.cut(txt)
    c = Counter()

    #给分词定义条件进行筛选统计词频
    for x in list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1

    #打开一个文本将统计好的词频存放进去
    with open('bb.txt', 'w', 'gbk') as fw:
        for (k, v) in c.most_common():
            fw.write(k + ' ' + str(v) + '\n')
        fw.close()
    
    # #绘制词云图
    # pac_mask = imageio.imread(r'e:\1000.png')
    # wc = WordCloud(font_path='simhei.ttf', background_color='white', max_words=2000, mask=pac_mask).fit_words(c)
    # plt.imshow(wc)
    # plt.axis('off')
    # plt.show()
    # wc.to_file('e:\\26.png')

if __name__ == '__main__':
    #打开需要分词的文本
    with codecs.open('nips2020paperlist.txt', 'r', 'gbk') as f:
        txt = f.readlines()
    get_words(txt)



# import matplotlib.pyplot as plt
# from matplotlib.font_manager import *
# fig, ax = plt.subplots()
# myfont = FontProperties(fname=r'C:\Windows.old\Windows\Fonts\simhei.ttf',size=12)
# N = 10
# words = []
# counts = []
# for line in open('e:\word\\bb.txt'):
#     line.strip('\n')
#     words.append(line.split(' ')[0])
#     counts.append(int(line.split(' ')[1].strip('\n')))
# colors = ['#FA8072']

# #绘制前十条数据（N=10）
# rects = ax.barh(words[:N], counts[:N], align='center', color=colors)
# ax.set_yticklabels(words[:N],fontproperties=myfont)
# ax.invert_yaxis()
# ax.set_title('高频词汇',fontproperties=myfont, fontsize=17)
# ax.set_xlabel(u"出现次数",fontproperties=myfont)
# plt.show()