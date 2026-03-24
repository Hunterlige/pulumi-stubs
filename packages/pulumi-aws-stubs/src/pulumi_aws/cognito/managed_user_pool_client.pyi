

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedUserPoolClientArgs', 'ManagedUserPoolClient']
@pulumi.input_type
class ManagedUserPoolClientArgs:
    def __init__(__self__, *, user_pool_id: pulumi.Input[_builtins.str], access_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., allowed_oauth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_oauth_flows_user_pool_client: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_oauth_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., analytics_configuration: Optional[pulumi.Input[ManagedUserPoolClientAnalyticsConfigurationArgs]] = ..., auth_session_validity: Optional[pulumi.Input[_builtins.int]] = ..., callback_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., default_redirect_uri: Optional[pulumi.Input[_builtins.str]] = ..., enable_propagate_additional_user_context_data: Optional[pulumi.Input[_builtins.bool]] = ..., enable_token_revocation: Optional[pulumi.Input[_builtins.bool]] = ..., explicit_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., logout_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name_pattern: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., prevent_user_existence_errors: Optional[pulumi.Input[_builtins.str]] = ..., read_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., refresh_token_rotation: Optional[pulumi.Input[ManagedUserPoolClientRefreshTokenRotationArgs]] = ..., refresh_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., supported_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., token_validity_units: Optional[pulumi.Input[ManagedUserPoolClientTokenValidityUnitsArgs]] = ..., write_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenValidity")
    def access_token_validity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @access_token_validity.setter
    def access_token_validity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthFlows")
    def allowed_oauth_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_oauth_flows.setter
    def allowed_oauth_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthFlowsUserPoolClient")
    def allowed_oauth_flows_user_pool_client(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allowed_oauth_flows_user_pool_client.setter
    def allowed_oauth_flows_user_pool_client(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthScopes")
    def allowed_oauth_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_oauth_scopes.setter
    def allowed_oauth_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsConfiguration")
    def analytics_configuration(self) -> Optional[pulumi.Input[ManagedUserPoolClientAnalyticsConfigurationArgs]]:
        
        ...
    
    @analytics_configuration.setter
    def analytics_configuration(self, value: Optional[pulumi.Input[ManagedUserPoolClientAnalyticsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authSessionValidity")
    def auth_session_validity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @auth_session_validity.setter
    def auth_session_validity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrls")
    def callback_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @callback_urls.setter
    def callback_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRedirectUri")
    def default_redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_redirect_uri.setter
    def default_redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePropagateAdditionalUserContextData")
    def enable_propagate_additional_user_context_data(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_propagate_additional_user_context_data.setter
    def enable_propagate_additional_user_context_data(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTokenRevocation")
    def enable_token_revocation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_token_revocation.setter
    def enable_token_revocation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitAuthFlows")
    def explicit_auth_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @explicit_auth_flows.setter
    def explicit_auth_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idTokenValidity")
    def id_token_validity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @id_token_validity.setter
    def id_token_validity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logoutUrls")
    def logout_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @logout_urls.setter
    def logout_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePattern")
    def name_pattern(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_pattern.setter
    def name_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prevent_user_existence_errors.setter
    def prevent_user_existence_errors(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAttributes")
    def read_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @read_attributes.setter
    def read_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTokenRotation")
    def refresh_token_rotation(self) -> Optional[pulumi.Input[ManagedUserPoolClientRefreshTokenRotationArgs]]:
        
        ...
    
    @refresh_token_rotation.setter
    def refresh_token_rotation(self, value: Optional[pulumi.Input[ManagedUserPoolClientRefreshTokenRotationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTokenValidity")
    def refresh_token_validity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @refresh_token_validity.setter
    def refresh_token_validity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedIdentityProviders")
    def supported_identity_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_identity_providers.setter
    def supported_identity_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenValidityUnits")
    def token_validity_units(self) -> Optional[pulumi.Input[ManagedUserPoolClientTokenValidityUnitsArgs]]:
        
        ...
    
    @token_validity_units.setter
    def token_validity_units(self, value: Optional[pulumi.Input[ManagedUserPoolClientTokenValidityUnitsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAttributes")
    def write_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @write_attributes.setter
    def write_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ManagedUserPoolClientState:
    def __init__(__self__, *, access_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., allowed_oauth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_oauth_flows_user_pool_client: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_oauth_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., analytics_configuration: Optional[pulumi.Input[ManagedUserPoolClientAnalyticsConfigurationArgs]] = ..., auth_session_validity: Optional[pulumi.Input[_builtins.int]] = ..., callback_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ..., default_redirect_uri: Optional[pulumi.Input[_builtins.str]] = ..., enable_propagate_additional_user_context_data: Optional[pulumi.Input[_builtins.bool]] = ..., enable_token_revocation: Optional[pulumi.Input[_builtins.bool]] = ..., explicit_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., logout_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_pattern: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., prevent_user_existence_errors: Optional[pulumi.Input[_builtins.str]] = ..., read_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., refresh_token_rotation: Optional[pulumi.Input[ManagedUserPoolClientRefreshTokenRotationArgs]] = ..., refresh_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., supported_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., token_validity_units: Optional[pulumi.Input[ManagedUserPoolClientTokenValidityUnitsArgs]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., write_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenValidity")
    def access_token_validity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @access_token_validity.setter
    def access_token_validity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthFlows")
    def allowed_oauth_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_oauth_flows.setter
    def allowed_oauth_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthFlowsUserPoolClient")
    def allowed_oauth_flows_user_pool_client(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allowed_oauth_flows_user_pool_client.setter
    def allowed_oauth_flows_user_pool_client(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthScopes")
    def allowed_oauth_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_oauth_scopes.setter
    def allowed_oauth_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsConfiguration")
    def analytics_configuration(self) -> Optional[pulumi.Input[ManagedUserPoolClientAnalyticsConfigurationArgs]]:
        
        ...
    
    @analytics_configuration.setter
    def analytics_configuration(self, value: Optional[pulumi.Input[ManagedUserPoolClientAnalyticsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authSessionValidity")
    def auth_session_validity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @auth_session_validity.setter
    def auth_session_validity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrls")
    def callback_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @callback_urls.setter
    def callback_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRedirectUri")
    def default_redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_redirect_uri.setter
    def default_redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePropagateAdditionalUserContextData")
    def enable_propagate_additional_user_context_data(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_propagate_additional_user_context_data.setter
    def enable_propagate_additional_user_context_data(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTokenRevocation")
    def enable_token_revocation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_token_revocation.setter
    def enable_token_revocation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitAuthFlows")
    def explicit_auth_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @explicit_auth_flows.setter
    def explicit_auth_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idTokenValidity")
    def id_token_validity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @id_token_validity.setter
    def id_token_validity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logoutUrls")
    def logout_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @logout_urls.setter
    def logout_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePattern")
    def name_pattern(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_pattern.setter
    def name_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prevent_user_existence_errors.setter
    def prevent_user_existence_errors(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAttributes")
    def read_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @read_attributes.setter
    def read_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTokenRotation")
    def refresh_token_rotation(self) -> Optional[pulumi.Input[ManagedUserPoolClientRefreshTokenRotationArgs]]:
        
        ...
    
    @refresh_token_rotation.setter
    def refresh_token_rotation(self, value: Optional[pulumi.Input[ManagedUserPoolClientRefreshTokenRotationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTokenValidity")
    def refresh_token_validity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @refresh_token_validity.setter
    def refresh_token_validity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedIdentityProviders")
    def supported_identity_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_identity_providers.setter
    def supported_identity_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenValidityUnits")
    def token_validity_units(self) -> Optional[pulumi.Input[ManagedUserPoolClientTokenValidityUnitsArgs]]:
        
        ...
    
    @token_validity_units.setter
    def token_validity_units(self, value: Optional[pulumi.Input[ManagedUserPoolClientTokenValidityUnitsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAttributes")
    def write_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @write_attributes.setter
    def write_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ManagedUserPoolClient(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., allowed_oauth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_oauth_flows_user_pool_client: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_oauth_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., analytics_configuration: Optional[pulumi.Input[Union[ManagedUserPoolClientAnalyticsConfigurationArgs, ManagedUserPoolClientAnalyticsConfigurationArgsDict]]] = ..., auth_session_validity: Optional[pulumi.Input[_builtins.int]] = ..., callback_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., default_redirect_uri: Optional[pulumi.Input[_builtins.str]] = ..., enable_propagate_additional_user_context_data: Optional[pulumi.Input[_builtins.bool]] = ..., enable_token_revocation: Optional[pulumi.Input[_builtins.bool]] = ..., explicit_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., logout_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name_pattern: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., prevent_user_existence_errors: Optional[pulumi.Input[_builtins.str]] = ..., read_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., refresh_token_rotation: Optional[pulumi.Input[Union[ManagedUserPoolClientRefreshTokenRotationArgs, ManagedUserPoolClientRefreshTokenRotationArgsDict]]] = ..., refresh_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., supported_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., token_validity_units: Optional[pulumi.Input[Union[ManagedUserPoolClientTokenValidityUnitsArgs, ManagedUserPoolClientTokenValidityUnitsArgsDict]]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., write_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedUserPoolClientArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., allowed_oauth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_oauth_flows_user_pool_client: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_oauth_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., analytics_configuration: Optional[pulumi.Input[Union[ManagedUserPoolClientAnalyticsConfigurationArgs, ManagedUserPoolClientAnalyticsConfigurationArgsDict]]] = ..., auth_session_validity: Optional[pulumi.Input[_builtins.int]] = ..., callback_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ..., default_redirect_uri: Optional[pulumi.Input[_builtins.str]] = ..., enable_propagate_additional_user_context_data: Optional[pulumi.Input[_builtins.bool]] = ..., enable_token_revocation: Optional[pulumi.Input[_builtins.bool]] = ..., explicit_auth_flows: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., logout_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_pattern: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., prevent_user_existence_errors: Optional[pulumi.Input[_builtins.str]] = ..., read_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., refresh_token_rotation: Optional[pulumi.Input[Union[ManagedUserPoolClientRefreshTokenRotationArgs, ManagedUserPoolClientRefreshTokenRotationArgsDict]]] = ..., refresh_token_validity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., supported_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., token_validity_units: Optional[pulumi.Input[Union[ManagedUserPoolClientTokenValidityUnitsArgs, ManagedUserPoolClientTokenValidityUnitsArgsDict]]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., write_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> ManagedUserPoolClient:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenValidity")
    def access_token_validity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthFlows")
    def allowed_oauth_flows(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthFlowsUserPoolClient")
    def allowed_oauth_flows_user_pool_client(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthScopes")
    def allowed_oauth_scopes(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsConfiguration")
    def analytics_configuration(self) -> pulumi.Output[Optional[outputs.ManagedUserPoolClientAnalyticsConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authSessionValidity")
    def auth_session_validity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrls")
    def callback_urls(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRedirectUri")
    def default_redirect_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePropagateAdditionalUserContextData")
    def enable_propagate_additional_user_context_data(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTokenRevocation")
    def enable_token_revocation(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitAuthFlows")
    def explicit_auth_flows(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idTokenValidity")
    def id_token_validity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logoutUrls")
    def logout_urls(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePattern")
    def name_pattern(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAttributes")
    def read_attributes(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTokenRotation")
    def refresh_token_rotation(self) -> pulumi.Output[Optional[outputs.ManagedUserPoolClientRefreshTokenRotation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTokenValidity")
    def refresh_token_validity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedIdentityProviders")
    def supported_identity_providers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenValidityUnits")
    def token_validity_units(self) -> pulumi.Output[Optional[outputs.ManagedUserPoolClientTokenValidityUnits]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAttributes")
    def write_attributes(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


