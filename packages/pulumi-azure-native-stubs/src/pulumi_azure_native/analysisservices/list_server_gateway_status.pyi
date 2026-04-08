import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListServerGatewayStatusResult",
    "AwaitableListServerGatewayStatusResult",
    "list_server_gateway_status",
    "list_server_gateway_status_output",
]

@pulumi.output_type
class ListServerGatewayStatusResult:
    def __init__(__self__, status=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.int]: ...

class AwaitableListServerGatewayStatusResult(ListServerGatewayStatusResult):
    def __await__(self): ...

def list_server_gateway_status(
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListServerGatewayStatusResult: ...
def list_server_gateway_status_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListServerGatewayStatusResult]: ...
