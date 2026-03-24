import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccessKeysResult",
    "AwaitableGetAccessKeysResult",
    "get_access_keys",
    "get_access_keys_output",
]

@pulumi.output_type
class GetAccessKeysResult:
    def __init__(__self__, access_keys=..., id=..., user=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKeys")
    def access_keys(self) -> Sequence[outputs.GetAccessKeysAccessKeyResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> _builtins.str: ...

class AwaitableGetAccessKeysResult(GetAccessKeysResult):
    def __await__(self): ...

def get_access_keys(
    user: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetAccessKeysResult: ...
def get_access_keys_output(
    user: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccessKeysResult]: ...
