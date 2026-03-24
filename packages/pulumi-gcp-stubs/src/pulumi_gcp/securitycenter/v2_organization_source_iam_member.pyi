import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["V2OrganizationSourceIamMemberArgs", "V2OrganizationSourceIamMember"]

@pulumi.input_type
class V2OrganizationSourceIamMemberArgs:
    def __init__(
        __self__,
        *,
        member: pulumi.Input[_builtins.str],
        organization: pulumi.Input[_builtins.str],
        role: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        condition: Optional[
            pulumi.Input[V2OrganizationSourceIamMemberConditionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def member(self) -> pulumi.Input[_builtins.str]: ...
    @member.setter
    def member(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]: ...
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[V2OrganizationSourceIamMemberConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[V2OrganizationSourceIamMemberConditionArgs]]
    ): ...

@pulumi.input_type
class _V2OrganizationSourceIamMemberState:
    def __init__(
        __self__,
        *,
        condition: Optional[
            pulumi.Input[V2OrganizationSourceIamMemberConditionArgs]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[V2OrganizationSourceIamMemberConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[V2OrganizationSourceIamMemberConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def member(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member.setter
    def member(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class V2OrganizationSourceIamMember(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    V2OrganizationSourceIamMemberConditionArgs,
                    V2OrganizationSourceIamMemberConditionArgsDict,
                ]
            ]
        ] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: V2OrganizationSourceIamMemberArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    V2OrganizationSourceIamMemberConditionArgs,
                    V2OrganizationSourceIamMemberConditionArgsDict,
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        member: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> V2OrganizationSourceIamMember: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> pulumi.Output[Optional[outputs.V2OrganizationSourceIamMemberCondition]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def member(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]: ...
