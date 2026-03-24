

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIotConnectorFhirDestinationResult', 'AwaitableGetIotConnectorFhirDestinationResult', 'get_iot_connector_fhir_destination', 'get_iot_connector_fhir_destination_output']
@pulumi.output_type
class GetIotConnectorFhirDestinationResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., fhir_mapping=..., fhir_service_resource_id=..., id=..., location=..., name=..., resource_identity_resolution_type=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fhirMapping")
    def fhir_mapping(self) -> outputs.IotMappingPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fhirServiceResourceId")
    def fhir_service_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdentityResolutionType")
    def resource_identity_resolution_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIotConnectorFhirDestinationResult(GetIotConnectorFhirDestinationResult):
    def __await__(self): # -> Generator[Never, Any, GetIotConnectorFhirDestinationResult]:
        ...
    


def get_iot_connector_fhir_destination(fhir_destination_name: Optional[_builtins.str] = ..., iot_connector_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIotConnectorFhirDestinationResult:
    
    ...

def get_iot_connector_fhir_destination_output(fhir_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., iot_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIotConnectorFhirDestinationResult]:
    
    ...

