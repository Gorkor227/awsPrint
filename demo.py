from awsPrint import print, FontColor, sepLine
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
