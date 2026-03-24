

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
__all__ = ['ProjectKajPolicyConfigArgs', 'ProjectKajPolicyConfig']
@pulumi.input_type
class ProjectKajPolicyConfigArgs:
    def __init__(__self__, *, default_key_access_justification_policy: Optional[pulumi.Input[ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> Optional[pulumi.Input[ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]:
        
        ...
    
    @default_key_access_justification_policy.setter
    def default_key_access_justification_policy(self, value: Optional[pulumi.Input[ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ProjectKajPolicyConfigState:
    def __init__(__self__, *, default_key_access_justification_policy: Optional[pulumi.Input[ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> Optional[pulumi.Input[ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]:
        
        ...
    
    @default_key_access_justification_policy.setter
    def default_key_access_justification_policy(self, value: Optional[pulumi.Input[ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ProjectKajPolicyConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_key_access_justification_policy: Optional[pulumi.Input[Union[ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs, ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ProjectKajPolicyConfigArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., default_key_access_justification_policy: Optional[pulumi.Input[Union[ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs, ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> ProjectKajPolicyConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> pulumi.Output[Optional[outputs.ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


