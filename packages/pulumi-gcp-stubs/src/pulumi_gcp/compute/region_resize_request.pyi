

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
__all__ = ['RegionResizeRequestArgs', 'RegionResizeRequest']
@pulumi.input_type
class RegionResizeRequestArgs:
    def __init__(__self__, *, instance_group_manager: pulumi.Input[_builtins.str], resize_by: pulumi.Input[_builtins.int], description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., requested_run_duration: Optional[pulumi.Input[RegionResizeRequestRequestedRunDurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManager")
    def instance_group_manager(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_group_manager.setter
    def instance_group_manager(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resizeBy")
    def resize_by(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @resize_by.setter
    def resize_by(self, value: pulumi.Input[_builtins.int]): # -> None:
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedRunDuration")
    def requested_run_duration(self) -> Optional[pulumi.Input[RegionResizeRequestRequestedRunDurationArgs]]:
        
        ...
    
    @requested_run_duration.setter
    def requested_run_duration(self, value: Optional[pulumi.Input[RegionResizeRequestRequestedRunDurationArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionResizeRequestState:
    def __init__(__self__, *, creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., requested_run_duration: Optional[pulumi.Input[RegionResizeRequestRequestedRunDurationArgs]] = ..., resize_by: Optional[pulumi.Input[_builtins.int]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[RegionResizeRequestStatusArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManager")
    def instance_group_manager(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_group_manager.setter
    def instance_group_manager(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedRunDuration")
    def requested_run_duration(self) -> Optional[pulumi.Input[RegionResizeRequestRequestedRunDurationArgs]]:
        
        ...
    
    @requested_run_duration.setter
    def requested_run_duration(self, value: Optional[pulumi.Input[RegionResizeRequestRequestedRunDurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resizeBy")
    def resize_by(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @resize_by.setter
    def resize_by(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionResizeRequestStatusArgs]]]]:
        
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionResizeRequestStatusArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RegionResizeRequest(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., requested_run_duration: Optional[pulumi.Input[Union[RegionResizeRequestRequestedRunDurationArgs, RegionResizeRequestRequestedRunDurationArgsDict]]] = ..., resize_by: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegionResizeRequestArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., requested_run_duration: Optional[pulumi.Input[Union[RegionResizeRequestRequestedRunDurationArgs, RegionResizeRequestRequestedRunDurationArgsDict]]] = ..., resize_by: Optional[pulumi.Input[_builtins.int]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionResizeRequestStatusArgs, RegionResizeRequestStatusArgsDict]]]]] = ...) -> RegionResizeRequest:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManager")
    def instance_group_manager(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedRunDuration")
    def requested_run_duration(self) -> pulumi.Output[Optional[outputs.RegionResizeRequestRequestedRunDuration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resizeBy")
    def resize_by(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.RegionResizeRequestStatus]]:
        
        ...
    


