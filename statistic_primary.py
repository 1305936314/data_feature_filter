import tqdm
import shutil
import argparse
from pathlib import Path
from configs import config_dict
from utils import subplot_hist, ImageFold2PathList, get_img_info


def imgFold_Processor(filter_cfg, proc_cfg, suffix):
    fold_root = proc_cfg["src_root"]
    dst_root = proc_cfg["dst_root"]

    print("#" * 50)
    print("Loading imgs in {} ...")
    img_list = ImageFold2PathList(fold_root, suffix)
    print("#" * 50)
    info_list = []
    print("Extracting img info ...")
    for img_path in tqdm.tqdm(img_list):
        info = get_img_info(img_path, filter_cfg)
        info_list.append(info)
    print("Complete extract")
    keys = [x for x in filter_cfg]

    if proc_cfg["plot"]:
        print("Ploting hist...")
        subplot_hist(keys, info_list)

    if proc_cfg["filter"]:
        filtered_list = info_list
        print("#" * 50)
        print("Filtering pictures")
        for key in tqdm.tqdm(keys):
            filtered_generator = filter(filter_cfg[key], filtered_list)
            filtered_list = list(filtered_generator)
            print("num of pics is {}".format(len(filtered_list)))

        if len(filtered_list) > 0:
            print("Moving pictures...")

        if isinstance(proc_cfg["proc"], str) and proc_cfg["proc"] == "copy":
            func = shutil.copy
        elif isinstance(proc_cfg["proc"], str) and proc_cfg["proc"] == "move":
            func = shutil.move
        else:
            return
        for img_dict in tqdm.tqdm(filtered_list):
            img_path = img_dict["path"]
            relative_path = Path(img_path).relative_to(fold_root)
            dst_path = Path(dst_root) / relative_path
            dst_path.parent.mkdir(exist_ok=True, parents=True)
            func(img_path, dst_path)
        print("Complete moving")


def args_parser():
    parser = argparse.ArgumentParser(description="Primary Image Filter")
    parser.add_argument("--config", type=str, default=r"primary",
                        choices=[key for key in config_dict])
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = args_parser()
    filter_cfg, processor_cfg, suffix = config_dict[args.config]
    imgFold_Processor(filter_cfg, processor_cfg, suffix)
