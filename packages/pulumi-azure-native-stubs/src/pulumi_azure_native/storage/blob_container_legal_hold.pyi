

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BlobContainerLegalHoldArgs', 'BlobContainerLegalHold']
@pulumi.input_type
class BlobContainerLegalHoldArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], container_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], tags: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allow_protected_append_writes_all: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
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
    @pulumi.getter
    def tags(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWritesAll")
    def allow_protected_append_writes_all(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_protected_append_writes_all.setter
    def allow_protected_append_writes_all(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storage:BlobContainerLegalHold")
class BlobContainerLegalHold(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., allow_protected_append_writes_all: Optional[pulumi.Input[_builtins.bool]] = ..., container_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BlobContainerLegalHoldArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BlobContainerLegalHold:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWritesAll")
    def allow_protected_append_writes_all(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


