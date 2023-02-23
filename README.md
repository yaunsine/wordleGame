# Wordle游戏 Python实现
![版本](https://img.shields.io/badge/Python版本-3.7-red.svg)
![类型](https://img.shields.io/badge/类型-console程序-blue.svg)

> Wordle是一款免费无广告的网页填字游戏，玩法非常简单：玩家需要在6次机会中猜出一个由5个英文字母组成的英文单词，玩家猜中的字母会以绿底呈现，黄底则表示单词包含此字母但位置有误，而灰底代表字母未包含在单词内。猜中后可将通关时间、猜字次数分享到社交平台，与朋友比拼猜字速度。

# 运行程序
```shell
python __init__.py
```


#### 运行效果：
```console
E:\Coding\python\anaconda\envs\py37\python.exe E:/Coding/python/wordle/__init__.py
=============wordle游戏，G代表Green，Y代表Yello，K代表Grey================
您还有6次机会
请输入1个包含5个字母的单词：about
校验结果： KKKYK
=============wordle游戏，G代表Green，Y代表Yello，K代表Grey================
您还有5次机会
请输入1个包含5个字母的单词：lucky
校验结果： YYKKK
=============wordle游戏，G代表Green，Y代表Yello，K代表Grey================
您还有4次机会
请输入1个包含5个字母的单词：fuels
校验结果： KYKYY
=============wordle游戏，G代表Green，Y代表Yello，K代表Grey================
您还有3次机会
请输入1个包含5个字母的单词：blush
校验结果： KGGYK
=============wordle游戏，G代表Green，Y代表Yello，K代表Grey================
您还有2次机会
请输入1个包含5个字母的单词：slump

校验结果： GGGGG
输入正确, 游戏结束!!!
=================
正确答案： slump
```
