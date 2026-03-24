import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetControlsResult",
    "AwaitableGetControlsResult",
    "get_controls",
    "get_controls_output",
]

@pulumi.output_type
class GetControlsResult:
    def __init__(
        __self__, enabled_controls=..., id=..., region=..., target_identifier=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledControls")
    def enabled_controls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetIdentifier")
    def target_identifier(self) -> _builtins.str: ...

class AwaitableGetControlsResult(GetControlsResult):
    def __await__(self): ...

def get_controls(
    region: Optional[_builtins.str] = ...,
    target_identifier: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetControlsResult: ...
def get_controls_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    target_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetControlsResult]: ...
