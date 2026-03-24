

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OrganizationKajPolicyConfigArgs', 'OrganizationKajPolicyConfig']
@pulumi.input_type
class OrganizationKajPolicyConfigArgs:
    def __init__(__self__, *, organization: pulumi.Input[_builtins.str], default_key_access_justification_policy: Optional[pulumi.Input[OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> Optional[pulumi.Input[OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]:
        
        ...
    
    @default_key_access_justification_policy.setter
    def default_key_access_justification_policy(self, value: Optional[pulumi.Input[OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _OrganizationKajPolicyConfigState:
    def __init__(__self__, *, default_key_access_justification_policy: Optional[pulumi.Input[OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> Optional[pulumi.Input[OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]:
        
        ...
    
    @default_key_access_justification_policy.setter
    def default_key_access_justification_policy(self, value: Optional[pulumi.Input[OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class OrganizationKajPolicyConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_key_access_justification_policy: Optional[pulumi.Input[Union[OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs, OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict]]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OrganizationKajPolicyConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., default_key_access_justification_policy: Optional[pulumi.Input[Union[OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs, OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict]]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ...) -> OrganizationKajPolicyConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> pulumi.Output[Optional[outputs.OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


