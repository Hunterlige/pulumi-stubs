import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAddressesResult",
    "AwaitableGetAddressesResult",
    "get_addresses",
    "get_addresses_output",
]

@pulumi.output_type
class GetAddressesResult:
    def __init__(
        __self__, addresses=..., filter=..., id=..., project=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[outputs.GetAddressesAddressResult]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

class AwaitableGetAddressesResult(GetAddressesResult):
    def __await__(self): ...

def get_addresses(
    filter: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAddressesResult: ...
def get_addresses_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAddressesResult]: ...
