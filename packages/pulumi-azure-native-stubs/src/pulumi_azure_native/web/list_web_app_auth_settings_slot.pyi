

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWebAppAuthSettingsSlotResult', 'AwaitableListWebAppAuthSettingsSlotResult', 'list_web_app_auth_settings_slot', 'list_web_app_auth_settings_slot_output']
@pulumi.output_type
class ListWebAppAuthSettingsSlotResult:
    
    def __init__(__self__, aad_claims_authorization=..., additional_login_params=..., allowed_audiences=..., allowed_external_redirect_urls=..., auth_file_path=..., client_id=..., client_secret=..., client_secret_certificate_thumbprint=..., client_secret_setting_name=..., config_version=..., default_provider=..., enabled=..., facebook_app_id=..., facebook_app_secret=..., facebook_app_secret_setting_name=..., facebook_o_auth_scopes=..., git_hub_client_id=..., git_hub_client_secret=..., git_hub_client_secret_setting_name=..., git_hub_o_auth_scopes=..., google_client_id=..., google_client_secret=..., google_client_secret_setting_name=..., google_o_auth_scopes=..., id=..., is_auth_from_file=..., issuer=..., kind=..., microsoft_account_client_id=..., microsoft_account_client_secret=..., microsoft_account_client_secret_setting_name=..., microsoft_account_o_auth_scopes=..., name=..., runtime_version=..., token_refresh_extension_hours=..., token_store_enabled=..., twitter_consumer_key=..., twitter_consumer_secret=..., twitter_consumer_secret_setting_name=..., type=..., unauthenticated_client_action=..., validate_issuer=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadClaimsAuthorization")
    def aad_claims_authorization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalLoginParams")
    def additional_login_params(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authFilePath")
    def auth_file_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateThumbprint")
    def client_secret_certificate_thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultProvider")
    def default_provider(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="facebookAppId")
    def facebook_app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="facebookAppSecret")
    def facebook_app_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="facebookAppSecretSettingName")
    def facebook_app_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="facebookOAuthScopes")
    def facebook_o_auth_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHubClientId")
    def git_hub_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHubClientSecret")
    def git_hub_client_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHubClientSecretSettingName")
    def git_hub_client_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHubOAuthScopes")
    def git_hub_o_auth_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleClientId")
    def google_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleClientSecret")
    def google_client_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleClientSecretSettingName")
    def google_client_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleOAuthScopes")
    def google_o_auth_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAuthFromFile")
    def is_auth_from_file(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientId")
    def microsoft_account_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientSecret")
    def microsoft_account_client_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientSecretSettingName")
    def microsoft_account_client_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="microsoftAccountOAuthScopes")
    def microsoft_account_o_auth_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenStoreEnabled")
    def token_store_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="twitterConsumerKey")
    def twitter_consumer_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="twitterConsumerSecret")
    def twitter_consumer_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="twitterConsumerSecretSettingName")
    def twitter_consumer_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unauthenticatedClientAction")
    def unauthenticated_client_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateIssuer")
    def validate_issuer(self) -> Optional[_builtins.bool]:
        
        ...
    


class AwaitableListWebAppAuthSettingsSlotResult(ListWebAppAuthSettingsSlotResult):
    def __await__(self): # -> Generator[Never, Any, ListWebAppAuthSettingsSlotResult]:
        ...
    


def list_web_app_auth_settings_slot(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., slot: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWebAppAuthSettingsSlotResult:
    
    ...

def list_web_app_auth_settings_slot_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWebAppAuthSettingsSlotResult]:
    
    ...

