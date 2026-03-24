

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
__all__ = ['ExpressRouteGatewayArgs', 'ExpressRouteGateway']
@pulumi.input_type
class ExpressRouteGatewayArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], virtual_hub: pulumi.Input[VirtualHubIdArgs], allow_non_virtual_wan_traffic: Optional[pulumi.Input[_builtins.bool]] = ..., auto_scale_configuration: Optional[pulumi.Input[ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs]] = ..., express_route_connections: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteConnectionArgs]]]] = ..., express_route_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Input[VirtualHubIdArgs]:
        
        ...
    
    @virtual_hub.setter
    def virtual_hub(self, value: pulumi.Input[VirtualHubIdArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowNonVirtualWanTraffic")
    def allow_non_virtual_wan_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_non_virtual_wan_traffic.setter
    def allow_non_virtual_wan_traffic(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScaleConfiguration")
    def auto_scale_configuration(self) -> Optional[pulumi.Input[ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs]]:
        
        ...
    
    @auto_scale_configuration.setter
    def auto_scale_configuration(self, value: Optional[pulumi.Input[ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteConnections")
    def express_route_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteConnectionArgs]]]]:
        
        ...
    
    @express_route_connections.setter
    def express_route_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteGatewayName")
    def express_route_gateway_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @express_route_gateway_name.setter
    def express_route_gateway_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("azure-native:network:ExpressRouteGateway")
class ExpressRouteGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_non_virtual_wan_traffic: Optional[pulumi.Input[_builtins.bool]] = ..., auto_scale_configuration: Optional[pulumi.Input[Union[ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs, ExpressRouteGatewayPropertiesAutoScaleConfigurationArgsDict]]] = ..., express_route_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressRouteConnectionArgs, ExpressRouteConnectionArgsDict]]]]] = ..., express_route_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_hub: Optional[pulumi.Input[Union[VirtualHubIdArgs, VirtualHubIdArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExpressRouteGatewayArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ExpressRouteGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowNonVirtualWanTraffic")
    def allow_non_virtual_wan_traffic(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScaleConfiguration")
    def auto_scale_configuration(self) -> pulumi.Output[Optional[outputs.ExpressRouteGatewayPropertiesResponseAutoScaleConfiguration]]:
        
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
    @pulumi.getter(name="expressRouteConnections")
    def express_route_connections(self) -> pulumi.Output[Optional[Sequence[outputs.ExpressRouteConnectionResponse]]]:
        
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
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[outputs.VirtualHubIdResponse]:
        
        ...
    


