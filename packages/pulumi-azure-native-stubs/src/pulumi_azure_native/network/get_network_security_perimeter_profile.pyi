

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkSecurityPerimeterProfileResult', 'AwaitableGetNetworkSecurityPerimeterProfileResult', 'get_network_security_perimeter_profile', 'get_network_security_perimeter_profile_output']
@pulumi.output_type
class GetNetworkSecurityPerimeterProfileResult:
    
    def __init__(__self__, access_rules_version=..., azure_api_version=..., diagnostic_settings_version=..., id=..., location=..., name=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRulesVersion")
    def access_rules_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticSettingsVersion")
    def diagnostic_settings_version(self) -> _builtins.str:
        
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
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNetworkSecurityPerimeterProfileResult(GetNetworkSecurityPerimeterProfileResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkSecurityPerimeterProfileResult]:
        ...
    


def get_network_security_perimeter_profile(network_security_perimeter_name: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkSecurityPerimeterProfileResult:
    
    ...

def get_network_security_perimeter_profile_output(network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkSecurityPerimeterProfileResult]:
    
    ...

