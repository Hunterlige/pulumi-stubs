

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
__all__ = ['SnapshotSettingsArgs', 'SnapshotSettings']
@pulumi.input_type
class SnapshotSettingsArgs:
    def __init__(__self__, *, storage_location: pulumi.Input[SnapshotSettingsStorageLocationArgs], project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Input[SnapshotSettingsStorageLocationArgs]:
        
        ...
    
    @storage_location.setter
    def storage_location(self, value: pulumi.Input[SnapshotSettingsStorageLocationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SnapshotSettingsState:
    def __init__(__self__, *, project: Optional[pulumi.Input[_builtins.str]] = ..., storage_location: Optional[pulumi.Input[SnapshotSettingsStorageLocationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input[SnapshotSettingsStorageLocationArgs]]:
        
        ...
    
    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input[SnapshotSettingsStorageLocationArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/snapshotSettings:SnapshotSettings")
class SnapshotSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., storage_location: Optional[pulumi.Input[Union[SnapshotSettingsStorageLocationArgs, SnapshotSettingsStorageLocationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SnapshotSettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., storage_location: Optional[pulumi.Input[Union[SnapshotSettingsStorageLocationArgs, SnapshotSettingsStorageLocationArgsDict]]] = ...) -> SnapshotSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Output[outputs.SnapshotSettingsStorageLocation]:
        
        ...
    


