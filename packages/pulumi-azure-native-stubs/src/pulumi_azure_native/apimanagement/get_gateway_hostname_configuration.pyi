

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGatewayHostnameConfigurationResult', 'AwaitableGetGatewayHostnameConfigurationResult', 'get_gateway_hostname_configuration', 'get_gateway_hostname_configuration_output']
@pulumi.output_type
class GetGatewayHostnameConfigurationResult:
    
    def __init__(__self__, azure_api_version=..., certificate_id=..., hostname=..., http2_enabled=..., id=..., name=..., negotiate_client_certificate=..., tls10_enabled=..., tls11_enabled=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="http2Enabled")
    def http2_enabled(self) -> Optional[_builtins.bool]:
        
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
    @pulumi.getter(name="negotiateClientCertificate")
    def negotiate_client_certificate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tls10Enabled")
    def tls10_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tls11Enabled")
    def tls11_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetGatewayHostnameConfigurationResult(GetGatewayHostnameConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetGatewayHostnameConfigurationResult]:
        ...
    


def get_gateway_hostname_configuration(gateway_id: Optional[_builtins.str] = ..., hc_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGatewayHostnameConfigurationResult:
    
    ...

def get_gateway_hostname_configuration_output(gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., hc_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGatewayHostnameConfigurationResult]:
    
    ...

