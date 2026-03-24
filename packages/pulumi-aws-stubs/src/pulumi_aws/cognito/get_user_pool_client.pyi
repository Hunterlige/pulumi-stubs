

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserPoolClientResult', 'AwaitableGetUserPoolClientResult', 'get_user_pool_client', 'get_user_pool_client_output']
@pulumi.output_type
class GetUserPoolClientResult:
    
    def __init__(__self__, access_token_validity=..., allowed_oauth_flows=..., allowed_oauth_flows_user_pool_client=..., allowed_oauth_scopes=..., analytics_configurations=..., callback_urls=..., client_id=..., client_secret=..., default_redirect_uri=..., enable_propagate_additional_user_context_data=..., enable_token_revocation=..., explicit_auth_flows=..., generate_secret=..., id=..., id_token_validity=..., logout_urls=..., name=..., prevent_user_existence_errors=..., read_attributes=..., refresh_token_rotations=..., refresh_token_validity=..., region=..., supported_identity_providers=..., token_validity_units=..., user_pool_id=..., write_attributes=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenValidity")
    def access_token_validity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthFlows")
    def allowed_oauth_flows(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthFlowsUserPoolClient")
    def allowed_oauth_flows_user_pool_client(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOauthScopes")
    def allowed_oauth_scopes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsConfigurations")
    def analytics_configurations(self) -> Sequence[outputs.GetUserPoolClientAnalyticsConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrls")
    def callback_urls(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRedirectUri")
    def default_redirect_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePropagateAdditionalUserContextData")
    def enable_propagate_additional_user_context_data(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTokenRevocation")
    def enable_token_revocation(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitAuthFlows")
    def explicit_auth_flows(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generateSecret")
    def generate_secret(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idTokenValidity")
    def id_token_validity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logoutUrls")
    def logout_urls(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAttributes")
    def read_attributes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTokenRotations")
    def refresh_token_rotations(self) -> Sequence[outputs.GetUserPoolClientRefreshTokenRotationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshTokenValidity")
    def refresh_token_validity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedIdentityProviders")
    def supported_identity_providers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenValidityUnits")
    def token_validity_units(self) -> Sequence[outputs.GetUserPoolClientTokenValidityUnitResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAttributes")
    def write_attributes(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetUserPoolClientResult(GetUserPoolClientResult):
    def __await__(self): # -> Generator[Never, Any, GetUserPoolClientResult]:
        ...
    


def get_user_pool_client(client_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., user_pool_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserPoolClientResult:
    
    ...

def get_user_pool_client_output(client_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserPoolClientResult]:
    
    ...

