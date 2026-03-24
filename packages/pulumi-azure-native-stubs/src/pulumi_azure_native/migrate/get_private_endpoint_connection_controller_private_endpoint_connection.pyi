

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
class GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult:
    
    def __init__(__self__, azure_api_version=..., e_tag=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str:
        
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
    


class AwaitableGetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult(GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult]:
        ...
    


def get_private_endpoint_connection_controller_private_endpoint_connection(migrate_project_name: Optional[_builtins.str] = ..., pe_connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult:
    
    ...

def get_private_endpoint_connection_controller_private_endpoint_connection_output(migrate_project_name: Optional[pulumi.Input[_builtins.str]] = ..., pe_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult]:
    
    ...

