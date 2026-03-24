import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecretPolicyArgs", "SecretPolicy"]

@pulumi.input_type
class SecretPolicyArgs:
    def __init__(
        __self__,
        *,
        policy: pulumi.Input[_builtins.str],
        secret_arn: pulumi.Input[_builtins.str],
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[_builtins.str]: ...
    @policy.setter
    def policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @secret_arn.setter
    def secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @block_public_policy.setter
    def block_public_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SecretPolicyState:
    def __init__(
        __self__,
        *,
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @block_public_policy.setter
    def block_public_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:secretsmanager/secretPolicy:SecretPolicy")
class SecretPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecretPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecretPolicy: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Output[_builtins.str]: ...
