

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
__all__ = ['PolicyArgs', 'Policy']
@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *, constraint: pulumi.Input[_builtins.str], org_id: pulumi.Input[_builtins.str], boolean_policy: Optional[pulumi.Input[PolicyBooleanPolicyArgs]] = ..., list_policy: Optional[pulumi.Input[PolicyListPolicyArgs]] = ..., restore_policy: Optional[pulumi.Input[PolicyRestorePolicyArgs]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def constraint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @constraint.setter
    def constraint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanPolicy")
    def boolean_policy(self) -> Optional[pulumi.Input[PolicyBooleanPolicyArgs]]:
        
        ...
    
    @boolean_policy.setter
    def boolean_policy(self, value: Optional[pulumi.Input[PolicyBooleanPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listPolicy")
    def list_policy(self) -> Optional[pulumi.Input[PolicyListPolicyArgs]]:
        
        ...
    
    @list_policy.setter
    def list_policy(self, value: Optional[pulumi.Input[PolicyListPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> Optional[pulumi.Input[PolicyRestorePolicyArgs]]:
        
        ...
    
    @restore_policy.setter
    def restore_policy(self, value: Optional[pulumi.Input[PolicyRestorePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *, boolean_policy: Optional[pulumi.Input[PolicyBooleanPolicyArgs]] = ..., constraint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., list_policy: Optional[pulumi.Input[PolicyListPolicyArgs]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., restore_policy: Optional[pulumi.Input[PolicyRestorePolicyArgs]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanPolicy")
    def boolean_policy(self) -> Optional[pulumi.Input[PolicyBooleanPolicyArgs]]:
        
        ...
    
    @boolean_policy.setter
    def boolean_policy(self, value: Optional[pulumi.Input[PolicyBooleanPolicyArgs]]): # -> None:
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
    @pulumi.getter(name="listPolicy")
    def list_policy(self) -> Optional[pulumi.Input[PolicyListPolicyArgs]]:
        
        ...
    
    @list_policy.setter
    def list_policy(self, value: Optional[pulumi.Input[PolicyListPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> Optional[pulumi.Input[PolicyRestorePolicyArgs]]:
        
        ...
    
    @restore_policy.setter
    def restore_policy(self, value: Optional[pulumi.Input[PolicyRestorePolicyArgs]]): # -> None:
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
    


@pulumi.type_token("gcp:organizations/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., boolean_policy: Optional[pulumi.Input[Union[PolicyBooleanPolicyArgs, PolicyBooleanPolicyArgsDict]]] = ..., constraint: Optional[pulumi.Input[_builtins.str]] = ..., list_policy: Optional[pulumi.Input[Union[PolicyListPolicyArgs, PolicyListPolicyArgsDict]]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., restore_policy: Optional[pulumi.Input[Union[PolicyRestorePolicyArgs, PolicyRestorePolicyArgsDict]]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., boolean_policy: Optional[pulumi.Input[Union[PolicyBooleanPolicyArgs, PolicyBooleanPolicyArgsDict]]] = ..., constraint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., list_policy: Optional[pulumi.Input[Union[PolicyListPolicyArgs, PolicyListPolicyArgsDict]]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., restore_policy: Optional[pulumi.Input[Union[PolicyRestorePolicyArgs, PolicyRestorePolicyArgsDict]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> Policy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanPolicy")
    def boolean_policy(self) -> pulumi.Output[Optional[outputs.PolicyBooleanPolicy]]:
        
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
    @pulumi.getter(name="listPolicy")
    def list_policy(self) -> pulumi.Output[Optional[outputs.PolicyListPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> pulumi.Output[Optional[outputs.PolicyRestorePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


