

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
__all__ = ['InstancePublicPortsArgs', 'InstancePublicPorts']
@pulumi.input_type
class InstancePublicPortsArgs:
    def __init__(__self__, *, instance_name: pulumi.Input[_builtins.str], port_infos: pulumi.Input[Sequence[pulumi.Input[InstancePublicPortsPortInfoArgs]]], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_name.setter
    def instance_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portInfos")
    def port_infos(self) -> pulumi.Input[Sequence[pulumi.Input[InstancePublicPortsPortInfoArgs]]]:
        
        ...
    
    @port_infos.setter
    def port_infos(self, value: pulumi.Input[Sequence[pulumi.Input[InstancePublicPortsPortInfoArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstancePublicPortsState:
    def __init__(__self__, *, instance_name: Optional[pulumi.Input[_builtins.str]] = ..., port_infos: Optional[pulumi.Input[Sequence[pulumi.Input[InstancePublicPortsPortInfoArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portInfos")
    def port_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstancePublicPortsPortInfoArgs]]]]:
        
        ...
    
    @port_infos.setter
    def port_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstancePublicPortsPortInfoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InstancePublicPorts(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., port_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstancePublicPortsPortInfoArgs, InstancePublicPortsPortInfoArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstancePublicPortsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., port_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstancePublicPortsPortInfoArgs, InstancePublicPortsPortInfoArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> InstancePublicPorts:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portInfos")
    def port_infos(self) -> pulumi.Output[Sequence[outputs.InstancePublicPortsPortInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


