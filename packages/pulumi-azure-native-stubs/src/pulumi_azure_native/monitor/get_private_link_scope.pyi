

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrivateLinkScopeResult', 'AwaitableGetPrivateLinkScopeResult', 'get_private_link_scope', 'get_private_link_scope_output']
@pulumi.output_type
class GetPrivateLinkScopeResult:
    
    def __init__(__self__, access_mode_settings=..., azure_api_version=..., id=..., location=..., name=..., private_endpoint_connections=..., provisioning_state=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessModeSettings")
    def access_mode_settings(self) -> outputs.AccessModeSettingsResponse:
        
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
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
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
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPrivateLinkScopeResult(GetPrivateLinkScopeResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateLinkScopeResult]:
        ...
    


def get_private_link_scope(resource_group_name: Optional[_builtins.str] = ..., scope_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateLinkScopeResult:
    
    ...

def get_private_link_scope_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scope_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateLinkScopeResult]:
    
    ...

