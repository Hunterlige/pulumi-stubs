import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFrameworkResult",
    "AwaitableGetFrameworkResult",
    "get_framework",
    "get_framework_output",
]

@pulumi.output_type
class GetFrameworkResult:
    def __init__(
        __self__,
        arn=...,
        compliance_type=...,
        control_sets=...,
        description=...,
        framework_type=...,
        id=...,
        name=...,
        region=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="complianceType")
    def compliance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="controlSets")
    def control_sets(self) -> Sequence[outputs.GetFrameworkControlSetResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="frameworkType")
    def framework_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetFrameworkResult(GetFrameworkResult):
    def __await__(self): ...

def get_framework(
    framework_type: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFrameworkResult: ...
def get_framework_output(
    framework_type: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFrameworkResult]: ...
