import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClientResult",
    "AwaitableGetClientResult",
    "get_client",
    "get_client_output",
]

@pulumi.output_type
class GetClientResult:
    def __init__(
        __self__, brand=..., client_id=..., display_name=..., id=..., secret=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def brand(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str: ...

class AwaitableGetClientResult(GetClientResult):
    def __await__(self): ...

def get_client(
    brand: Optional[_builtins.str] = ...,
    client_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClientResult: ...
def get_client_output(
    brand: Optional[pulumi.Input[_builtins.str]] = ...,
    client_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClientResult]: ...
