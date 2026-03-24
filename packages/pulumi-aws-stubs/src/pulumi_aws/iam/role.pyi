import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RoleArgs", "Role"]

@pulumi.input_type
class RoleArgs:
    def __init__(
        __self__,
        *,
        assume_role_policy: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        force_detach_policies: Optional[pulumi.Input[_builtins.bool]] = ...,
        inline_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoleInlinePolicyArgs]]]
        ] = ...,
        managed_policy_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        max_session_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_boundary: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assumeRolePolicy")
    def assume_role_policy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]: ...
    @assume_role_policy.setter
    def assume_role_policy(
        self, value: pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDetachPolicies")
    def force_detach_policies(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_detach_policies.setter
    def force_detach_policies(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="inlinePolicies")
    def inline_policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoleInlinePolicyArgs]]]]: ...
    @inline_policies.setter
    def inline_policies(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RoleInlinePolicyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @managed_policy_arns.setter
    def managed_policy_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_session_duration.setter
    def max_session_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permissions_boundary.setter
    def permissions_boundary(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RoleState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assume_role_policy: Optional[
            pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]
        ] = ...,
        create_date: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        force_detach_policies: Optional[pulumi.Input[_builtins.bool]] = ...,
        inline_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoleInlinePolicyArgs]]]
        ] = ...,
        managed_policy_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        max_session_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_boundary: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="assumeRolePolicy")
    def assume_role_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]: ...
    @assume_role_policy.setter
    def assume_role_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyDocumentArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_date.setter
    def create_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDetachPolicies")
    def force_detach_policies(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_detach_policies.setter
    def force_detach_policies(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="inlinePolicies")
    def inline_policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoleInlinePolicyArgs]]]]: ...
    @inline_policies.setter
    def inline_policies(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RoleInlinePolicyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @managed_policy_arns.setter
    def managed_policy_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_session_duration.setter
    def max_session_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permissions_boundary.setter
    def permissions_boundary(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unique_id.setter
    def unique_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:iam/role:Role")
class Role(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        assume_role_policy: Optional[
            pulumi.Input[
                Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        force_detach_policies: Optional[pulumi.Input[_builtins.bool]] = ...,
        inline_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[RoleInlinePolicyArgs, RoleInlinePolicyArgsDict]]
                ]
            ]
        ] = ...,
        managed_policy_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        max_session_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_boundary: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RoleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assume_role_policy: Optional[
            pulumi.Input[
                Union[_builtins.str, Union[PolicyDocumentArgs, PolicyDocumentArgsDict]]
            ]
        ] = ...,
        create_date: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        force_detach_policies: Optional[pulumi.Input[_builtins.bool]] = ...,
        inline_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[RoleInlinePolicyArgs, RoleInlinePolicyArgsDict]]
                ]
            ]
        ] = ...,
        managed_policy_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        max_session_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions_boundary: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Role: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="assumeRolePolicy")
    def assume_role_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="forceDetachPolicies")
    def force_detach_policies(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="inlinePolicies")
    def inline_policies(self) -> pulumi.Output[Sequence[outputs.RoleInlinePolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[_builtins.str]: ...
