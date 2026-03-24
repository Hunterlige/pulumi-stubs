

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationPortalOptionsArgs', 'ApplicationPortalOptionsArgsDict', 'ApplicationPortalOptionsSignInOptionsArgs', 'ApplicationPortalOptionsSignInOptionsArgsDict', ..., ..., ..., ..., ..., ..., 'InstanceAccessControlAttributesAttributeArgs', 'InstanceAccessControlAttributesAttributeArgsDict', 'InstanceAccessControlAttributesAttributeValueArgs', ..., 'ManagedPolicyAttachmentsExclusiveTimeoutsArgs', 'ManagedPolicyAttachmentsExclusiveTimeoutsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ...]
class ApplicationPortalOptionsArgsDict(TypedDict):
    sign_in_options: NotRequired[pulumi.Input[ApplicationPortalOptionsSignInOptionsArgsDict]]
    visibility: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationPortalOptionsArgs:
    def __init__(__self__, *, sign_in_options: Optional[pulumi.Input[ApplicationPortalOptionsSignInOptionsArgs]] = ..., visibility: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signInOptions")
    def sign_in_options(self) -> Optional[pulumi.Input[ApplicationPortalOptionsSignInOptionsArgs]]:
        
        ...
    
    @sign_in_options.setter
    def sign_in_options(self, value: Optional[pulumi.Input[ApplicationPortalOptionsSignInOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationPortalOptionsSignInOptionsArgsDict(TypedDict):
    origin: pulumi.Input[_builtins.str]
    application_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationPortalOptionsSignInOptionsArgs:
    def __init__(__self__, *, origin: pulumi.Input[_builtins.str], application_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @origin.setter
    def origin(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_url.setter
    def application_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceAccessControlAttributesAttributeArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[InstanceAccessControlAttributesAttributeValueArgsDict]]]


@pulumi.input_type
class InstanceAccessControlAttributesAttributeArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], values: pulumi.Input[Sequence[pulumi.Input[InstanceAccessControlAttributesAttributeValueArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[InstanceAccessControlAttributesAttributeValueArgs]]]:
        
        ...
    
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[InstanceAccessControlAttributesAttributeValueArgs]]]): # -> None:
        ...
    


class InstanceAccessControlAttributesAttributeValueArgsDict(TypedDict):
    sources: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class InstanceAccessControlAttributesAttributeValueArgs:
    def __init__(__self__, *, sources: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @sources.setter
    def sources(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ManagedPolicyAttachmentsExclusiveTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedPolicyAttachmentsExclusiveTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PermissionsBoundaryAttachmentPermissionsBoundaryArgsDict(TypedDict):
    customer_managed_policy_reference: NotRequired[pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceArgsDict]]
    managed_policy_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PermissionsBoundaryAttachmentPermissionsBoundaryArgs:
    def __init__(__self__, *, customer_managed_policy_reference: Optional[pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceArgs]] = ..., managed_policy_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedPolicyReference")
    def customer_managed_policy_reference(self) -> Optional[pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceArgs]]:
        
        ...
    
    @customer_managed_policy_reference.setter
    def customer_managed_policy_reference(self, value: Optional[pulumi.Input[PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArn")
    def managed_policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_policy_arn.setter
    def managed_policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TrustedTokenIssuerTrustedTokenIssuerConfigurationArgsDict(TypedDict):
    oidc_jwt_configuration: pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfigurationArgsDict]


@pulumi.input_type
class TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs:
    def __init__(__self__, *, oidc_jwt_configuration: pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfigurationArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcJwtConfiguration")
    def oidc_jwt_configuration(self) -> pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfigurationArgs]:
        
        ...
    
    @oidc_jwt_configuration.setter
    def oidc_jwt_configuration(self, value: pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfigurationArgs]): # -> None:
        ...
    


class TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfigurationArgsDict(TypedDict):
    claim_attribute_path: pulumi.Input[_builtins.str]
    identity_store_attribute_path: pulumi.Input[_builtins.str]
    issuer_url: pulumi.Input[_builtins.str]
    jwks_retrieval_option: pulumi.Input[_builtins.str]


@pulumi.input_type
class TrustedTokenIssuerTrustedTokenIssuerConfigurationOidcJwtConfigurationArgs:
    def __init__(__self__, *, claim_attribute_path: pulumi.Input[_builtins.str], identity_store_attribute_path: pulumi.Input[_builtins.str], issuer_url: pulumi.Input[_builtins.str], jwks_retrieval_option: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="claimAttributePath")
    def claim_attribute_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @claim_attribute_path.setter
    def claim_attribute_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreAttributePath")
    def identity_store_attribute_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_store_attribute_path.setter
    def identity_store_attribute_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer_url.setter
    def issuer_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwksRetrievalOption")
    def jwks_retrieval_option(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @jwks_retrieval_option.setter
    def jwks_retrieval_option(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GetPrincipalApplicationAssignmentsApplicationAssignmentArgsDict(TypedDict):
    application_arn: _builtins.str
    principal_id: _builtins.str
    principal_type: _builtins.str


@pulumi.input_type
class GetPrincipalApplicationAssignmentsApplicationAssignmentArgs:
    def __init__(__self__, *, application_arn: _builtins.str, principal_id: _builtins.str, principal_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> _builtins.str:
        
        ...
    
    @application_arn.setter
    def application_arn(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @principal_id.setter
    def principal_id(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str:
        
        ...
    
    @principal_type.setter
    def principal_type(self, value: _builtins.str): # -> None:
        ...
    


