import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetPlanResult", "AwaitableGetPlanResult", "get_plan", "get_plan_output"]

@pulumi.output_type
class GetPlanResult:
    def __init__(
        __self__,
        arn=...,
        id=...,
        name=...,
        plan_id=...,
        region=...,
        rules=...,
        scan_settings=...,
        tags=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetPlanRuleResult]: ...
    @_builtins.property
    @pulumi.getter(name="scanSettings")
    def scan_settings(self) -> Sequence[outputs.GetPlanScanSettingResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetPlanResult(GetPlanResult):
    def __await__(self): ...

def get_plan(
    plan_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPlanResult: ...
def get_plan_output(
    plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPlanResult]: ...
