# data_feature_filter

初级筛选：通过对图像的基础属性进行筛选

高级筛选：通过对图像提取特征进行筛选

> configs: 通过字典存储过滤条件，处理方式和地址

> pretrained_model: 不同模型的Module类

> utils: 获取图像信息，特征，图片io，以及画图组件

# TODO

- [ ] 增加聚类方法：kmeans, DBSCAN, OPTICS

- [ ] 增加聚类后剔除异常数据的方法

- [ ] 增加局部特征描述子：SIFT, SURF

# 说明

## 0.requirements(运行所需库)

### primary
- numpy
- matplotlib
- opencv
- tqdm

### advanced(optional)
- torch
- torchvision
- umap-learn
- scikit-learn

## 1. 运行方式

**primary**:

python statistic_primary.py --config primary

> 选择有 ['primary', 'primary_L']

**advanced**：

python statistic_advanced.py -config advanced

> 可以自行通过编写或更改config后加入__init__中的字典来增加可选项
 
## 2. 注意事项

1. primary和advanced配置文件不可混用，导入init时由于名称相同，要紧挨着导入dict的语句前
2. 对大图进行特征提取时容易炸显存（0.5M以下为宜），要在pretrained_model中手动将self.device改为cpu
3. 暂时没有advanced方法的图片筛选，需要通过二维的特征分布图，寻找离群点
4. 用神经网络提取图像特征时需要下载预训练模型，[ResNet50](https://download.pytorch.org/models/resnet50-19c8e357.pth)