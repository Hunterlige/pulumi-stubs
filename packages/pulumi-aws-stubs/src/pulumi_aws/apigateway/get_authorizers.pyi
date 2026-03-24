import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAuthorizersResult",
    "AwaitableGetAuthorizersResult",
    "get_authorizers",
    "get_authorizers_output",
]

@pulumi.output_type
class GetAuthorizersResult:
    def __init__(__self__, id=..., ids=..., region=..., rest_api_id=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> _builtins.str: ...

class AwaitableGetAuthorizersResult(GetAuthorizersResult):
    def __await__(self): ...

def get_authorizers(
    region: Optional[_builtins.str] = ...,
    rest_api_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAuthorizersResult: ...
def get_authorizers_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    rest_api_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAuthorizersResult]: ...
