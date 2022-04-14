suffix = "jpeg|jpg|png"

processor_cfg = dict()

# 特征提取： 局部特征描述子(SIFT, SURF), 预训练神经网络
processor_cfg["model_name"] = 'resnet50'
processor_cfg["pretrained_path"] = r"F:\MODEL_ZOO\ResNet\Origin\resnet50-0676ba61.pth"
processor_cfg["plot"] = True
processor_cfg["src_root"] = r"F:\cv_projects_camp\camp\tools\spyder\Image-Downloader\download_images\cup_pri_filtered"


filter_cfg = dict()
