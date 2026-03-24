

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
__all__ = ['PeeringConnectionOptionsArgs', 'PeeringConnectionOptions']
@pulumi.input_type
class PeeringConnectionOptionsArgs:
    def __init__(__self__, *, vpc_peering_connection_id: pulumi.Input[_builtins.str], accepter: Optional[pulumi.Input[PeeringConnectionOptionsAccepterArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., requester: Optional[pulumi.Input[PeeringConnectionOptionsRequesterArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accepter(self) -> Optional[pulumi.Input[PeeringConnectionOptionsAccepterArgs]]:
        
        ...
    
    @accepter.setter
    def accepter(self, value: Optional[pulumi.Input[PeeringConnectionOptionsAccepterArgs]]): # -> None:
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
    def requester(self) -> Optional[pulumi.Input[PeeringConnectionOptionsRequesterArgs]]:
        
        ...
    
    @requester.setter
    def requester(self, value: Optional[pulumi.Input[PeeringConnectionOptionsRequesterArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _PeeringConnectionOptionsState:
    def __init__(__self__, *, accepter: Optional[pulumi.Input[PeeringConnectionOptionsAccepterArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., requester: Optional[pulumi.Input[PeeringConnectionOptionsRequesterArgs]] = ..., vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accepter(self) -> Optional[pulumi.Input[PeeringConnectionOptionsAccepterArgs]]:
        
        ...
    
    @accepter.setter
    def accepter(self, value: Optional[pulumi.Input[PeeringConnectionOptionsAccepterArgs]]): # -> None:
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
    def requester(self) -> Optional[pulumi.Input[PeeringConnectionOptionsRequesterArgs]]:
        
        ...
    
    @requester.setter
    def requester(self, value: Optional[pulumi.Input[PeeringConnectionOptionsRequesterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class PeeringConnectionOptions(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accepter: Optional[pulumi.Input[Union[PeeringConnectionOptionsAccepterArgs, PeeringConnectionOptionsAccepterArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., requester: Optional[pulumi.Input[Union[PeeringConnectionOptionsRequesterArgs, PeeringConnectionOptionsRequesterArgsDict]]] = ..., vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PeeringConnectionOptionsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accepter: Optional[pulumi.Input[Union[PeeringConnectionOptionsAccepterArgs, PeeringConnectionOptionsAccepterArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., requester: Optional[pulumi.Input[Union[PeeringConnectionOptionsRequesterArgs, PeeringConnectionOptionsRequesterArgsDict]]] = ..., vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> PeeringConnectionOptions:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accepter(self) -> pulumi.Output[outputs.PeeringConnectionOptionsAccepter]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requester(self) -> pulumi.Output[outputs.PeeringConnectionOptionsRequester]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


