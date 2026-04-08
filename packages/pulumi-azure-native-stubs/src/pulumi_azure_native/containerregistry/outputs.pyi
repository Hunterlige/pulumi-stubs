import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ActivationPropertiesResponse",
    "ActorResponse",
    "AgentPropertiesResponse",
    "ArchivePackageSourcePropertiesResponse",
    "ArgumentResponse",
    "AuthCredentialResponse",
    "AuthInfoResponse",
    "AzureADAuthenticationAsArmPolicyResponse",
    "BaseImageDependencyResponse",
    "BaseImageTriggerResponse",
    "CredentialHealthResponse",
    "CredentialsResponse",
    "CustomRegistryCredentialsResponse",
    "DockerBuildRequestResponse",
    "DockerBuildStepResponse",
    "EncodedTaskRunRequestResponse",
    "EncodedTaskStepResponse",
    "EncryptionPropertyResponse",
    "EventContentResponse",
    "EventRequestMessageResponse",
    "EventResponse",
    "EventResponseMessageResponse",
    "ExportPipelineTargetPropertiesResponse",
    "ExportPolicyResponse",
    "FileTaskRunRequestResponse",
    "FileTaskStepResponse",
    "GarbageCollectionPropertiesResponse",
    "IPRuleResponse",
    "IdentityPropertiesResponse",
    "ImageDescriptorResponse",
    "ImageUpdateTriggerResponse",
    "ImportPipelineSourcePropertiesResponse",
    "KeyVaultPropertiesResponse",
    "LoggingPropertiesResponse",
    "LoginServerPropertiesResponse",
    "NetworkRuleSetResponse",
    "OverrideTaskStepPropertiesResponse",
    "ParentPropertiesResponse",
    "PipelineRunRequestResponse",
    "PipelineRunResponseResponse",
    "PipelineRunSourcePropertiesResponse",
    "PipelineRunTargetPropertiesResponse",
    "PipelineSourceTriggerDescriptorResponse",
    "PipelineSourceTriggerPropertiesResponse",
    "PipelineTriggerDescriptorResponse",
    "PipelineTriggerPropertiesResponse",
    "PlatformPropertiesResponse",
    "PoliciesResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "ProgressPropertiesResponse",
    "QuarantinePolicyResponse",
    "RegistryPasswordResponse",
    "RequestResponse",
    "RetentionPolicyResponse",
    "RunResponse",
    "SecretObjectResponse",
    "SetValueResponse",
    "SkuResponse",
    "SoftDeletePolicyResponse",
    "SourcePropertiesResponse",
    "SourceRegistryCredentialsResponse",
    "SourceResponse",
    "SourceTriggerDescriptorResponse",
    "SourceTriggerResponse",
    "StatusDetailPropertiesResponse",
    "StatusResponse",
    "SyncPropertiesResponse",
    "SystemDataResponse",
    "TargetResponse",
    "TaskRunRequestResponse",
    "TimerTriggerDescriptorResponse",
    "TimerTriggerResponse",
    "TlsCertificatePropertiesResponse",
    "TlsPropertiesResponse",
    "TokenCertificateResponse",
    "TokenCredentialsPropertiesResponse",
    "TokenPasswordResponse",
    "TriggerPropertiesResponse",
    "TrustPolicyResponse",
    "UserIdentityPropertiesResponse",
]

