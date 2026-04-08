import builtins as _builtins
import pulumi
from enum import Enum

__all__ = [
    "ActionType",
    "BlockResponseCode",
    "DnsSecurityRuleState",
    "ForwardingRuleState",
    "IpAllocationMethod",
]

@pulumi.type_token("azure-native:dnsresolver:ActionType")
class ActionType(_builtins.str, Enum):
    ALLOW = ...
    ALERT = ...
    BLOCK = ...

@pulumi.type_token("azure-native:dnsresolver:BlockResponseCode")
class BlockResponseCode(_builtins.str, Enum):
    SERVFAIL = ...

@pulumi.type_token("azure-native:dnsresolver:DnsSecurityRuleState")
class DnsSecurityRuleState(_builtins.str, Enum):
    ENABLED = ...
    DISABLED = ...

@pulumi.type_token("azure-native:dnsresolver:ForwardingRuleState")
class ForwardingRuleState(_builtins.str, Enum):
    ENABLED = ...
    DISABLED = ...

@pulumi.type_token("azure-native:dnsresolver:IpAllocationMethod")
class IpAllocationMethod(_builtins.str, Enum):
    STATIC = ...
    DYNAMIC = ...
