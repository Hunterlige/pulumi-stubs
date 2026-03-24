

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFhirServiceResult', 'AwaitableGetFhirServiceResult', 'get_fhir_service', 'get_fhir_service_output']
@pulumi.output_type
class GetFhirServiceResult:
    
    def __init__(__self__, acr_configuration=..., authentication_configuration=..., azure_api_version=..., cors_configuration=..., encryption=..., etag=..., event_state=..., export_configuration=..., id=..., identity=..., implementation_guides_configuration=..., import_configuration=..., kind=..., location=..., name=..., private_endpoint_connections=..., provisioning_state=..., public_network_access=..., resource_version_policy_configuration=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acrConfiguration")
    def acr_configuration(self) -> Optional[outputs.FhirServiceAcrConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional[outputs.FhirServiceAuthenticationConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional[outputs.FhirServiceCorsConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventState")
    def event_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(self) -> Optional[outputs.FhirServiceExportConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ServiceManagedIdentityResponseIdentity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="implementationGuidesConfiguration")
    def implementation_guides_configuration(self) -> Optional[outputs.ImplementationGuidesConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importConfiguration")
    def import_configuration(self) -> Optional[outputs.FhirServiceImportConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceVersionPolicyConfiguration")
    def resource_version_policy_configuration(self) -> Optional[outputs.ResourceVersionPolicyConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFhirServiceResult(GetFhirServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetFhirServiceResult]:
        ...
    


def get_fhir_service(fhir_service_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFhirServiceResult:
    
    ...

def get_fhir_service_output(fhir_service_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFhirServiceResult]:
    
    ...

