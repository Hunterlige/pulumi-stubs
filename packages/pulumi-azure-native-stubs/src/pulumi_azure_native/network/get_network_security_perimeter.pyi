

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkSecurityPerimeterResult', 'AwaitableGetNetworkSecurityPerimeterResult', 'get_network_security_perimeter', 'get_network_security_perimeter_output']
@pulumi.output_type
class GetNetworkSecurityPerimeterResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., perimeter_guid=..., provisioning_state=..., tags=..., type=...) -> None:
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
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perimeterGuid")
    def perimeter_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNetworkSecurityPerimeterResult(GetNetworkSecurityPerimeterResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkSecurityPerimeterResult]:
        ...
    


def get_network_security_perimeter(network_security_perimeter_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkSecurityPerimeterResult:
    
    ...

def get_network_security_perimeter_output(network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkSecurityPerimeterResult]:
    
    ...

