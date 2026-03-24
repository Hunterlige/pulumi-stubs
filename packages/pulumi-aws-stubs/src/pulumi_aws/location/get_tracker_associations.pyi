import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTrackerAssociationsResult",
    "AwaitableGetTrackerAssociationsResult",
    "get_tracker_associations",
    "get_tracker_associations_output",
]

@pulumi.output_type
class GetTrackerAssociationsResult:
    def __init__(
        __self__, consumer_arns=..., id=..., region=..., tracker_name=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerArns")
    def consumer_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trackerName")
    def tracker_name(self) -> _builtins.str: ...

class AwaitableGetTrackerAssociationsResult(GetTrackerAssociationsResult):
    def __await__(self): ...

def get_tracker_associations(
    region: Optional[_builtins.str] = ...,
    tracker_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTrackerAssociationsResult: ...
def get_tracker_associations_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tracker_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTrackerAssociationsResult]: ...
