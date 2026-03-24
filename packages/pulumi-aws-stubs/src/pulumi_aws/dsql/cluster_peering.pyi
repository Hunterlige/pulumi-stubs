

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
__all__ = ['ClusterPeeringArgs', 'ClusterPeering']
@pulumi.input_type
class ClusterPeeringArgs:
    def __init__(__self__, *, clusters: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], identifier: pulumi.Input[_builtins.str], witness_region: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ClusterPeeringTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusters(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @clusters.setter
    def clusters(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identifier.setter
    def identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="witnessRegion")
    def witness_region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @witness_region.setter
    def witness_region(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[ClusterPeeringTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ClusterPeeringTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterPeeringState:
    def __init__(__self__, *, clusters: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ClusterPeeringTimeoutsArgs]] = ..., witness_region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @clusters.setter
    def clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[ClusterPeeringTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ClusterPeeringTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="witnessRegion")
    def witness_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @witness_region.setter
    def witness_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:dsql/clusterPeering:ClusterPeering")
class ClusterPeering(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., clusters: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ClusterPeeringTimeoutsArgs, ClusterPeeringTimeoutsArgsDict]]] = ..., witness_region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterPeeringArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., clusters: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ClusterPeeringTimeoutsArgs, ClusterPeeringTimeoutsArgsDict]]] = ..., witness_region: Optional[pulumi.Input[_builtins.str]] = ...) -> ClusterPeering:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusters(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ClusterPeeringTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="witnessRegion")
    def witness_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


