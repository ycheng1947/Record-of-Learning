# Record-of-Learning

## JavaScript Learning

### 基础
- 对象：
	- 由若干的键值对组成的无序集合；
	- 用`{xxxx}`表示一个对象，键值对以`xx:xx`形式表示，以`,`分隔，最后一个键值对后不加`,`；
	- 访问属性是通过`.`操作符完成的，但这要求属性名必须是一个有效的变量名。如果属性名包含特殊字符，就必须用`''`括起来；
	- JavaScript的对象是动态类型，你可以自由地给一个对象添加或删除属性；
	- 我们要检测xiaoming是否拥有某一属性，可以用`in`操作符；
	- 如果in判断一个属性存在，这个属性不一定是xiaoming的，它可能是xiaoming继承得到的。
	- JavaScript把`null`、`undefined`、`0`、`NaN`和空字符串`''`视为`fals`e，其他值一概视为`true`。

## Python Learning
###基础学习
- main函数：`if _name_='_main_':`
- 交互输入：`name = raw_input(please input your name)`
- 缩进表示代码块，`#`号表示注释，大小写敏感。
- 数据类型和变量：
	- 转义：`\`，`r''`表示`''`之间的字符串默认不转义
	- 多行内容表示：` ```xxx``` `
	- 布尔值：True，False
	- and , or ,not 运算

- 格式化的输出：
	- `print "%s" %i`
- list和Tuple
	- list：一种可变有序集合，可以随时增加和删除元素，assert(),append(),pop()；
	- tuple：与list相似，但一旦初始化就不能修改；用`()`定义tuple，只有一个元素的时候必须加`,`号，如`t=(1,)`
	- tuple不可变，但tuple中有list的时候，指向list不变，list中内容是可变的。

- 条件判断：
	- `if x:`，若`x`为非零数，非空字符串，非空list，则为True。

- 循环：
	- `for x in y`循环：将`y`中的每个元素带入变量`x`，执行缩进块代码。
	- `range(100)`：range函数表示0-99的整数序列。
	- `raw_input()`：返回的是字符串，需要转换成int型。

- dict & set
	- dict：
		- 相当于map,`k-v`键值对，一个key只能对应一个value；
		- key不存在会报错，可以用`in`判断，key  in dict；或者通过dict.get(key)或dict.get(key,'xxx')，key不存在返回None或者指定值xxx。
		- 删除一个key ，用pop(key),删除dict中key对应的value。
	- dict vs list：
		- dict：查找和插入速度快，不会随着key的增加而增加；list：查找和插入的时间随着key的增加而增加。
		- dict：需要占用大量的内存，内存浪费多；list：占用空间小，且浪费内存少。
	- set：
		- set是一组key的集合，不存储value值，key不能重复。
		- 创建set，需要传入一个list作为输入集合，注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。
		- add(key),remove(key)
		- 交集和并集操作
		- 和dict类似，不可以放入可变对象，不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

- 函数：
	- 参数检查：
		- 空函数，`pass`语句，什么都不做，占位符。
        - 数据类型检查可以用内置函数`isinstance`实现。

### 特殊语法
#### filter
- filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回

```
def g(x) : return x!='a'
print filter(g,'asdfg')
sdfg
```

#### map
- map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回

```
def m(x):return x*x*x
print map(m,(1,2,3,4))
[1, 8, 27, 64]

```
####reduce
- reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和

```
def add(x,y): return x+y
print reduce(add,range(1,10),20)
65

```

#### lambda
- 这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方

```
g = lambda x:x+1
print g(1)
2

```
- [参考](http://www.cnblogs.com/longdouhzt/archive/2012/05/19/2508844.html)

## Scala Learing

## Spark Learning
