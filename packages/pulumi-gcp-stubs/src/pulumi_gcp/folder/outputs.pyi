import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessApprovalSettingsEnrolledService",
    "IAMBindingCondition",
    "IAMMemberCondition",
    "IamAuditConfigAuditLogConfig",
    "OrganizationPolicyBooleanPolicy",
    "OrganizationPolicyListPolicy",
    "OrganizationPolicyListPolicyAllow",
    "OrganizationPolicyListPolicyDeny",
    "OrganizationPolicyRestorePolicy",
    "GetOrganizationPolicyBooleanPolicyResult",
    "GetOrganizationPolicyListPolicyResult",
    "GetOrganizationPolicyListPolicyAllowResult",
    "GetOrganizationPolicyListPolicyDenyResult",
    "GetOrganizationPolicyRestorePolicyResult",
]

@pulumi.output_type
class AccessApprovalSettingsEnrolledService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_product: _builtins.str,
        enrollment_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudProduct")
    def cloud_product(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enrollmentLevel")
    def enrollment_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IAMBindingCondition(dict):
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
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IAMMemberCondition(dict):
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
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IamAuditConfigAuditLogConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        log_type: _builtins.str,
        exempted_members: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exemptedMembers")
    def exempted_members(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OrganizationPolicyBooleanPolicy(dict):
    def __init__(__self__, *, enforced: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enforced(self) -> _builtins.bool: ...

@pulumi.output_type
class OrganizationPolicyListPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow: Optional[outputs.OrganizationPolicyListPolicyAllow] = ...,
        deny: Optional[outputs.OrganizationPolicyListPolicyDeny] = ...,
        inherit_from_parent: Optional[_builtins.bool] = ...,
        suggested_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.OrganizationPolicyListPolicyAllow]: ...
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[outputs.OrganizationPolicyListPolicyDeny]: ...
    @_builtins.property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="suggestedValue")
    def suggested_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationPolicyListPolicyAllow(dict):
    def __init__(
        __self__,
        *,
        all: Optional[_builtins.bool] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OrganizationPolicyListPolicyDeny(dict):
    def __init__(
        __self__,
        *,
        all: Optional[_builtins.bool] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OrganizationPolicyRestorePolicy(dict):
    def __init__(__self__, *, default: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> _builtins.bool: ...

@pulumi.output_type
class GetOrganizationPolicyBooleanPolicyResult(dict):
    def __init__(__self__, *, enforced: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enforced(self) -> _builtins.bool: ...

@pulumi.output_type
class GetOrganizationPolicyListPolicyResult(dict):
    def __init__(
        __self__,
        *,
        allows: Sequence[outputs.GetOrganizationPolicyListPolicyAllowResult],
        denies: Sequence[outputs.GetOrganizationPolicyListPolicyDenyResult],
        inherit_from_parent: _builtins.bool,
        suggested_value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allows(
        self,
    ) -> Sequence[outputs.GetOrganizationPolicyListPolicyAllowResult]: ...
    @_builtins.property
    @pulumi.getter
    def denies(self) -> Sequence[outputs.GetOrganizationPolicyListPolicyDenyResult]: ...
    @_builtins.property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="suggestedValue")
    def suggested_value(self) -> _builtins.str: ...

@pulumi.output_type
class GetOrganizationPolicyListPolicyAllowResult(dict):
    def __init__(
        __self__, *, all: _builtins.bool, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOrganizationPolicyListPolicyDenyResult(dict):
    def __init__(
        __self__, *, all: _builtins.bool, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOrganizationPolicyRestorePolicyResult(dict):
    def __init__(__self__, *, default: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> _builtins.bool: ...
