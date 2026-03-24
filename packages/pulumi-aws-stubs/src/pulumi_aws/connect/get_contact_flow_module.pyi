import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContactFlowModuleResult",
    "AwaitableGetContactFlowModuleResult",
    "get_contact_flow_module",
    "get_contact_flow_module_output",
]

@pulumi.output_type
class GetContactFlowModuleResult:
    def __init__(
        __self__,
        arn=...,
        contact_flow_module_id=...,
        content=...,
        description=...,
        id=...,
        instance_id=...,
        name=...,
        region=...,
        state=...,
        status=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactFlowModuleId")
    def contact_flow_module_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetContactFlowModuleResult(GetContactFlowModuleResult):
    def __await__(self): ...

def get_contact_flow_module(
    contact_flow_module_id: Optional[_builtins.str] = ...,
    instance_id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContactFlowModuleResult: ...
def get_contact_flow_module_output(
    contact_flow_module_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContactFlowModuleResult]: ...
