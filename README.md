# epui
2.9'' E-ink paper UI system with MicroPython FrameBuffer running on ESP32 boards
pure python

纯python，100% python代码

硬件：2.9寸墨水屏WFT0290CZ10LP

MCU：ESP32S2

键盘：3键以上，8键以下开关键盘

同时支持MicroPython及Circuitpython（如果要使用声音驱动需使用Circuitpython）

特性：
1. 基于framebuffer的ui库驱动。包括固定位置模型、横向盒模型、纵向盒模型、画布、文本标签、进度条、图片及文本按钮（3种样式）、对话框、消息框组件
2. 整合了Bmp位图（支持gzip压缩，支持透明背景色精灵）和字体驱动（可以自己扩展）
3. 支持ADC0832模块测量电池电量
4. 支持SD卡驱动（已改进，防掉卡）
5. 键盘模块（支持点按，长按，多键同时操作），截屏快照
6. 支持插件模式开发，只需要将对应文件复制到目录即完成功能扩展

![image](https://github.com/foxmale007/epui/blob/main/screenshot/hardware.jpg)

运行步骤：
1. 请根据 [IO定义](https://github.com/foxmale007/epui/blob/main/driver/driver_def.py)接好线
2. 烧录好Micropython固件（建议>1.19.1）
3. 将文件使用Thonny上传至MicroPython设备/目录
4. 运行start.py查看效果
5. 运行 [组件测试](https://github.com/foxmale007/epui/blob/main/tests/widgets_test.py) 进行组件测试了解特性
6. 运行 [模块测试](https://github.com/foxmale007/epui/blob/main/tests/module_test.py) 了解模块单元测试方式
开放了日历组件源码，可以参考进行二次开发添加自己的模块

运行快照：

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710144713.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710143945.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710144801.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710144813.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710144856.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710144909.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710144915.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710145028.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710145116.png)

![image](https://github.com/foxmale007/epui/blob/main/screenshot/snap20230710145145.png)

下一步计划：

1. 中文/英文输入法
2. 输入框组件
3. 深度休眠
4. 单词卡学习模块
5. 英文电子字典模块
6. 模块市场
