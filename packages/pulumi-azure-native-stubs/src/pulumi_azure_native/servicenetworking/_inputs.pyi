

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssociationSubnetArgs', 'AssociationSubnetArgsDict', 'SecurityPolicyConfigurationsArgs', 'SecurityPolicyConfigurationsArgsDict', 'WafPolicyArgs', 'WafPolicyArgsDict', 'WafSecurityPolicyArgs', 'WafSecurityPolicyArgsDict']
class AssociationSubnetArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class AssociationSubnetArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecurityPolicyConfigurationsArgsDict(TypedDict):
    
    waf_security_policy: NotRequired[pulumi.Input[WafSecurityPolicyArgsDict]]


@pulumi.input_type
class SecurityPolicyConfigurationsArgs:
    def __init__(__self__, *, waf_security_policy: Optional[pulumi.Input[WafSecurityPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wafSecurityPolicy")
    def waf_security_policy(self) -> Optional[pulumi.Input[WafSecurityPolicyArgs]]:
        
        ...
    
    @waf_security_policy.setter
    def waf_security_policy(self, value: Optional[pulumi.Input[WafSecurityPolicyArgs]]): # -> None:
        ...
    


class WafPolicyArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class WafPolicyArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WafSecurityPolicyArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class WafSecurityPolicyArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


