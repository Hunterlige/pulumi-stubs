import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCanonicalUserIdResult",
    "AwaitableGetCanonicalUserIdResult",
    "get_canonical_user_id",
    "get_canonical_user_id_output",
]

@pulumi.output_type
class GetCanonicalUserIdResult:
    def __init__(__self__, display_name=..., id=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

class AwaitableGetCanonicalUserIdResult(GetCanonicalUserIdResult):
    def __await__(self): ...

def get_canonical_user_id(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCanonicalUserIdResult: ...
def get_canonical_user_id_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCanonicalUserIdResult]: ...
