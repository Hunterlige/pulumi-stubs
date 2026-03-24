

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
__all__ = ['IotConnectorArgs', 'IotConnector']
@pulumi.input_type
class IotConnectorArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], device_mapping: Optional[pulumi.Input[IotMappingPropertiesArgs]] = ..., identity: Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]] = ..., ingestion_endpoint_configuration: Optional[pulumi.Input[IotEventHubIngestionEndpointConfigurationArgs]] = ..., iot_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceMapping")
    def device_mapping(self) -> Optional[pulumi.Input[IotMappingPropertiesArgs]]:
        
        ...
    
    @device_mapping.setter
    def device_mapping(self, value: Optional[pulumi.Input[IotMappingPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ServiceManagedIdentityIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionEndpointConfiguration")
    def ingestion_endpoint_configuration(self) -> Optional[pulumi.Input[IotEventHubIngestionEndpointConfigurationArgs]]:
        
        ...
    
    @ingestion_endpoint_configuration.setter
    def ingestion_endpoint_configuration(self, value: Optional[pulumi.Input[IotEventHubIngestionEndpointConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotConnectorName")
    def iot_connector_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iot_connector_name.setter
    def iot_connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("azure-native:healthcareapis:IotConnector")
class IotConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., device_mapping: Optional[pulumi.Input[Union[IotMappingPropertiesArgs, IotMappingPropertiesArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[ServiceManagedIdentityIdentityArgs, ServiceManagedIdentityIdentityArgsDict]]] = ..., ingestion_endpoint_configuration: Optional[pulumi.Input[Union[IotEventHubIngestionEndpointConfigurationArgs, IotEventHubIngestionEndpointConfigurationArgsDict]]] = ..., iot_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IotConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> IotConnector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceMapping")
    def device_mapping(self) -> pulumi.Output[Optional[outputs.IotMappingPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ServiceManagedIdentityResponseIdentity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionEndpointConfiguration")
    def ingestion_endpoint_configuration(self) -> pulumi.Output[Optional[outputs.IotEventHubIngestionEndpointConfigurationResponse]]:
        
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
    


