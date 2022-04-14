suffix = "jpeg|jpg|png"

"""
图片大小：10k ~ 1M
图片分辨率：
    宽 : 300 ~ 2000
    高 : 300 ~ 2000
图片梯度平均绝对值:
    < 50
"""
filter_cfg = dict()
filter_cfg["size"] = lambda x: 10 * 1024 < x["size"] < 1000 * 1024  # 10k~1M
filter_cfg["width"] = lambda x: 300 <= x["width"] < 2000
filter_cfg["height"] = lambda x: 300 <= x["height"] < 2000
filter_cfg["grad"] = lambda x: x["grad"] < 150  # 图片平滑程度


"""
plot：    是否画图
filter：  是否过滤，否的话则不考虑
proc：    False则不操作，copy复制，move则移动
"""
processor_cfg = dict()
processor_cfg["plot"] = True
processor_cfg["filter"] = True
processor_cfg["proc"] = "move"  # "copy" / "move" / False
processor_cfg["src_root"] = r"F:\cv_projects_camp\camp\tools\spyder\Image-Downloader\download_images\cup"
processor_cfg["dst_root"] = r"F:\cv_projects_camp\camp\tools\spyder\Image-Downloader\download_images\cup_pri_filtered"


