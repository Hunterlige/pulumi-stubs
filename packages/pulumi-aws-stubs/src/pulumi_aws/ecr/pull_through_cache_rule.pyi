import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PullThroughCacheRuleArgs", "PullThroughCacheRule"]

@pulumi.input_type
class PullThroughCacheRuleArgs:
    def __init__(
        __self__,
        *,
        ecr_repository_prefix: pulumi.Input[_builtins.str],
        upstream_registry_url: pulumi.Input[_builtins.str],
        credential_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        upstream_repository_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ecrRepositoryPrefix")
    def ecr_repository_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @ecr_repository_prefix.setter
    def ecr_repository_prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="upstreamRegistryUrl")
    def upstream_registry_url(self) -> pulumi.Input[_builtins.str]: ...
    @upstream_registry_url.setter
    def upstream_registry_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialArn")
    def credential_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_arn.setter
    def credential_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_role_arn.setter
    def custom_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upstreamRepositoryPrefix")
    def upstream_repository_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upstream_repository_prefix.setter
    def upstream_repository_prefix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _PullThroughCacheRuleState:
    def __init__(
        __self__,
        *,
        credential_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ecr_repository_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        upstream_registry_url: Optional[pulumi.Input[_builtins.str]] = ...,
        upstream_repository_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialArn")
    def credential_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_arn.setter
    def credential_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_role_arn.setter
    def custom_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ecrRepositoryPrefix")
    def ecr_repository_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ecr_repository_prefix.setter
    def ecr_repository_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upstreamRegistryUrl")
    def upstream_registry_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upstream_registry_url.setter
    def upstream_registry_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upstreamRepositoryPrefix")
    def upstream_repository_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upstream_repository_prefix.setter
    def upstream_repository_prefix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:ecr/pullThroughCacheRule:PullThroughCacheRule")
class PullThroughCacheRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        credential_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ecr_repository_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        upstream_registry_url: Optional[pulumi.Input[_builtins.str]] = ...,
        upstream_repository_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PullThroughCacheRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        credential_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ecr_repository_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        upstream_registry_url: Optional[pulumi.Input[_builtins.str]] = ...,
        upstream_repository_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PullThroughCacheRule: ...
    @_builtins.property
    @pulumi.getter(name="credentialArn")
    def credential_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrRepositoryPrefix")
    def ecr_repository_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="upstreamRegistryUrl")
    def upstream_registry_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="upstreamRepositoryPrefix")
    def upstream_repository_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
