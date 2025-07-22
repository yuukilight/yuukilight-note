## CMake 检测 python 解释器和python 库

1. cpp 中使用 python 脚本
2. 将python 封装成 cpp 库
3. 将python 解释器嵌入到c++程序中

因此需要 cmake 能够获取到 python 解释器的工作版本，头文件的可用性，以及运行时的 libpython

展示一段 CMakeLists.txt 代码
```cmake
# 指定 cmake 的最低版本，否则会终止报错
cmake_minimum_required(VERSION 3.10 FATAL_ERROR)

# 声明项目名称，已经告诉 cmake 不涉及编程语言
project(python_interpreter LANGUAGES NONE)

# 查找系统中已安装的Python解释器，
find_package(PythonInterp REQUIRED)

execute_process(
  COMMAND ${PYTHON_EXECUTABLE} -c "print('Hello, python interpreter!')"
  RESULT_VARIABLE RESULT_STATUS
  OUTPUT_VARIABLE RESULT_OUTPUT
  ERROR_QUIET
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

message(STATUS "RESULT_VARIABLE is: ${RESULT_STATUS}")
message(STATUS "OUTPUT_VARIABLE is: ${RESULT_OUTPUT}")
```