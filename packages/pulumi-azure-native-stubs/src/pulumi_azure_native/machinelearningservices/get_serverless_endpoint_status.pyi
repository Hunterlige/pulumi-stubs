

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerlessEndpointStatusResult', 'AwaitableGetServerlessEndpointStatusResult', 'get_serverless_endpoint_status', 'get_serverless_endpoint_status_output']
@pulumi.output_type
class GetServerlessEndpointStatusResult:
    def __init__(__self__, metrics=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetServerlessEndpointStatusResult(GetServerlessEndpointStatusResult):
    def __await__(self): # -> Generator[Never, Any, GetServerlessEndpointStatusResult]:
        ...
    


def get_serverless_endpoint_status(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerlessEndpointStatusResult:
    
    ...

def get_serverless_endpoint_status_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerlessEndpointStatusResult]:
    
    ...

