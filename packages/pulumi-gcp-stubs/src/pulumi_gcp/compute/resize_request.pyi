

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
__all__ = ['ResizeRequestArgs', 'ResizeRequest']
@pulumi.input_type
class ResizeRequestArgs:
    def __init__(__self__, *, instance_group_manager: pulumi.Input[_builtins.str], resize_by: pulumi.Input[_builtins.int], description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., requested_run_duration: Optional[pulumi.Input[ResizeRequestRequestedRunDurationArgs]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="requestedRunDuration")
    def requested_run_duration(self) -> Optional[pulumi.Input[ResizeRequestRequestedRunDurationArgs]]:
        
        ...
    
    @requested_run_duration.setter
    def requested_run_duration(self, value: Optional[pulumi.Input[ResizeRequestRequestedRunDurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ResizeRequestState:
    def __init__(__self__, *, creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., requested_run_duration: Optional[pulumi.Input[ResizeRequestRequestedRunDurationArgs]] = ..., resize_by: Optional[pulumi.Input[_builtins.int]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[ResizeRequestStatusArgs]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="requestedRunDuration")
    def requested_run_duration(self) -> Optional[pulumi.Input[ResizeRequestRequestedRunDurationArgs]]:
        
        ...
    
    @requested_run_duration.setter
    def requested_run_duration(self, value: Optional[pulumi.Input[ResizeRequestRequestedRunDurationArgs]]): # -> None:
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
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResizeRequestStatusArgs]]]]:
        
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResizeRequestStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/resizeRequest:ResizeRequest")
class ResizeRequest(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., requested_run_duration: Optional[pulumi.Input[Union[ResizeRequestRequestedRunDurationArgs, ResizeRequestRequestedRunDurationArgsDict]]] = ..., resize_by: Optional[pulumi.Input[_builtins.int]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResizeRequestArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., requested_run_duration: Optional[pulumi.Input[Union[ResizeRequestRequestedRunDurationArgs, ResizeRequestRequestedRunDurationArgsDict]]] = ..., resize_by: Optional[pulumi.Input[_builtins.int]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResizeRequestStatusArgs, ResizeRequestStatusArgsDict]]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> ResizeRequest:
        
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
    @pulumi.getter(name="requestedRunDuration")
    def requested_run_duration(self) -> pulumi.Output[Optional[outputs.ResizeRequestRequestedRunDuration]]:
        
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
    def statuses(self) -> pulumi.Output[Sequence[outputs.ResizeRequestStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


