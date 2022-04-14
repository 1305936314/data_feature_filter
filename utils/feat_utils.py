from sklearn.manifold import TSNE
import umap
import torch

__all__ = ["do_umap", "do_tsne", "get_img_feature"]


# UMAP降维
def do_umap(features, channel=2, random_state=None):
    model = umap.UMAP(n_components=channel, random_state=random_state)
    return model.fit_transform(features), model


# t-SNE降维
def do_tsne(data, random_state=0):
    tsne = TSNE(n_components=2, init='pca', random_state=random_state)
    return tsne.fit_transform(data), tsne


# 提取图像特征
def get_img_feature(model, img):
    img = torch.from_numpy(img)
    img = img.to(model.device).float()
    img = torch.unsqueeze(img, 0)  # batch size 1
    img = img.permute(0, 3, 1, 2)
    feature = model(img)
    return feature
