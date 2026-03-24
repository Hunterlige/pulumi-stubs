import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBotAliasResult",
    "AwaitableGetBotAliasResult",
    "get_bot_alias",
    "get_bot_alias_output",
]

@pulumi.output_type
class GetBotAliasResult:
    def __init__(
        __self__,
        arn=...,
        bot_name=...,
        bot_version=...,
        checksum=...,
        created_date=...,
        description=...,
        id=...,
        last_updated_date=...,
        name=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="botName")
    def bot_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetBotAliasResult(GetBotAliasResult):
    def __await__(self): ...

def get_bot_alias(
    bot_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBotAliasResult: ...
def get_bot_alias_output(
    bot_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBotAliasResult]: ...
