# AMD虚拟机安装MacOS系统

## 首先安装VMware

目前测试最新版VMwar15.10不行，VMware15.1可以

刚安装的VMware是没有支持安装MacOS，需要[下载解锁工具](#下载解锁工具)解锁后才能选择安装MacOS

## 下载解锁工具

[下载地址](https://www.lanzoux.com/i32SQfqw44b)

**已管理员身份运行`win-install.cmd`**

![](https://gitee.com/koyangyang/pictures/raw/master/20200818095345.png)

到目前为止，VMware就支持安装MacOS了

## 创建MacOS

解锁完创建就可以创建MacOS系统

![](https://gitee.com/koyangyang/pictures/raw/master/20200818100054.png)

## 编辑`.vmx`文件

打开MacOS虚拟机目录，用编辑打开`.vmx`文件

![](https://gitee.com/koyangyang/pictures/raw/master/20200818095013.png)

```vmx
smc.version = "0"
cpuid.0.eax = "0000:0000:0000:0000:0000:0000:0000:1011"
cpuid.0.ebx = "0111:0101:0110:1110:0110:0101:0100:0111"
cpuid.0.ecx = "0110:1100:0110:0101:0111:0100:0110:1110"
cpuid.0.edx = "0100:1001:0110:0101:0110:1110:0110:1001"
cpuid.1.eax = "0000:0000:0000:0001:0000:0110:0111:0001"
cpuid.1.ebx = "0000:0010:0000:0001:0000:1000:0000:0000"
cpuid.1.ecx = "1000:0010:1001:1000:0010:0010:0000:0011"
cpuid.1.edx = "0000:1111:1010:1011:1111:1011:1111:1111"
featureCompat.enable = "FALSE"
```

**一定要在这两行中插入代码**

![](https://gitee.com/koyangyang/pictures/raw/master/20200818100455.png)

## 启动安装

![](http://p.ananas.chaoxing.com/star3/origin/90cfd4b8e52aae51e3ccc98a56c044ad.png)

## FAQ

### 1.没有网络

把网络设为`桥接模式`

![](https://gitee.com/koyangyang/pictures/raw/master/20200818100916.png)

### 2.报错"这个虚拟机需要avx2，但是没有avx"

将vmx文件中 **virtualHW.version = "16"**改为 **virtualHW.version = "10"**

### 3.无法使用鼠标键盘

1、关闭虚拟机。

2、找到 vmx文件，在其中添加：

**keyboard.vusb.enable = "TRUE"**

**mouse.vusb.enable = "TRUE"**

3、把虚拟机设置，选择“硬件”的“USB控制器”，

   在左侧的界面里勾选“显示所有USB输入设备（S）”，并把顶部的“USB兼容性（C）”改为USB2.0。

4、重启虚拟机。

### 4.虚拟机进入BIOS

```
1.常规方法：
开启虚拟机，按F2键，注意要将鼠标点进虚拟机环境中
 
2.特殊情况,按F2键无反应：
进入虚拟机目录，找到vmx文件，在文件最前端加入一行：
 
bios.forceSetupOnce = "TRUE"
 
保存后开启虚拟机直接进入bios
该方法只生效一次
下次如需进入bios需重新编辑vmx文件
 
 
3.延长bios等待时间：
在vmx文件前端加入：
 
bios.bootDelay = "6000"
注意保存。
6000=6秒，可自行设置。
 
如果进入bios后无法引导进入光盘镜像，
例如 .cdr 镜像文件，
或许是 cdr文件本身经过修改，
可更换为其他镜像。
```

