# 基于树莓派的超声波测密仪

## 项目简介
- 本项目为 长春工业大学2017年校电子设计竞赛 E题：物体密度测量装置 的参赛作品
- 

## 系统结构图

## 硬件电路图
- 声波接收测速电路

- 高速MOS电路

## 工作流程图
'''flow
st=>start: 开始
e=>end: 结束
op1=>operation: 测量物体材质的选择
op2=>operation: 一键开始测量
op3=>operation: 定距超声波测速
op4=>operation: 压力传感测量物体净重
op5=>operation: 计算物体密度，体积
op6=>operation: 显示本次测量结果
print=>condition: 是否开启打印功能
opprint=>operation: 打印本次测量结果
print(yes, right)->opprint->e
print(no)->e
