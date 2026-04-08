import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListTopicSharedAccessKeysResult",
    "AwaitableListTopicSharedAccessKeysResult",
    "list_topic_shared_access_keys",
    "list_topic_shared_access_keys_output",
]

@pulumi.output_type
class ListTopicSharedAccessKeysResult:
    def __init__(__self__, key1=..., key2=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key2(self) -> Optional[_builtins.str]: ...

class AwaitableListTopicSharedAccessKeysResult(ListTopicSharedAccessKeysResult):
    def __await__(self): ...

def list_topic_shared_access_keys(
    resource_group_name: Optional[_builtins.str] = ...,
    topic_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListTopicSharedAccessKeysResult: ...
def list_topic_shared_access_keys_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListTopicSharedAccessKeysResult]: ...
