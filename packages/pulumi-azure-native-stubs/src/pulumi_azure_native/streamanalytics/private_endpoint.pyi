

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
__all__ = ['PrivateEndpointArgs', 'PrivateEndpoint']
@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], manual_private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]] = ..., private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]]:
        
        ...
    
    @manual_private_link_service_connections.setter
    def manual_private_link_service_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_endpoint_name.setter
    def private_endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:streamanalytics:PrivateEndpoint")
class PrivateEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., manual_private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PrivateLinkServiceConnectionArgs, PrivateLinkServiceConnectionArgsDict]]]]] = ..., private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrivateEndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> PrivateEndpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> pulumi.Output[Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


