import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCachePolicyResult",
    "AwaitableGetCachePolicyResult",
    "get_cache_policy",
    "get_cache_policy_output",
]

@pulumi.output_type
class GetCachePolicyResult:
    def __init__(
        __self__,
        arn=...,
        comment=...,
        default_ttl=...,
        etag=...,
        id=...,
        max_ttl=...,
        min_ttl=...,
        name=...,
        parameters_in_cache_key_and_forwarded_to_origins=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minTtl")
    def min_ttl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parametersInCacheKeyAndForwardedToOrigins")
    def parameters_in_cache_key_and_forwarded_to_origins(
        self,
    ) -> Sequence[
        outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginResult
    ]: ...

class AwaitableGetCachePolicyResult(GetCachePolicyResult):
    def __await__(self): ...

def get_cache_policy(
    id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCachePolicyResult: ...
def get_cache_policy_output(
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCachePolicyResult]: ...
