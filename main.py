
import jieba
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import imageio
import pdb

def get_words(txt):

    list = jieba.cut(txt)
    c = Counter()

    for x in list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1


    fw = open('bb.txt', 'w')
    for (k, v) in c.most_common():
        fw.write(k + ' ' + str(v) + '\n')
    fw.close()


    # pac_mask = imageio.imread(r'e:\1000.png')
    # wc = WordCloud(font_path='simhei.ttf', background_color='white', max_words=2000, mask=pac_mask).fit_words(c)
    # plt.imshow(wc)
    # plt.axis('off')
    # plt.show()
    # wc.to_file('e:\\26.png')

if __name__ == '__main__':
    f = open('nips2020paperlist.txt', 'r', encoding='utf-8')
    # f = open('Accepted Papers.txt', 'r', encoding='utf-8')
    get_words(f.readlines())



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