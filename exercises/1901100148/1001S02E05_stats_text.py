text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#1.使⽤字典（dict）统计字符串样本 text 中各个英⽂单词出现的次数
# 先将字符串根据 空白字符 分割成 list
elements=text.split()
# 定义一个新的 list 类型的变量，用以存储处理过的单词
words=[]
# 先针对样本文本挑选出需要剔除的非单词符号
symbols=',.*-!'
for element in elements:
    # 遍历一遍要剔除的符号
    for symbol in symbols:
        # 逐个替换字符号，用''是为了同时剔除符号所占的位置
        element=element.replace(symbol,'')
    # 剔除了字符后，如果 element 的长度不为0，则算作正常单词
    if len(element):
        words.append(element)
print('正常的英文单词--->',words)

# 初始化一个 dict（字典）类型的变量，用来存放单词出现的次数
counter={}
# set（集合）类型可以去掉 列表 里的重复元素，可以在for-in里减少循环次数
word_set=set(words)
for word in word_set:
    counter[word]=words.count(word)
print('英文单词出现的次数---->',counter)
print()
# 2.按照出现次数从⼤到⼩输出所有的单词及出现的次数
# 内置函数 sorted 的参数 key 表示按元素的第一项的值进行排序
# dict 类型 counter 的items 方法会返回一个包含 相应项（key,value) 的元组 列表
# print('counter.items()--->',counter.items())
print('从大到小输出所有单词及出现的次数===》',sorted(counter.items(),key=lambda x:x[1],reverse=True))