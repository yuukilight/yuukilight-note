## [小彭老师cpp高性能并行编程与优化计算课程](https://www.bilibili.com/video/BV1fa411r7zp/?spm_id_from=333.1387.collection.video_card.click&vd_source=f061ef4a4daa8d17a2109544977d75d9)随笔录

构建大型项目，每次都全部重新编译很浪费时间。可以使用 ```-c``` 预编译部分文件。

为了方便的构建和编译大型项目，出现了构建系统(Makefile)。

Makefile -> Cmake

Cmake: 构建系统的构建系统

静态库与动态库， LIB 与 DLL, so 与 a

写 c++ 就是在只会编译器干活。需要清晰的声明。

c++ 调用 c 时，编译 c 是不希望使用重载机制的。因此在 c 的头文件需要声明。

```""``` 与 ```<>```
  
使用第三方库
1. 纯头文件
2. cmkae 作为子模块引入
3. cmake 引用系统中预安装的第三方库。A,B都依赖C，这时可以预安装C到系统，再安装A，B就会通过 find_package(C) 在系统中找到这个库。

c++ 包管理

