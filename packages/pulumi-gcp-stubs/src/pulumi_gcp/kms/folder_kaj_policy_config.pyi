

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
__all__ = ['FolderKajPolicyConfigArgs', 'FolderKajPolicyConfig']
@pulumi.input_type
class FolderKajPolicyConfigArgs:
    def __init__(__self__, *, folder: pulumi.Input[_builtins.str], default_key_access_justification_policy: Optional[pulumi.Input[FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @folder.setter
    def folder(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> Optional[pulumi.Input[FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]:
        
        ...
    
    @default_key_access_justification_policy.setter
    def default_key_access_justification_policy(self, value: Optional[pulumi.Input[FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _FolderKajPolicyConfigState:
    def __init__(__self__, *, default_key_access_justification_policy: Optional[pulumi.Input[FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> Optional[pulumi.Input[FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]:
        
        ...
    
    @default_key_access_justification_policy.setter
    def default_key_access_justification_policy(self, value: Optional[pulumi.Input[FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class FolderKajPolicyConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_key_access_justification_policy: Optional[pulumi.Input[Union[FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs, FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict]]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FolderKajPolicyConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., default_key_access_justification_policy: Optional[pulumi.Input[Union[FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs, FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict]]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ...) -> FolderKajPolicyConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeyAccessJustificationPolicy")
    def default_key_access_justification_policy(self) -> pulumi.Output[Optional[outputs.FolderKajPolicyConfigDefaultKeyAccessJustificationPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


