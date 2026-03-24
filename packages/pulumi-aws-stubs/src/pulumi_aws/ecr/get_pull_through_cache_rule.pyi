import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPullThroughCacheRuleResult",
    "AwaitableGetPullThroughCacheRuleResult",
    "get_pull_through_cache_rule",
    "get_pull_through_cache_rule_output",
]

@pulumi.output_type
class GetPullThroughCacheRuleResult:
    def __init__(
        __self__,
        credential_arn=...,
        custom_role_arn=...,
        ecr_repository_prefix=...,
        id=...,
        region=...,
        registry_id=...,
        upstream_registry_url=...,
        upstream_repository_prefix=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialArn")
    def credential_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ecrRepositoryPrefix")
    def ecr_repository_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upstreamRegistryUrl")
    def upstream_registry_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upstreamRepositoryPrefix")
    def upstream_repository_prefix(self) -> _builtins.str: ...

class AwaitableGetPullThroughCacheRuleResult(GetPullThroughCacheRuleResult):
    def __await__(self): ...

def get_pull_through_cache_rule(
    ecr_repository_prefix: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPullThroughCacheRuleResult: ...
def get_pull_through_cache_rule_output(
    ecr_repository_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPullThroughCacheRuleResult]: ...
