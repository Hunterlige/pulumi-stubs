

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BlobContainerImmutabilityPolicyArgs', 'BlobContainerImmutabilityPolicy']
@pulumi.input_type
class BlobContainerImmutabilityPolicyArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], container_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], allow_protected_append_writes: Optional[pulumi.Input[_builtins.bool]] = ..., allow_protected_append_writes_all: Optional[pulumi.Input[_builtins.bool]] = ..., immutability_period_since_creation_in_days: Optional[pulumi.Input[_builtins.int]] = ..., immutability_policy_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWrites")
    def allow_protected_append_writes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_protected_append_writes.setter
    def allow_protected_append_writes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWritesAll")
    def allow_protected_append_writes_all(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_protected_append_writes_all.setter
    def allow_protected_append_writes_all(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutabilityPeriodSinceCreationInDays")
    def immutability_period_since_creation_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @immutability_period_since_creation_in_days.setter
    def immutability_period_since_creation_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutabilityPolicyName")
    def immutability_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @immutability_policy_name.setter
    def immutability_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BlobContainerImmutabilityPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., allow_protected_append_writes: Optional[pulumi.Input[_builtins.bool]] = ..., allow_protected_append_writes_all: Optional[pulumi.Input[_builtins.bool]] = ..., container_name: Optional[pulumi.Input[_builtins.str]] = ..., immutability_period_since_creation_in_days: Optional[pulumi.Input[_builtins.int]] = ..., immutability_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BlobContainerImmutabilityPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BlobContainerImmutabilityPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWrites")
    def allow_protected_append_writes(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWritesAll")
    def allow_protected_append_writes_all(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutabilityPeriodSinceCreationInDays")
    def immutability_period_since_creation_in_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


