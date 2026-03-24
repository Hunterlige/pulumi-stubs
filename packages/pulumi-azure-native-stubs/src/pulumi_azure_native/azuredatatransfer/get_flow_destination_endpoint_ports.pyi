

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFlowDestinationEndpointPortsResult', 'AwaitableGetFlowDestinationEndpointPortsResult', 'get_flow_destination_endpoint_ports', 'get_flow_destination_endpoint_ports_output']
@pulumi.output_type
class GetFlowDestinationEndpointPortsResult:
    
    def __init__(__self__, ports=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[_builtins.float]]:
        
        ...
    


class AwaitableGetFlowDestinationEndpointPortsResult(GetFlowDestinationEndpointPortsResult):
    def __await__(self): # -> Generator[Never, Any, GetFlowDestinationEndpointPortsResult]:
        ...
    


def get_flow_destination_endpoint_ports(connection_name: Optional[_builtins.str] = ..., flow_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFlowDestinationEndpointPortsResult:
    
    ...

def get_flow_destination_endpoint_ports_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., flow_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFlowDestinationEndpointPortsResult]:
    
    ...

