

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBookshelfPrivateEndpointConnectionResult', ..., 'get_bookshelf_private_endpoint_connection', 'get_bookshelf_private_endpoint_connection_output']
@pulumi.output_type
class GetBookshelfPrivateEndpointConnectionResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
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
    def properties(self) -> outputs.PrivateEndpointConnectionPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBookshelfPrivateEndpointConnectionResult(GetBookshelfPrivateEndpointConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetBookshelfPrivateEndpointConnectionResult]:
        ...
    


def get_bookshelf_private_endpoint_connection(bookshelf_name: Optional[_builtins.str] = ..., private_endpoint_connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBookshelfPrivateEndpointConnectionResult:
    
    ...

def get_bookshelf_private_endpoint_connection_output(bookshelf_name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBookshelfPrivateEndpointConnectionResult]:
    
    ...

