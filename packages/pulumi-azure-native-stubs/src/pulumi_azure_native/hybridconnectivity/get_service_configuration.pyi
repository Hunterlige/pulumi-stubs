

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServiceConfigurationResult', 'AwaitableGetServiceConfigurationResult', 'get_service_configuration', 'get_service_configuration_output']
@pulumi.output_type
class GetServiceConfigurationResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., port=..., provisioning_state=..., resource_id=..., service_name=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    @pulumi.getter
    def port(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServiceConfigurationResult(GetServiceConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetServiceConfigurationResult]:
        ...
    


def get_service_configuration(endpoint_name: Optional[_builtins.str] = ..., resource_uri: Optional[_builtins.str] = ..., service_configuration_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServiceConfigurationResult:
    
    ...

def get_service_configuration_output(endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., service_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServiceConfigurationResult]:
    
    ...

