import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessApprovalSettingsEnrolledServiceArgs",
    "AccessApprovalSettingsEnrolledServiceArgsDict",
    "IAMBindingConditionArgs",
    "IAMBindingConditionArgsDict",
    "IAMMemberConditionArgs",
    "IAMMemberConditionArgsDict",
    "IamAuditConfigAuditLogConfigArgs",
    "IamAuditConfigAuditLogConfigArgsDict",
    "OrganizationPolicyBooleanPolicyArgs",
    "OrganizationPolicyBooleanPolicyArgsDict",
    "OrganizationPolicyListPolicyArgs",
    "OrganizationPolicyListPolicyArgsDict",
    "OrganizationPolicyListPolicyAllowArgs",
    "OrganizationPolicyListPolicyAllowArgsDict",
    "OrganizationPolicyListPolicyDenyArgs",
    "OrganizationPolicyListPolicyDenyArgsDict",
    "OrganizationPolicyRestorePolicyArgs",
    "OrganizationPolicyRestorePolicyArgsDict",
]

class AccessApprovalSettingsEnrolledServiceArgsDict(TypedDict):
    cloud_product: pulumi.Input[_builtins.str]
    enrollment_level: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AccessApprovalSettingsEnrolledServiceArgs:
    def __init__(
        __self__,
        *,
        cloud_product: pulumi.Input[_builtins.str],
        enrollment_level: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudProduct")
    def cloud_product(self) -> pulumi.Input[_builtins.str]: ...
    @cloud_product.setter
    def cloud_product(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enrollmentLevel")
    def enrollment_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enrollment_level.setter
    def enrollment_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IamAuditConfigAuditLogConfigArgsDict(TypedDict):
    log_type: pulumi.Input[_builtins.str]
    exempted_members: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class IamAuditConfigAuditLogConfigArgs:
    def __init__(
        __self__,
        *,
        log_type: pulumi.Input[_builtins.str],
        exempted_members: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> pulumi.Input[_builtins.str]: ...
    @log_type.setter
    def log_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exemptedMembers")
    def exempted_members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exempted_members.setter
    def exempted_members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OrganizationPolicyBooleanPolicyArgsDict(TypedDict):
    enforced: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class OrganizationPolicyBooleanPolicyArgs:
    def __init__(__self__, *, enforced: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enforced(self) -> pulumi.Input[_builtins.bool]: ...
    @enforced.setter
    def enforced(self, value: pulumi.Input[_builtins.bool]): ...

class OrganizationPolicyListPolicyArgsDict(TypedDict):
    allow: NotRequired[pulumi.Input[OrganizationPolicyListPolicyAllowArgsDict]]
    deny: NotRequired[pulumi.Input[OrganizationPolicyListPolicyDenyArgsDict]]
    inherit_from_parent: NotRequired[pulumi.Input[_builtins.bool]]
    suggested_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OrganizationPolicyListPolicyArgs:
    def __init__(
        __self__,
        *,
        allow: Optional[pulumi.Input[OrganizationPolicyListPolicyAllowArgs]] = ...,
        deny: Optional[pulumi.Input[OrganizationPolicyListPolicyDenyArgs]] = ...,
        inherit_from_parent: Optional[pulumi.Input[_builtins.bool]] = ...,
        suggested_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allow(
        self,
    ) -> Optional[pulumi.Input[OrganizationPolicyListPolicyAllowArgs]]: ...
    @allow.setter
    def allow(
        self, value: Optional[pulumi.Input[OrganizationPolicyListPolicyAllowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[OrganizationPolicyListPolicyDenyArgs]]: ...
    @deny.setter
    def deny(
        self, value: Optional[pulumi.Input[OrganizationPolicyListPolicyDenyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @inherit_from_parent.setter
    def inherit_from_parent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="suggestedValue")
    def suggested_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suggested_value.setter
    def suggested_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OrganizationPolicyListPolicyAllowArgsDict(TypedDict):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class OrganizationPolicyListPolicyAllowArgs:
    def __init__(
        __self__,
        *,
        all: Optional[pulumi.Input[_builtins.bool]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all.setter
    def all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OrganizationPolicyListPolicyDenyArgsDict(TypedDict):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class OrganizationPolicyListPolicyDenyArgs:
    def __init__(
        __self__,
        *,
        all: Optional[pulumi.Input[_builtins.bool]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all.setter
    def all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OrganizationPolicyRestorePolicyArgsDict(TypedDict):
    default: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class OrganizationPolicyRestorePolicyArgs:
    def __init__(__self__, *, default: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> pulumi.Input[_builtins.bool]: ...
    @default.setter
    def default(self, value: pulumi.Input[_builtins.bool]): ...
