import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRedisLinkedServerResult",
    "AwaitableGetRedisLinkedServerResult",
    "get_redis_linked_server",
    "get_redis_linked_server_output",
]

@pulumi.output_type
class GetRedisLinkedServerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        linked_redis_cache_id=...,
        linked_redis_cache_location=...,
        name=...,
        provisioning_state=...,
        server_role=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkedRedisCacheId")
    def linked_redis_cache_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkedRedisCacheLocation")
    def linked_redis_cache_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serverRole")
    def server_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRedisLinkedServerResult(GetRedisLinkedServerResult):
    def __await__(self): ...

def get_redis_linked_server(
    linked_server_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRedisLinkedServerResult: ...
def get_redis_linked_server_output(
    linked_server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRedisLinkedServerResult]: ...
