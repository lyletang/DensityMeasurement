# 基于树莓派的超声波测密仪

- School: CCUT
- TeamLeader: Jiahui Tang
- TeamMember: Xiaoyu Qu, Pengyue Zhao, Xinguang Guo
- Date: 2017-07-03

## 装置简介
本套测量系统实现了如下功能和特色：
- 非接触条件下动态测量检测区内不规则物体的密度，一键开启测量，快速，方便。
- 测量不规则被测物体的重量，体积。
- 按钮设置测量物体的材质，被测量物体的材质分为四大类：1.钢铁等常见重金属制品；2.各类锌铝等轻金属及天然岩类；3.砖，混凝土等人工建材； 4.各种常见木材，石蜡类，烯烃类塑料等密度小于1的材质。四类材质对应常见固体物质的弹性模量。几乎适应所有需要测量的固体物质。(密度1以下的物质只需选择第四项即可)
- 装置具备显示测量结果的功能，直观，实时。
- 装置具备打印测量结果的功能，也可以通过扫描微信二维码在移动端查看单次测量结果。
- 装置具备语音提示功能，更人性化。
- 测量过程进度条实时监控

## 硬件电路图
### 声波接收测速电路
![image](https://raw.githubusercontent.com/tangjiahui1014/DensityMeasurement/master/Image/cesu.png)

### 高速MOS电路
![image](https://raw.githubusercontent.com/tangjiahui1014/DensityMeasurement/master/Image/mos.png)

## 理论分析与计算

### 工作原理

#### 超声波的定义
> 当声的频率高到超过人耳的频率极限时，人们就察觉不出声的存在，我们称这种高频率的声为超声。频率高于人类听觉极限（约20000Hz）的声波，成为超声波。

#### 超声波的特点
- > 能以各式各样的传播形式（纵波，横波，表面波，薄板波）在气体，液体，固体或他们的混合物等各种媒介中传播，也可在光不能通过的金属，生物中传播，是探测物体内部的有效手段。
- > 由于超声波与电磁波相比速度慢，对于相同的频率波长短，容易提高测量的分辨度。
- > 由于传播时受介质声速，声阻抗和衰减常量的影响大，所以，反过来可由超声波传播的情况测量物质的状态。
- > 方向性强，能量远远大于振幅相同的一般声波，并且具有很高的穿透能力。

#### 超声波测密原理
> 利用超声波技术实现密度的测量是根据超声波在介质中传播时，其传播速度与介质的密度有关，当介质密度发生变化时，超声波传播速度也会发生变化。因此，可以通过测量超声波在介质中的传播速度来间接测量介质密度。

### 理论计算

#### 声速测量
> 发射头发射一组超声波脉冲后，输出信号由高电平变为低电平；当测量装置另一侧的接收头收到足够强的超声波信号后，输出信号由低电平转为高电平，高电平持续时长即为声波传播时长。

```math
c = \frac {d} {t}
```

> 如上为超声波传播速度与传播时间的关系式，其中，c为超声波传播速度，d为传播距离，t为传播时长。

#### 密度计算

```math
c = \frac {1} {\sqrt {{\rho} {\kappa}}}
```

> 如上为声波传播时，传播速度与介质密度的关系式，其中，c为超声波在介质中的传播速度，为介质的密度，为介质的弹性模量常数。

### 误差分析

#### 温度影响

```math
C = C0 + 0.607 \times \tau (\degree C)
```

> 如上为声波传播速度与环境温度的关系式，其中，C0为零度时的声波传播速度332m/s，`$\tau$` 为实际环境温度。 \
可做适当的温度补偿尽可能来消除温度造成的误差。

#### 三角误差

> 当被测物体与传感装置成一定角度的时候，由于声波的强方向性，会造成三角误差。

#### 多次反射

> 声波在物体内部可能会因为多次反射而造成测量数据的不真实性。

#### 弹性模量造成的误差量

> 相似材质物体的弹性模量间的差距甚微，例如各类砖，混凝土等合成建材的弹性模量均分布在`$0.1\times10^5MPa$`左右，各类钢铁制品的弹性模量均分布在`$2.0\times10^5MPa$`左右，各类锌铝等轻金属，天然岩的弹性模量均分布在`$1.0\times10^5MPa$`左右，各种烯烃类人工塑料，木材等材质的弹性模量均分布在`$0.01\times10^5MPa$`左右。 \
由于测量物体的不确定性，只能确定测量物体的大致材质，由弹性模量引起的误差量在测量中难以消除。 \
弹性模量的不一致性也决定了本套装置只能测量部分常见固体物质的密度。

## 测量结果

| 物体 | 重量(`$g$`) | 体积(`$cm^3$`) | 密度(`$g/cm^3$`) |
|:---:|:---:|:---:|:---:|:---:|
| 碎钢板 | 306.0 | 35.29 | 8.67 |
| 铁锁 | 230.0 | 30.82 | 7.46 |
| 石英岩块 | 89.0 | 33.71 | 2.64 |
| 砾岩块 | 87.0 | 34.95 | 2.49 |
| 工地砖块 | 62.0 | 29.52 | 2.10 |
| 木板 | 27.0 | 38.03 | 0.71 |

## 使用说明
### 所用硬件

### 准备软件环境
#### 树莓派3的串口BUG
在释放串口之前，我们要先解决一下树莓派3的BUG（如果用1,2代请忽略这一步）树莓派3的硬件串口被分配分配给了蓝牙模块，而GPIO14和GPIO15的串口是由内核模拟的，不稳定（可以说基本不能用)，所以首先要把GPIO14和GPIO15改成硬件驱动。

1. 确保SD卡刷了最新的raspbian jessie镜像
2. 系统启动，并连接了网络
3. 执行

```
sudo apt-get update
sudo apt-get upgrade
```

4. 编辑 /boot/config.txt 添加一行

```
dtoverlay=pi3-miniuart-bt
```

5. 最后，禁用自带蓝牙

```
sudo systemctl disable hciuart
```

#### 释放串口
编辑 /boot/cmdline.txt，默认是下面这样

```
dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
```

或者这样

```
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 kgdboc=serial0,115200 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
```

把 **console=ttyAMA0**, **console=serial0**, **kgdboc=***** 这两个参数删除，变成下面这样

```
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
```

之后`sudo reboot`重启系统，串口就可以正常使用了。

#### 打开树莓派GPIO等接口

```
sudo raspi-config
```

打开gpio，serial，i2c等接口，使其可用。

#### 安装软件依赖

```
sudo apt-get install python-requests python-lxml python-serial git build-essential python-dev python-imaging python-usb python2.7-usbtc08 alsa-utils  
sudo pip install python-escpos
git clone http://github.com/tangjiahui1014/DensityMeasurement.git
```

#### 准备串口屏幕的图片和字体资源
这个串口屏是通过TF卡加载字体和图片资源的，所以你需要准备一张TF卡，格式化为 FAT32 文件系统，分配单元大小选择 4096 字节，然后把tf_card文件夹中的文件全部copy到TF卡根目录，并把TF卡插到屏幕的卡槽里。

#### 调高提示音音量

```
sudo alsamixer
```

#### 开始运行！！！
在运行之前先编辑一下`RpiePaper/index.py`，找到下面2行，把注释取消掉，运行时会把屏幕TF卡中的文件加载到屏幕自带的NandFlash中，之后就不需要插TF卡了~

```
screen.load_pic()
time.sleep(5)
```

运行脚本
```
sudo python index.py
```

### 成品图

![image](https://raw.githubusercontent.com/tangjiahui1014/DensityMeasurement/master/Image/index.JPG)
