# connectedComponentsWithStats() 官方接口说明

官方文档：https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html#ga107a78bf7cd25dec05fb4dfc5c9e765f

查阅日期：2026年10月11日。官方网页截图与本文放在同一个 `common` 文件夹下。

## 作用

在单通道二值图中，给相互连接的前景像素分组。每个连通区域得到一个编号，同时返回区域的位置、大小、面积和质心。

这里通常用 0 表示背景、255 表示前景，函数按非零像素识别前景。标签 0 表示背景。

## Python 调用形式

```python
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    binary,
    connectivity=8,
    ltype=cv2.CV_32S
)
```

`binary` 是已经准备好的 8 位单通道二值图。使用前先 `import cv2`。上面展示接口调用形式，不能在没有定义 `binary` 时直接运行。

## 输入参数

| 参数 | 含义 |
|---|---|
| image / binary | 待分析的 8 位单通道图像，常用 `uint8` 二值图 |
| connectivity=4 | 上、下、左、右邻接的前景像素才算连接 |
| connectivity=8 | 还包含四个对角方向，默认使用 8 邻域 |
| ltype=cv2.CV_32S | 标签图的数据类型，默认是 32 位有符号整数，另支持 `CV_16U` |

## 四个返回值

| 返回值 | 含义 |
|---|---|
| num_labels | 标签总数，包含背景标签 0，前景区域数为 `num_labels - 1` |
| labels | 与输入图宽高相同，每个像素的值表示所属区域编号 |
| stats | 每个标签的一行统计信息，包含背景行，类型是 `int32` |
| centroids | 每个标签的质心坐标 `(cx, cy)`，包含背景行，类型是 `float64` |

## stats 的五列

每行顺序是 `[左上角x, 左上角y, 宽度, 高度, 面积]`，对应常量如下。

| 列索引 | OpenCV 常量 | 含义 |
|---|---|---|
| 0 | cv2.CC_STAT_LEFT | 区域外接矩形左上角横坐标 |
| 1 | cv2.CC_STAT_TOP | 区域外接矩形左上角纵坐标 |
| 2 | cv2.CC_STAT_WIDTH | 外接矩形宽度 |
| 3 | cv2.CC_STAT_HEIGHT | 外接矩形高度 |
| 4 | cv2.CC_STAT_AREA | 该连通区域实际包含的像素数，通常不同于宽度乘高度 |

处理前景区域时遍历 `range(1, num_labels)`，跳过编号 0 的背景。

质心是区域内所有像素横坐标、纵坐标分别求平均得到的位置。

## 本任务的完成内容

已经查阅官方接口，并保存函数说明和参数说明的网页截图。本任务的补充要求是查阅和保存接口资料，不要求额外实现一套连通区域识别程序。
