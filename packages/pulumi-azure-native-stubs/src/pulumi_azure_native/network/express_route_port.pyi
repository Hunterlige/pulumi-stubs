

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExpressRoutePortArgs', 'ExpressRoutePort']
@pulumi.input_type
class ExpressRoutePortArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], bandwidth_in_gbps: Optional[pulumi.Input[_builtins.int]] = ..., billing_type: Optional[pulumi.Input[Union[_builtins.str, ExpressRoutePortsBillingType]]] = ..., encapsulation: Optional[pulumi.Input[Union[_builtins.str, ExpressRoutePortsEncapsulation]]] = ..., express_route_port_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., links: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteLinkArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., peering_location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthInGbps")
    def bandwidth_in_gbps(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bandwidth_in_gbps.setter
    def bandwidth_in_gbps(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ExpressRoutePortsBillingType]]]:
        
        ...
    
    @billing_type.setter
    def billing_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ExpressRoutePortsBillingType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encapsulation(self) -> Optional[pulumi.Input[Union[_builtins.str, ExpressRoutePortsEncapsulation]]]:
        
        ...
    
    @encapsulation.setter
    def encapsulation(self, value: Optional[pulumi.Input[Union[_builtins.str, ExpressRoutePortsEncapsulation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRoutePortName")
    def express_route_port_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @express_route_port_name.setter
    def express_route_port_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteLinkArgs]]]]:
        
        ...
    
    @links.setter
    def links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteLinkArgs]]]]): # -> None:
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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:ExpressRoutePort")
class ExpressRoutePort(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bandwidth_in_gbps: Optional[pulumi.Input[_builtins.int]] = ..., billing_type: Optional[pulumi.Input[Union[_builtins.str, ExpressRoutePortsBillingType]]] = ..., encapsulation: Optional[pulumi.Input[Union[_builtins.str, ExpressRoutePortsEncapsulation]]] = ..., express_route_port_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., links: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressRouteLinkArgs, ExpressRouteLinkArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., peering_location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExpressRoutePortArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ExpressRoutePort:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationDate")
    def allocation_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthInGbps")
    def bandwidth_in_gbps(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def circuits(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encapsulation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="etherType")
    def ether_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> pulumi.Output[Optional[Sequence[outputs.ExpressRouteLinkResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="provisionedBandwidthInGbps")
    def provisioned_bandwidth_in_gbps(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


