import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetStackResult", "AwaitableGetStackResult", "get_stack", "get_stack_output"]

@pulumi.output_type
class GetStackResult:
    def __init__(
        __self__,
        capabilities=...,
        description=...,
        disable_rollback=...,
        iam_role_arn=...,
        id=...,
        name=...,
        notification_arns=...,
        outputs=...,
        parameters=...,
        region=...,
        tags=...,
        template_body=...,
        timeout_in_minutes=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disableRollback")
    def disable_rollback(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> _builtins.int: ...

class AwaitableGetStackResult(GetStackResult):
    def __await__(self): ...

def get_stack(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStackResult: ...
def get_stack_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStackResult]: ...
