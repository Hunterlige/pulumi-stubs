

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectedEnvironmentsCertificateResult', 'AwaitableGetConnectedEnvironmentsCertificateResult', 'get_connected_environments_certificate', 'get_connected_environments_certificate_output']
@pulumi.output_type
class GetConnectedEnvironmentsCertificateResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
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
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.CertificateResponseProperties:
        
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
    


class AwaitableGetConnectedEnvironmentsCertificateResult(GetConnectedEnvironmentsCertificateResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectedEnvironmentsCertificateResult]:
        ...
    


def get_connected_environments_certificate(certificate_name: Optional[_builtins.str] = ..., connected_environment_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectedEnvironmentsCertificateResult:
    
    ...

def get_connected_environments_certificate_output(certificate_name: Optional[pulumi.Input[_builtins.str]] = ..., connected_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectedEnvironmentsCertificateResult]:
    
    ...

