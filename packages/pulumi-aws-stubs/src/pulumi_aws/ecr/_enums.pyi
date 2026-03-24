

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['LifecyclePolicyActionType', 'LifecyclePolicyCountType', 'LifecyclePolicyTagStatus']
@pulumi.type_token(...)
class LifecyclePolicyActionType(_builtins.str, Enum):
    
    EXPIRE = ...


@pulumi.type_token(...)
class LifecyclePolicyCountType(_builtins.str, Enum):
    
    IMAGE_COUNT_MORE_THAN = ...
    SINCE_IMAGE_PUSHED = ...


@pulumi.type_token(...)
class LifecyclePolicyTagStatus(_builtins.str, Enum):
    
    TAGGED = ...
    UNTAGGED = ...
    ANY = ...


