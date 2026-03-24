

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessBoundaryPolicyRule', 'AccessBoundaryPolicyRuleAccessBoundaryRule', ..., 'DenyPolicyRule', 'DenyPolicyRuleDenyRule', 'DenyPolicyRuleDenyRuleDenialCondition', 'FoldersPolicyBindingCondition', 'FoldersPolicyBindingTarget', 'OrganizationsPolicyBindingCondition', 'OrganizationsPolicyBindingTarget', 'PrincipalAccessBoundaryPolicyDetails', 'PrincipalAccessBoundaryPolicyDetailsRule', 'ProjectsPolicyBindingCondition', 'ProjectsPolicyBindingTarget', 'WorkforcePoolAccessRestrictions', 'WorkforcePoolAccessRestrictionsAllowedService', 'WorkforcePoolIamBindingCondition', 'WorkforcePoolIamMemberCondition', ..., ..., ..., ..., 'WorkforcePoolProviderExtraAttributesOauth2Client', ..., ..., ..., 'WorkforcePoolProviderKeyKeyData', 'WorkforcePoolProviderOidc', 'WorkforcePoolProviderOidcClientSecret', 'WorkforcePoolProviderOidcClientSecretValue', 'WorkforcePoolProviderOidcWebSsoConfig', 'WorkforcePoolProviderSaml', 'WorkloadIdentityPoolIamBindingCondition', 'WorkloadIdentityPoolIamMemberCondition', ..., 'WorkloadIdentityPoolInlineTrustConfig', ..., ..., 'WorkloadIdentityPoolManagedIdentityAttestationRule', 'WorkloadIdentityPoolNamespaceOwnerService', 'WorkloadIdentityPoolProviderAws', 'WorkloadIdentityPoolProviderOidc', 'WorkloadIdentityPoolProviderSaml', 'WorkloadIdentityPoolProviderX509', 'WorkloadIdentityPoolProviderX509TrustStore', ..., ..., 'GetTestablePermissionsPermissionResult', ..., 'GetWorkloadIdentityPoolInlineTrustConfigResult', ..., ..., 'GetWorkloadIdentityPoolProviderAwResult', 'GetWorkloadIdentityPoolProviderOidcResult', 'GetWorkloadIdentityPoolProviderSamlResult', 'GetWorkloadIdentityPoolProviderX509Result', ..., ..., ...]
@pulumi.output_type
class AccessBoundaryPolicyRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_boundary_rule: Optional[outputs.AccessBoundaryPolicyRuleAccessBoundaryRule] = ..., description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessBoundaryRule")
    def access_boundary_rule(self) -> Optional[outputs.AccessBoundaryPolicyRuleAccessBoundaryRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AccessBoundaryPolicyRuleAccessBoundaryRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_condition: Optional[outputs.AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityCondition] = ..., available_permissions: Optional[Sequence[_builtins.str]] = ..., available_resource: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityCondition")
    def availability_condition(self) -> Optional[outputs.AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availablePermissions")
    def available_permissions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableResource")
    def available_resource(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AccessBoundaryPolicyRuleAccessBoundaryRuleAvailabilityCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DenyPolicyRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deny_rule: Optional[outputs.DenyPolicyRuleDenyRule] = ..., description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyRule")
    def deny_rule(self) -> Optional[outputs.DenyPolicyRuleDenyRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DenyPolicyRuleDenyRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, denial_condition: Optional[outputs.DenyPolicyRuleDenyRuleDenialCondition] = ..., denied_permissions: Optional[Sequence[_builtins.str]] = ..., denied_principals: Optional[Sequence[_builtins.str]] = ..., exception_permissions: Optional[Sequence[_builtins.str]] = ..., exception_principals: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denialCondition")
    def denial_condition(self) -> Optional[outputs.DenyPolicyRuleDenyRuleDenialCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedPermissions")
    def denied_permissions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedPrincipals")
    def denied_principals(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionPermissions")
    def exception_permissions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionPrincipals")
    def exception_principals(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DenyPolicyRuleDenyRuleDenialCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FoldersPolicyBindingCondition(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., expression: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FoldersPolicyBindingTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_set: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalSet")
    def principal_set(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OrganizationsPolicyBindingCondition(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., expression: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OrganizationsPolicyBindingTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_set: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalSet")
    def principal_set(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrincipalAccessBoundaryPolicyDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rules: Sequence[outputs.PrincipalAccessBoundaryPolicyDetailsRule], enforcement_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.PrincipalAccessBoundaryPolicyDetailsRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforcementVersion")
    def enforcement_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrincipalAccessBoundaryPolicyDetailsRule(dict):
    def __init__(__self__, *, effect: _builtins.str, resources: Sequence[_builtins.str], description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProjectsPolicyBindingCondition(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., expression: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProjectsPolicyBindingTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_set: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalSet")
    def principal_set(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolAccessRestrictions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_services: Optional[Sequence[outputs.WorkforcePoolAccessRestrictionsAllowedService]] = ..., disable_programmatic_signin: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedServices")
    def allowed_services(self) -> Optional[Sequence[outputs.WorkforcePoolAccessRestrictionsAllowedService]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableProgrammaticSignin")
    def disable_programmatic_signin(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolAccessRestrictionsAllowedService(dict):
    def __init__(__self__, *, domain: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class WorkforcePoolIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class WorkforcePoolProviderExtendedAttributesOauth2Client(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attributes_type: _builtins.str, client_id: _builtins.str, client_secret: outputs.WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecret, issuer_uri: _builtins.str, query_parameters: Optional[outputs.WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParameters] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributesType")
    def attributes_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> outputs.WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecret:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[outputs.WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParameters]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecret(dict):
    def __init__(__self__, *, value: Optional[outputs.WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValue]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderExtendedAttributesOauth2ClientClientSecretValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, plain_text: _builtins.str, thumbprint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainText")
    def plain_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderExtendedAttributesOauth2ClientQueryParameters(dict):
    def __init__(__self__, *, filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderExtraAttributesOauth2Client(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attributes_type: _builtins.str, client_id: _builtins.str, client_secret: outputs.WorkforcePoolProviderExtraAttributesOauth2ClientClientSecret, issuer_uri: _builtins.str, query_parameters: Optional[outputs.WorkforcePoolProviderExtraAttributesOauth2ClientQueryParameters] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributesType")
    def attributes_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> outputs.WorkforcePoolProviderExtraAttributesOauth2ClientClientSecret:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[outputs.WorkforcePoolProviderExtraAttributesOauth2ClientQueryParameters]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderExtraAttributesOauth2ClientClientSecret(dict):
    def __init__(__self__, *, value: Optional[outputs.WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValue]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderExtraAttributesOauth2ClientClientSecretValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, plain_text: _builtins.str, thumbprint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainText")
    def plain_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderExtraAttributesOauth2ClientQueryParameters(dict):
    def __init__(__self__, *, filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderKeyKeyData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_spec: _builtins.str, format: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., not_after_time: Optional[_builtins.str] = ..., not_before_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySpec")
    def key_spec(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAfterTime")
    def not_after_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBeforeTime")
    def not_before_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderOidc(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, issuer_uri: _builtins.str, client_secret: Optional[outputs.WorkforcePoolProviderOidcClientSecret] = ..., jwks_json: Optional[_builtins.str] = ..., web_sso_config: Optional[outputs.WorkforcePoolProviderOidcWebSsoConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[outputs.WorkforcePoolProviderOidcClientSecret]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwksJson")
    def jwks_json(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webSsoConfig")
    def web_sso_config(self) -> Optional[outputs.WorkforcePoolProviderOidcWebSsoConfig]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderOidcClientSecret(dict):
    def __init__(__self__, *, value: Optional[outputs.WorkforcePoolProviderOidcClientSecretValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.WorkforcePoolProviderOidcClientSecretValue]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderOidcClientSecretValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, plain_text: _builtins.str, thumbprint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainText")
    def plain_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderOidcWebSsoConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assertion_claims_behavior: _builtins.str, response_type: _builtins.str, additional_scopes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assertionClaimsBehavior")
    def assertion_claims_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalScopes")
    def additional_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkforcePoolProviderSaml(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, idp_metadata_xml: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idpMetadataXml")
    def idp_metadata_xml(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolInlineCertificateIssuanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_pools: Mapping[str, _builtins.str], key_algorithm: Optional[_builtins.str] = ..., lifetime: Optional[_builtins.str] = ..., rotation_window_percentage: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caPools")
    def ca_pools(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationWindowPercentage")
    def rotation_window_percentage(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolInlineTrustConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_trust_bundles: Optional[Sequence[outputs.WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundle]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalTrustBundles")
    def additional_trust_bundles(self) -> Optional[Sequence[outputs.WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundle]]:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundle(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, trust_anchors: Sequence[outputs.WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchor], trust_domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustAnchors")
    def trust_anchors(self) -> Sequence[outputs.WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchor]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustDomain")
    def trust_domain(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pem_certificate: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolManagedIdentityAttestationRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, google_cloud_resource: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleCloudResource")
    def google_cloud_resource(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolNamespaceOwnerService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_subject: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalSubject")
    def principal_subject(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolProviderAws(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolProviderOidc(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, issuer_uri: _builtins.str, allowed_audiences: Optional[Sequence[_builtins.str]] = ..., jwks_json: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwksJson")
    def jwks_json(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolProviderSaml(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, idp_metadata_xml: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idpMetadataXml")
    def idp_metadata_xml(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolProviderX509(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, trust_store: outputs.WorkloadIdentityPoolProviderX509TrustStore) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStore")
    def trust_store(self) -> outputs.WorkloadIdentityPoolProviderX509TrustStore:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolProviderX509TrustStore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, trust_anchors: Sequence[outputs.WorkloadIdentityPoolProviderX509TrustStoreTrustAnchor], intermediate_cas: Optional[Sequence[outputs.WorkloadIdentityPoolProviderX509TrustStoreIntermediateCa]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustAnchors")
    def trust_anchors(self) -> Sequence[outputs.WorkloadIdentityPoolProviderX509TrustStoreTrustAnchor]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intermediateCas")
    def intermediate_cas(self) -> Optional[Sequence[outputs.WorkloadIdentityPoolProviderX509TrustStoreIntermediateCa]]:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolProviderX509TrustStoreIntermediateCa(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pem_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadIdentityPoolProviderX509TrustStoreTrustAnchor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pem_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetTestablePermissionsPermissionResult(dict):
    def __init__(__self__, *, api_disabled: _builtins.bool, custom_support_level: _builtins.str, name: _builtins.str, stage: _builtins.str, title: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiDisabled")
    def api_disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSupportLevel")
    def custom_support_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolInlineCertificateIssuanceConfigResult(dict):
    def __init__(__self__, *, ca_pools: Mapping[str, _builtins.str], key_algorithm: _builtins.str, lifetime: _builtins.str, rotation_window_percentage: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caPools")
    def ca_pools(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationWindowPercentage")
    def rotation_window_percentage(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolInlineTrustConfigResult(dict):
    def __init__(__self__, *, additional_trust_bundles: Sequence[outputs.GetWorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalTrustBundles")
    def additional_trust_bundles(self) -> Sequence[outputs.GetWorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleResult]:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleResult(dict):
    def __init__(__self__, *, trust_anchors: Sequence[outputs.GetWorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorResult], trust_domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustAnchors")
    def trust_anchors(self) -> Sequence[outputs.GetWorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustDomain")
    def trust_domain(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolInlineTrustConfigAdditionalTrustBundleTrustAnchorResult(dict):
    def __init__(__self__, *, pem_certificate: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolProviderAwResult(dict):
    def __init__(__self__, *, account_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolProviderOidcResult(dict):
    def __init__(__self__, *, allowed_audiences: Sequence[_builtins.str], issuer_uri: _builtins.str, jwks_json: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwksJson")
    def jwks_json(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolProviderSamlResult(dict):
    def __init__(__self__, *, idp_metadata_xml: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idpMetadataXml")
    def idp_metadata_xml(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolProviderX509Result(dict):
    def __init__(__self__, *, trust_stores: Sequence[outputs.GetWorkloadIdentityPoolProviderX509TrustStoreResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStores")
    def trust_stores(self) -> Sequence[outputs.GetWorkloadIdentityPoolProviderX509TrustStoreResult]:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolProviderX509TrustStoreResult(dict):
    def __init__(__self__, *, intermediate_cas: Sequence[outputs.GetWorkloadIdentityPoolProviderX509TrustStoreIntermediateCaResult], trust_anchors: Sequence[outputs.GetWorkloadIdentityPoolProviderX509TrustStoreTrustAnchorResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intermediateCas")
    def intermediate_cas(self) -> Sequence[outputs.GetWorkloadIdentityPoolProviderX509TrustStoreIntermediateCaResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustAnchors")
    def trust_anchors(self) -> Sequence[outputs.GetWorkloadIdentityPoolProviderX509TrustStoreTrustAnchorResult]:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolProviderX509TrustStoreIntermediateCaResult(dict):
    def __init__(__self__, *, pem_certificate: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkloadIdentityPoolProviderX509TrustStoreTrustAnchorResult(dict):
    def __init__(__self__, *, pem_certificate: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> _builtins.str:
        
        ...
    


