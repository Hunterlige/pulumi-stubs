

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
__all__ = ['ListenerArgs', 'Listener']
@pulumi.input_type
class ListenerArgs:
    def __init__(__self__, *, accelerator_arn: pulumi.Input[_builtins.str], port_ranges: pulumi.Input[Sequence[pulumi.Input[ListenerPortRangeArgs]]], protocol: pulumi.Input[_builtins.str], client_affinity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @accelerator_arn.setter
    def accelerator_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> pulumi.Input[Sequence[pulumi.Input[ListenerPortRangeArgs]]]:
        
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: pulumi.Input[Sequence[pulumi.Input[ListenerPortRangeArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAffinity")
    def client_affinity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_affinity.setter
    def client_affinity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ListenerState:
    def __init__(__self__, *, accelerator_arn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., client_affinity: Optional[pulumi.Input[_builtins.str]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerPortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accelerator_arn.setter
    def accelerator_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAffinity")
    def client_affinity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_affinity.setter
    def client_affinity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerPortRangeArgs]]]]:
        
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:globalaccelerator/listener:Listener")
class Listener(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accelerator_arn: Optional[pulumi.Input[_builtins.str]] = ..., client_affinity: Optional[pulumi.Input[_builtins.str]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListenerPortRangeArgs, ListenerPortRangeArgsDict]]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ListenerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accelerator_arn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., client_affinity: Optional[pulumi.Input[_builtins.str]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListenerPortRangeArgs, ListenerPortRangeArgsDict]]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ...) -> Listener:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAffinity")
    def client_affinity(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> pulumi.Output[Sequence[outputs.ListenerPortRange]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


