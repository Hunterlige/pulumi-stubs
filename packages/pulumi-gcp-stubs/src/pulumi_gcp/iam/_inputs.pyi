import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessBoundaryPolicyRuleArgs",
    "AccessBoundaryPolicyRuleArgsDict",
    "AccessBoundaryPolicyRuleAccessBoundaryRuleArgs",
    "AccessBoundaryPolicyRuleAccessBoundaryRuleArgsDict",
    ...,
    ...,
    "DenyPolicyRuleArgs",
    "DenyPolicyRuleArgsDict",
    "DenyPolicyRuleDenyRuleArgs",
    "DenyPolicyRuleDenyRuleArgsDict",
    "DenyPolicyRuleDenyRuleDenialConditionArgs",
    "DenyPolicyRuleDenyRuleDenialConditionArgsDict",
    "FoldersPolicyBindingConditionArgs",
    "FoldersPolicyBindingConditionArgsDict",
    "FoldersPolicyBindingTargetArgs",
    "FoldersPolicyBindingTargetArgsDict",
    "OrganizationsPolicyBindingConditionArgs",
    "OrganizationsPolicyBindingConditionArgsDict",
    "OrganizationsPolicyBindingTargetArgs",
    "OrganizationsPolicyBindingTargetArgsDict",
    "PrincipalAccessBoundaryPolicyDetailsArgs",
    "PrincipalAccessBoundaryPolicyDetailsArgsDict",
    "PrincipalAccessBoundaryPolicyDetailsRuleArgs",
    "PrincipalAccessBoundaryPolicyDetailsRuleArgsDict",
    "ProjectsPolicyBindingConditionArgs",
    "ProjectsPolicyBindingConditionArgsDict",
    "ProjectsPolicyBindingTargetArgs",
    "ProjectsPolicyBindingTargetArgsDict",
    "WorkforcePoolAccessRestrictionsArgs",
    "WorkforcePoolAccessRestrictionsArgsDict",
    "WorkforcePoolAccessRestrictionsAllowedServiceArgs",
    ...,
    "WorkforcePoolIamBindingConditionArgs",
    "WorkforcePoolIamBindingConditionArgsDict",
    "WorkforcePoolIamMemberConditionArgs",
    "WorkforcePoolIamMemberConditionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkforcePoolProviderKeyKeyDataArgs",
    "WorkforcePoolProviderKeyKeyDataArgsDict",
    "WorkforcePoolProviderOidcArgs",
    "WorkforcePoolProviderOidcArgsDict",
    "WorkforcePoolProviderOidcClientSecretArgs",
    "WorkforcePoolProviderOidcClientSecretArgsDict",
    "WorkforcePoolProviderOidcClientSecretValueArgs",
    "WorkforcePoolProviderOidcClientSecretValueArgsDict",
    "WorkforcePoolProviderOidcWebSsoConfigArgs",
    "WorkforcePoolProviderOidcWebSsoConfigArgsDict",
    "WorkforcePoolProviderSamlArgs",
    "WorkforcePoolProviderSamlArgsDict",
    "WorkloadIdentityPoolIamBindingConditionArgs",
    "WorkloadIdentityPoolIamBindingConditionArgsDict",
    "WorkloadIdentityPoolIamMemberConditionArgs",
    "WorkloadIdentityPoolIamMemberConditionArgsDict",
    ...,
    ...,
    "WorkloadIdentityPoolInlineTrustConfigArgs",
    "WorkloadIdentityPoolInlineTrustConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkloadIdentityPoolNamespaceOwnerServiceArgs",
    "WorkloadIdentityPoolNamespaceOwnerServiceArgsDict",
    "WorkloadIdentityPoolProviderAwsArgs",
    "WorkloadIdentityPoolProviderAwsArgsDict",
    "WorkloadIdentityPoolProviderOidcArgs",
    "WorkloadIdentityPoolProviderOidcArgsDict",
    "WorkloadIdentityPoolProviderSamlArgs",
    "WorkloadIdentityPoolProviderSamlArgsDict",
    "WorkloadIdentityPoolProviderX509Args",
    "WorkloadIdentityPoolProviderX509ArgsDict",
    "WorkloadIdentityPoolProviderX509TrustStoreArgs",
    "WorkloadIdentityPoolProviderX509TrustStoreArgsDict",
    ...,
    ...,
    ...,
    ...,
]

