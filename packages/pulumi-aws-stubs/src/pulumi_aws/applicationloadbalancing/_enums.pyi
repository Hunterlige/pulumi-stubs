import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["IpAddressType", "LoadBalancerType"]

@pulumi.type_token(...)
class IpAddressType(_builtins.str, Enum):
    IPV4 = ...
    DUALSTACK = ...

@pulumi.type_token(...)
class LoadBalancerType(_builtins.str, Enum):
    APPLICATION = ...
    NETWORK = ...
