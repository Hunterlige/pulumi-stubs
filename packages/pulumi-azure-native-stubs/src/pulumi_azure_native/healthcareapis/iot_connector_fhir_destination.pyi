

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IotConnectorFhirDestinationArgs', 'IotConnectorFhirDestination']
@pulumi.input_type
class IotConnectorFhirDestinationArgs:
    def __init__(__self__, *, fhir_mapping: pulumi.Input[IotMappingPropertiesArgs], fhir_service_resource_id: pulumi.Input[_builtins.str], iot_connector_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], resource_identity_resolution_type: pulumi.Input[Union[_builtins.str, IotIdentityResolutionType]], workspace_name: pulumi.Input[_builtins.str], fhir_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fhirMapping")
    def fhir_mapping(self) -> pulumi.Input[IotMappingPropertiesArgs]:
        
        ...
    
    @fhir_mapping.setter
    def fhir_mapping(self, value: pulumi.Input[IotMappingPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fhirServiceResourceId")
    def fhir_service_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fhir_service_resource_id.setter
    def fhir_service_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotConnectorName")
    def iot_connector_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @iot_connector_name.setter
    def iot_connector_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdentityResolutionType")
    def resource_identity_resolution_type(self) -> pulumi.Input[Union[_builtins.str, IotIdentityResolutionType]]:
        
        ...
    
    @resource_identity_resolution_type.setter
    def resource_identity_resolution_type(self, value: pulumi.Input[Union[_builtins.str, IotIdentityResolutionType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fhirDestinationName")
    def fhir_destination_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fhir_destination_name.setter
    def fhir_destination_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class IotConnectorFhirDestination(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., fhir_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., fhir_mapping: Optional[pulumi.Input[Union[IotMappingPropertiesArgs, IotMappingPropertiesArgsDict]]] = ..., fhir_service_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., iot_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_identity_resolution_type: Optional[pulumi.Input[Union[_builtins.str, IotIdentityResolutionType]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IotConnectorFhirDestinationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> IotConnectorFhirDestination:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fhirMapping")
    def fhir_mapping(self) -> pulumi.Output[outputs.IotMappingPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fhirServiceResourceId")
    def fhir_service_resource_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="resourceIdentityResolutionType")
    def resource_identity_resolution_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


