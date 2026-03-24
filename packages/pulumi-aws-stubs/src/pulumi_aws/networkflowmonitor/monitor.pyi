

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MonitorArgs', 'Monitor']
@pulumi.input_type
class MonitorArgs:
    def __init__(__self__, *, local_resources: pulumi.Input[Sequence[pulumi.Input[MonitorLocalResourceArgs]]], monitor_name: pulumi.Input[_builtins.str], scope_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., remote_resources: Optional[pulumi.Input[Sequence[pulumi.Input[MonitorRemoteResourceArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[MonitorTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localResources")
    def local_resources(self) -> pulumi.Input[Sequence[pulumi.Input[MonitorLocalResourceArgs]]]:
        
        ...
    
    @local_resources.setter
    def local_resources(self, value: pulumi.Input[Sequence[pulumi.Input[MonitorLocalResourceArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @monitor_name.setter
    def monitor_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeArn")
    def scope_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope_arn.setter
    def scope_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteResources")
    def remote_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MonitorRemoteResourceArgs]]]]:
        
        ...
    
    @remote_resources.setter
    def remote_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MonitorRemoteResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[MonitorTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[MonitorTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _MonitorState:
    def __init__(__self__, *, local_resources: Optional[pulumi.Input[Sequence[pulumi.Input[MonitorLocalResourceArgs]]]] = ..., monitor_arn: Optional[pulumi.Input[_builtins.str]] = ..., monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_resources: Optional[pulumi.Input[Sequence[pulumi.Input[MonitorRemoteResourceArgs]]]] = ..., scope_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[MonitorTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localResources")
    def local_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MonitorLocalResourceArgs]]]]:
        
        ...
    
    @local_resources.setter
    def local_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MonitorLocalResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorArn")
    def monitor_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monitor_arn.setter
    def monitor_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monitor_name.setter
    def monitor_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteResources")
    def remote_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MonitorRemoteResourceArgs]]]]:
        
        ...
    
    @remote_resources.setter
    def remote_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MonitorRemoteResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeArn")
    def scope_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope_arn.setter
    def scope_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[MonitorTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[MonitorTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:networkflowmonitor/monitor:Monitor")
class Monitor(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., local_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MonitorLocalResourceArgs, MonitorLocalResourceArgsDict]]]]] = ..., monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MonitorRemoteResourceArgs, MonitorRemoteResourceArgsDict]]]]] = ..., scope_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[MonitorTimeoutsArgs, MonitorTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MonitorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., local_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MonitorLocalResourceArgs, MonitorLocalResourceArgsDict]]]]] = ..., monitor_arn: Optional[pulumi.Input[_builtins.str]] = ..., monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MonitorRemoteResourceArgs, MonitorRemoteResourceArgsDict]]]]] = ..., scope_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[MonitorTimeoutsArgs, MonitorTimeoutsArgsDict]]] = ...) -> Monitor:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localResources")
    def local_resources(self) -> pulumi.Output[Sequence[outputs.MonitorLocalResource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorArn")
    def monitor_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteResources")
    def remote_resources(self) -> pulumi.Output[Optional[Sequence[outputs.MonitorRemoteResource]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeArn")
    def scope_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.MonitorTimeouts]]:
        ...
    


