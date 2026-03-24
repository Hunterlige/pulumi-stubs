

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['ExtendedLocationType', 'KubernetesSecretType']
@pulumi.type_token(...)
class ExtendedLocationType(_builtins.str, Enum):
    
    EDGE_ZONE = ...
    CUSTOM_LOCATION = ...


@pulumi.type_token(...)
class KubernetesSecretType(_builtins.str, Enum):
    
    OPAQUE = ...
    TLS = ...


