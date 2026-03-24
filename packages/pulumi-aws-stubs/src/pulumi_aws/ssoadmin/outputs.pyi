import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationPortalOptions",
    "ApplicationPortalOptionsSignInOptions",
    ...,
    ...,
    "CustomerManagedPolicyAttachmentsExclusiveTimeouts",
    "InstanceAccessControlAttributesAttribute",
    "InstanceAccessControlAttributesAttributeValue",
    "ManagedPolicyAttachmentsExclusiveTimeouts",
    "PermissionsBoundaryAttachmentPermissionsBoundary",
    ...,
    "TrustedTokenIssuerTrustedTokenIssuerConfiguration",
    ...,
    ...,
    "GetApplicationPortalOptionResult",
    "GetApplicationPortalOptionSignInOptionResult",
    "GetApplicationProvidersApplicationProviderResult",
    ...,
    ...,
]

@pulumi.output_type
class ApplicationPortalOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sign_in_options: Optional[outputs.ApplicationPortalOptionsSignInOptions] = ...,
        visibility: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signInOptions")
    def sign_in_options(
        self,
    ) -> Optional[outputs.ApplicationPortalOptionsSignInOptions]: ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationPortalOptionsSignInOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        origin: _builtins.str,
        application_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomerManagedPolicyAttachmentCustomerManagedPolicyReference(dict):
    def __init__(
        __self__, *, name: _builtins.str, path: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReference(dict):
    def __init__(
        __self__, *, name: _builtins.str, path: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomerManagedPolicyAttachmentsExclusiveTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceAccessControlAttributesAttribute(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        values: Sequence[outputs.InstanceAccessControlAttributesAttributeValue],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Sequence[outputs.InstanceAccessControlAttributesAttributeValue]: ...

@pulumi.output_type
class InstanceAccessControlAttributesAttributeValue(dict):
    def __init__(__self__, *, sources: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ManagedPolicyAttachmentsExclusiveTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PermissionsBoundaryAttachmentPermissionsBoundary(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        customer_managed_policy_reference: Optional[
            outputs.PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference
        ] = ...,
        managed_policy_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedPolicyReference")
    def customer_managed_policy_reference(
        self,
    ) -> Optional[
        outputs.PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference
    ]: ...
    @_builtins.property
    @pulumi.getter(name="managedPolicyArn")
    def managed_policy_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference(
    dict
):
    def __init__(
        __self__, *, name: _builtins.str, path: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrustedTokenIssuerTrustedTokenIssuerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oidc_jwt_configuration: outputs.TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfiguration,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oidcJwtConfiguration")
    def oidc_jwt_configuration(
        self,
    ) -> (
        outputs.TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfiguration
    ): ...

@pulumi.output_type
class TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        claim_attribute_path: _builtins.str,
        identity_store_attribute_path: _builtins.str,
        issuer_url: _builtins.str,
        jwks_retrieval_option: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="claimAttributePath")
    def claim_attribute_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityStoreAttributePath")
    def identity_store_attribute_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jwksRetrievalOption")
    def jwks_retrieval_option(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationAssignmentsApplicationAssignmentResult(dict):
    def __init__(
        __self__,
        *,
        application_arn: _builtins.str,
        principal_id: _builtins.str,
        principal_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationPortalOptionResult(dict):
    def __init__(
        __self__,
        *,
        sign_in_options: Sequence[outputs.GetApplicationPortalOptionSignInOptionResult],
        visibility: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signInOptions")
    def sign_in_options(
        self,
    ) -> Sequence[outputs.GetApplicationPortalOptionSignInOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationPortalOptionSignInOptionResult(dict):
    def __init__(
        __self__, *, application_url: _builtins.str, origin: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationProvidersApplicationProviderResult(dict):
    def __init__(
        __self__,
        *,
        application_provider_arn: _builtins.str,
        display_datas: Sequence[
            outputs.GetApplicationProvidersApplicationProviderDisplayDataResult
        ],
        federation_protocol: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationProviderArn")
    def application_provider_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayDatas")
    def display_datas(
        self,
    ) -> Sequence[
        outputs.GetApplicationProvidersApplicationProviderDisplayDataResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="federationProtocol")
    def federation_protocol(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationProvidersApplicationProviderDisplayDataResult(dict):
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        display_name: _builtins.str,
        icon_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> _builtins.str: ...

@pulumi.output_type
class GetPrincipalApplicationAssignmentsApplicationAssignmentResult(dict):
    def __init__(
        __self__,
        *,
        application_arn: _builtins.str,
        principal_id: _builtins.str,
        principal_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str: ...
