import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import resnet50


def global_std_pool2d(x):
    """2D global standard variation pooling"""
    return torch.std(x.view(x.size()[0], x.size()[1], -1, 1), dim=2, keepdim=True)


class ResNet50(nn.Module):
    """预训练ResNet50模型 修改以提取特征"""
    def __init__(self, model_path):
        super(ResNet50, self).__init__()
        model = resnet50()
        model.load_state_dict(torch.load(model_path), strict=True)
        self.features = nn.Sequential(*list(model.children())[:-2])

        # 冻结模型
        for p in self.features.parameters():
            p.requires_grad = False
        # self.features.eval()

        # 检测是否有GPU
        self.device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        # self.device = torch.device("cpu")
        self.to(self.device)

    def forward(self, x):
        # features@: 7 -> res5c
        for ii, model in enumerate(self.features):
            x = model(x)
            if ii == 7:
                features_mean = F.adaptive_avg_pool2d(x, 1)
                features_std = global_std_pool2d(x)
                return features_mean, features_std
