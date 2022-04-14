from typing import Optional, Union
import cv2
from pathlib import Path
import numpy as np


def imread(path: Union[str, Path]) -> Optional[np.ndarray]:
    with open(path, 'rb') as stream:
        bytes = bytearray(stream.read())
    numpyarray = np.asarray(bytes, dtype=np.uint8)
    if len(numpyarray) == 0:
        return None
    bgrImage = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
    if bgrImage is None:
        return None
    if bgrImage.shape[2] > 3:
        bgrImage = bgrImage[:, :, :-1].copy()
    return bgrImage


def imwrite(path: Union[str, Path], image: np.ndarray) -> None:
    path = Path(path)
    cv2.imencode(path.suffix, image)[1].tofile(path)
