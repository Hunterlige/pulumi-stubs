import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetAliasResult", "AwaitableGetAliasResult", "get_alias", "get_alias_output"]

@pulumi.output_type
class GetAliasResult:
    def __init__(
        __self__,
        arn=...,
        id=...,
        name=...,
        region=...,
        target_key_arn=...,
        target_key_id=...,
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
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetKeyArn")
    def target_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetKeyId")
    def target_key_id(self) -> _builtins.str: ...

class AwaitableGetAliasResult(GetAliasResult):
    def __await__(self): ...

def get_alias(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAliasResult: ...
def get_alias_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAliasResult]: ...
