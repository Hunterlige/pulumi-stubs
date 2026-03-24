

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetNetworkSecurityPerimeterLoggingConfigurationResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., properties=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
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
    def properties(self) -> outputs.NspLoggingConfigurationPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNetworkSecurityPerimeterLoggingConfigurationResult(GetNetworkSecurityPerimeterLoggingConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkSecurityPerimeterLoggingConfigurationResult]:
        ...
    


def get_network_security_perimeter_logging_configuration(logging_configuration_name: Optional[_builtins.str] = ..., network_security_perimeter_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkSecurityPerimeterLoggingConfigurationResult:
    
    ...

def get_network_security_perimeter_logging_configuration_output(logging_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkSecurityPerimeterLoggingConfigurationResult]:
    
    ...

