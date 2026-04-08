import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessApprovalSettingsEnrolledServiceArgs",
    "AccessApprovalSettingsEnrolledServiceArgsDict",
    "ApiKeyRestrictionsArgs",
    "ApiKeyRestrictionsArgsDict",
    "ApiKeyRestrictionsAndroidKeyRestrictionsArgs",
    "ApiKeyRestrictionsAndroidKeyRestrictionsArgsDict",
    ...,
    ...,
    "ApiKeyRestrictionsApiTargetArgs",
    "ApiKeyRestrictionsApiTargetArgsDict",
    "ApiKeyRestrictionsBrowserKeyRestrictionsArgs",
    "ApiKeyRestrictionsBrowserKeyRestrictionsArgsDict",
    "ApiKeyRestrictionsIosKeyRestrictionsArgs",
    "ApiKeyRestrictionsIosKeyRestrictionsArgsDict",
    "ApiKeyRestrictionsServerKeyRestrictionsArgs",
    "ApiKeyRestrictionsServerKeyRestrictionsArgsDict",
    "IAMAuditConfigAuditLogConfigArgs",
    "IAMAuditConfigAuditLogConfigArgsDict",
    "IAMBindingConditionArgs",
    "IAMBindingConditionArgsDict",
    "IAMMemberConditionArgs",
    "IAMMemberConditionArgsDict",
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

class ApiKeyRestrictionsArgsDict(TypedDict):
    android_key_restrictions: NotRequired[
        pulumi.Input[ApiKeyRestrictionsAndroidKeyRestrictionsArgsDict]
    ]
    api_targets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ApiKeyRestrictionsApiTargetArgsDict]]]
    ]
    browser_key_restrictions: NotRequired[
        pulumi.Input[ApiKeyRestrictionsBrowserKeyRestrictionsArgsDict]
    ]
    ios_key_restrictions: NotRequired[
        pulumi.Input[ApiKeyRestrictionsIosKeyRestrictionsArgsDict]
    ]
    server_key_restrictions: NotRequired[
        pulumi.Input[ApiKeyRestrictionsServerKeyRestrictionsArgsDict]
    ]

@pulumi.input_type
class ApiKeyRestrictionsArgs:
    def __init__(
        __self__,
        *,
        android_key_restrictions: Optional[
            pulumi.Input[ApiKeyRestrictionsAndroidKeyRestrictionsArgs]
        ] = ...,
        api_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApiKeyRestrictionsApiTargetArgs]]]
        ] = ...,
        browser_key_restrictions: Optional[
            pulumi.Input[ApiKeyRestrictionsBrowserKeyRestrictionsArgs]
        ] = ...,
        ios_key_restrictions: Optional[
            pulumi.Input[ApiKeyRestrictionsIosKeyRestrictionsArgs]
        ] = ...,
        server_key_restrictions: Optional[
            pulumi.Input[ApiKeyRestrictionsServerKeyRestrictionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="androidKeyRestrictions")
    def android_key_restrictions(
        self,
    ) -> Optional[pulumi.Input[ApiKeyRestrictionsAndroidKeyRestrictionsArgs]]: ...
    @android_key_restrictions.setter
    def android_key_restrictions(
        self,
        value: Optional[pulumi.Input[ApiKeyRestrictionsAndroidKeyRestrictionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiTargets")
    def api_targets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApiKeyRestrictionsApiTargetArgs]]]
    ]: ...
    @api_targets.setter
    def api_targets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApiKeyRestrictionsApiTargetArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="browserKeyRestrictions")
    def browser_key_restrictions(
        self,
    ) -> Optional[pulumi.Input[ApiKeyRestrictionsBrowserKeyRestrictionsArgs]]: ...
    @browser_key_restrictions.setter
    def browser_key_restrictions(
        self,
        value: Optional[pulumi.Input[ApiKeyRestrictionsBrowserKeyRestrictionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="iosKeyRestrictions")
    def ios_key_restrictions(
        self,
    ) -> Optional[pulumi.Input[ApiKeyRestrictionsIosKeyRestrictionsArgs]]: ...
    @ios_key_restrictions.setter
    def ios_key_restrictions(
        self, value: Optional[pulumi.Input[ApiKeyRestrictionsIosKeyRestrictionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverKeyRestrictions")
    def server_key_restrictions(
        self,
    ) -> Optional[pulumi.Input[ApiKeyRestrictionsServerKeyRestrictionsArgs]]: ...
    @server_key_restrictions.setter
    def server_key_restrictions(
        self, value: Optional[pulumi.Input[ApiKeyRestrictionsServerKeyRestrictionsArgs]]
    ): ...

class ApiKeyRestrictionsAndroidKeyRestrictionsArgsDict(TypedDict):
    allowed_applications: pulumi.Input[
        Sequence[
            pulumi.Input[
                ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationArgsDict
            ]
        ]
    ]

@pulumi.input_type
class ApiKeyRestrictionsAndroidKeyRestrictionsArgs:
    def __init__(
        __self__,
        *,
        allowed_applications: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedApplications")
    def allowed_applications(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationArgs]
        ]
    ]: ...
    @allowed_applications.setter
    def allowed_applications(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationArgs
                ]
            ]
        ],
    ): ...

class ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationArgsDict(TypedDict):
    package_name: pulumi.Input[_builtins.str]
    sha1_fingerprint: pulumi.Input[_builtins.str]

@pulumi.input_type
class ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationArgs:
    def __init__(
        __self__,
        *,
        package_name: pulumi.Input[_builtins.str],
        sha1_fingerprint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> pulumi.Input[_builtins.str]: ...
    @package_name.setter
    def package_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> pulumi.Input[_builtins.str]: ...
    @sha1_fingerprint.setter
    def sha1_fingerprint(self, value: pulumi.Input[_builtins.str]): ...

class ApiKeyRestrictionsApiTargetArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ApiKeyRestrictionsApiTargetArgs:
    def __init__(
        __self__,
        *,
        service: pulumi.Input[_builtins.str],
        methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def methods(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @methods.setter
    def methods(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ApiKeyRestrictionsBrowserKeyRestrictionsArgsDict(TypedDict):
    allowed_referrers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ApiKeyRestrictionsBrowserKeyRestrictionsArgs:
    def __init__(
        __self__,
        *,
        allowed_referrers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedReferrers")
    def allowed_referrers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_referrers.setter
    def allowed_referrers(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ApiKeyRestrictionsIosKeyRestrictionsArgsDict(TypedDict):
    allowed_bundle_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ApiKeyRestrictionsIosKeyRestrictionsArgs:
    def __init__(
        __self__,
        *,
        allowed_bundle_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedBundleIds")
    def allowed_bundle_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_bundle_ids.setter
    def allowed_bundle_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ApiKeyRestrictionsServerKeyRestrictionsArgsDict(TypedDict):
    allowed_ips: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ApiKeyRestrictionsServerKeyRestrictionsArgs:
    def __init__(
        __self__, *, allowed_ips: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIps")
    def allowed_ips(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_ips.setter
    def allowed_ips(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class IAMAuditConfigAuditLogConfigArgsDict(TypedDict):
    log_type: pulumi.Input[_builtins.str]
    exempted_members: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class IAMAuditConfigAuditLogConfigArgs:
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

class OrganizationPolicyBooleanPolicyArgsDict(TypedDict):
    enforced: pulumi.Input[_builtins.bool]

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

@pulumi.input_type
class OrganizationPolicyRestorePolicyArgs:
    def __init__(__self__, *, default: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> pulumi.Input[_builtins.bool]: ...
    @default.setter
    def default(self, value: pulumi.Input[_builtins.bool]): ...
