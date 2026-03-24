import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRequiredTagsResult",
    "AwaitableGetRequiredTagsResult",
    "get_required_tags",
    "get_required_tags_output",
]

@pulumi.output_type
class GetRequiredTagsResult:
    def __init__(__self__, id=..., region=..., required_tags=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiredTags")
    def required_tags(self) -> Sequence[outputs.GetRequiredTagsRequiredTagResult]: ...

class AwaitableGetRequiredTagsResult(GetRequiredTagsResult):
    def __await__(self): ...

def get_required_tags(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetRequiredTagsResult: ...
def get_required_tags_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRequiredTagsResult]: ...