@pulumi.output_type
class ActivationPropertiesResponse(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class ActorResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentPropertiesResponse(dict):
    def __init__(__self__, *, cpu: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ArchivePackageSourcePropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ArgumentResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        value: _builtins.str,
        is_secret: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isSecret")
    def is_secret(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AuthCredentialResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        credential_health: outputs.CredentialHealthResponse,
        name: Optional[_builtins.str] = ...,
        password_secret_identifier: Optional[_builtins.str] = ...,
        username_secret_identifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialHealth")
    def credential_health(self) -> outputs.CredentialHealthResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="passwordSecretIdentifier")
    def password_secret_identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usernameSecretIdentifier")
    def username_secret_identifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AuthInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        token: _builtins.str,
        token_type: _builtins.str,
        expires_in: Optional[_builtins.int] = ...,
        refresh_token: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenType")
    def token_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expiresIn")
    def expires_in(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureADAuthenticationAsArmPolicyResponse(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BaseImageDependencyResponse(dict):
    def __init__(
        __self__,
        *,
        digest: Optional[_builtins.str] = ...,
        registry: Optional[_builtins.str] = ...,
        repository: Optional[_builtins.str] = ...,
        tag: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def registry(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BaseImageTriggerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_image_trigger_type: _builtins.str,
        name: _builtins.str,
        status: Optional[_builtins.str] = ...,
        update_trigger_endpoint: Optional[_builtins.str] = ...,
        update_trigger_payload_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseImageTriggerType")
    def base_image_trigger_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTriggerEndpoint")
    def update_trigger_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTriggerPayloadType")
    def update_trigger_payload_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CredentialHealthResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_code: Optional[_builtins.str] = ...,
        error_message: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_registries: Optional[
            Mapping[str, outputs.CustomRegistryCredentialsResponse]
        ] = ...,
        source_registry: Optional[outputs.SourceRegistryCredentialsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRegistries")
    def custom_registries(
        self,
    ) -> Optional[Mapping[str, outputs.CustomRegistryCredentialsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRegistry")
    def source_registry(
        self,
    ) -> Optional[outputs.SourceRegistryCredentialsResponse]: ...

@pulumi.output_type
class CustomRegistryCredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identity: Optional[_builtins.str] = ...,
        password: Optional[outputs.SecretObjectResponse] = ...,
        user_name: Optional[outputs.SecretObjectResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[outputs.SecretObjectResponse]: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[outputs.SecretObjectResponse]: ...

@pulumi.output_type
class DockerBuildRequestResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        docker_file_path: _builtins.str,
        platform: outputs.PlatformPropertiesResponse,
        type: _builtins.str,
        agent_configuration: Optional[outputs.AgentPropertiesResponse] = ...,
        agent_pool_name: Optional[_builtins.str] = ...,
        arguments: Optional[Sequence[outputs.ArgumentResponse]] = ...,
        credentials: Optional[outputs.CredentialsResponse] = ...,
        image_names: Optional[Sequence[_builtins.str]] = ...,
        is_archive_enabled: Optional[_builtins.bool] = ...,
        is_push_enabled: Optional[_builtins.bool] = ...,
        log_template: Optional[_builtins.str] = ...,
        no_cache: Optional[_builtins.bool] = ...,
        source_location: Optional[_builtins.str] = ...,
        target: Optional[_builtins.str] = ...,
        timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dockerFilePath")
    def docker_file_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> outputs.PlatformPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional[outputs.AgentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[Sequence[outputs.ArgumentResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.CredentialsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="imageNames")
    def image_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isPushEnabled")
    def is_push_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="noCache")
    def no_cache(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DockerBuildStepResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_image_dependencies: Sequence[outputs.BaseImageDependencyResponse],
        docker_file_path: _builtins.str,
        type: _builtins.str,
        arguments: Optional[Sequence[outputs.ArgumentResponse]] = ...,
        context_access_token: Optional[_builtins.str] = ...,
        context_path: Optional[_builtins.str] = ...,
        image_names: Optional[Sequence[_builtins.str]] = ...,
        is_push_enabled: Optional[_builtins.bool] = ...,
        no_cache: Optional[_builtins.bool] = ...,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseImageDependencies")
    def base_image_dependencies(
        self,
    ) -> Sequence[outputs.BaseImageDependencyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dockerFilePath")
    def docker_file_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[Sequence[outputs.ArgumentResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="contextAccessToken")
    def context_access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageNames")
    def image_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isPushEnabled")
    def is_push_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="noCache")
    def no_cache(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EncodedTaskRunRequestResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encoded_task_content: _builtins.str,
        platform: outputs.PlatformPropertiesResponse,
        type: _builtins.str,
        agent_configuration: Optional[outputs.AgentPropertiesResponse] = ...,
        agent_pool_name: Optional[_builtins.str] = ...,
        credentials: Optional[outputs.CredentialsResponse] = ...,
        encoded_values_content: Optional[_builtins.str] = ...,
        is_archive_enabled: Optional[_builtins.bool] = ...,
        log_template: Optional[_builtins.str] = ...,
        source_location: Optional[_builtins.str] = ...,
        timeout: Optional[_builtins.int] = ...,
        values: Optional[Sequence[outputs.SetValueResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encodedTaskContent")
    def encoded_task_content(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> outputs.PlatformPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional[outputs.AgentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.CredentialsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="encodedValuesContent")
    def encoded_values_content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[outputs.SetValueResponse]]: ...

@pulumi.output_type
class EncodedTaskStepResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_image_dependencies: Sequence[outputs.BaseImageDependencyResponse],
        encoded_task_content: _builtins.str,
        type: _builtins.str,
        context_access_token: Optional[_builtins.str] = ...,
        context_path: Optional[_builtins.str] = ...,
        encoded_values_content: Optional[_builtins.str] = ...,
        values: Optional[Sequence[outputs.SetValueResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseImageDependencies")
    def base_image_dependencies(
        self,
    ) -> Sequence[outputs.BaseImageDependencyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="encodedTaskContent")
    def encoded_task_content(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contextAccessToken")
    def context_access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encodedValuesContent")
    def encoded_values_content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[outputs.SetValueResponse]]: ...

@pulumi.output_type
class EncryptionPropertyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_vault_properties: Optional[outputs.KeyVaultPropertiesResponse] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.KeyVaultPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventContentResponse(dict):
    def __init__(
        __self__,
        *,
        action: Optional[_builtins.str] = ...,
        actor: Optional[outputs.ActorResponse] = ...,
        id: Optional[_builtins.str] = ...,
        request: Optional[outputs.RequestResponse] = ...,
        source: Optional[outputs.SourceResponse] = ...,
        target: Optional[outputs.TargetResponse] = ...,
        timestamp: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def actor(self) -> Optional[outputs.ActorResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[outputs.RequestResponse]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.SourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.TargetResponse]: ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventRequestMessageResponse(dict):
    def __init__(
        __self__,
        *,
        content: Optional[outputs.EventContentResponse] = ...,
        headers: Optional[Mapping[str, _builtins.str]] = ...,
        method: Optional[_builtins.str] = ...,
        request_uri: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[outputs.EventContentResponse]: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestUri")
    def request_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventResponse(dict):
    def __init__(
        __self__,
        *,
        event_request_message: Optional[outputs.EventRequestMessageResponse] = ...,
        event_response_message: Optional[outputs.EventResponseMessageResponse] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventRequestMessage")
    def event_request_message(
        self,
    ) -> Optional[outputs.EventRequestMessageResponse]: ...
    @_builtins.property
    @pulumi.getter(name="eventResponseMessage")
    def event_response_message(
        self,
    ) -> Optional[outputs.EventResponseMessageResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventResponseMessageResponse(dict):
    def __init__(
        __self__,
        *,
        content: Optional[_builtins.str] = ...,
        headers: Optional[Mapping[str, _builtins.str]] = ...,
        reason_phrase: Optional[_builtins.str] = ...,
        status_code: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="reasonPhrase")
    def reason_phrase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExportPipelineTargetPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_vault_uri: _builtins.str,
        type: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExportPolicyResponse(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileTaskRunRequestResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        platform: outputs.PlatformPropertiesResponse,
        task_file_path: _builtins.str,
        type: _builtins.str,
        agent_configuration: Optional[outputs.AgentPropertiesResponse] = ...,
        agent_pool_name: Optional[_builtins.str] = ...,
        credentials: Optional[outputs.CredentialsResponse] = ...,
        is_archive_enabled: Optional[_builtins.bool] = ...,
        log_template: Optional[_builtins.str] = ...,
        source_location: Optional[_builtins.str] = ...,
        timeout: Optional[_builtins.int] = ...,
        values: Optional[Sequence[outputs.SetValueResponse]] = ...,
        values_file_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> outputs.PlatformPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="taskFilePath")
    def task_file_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional[outputs.AgentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.CredentialsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[outputs.SetValueResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="valuesFilePath")
    def values_file_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileTaskStepResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_image_dependencies: Sequence[outputs.BaseImageDependencyResponse],
        task_file_path: _builtins.str,
        type: _builtins.str,
        context_access_token: Optional[_builtins.str] = ...,
        context_path: Optional[_builtins.str] = ...,
        values: Optional[Sequence[outputs.SetValueResponse]] = ...,
        values_file_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseImageDependencies")
    def base_image_dependencies(
        self,
    ) -> Sequence[outputs.BaseImageDependencyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="taskFilePath")
    def task_file_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contextAccessToken")
    def context_access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[outputs.SetValueResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="valuesFilePath")
    def values_file_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GarbageCollectionPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        schedule: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IPRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        i_p_address_or_range: _builtins.str,
        action: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iPAddressOrRange")
    def i_p_address_or_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserIdentityPropertiesResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserIdentityPropertiesResponse]]: ...

@pulumi.output_type
class ImageDescriptorResponse(dict):
    def __init__(
        __self__,
        *,
        digest: Optional[_builtins.str] = ...,
        registry: Optional[_builtins.str] = ...,
        repository: Optional[_builtins.str] = ...,
        tag: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def registry(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageUpdateTriggerResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        images: Optional[Sequence[outputs.ImageDescriptorResponse]] = ...,
        timestamp: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def images(self) -> Optional[Sequence[outputs.ImageDescriptorResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImportPipelineSourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_vault_uri: _builtins.str,
        type: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyVaultPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_rotation_enabled: _builtins.bool,
        last_key_rotation_timestamp: _builtins.str,
        versioned_key_identifier: _builtins.str,
        identity: Optional[_builtins.str] = ...,
        key_identifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyRotationEnabled")
    def key_rotation_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="lastKeyRotationTimestamp")
    def last_key_rotation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionedKeyIdentifier")
    def versioned_key_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoggingPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audit_log_status: Optional[_builtins.str] = ...,
        log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogStatus")
    def audit_log_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoginServerPropertiesResponse(dict):
    def __init__(
        __self__, *, host: _builtins.str, tls: outputs.TlsPropertiesResponse
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> outputs.TlsPropertiesResponse: ...

@pulumi.output_type
class NetworkRuleSetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_action: Optional[_builtins.str] = ...,
        ip_rules: Optional[Sequence[outputs.IPRuleResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[Sequence[outputs.IPRuleResponse]]: ...

@pulumi.output_type
class OverrideTaskStepPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arguments: Optional[Sequence[outputs.ArgumentResponse]] = ...,
        context_path: Optional[_builtins.str] = ...,
        file: Optional[_builtins.str] = ...,
        target: Optional[_builtins.str] = ...,
        update_trigger_token: Optional[_builtins.str] = ...,
        values: Optional[Sequence[outputs.SetValueResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[Sequence[outputs.ArgumentResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTriggerToken")
    def update_trigger_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[outputs.SetValueResponse]]: ...

@pulumi.output_type
class ParentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sync_properties: outputs.SyncPropertiesResponse,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="syncProperties")
    def sync_properties(self) -> outputs.SyncPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineRunRequestResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifacts: Optional[Sequence[_builtins.str]] = ...,
        catalog_digest: Optional[_builtins.str] = ...,
        pipeline_resource_id: Optional[_builtins.str] = ...,
        source: Optional[outputs.PipelineRunSourcePropertiesResponse] = ...,
        target: Optional[outputs.PipelineRunTargetPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="catalogDigest")
    def catalog_digest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineResourceId")
    def pipeline_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.PipelineRunSourcePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.PipelineRunTargetPropertiesResponse]: ...

@pulumi.output_type
class PipelineRunResponseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog_digest: Optional[_builtins.str] = ...,
        finish_time: Optional[_builtins.str] = ...,
        imported_artifacts: Optional[Sequence[_builtins.str]] = ...,
        pipeline_run_error_message: Optional[_builtins.str] = ...,
        progress: Optional[outputs.ProgressPropertiesResponse] = ...,
        source: Optional[outputs.ImportPipelineSourcePropertiesResponse] = ...,
        start_time: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        target: Optional[outputs.ExportPipelineTargetPropertiesResponse] = ...,
        trigger: Optional[outputs.PipelineTriggerDescriptorResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogDigest")
    def catalog_digest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="importedArtifacts")
    def imported_artifacts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineRunErrorMessage")
    def pipeline_run_error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[outputs.ProgressPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.ImportPipelineSourcePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.ExportPipelineTargetPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[outputs.PipelineTriggerDescriptorResponse]: ...

@pulumi.output_type
class PipelineRunSourcePropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineRunTargetPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineSourceTriggerDescriptorResponse(dict):
    def __init__(__self__, *, timestamp: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineSourceTriggerPropertiesResponse(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class PipelineTriggerDescriptorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_trigger: Optional[outputs.PipelineSourceTriggerDescriptorResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTrigger")
    def source_trigger(
        self,
    ) -> Optional[outputs.PipelineSourceTriggerDescriptorResponse]: ...

@pulumi.output_type
class PipelineTriggerPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_trigger: Optional[outputs.PipelineSourceTriggerPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTrigger")
    def source_trigger(
        self,
    ) -> Optional[outputs.PipelineSourceTriggerPropertiesResponse]: ...

@pulumi.output_type
class PlatformPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        os: _builtins.str,
        architecture: Optional[_builtins.str] = ...,
        variant: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def os(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def variant(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PoliciesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_ad_authentication_as_arm_policy: Optional[
            outputs.AzureADAuthenticationAsArmPolicyResponse
        ] = ...,
        export_policy: Optional[outputs.ExportPolicyResponse] = ...,
        quarantine_policy: Optional[outputs.QuarantinePolicyResponse] = ...,
        retention_policy: Optional[outputs.RetentionPolicyResponse] = ...,
        soft_delete_policy: Optional[outputs.SoftDeletePolicyResponse] = ...,
        trust_policy: Optional[outputs.TrustPolicyResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureADAuthenticationAsArmPolicy")
    def azure_ad_authentication_as_arm_policy(
        self,
    ) -> Optional[outputs.AzureADAuthenticationAsArmPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[outputs.ExportPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="quarantinePolicy")
    def quarantine_policy(self) -> Optional[outputs.QuarantinePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[outputs.RetentionPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> Optional[outputs.SoftDeletePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="trustPolicy")
    def trust_policy(self) -> Optional[outputs.TrustPolicyResponse]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
        private_link_service_connection_state: Optional[
            outputs.PrivateLinkServiceConnectionStateResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProgressPropertiesResponse(dict):
    def __init__(__self__, *, percentage: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class QuarantinePolicyResponse(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegistryPasswordResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RequestResponse(dict):
    def __init__(
        __self__,
        *,
        addr: Optional[_builtins.str] = ...,
        host: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        method: Optional[_builtins.str] = ...,
        useragent: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def useragent(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RetentionPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_updated_time: _builtins.str,
        days: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RunResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        log_artifact: outputs.ImageDescriptorResponse,
        name: _builtins.str,
        run_error_message: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        agent_configuration: Optional[outputs.AgentPropertiesResponse] = ...,
        agent_pool_name: Optional[_builtins.str] = ...,
        create_time: Optional[_builtins.str] = ...,
        custom_registries: Optional[Sequence[_builtins.str]] = ...,
        finish_time: Optional[_builtins.str] = ...,
        image_update_trigger: Optional[outputs.ImageUpdateTriggerResponse] = ...,
        is_archive_enabled: Optional[_builtins.bool] = ...,
        last_updated_time: Optional[_builtins.str] = ...,
        output_images: Optional[Sequence[outputs.ImageDescriptorResponse]] = ...,
        platform: Optional[outputs.PlatformPropertiesResponse] = ...,
        provisioning_state: Optional[_builtins.str] = ...,
        run_id: Optional[_builtins.str] = ...,
        run_type: Optional[_builtins.str] = ...,
        source_registry_auth: Optional[_builtins.str] = ...,
        source_trigger: Optional[outputs.SourceTriggerDescriptorResponse] = ...,
        start_time: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        task: Optional[_builtins.str] = ...,
        timer_trigger: Optional[outputs.TimerTriggerDescriptorResponse] = ...,
        update_trigger_token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logArtifact")
    def log_artifact(self) -> outputs.ImageDescriptorResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runErrorMessage")
    def run_error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional[outputs.AgentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customRegistries")
    def custom_registries(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageUpdateTrigger")
    def image_update_trigger(self) -> Optional[outputs.ImageUpdateTriggerResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputImages")
    def output_images(self) -> Optional[Sequence[outputs.ImageDescriptorResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[outputs.PlatformPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runId")
    def run_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runType")
    def run_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRegistryAuth")
    def source_registry_auth(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceTrigger")
    def source_trigger(self) -> Optional[outputs.SourceTriggerDescriptorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def task(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timerTrigger")
    def timer_trigger(self) -> Optional[outputs.TimerTriggerDescriptorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="updateTriggerToken")
    def update_trigger_token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecretObjectResponse(dict):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SetValueResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        value: _builtins.str,
        is_secret: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isSecret")
    def is_secret(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *, name: _builtins.str, tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str: ...

@pulumi.output_type
class SoftDeletePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_updated_time: _builtins.str,
        retention_days: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        repository_url: _builtins.str,
        source_control_type: _builtins.str,
        branch: Optional[_builtins.str] = ...,
        source_control_auth_properties: Optional[outputs.AuthInfoResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceControlType")
    def source_control_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceControlAuthProperties")
    def source_control_auth_properties(self) -> Optional[outputs.AuthInfoResponse]: ...

@pulumi.output_type
class SourceRegistryCredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, login_mode: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginMode")
    def login_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SourceResponse(dict):
    def __init__(
        __self__,
        *,
        addr: Optional[_builtins.str] = ...,
        instance_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceID")
    def instance_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SourceTriggerDescriptorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        branch_name: Optional[_builtins.str] = ...,
        commit_id: Optional[_builtins.str] = ...,
        event_type: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        provider_type: Optional[_builtins.str] = ...,
        pull_request_id: Optional[_builtins.str] = ...,
        repository_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="commitId")
    def commit_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pullRequestId")
    def pull_request_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SourceTriggerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        source_repository: outputs.SourcePropertiesResponse,
        source_trigger_events: Sequence[_builtins.str],
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> outputs.SourcePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="sourceTriggerEvents")
    def source_trigger_events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StatusDetailPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        correlation_id: _builtins.str,
        description: _builtins.str,
        timestamp: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class StatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_status: _builtins.str,
        message: _builtins.str,
        timestamp: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> _builtins.str: ...

@pulumi.output_type
class SyncPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gateway_endpoint: _builtins.str,
        last_sync_time: _builtins.str,
        message_ttl: _builtins.str,
        token_id: _builtins.str,
        schedule: Optional[_builtins.str] = ...,
        sync_window: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gatewayEndpoint")
    def gateway_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messageTtl")
    def message_ttl(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenId")
    def token_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncWindow")
    def sync_window(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetResponse(dict):
    def __init__(
        __self__,
        *,
        digest: Optional[_builtins.str] = ...,
        length: Optional[_builtins.float] = ...,
        media_type: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        repository: Optional[_builtins.str] = ...,
        size: Optional[_builtins.float] = ...,
        tag: Optional[_builtins.str] = ...,
        url: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskRunRequestResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        task_id: _builtins.str,
        type: _builtins.str,
        agent_pool_name: Optional[_builtins.str] = ...,
        is_archive_enabled: Optional[_builtins.bool] = ...,
        log_template: Optional[_builtins.str] = ...,
        override_task_step_properties: Optional[
            outputs.OverrideTaskStepPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overrideTaskStepProperties")
    def override_task_step_properties(
        self,
    ) -> Optional[outputs.OverrideTaskStepPropertiesResponse]: ...

@pulumi.output_type
class TimerTriggerDescriptorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule_occurrence: Optional[_builtins.str] = ...,
        timer_trigger_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleOccurrence")
    def schedule_occurrence(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timerTriggerName")
    def timer_trigger_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TimerTriggerResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        schedule: _builtins.str,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TlsCertificatePropertiesResponse(dict):
    def __init__(__self__, *, location: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class TlsPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        certificate: outputs.TlsCertificatePropertiesResponse,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> outputs.TlsCertificatePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class TokenCertificateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encoded_pem_certificate: Optional[_builtins.str] = ...,
        expiry: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        thumbprint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encodedPemCertificate")
    def encoded_pem_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def expiry(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TokenCredentialsPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        certificates: Optional[Sequence[outputs.TokenCertificateResponse]] = ...,
        passwords: Optional[Sequence[outputs.TokenPasswordResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[outputs.TokenCertificateResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def passwords(self) -> Optional[Sequence[outputs.TokenPasswordResponse]]: ...

@pulumi.output_type
class TokenPasswordResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        value: _builtins.str,
        creation_time: Optional[_builtins.str] = ...,
        expiry: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def expiry(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TriggerPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_image_trigger: Optional[outputs.BaseImageTriggerResponse] = ...,
        source_triggers: Optional[Sequence[outputs.SourceTriggerResponse]] = ...,
        timer_triggers: Optional[Sequence[outputs.TimerTriggerResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseImageTrigger")
    def base_image_trigger(self) -> Optional[outputs.BaseImageTriggerResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sourceTriggers")
    def source_triggers(self) -> Optional[Sequence[outputs.SourceTriggerResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="timerTriggers")
    def timer_triggers(self) -> Optional[Sequence[outputs.TimerTriggerResponse]]: ...

@pulumi.output_type
class TrustPolicyResponse(dict):
    def __init__(
        __self__,
        *,
        status: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserIdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        principal_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
