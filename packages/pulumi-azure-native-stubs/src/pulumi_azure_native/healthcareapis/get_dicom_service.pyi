

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDicomServiceResult', 'AwaitableGetDicomServiceResult', 'get_dicom_service', 'get_dicom_service_output']
@pulumi.output_type
class GetDicomServiceResult:
    
    def __init__(__self__, authentication_configuration=..., azure_api_version=..., cors_configuration=..., enable_data_partitions=..., encryption=..., etag=..., event_state=..., id=..., identity=..., location=..., name=..., private_endpoint_connections=..., provisioning_state=..., public_network_access=..., service_url=..., storage_configuration=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional[outputs.DicomServiceAuthenticationConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional[outputs.CorsConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataPartitions")
    def enable_data_partitions(self) -> Optional[_builtins.bool]:
        
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
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ServiceManagedIdentityResponseIdentity]:
        
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
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> Optional[outputs.StorageConfigurationResponse]:
        
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
    


class AwaitableGetDicomServiceResult(GetDicomServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetDicomServiceResult]:
        ...
    


def get_dicom_service(dicom_service_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDicomServiceResult:
    
    ...

def get_dicom_service_output(dicom_service_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDicomServiceResult]:
    
    ...

