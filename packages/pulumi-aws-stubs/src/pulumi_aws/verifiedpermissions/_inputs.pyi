

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IdentitySourceConfigurationArgs', 'IdentitySourceConfigurationArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PolicyDefinitionArgs', 'PolicyDefinitionArgsDict', 'PolicyDefinitionStaticArgs', 'PolicyDefinitionStaticArgsDict', 'PolicyDefinitionTemplateLinkedArgs', 'PolicyDefinitionTemplateLinkedArgsDict', 'PolicyDefinitionTemplateLinkedPrincipalArgs', 'PolicyDefinitionTemplateLinkedPrincipalArgsDict', 'PolicyDefinitionTemplateLinkedResourceArgs', 'PolicyDefinitionTemplateLinkedResourceArgsDict', 'PolicyStoreValidationSettingsArgs', 'PolicyStoreValidationSettingsArgsDict', 'SchemaDefinitionArgs', 'SchemaDefinitionArgsDict']
class IdentitySourceConfigurationArgsDict(TypedDict):
    cognito_user_pool_configuration: NotRequired[pulumi.Input[IdentitySourceConfigurationCognitoUserPoolConfigurationArgsDict]]
    open_id_connect_configuration: NotRequired[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationArgsDict]]


@pulumi.input_type
class IdentitySourceConfigurationArgs:
    def __init__(__self__, *, cognito_user_pool_configuration: Optional[pulumi.Input[IdentitySourceConfigurationCognitoUserPoolConfigurationArgs]] = ..., open_id_connect_configuration: Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoUserPoolConfiguration")
    def cognito_user_pool_configuration(self) -> Optional[pulumi.Input[IdentitySourceConfigurationCognitoUserPoolConfigurationArgs]]:
        
        ...
    
    @cognito_user_pool_configuration.setter
    def cognito_user_pool_configuration(self, value: Optional[pulumi.Input[IdentitySourceConfigurationCognitoUserPoolConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openIdConnectConfiguration")
    def open_id_connect_configuration(self) -> Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationArgs]]:
        
        ...
    
    @open_id_connect_configuration.setter
    def open_id_connect_configuration(self, value: Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationArgs]]): # -> None:
        ...
    


class IdentitySourceConfigurationCognitoUserPoolConfigurationArgsDict(TypedDict):
    user_pool_arn: pulumi.Input[_builtins.str]
    client_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    group_configuration: NotRequired[pulumi.Input[IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfigurationArgsDict]]


@pulumi.input_type
class IdentitySourceConfigurationCognitoUserPoolConfigurationArgs:
    def __init__(__self__, *, user_pool_arn: pulumi.Input[_builtins.str], client_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., group_configuration: Optional[pulumi.Input[IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_arn.setter
    def user_pool_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIds")
    def client_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_ids.setter
    def client_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupConfiguration")
    def group_configuration(self) -> Optional[pulumi.Input[IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfigurationArgs]]:
        
        ...
    
    @group_configuration.setter
    def group_configuration(self, value: Optional[pulumi.Input[IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfigurationArgs]]): # -> None:
        ...
    


class IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfigurationArgsDict(TypedDict):
    group_entity_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class IdentitySourceConfigurationCognitoUserPoolConfigurationGroupConfigurationArgs:
    def __init__(__self__, *, group_entity_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupEntityType")
    def group_entity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_entity_type.setter
    def group_entity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class IdentitySourceConfigurationOpenIdConnectConfigurationArgsDict(TypedDict):
    issuer: pulumi.Input[_builtins.str]
    token_selection: pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionArgsDict]
    entity_id_prefix: NotRequired[pulumi.Input[_builtins.str]]
    group_configuration: NotRequired[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfigurationArgsDict]]


@pulumi.input_type
class IdentitySourceConfigurationOpenIdConnectConfigurationArgs:
    def __init__(__self__, *, issuer: pulumi.Input[_builtins.str], token_selection: pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionArgs], entity_id_prefix: Optional[pulumi.Input[_builtins.str]] = ..., group_configuration: Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenSelection")
    def token_selection(self) -> pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionArgs]:
        
        ...
    
    @token_selection.setter
    def token_selection(self, value: pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityIdPrefix")
    def entity_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entity_id_prefix.setter
    def entity_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupConfiguration")
    def group_configuration(self) -> Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfigurationArgs]]:
        
        ...
    
    @group_configuration.setter
    def group_configuration(self, value: Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfigurationArgs]]): # -> None:
        ...
    


class IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfigurationArgsDict(TypedDict):
    group_claim: pulumi.Input[_builtins.str]
    group_entity_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class IdentitySourceConfigurationOpenIdConnectConfigurationGroupConfigurationArgs:
    def __init__(__self__, *, group_claim: pulumi.Input[_builtins.str], group_entity_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupClaim")
    def group_claim(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_claim.setter
    def group_claim(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupEntityType")
    def group_entity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_entity_type.setter
    def group_entity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionArgsDict(TypedDict):
    access_token_only: NotRequired[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnlyArgsDict]]
    identity_token_only: NotRequired[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnlyArgsDict]]


@pulumi.input_type
class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionArgs:
    def __init__(__self__, *, access_token_only: Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnlyArgs]] = ..., identity_token_only: Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnlyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenOnly")
    def access_token_only(self) -> Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnlyArgs]]:
        
        ...
    
    @access_token_only.setter
    def access_token_only(self, value: Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnlyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityTokenOnly")
    def identity_token_only(self) -> Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnlyArgs]]:
        
        ...
    
    @identity_token_only.setter
    def identity_token_only(self, value: Optional[pulumi.Input[IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnlyArgs]]): # -> None:
        ...
    


class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnlyArgsDict(TypedDict):
    audiences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    principal_id_claim: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionAccessTokenOnlyArgs:
    def __init__(__self__, *, audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., principal_id_claim: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @audiences.setter
    def audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalIdClaim")
    def principal_id_claim(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_id_claim.setter
    def principal_id_claim(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnlyArgsDict(TypedDict):
    client_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    principal_id_claim: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IdentitySourceConfigurationOpenIdConnectConfigurationTokenSelectionIdentityTokenOnlyArgs:
    def __init__(__self__, *, client_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., principal_id_claim: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIds")
    def client_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_ids.setter
    def client_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalIdClaim")
    def principal_id_claim(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_id_claim.setter
    def principal_id_claim(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PolicyDefinitionArgsDict(TypedDict):
    static: NotRequired[pulumi.Input[PolicyDefinitionStaticArgsDict]]
    template_linked: NotRequired[pulumi.Input[PolicyDefinitionTemplateLinkedArgsDict]]


@pulumi.input_type
class PolicyDefinitionArgs:
    def __init__(__self__, *, static: Optional[pulumi.Input[PolicyDefinitionStaticArgs]] = ..., template_linked: Optional[pulumi.Input[PolicyDefinitionTemplateLinkedArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def static(self) -> Optional[pulumi.Input[PolicyDefinitionStaticArgs]]:
        
        ...
    
    @static.setter
    def static(self, value: Optional[pulumi.Input[PolicyDefinitionStaticArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateLinked")
    def template_linked(self) -> Optional[pulumi.Input[PolicyDefinitionTemplateLinkedArgs]]:
        
        ...
    
    @template_linked.setter
    def template_linked(self, value: Optional[pulumi.Input[PolicyDefinitionTemplateLinkedArgs]]): # -> None:
        ...
    


class PolicyDefinitionStaticArgsDict(TypedDict):
    statement: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PolicyDefinitionStaticArgs:
    def __init__(__self__, *, statement: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statement(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @statement.setter
    def statement(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PolicyDefinitionTemplateLinkedArgsDict(TypedDict):
    policy_template_id: pulumi.Input[_builtins.str]
    principal: NotRequired[pulumi.Input[PolicyDefinitionTemplateLinkedPrincipalArgsDict]]
    resource: NotRequired[pulumi.Input[PolicyDefinitionTemplateLinkedResourceArgsDict]]


@pulumi.input_type
class PolicyDefinitionTemplateLinkedArgs:
    def __init__(__self__, *, policy_template_id: pulumi.Input[_builtins.str], principal: Optional[pulumi.Input[PolicyDefinitionTemplateLinkedPrincipalArgs]] = ..., resource: Optional[pulumi.Input[PolicyDefinitionTemplateLinkedResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyTemplateId")
    def policy_template_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_template_id.setter
    def policy_template_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[PolicyDefinitionTemplateLinkedPrincipalArgs]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[PolicyDefinitionTemplateLinkedPrincipalArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[PolicyDefinitionTemplateLinkedResourceArgs]]:
        
        ...
    
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[PolicyDefinitionTemplateLinkedResourceArgs]]): # -> None:
        ...
    


class PolicyDefinitionTemplateLinkedPrincipalArgsDict(TypedDict):
    entity_id: pulumi.Input[_builtins.str]
    entity_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class PolicyDefinitionTemplateLinkedPrincipalArgs:
    def __init__(__self__, *, entity_id: pulumi.Input[_builtins.str], entity_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_id.setter
    def entity_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_type.setter
    def entity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PolicyDefinitionTemplateLinkedResourceArgsDict(TypedDict):
    entity_id: pulumi.Input[_builtins.str]
    entity_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class PolicyDefinitionTemplateLinkedResourceArgs:
    def __init__(__self__, *, entity_id: pulumi.Input[_builtins.str], entity_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_id.setter
    def entity_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_type.setter
    def entity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PolicyStoreValidationSettingsArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]


@pulumi.input_type
class PolicyStoreValidationSettingsArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SchemaDefinitionArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class SchemaDefinitionArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


