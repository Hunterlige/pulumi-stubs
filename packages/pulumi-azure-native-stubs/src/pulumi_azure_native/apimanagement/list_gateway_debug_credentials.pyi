import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListGatewayDebugCredentialsResult",
    "AwaitableListGatewayDebugCredentialsResult",
    "list_gateway_debug_credentials",
    "list_gateway_debug_credentials_output",
]

@pulumi.output_type
class ListGatewayDebugCredentialsResult:
    def __init__(__self__, token=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]: ...

class AwaitableListGatewayDebugCredentialsResult(ListGatewayDebugCredentialsResult):
    def __await__(self): ...

def list_gateway_debug_credentials(
    api_id: Optional[_builtins.str] = ...,
    credentials_expire_after: Optional[_builtins.str] = ...,
    gateway_id: Optional[_builtins.str] = ...,
    purposes: Optional[
        Sequence[Union[_builtins.str, GatewayListDebugCredentialsContractPurpose]]
    ] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListGatewayDebugCredentialsResult: ...
def list_gateway_debug_credentials_output(
    api_id: Optional[pulumi.Input[_builtins.str]] = ...,
    credentials_expire_after: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
    purposes: Optional[
        pulumi.Input[
            Sequence[Union[_builtins.str, GatewayListDebugCredentialsContractPurpose]]
        ]
    ] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListGatewayDebugCredentialsResult]: ...
