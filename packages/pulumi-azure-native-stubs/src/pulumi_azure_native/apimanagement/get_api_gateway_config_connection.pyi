

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApiGatewayConfigConnectionResult', 'AwaitableGetApiGatewayConfigConnectionResult', 'get_api_gateway_config_connection', 'get_api_gateway_config_connection_output']
@pulumi.output_type
class GetApiGatewayConfigConnectionResult:
    
    def __init__(__self__, azure_api_version=..., default_hostname=..., etag=..., hostnames=..., id=..., name=..., provisioning_state=..., source_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostnames(self) -> Optional[Sequence[_builtins.str]]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetApiGatewayConfigConnectionResult(GetApiGatewayConfigConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetApiGatewayConfigConnectionResult]:
        ...
    


def get_api_gateway_config_connection(config_connection_name: Optional[_builtins.str] = ..., gateway_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApiGatewayConfigConnectionResult:
    
    ...

def get_api_gateway_config_connection_output(config_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApiGatewayConfigConnectionResult]:
    
    ...

