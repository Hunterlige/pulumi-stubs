

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagementServerResult', 'AwaitableGetManagementServerResult', 'get_management_server', 'get_management_server_output']
@pulumi.output_type
class GetManagementServerResult:
    
    def __init__(__self__, id=..., location=..., management_uris=..., name=..., networks=..., oauth2_client_id=..., project=..., type=...) -> None:
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
    @pulumi.getter(name="managementUris")
    def management_uris(self) -> Sequence[outputs.GetManagementServerManagementUriResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Sequence[outputs.GetManagementServerNetworkResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2ClientId")
    def oauth2_client_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


class AwaitableGetManagementServerResult(GetManagementServerResult):
    def __await__(self): # -> Generator[Never, Any, GetManagementServerResult]:
        ...
    


def get_management_server(location: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagementServerResult:
    
    ...

def get_management_server_output(location: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagementServerResult]:
    
    ...

