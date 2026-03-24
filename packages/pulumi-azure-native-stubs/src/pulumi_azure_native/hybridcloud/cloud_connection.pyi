

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CloudConnectionArgs', 'CloudConnection']
@pulumi.input_type
class CloudConnectionArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], cloud_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., cloud_connector: Optional[pulumi.Input[ResourceReferenceArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., remote_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., shared_key: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_hub: Optional[pulumi.Input[ResourceReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudConnectionName")
    def cloud_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_connection_name.setter
    def cloud_connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudConnector")
    def cloud_connector(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @cloud_connector.setter
    def cloud_connector(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteResourceId")
    def remote_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remote_resource_id.setter
    def remote_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_key.setter
    def shared_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @virtual_hub.setter
    def virtual_hub(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:hybridcloud:CloudConnection")
class CloudConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloud_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., cloud_connector: Optional[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., remote_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., shared_key: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_hub: Optional[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CloudConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> CloudConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudConnector")
    def cloud_connector(self) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteResourceId")
    def remote_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
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
    def virtual_hub(self) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]:
        
        ...
    


