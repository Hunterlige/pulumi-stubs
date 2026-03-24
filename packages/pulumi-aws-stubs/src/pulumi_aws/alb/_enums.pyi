

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['IpAddressType', 'LoadBalancerType']
@pulumi.type_token("aws:alb/IpAddressType:IpAddressType")
class IpAddressType(_builtins.str, Enum):
    IPV4 = ...
    DUALSTACK = ...
    DUALSTACK_WITHOUT_PUBLIC_IPV4 = ...


@pulumi.type_token("aws:alb/LoadBalancerType:LoadBalancerType")
class LoadBalancerType(_builtins.str, Enum):
    APPLICATION = ...
    NETWORK = ...


