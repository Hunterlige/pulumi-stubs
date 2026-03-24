

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFlowDestinationEndpointsResult', 'AwaitableGetFlowDestinationEndpointsResult', 'get_flow_destination_endpoints', 'get_flow_destination_endpoints_output']
@pulumi.output_type
class GetFlowDestinationEndpointsResult:
    
    def __init__(__self__, endpoints=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetFlowDestinationEndpointsResult(GetFlowDestinationEndpointsResult):
    def __await__(self): # -> Generator[Never, Any, GetFlowDestinationEndpointsResult]:
        ...
    


def get_flow_destination_endpoints(connection_name: Optional[_builtins.str] = ..., flow_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFlowDestinationEndpointsResult:
    
    ...

def get_flow_destination_endpoints_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., flow_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFlowDestinationEndpointsResult]:
    
    ...

