config_dict = dict()
from .primary_config import filter_cfg, processor_cfg, suffix
config_dict["primary"] = (filter_cfg, processor_cfg, suffix)
from .primary_config_L import filter_cfg, processor_cfg, suffix
config_dict["primary_L"] = (filter_cfg, processor_cfg, suffix)
from .advanced_config import filter_cfg, processor_cfg, suffix
config_dict["advanced"] = (filter_cfg, processor_cfg, suffix)
