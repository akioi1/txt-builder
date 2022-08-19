# txt-builder
一个图片文字生成器

# 前言
国际惯例，先扔仓库地址[link](https://github.com/akioi1/txt-builder)，另外，不喜勿喷

# 预处理
这个代码是在作者的电脑上所运行测试的，由于我是在桌面运行，考虑到操作系统，电脑用户名，安装的地方都会影响代码的运行，所以你需要实现改那么一下下的代码

1. 打开父目录下的（就有三个文件夹下面那个）`run.py`,有三个C盘路径，请把第一个`C:/Users/Administrator/Desktop/txt builder/image/CSPRP++.jpg`，改成你的路径+`/txt builder/image/CSPRP++.jpg`（比如，在F盘，就是`F:/`+`/txt builder/image/CSPRP++.jpg`）

第二个`C:/Users/Administrator/Desktop/txt builder/image2/*.jpg`改成你的路径+`/txt builder/image2/*.jpg`

第三个`C:/Users/Administrator/Desktop/txt builder/out.jpg`改成你的路径+`/txt builder/out.jpg`

至此，这个代码改完了

来到`txt builder\txt-builder\firstimage`，打开这里的`run.py`，有两个路径

第一个`C:/Users/Administrator/Desktop/txt builder/firstimage/`改成你的路径+`/txt builder/firstimage/`

第二个`C:/Users/Administrator/Desktop/txt builder/image2/`改成你的路径+`/txt builder/image2/`

至此，预处理完毕，代码改完了，不需要在对代码进行操作

# 使用教程

1. 由于本生成器用Python所编写，并且依赖几个Python包，请确保你的电脑上安装了Python3，并且安装了`photomosaic`，`os`,`Pillow`这几个包，如果没有，请自行安装

2. 首先，你需要准备一堆图片，越多，最后的效果就越~~五彩斑斓~~多样（这里默认你用的是洛谷用户头像，其他长图宽图没试过，可能有bug），将其存在`firstimage`这个文件夹内，存完后，运行该文件夹下的`run.py`进行预处理

3. 预处理完毕后，请到`image2`文件夹内查看你的图片是否在这个文件夹内（有个`1.jpg`图片，请不要动它）

4. 最后一步，运行`run.py`（父目录，也就是有三个文件夹下面的那个），然后耐心等待

5. 结果保存为`out.jpg`

# 后言

如果有bug或者更新建议，可以在Github的issue下提出（虽然这个垃圾有很大概率做不到）

# 关于协议

你可以自由下载使用这个东西，也可以宣传，但必须注明原作者，并且不能收费，这个东东完全免费~~因为它太烂了，不值得收钱~~

# 目前缺点

1. 生成出的图片放大后看不清小图片（未解决）

# 即将可能大概也许有概论更新的

目前，无
