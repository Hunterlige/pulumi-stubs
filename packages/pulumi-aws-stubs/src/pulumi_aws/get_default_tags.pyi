import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDefaultTagsResult",
    "AwaitableGetDefaultTagsResult",
    "get_default_tags",
    "get_default_tags_output",
]

@pulumi.output_type
class GetDefaultTagsResult:
    def __init__(__self__, id=..., tags=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetDefaultTagsResult(GetDefaultTagsResult):
    def __await__(self): ...

def get_default_tags(
    id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetDefaultTagsResult: ...
def get_default_tags_output(
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDefaultTagsResult]: ...
