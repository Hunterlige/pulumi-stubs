

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MaintenanceWindowTargetArgs', 'MaintenanceWindowTarget']
@pulumi.input_type
class MaintenanceWindowTargetArgs:
    def __init__(__self__, *, resource_type: pulumi.Input[_builtins.str], targets: pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTargetTargetArgs]]], window_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner_information: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTargetTargetArgs]]]:
        
        ...
    
    @targets.setter
    def targets(self, value: pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTargetTargetArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowId")
    def window_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @window_id.setter
    def window_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerInformation")
    def owner_information(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_information.setter
    def owner_information(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _MaintenanceWindowTargetState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner_information: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., targets: Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTargetTargetArgs]]]] = ..., window_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerInformation")
    def owner_information(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_information.setter
    def owner_information(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTargetTargetArgs]]]]:
        
        ...
    
    @targets.setter
    def targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTargetTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowId")
    def window_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @window_id.setter
    def window_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class MaintenanceWindowTarget(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner_information: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MaintenanceWindowTargetTargetArgs, MaintenanceWindowTargetTargetArgsDict]]]]] = ..., window_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MaintenanceWindowTargetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner_information: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MaintenanceWindowTargetTargetArgs, MaintenanceWindowTargetTargetArgsDict]]]]] = ..., window_id: Optional[pulumi.Input[_builtins.str]] = ...) -> MaintenanceWindowTarget:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerInformation")
    def owner_information(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Output[Sequence[outputs.MaintenanceWindowTargetTarget]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowId")
    def window_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


