# color_print: python的可以指定颜色的print

```
from color_print import print, font_color
print('Hi CPrint')
print('Hello CPrint', color=font_color.RED)
print.set_default_color(font_color.green)
print('Hello world')
```

![](img/img.png)

你可以使用导入的print默认颜色输出，或者通过set_default_color修改默认颜色。
