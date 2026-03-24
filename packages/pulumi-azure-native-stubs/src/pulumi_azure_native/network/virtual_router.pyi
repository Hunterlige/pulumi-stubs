

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
__all__ = ['VirtualRouterArgs', 'VirtualRouter']
@pulumi.input_type
class VirtualRouterArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], hosted_gateway: Optional[pulumi.Input[SubResourceArgs]] = ..., hosted_subnet: Optional[pulumi.Input[SubResourceArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_router_asn: Optional[pulumi.Input[_builtins.float]] = ..., virtual_router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., virtual_router_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedGateway")
    def hosted_gateway(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @hosted_gateway.setter
    def hosted_gateway(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedSubnet")
    def hosted_subnet(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @hosted_subnet.setter
    def hosted_subnet(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @virtual_router_asn.setter
    def virtual_router_asn(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @virtual_router_ips.setter
    def virtual_router_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_router_name.setter
    def virtual_router_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:VirtualRouter")
class VirtualRouter(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., hosted_gateway: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., hosted_subnet: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_router_asn: Optional[pulumi.Input[_builtins.float]] = ..., virtual_router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., virtual_router_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VirtualRouterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VirtualRouter:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedGateway")
    def hosted_gateway(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedSubnet")
    def hosted_subnet(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def peerings(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


