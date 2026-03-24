import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GroupPolicyAttachmentArgs", "GroupPolicyAttachment"]

@pulumi.input_type
class GroupPolicyAttachmentArgs:
    def __init__(
        __self__,
        *,
        group: pulumi.Input[_builtins.str],
        policy_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> pulumi.Input[_builtins.str]: ...
    @group.setter
    def group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Input[_builtins.str]: ...
    @policy_arn.setter
    def policy_arn(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _GroupPolicyAttachmentState:
    def __init__(
        __self__,
        *,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_arn.setter
    def policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class GroupPolicyAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GroupPolicyAttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> GroupPolicyAttachment: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Output[_builtins.str]: ...
