## shell语法

[toc]

### 1. 概论

shell是我们通过命令行与操作系统沟通的语言。

shell脚本可以直接在命令行中执行，也可以将一套逻辑组织成一个文件，方便复用。

Linux中常见的shell脚本有很多种，常见的有：
- Bourne Shell(/usr/bin/sh或/bin/sh)
- Bourne Again Shell(/bin/bash)
- C Shell(/usr/bin/csh)
- K Shell(/usr/bin/ksh)
- zsh
- …
Linux系统中一般默认使用bash，所以接下来讲解bash中的语法。
文件开头需要写```#! /bin/bash```，指明bash为脚本解释器。

#### 1.1 使用示范
新建 test.sh 文件，编辑内容如下：
```bash
#! /bin/bash

echo "Hello World!"
```
```#! ``` 其后指定了运行该文件所使用的解释器。可以直接通过 test.sh 执行，而不需要输入解释器（例如 bash test.sh）。

通过通过执行文件执行
```shell
acs@9e0ebfcd82d7:~$ chmod +x test.sh  # 使脚本具有可执行权限
acs@9e0ebfcd82d7:~$ ./test.sh  # 当前路径下执行
Hello World!  # 脚本输出
acs@9e0ebfcd82d7:~$ /home/acs/test.sh  # 绝对路径下执行
Hello World!  # 脚本输出
acs@9e0ebfcd82d7:~$ ~/test.sh  # 家目录路径下执行
Hello World!  # 脚本输出
```
也可以通过解释器执行
```shell
acs@9e0ebfcd82d7:~$ bash test.sh
Hello World!  # 脚本输出
```

### 2. 注释
#### 2.1 当行注释
每行中```#```之后的内容均是注释。
```bash
# 这是一行注释

echo 'Hello World'  #  这也是注释
```

#### 2.2 多行注释
格式：
```bash
:<<EOF
第一行注释
第二行注释
第三行注释
EOF
```
其中```EOF```可以换成其它任意字符串。例如：
```bash
:<<abc
第一行注释
第二行注释
第三行注释
abc

:<<!
第一行注释
第二行注释
第三行注释
!
```

### 3. 变量
#### 3.1 定义变量
定义变量，不需要加```$```符号，例如：
```bash
name1='yxc'  # 单引号定义字符串
name2="yxc"  # 双引号定义字符串
name3=yxc    # 也可以不加引号，同样表示字符串
```
#### 3.2 使用变量
使用变量，需要加上$符号，或者${}符号。花括号是可选的，主要为了帮助解释器识别变量边界。
```bash
name=yxc
echo $name  # 输出yxc
echo ${name}  # 输出yxc
echo ${name}acwing  # 输出yxcacwing
```

#### 3.3 只读变量
使用```readonly```或者```declare```可以将变量变为只读。
```bash
name=yxc
readonly name
declare -r name  # 两种写法均可

name=abc  # 会报错，因为此时name只读
```

#### 3.4 删除变量
```unset```可以删除变量。

```bash
name=yxc
unset name
echo $name  # 输出空行
```
#### 3.5 变量类型
1. 自定义变量（局部变量）子进程不能访问的变量
2. 环境变量（全局变量）子进程可以访问的变量

自定义变量改成环境变量：
(这里的 x 代表的是 export 而不是 executable)
```bash
acs@9e0ebfcd82d7:~$ name=yxc  # 定义变量
acs@9e0ebfcd82d7:~$ export name  # 第一种方法
acs@9e0ebfcd82d7:~$ declare -x name  # 第二种方法
```
环境变量改为自定义变量：
```bash
acs@9e0ebfcd82d7:~$ export name=yxc  # 定义环境变量
acs@9e0ebfcd82d7:~$ declare +x name  # 改为自定义变量
```
#### 3.6 字符串
字符串可以用单引号，也可以用双引号，也可以不用引号。

单引号与双引号的区别：
- 单引号中的内容会原样输出，不会执行、不会取变量；
- 双引号中的内容可以执行、可以取变量；
  
```bash
name=yxc  # 不用引号
echo 'hello, $name \"hh\"'  # 单引号字符串，输出 hello, $name \"hh\"
echo "hello, $name \"hh\""  # 双引号字符串，输出 hello, yxc "hh"
```
获取字符串长度
```bash
name="yxc"
echo ${#name}  # 输出3
```
提取子串
```bash
name="hello, yxc"
echo ${name:0:5}  # 提取从0开始的5个字符
```

### 4. 默认变量
#### 4.1 文件参数变量
在执行shell脚本时，可以向脚本传递参数。```$1```是第一个参数，```$2```是第二个参数，以此类推。特殊的，```$0```是文件名（包含路径）。例如：
创建文件```test.sh```：
```bash
#! /bin/bash

echo "文件名："$0
echo "第一个参数："$1
echo "第二个参数："$2
echo "第三个参数："$3
echo "第四个参数："$4
```
然后执行该脚本：
```shell
acs@9e0ebfcd82d7:~$ chmod +x test.sh 
acs@9e0ebfcd82d7:~$ ./test.sh 1 2 3 4
文件名：./test.sh
第一个参数：1
第二个参数：2
第三个参数：3
第四个参数：4
```
#### 4.2 其它参数相关变量
| 参数              | 说明                                                             |
| --------------- | -------------------------------------------------------------- |
| `$#`            | 代表文件传入的参数个数，例如，若传入了 4 个参数，则值为 `4`                              |
| `$*`            | 由所有参数构成的用空格隔开的字符串，例如 `"$1 $2 $3 $4"`                           |
| `$@`            | 每个参数分别用双引号括起来的字符串，例如 `"$1" "$2" "$3" "$4"`                     |
| `$$`            | 脚本当前运行的进程 ID                                                   |
| `$?`            | 上一条命令的退出状态（不是标准输出 stdout，而是 exit code）。返回 `0` 表示正常退出，其他值表示出现错误 |
| `$(command)`    | 返回 `command` 命令的标准输出，**支持嵌套**                                  |
| `` `command` `` | 返回 `command` 命令的标准输出，**不支持嵌套**                                 |

