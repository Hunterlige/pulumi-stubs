

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
__all__ = ['PeeringArgs', 'Peering']
@pulumi.input_type
class PeeringArgs:
    def __init__(__self__, *, kind: pulumi.Input[Union[_builtins.str, Kind]], resource_group_name: pulumi.Input[_builtins.str], sku: pulumi.Input[PeeringSkuArgs], direct: Optional[pulumi.Input[PeeringPropertiesDirectArgs]] = ..., exchange: Optional[pulumi.Input[PeeringPropertiesExchangeArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., peering_location: Optional[pulumi.Input[_builtins.str]] = ..., peering_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[_builtins.str, Kind]]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[Union[_builtins.str, Kind]]): # -> None:
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
    def sku(self) -> pulumi.Input[PeeringSkuArgs]:
        
        ...
    
    @sku.setter
    def sku(self, value: pulumi.Input[PeeringSkuArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direct(self) -> Optional[pulumi.Input[PeeringPropertiesDirectArgs]]:
        
        ...
    
    @direct.setter
    def direct(self, value: Optional[pulumi.Input[PeeringPropertiesDirectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exchange(self) -> Optional[pulumi.Input[PeeringPropertiesExchangeArgs]]:
        
        ...
    
    @exchange.setter
    def exchange(self, value: Optional[pulumi.Input[PeeringPropertiesExchangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringLocation")
    def peering_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peering_location.setter
    def peering_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peering_name.setter
    def peering_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:peering:Peering")
class Peering(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., direct: Optional[pulumi.Input[Union[PeeringPropertiesDirectArgs, PeeringPropertiesDirectArgsDict]]] = ..., exchange: Optional[pulumi.Input[Union[PeeringPropertiesExchangeArgs, PeeringPropertiesExchangeArgsDict]]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., peering_location: Optional[pulumi.Input[_builtins.str]] = ..., peering_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[PeeringSkuArgs, PeeringSkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PeeringArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Peering:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direct(self) -> pulumi.Output[Optional[outputs.PeeringPropertiesDirectResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exchange(self) -> pulumi.Output[Optional[outputs.PeeringPropertiesExchangeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringLocation")
    def peering_location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.PeeringSkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


