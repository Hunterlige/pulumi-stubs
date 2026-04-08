import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetQueueResult", "AwaitableGetQueueResult", "get_queue", "get_queue_output"]

@pulumi.output_type
class GetQueueResult:
    def __init__(
        __self__,
        approximate_message_count=...,
        azure_api_version=...,
        id=...,
        metadata=...,
        name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approximateMessageCount")
    def approximate_message_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetQueueResult(GetQueueResult):
    def __await__(self): ...

def get_queue(
    account_name: Optional[_builtins.str] = ...,
    queue_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetQueueResult: ...
def get_queue_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    queue_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetQueueResult]: ...
