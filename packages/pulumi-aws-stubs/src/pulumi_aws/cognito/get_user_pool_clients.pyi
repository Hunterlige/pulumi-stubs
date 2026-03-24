import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetUserPoolClientsResult",
    "AwaitableGetUserPoolClientsResult",
    "get_user_pool_clients",
    "get_user_pool_clients_output",
]

@pulumi.output_type
class GetUserPoolClientsResult:
    def __init__(
        __self__, client_ids=..., client_names=..., id=..., region=..., user_pool_id=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientIds")
    def client_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientNames")
    def client_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str: ...

class AwaitableGetUserPoolClientsResult(GetUserPoolClientsResult):
    def __await__(self): ...

def get_user_pool_clients(
    region: Optional[_builtins.str] = ...,
    user_pool_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUserPoolClientsResult: ...
def get_user_pool_clients_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUserPoolClientsResult]: ...
