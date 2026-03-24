

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
__all__ = ['OrganizationPolicyArgs', 'OrganizationPolicy']
@pulumi.input_type
class OrganizationPolicyArgs:
    def __init__(__self__, *, constraint: pulumi.Input[_builtins.str], folder: pulumi.Input[_builtins.str], boolean_policy: Optional[pulumi.Input[OrganizationPolicyBooleanPolicyArgs]] = ..., list_policy: Optional[pulumi.Input[OrganizationPolicyListPolicyArgs]] = ..., restore_policy: Optional[pulumi.Input[OrganizationPolicyRestorePolicyArgs]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def constraint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @constraint.setter
    def constraint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @folder.setter
    def folder(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanPolicy")
    def boolean_policy(self) -> Optional[pulumi.Input[OrganizationPolicyBooleanPolicyArgs]]:
        
        ...
    
    @boolean_policy.setter
    def boolean_policy(self, value: Optional[pulumi.Input[OrganizationPolicyBooleanPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listPolicy")
    def list_policy(self) -> Optional[pulumi.Input[OrganizationPolicyListPolicyArgs]]:
        
        ...
    
    @list_policy.setter
    def list_policy(self, value: Optional[pulumi.Input[OrganizationPolicyListPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> Optional[pulumi.Input[OrganizationPolicyRestorePolicyArgs]]:
        
        ...
    
    @restore_policy.setter
    def restore_policy(self, value: Optional[pulumi.Input[OrganizationPolicyRestorePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _OrganizationPolicyState:
    def __init__(__self__, *, boolean_policy: Optional[pulumi.Input[OrganizationPolicyBooleanPolicyArgs]] = ..., constraint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., list_policy: Optional[pulumi.Input[OrganizationPolicyListPolicyArgs]] = ..., restore_policy: Optional[pulumi.Input[OrganizationPolicyRestorePolicyArgs]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanPolicy")
    def boolean_policy(self) -> Optional[pulumi.Input[OrganizationPolicyBooleanPolicyArgs]]:
        
        ...
    
    @boolean_policy.setter
    def boolean_policy(self, value: Optional[pulumi.Input[OrganizationPolicyBooleanPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def constraint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @constraint.setter
    def constraint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listPolicy")
    def list_policy(self) -> Optional[pulumi.Input[OrganizationPolicyListPolicyArgs]]:
        
        ...
    
    @list_policy.setter
    def list_policy(self, value: Optional[pulumi.Input[OrganizationPolicyListPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> Optional[pulumi.Input[OrganizationPolicyRestorePolicyArgs]]:
        
        ...
    
    @restore_policy.setter
    def restore_policy(self, value: Optional[pulumi.Input[OrganizationPolicyRestorePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("gcp:folder/organizationPolicy:OrganizationPolicy")
class OrganizationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., boolean_policy: Optional[pulumi.Input[Union[OrganizationPolicyBooleanPolicyArgs, OrganizationPolicyBooleanPolicyArgsDict]]] = ..., constraint: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., list_policy: Optional[pulumi.Input[Union[OrganizationPolicyListPolicyArgs, OrganizationPolicyListPolicyArgsDict]]] = ..., restore_policy: Optional[pulumi.Input[Union[OrganizationPolicyRestorePolicyArgs, OrganizationPolicyRestorePolicyArgsDict]]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OrganizationPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., boolean_policy: Optional[pulumi.Input[Union[OrganizationPolicyBooleanPolicyArgs, OrganizationPolicyBooleanPolicyArgsDict]]] = ..., constraint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., list_policy: Optional[pulumi.Input[Union[OrganizationPolicyListPolicyArgs, OrganizationPolicyListPolicyArgsDict]]] = ..., restore_policy: Optional[pulumi.Input[Union[OrganizationPolicyRestorePolicyArgs, OrganizationPolicyRestorePolicyArgsDict]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> OrganizationPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanPolicy")
    def boolean_policy(self) -> pulumi.Output[Optional[outputs.OrganizationPolicyBooleanPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def constraint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listPolicy")
    def list_policy(self) -> pulumi.Output[Optional[outputs.OrganizationPolicyListPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> pulumi.Output[Optional[outputs.OrganizationPolicyRestorePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


