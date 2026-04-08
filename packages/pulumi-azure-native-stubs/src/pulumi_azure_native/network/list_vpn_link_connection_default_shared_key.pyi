import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListVpnLinkConnectionDefaultSharedKeyResult",
    ...,
    "list_vpn_link_connection_default_shared_key",
    "list_vpn_link_connection_default_shared_key_output",
]

@pulumi.output_type
class ListVpnLinkConnectionDefaultSharedKeyResult:
    def __init__(__self__, id=..., name=..., properties=..., type=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.SharedKeyPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableListVpnLinkConnectionDefaultSharedKeyResult(
    ListVpnLinkConnectionDefaultSharedKeyResult
):
    def __await__(self): ...

def list_vpn_link_connection_default_shared_key(
    connection_name: Optional[_builtins.str] = ...,
    gateway_name: Optional[_builtins.str] = ...,
    link_connection_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListVpnLinkConnectionDefaultSharedKeyResult: ...
def list_vpn_link_connection_default_shared_key_output(
    connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    link_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListVpnLinkConnectionDefaultSharedKeyResult]: ...
