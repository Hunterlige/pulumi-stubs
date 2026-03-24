

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
__all__ = ['InventoryArgs', 'Inventory']
@pulumi.input_type
class InventoryArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], destination: pulumi.Input[InventoryDestinationArgs], included_object_versions: pulumi.Input[_builtins.str], schedule: pulumi.Input[InventoryScheduleArgs], enabled: Optional[pulumi.Input[_builtins.bool]] = ..., filter: Optional[pulumi.Input[InventoryFilterArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., optional_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[InventoryDestinationArgs]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[InventoryDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedObjectVersions")
    def included_object_versions(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @included_object_versions.setter
    def included_object_versions(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[InventoryScheduleArgs]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: pulumi.Input[InventoryScheduleArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[InventoryFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[InventoryFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalFields")
    def optional_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @optional_fields.setter
    def optional_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InventoryState:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[InventoryDestinationArgs]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., filter: Optional[pulumi.Input[InventoryFilterArgs]] = ..., included_object_versions: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., optional_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[InventoryScheduleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[InventoryDestinationArgs]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[InventoryDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[InventoryFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[InventoryFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedObjectVersions")
    def included_object_versions(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @included_object_versions.setter
    def included_object_versions(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalFields")
    def optional_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @optional_fields.setter
    def optional_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[InventoryScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[InventoryScheduleArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/inventory:Inventory")
class Inventory(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[Union[InventoryDestinationArgs, InventoryDestinationArgsDict]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., filter: Optional[pulumi.Input[Union[InventoryFilterArgs, InventoryFilterArgsDict]]] = ..., included_object_versions: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., optional_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[Union[InventoryScheduleArgs, InventoryScheduleArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InventoryArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[Union[InventoryDestinationArgs, InventoryDestinationArgsDict]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., filter: Optional[pulumi.Input[Union[InventoryFilterArgs, InventoryFilterArgsDict]]] = ..., included_object_versions: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., optional_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[Union[InventoryScheduleArgs, InventoryScheduleArgsDict]]] = ...) -> Inventory:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[outputs.InventoryDestination]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[outputs.InventoryFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedObjectVersions")
    def included_object_versions(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalFields")
    def optional_fields(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[outputs.InventorySchedule]:
        
        ...
    


