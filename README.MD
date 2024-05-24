# color_print: python的可以指定颜色的print

```
from color_print import print, FontColor, sepLine
li = {
    'today': 'Mon',
    'time_hour': '15',
    'time_minute': '40',
    'time_second': '20',
    'a': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}
# [print default]: color:'FontColor.YELLOW' isFormat(use pprint.pformat):False
print('Hi CPrint')
print('Hello CPrint', color=FontColor.RED)
print('Hello', color=FontColor.GREEN, end=' ')('world')
print(li, color=FontColor.CYAN)
# [sepLine default] string:'——', multiple:50, color:FontColor.YELLOW
sepLine(color=FontColor.WHITE)
print(li, color=FontColor.cyan, isFormat=True)
```

![](./img/img.png)

你可以使用导入的print默认颜色输出，或者通过color参数修改颜色。

🦄function: print  
        增加isFormat参数，是否使用pprint.pformat进行格式化
        增加color参数，指定颜色
        其余参数与python默认的print一致

🦄function: sepLine 
        string:'——'  字符串
        multiple:50, 倍数
        color:FontColor.YELLOW  颜色

🦄class: FontColor
        颜色类
        大写字符代表该颜色的高亮状态
