

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFlowStreamConnectionStringResult', 'AwaitableGetFlowStreamConnectionStringResult', 'get_flow_stream_connection_string', 'get_flow_stream_connection_string_output']
@pulumi.output_type
class GetFlowStreamConnectionStringResult:
    
    def __init__(__self__, connection_string=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetFlowStreamConnectionStringResult(GetFlowStreamConnectionStringResult):
    def __await__(self): # -> Generator[Never, Any, GetFlowStreamConnectionStringResult]:
        ...
    


def get_flow_stream_connection_string(connection_name: Optional[_builtins.str] = ..., flow_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFlowStreamConnectionStringResult:
    
    ...

def get_flow_stream_connection_string_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., flow_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFlowStreamConnectionStringResult]:
    
    ...

