# epui
2.9‘’ E-ink paper UI system with micropython running on ESP32

硬件：2.9寸墨水屏WFT0290CZ10LP
MCU：ESP32S2 或 ESP32S3
键盘：3键以上，8键以下开关键盘

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