class AccessBoundaryPolicyRuleArgsDict(TypedDict):
    access_boundary_rule: NotRequired[
        pulumi.Input[AccessBoundaryPolicyRuleAccessBoundaryRuleArgsDict]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessBoundaryPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        access_boundary_rule: Optional[
            pulumi.Input[AccessBoundaryPolicyRuleAccessBoundaryRuleArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessBoundaryRule")
    def access_boundary_rule(
        self,
    ) -> Optional[pulumi.Input[AccessBoundaryPolicyRuleAccessBoundaryRuleArgs]]: ...
    @access_boundary_rule.setter
    def access_boundary_rule(
        self,
        value: Optional[pulumi.Input[AccessBoundaryPolicyRuleAccessBoundaryRuleArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessBoundaryPolicyRuleAccessBoundaryRuleArgsDict(TypedDict):
    availability_condition: NotRequired[
        pulumi.Input[
            AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityConditionArgsDict
        ]
    ]
    available_permissions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    available_resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessBoundaryPolicyRuleAccessBoundaryRuleArgs:
    def __init__(
        __self__,
        *,
        availability_condition: Optional[
            pulumi.Input[
                AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityConditionArgs
            ]
        ] = ...,
        available_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        available_resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityCondition")
    def availability_condition(
        self,
    ) -> Optional[
        pulumi.Input[
            AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityConditionArgs
        ]
    ]: ...
    @availability_condition.setter
    def availability_condition(
        self,
        value: Optional[
            pulumi.Input[
                AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityConditionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="availablePermissions")
    def available_permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @available_permissions.setter
    def available_permissions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availableResource")
    def available_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @available_resource.setter
    def available_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityConditionArgsDict(
    TypedDict
):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DenyPolicyRuleArgsDict(TypedDict):
    deny_rule: NotRequired[pulumi.Input[DenyPolicyRuleDenyRuleArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DenyPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        deny_rule: Optional[pulumi.Input[DenyPolicyRuleDenyRuleArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="denyRule")
    def deny_rule(self) -> Optional[pulumi.Input[DenyPolicyRuleDenyRuleArgs]]: ...
    @deny_rule.setter
    def deny_rule(self, value: Optional[pulumi.Input[DenyPolicyRuleDenyRuleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DenyPolicyRuleDenyRuleArgsDict(TypedDict):
    denial_condition: NotRequired[
        pulumi.Input[DenyPolicyRuleDenyRuleDenialConditionArgsDict]
    ]
    denied_permissions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    denied_principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exception_permissions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    exception_principals: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DenyPolicyRuleDenyRuleArgs:
    def __init__(
        __self__,
        *,
        denial_condition: Optional[
            pulumi.Input[DenyPolicyRuleDenyRuleDenialConditionArgs]
        ] = ...,
        denied_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        denied_principals: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        exception_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        exception_principals: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="denialCondition")
    def denial_condition(
        self,
    ) -> Optional[pulumi.Input[DenyPolicyRuleDenyRuleDenialConditionArgs]]: ...
    @denial_condition.setter
    def denial_condition(
        self, value: Optional[pulumi.Input[DenyPolicyRuleDenyRuleDenialConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deniedPermissions")
    def denied_permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @denied_permissions.setter
    def denied_permissions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deniedPrincipals")
    def denied_principals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @denied_principals.setter
    def denied_principals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exceptionPermissions")
    def exception_permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exception_permissions.setter
    def exception_permissions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exceptionPrincipals")
    def exception_principals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exception_principals.setter
    def exception_principals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DenyPolicyRuleDenyRuleDenialConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DenyPolicyRuleDenyRuleDenialConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FoldersPolicyBindingConditionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FoldersPolicyBindingConditionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FoldersPolicyBindingTargetArgsDict(TypedDict):
    principal_set: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FoldersPolicyBindingTargetArgs:
    def __init__(
        __self__, *, principal_set: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalSet")
    def principal_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_set.setter
    def principal_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OrganizationsPolicyBindingConditionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OrganizationsPolicyBindingConditionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OrganizationsPolicyBindingTargetArgsDict(TypedDict):
    principal_set: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OrganizationsPolicyBindingTargetArgs:
    def __init__(
        __self__, *, principal_set: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalSet")
    def principal_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_set.setter
    def principal_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrincipalAccessBoundaryPolicyDetailsArgsDict(TypedDict):
    rules: pulumi.Input[
        Sequence[pulumi.Input[PrincipalAccessBoundaryPolicyDetailsRuleArgsDict]]
    ]
    enforcement_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrincipalAccessBoundaryPolicyDetailsArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[
            Sequence[pulumi.Input[PrincipalAccessBoundaryPolicyDetailsRuleArgs]]
        ],
        enforcement_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[PrincipalAccessBoundaryPolicyDetailsRuleArgs]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[PrincipalAccessBoundaryPolicyDetailsRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enforcementVersion")
    def enforcement_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enforcement_version.setter
    def enforcement_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrincipalAccessBoundaryPolicyDetailsRuleArgsDict(TypedDict):
    effect: pulumi.Input[_builtins.str]
    resources: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrincipalAccessBoundaryPolicyDetailsRuleArgs:
    def __init__(
        __self__,
        *,
        effect: pulumi.Input[_builtins.str],
        resources: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> pulumi.Input[_builtins.str]: ...
    @effect.setter
    def effect(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @resources.setter
    def resources(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectsPolicyBindingConditionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectsPolicyBindingConditionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectsPolicyBindingTargetArgsDict(TypedDict):
    principal_set: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectsPolicyBindingTargetArgs:
    def __init__(
        __self__, *, principal_set: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalSet")
    def principal_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_set.setter
    def principal_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkforcePoolAccessRestrictionsArgsDict(TypedDict):
    allowed_services: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[WorkforcePoolAccessRestrictionsAllowedServiceArgsDict]
            ]
        ]
    ]
    disable_programmatic_signin: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WorkforcePoolAccessRestrictionsArgs:
    def __init__(
        __self__,
        *,
        allowed_services: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[WorkforcePoolAccessRestrictionsAllowedServiceArgs]
                ]
            ]
        ] = ...,
        disable_programmatic_signin: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[WorkforcePoolAccessRestrictionsAllowedServiceArgs]]
        ]
    ]: ...
    @allowed_services.setter
    def allowed_services(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[WorkforcePoolAccessRestrictionsAllowedServiceArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableProgrammaticSignin")
    def disable_programmatic_signin(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_programmatic_signin.setter
    def disable_programmatic_signin(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class WorkforcePoolAccessRestrictionsAllowedServiceArgsDict(TypedDict):
    domain: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolAccessRestrictionsAllowedServiceArgs:
    def __init__(
        __self__, *, domain: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkforcePoolIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolIamBindingConditionArgs:
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

class WorkforcePoolIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolIamMemberConditionArgs:
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

class WorkforcePoolProviderExtendedAttributesOauth2ClientArgsDict(TypedDict):
    attributes_type: pulumi.Input[_builtins.str]
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[
        WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretArgsDict
    ]
    issuer_uri: pulumi.Input[_builtins.str]
    query_parameters: NotRequired[
        pulumi.Input[
            WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParametersArgsDict
        ]
    ]

@pulumi.input_type
class WorkforcePoolProviderExtendedAttributesOauth2ClientArgs:
    def __init__(
        __self__,
        *,
        attributes_type: pulumi.Input[_builtins.str],
        client_id: pulumi.Input[_builtins.str],
        client_secret: pulumi.Input[
            WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretArgs
        ],
        issuer_uri: pulumi.Input[_builtins.str],
        query_parameters: Optional[
            pulumi.Input[
                WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParametersArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributesType")
    def attributes_type(self) -> pulumi.Input[_builtins.str]: ...
    @attributes_type.setter
    def attributes_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> pulumi.Input[
        WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretArgs
    ]: ...
    @client_secret.setter
    def client_secret(
        self,
        value: pulumi.Input[
            WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> pulumi.Input[_builtins.str]: ...
    @issuer_uri.setter
    def issuer_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParametersArgs
        ]
    ]: ...
    @query_parameters.setter
    def query_parameters(
        self,
        value: Optional[
            pulumi.Input[
                WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParametersArgs
            ]
        ],
    ): ...

class WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretArgsDict(
    TypedDict
):
    value: NotRequired[
        pulumi.Input[
            WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValueArgsDict
        ]
    ]

@pulumi.input_type
class WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretArgs:
    def __init__(
        __self__,
        *,
        value: Optional[
            pulumi.Input[
                WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValueArgs
        ]
    ]: ...
    @value.setter
    def value(
        self,
        value: Optional[
            pulumi.Input[
                WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValueArgs
            ]
        ],
    ): ...

class WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValueArgsDict(
    TypedDict
):
    plain_text: pulumi.Input[_builtins.str]
    thumbprint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValueArgs:
    def __init__(
        __self__,
        *,
        plain_text: pulumi.Input[_builtins.str],
        thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="plainText")
    def plain_text(self) -> pulumi.Input[_builtins.str]: ...
    @plain_text.setter
    def plain_text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParametersArgsDict(
    TypedDict
):
    filter: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParametersArgs:
    def __init__(
        __self__, *, filter: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkforcePoolProviderExtraAttributesOauth2ClientArgsDict(TypedDict):
    attributes_type: pulumi.Input[_builtins.str]
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[
        WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretArgsDict
    ]
    issuer_uri: pulumi.Input[_builtins.str]
    query_parameters: NotRequired[
        pulumi.Input[
            WorkforcePoolProviderExtraAttributesOauth2ClientQueryParametersArgsDict
        ]
    ]

@pulumi.input_type
class WorkforcePoolProviderExtraAttributesOauth2ClientArgs:
    def __init__(
        __self__,
        *,
        attributes_type: pulumi.Input[_builtins.str],
        client_id: pulumi.Input[_builtins.str],
        client_secret: pulumi.Input[
            WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretArgs
        ],
        issuer_uri: pulumi.Input[_builtins.str],
        query_parameters: Optional[
            pulumi.Input[
                WorkforcePoolProviderExtraAttributesOauth2ClientQueryParametersArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributesType")
    def attributes_type(self) -> pulumi.Input[_builtins.str]: ...
    @attributes_type.setter
    def attributes_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> pulumi.Input[
        WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretArgs
    ]: ...
    @client_secret.setter
    def client_secret(
        self,
        value: pulumi.Input[
            WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> pulumi.Input[_builtins.str]: ...
    @issuer_uri.setter
    def issuer_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkforcePoolProviderExtraAttributesOauth2ClientQueryParametersArgs
        ]
    ]: ...
    @query_parameters.setter
    def query_parameters(
        self,
        value: Optional[
            pulumi.Input[
                WorkforcePoolProviderExtraAttributesOauth2ClientQueryParametersArgs
            ]
        ],
    ): ...

class WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretArgsDict(TypedDict):
    value: NotRequired[
        pulumi.Input[
            WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValueArgsDict
        ]
    ]

@pulumi.input_type
class WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretArgs:
    def __init__(
        __self__,
        *,
        value: Optional[
            pulumi.Input[
                WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValueArgs
        ]
    ]: ...
    @value.setter
    def value(
        self,
        value: Optional[
            pulumi.Input[
                WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValueArgs
            ]
        ],
    ): ...

class WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValueArgsDict(
    TypedDict
):
    plain_text: pulumi.Input[_builtins.str]
    thumbprint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValueArgs:
    def __init__(
        __self__,
        *,
        plain_text: pulumi.Input[_builtins.str],
        thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="plainText")
    def plain_text(self) -> pulumi.Input[_builtins.str]: ...
    @plain_text.setter
    def plain_text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkforcePoolProviderExtraAttributesOauth2ClientQueryParametersArgsDict(
    TypedDict
):
    filter: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolProviderExtraAttributesOauth2ClientQueryParametersArgs:
    def __init__(
        __self__, *, filter: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkforcePoolProviderKeyKeyDataArgsDict(TypedDict):
    key_spec: pulumi.Input[_builtins.str]
    format: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    not_after_time: NotRequired[pulumi.Input[_builtins.str]]
    not_before_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolProviderKeyKeyDataArgs:
    def __init__(
        __self__,
        *,
        key_spec: pulumi.Input[_builtins.str],
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        not_after_time: Optional[pulumi.Input[_builtins.str]] = ...,
        not_before_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> pulumi.Input[_builtins.str]: ...
    @key_spec.setter
    def key_spec(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notAfterTime")
    def not_after_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_after_time.setter
    def not_after_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notBeforeTime")
    def not_before_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_before_time.setter
    def not_before_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkforcePoolProviderOidcArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    issuer_uri: pulumi.Input[_builtins.str]
    client_secret: NotRequired[
        pulumi.Input[WorkforcePoolProviderOidcClientSecretArgsDict]
    ]
    jwks_json: NotRequired[pulumi.Input[_builtins.str]]
    web_sso_config: NotRequired[
        pulumi.Input[WorkforcePoolProviderOidcWebSsoConfigArgsDict]
    ]

@pulumi.input_type
class WorkforcePoolProviderOidcArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        issuer_uri: pulumi.Input[_builtins.str],
        client_secret: Optional[
            pulumi.Input[WorkforcePoolProviderOidcClientSecretArgs]
        ] = ...,
        jwks_json: Optional[pulumi.Input[_builtins.str]] = ...,
        web_sso_config: Optional[
            pulumi.Input[WorkforcePoolProviderOidcWebSsoConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> pulumi.Input[_builtins.str]: ...
    @issuer_uri.setter
    def issuer_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> Optional[pulumi.Input[WorkforcePoolProviderOidcClientSecretArgs]]: ...
    @client_secret.setter
    def client_secret(
        self, value: Optional[pulumi.Input[WorkforcePoolProviderOidcClientSecretArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jwksJson")
    def jwks_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @jwks_json.setter
    def jwks_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webSsoConfig")
    def web_sso_config(
        self,
    ) -> Optional[pulumi.Input[WorkforcePoolProviderOidcWebSsoConfigArgs]]: ...
    @web_sso_config.setter
    def web_sso_config(
        self, value: Optional[pulumi.Input[WorkforcePoolProviderOidcWebSsoConfigArgs]]
    ): ...

class WorkforcePoolProviderOidcClientSecretArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[WorkforcePoolProviderOidcClientSecretValueArgsDict]]

@pulumi.input_type
class WorkforcePoolProviderOidcClientSecretArgs:
    def __init__(
        __self__,
        *,
        value: Optional[
            pulumi.Input[WorkforcePoolProviderOidcClientSecretValueArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[pulumi.Input[WorkforcePoolProviderOidcClientSecretValueArgs]]: ...
    @value.setter
    def value(
        self,
        value: Optional[pulumi.Input[WorkforcePoolProviderOidcClientSecretValueArgs]],
    ): ...

class WorkforcePoolProviderOidcClientSecretValueArgsDict(TypedDict):
    plain_text: pulumi.Input[_builtins.str]
    thumbprint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkforcePoolProviderOidcClientSecretValueArgs:
    def __init__(
        __self__,
        *,
        plain_text: pulumi.Input[_builtins.str],
        thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="plainText")
    def plain_text(self) -> pulumi.Input[_builtins.str]: ...
    @plain_text.setter
    def plain_text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkforcePoolProviderOidcWebSsoConfigArgsDict(TypedDict):
    assertion_claims_behavior: pulumi.Input[_builtins.str]
    response_type: pulumi.Input[_builtins.str]
    additional_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkforcePoolProviderOidcWebSsoConfigArgs:
    def __init__(
        __self__,
        *,
        assertion_claims_behavior: pulumi.Input[_builtins.str],
        response_type: pulumi.Input[_builtins.str],
        additional_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assertionClaimsBehavior")
    def assertion_claims_behavior(self) -> pulumi.Input[_builtins.str]: ...
    @assertion_claims_behavior.setter
    def assertion_claims_behavior(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> pulumi.Input[_builtins.str]: ...
    @response_type.setter
    def response_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalScopes")
    def additional_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_scopes.setter
    def additional_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WorkforcePoolProviderSamlArgsDict(TypedDict):
    idp_metadata_xml: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkforcePoolProviderSamlArgs:
    def __init__(
        __self__, *, idp_metadata_xml: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idpMetadataXml")
    def idp_metadata_xml(self) -> pulumi.Input[_builtins.str]: ...
    @idp_metadata_xml.setter
    def idp_metadata_xml(self, value: pulumi.Input[_builtins.str]): ...

class WorkloadIdentityPoolIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadIdentityPoolIamBindingConditionArgs:
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

class WorkloadIdentityPoolIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadIdentityPoolIamMemberConditionArgs:
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

class WorkloadIdentityPoolInlineCertificateIssuanceConfigArgsDict(TypedDict):
    ca_pools: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    key_algorithm: NotRequired[pulumi.Input[_builtins.str]]
    lifetime: NotRequired[pulumi.Input[_builtins.str]]
    rotation_window_percentage: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs:
    def __init__(
        __self__,
        *,
        ca_pools: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        key_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        lifetime: Optional[pulumi.Input[_builtins.str]] = ...,
        rotation_window_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caPools")
    def ca_pools(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @ca_pools.setter
    def ca_pools(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_algorithm.setter
    def key_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifetime.setter
    def lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rotationWindowPercentage")
    def rotation_window_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rotation_window_percentage.setter
    def rotation_window_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class WorkloadIdentityPoolInlineTrustConfigArgsDict(TypedDict):
    additional_trust_bundles: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class WorkloadIdentityPoolInlineTrustConfigArgs:
    def __init__(
        __self__,
        *,
        additional_trust_bundles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalTrustBundles")
    def additional_trust_bundles(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleArgs
                ]
            ]
        ]
    ]: ...
    @additional_trust_bundles.setter
    def additional_trust_bundles(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleArgs
                    ]
                ]
            ]
        ],
    ): ...

class WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleArgsDict(TypedDict):
    trust_anchors: pulumi.Input[
        Sequence[
            pulumi.Input[
                WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorArgsDict
            ]
        ]
    ]
    trust_domain: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleArgs:
    def __init__(
        __self__,
        *,
        trust_anchors: pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorArgs
                ]
            ]
        ],
        trust_domain: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trustAnchors")
    def trust_anchors(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorArgs
            ]
        ]
    ]: ...
    @trust_anchors.setter
    def trust_anchors(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustDomain")
    def trust_domain(self) -> pulumi.Input[_builtins.str]: ...
    @trust_domain.setter
    def trust_domain(self, value: pulumi.Input[_builtins.str]): ...

class WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorArgsDict(
    TypedDict
):
    pem_certificate: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorArgs:
    def __init__(__self__, *, pem_certificate: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> pulumi.Input[_builtins.str]: ...
    @pem_certificate.setter
    def pem_certificate(self, value: pulumi.Input[_builtins.str]): ...

class WorkloadIdentityPoolManagedIdentityAttestationRuleArgsDict(TypedDict):
    google_cloud_resource: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkloadIdentityPoolManagedIdentityAttestationRuleArgs:
    def __init__(
        __self__, *, google_cloud_resource: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="googleCloudResource")
    def google_cloud_resource(self) -> pulumi.Input[_builtins.str]: ...
    @google_cloud_resource.setter
    def google_cloud_resource(self, value: pulumi.Input[_builtins.str]): ...

class WorkloadIdentityPoolNamespaceOwnerServiceArgsDict(TypedDict):
    principal_subject: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadIdentityPoolNamespaceOwnerServiceArgs:
    def __init__(
        __self__, *, principal_subject: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalSubject")
    def principal_subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_subject.setter
    def principal_subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkloadIdentityPoolProviderAwsArgsDict(TypedDict):
    account_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkloadIdentityPoolProviderAwsArgs:
    def __init__(__self__, *, account_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]: ...
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): ...

class WorkloadIdentityPoolProviderOidcArgsDict(TypedDict):
    issuer_uri: pulumi.Input[_builtins.str]
    allowed_audiences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jwks_json: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadIdentityPoolProviderOidcArgs:
    def __init__(
        __self__,
        *,
        issuer_uri: pulumi.Input[_builtins.str],
        allowed_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        jwks_json: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> pulumi.Input[_builtins.str]: ...
    @issuer_uri.setter
    def issuer_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_audiences.setter
    def allowed_audiences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jwksJson")
    def jwks_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @jwks_json.setter
    def jwks_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkloadIdentityPoolProviderSamlArgsDict(TypedDict):
    idp_metadata_xml: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkloadIdentityPoolProviderSamlArgs:
    def __init__(
        __self__, *, idp_metadata_xml: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idpMetadataXml")
    def idp_metadata_xml(self) -> pulumi.Input[_builtins.str]: ...
    @idp_metadata_xml.setter
    def idp_metadata_xml(self, value: pulumi.Input[_builtins.str]): ...

class WorkloadIdentityPoolProviderX509ArgsDict(TypedDict):
    trust_store: pulumi.Input[WorkloadIdentityPoolProviderX509TrustStoreArgsDict]

@pulumi.input_type
class WorkloadIdentityPoolProviderX509Args:
    def __init__(
        __self__,
        *,
        trust_store: pulumi.Input[WorkloadIdentityPoolProviderX509TrustStoreArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trustStore")
    def trust_store(
        self,
    ) -> pulumi.Input[WorkloadIdentityPoolProviderX509TrustStoreArgs]: ...
    @trust_store.setter
    def trust_store(
        self, value: pulumi.Input[WorkloadIdentityPoolProviderX509TrustStoreArgs]
    ): ...

class WorkloadIdentityPoolProviderX509TrustStoreArgsDict(TypedDict):
    trust_anchors: pulumi.Input[
        Sequence[
            pulumi.Input[WorkloadIdentityPoolProviderX509TrustStoreTrustAnchorArgsDict]
        ]
    ]
    intermediate_cas: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkloadIdentityPoolProviderX509TrustStoreIntermediateCaArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class WorkloadIdentityPoolProviderX509TrustStoreArgs:
    def __init__(
        __self__,
        *,
        trust_anchors: pulumi.Input[
            Sequence[
                pulumi.Input[WorkloadIdentityPoolProviderX509TrustStoreTrustAnchorArgs]
            ]
        ],
        intermediate_cas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkloadIdentityPoolProviderX509TrustStoreIntermediateCaArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trustAnchors")
    def trust_anchors(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[WorkloadIdentityPoolProviderX509TrustStoreTrustAnchorArgs]
        ]
    ]: ...
    @trust_anchors.setter
    def trust_anchors(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[WorkloadIdentityPoolProviderX509TrustStoreTrustAnchorArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="intermediateCas")
    def intermediate_cas(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkloadIdentityPoolProviderX509TrustStoreIntermediateCaArgs
                ]
            ]
        ]
    ]: ...
    @intermediate_cas.setter
    def intermediate_cas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkloadIdentityPoolProviderX509TrustStoreIntermediateCaArgs
                    ]
                ]
            ]
        ],
    ): ...

class WorkloadIdentityPoolProviderX509TrustStoreIntermediateCaArgsDict(TypedDict):
    pem_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadIdentityPoolProviderX509TrustStoreIntermediateCaArgs:
    def __init__(
        __self__, *, pem_certificate: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_certificate.setter
    def pem_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkloadIdentityPoolProviderX509TrustStoreTrustAnchorArgsDict(TypedDict):
    pem_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadIdentityPoolProviderX509TrustStoreTrustAnchorArgs:
    def __init__(
        __self__, *, pem_certificate: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_certificate.setter
    def pem_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
