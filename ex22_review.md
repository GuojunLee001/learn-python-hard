## ex1

- 输入中文时会出错，需要在开头使用：# -*- coding: utf-8 -*-或者 # coding:utf-8

- 引号使用：引号必须成队出现，而且必须是英文状态下的引号，单双引号都可以

  转义字符使用：

  | 转义字符     | 描述                                     |
  | ------------ | ---------------------------------------- |
  | \ (在行尾时) | 续行符                                   |
  | \\\          | 反斜杠符号                               |
  | \\'          | 单引号                                   |
  | \\"          | 双引号                                   |
  | \\a          | 响铃                                     |
  | \b           | 退格                                     |
  | \\e          | 转义                                     |
  | \000         | 空                                       |
  | \n           | 换行                                     |
  | \v           | 纵向制表符                               |
  | \t           | 横向制表符                               |
  | \r           | 回车                                     |
  | \f           | 换页                                     |
  | \oyy         | 八进制数yy代表的字符，例如：\o12代表换行 |
  | \xyy         | 十进制数yy代表的字符，例如：\x0a代表换行 |
  | \other       | 其它的字符以普通格式输出                 |

  

## ex2

- "#" 使用规则
  - 用于注释，放在需要注释的代码的最前面一行
  - 有的注释也放在里面

- 多行注释用`""" `或`‘’‘`

  - 例如

    ​    '''
    ​    print hohohoho~ happy new year~
    ​    '''

- 快捷键： ctrl+/ 

## ex3

符号的使用

> - \+ plus 加号
> - \- minus 减号
> - / slash 斜杠 除法
> - \* asterisk 星号 乘法
> - % percent 百分号 模除
> - < less-than 小于号
> - \> greater-than 大于号
> - <= less-than-equal 小于等于号
> - \>= greater-than-equal 大于等于号



## ex4

- 重点是变量的表示，变量需要用`_`连接，
- 变量是把经常要用的表示出来，可以减少运算量
- `%r`表示变量会经常用到，叫做`格式化字符串(format string)`例如：`cars = 100,print "There are", %r, "cars available." % cars`。我理解这样做的好处是更方便阅读和修改。

## ex5

格式化字符串总结

>`%s`    字符串 (采用str()的显示)
 `%r`    字符串 (采用repr()的显示)
 `%c`    单个字符
 `%b`    二进制整数
 `%d`    十进制整数
 `%i`    十进制整数
 `%o`    八进制整数
 `%x`   十六进制整数
 `%e`    指数 (基底写为e)
 `%E`    指数 (基底写为E)
 `%f`    浮点数
 `%F`    浮点数，与上相同
 `%g`    指数(e)�或浮点数 (根据显示长度)
 `%G`    指数(E)或浮点数 (根据显示长度)
 `%%`    字符"%"

转自[简书-古佛青灯度流年](https://www.jianshu.com/p/5017db7b38e6)

## ex11,ex12，ex13

[raw_input()和input() 函数](https://www.jianshu.com/p/a7070a87435a)

- raw_input 和 input都是实现与用户交互，语法`raw_input([prompt])、input([prompt])`
- raw_input()： 读取控制台的输入，返回字符串类型、input()：读取控制台的输入，但输入时必须使用引号括起来，否则会报错。

## ex13，ex4

- argv：参数变量(argument variable)
- 注意点：必须在开始就赋予值，不然会报错
- 与raw_inout(promt)结合起来使用，进一步明确raw_input与用户交互的输入作用。

## ex15

- open()

## ex16.ex17

掌握度一般，还需要多练习，`target = open(filename, 'w')`未完全理解

> - close -- 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
> - read -- 读取文件内容。你可以把结果赋给一个变量。
> - readline -- 读取文本文件中的一行。
> - truncate -- 清空文件，请谨慎使用该命令。
> - write('stuff') -- 将stuff写入文件。

## ex18，ex19，ex20,ex21

- 四种基本函数表达式：

  ```python
  # this one is like your scripts with argv
  def print_two(*args):
      arg1, arg2 = args
      print "arg1: %r, arg2: %r" % (arg1, arg2)
  
  # ok, that *args is actually pointless, we can just do this
  def print_two_again(arg1, arg2):
      print "arg1: %r, arg2: %r" % (arg1, arg2)
  
  # this just takes one argument
  def print_one(arg1):
      print "arg1: %r" % arg1
  
  # this one takes no arguments
  def print_none():
      print "I got nothin'."
  
  
  print_two("Zed","Shaw")
  print_two_again("Zed","Shaw")
  print_one("First!")
  print_none()
  ```

- 函数与文件

  - 函数本质是一种关系连接，所以可以用来打开文件

  - return 函数是返回函数































## 错误提示总结



