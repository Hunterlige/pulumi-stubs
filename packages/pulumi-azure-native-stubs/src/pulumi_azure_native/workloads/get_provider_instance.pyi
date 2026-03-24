

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProviderInstanceResult', 'AwaitableGetProviderInstanceResult', 'get_provider_instance', 'get_provider_instance_output']
@pulumi.output_type
class GetProviderInstanceResult:
    
    def __init__(__self__, azure_api_version=..., errors=..., health=..., id=..., name=..., provider_settings=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.ErrorDetailResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> outputs.HealthResponse:
        
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
    @pulumi.getter(name="providerSettings")
    def provider_settings(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetProviderInstanceResult(GetProviderInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetProviderInstanceResult]:
        ...
    


def get_provider_instance(monitor_name: Optional[_builtins.str] = ..., provider_instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProviderInstanceResult:
    
    ...

def get_provider_instance_output(monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., provider_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProviderInstanceResult]:
    
    ...