### 5. 数组
数组中可以存放多个不同类型的值，只支持一维数组，初始化时不需要指明数组大小。
数组下标从0开始。
#### 5.1 定义
数组用小括号表示，元素之间用空格隔开。例如：
```bash
array=(1 abc "def" yxc)
```
也可以直接定义数组中某个元素的值：
```bash
array[0]=1
array[1]=abc
array[2]="def"
array[3]=yxc
```

#### 5.2 读取数组中某个元素的值
格式：
```bash
${array[index]}
```
例如：
```bash
array=(1 abc "def" yxc)
echo ${array[0]}
echo ${array[1]}
echo ${array[2]}
echo ${array[3]}
```
#### 5.3 读取整个数组
格式：
```bash
${array[@]}  # 第一种写法
${array[*]}  # 第二种写法
```
例如：
```bash
array=(1 abc "def" yxc)

echo ${array[@]}  # 第一种写法
echo ${array[*]}  # 第二种写法
```
#### 5.4 数组长度
类似于字符串
```bash
${#array[@]}  # 第一种写法
${#array[*]}  # 第二种写法
```
例如：
```bash
array=(1 abc "def" yxc)

echo ${#array[@]}  # 第一种写法
echo ${#array[*]}  # 第二种写法
```

### expr命令
expr命令用于求表达式的值，格式为：
```bash
expr 表达式
```
表达式说明：

- 用空格隔开每一项
- 用反斜杠放在shell特定的字符前面（发现表达式运行错误时，可以试试转义）
- 对包含空格和其他特殊字符的字符串要用引号括起来
- expr会在stdout中输出结果。如果为逻辑关系表达式，则结果为真时，stdout输出1，否则输出0。
- expr的exit code：如果为逻辑关系表达式，则结果为真时，exit code为0，否则为1。

***

#### 字符串表达式
- ```length STRING```
返回```STRING```的长度
- ```index STRING CHARSET```
CHARSET中任意单个字符在STRING中最前面的字符位置，下标从1开始。如果在STRING中完全不存在CHARSET中的字符，则返回0。
substr STRING POSITION LENGTH
返回STRING字符串中从POSITION开始，长度最大为LENGTH的子串。如果POSITION或LENGTH为负数，0或非数值，则返回空字符串。
示例：

str="Hello World!"

echo `expr length "$str"`  # ``不是单引号，表示执行该命令，输出12
echo `expr index "$str" aWd`  # 输出7，下标从1开始
echo `expr substr "$str" 2 3`  # 输出 ell
整数表达式
expr支持普通的算术操作，算术表达式优先级低于字符串表达式，高于逻辑关系表达式。

+ -
加减运算。两端参数会转换为整数，如果转换失败则报错。

* / %
乘，除，取模运算。两端参数会转换为整数，如果转换失败则报错。

() 可以改变优先级，但需要用反斜杠转义

示例：

a=3
b=4

echo `expr $a + $b`  # 输出7
echo `expr $a - $b`  # 输出-1
echo `expr $a \* $b`  # 输出12，*需要转义
echo `expr $a / $b`  # 输出0，整除
echo `expr $a % $b` # 输出3
echo `expr \( $a + 1 \) \* \( $b + 1 \)`  # 输出20，值为(a + 1) * (b + 1)
逻辑关系表达式
|
如果第一个参数非空且非0，则返回第一个参数的值，否则返回第二个参数的值，但要求第二个参数的值也是非空或非0，否则返回0。如果第一个参数是非空或非0时，不会计算第二个参数。
&
如果两个参数都非空且非0，则返回第一个参数，否则返回0。如果第一个参为0或为空，则不会计算第二个参数。

< <= = == != >= >
比较两端的参数，如果为true，则返回1，否则返回0。”==”是”=”的同义词。”expr”首先尝试将两端参数转换为整数，并做算术比较，如果转换失败，则按字符集排序规则做字符比较。

() 可以改变优先级，但需要用反斜杠转义
示例：

a=3
b=4

echo `expr $a \> $b`  # 输出0，>需要转义
echo `expr $a '<' $b`  # 输出1，也可以将特殊字符用引号引起来
echo `expr $a '>=' $b`  # 输出0
echo `expr $a \<\= $b`  # 输出1

c=0
d=5

echo `expr $c \& $d`  # 输出0
echo `expr $a \& $b`  # 输出3
echo `expr $c \| $d`  # 输出5
echo `expr $a \| $b`  # 输出3


### read命令
### echo命令
### printf命令
### test命令与判断符号[]
### 判断语句
### 循环语句
### 函数
### exit命令
### 文件重定向
### 引入外部脚本