import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessApprovalSettingsEnrolledService",
    "ApiKeyRestrictions",
    "ApiKeyRestrictionsAndroidKeyRestrictions",
    ...,
    "ApiKeyRestrictionsApiTarget",
    "ApiKeyRestrictionsBrowserKeyRestrictions",
    "ApiKeyRestrictionsIosKeyRestrictions",
    "ApiKeyRestrictionsServerKeyRestrictions",
    "IAMAuditConfigAuditLogConfig",
    "IAMBindingCondition",
    "IAMMemberCondition",
    "OrganizationPolicyBooleanPolicy",
    "OrganizationPolicyListPolicy",
    "OrganizationPolicyListPolicyAllow",
    "OrganizationPolicyListPolicyDeny",
    "OrganizationPolicyRestorePolicy",
    "GetAncestryAncestorResult",
    "GetIamCustomRolesRoleResult",
    "GetOrganizationPolicyBooleanPolicyResult",
    "GetOrganizationPolicyListPolicyResult",
    "GetOrganizationPolicyListPolicyAllowResult",
    "GetOrganizationPolicyListPolicyDenyResult",
    "GetOrganizationPolicyRestorePolicyResult",
    "GetProjectProjectResult",
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
class ApiKeyRestrictions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        android_key_restrictions: Optional[
            outputs.ApiKeyRestrictionsAndroidKeyRestrictions
        ] = ...,
        api_targets: Optional[Sequence[outputs.ApiKeyRestrictionsApiTarget]] = ...,
        browser_key_restrictions: Optional[
            outputs.ApiKeyRestrictionsBrowserKeyRestrictions
        ] = ...,
        ios_key_restrictions: Optional[
            outputs.ApiKeyRestrictionsIosKeyRestrictions
        ] = ...,
        server_key_restrictions: Optional[
            outputs.ApiKeyRestrictionsServerKeyRestrictions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="androidKeyRestrictions")
    def android_key_restrictions(
        self,
    ) -> Optional[outputs.ApiKeyRestrictionsAndroidKeyRestrictions]: ...
    @_builtins.property
    @pulumi.getter(name="apiTargets")
    def api_targets(
        self,
    ) -> Optional[Sequence[outputs.ApiKeyRestrictionsApiTarget]]: ...
    @_builtins.property
    @pulumi.getter(name="browserKeyRestrictions")
    def browser_key_restrictions(
        self,
    ) -> Optional[outputs.ApiKeyRestrictionsBrowserKeyRestrictions]: ...
    @_builtins.property
    @pulumi.getter(name="iosKeyRestrictions")
    def ios_key_restrictions(
        self,
    ) -> Optional[outputs.ApiKeyRestrictionsIosKeyRestrictions]: ...
    @_builtins.property
    @pulumi.getter(name="serverKeyRestrictions")
    def server_key_restrictions(
        self,
    ) -> Optional[outputs.ApiKeyRestrictionsServerKeyRestrictions]: ...

@pulumi.output_type
class ApiKeyRestrictionsAndroidKeyRestrictions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_applications: Sequence[
            outputs.ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplication
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedApplications")
    def allowed_applications(
        self,
    ) -> Sequence[
        outputs.ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplication
    ]: ...

@pulumi.output_type
class ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, package_name: _builtins.str, sha1_fingerprint: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> _builtins.str: ...

@pulumi.output_type
class ApiKeyRestrictionsApiTarget(dict):
    def __init__(
        __self__,
        *,
        service: _builtins.str,
        methods: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ApiKeyRestrictionsBrowserKeyRestrictions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, allowed_referrers: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedReferrers")
    def allowed_referrers(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ApiKeyRestrictionsIosKeyRestrictions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, allowed_bundle_ids: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedBundleIds")
    def allowed_bundle_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ApiKeyRestrictionsServerKeyRestrictions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, allowed_ips: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIps")
    def allowed_ips(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class IAMAuditConfigAuditLogConfig(dict):
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
class GetAncestryAncestorResult(dict):
    def __init__(__self__, *, id: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetIamCustomRolesRoleResult(dict):
    def __init__(
        __self__,
        *,
        deleted: _builtins.bool,
        description: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        permissions: Sequence[_builtins.str],
        role_id: _builtins.str,
        stage: _builtins.str,
        title: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...

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

@pulumi.output_type
class GetProjectProjectResult(dict):
    def __init__(
        __self__,
        *,
        create_time: _builtins.str,
        labels: Mapping[str, _builtins.str],
        lifecycle_state: _builtins.str,
        name: _builtins.str,
        number: _builtins.str,
        parent: Mapping[str, _builtins.str],
        project_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
