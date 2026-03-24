

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['ActionRouting', 'ResourceTypeRouting', 'ValidationType']
@pulumi.type_token("azure-native:customproviders:ActionRouting")
class ActionRouting(_builtins.str, Enum):
    
    PROXY = ...


@pulumi.type_token("azure-native:customproviders:ResourceTypeRouting")
class ResourceTypeRouting(_builtins.str, Enum):
    
    PROXY = ...
    PROXY_CACHE = ...


@pulumi.type_token("azure-native:customproviders:ValidationType")
class ValidationType(_builtins.str, Enum):
    
    SWAGGER = ...


