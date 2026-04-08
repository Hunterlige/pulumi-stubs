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
    "PolicyBooleanPolicyArgs",
    "PolicyBooleanPolicyArgsDict",
    "PolicyListPolicyArgs",
    "PolicyListPolicyArgsDict",
    "PolicyListPolicyAllowArgs",
    "PolicyListPolicyAllowArgsDict",
    "PolicyListPolicyDenyArgs",
    "PolicyListPolicyDenyArgsDict",
    "PolicyRestorePolicyArgs",
    "PolicyRestorePolicyArgsDict",
    "GetIAMPolicyAuditConfigArgs",
    "GetIAMPolicyAuditConfigArgsDict",
    "GetIAMPolicyAuditConfigAuditLogConfigArgs",
    "GetIAMPolicyAuditConfigAuditLogConfigArgsDict",
    "GetIAMPolicyBindingArgs",
    "GetIAMPolicyBindingArgsDict",
    "GetIAMPolicyBindingConditionArgs",
    "GetIAMPolicyBindingConditionArgsDict",
]

class AccessApprovalSettingsEnrolledServiceArgsDict(TypedDict):
    cloud_product: pulumi.Input[_builtins.str]
    enrollment_level: NotRequired[pulumi.Input[_builtins.str]]

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

class PolicyBooleanPolicyArgsDict(TypedDict):
    enforced: pulumi.Input[_builtins.bool]

@pulumi.input_type
class PolicyBooleanPolicyArgs:
    def __init__(__self__, *, enforced: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enforced(self) -> pulumi.Input[_builtins.bool]: ...
    @enforced.setter
    def enforced(self, value: pulumi.Input[_builtins.bool]): ...

class PolicyListPolicyArgsDict(TypedDict):
    allow: NotRequired[pulumi.Input[PolicyListPolicyAllowArgsDict]]
    deny: NotRequired[pulumi.Input[PolicyListPolicyDenyArgsDict]]
    inherit_from_parent: NotRequired[pulumi.Input[_builtins.bool]]
    suggested_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyListPolicyArgs:
    def __init__(
        __self__,
        *,
        allow: Optional[pulumi.Input[PolicyListPolicyAllowArgs]] = ...,
        deny: Optional[pulumi.Input[PolicyListPolicyDenyArgs]] = ...,
        inherit_from_parent: Optional[pulumi.Input[_builtins.bool]] = ...,
        suggested_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[pulumi.Input[PolicyListPolicyAllowArgs]]: ...
    @allow.setter
    def allow(self, value: Optional[pulumi.Input[PolicyListPolicyAllowArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[PolicyListPolicyDenyArgs]]: ...
    @deny.setter
    def deny(self, value: Optional[pulumi.Input[PolicyListPolicyDenyArgs]]): ...
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

class PolicyListPolicyAllowArgsDict(TypedDict):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PolicyListPolicyAllowArgs:
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

class PolicyListPolicyDenyArgsDict(TypedDict):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PolicyListPolicyDenyArgs:
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

class PolicyRestorePolicyArgsDict(TypedDict):
    default: pulumi.Input[_builtins.bool]

@pulumi.input_type
class PolicyRestorePolicyArgs:
    def __init__(__self__, *, default: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> pulumi.Input[_builtins.bool]: ...
    @default.setter
    def default(self, value: pulumi.Input[_builtins.bool]): ...

class GetIAMPolicyAuditConfigArgsDict(TypedDict):
    audit_log_configs: Sequence[GetIAMPolicyAuditConfigAuditLogConfigArgsDict]
    service: _builtins.str

@pulumi.input_type
class GetIAMPolicyAuditConfigArgs:
    def __init__(
        __self__,
        *,
        audit_log_configs: Sequence[GetIAMPolicyAuditConfigAuditLogConfigArgs],
        service: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(
        self,
    ) -> Sequence[GetIAMPolicyAuditConfigAuditLogConfigArgs]: ...
    @audit_log_configs.setter
    def audit_log_configs(
        self, value: Sequence[GetIAMPolicyAuditConfigAuditLogConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @service.setter
    def service(self, value: _builtins.str): ...

class GetIAMPolicyAuditConfigAuditLogConfigArgsDict(TypedDict):
    log_type: _builtins.str
    exempted_members: NotRequired[Sequence[_builtins.str]]

@pulumi.input_type
class GetIAMPolicyAuditConfigAuditLogConfigArgs:
    def __init__(
        __self__,
        *,
        log_type: _builtins.str,
        exempted_members: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str: ...
    @log_type.setter
    def log_type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="exemptedMembers")
    def exempted_members(self) -> Optional[Sequence[_builtins.str]]: ...
    @exempted_members.setter
    def exempted_members(self, value: Optional[Sequence[_builtins.str]]): ...

class GetIAMPolicyBindingArgsDict(TypedDict):
    members: Sequence[_builtins.str]
    role: _builtins.str
    condition: NotRequired[GetIAMPolicyBindingConditionArgsDict]

@pulumi.input_type
class GetIAMPolicyBindingArgs:
    def __init__(
        __self__,
        *,
        members: Sequence[_builtins.str],
        role: _builtins.str,
        condition: Optional[GetIAMPolicyBindingConditionArgs] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> Sequence[_builtins.str]: ...
    @members.setter
    def members(self, value: Sequence[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @role.setter
    def role(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[GetIAMPolicyBindingConditionArgs]: ...
    @condition.setter
    def condition(self, value: Optional[GetIAMPolicyBindingConditionArgs]): ...

class GetIAMPolicyBindingConditionArgsDict(TypedDict):
    expression: _builtins.str
    title: _builtins.str
    description: NotRequired[_builtins.str]

@pulumi.input_type
class GetIAMPolicyBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @expression.setter
    def expression(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @title.setter
    def title(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @description.setter
    def description(self, value: Optional[_builtins.str]): ...
