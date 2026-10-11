study opencv

hello world

## 任务一：工具库构建

`common` 存放可以重复使用的工具函数和接口学习资料，`__init__.py` 保留为空。

### 创建文件夹

```python
from common.FileUtils import createFolder

existed = createFolder("output")
print(existed)
```

路径已经存在时返回 `True`。路径不存在时创建路径，并返回 `False`。返回值表示调用前路径是否存在。调用时请传入具体的文件夹路径。

`FileUtils.py` 的演示代码放在 `if __name__ == "__main__":` 下，其他程序导入工具函数时不会自动创建演示文件夹。

### 补充说明：查阅 OpenCV 接口

- [connectedComponentsWithStats 中文接口说明](common/connectedComponentsWithStats_接口说明.md)
- [已有函数接口截图](common/接口说明.png)
- [官方函数页面截图](common/connectedComponentsWithStats_官方接口.jpg)
- [官方参数说明截图](common/connectedComponentsWithStats_参数说明.jpg)

官方来源：https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html

### Git 的常用操作

`clone` 获取远程仓库及其历史，`commit` 保存本地修改记录，`push` 上传本地提交，`pull` 获取并整合远程分支的新提交。每次修改工具函数或资料后，先检查改动，再提交并推送。
