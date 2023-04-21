## 用图

DSLogic_U3Pro16 逻辑分析仪 DSView v1.1.2 数据可视化转换工具


![](https://dreamsourcelab.cn/wp-content/uploads/2017/08/logo-small1.png)
![](https://dreamsourcelab.cn/wp-content/uploads/2013/11/DSLogicPlus_sf1.jpg)

## 依赖环境

- Linux 操作系统
- 安装 python3

## 参考资料

https://dreamsourcelab.cn/doc/DSLogic_U3Pro16_Datasheet_cn.pdf
https://dreamsourcelab.cn/doc/DSView_User_Guide.pdf

## 操作方法

1. 逻辑分析仪捕获 SPI 波形，然后参考 [DSView_User_Guide](https://dreamsourcelab.cn/doc/DSView_User_Guide.pdf)
**2.8.5.协议导出** 章节，导出数据为 txt 文本文件
2. python3 parse_logic_data.py <导出的 txt 文本文件>
3. 以 MISO 为例，输出的文件为： MISO_data.txt


目前只支持 SPI 协议数据可视化转换
