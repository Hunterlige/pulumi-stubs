import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebAppAuthSettingsArgs", "WebAppAuthSettings"]

@pulumi.input_type
class WebAppAuthSettingsArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        aad_claims_authorization: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_login_params: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_external_redirect_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        auth_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_certificate_thumbprint: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        config_version: Optional[pulumi.Input[_builtins.str]] = ...,
        default_provider: Optional[pulumi.Input[BuiltInAuthenticationProvider]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        facebook_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        facebook_app_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        facebook_app_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        facebook_o_auth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        git_hub_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        git_hub_client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        git_hub_client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        git_hub_o_auth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        google_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        google_client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        google_client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        google_o_auth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_auth_from_file: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        microsoft_account_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        microsoft_account_client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        microsoft_account_client_secret_setting_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        microsoft_account_o_auth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        runtime_version: Optional[pulumi.Input[_builtins.str]] = ...,
        token_refresh_extension_hours: Optional[pulumi.Input[_builtins.float]] = ...,
        token_store_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        twitter_consumer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        twitter_consumer_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        twitter_consumer_secret_setting_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        unauthenticated_client_action: Optional[
            pulumi.Input[UnauthenticatedClientAction]
        ] = ...,
        validate_issuer: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="aadClaimsAuthorization")
    def aad_claims_authorization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aad_claims_authorization.setter
    def aad_claims_authorization(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalLoginParams")
    def additional_login_params(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_login_params.setter
    def additional_login_params(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_external_redirect_urls.setter
    def allowed_external_redirect_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authFilePath")
    def auth_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_file_path.setter
    def auth_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateThumbprint")
    def client_secret_certificate_thumbprint(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_certificate_thumbprint.setter
    def client_secret_certificate_thumbprint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_setting_name.setter
    def client_secret_setting_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @config_version.setter
    def config_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultProvider")
    def default_provider(
        self,
    ) -> Optional[pulumi.Input[BuiltInAuthenticationProvider]]: ...
    @default_provider.setter
    def default_provider(
        self, value: Optional[pulumi.Input[BuiltInAuthenticationProvider]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="facebookAppId")
    def facebook_app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @facebook_app_id.setter
    def facebook_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="facebookAppSecret")
    def facebook_app_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @facebook_app_secret.setter
    def facebook_app_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="facebookAppSecretSettingName")
    def facebook_app_secret_setting_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @facebook_app_secret_setting_name.setter
    def facebook_app_secret_setting_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="facebookOAuthScopes")
    def facebook_o_auth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @facebook_o_auth_scopes.setter
    def facebook_o_auth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gitHubClientId")
    def git_hub_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_hub_client_id.setter
    def git_hub_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitHubClientSecret")
    def git_hub_client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_hub_client_secret.setter
    def git_hub_client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitHubClientSecretSettingName")
    def git_hub_client_secret_setting_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_hub_client_secret_setting_name.setter
    def git_hub_client_secret_setting_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gitHubOAuthScopes")
    def git_hub_o_auth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @git_hub_o_auth_scopes.setter
    def git_hub_o_auth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleClientId")
    def google_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @google_client_id.setter
    def google_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="googleClientSecret")
    def google_client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @google_client_secret.setter
    def google_client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="googleClientSecretSettingName")
    def google_client_secret_setting_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @google_client_secret_setting_name.setter
    def google_client_secret_setting_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleOAuthScopes")
    def google_o_auth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @google_o_auth_scopes.setter
    def google_o_auth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAuthFromFile")
    def is_auth_from_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @is_auth_from_file.setter
    def is_auth_from_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientId")
    def microsoft_account_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @microsoft_account_client_id.setter
    def microsoft_account_client_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientSecret")
    def microsoft_account_client_secret(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @microsoft_account_client_secret.setter
    def microsoft_account_client_secret(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientSecretSettingName")
    def microsoft_account_client_secret_setting_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @microsoft_account_client_secret_setting_name.setter
    def microsoft_account_client_secret_setting_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="microsoftAccountOAuthScopes")
    def microsoft_account_o_auth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @microsoft_account_o_auth_scopes.setter
    def microsoft_account_o_auth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @token_refresh_extension_hours.setter
    def token_refresh_extension_hours(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenStoreEnabled")
    def token_store_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @token_store_enabled.setter
    def token_store_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="twitterConsumerKey")
    def twitter_consumer_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @twitter_consumer_key.setter
    def twitter_consumer_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="twitterConsumerSecret")
    def twitter_consumer_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @twitter_consumer_secret.setter
    def twitter_consumer_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="twitterConsumerSecretSettingName")
    def twitter_consumer_secret_setting_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @twitter_consumer_secret_setting_name.setter
    def twitter_consumer_secret_setting_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="unauthenticatedClientAction")
    def unauthenticated_client_action(
        self,
    ) -> Optional[pulumi.Input[UnauthenticatedClientAction]]: ...
    @unauthenticated_client_action.setter
    def unauthenticated_client_action(
        self, value: Optional[pulumi.Input[UnauthenticatedClientAction]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validateIssuer")
    def validate_issuer(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @validate_issuer.setter
    def validate_issuer(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("azure-native:web:WebAppAuthSettings")
class WebAppAuthSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aad_claims_authorization: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_login_params: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_external_redirect_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        auth_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_certificate_thumbprint: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        config_version: Optional[pulumi.Input[_builtins.str]] = ...,
        default_provider: Optional[pulumi.Input[BuiltInAuthenticationProvider]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        facebook_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        facebook_app_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        facebook_app_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        facebook_o_auth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        git_hub_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        git_hub_client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        git_hub_client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        git_hub_o_auth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        google_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        google_client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        google_client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        google_o_auth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_auth_from_file: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        microsoft_account_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        microsoft_account_client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        microsoft_account_client_secret_setting_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        microsoft_account_o_auth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_version: Optional[pulumi.Input[_builtins.str]] = ...,
        token_refresh_extension_hours: Optional[pulumi.Input[_builtins.float]] = ...,
        token_store_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        twitter_consumer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        twitter_consumer_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        twitter_consumer_secret_setting_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        unauthenticated_client_action: Optional[
            pulumi.Input[UnauthenticatedClientAction]
        ] = ...,
        validate_issuer: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebAppAuthSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WebAppAuthSettings: ...
    @_builtins.property
    @pulumi.getter(name="aadClaimsAuthorization")
    def aad_claims_authorization(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="additionalLoginParams")
    def additional_login_params(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="authFilePath")
    def auth_file_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateThumbprint")
    def client_secret_certificate_thumbprint(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultProvider")
    def default_provider(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="facebookAppId")
    def facebook_app_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="facebookAppSecret")
    def facebook_app_secret(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="facebookAppSecretSettingName")
    def facebook_app_secret_setting_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="facebookOAuthScopes")
    def facebook_o_auth_scopes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="gitHubClientId")
    def git_hub_client_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gitHubClientSecret")
    def git_hub_client_secret(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gitHubClientSecretSettingName")
    def git_hub_client_secret_setting_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gitHubOAuthScopes")
    def git_hub_o_auth_scopes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="googleClientId")
    def google_client_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="googleClientSecret")
    def google_client_secret(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="googleClientSecretSettingName")
    def google_client_secret_setting_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="googleOAuthScopes")
    def google_o_auth_scopes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="isAuthFromFile")
    def is_auth_from_file(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientId")
    def microsoft_account_client_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientSecret")
    def microsoft_account_client_secret(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="microsoftAccountClientSecretSettingName")
    def microsoft_account_client_secret_setting_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="microsoftAccountOAuthScopes")
    def microsoft_account_o_auth_scopes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(
        self,
    ) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="tokenStoreEnabled")
    def token_store_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="twitterConsumerKey")
    def twitter_consumer_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="twitterConsumerSecret")
    def twitter_consumer_secret(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="twitterConsumerSecretSettingName")
    def twitter_consumer_secret_setting_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unauthenticatedClientAction")
    def unauthenticated_client_action(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="validateIssuer")
    def validate_issuer(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
