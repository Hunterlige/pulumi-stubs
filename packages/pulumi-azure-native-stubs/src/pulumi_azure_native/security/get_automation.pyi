import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAutomationResult",
    "AwaitableGetAutomationResult",
    "get_automation",
    "get_automation_output",
]

@pulumi.output_type
class GetAutomationResult:
    def __init__(
        __self__,
        actions=...,
        azure_api_version=...,
        description=...,
        etag=...,
        id=...,
        is_enabled=...,
        kind=...,
        location=...,
        name=...,
        scopes=...,
        sources=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[outputs.AutomationScopeResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[Sequence[outputs.AutomationSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAutomationResult(GetAutomationResult):
    def __await__(self): ...

def get_automation(
    automation_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAutomationResult: ...
def get_automation_output(
    automation_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAutomationResult]: ...
