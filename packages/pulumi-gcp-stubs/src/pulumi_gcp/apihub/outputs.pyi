import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApiHubInstanceConfig",
    "CurationEndpoint",
    ...,
    "CurationPluginInstanceAction",
    "PluginActionsConfig",
    "PluginConfigTemplate",
    "PluginConfigTemplateAdditionalConfigTemplate",
    ...,
    ...,
    "PluginConfigTemplateAuthConfigTemplate",
    ...,
    "PluginDocumentation",
    "PluginHostingService",
    "PluginInstanceAction",
    "PluginInstanceActionCurationConfig",
    "PluginInstanceActionCurationConfigCustomCuration",
    "PluginInstanceActionHubInstanceAction",
    "PluginInstanceActionHubInstanceActionLastExecution",
    "PluginInstanceAuthConfig",
    "PluginInstanceAuthConfigApiKeyConfig",
    "PluginInstanceAuthConfigApiKeyConfigApiKey",
    "PluginInstanceAuthConfigGoogleServiceAccountConfig",
    ...,
    ...,
    "PluginInstanceAuthConfigUserPasswordConfig",
    "PluginInstanceAuthConfigUserPasswordConfigPassword",
]

@pulumi.output_type
class ApiHubInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cmek_key_name: Optional[_builtins.str] = ...,
        disable_search: Optional[_builtins.bool] = ...,
        encryption_type: Optional[_builtins.str] = ...,
        vertex_location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cmekKeyName")
    def cmek_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableSearch")
    def disable_search(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vertexLocation")
    def vertex_location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CurationEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_integration_endpoint_details: outputs.CurationEndpointApplicationIntegrationEndpointDetails,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationIntegrationEndpointDetails")
    def application_integration_endpoint_details(
        self,
    ) -> outputs.CurationEndpointApplicationIntegrationEndpointDetails: ...

@pulumi.output_type
class CurationEndpointApplicationIntegrationEndpointDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, trigger_id: _builtins.str, uri: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class CurationPluginInstanceAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_id: Optional[_builtins.str] = ...,
        plugin_instance: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PluginActionsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        display_name: _builtins.str,
        id: _builtins.str,
        trigger_mode: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="triggerMode")
    def trigger_mode(self) -> _builtins.str: ...

