

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagementLockAtResourceLevelArgs', 'ManagementLockAtResourceLevel']
@pulumi.input_type
class ManagementLockAtResourceLevelArgs:
    def __init__(__self__, *, api_version: pulumi.Input[_builtins.str], level: pulumi.Input[Union[_builtins.str, LockLevel]], parent_resource_path: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], resource_name: pulumi.Input[_builtins.str], resource_provider_namespace: pulumi.Input[_builtins.str], resource_type: pulumi.Input[_builtins.str], lock_name: Optional[pulumi.Input[_builtins.str]] = ..., notes: Optional[pulumi.Input[_builtins.str]] = ..., owners: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementLockOwnerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_version.setter
    def api_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> pulumi.Input[Union[_builtins.str, LockLevel]]:
        
        ...
    
    @level.setter
    def level(self, value: pulumi.Input[Union[_builtins.str, LockLevel]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentResourcePath")
    def parent_resource_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent_resource_path.setter
    def parent_resource_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceProviderNamespace")
    def resource_provider_namespace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_provider_namespace.setter
    def resource_provider_namespace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lockName")
    def lock_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lock_name.setter
    def lock_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementLockOwnerArgs]]]]:
        
        ...
    
    @owners.setter
    def owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementLockOwnerArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ManagementLockAtResourceLevel(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_version: Optional[pulumi.Input[_builtins.str]] = ..., level: Optional[pulumi.Input[Union[_builtins.str, LockLevel]]] = ..., lock_name: Optional[pulumi.Input[_builtins.str]] = ..., notes: Optional[pulumi.Input[_builtins.str]] = ..., owners: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ManagementLockOwnerArgs, ManagementLockOwnerArgsDict]]]]] = ..., parent_resource_path: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name_: Optional[pulumi.Input[_builtins.str]] = ..., resource_provider_namespace: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagementLockAtResourceLevelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ManagementLockAtResourceLevel:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owners(self) -> pulumi.Output[Optional[Sequence[outputs.ManagementLockOwnerResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


