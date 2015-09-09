|学习规划|开始时间|结束时间|完成进度|
|----|
|JS教程|2015.9.8|2015.9.11|-|
|Js函数|2015.9.12|2015.9.12|0%|
|JS HTML DOM|2015.9.13|2015.9.14|0%|
|JS 库|2015.9.15|2015.9.15|0%|

# JavaScript Learning
## 基础
- [参考](http://www.runoob.com/js/js-tutorial.html)
- 文本输出：
	- `document.write(Date());`
	- document.write("<p>" + txt.length + "</p>")
	- 换行：`document.write( "<br>");`

- 函数：
```
function myFunction(){
  var x="";
var time=new Date().getHours();
if (time<20)
  {
  x="Good day";
  }
else
  {
  x="Good evening";
  }
document.getElementById("demo").innerHTML=x;
    } 
    ```

- 变量：
	- 变量是存储数据的容器；
	- 必须以字母开头，大小写敏感；
	- 变量可以保存数据类型，JavaScript主要关注数字和字符串（以单引号或者双引号包围）；
	- 申明（创建）变量，用`var`，申明后为空，赋值用`=`
	- 一条语句申明多个变量，以`var`开头，逗号分隔变量；
	- 申明无值的变量，其值实际上是undefined；
	- 重新申明变量，变量的值任然保留。

- 数据类型：
	-  7种：字符串（String）、数字（Number）、布尔（Boolean）、数组（Array）、对象（Object)、空（Null）、未定义（undefined）；
	-  JavaScript拥有动态类型，相同的变量可以用作不同的类型；
	-  字符串中可以使用引号，只要不匹配包围字符串的引号即可；
	-  JavaScript只有一种数字类型，可以带小数点，也可以不带，极大或者极小的数字用科学（指数）计数法表示；
	-  布尔值：true、false；
	-  数组：
		- 创建1：
		```
        var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";
```
		- condensed array：
		```
        var cars=new Array("Saab","Volvo","BMW");
```

		- literal array:
		```
        var cars=["Saab","Volvo","BMW"];
```
- JavaScript 对象：
	-  对象由花括号分隔，括号内，对象的属性以名称和值对的形式（name:value)来定义，属性由逗号分隔开；
	-  对象属性由两种寻址方式
	```
    name=person.lastname;
name=person["lastname"];
```
-  `undefined & Null`:
	-  Undefined 这个值表示变量不含有值;
	-  可以通过将变量的值设置为 null 来清空变量。

-  申明变量类型：
	-  申明新变量时，可以使用`new`来申明其类型；
	```
    var carname=new String;
var x=      new Number;
var y=      new Boolean;
var cars=   new Array;
var person= new Object;
```
### JavaScript对象
-  JavaScript 变量均为对象。当您声明一个变量时，就创建了一个新的对象。
-  对象也是一个变量，可以包含多个值（多个变量）。JavaScript对象是变量的容器，也说JavaScript对象是键值对的容器。
-  对象方法：
	- 对象的方法定义了一个函数，并作为对象的属性存储。
	- 对象方法通过添加()调用，如person.fullName()。
	- 如果要访问person对象的fullName属性，它将作为一个定义函数的字符串返回。
- 访问对象的方法：
	```
    methodName : function() { code lines }
```
	```
    objectName.methodName()
```
### JS函数
- 函数是由事件驱动或者当它被调用时执行的可重复使用的代码块。
- 局部变量：
	- 在函数内部申明的变量（使用var）
- 全局变量：
	- 在函数外申明的变量，网页上所有的脚本和函数都能访问的。
- 向未申明的变量分配值，该变量自动作为全局变量申明，即使它在函数内执行。
- 在HTML中，全局变量是window对象；所有数据变量都属于window对象。

### JavaScript 事件
- [TODO](http://www.runoob.com/js/js-events.html)






