@pulumi.output_type
class PluginConfigTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_config_templates: Optional[
            Sequence[outputs.PluginConfigTemplateAdditionalConfigTemplate]
        ] = ...,
        auth_config_template: Optional[
            outputs.PluginConfigTemplateAuthConfigTemplate
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalConfigTemplates")
    def additional_config_templates(
        self,
    ) -> Optional[Sequence[outputs.PluginConfigTemplateAdditionalConfigTemplate]]: ...
    @_builtins.property
    @pulumi.getter(name="authConfigTemplate")
    def auth_config_template(
        self,
    ) -> Optional[outputs.PluginConfigTemplateAuthConfigTemplate]: ...

@pulumi.output_type
class PluginConfigTemplateAdditionalConfigTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        value_type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        enum_options: Optional[
            Sequence[outputs.PluginConfigTemplateAdditionalConfigTemplateEnumOption]
        ] = ...,
        multi_select_options: Optional[
            Sequence[
                outputs.PluginConfigTemplateAdditionalConfigTemplateMultiSelectOption
            ]
        ] = ...,
        required: Optional[_builtins.bool] = ...,
        validation_regex: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enumOptions")
    def enum_options(
        self,
    ) -> Optional[
        Sequence[outputs.PluginConfigTemplateAdditionalConfigTemplateEnumOption]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="multiSelectOptions")
    def multi_select_options(
        self,
    ) -> Optional[
        Sequence[outputs.PluginConfigTemplateAdditionalConfigTemplateMultiSelectOption]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="validationRegex")
    def validation_regex(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PluginConfigTemplateAdditionalConfigTemplateEnumOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: _builtins.str,
        id: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PluginConfigTemplateAdditionalConfigTemplateMultiSelectOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: _builtins.str,
        id: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PluginConfigTemplateAuthConfigTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        supported_auth_types: Sequence[_builtins.str],
        service_account: Optional[
            outputs.PluginConfigTemplateAuthConfigTemplateServiceAccount
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportedAuthTypes")
    def supported_auth_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(
        self,
    ) -> Optional[outputs.PluginConfigTemplateAuthConfigTemplateServiceAccount]: ...

@pulumi.output_type
class PluginConfigTemplateAuthConfigTemplateServiceAccount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, service_account: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str: ...

@pulumi.output_type
class PluginDocumentation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, external_uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalUri")
    def external_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PluginHostingService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, service_uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PluginInstanceAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_id: _builtins.str,
        curation_config: Optional[outputs.PluginInstanceActionCurationConfig] = ...,
        hub_instance_actions: Optional[
            Sequence[outputs.PluginInstanceActionHubInstanceAction]
        ] = ...,
        schedule_cron_expression: Optional[_builtins.str] = ...,
        schedule_time_zone: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="curationConfig")
    def curation_config(
        self,
    ) -> Optional[outputs.PluginInstanceActionCurationConfig]: ...
    @_builtins.property
    @pulumi.getter(name="hubInstanceActions")
    def hub_instance_actions(
        self,
    ) -> Optional[Sequence[outputs.PluginInstanceActionHubInstanceAction]]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleCronExpression")
    def schedule_cron_expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleTimeZone")
    def schedule_time_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PluginInstanceActionCurationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        curation_type: Optional[_builtins.str] = ...,
        custom_curation: Optional[
            outputs.PluginInstanceActionCurationConfigCustomCuration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="curationType")
    def curation_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customCuration")
    def custom_curation(
        self,
    ) -> Optional[outputs.PluginInstanceActionCurationConfigCustomCuration]: ...

@pulumi.output_type
class PluginInstanceActionCurationConfigCustomCuration(dict):
    def __init__(__self__, *, curation: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def curation(self) -> _builtins.str: ...

@pulumi.output_type
class PluginInstanceActionHubInstanceAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_execution_state: Optional[_builtins.str] = ...,
        last_executions: Optional[
            Sequence[outputs.PluginInstanceActionHubInstanceActionLastExecution]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentExecutionState")
    def current_execution_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastExecutions")
    def last_executions(
        self,
    ) -> Optional[
        Sequence[outputs.PluginInstanceActionHubInstanceActionLastExecution]
    ]: ...

@pulumi.output_type
class PluginInstanceActionHubInstanceActionLastExecution(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        error_message: Optional[_builtins.str] = ...,
        result: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PluginInstanceAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_type: _builtins.str,
        api_key_config: Optional[outputs.PluginInstanceAuthConfigApiKeyConfig] = ...,
        google_service_account_config: Optional[
            outputs.PluginInstanceAuthConfigGoogleServiceAccountConfig
        ] = ...,
        oauth2_client_credentials_config: Optional[
            outputs.PluginInstanceAuthConfigOauth2ClientCredentialsConfig
        ] = ...,
        user_password_config: Optional[
            outputs.PluginInstanceAuthConfigUserPasswordConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(
        self,
    ) -> Optional[outputs.PluginInstanceAuthConfigApiKeyConfig]: ...
    @_builtins.property
    @pulumi.getter(name="googleServiceAccountConfig")
    def google_service_account_config(
        self,
    ) -> Optional[outputs.PluginInstanceAuthConfigGoogleServiceAccountConfig]: ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientCredentialsConfig")
    def oauth2_client_credentials_config(
        self,
    ) -> Optional[outputs.PluginInstanceAuthConfigOauth2ClientCredentialsConfig]: ...
    @_builtins.property
    @pulumi.getter(name="userPasswordConfig")
    def user_password_config(
        self,
    ) -> Optional[outputs.PluginInstanceAuthConfigUserPasswordConfig]: ...

@pulumi.output_type
class PluginInstanceAuthConfigApiKeyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_key: outputs.PluginInstanceAuthConfigApiKeyConfigApiKey,
        http_element_location: _builtins.str,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> outputs.PluginInstanceAuthConfigApiKeyConfigApiKey: ...
    @_builtins.property
    @pulumi.getter(name="httpElementLocation")
    def http_element_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class PluginInstanceAuthConfigApiKeyConfigApiKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class PluginInstanceAuthConfigGoogleServiceAccountConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, service_account: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str: ...

@pulumi.output_type
class PluginInstanceAuthConfigOauth2ClientCredentialsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        client_secret: outputs.PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecret,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> outputs.PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecret: ...

@pulumi.output_type
class PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecret(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class PluginInstanceAuthConfigUserPasswordConfig(dict):
    def __init__(
        __self__,
        *,
        password: outputs.PluginInstanceAuthConfigUserPasswordConfigPassword,
        username: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(
        self,
    ) -> outputs.PluginInstanceAuthConfigUserPasswordConfigPassword: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class PluginInstanceAuthConfigUserPasswordConfigPassword(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...
