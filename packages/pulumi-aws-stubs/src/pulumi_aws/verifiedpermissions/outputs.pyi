

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IdentitySourceConfiguration', ..., ..., ..., ..., ..., ..., ..., 'PolicyDefinition', 'PolicyDefinitionStatic', 'PolicyDefinitionTemplateLinked', 'PolicyDefinitionTemplateLinkedPrincipal', 'PolicyDefinitionTemplateLinkedResource', 'PolicyStoreValidationSettings', 'SchemaDefinition', 'GetPolicyStoreValidationSettingResult']
@pulumi.output_type
class IdentitySourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cognito_user_pool_configuration: Optional[outputs.IdentitySourceConfigurationCognitoUserPoolConfiguration] = ..., open_id_connect_configuration: Optional[outputs.IdentitySourceConfigurationOpenIdConnectConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoUserPoolConfiguration")
    def cognito_user_pool_configuration(self) -> Optional[outputs.IdentitySourceConfigurationCognitoUserPoolConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openIdConnectConfiguration")
    def open_id_connect_configuration(self) -> Optional[outputs.IdentitySourceConfigurationOpenIdConnectConfiguration]:
        
        ...
    


@pulumi.output_type
class IdentitySourceConfigurationCognitoUserPoolConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_pool_arn: _builtins.str, client_ids: Optional[Sequence[_builtins.str]] = ..., group_configuration: Optional[outputs.IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIds")
    def client_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupConfiguration")
    def group_configuration(self) -> Optional[outputs.IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfiguration]:
        
        ...
    


@pulumi.output_type
class IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_entity_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupEntityType")
    def group_entity_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IdentitySourceConfigurationOpenIdConnectConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, issuer: _builtins.str, token_selection: outputs.IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelection, entity_id_prefix: Optional[_builtins.str] = ..., group_configuration: Optional[outputs.IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenSelection")
    def token_selection(self) -> outputs.IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityIdPrefix")
    def entity_id_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupConfiguration")
    def group_configuration(self) -> Optional[outputs.IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfiguration]:
        
        ...
    


@pulumi.output_type
class IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_claim: _builtins.str, group_entity_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupClaim")
    def group_claim(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupEntityType")
    def group_entity_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_token_only: Optional[outputs.IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnly] = ..., identity_token_only: Optional[outputs.IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnly] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenOnly")
    def access_token_only(self) -> Optional[outputs.IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnly]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityTokenOnly")
    def identity_token_only(self) -> Optional[outputs.IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnly]:
        
        ...
    


@pulumi.output_type
class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnly(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audiences: Optional[Sequence[_builtins.str]] = ..., principal_id_claim: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audiences(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalIdClaim")
    def principal_id_claim(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnly(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_ids: Optional[Sequence[_builtins.str]] = ..., principal_id_claim: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIds")
    def client_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalIdClaim")
    def principal_id_claim(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, static: Optional[outputs.PolicyDefinitionStatic] = ..., template_linked: Optional[outputs.PolicyDefinitionTemplateLinked] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def static(self) -> Optional[outputs.PolicyDefinitionStatic]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateLinked")
    def template_linked(self) -> Optional[outputs.PolicyDefinitionTemplateLinked]:
        
        ...
    


@pulumi.output_type
class PolicyDefinitionStatic(dict):
    def __init__(__self__, *, statement: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statement(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyDefinitionTemplateLinked(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_template_id: _builtins.str, principal: Optional[outputs.PolicyDefinitionTemplateLinkedPrincipal] = ..., resource: Optional[outputs.PolicyDefinitionTemplateLinkedResource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyTemplateId")
    def policy_template_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[outputs.PolicyDefinitionTemplateLinkedPrincipal]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[outputs.PolicyDefinitionTemplateLinkedResource]:
        
        ...
    


@pulumi.output_type
class PolicyDefinitionTemplateLinkedPrincipal(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, entity_id: _builtins.str, entity_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyDefinitionTemplateLinkedResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, entity_id: _builtins.str, entity_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyStoreValidationSettings(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SchemaDefinition(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPolicyStoreValidationSettingResult(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        ...
    


