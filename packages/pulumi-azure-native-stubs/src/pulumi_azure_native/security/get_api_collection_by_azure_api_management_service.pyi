

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAPICollectionByAzureApiManagementServiceResult', ..., 'get_api_collection_by_azure_api_management_service', ...]
@pulumi.output_type
class GetAPICollectionByAzureApiManagementServiceResult:
    
    def __init__(__self__, azure_api_version=..., base_url=..., discovered_via=..., display_name=..., id=..., name=..., number_of_api_endpoints=..., number_of_api_endpoints_with_sensitive_data_exposed=..., number_of_external_api_endpoints=..., number_of_inactive_api_endpoints=..., number_of_unauthenticated_api_endpoints=..., provisioning_state=..., sensitivity_label=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredVia")
    def discovered_via(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfApiEndpoints")
    def number_of_api_endpoints(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfApiEndpointsWithSensitiveDataExposed")
    def number_of_api_endpoints_with_sensitive_data_exposed(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfExternalApiEndpoints")
    def number_of_external_api_endpoints(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfInactiveApiEndpoints")
    def number_of_inactive_api_endpoints(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfUnauthenticatedApiEndpoints")
    def number_of_unauthenticated_api_endpoints(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityLabel")
    def sensitivity_label(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAPICollectionByAzureApiManagementServiceResult(GetAPICollectionByAzureApiManagementServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetAPICollectionByAzureApiManagementServiceResult]:
        ...
    


def get_api_collection_by_azure_api_management_service(api_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAPICollectionByAzureApiManagementServiceResult:
    
    ...

def get_api_collection_by_azure_api_management_service_output(api_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAPICollectionByAzureApiManagementServiceResult]:
    
    ...

