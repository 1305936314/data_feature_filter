import numpy as np
import tqdm
import argparse
from pathlib import Path
from utils import plot_embedding, ImageFold2PathList, get_img_info, get_img_feature, do_tsne, do_umap
from pretrained_model import model_dict
from configs import config_dict


def imgFold_Processor(filter_cfg, proc_cfg, suffix):
    fold_root = proc_cfg["src_root"]
    # dst_root = proc_cfg["dst_root"]
    pretrained_path = proc_cfg["pretrained_path"]
    print("#" * 50)
    print("Using model {} to Extract data features ...".format(proc_cfg["model_name"]))
    model = model_dict[proc_cfg["model_name"]](pretrained_path)

    print("#" * 50)
    print("Loading imgs in {} ...".format(fold_root))
    img_list = ImageFold2PathList(fold_root, suffix)
    print("#" * 50)
    info_list = []
    print("Extracting img info ...")
    for img_path in tqdm.tqdm(img_list):
        info = get_img_info(img_path, filter_cfg)
        mean, std = get_img_feature(model, info['img'])
        mean = mean.to('cpu').numpy().reshape(-1)
        std = std.to('cpu').numpy().reshape(-1)
        feature = np.concatenate((mean, std), 0)
        # print(feature.shape)
        info["feature"] = feature
        info_list.append(info)
    print("Complete extract")

    if proc_cfg["plot"]:
        print("Prepare data for plot ...")

        name_list = []
        feat_list = []
        for info in tqdm.tqdm(info_list):
            name = int(Path(info["path"]).stem.split("_")[1])
            feat = info["feature"]
            name_list.append(name)
            feat_list.append(feat)
        print("Ploting ...")
        tsne_feature, _ = do_tsne(np.array(feat_list))
        umap_feature, _ = do_umap(np.array(feat_list))
        plot_embedding(tsne_feature, text=name_list, title="tsne feat")
        plot_embedding(umap_feature, text=name_list, title="umap feat")
        print("Complete")


def args_parser():
    parser = argparse.ArgumentParser(description="Primary Image Filter")
    parser.add_argument("--config", type=str, default=r"advanced",
                        choices=[key for key in config_dict])
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = args_parser()
    filter_cfg, processor_cfg, suffix = config_dict[args.config]
    imgFold_Processor(filter_cfg, processor_cfg, suffix)
