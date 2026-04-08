import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetChannelResult",
    "AwaitableGetChannelResult",
    "get_channel",
    "get_channel_output",
]

@pulumi.output_type
class GetChannelResult:
    def __init__(
        __self__,
        azure_api_version=...,
        channel_functions=...,
        channel_type=...,
        credentials=...,
        id=...,
        name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="channelFunctions")
    def channel_functions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetChannelResult(GetChannelResult):
    def __await__(self): ...

def get_channel(
    account_name: Optional[_builtins.str] = ...,
    channel_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetChannelResult: ...
def get_channel_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    channel_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetChannelResult]: ...
