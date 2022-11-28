import random

ls = []
with open('./words.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        ls.append(line)

def judge(word):
    # 判断这个单词是否在词汇表中
    lines = ""
    with open('./valid_inputs.txt', 'r') as f:
        for line in f.readlines():
            if line.find(word) != -1:
                return True
    return False

def show_result(word, right_word):
    result = ['']*5
    for i, v in enumerate(list(word)):
        if v not in right_word:
            result[i] = 'K'
        if v in right_word:
            result[i] = 'Y'
        if v == right_word[i]:
            result[i] = 'G'
    return "".join(result)


right_word = random.choice(ls)

count = 6
while count > 0:
    print("=============wordle游戏，G代表Green，Y代表Yello，K代表Grey================")
    print("您还有{}次机会".format(count))
    x = input("请输入1个包含5个字母的单词：")
    if len(x) != 5:
        print("输入格式不正确")
        continue
    flag = False
    for item in x:
        if item.isalpha() is False:
            print("输入格式不正确")
            flag = True
            break
    if flag:
        continue

    x = x.lower()
    if judge(x):
        count -= 1
        if x == right_word:
            print("校验结果：", "G"*5)
            print("输入正确, 游戏结束!!!")
            break
        else:
            result = show_result(word=x, right_word=right_word)
            print("校验结果：", result)
    else:
        print("输入的单词不在列表中")


print("=================")
if count == 0:
    print("次数已用完，游戏失败")
print("正确答案：", right_word)

