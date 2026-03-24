

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MaintenanceConfigurationArgs', 'MaintenanceConfiguration']
@pulumi.input_type
class MaintenanceConfigurationArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], duration: Optional[pulumi.Input[_builtins.str]] = ..., expiration_date_time: Optional[pulumi.Input[_builtins.str]] = ..., extension_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., install_patches: Optional[pulumi.Input[InputPatchConfigurationArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_scope: Optional[pulumi.Input[Union[_builtins.str, MaintenanceScope]]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., recur_every: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., start_date_time: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., visibility: Optional[pulumi.Input[Union[_builtins.str, Visibility]]] = ...) -> None:
        
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
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDateTime")
    def expiration_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_date_time.setter
    def expiration_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionProperties")
    def extension_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @extension_properties.setter
    def extension_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="installPatches")
    def install_patches(self) -> Optional[pulumi.Input[InputPatchConfigurationArgs]]:
        
        ...
    
    @install_patches.setter
    def install_patches(self, value: Optional[pulumi.Input[InputPatchConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceScope")
    def maintenance_scope(self) -> Optional[pulumi.Input[Union[_builtins.str, MaintenanceScope]]]:
        
        ...
    
    @maintenance_scope.setter
    def maintenance_scope(self, value: Optional[pulumi.Input[Union[_builtins.str, MaintenanceScope]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurEvery")
    def recur_every(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recur_every.setter
    def recur_every(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_date_time.setter
    def start_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[Union[_builtins.str, Visibility]]]:
        
        ...
    
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[Union[_builtins.str, Visibility]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:maintenance:MaintenanceConfiguration")
class MaintenanceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., duration: Optional[pulumi.Input[_builtins.str]] = ..., expiration_date_time: Optional[pulumi.Input[_builtins.str]] = ..., extension_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., install_patches: Optional[pulumi.Input[Union[InputPatchConfigurationArgs, InputPatchConfigurationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_scope: Optional[pulumi.Input[Union[_builtins.str, MaintenanceScope]]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., recur_every: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name_: Optional[pulumi.Input[_builtins.str]] = ..., start_date_time: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., visibility: Optional[pulumi.Input[Union[_builtins.str, Visibility]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MaintenanceConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> MaintenanceConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDateTime")
    def expiration_date_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionProperties")
    def extension_properties(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installPatches")
    def install_patches(self) -> pulumi.Output[Optional[outputs.InputPatchConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceScope")
    def maintenance_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurEvery")
    def recur_every(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


