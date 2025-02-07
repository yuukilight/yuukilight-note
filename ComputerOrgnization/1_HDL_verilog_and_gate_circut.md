[toc]
## iverilog window环境配置和使用
[主要参考资料](https://zhuanlan.zhihu.com/p/95081329)
Icarus Verilog: vero;pg HDL 的开源编译器。
vvp, Verilog Virtual Processor： 仿真引擎，用于执行编译后的verilog 文件。
GTKWAVE, GTK Waveform Viewer: 查看VCD,LXT(Large eXtensible Trace),LXT2 等波形文件的图形化工具。
GTK： 是用于创建图形用户界面的工具包（GIMP Toolkit）。

### 下载和安装
[工具下载](http://bleyer.org/icarus/)
下载后直接安装即可

### 简单使用
```bash
# 编译
iverilog -o 编译生成文件名.vvp(vvp or out) -y 需要的其它模块路径 -l 需要的头文件路径 相关iverilog文件.v

# 执行
vvp xxx.vvp(or xxx.out) -lxt2

# 如果生成了 vcd 文件
gtkwave xxx.vcd
```

### 基本语法
包含其它模块文件
```verilog
`include "nand.v"
```

```
```

### 其它
iverilog 中
输出 x 表示输出不确定。
输出 z 表示高阻抗状态（high-impedance）,即断开。

## 门电路
NMOS 与 PMOS 互补组成 CMOS，可以用来构造与非门。其余所有的门电路都可以用与非门进行构造。 如下构造了一个与非门：
```verilog
module Nand(input a, b, output out);
  nmos n1(o1, 0, b);
  nmos n2(out, o1, a);

  pmos p1(out, 1, a);
  pmos p2(out, 1, b);
endmodule
```
NMOS 输入高电平导通，PMOS 输入低电平导通。
因此可以将两个 PMOS 并联，只要有一个低电平输入即可导通， 同时输入高电平时断开；
将两个 NMOS 串联，当同时输入高电平时接地；

### 异或门(Exclusive-OR gate, XOR gate)
异或门可以用于实现二进制的加法, 即 1+1 和 0+0 时当前位为 0, 而 1+0 与 0+1 时当前位为 1。

## 数字电路
数字电路类型：
1. 组合逻辑电路：无存储功能, 输出依赖当前的输入。例如运算器（加减乘除器），ALU。
2. 时序逻辑电路： 有存储功能, 电路可以存储或记住信息，不仅依赖输入，还以来存储单元当前的状态。例如寄存器，存储器。
### 数字电路与布尔代数
数字电路的设计通常会使用布尔代数的一些定律来进行优化，例如德摩根定律（ Not(x And y) = Not(x) Or Not(y) ）, 双重否定律等。
### 组合逻辑电路
#### 加法器
##### 半加器(Half Adder)
半加器即不考虑进位的加法器，只有两个输入a, b。
二进制运算中，可以使用一个 XOR gate 实现当前位的运算，用一个 AND gate 计算进位(carry)。
最后输入 sum 和 carry。
##### 全加器（Full Adder）
全加器考虑进位，有三个输入a, b, c。
输出 sum s和 carry。
相当于两个半加器和一个 OR gate。先计算a+b 得到中间变量s1, c1。再计算s1+c 得到中间变量c2 和结果 sum。c1 和 c2 通过 OR gate 得到 carry。