from .base import best_device, Pruner
from .sgd_pruner import get_sgd_pruner, SGDPruner

from typing import Optional

import torch.nn as nn
import torch.optim as optim


def get_causal_pruner(
        model: nn.Module, optimizer: optim.Optimizer, **kwargs) -> Optional[Pruner]:
    if isinstance(optimizer, optim.SGD):
        momentum = optimizer.defaults['momentum'] > 0
        return get_sgd_pruner(model, momentum=momentum, **kwargs)
    raise NotImplementedError(
        f"CausalPruner is not implemented for optimizer of type {type(optim)}")
