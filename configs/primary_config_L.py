suffix = "jpeg|jpg|png"

"""
图片大小：10k ~ 0.5M
图片分辨率：
    宽 : 400 ~ 2000
    高 : 400 ~ 2000
图片梯度平均绝对值:
    > 100
"""
filter_cfg = dict()
filter_cfg["size"] = lambda x: 10 * 1024 < x["size"] < 512 * 1024  # 10k~10M
filter_cfg["width"] = lambda x: 400 <= x["width"] < 5000
filter_cfg["height"] = lambda x: 400 <= x["height"] < 5000
filter_cfg["grad"] = lambda x: x["grad"] > 100  # 图片平滑程度


"""
plot：    是否画图
filter：  是否过滤，否的话则不考虑
proc：    False则不操作，copy复制，move则移动
"""
processor_cfg = dict()
processor_cfg["plot"] = True
processor_cfg["filter"] = True
processor_cfg["proc"] = 'copy'  # "copy"  # "copy" / "move" / False
processor_cfg["src_root"] = r"F:\cv_projects_camp\camp\tools\spyder\Image-Downloader\download_images\cow"
processor_cfg["dst_root"] = r"F:\cv_projects_camp\camp\tools\spyder\Image-Downloader\download_images\cow_pri_filtered"
