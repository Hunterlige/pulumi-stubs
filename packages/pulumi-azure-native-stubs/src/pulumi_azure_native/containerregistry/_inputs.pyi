import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgentPropertiesArgs",
    "AgentPropertiesArgsDict",
    "ArchivePackageSourcePropertiesArgs",
    "ArchivePackageSourcePropertiesArgsDict",
    "ArgumentArgs",
    "ArgumentArgsDict",
    "AuthCredentialArgs",
    "AuthCredentialArgsDict",
    "AuthInfoArgs",
    "AuthInfoArgsDict",
    "AzureADAuthenticationAsArmPolicyArgs",
    "AzureADAuthenticationAsArmPolicyArgsDict",
    "BaseImageTriggerArgs",
    "BaseImageTriggerArgsDict",
    "CredentialsArgs",
    "CredentialsArgsDict",
    "CustomRegistryCredentialsArgs",
    "CustomRegistryCredentialsArgsDict",
    "DockerBuildRequestArgs",
    "DockerBuildRequestArgsDict",
    "DockerBuildStepArgs",
    "DockerBuildStepArgsDict",
    "EncodedTaskRunRequestArgs",
    "EncodedTaskRunRequestArgsDict",
    "EncodedTaskStepArgs",
    "EncodedTaskStepArgsDict",
    "EncryptionPropertyArgs",
    "EncryptionPropertyArgsDict",
    "ExportPipelineTargetPropertiesArgs",
    "ExportPipelineTargetPropertiesArgsDict",
    "ExportPolicyArgs",
    "ExportPolicyArgsDict",
    "FileTaskRunRequestArgs",
    "FileTaskRunRequestArgsDict",
    "FileTaskStepArgs",
    "FileTaskStepArgsDict",
    "GarbageCollectionPropertiesArgs",
    "GarbageCollectionPropertiesArgsDict",
    "IPRuleArgs",
    "IPRuleArgsDict",
    "IdentityPropertiesArgs",
    "IdentityPropertiesArgsDict",
    "ImportPipelineSourcePropertiesArgs",
    "ImportPipelineSourcePropertiesArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "LoggingPropertiesArgs",
    "LoggingPropertiesArgsDict",
    "NetworkRuleSetArgs",
    "NetworkRuleSetArgsDict",
    "OverrideTaskStepPropertiesArgs",
    "OverrideTaskStepPropertiesArgsDict",
    "ParentPropertiesArgs",
    "ParentPropertiesArgsDict",
    "PipelineRunRequestArgs",
    "PipelineRunRequestArgsDict",
    "PipelineRunSourcePropertiesArgs",
    "PipelineRunSourcePropertiesArgsDict",
    "PipelineRunTargetPropertiesArgs",
    "PipelineRunTargetPropertiesArgsDict",
    "PipelineSourceTriggerPropertiesArgs",
    "PipelineSourceTriggerPropertiesArgsDict",
    "PipelineTriggerPropertiesArgs",
    "PipelineTriggerPropertiesArgsDict",
    "PlatformPropertiesArgs",
    "PlatformPropertiesArgsDict",
    "PoliciesArgs",
    "PoliciesArgsDict",
    "PrivateEndpointArgs",
    "PrivateEndpointArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "QuarantinePolicyArgs",
    "QuarantinePolicyArgsDict",
    "RetentionPolicyArgs",
    "RetentionPolicyArgsDict",
    "SecretObjectArgs",
    "SecretObjectArgsDict",
    "SetValueArgs",
    "SetValueArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SoftDeletePolicyArgs",
    "SoftDeletePolicyArgsDict",
    "SourcePropertiesArgs",
    "SourcePropertiesArgsDict",
    "SourceRegistryCredentialsArgs",
    "SourceRegistryCredentialsArgsDict",
    "SourceTriggerArgs",
    "SourceTriggerArgsDict",
    "SyncPropertiesArgs",
    "SyncPropertiesArgsDict",
    "TaskRunRequestArgs",
    "TaskRunRequestArgsDict",
    "TimerTriggerArgs",
    "TimerTriggerArgsDict",
    "TokenCertificateArgs",
    "TokenCertificateArgsDict",
    "TokenCredentialsPropertiesArgs",
    "TokenCredentialsPropertiesArgsDict",
    "TokenPasswordArgs",
    "TokenPasswordArgsDict",
    "TriggerPropertiesArgs",
    "TriggerPropertiesArgsDict",
    "TrustPolicyArgs",
    "TrustPolicyArgsDict",
    "UserIdentityPropertiesArgs",
    "UserIdentityPropertiesArgsDict",
]

class AgentPropertiesArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AgentPropertiesArgs:
    def __init__(
        __self__, *, cpu: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ArchivePackageSourcePropertiesArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, PackageSourceType]]]
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArchivePackageSourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, PackageSourceType]]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PackageSourceType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PackageSourceType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ArgumentArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    is_secret: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ArgumentArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        is_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isSecret")
    def is_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_secret.setter
    def is_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AuthCredentialArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[Union[_builtins.str, CredentialName]]]
    password_secret_identifier: NotRequired[pulumi.Input[_builtins.str]]
    username_secret_identifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AuthCredentialArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[Union[_builtins.str, CredentialName]]] = ...,
        password_secret_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        username_secret_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, CredentialName]]]: ...
    @name.setter
    def name(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CredentialName]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="passwordSecretIdentifier")
    def password_secret_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_secret_identifier.setter
    def password_secret_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usernameSecretIdentifier")
    def username_secret_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username_secret_identifier.setter
    def username_secret_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class AuthInfoArgsDict(TypedDict):
    token: pulumi.Input[_builtins.str]
    token_type: pulumi.Input[Union[_builtins.str, TokenType]]
    expires_in: NotRequired[pulumi.Input[_builtins.int]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AuthInfoArgs:
    def __init__(
        __self__,
        *,
        token: pulumi.Input[_builtins.str],
        token_type: pulumi.Input[Union[_builtins.str, TokenType]],
        expires_in: Optional[pulumi.Input[_builtins.int]] = ...,
        refresh_token: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> pulumi.Input[_builtins.str]: ...
    @token.setter
    def token(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tokenType")
    def token_type(self) -> pulumi.Input[Union[_builtins.str, TokenType]]: ...
    @token_type.setter
    def token_type(self, value: pulumi.Input[Union[_builtins.str, TokenType]]): ...
    @_builtins.property
    @pulumi.getter(name="expiresIn")
    def expires_in(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @expires_in.setter
    def expires_in(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureADAuthenticationAsArmPolicyArgsDict(TypedDict):
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, AzureADAuthenticationAsArmPolicyStatus]]
    ]

@pulumi.input_type
class AzureADAuthenticationAsArmPolicyArgs:
    def __init__(
        __self__,
        *,
        status: Optional[
            pulumi.Input[Union[_builtins.str, AzureADAuthenticationAsArmPolicyStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, AzureADAuthenticationAsArmPolicyStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, AzureADAuthenticationAsArmPolicyStatus]]
        ],
    ): ...

class BaseImageTriggerArgsDict(TypedDict):
    base_image_trigger_type: pulumi.Input[Union[_builtins.str, BaseImageTriggerType]]
    name: pulumi.Input[_builtins.str]
    status: NotRequired[pulumi.Input[Union[_builtins.str, TriggerStatus]]]
    update_trigger_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    update_trigger_payload_type: NotRequired[
        pulumi.Input[Union[_builtins.str, UpdateTriggerPayloadType]]
    ]

@pulumi.input_type
class BaseImageTriggerArgs:
    def __init__(
        __self__,
        *,
        base_image_trigger_type: pulumi.Input[
            Union[_builtins.str, BaseImageTriggerType]
        ],
        name: pulumi.Input[_builtins.str],
        status: Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]] = ...,
        update_trigger_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        update_trigger_payload_type: Optional[
            pulumi.Input[Union[_builtins.str, UpdateTriggerPayloadType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseImageTriggerType")
    def base_image_trigger_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, BaseImageTriggerType]]: ...
    @base_image_trigger_type.setter
    def base_image_trigger_type(
        self, value: pulumi.Input[Union[_builtins.str, BaseImageTriggerType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTriggerEndpoint")
    def update_trigger_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_trigger_endpoint.setter
    def update_trigger_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTriggerPayloadType")
    def update_trigger_payload_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, UpdateTriggerPayloadType]]]: ...
    @update_trigger_payload_type.setter
    def update_trigger_payload_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, UpdateTriggerPayloadType]]],
    ): ...

class CredentialsArgsDict(TypedDict):
    custom_registries: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[CustomRegistryCredentialsArgsDict]]]
    ]
    source_registry: NotRequired[pulumi.Input[SourceRegistryCredentialsArgsDict]]

@pulumi.input_type
class CredentialsArgs:
    def __init__(
        __self__,
        *,
        custom_registries: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[CustomRegistryCredentialsArgs]]]
        ] = ...,
        source_registry: Optional[pulumi.Input[SourceRegistryCredentialsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRegistries")
    def custom_registries(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[CustomRegistryCredentialsArgs]]]
    ]: ...
    @custom_registries.setter
    def custom_registries(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[CustomRegistryCredentialsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceRegistry")
    def source_registry(
        self,
    ) -> Optional[pulumi.Input[SourceRegistryCredentialsArgs]]: ...
    @source_registry.setter
    def source_registry(
        self, value: Optional[pulumi.Input[SourceRegistryCredentialsArgs]]
    ): ...

class CustomRegistryCredentialsArgsDict(TypedDict):
    identity: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[SecretObjectArgsDict]]
    user_name: NotRequired[pulumi.Input[SecretObjectArgsDict]]

@pulumi.input_type
class CustomRegistryCredentialsArgs:
    def __init__(
        __self__,
        *,
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[SecretObjectArgs]] = ...,
        user_name: Optional[pulumi.Input[SecretObjectArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[SecretObjectArgs]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[SecretObjectArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[SecretObjectArgs]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[SecretObjectArgs]]): ...

class DockerBuildRequestArgsDict(TypedDict):
    docker_file_path: pulumi.Input[_builtins.str]
    platform: pulumi.Input[PlatformPropertiesArgsDict]
    type: pulumi.Input[_builtins.str]
    agent_configuration: NotRequired[pulumi.Input[AgentPropertiesArgsDict]]
    agent_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    arguments: NotRequired[pulumi.Input[Sequence[pulumi.Input[ArgumentArgsDict]]]]
    credentials: NotRequired[pulumi.Input[CredentialsArgsDict]]
    image_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_push_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_template: NotRequired[pulumi.Input[_builtins.str]]
    no_cache: NotRequired[pulumi.Input[_builtins.bool]]
    source_location: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DockerBuildRequestArgs:
    def __init__(
        __self__,
        *,
        docker_file_path: pulumi.Input[_builtins.str],
        platform: pulumi.Input[PlatformPropertiesArgs],
        type: pulumi.Input[_builtins.str],
        agent_configuration: Optional[pulumi.Input[AgentPropertiesArgs]] = ...,
        agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        arguments: Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]] = ...,
        credentials: Optional[pulumi.Input[CredentialsArgs]] = ...,
        image_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_push_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_template: Optional[pulumi.Input[_builtins.str]] = ...,
        no_cache: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_location: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dockerFilePath")
    def docker_file_path(self) -> pulumi.Input[_builtins.str]: ...
    @docker_file_path.setter
    def docker_file_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Input[PlatformPropertiesArgs]: ...
    @platform.setter
    def platform(self, value: pulumi.Input[PlatformPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional[pulumi.Input[AgentPropertiesArgs]]: ...
    @agent_configuration.setter
    def agent_configuration(
        self, value: Optional[pulumi.Input[AgentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_pool_name.setter
    def agent_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arguments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]]: ...
    @arguments.setter
    def arguments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[CredentialsArgs]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[CredentialsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="imageNames")
    def image_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @image_names.setter
    def image_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isPushEnabled")
    def is_push_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_push_enabled.setter
    def is_push_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_template.setter
    def log_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="noCache")
    def no_cache(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_cache.setter
    def no_cache(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_location.setter
    def source_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DockerBuildStepArgsDict(TypedDict):
    docker_file_path: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    arguments: NotRequired[pulumi.Input[Sequence[pulumi.Input[ArgumentArgsDict]]]]
    context_access_token: NotRequired[pulumi.Input[_builtins.str]]
    context_path: NotRequired[pulumi.Input[_builtins.str]]
    image_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_push_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    no_cache: NotRequired[pulumi.Input[_builtins.bool]]
    target: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DockerBuildStepArgs:
    def __init__(
        __self__,
        *,
        docker_file_path: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        arguments: Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]] = ...,
        context_access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        context_path: Optional[pulumi.Input[_builtins.str]] = ...,
        image_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_push_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_cache: Optional[pulumi.Input[_builtins.bool]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dockerFilePath")
    def docker_file_path(self) -> pulumi.Input[_builtins.str]: ...
    @docker_file_path.setter
    def docker_file_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def arguments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]]: ...
    @arguments.setter
    def arguments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contextAccessToken")
    def context_access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context_access_token.setter
    def context_access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context_path.setter
    def context_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageNames")
    def image_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @image_names.setter
    def image_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isPushEnabled")
    def is_push_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_push_enabled.setter
    def is_push_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="noCache")
    def no_cache(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_cache.setter
    def no_cache(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EncodedTaskRunRequestArgsDict(TypedDict):
    encoded_task_content: pulumi.Input[_builtins.str]
    platform: pulumi.Input[PlatformPropertiesArgsDict]
    type: pulumi.Input[_builtins.str]
    agent_configuration: NotRequired[pulumi.Input[AgentPropertiesArgsDict]]
    agent_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    credentials: NotRequired[pulumi.Input[CredentialsArgsDict]]
    encoded_values_content: NotRequired[pulumi.Input[_builtins.str]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_template: NotRequired[pulumi.Input[_builtins.str]]
    source_location: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.int]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[SetValueArgsDict]]]]

@pulumi.input_type
class EncodedTaskRunRequestArgs:
    def __init__(
        __self__,
        *,
        encoded_task_content: pulumi.Input[_builtins.str],
        platform: pulumi.Input[PlatformPropertiesArgs],
        type: pulumi.Input[_builtins.str],
        agent_configuration: Optional[pulumi.Input[AgentPropertiesArgs]] = ...,
        agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[pulumi.Input[CredentialsArgs]] = ...,
        encoded_values_content: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_template: Optional[pulumi.Input[_builtins.str]] = ...,
        source_location: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encodedTaskContent")
    def encoded_task_content(self) -> pulumi.Input[_builtins.str]: ...
    @encoded_task_content.setter
    def encoded_task_content(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Input[PlatformPropertiesArgs]: ...
    @platform.setter
    def platform(self, value: pulumi.Input[PlatformPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional[pulumi.Input[AgentPropertiesArgs]]: ...
    @agent_configuration.setter
    def agent_configuration(
        self, value: Optional[pulumi.Input[AgentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_pool_name.setter
    def agent_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[CredentialsArgs]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[CredentialsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="encodedValuesContent")
    def encoded_values_content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoded_values_content.setter
    def encoded_values_content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_template.setter
    def log_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_location.setter
    def source_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]
    ): ...

class EncodedTaskStepArgsDict(TypedDict):
    encoded_task_content: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    context_access_token: NotRequired[pulumi.Input[_builtins.str]]
    context_path: NotRequired[pulumi.Input[_builtins.str]]
    encoded_values_content: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[SetValueArgsDict]]]]

@pulumi.input_type
class EncodedTaskStepArgs:
    def __init__(
        __self__,
        *,
        encoded_task_content: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        context_access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        context_path: Optional[pulumi.Input[_builtins.str]] = ...,
        encoded_values_content: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encodedTaskContent")
    def encoded_task_content(self) -> pulumi.Input[_builtins.str]: ...
    @encoded_task_content.setter
    def encoded_task_content(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contextAccessToken")
    def context_access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context_access_token.setter
    def context_access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context_path.setter
    def context_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encodedValuesContent")
    def encoded_values_content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoded_values_content.setter
    def encoded_values_content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]
    ): ...

class EncryptionPropertyArgsDict(TypedDict):
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, EncryptionStatus]]]

@pulumi.input_type
class EncryptionPropertyArgs:
    def __init__(
        __self__,
        *,
        key_vault_properties: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, EncryptionStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(
        self,
    ) -> Optional[pulumi.Input[KeyVaultPropertiesArgs]]: ...
    @key_vault_properties.setter
    def key_vault_properties(
        self, value: Optional[pulumi.Input[KeyVaultPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionStatus]]]
    ): ...

class ExportPipelineTargetPropertiesArgsDict(TypedDict):
    key_vault_uri: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExportPipelineTargetPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_vault_uri: pulumi.Input[_builtins.str],
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExportPolicyArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[Union[_builtins.str, ExportPolicyStatus]]]

@pulumi.input_type
class ExportPolicyArgs:
    def __init__(
        __self__,
        *,
        status: Optional[pulumi.Input[Union[_builtins.str, ExportPolicyStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ExportPolicyStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ExportPolicyStatus]]]
    ): ...

class FileTaskRunRequestArgsDict(TypedDict):
    platform: pulumi.Input[PlatformPropertiesArgsDict]
    task_file_path: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    agent_configuration: NotRequired[pulumi.Input[AgentPropertiesArgsDict]]
    agent_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    credentials: NotRequired[pulumi.Input[CredentialsArgsDict]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_template: NotRequired[pulumi.Input[_builtins.str]]
    source_location: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.int]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[SetValueArgsDict]]]]
    values_file_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FileTaskRunRequestArgs:
    def __init__(
        __self__,
        *,
        platform: pulumi.Input[PlatformPropertiesArgs],
        task_file_path: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        agent_configuration: Optional[pulumi.Input[AgentPropertiesArgs]] = ...,
        agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[pulumi.Input[CredentialsArgs]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_template: Optional[pulumi.Input[_builtins.str]] = ...,
        source_location: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]] = ...,
        values_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Input[PlatformPropertiesArgs]: ...
    @platform.setter
    def platform(self, value: pulumi.Input[PlatformPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="taskFilePath")
    def task_file_path(self) -> pulumi.Input[_builtins.str]: ...
    @task_file_path.setter
    def task_file_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional[pulumi.Input[AgentPropertiesArgs]]: ...
    @agent_configuration.setter
    def agent_configuration(
        self, value: Optional[pulumi.Input[AgentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_pool_name.setter
    def agent_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[CredentialsArgs]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[CredentialsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_template.setter
    def log_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_location.setter
    def source_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="valuesFilePath")
    def values_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @values_file_path.setter
    def values_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FileTaskStepArgsDict(TypedDict):
    task_file_path: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    context_access_token: NotRequired[pulumi.Input[_builtins.str]]
    context_path: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[SetValueArgsDict]]]]
    values_file_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FileTaskStepArgs:
    def __init__(
        __self__,
        *,
        task_file_path: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        context_access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        context_path: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]] = ...,
        values_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskFilePath")
    def task_file_path(self) -> pulumi.Input[_builtins.str]: ...
    @task_file_path.setter
    def task_file_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contextAccessToken")
    def context_access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context_access_token.setter
    def context_access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context_path.setter
    def context_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="valuesFilePath")
    def values_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @values_file_path.setter
    def values_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GarbageCollectionPropertiesArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    schedule: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GarbageCollectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IPRuleArgsDict(TypedDict):
    i_p_address_or_range: pulumi.Input[_builtins.str]
    action: NotRequired[pulumi.Input[Union[_builtins.str, Action]]]

@pulumi.input_type
class IPRuleArgs:
    def __init__(
        __self__,
        *,
        i_p_address_or_range: pulumi.Input[_builtins.str],
        action: Optional[pulumi.Input[Union[_builtins.str, Action]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iPAddressOrRange")
    def i_p_address_or_range(self) -> pulumi.Input[_builtins.str]: ...
    @i_p_address_or_range.setter
    def i_p_address_or_range(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, Action]]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[Union[_builtins.str, Action]]]): ...

class IdentityPropertiesArgsDict(TypedDict):
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgsDict]]]
    ]

@pulumi.input_type
class IdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[ResourceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgs]]]
    ]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgs]]]
        ],
    ): ...

class ImportPipelineSourcePropertiesArgsDict(TypedDict):
    key_vault_uri: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[Union[_builtins.str, PipelineSourceType]]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImportPipelineSourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        key_vault_uri: pulumi.Input[_builtins.str],
        type: Optional[pulumi.Input[Union[_builtins.str, PipelineSourceType]]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PipelineSourceType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PipelineSourceType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyVaultPropertiesArgsDict(TypedDict):
    identity: NotRequired[pulumi.Input[_builtins.str]]
    key_identifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
        key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_identifier.setter
    def key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LoggingPropertiesArgsDict(TypedDict):
    audit_log_status: NotRequired[pulumi.Input[Union[_builtins.str, AuditLogStatus]]]
    log_level: NotRequired[pulumi.Input[Union[_builtins.str, LogLevel]]]

@pulumi.input_type
class LoggingPropertiesArgs:
    def __init__(
        __self__,
        *,
        audit_log_status: Optional[
            pulumi.Input[Union[_builtins.str, AuditLogStatus]]
        ] = ...,
        log_level: Optional[pulumi.Input[Union[_builtins.str, LogLevel]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogStatus")
    def audit_log_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AuditLogStatus]]]: ...
    @audit_log_status.setter
    def audit_log_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuditLogStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[Union[_builtins.str, LogLevel]]]: ...
    @log_level.setter
    def log_level(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogLevel]]]
    ): ...

class NetworkRuleSetArgsDict(TypedDict):
    default_action: pulumi.Input[Union[_builtins.str, DefaultAction]]
    ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[IPRuleArgsDict]]]]

@pulumi.input_type
class NetworkRuleSetArgs:
    def __init__(
        __self__,
        *,
        default_action: Optional[
            pulumi.Input[Union[_builtins.str, DefaultAction]]
        ] = ...,
        ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[Union[_builtins.str, DefaultAction]]: ...
    @default_action.setter
    def default_action(
        self, value: pulumi.Input[Union[_builtins.str, DefaultAction]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]: ...
    @ip_rules.setter
    def ip_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]
    ): ...

class OverrideTaskStepPropertiesArgsDict(TypedDict):
    arguments: NotRequired[pulumi.Input[Sequence[pulumi.Input[ArgumentArgsDict]]]]
    context_path: NotRequired[pulumi.Input[_builtins.str]]
    file: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    update_trigger_token: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[SetValueArgsDict]]]]

@pulumi.input_type
class OverrideTaskStepPropertiesArgs:
    def __init__(
        __self__,
        *,
        arguments: Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]] = ...,
        context_path: Optional[pulumi.Input[_builtins.str]] = ...,
        file: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        update_trigger_token: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arguments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]]: ...
    @arguments.setter
    def arguments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ArgumentArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context_path.setter
    def context_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file.setter
    def file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTriggerToken")
    def update_trigger_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_trigger_token.setter
    def update_trigger_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SetValueArgs]]]]
    ): ...

class ParentPropertiesArgsDict(TypedDict):
    sync_properties: pulumi.Input[SyncPropertiesArgsDict]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ParentPropertiesArgs:
    def __init__(
        __self__,
        *,
        sync_properties: pulumi.Input[SyncPropertiesArgs],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="syncProperties")
    def sync_properties(self) -> pulumi.Input[SyncPropertiesArgs]: ...
    @sync_properties.setter
    def sync_properties(self, value: pulumi.Input[SyncPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineRunRequestArgsDict(TypedDict):
    artifacts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    catalog_digest: NotRequired[pulumi.Input[_builtins.str]]
    pipeline_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[PipelineRunSourcePropertiesArgsDict]]
    target: NotRequired[pulumi.Input[PipelineRunTargetPropertiesArgsDict]]

@pulumi.input_type
class PipelineRunRequestArgs:
    def __init__(
        __self__,
        *,
        artifacts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        catalog_digest: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[PipelineRunSourcePropertiesArgs]] = ...,
        target: Optional[pulumi.Input[PipelineRunTargetPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @artifacts.setter
    def artifacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="catalogDigest")
    def catalog_digest(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_digest.setter
    def catalog_digest(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineResourceId")
    def pipeline_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pipeline_resource_id.setter
    def pipeline_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[PipelineRunSourcePropertiesArgs]]: ...
    @source.setter
    def source(
        self, value: Optional[pulumi.Input[PipelineRunSourcePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[PipelineRunTargetPropertiesArgs]]: ...
    @target.setter
    def target(
        self, value: Optional[pulumi.Input[PipelineRunTargetPropertiesArgs]]
    ): ...

class PipelineRunSourcePropertiesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, PipelineRunSourceType]]]

@pulumi.input_type
class PipelineRunSourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, PipelineRunSourceType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PipelineRunSourceType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PipelineRunSourceType]]]
    ): ...

class PipelineRunTargetPropertiesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, PipelineRunTargetType]]]

@pulumi.input_type
class PipelineRunTargetPropertiesArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, PipelineRunTargetType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PipelineRunTargetType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PipelineRunTargetType]]]
    ): ...

class PipelineSourceTriggerPropertiesArgsDict(TypedDict):
    status: pulumi.Input[Union[_builtins.str, TriggerStatus]]

@pulumi.input_type
class PipelineSourceTriggerPropertiesArgs:
    def __init__(
        __self__,
        *,
        status: Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, TriggerStatus]]: ...
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, TriggerStatus]]): ...

class PipelineTriggerPropertiesArgsDict(TypedDict):
    source_trigger: NotRequired[pulumi.Input[PipelineSourceTriggerPropertiesArgsDict]]

@pulumi.input_type
class PipelineTriggerPropertiesArgs:
    def __init__(
        __self__,
        *,
        source_trigger: Optional[
            pulumi.Input[PipelineSourceTriggerPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTrigger")
    def source_trigger(
        self,
    ) -> Optional[pulumi.Input[PipelineSourceTriggerPropertiesArgs]]: ...
    @source_trigger.setter
    def source_trigger(
        self, value: Optional[pulumi.Input[PipelineSourceTriggerPropertiesArgs]]
    ): ...

class PlatformPropertiesArgsDict(TypedDict):
    os: pulumi.Input[Union[_builtins.str, OS]]
    architecture: NotRequired[pulumi.Input[Union[_builtins.str, Architecture]]]
    variant: NotRequired[pulumi.Input[Union[_builtins.str, Variant]]]

@pulumi.input_type
class PlatformPropertiesArgs:
    def __init__(
        __self__,
        *,
        os: pulumi.Input[Union[_builtins.str, OS]],
        architecture: Optional[pulumi.Input[Union[_builtins.str, Architecture]]] = ...,
        variant: Optional[pulumi.Input[Union[_builtins.str, Variant]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def os(self) -> pulumi.Input[Union[_builtins.str, OS]]: ...
    @os.setter
    def os(self, value: pulumi.Input[Union[_builtins.str, OS]]): ...
    @_builtins.property
    @pulumi.getter
    def architecture(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, Architecture]]]: ...
    @architecture.setter
    def architecture(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Architecture]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def variant(self) -> Optional[pulumi.Input[Union[_builtins.str, Variant]]]: ...
    @variant.setter
    def variant(self, value: Optional[pulumi.Input[Union[_builtins.str, Variant]]]): ...

class PoliciesArgsDict(TypedDict):
    azure_ad_authentication_as_arm_policy: NotRequired[
        pulumi.Input[AzureADAuthenticationAsArmPolicyArgsDict]
    ]
    export_policy: NotRequired[pulumi.Input[ExportPolicyArgsDict]]
    quarantine_policy: NotRequired[pulumi.Input[QuarantinePolicyArgsDict]]
    retention_policy: NotRequired[pulumi.Input[RetentionPolicyArgsDict]]
    soft_delete_policy: NotRequired[pulumi.Input[SoftDeletePolicyArgsDict]]
    trust_policy: NotRequired[pulumi.Input[TrustPolicyArgsDict]]

@pulumi.input_type
class PoliciesArgs:
    def __init__(
        __self__,
        *,
        azure_ad_authentication_as_arm_policy: Optional[
            pulumi.Input[AzureADAuthenticationAsArmPolicyArgs]
        ] = ...,
        export_policy: Optional[pulumi.Input[ExportPolicyArgs]] = ...,
        quarantine_policy: Optional[pulumi.Input[QuarantinePolicyArgs]] = ...,
        retention_policy: Optional[pulumi.Input[RetentionPolicyArgs]] = ...,
        soft_delete_policy: Optional[pulumi.Input[SoftDeletePolicyArgs]] = ...,
        trust_policy: Optional[pulumi.Input[TrustPolicyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureADAuthenticationAsArmPolicy")
    def azure_ad_authentication_as_arm_policy(
        self,
    ) -> Optional[pulumi.Input[AzureADAuthenticationAsArmPolicyArgs]]: ...
    @azure_ad_authentication_as_arm_policy.setter
    def azure_ad_authentication_as_arm_policy(
        self, value: Optional[pulumi.Input[AzureADAuthenticationAsArmPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input[ExportPolicyArgs]]: ...
    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input[ExportPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="quarantinePolicy")
    def quarantine_policy(self) -> Optional[pulumi.Input[QuarantinePolicyArgs]]: ...
    @quarantine_policy.setter
    def quarantine_policy(
        self, value: Optional[pulumi.Input[QuarantinePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[RetentionPolicyArgs]]: ...
    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input[RetentionPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> Optional[pulumi.Input[SoftDeletePolicyArgs]]: ...
    @soft_delete_policy.setter
    def soft_delete_policy(
        self, value: Optional[pulumi.Input[SoftDeletePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustPolicy")
    def trust_policy(self) -> Optional[pulumi.Input[TrustPolicyArgs]]: ...
    @trust_policy.setter
    def trust_policy(self, value: Optional[pulumi.Input[TrustPolicyArgs]]): ...

class PrivateEndpointArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[Union[_builtins.str, ActionsRequired]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionStatus]]]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[
            pulumi.Input[Union[_builtins.str, ActionsRequired]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, ConnectionStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ActionsRequired]]]: ...
    @actions_required.setter
    def actions_required(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ActionsRequired]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionStatus]]]
    ): ...

class QuarantinePolicyArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[Union[_builtins.str, PolicyStatus]]]

@pulumi.input_type
class QuarantinePolicyArgs:
    def __init__(
        __self__,
        *,
        status: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]
    ): ...

class RetentionPolicyArgsDict(TypedDict):
    days: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PolicyStatus]]]

@pulumi.input_type
class RetentionPolicyArgs:
    def __init__(
        __self__,
        *,
        days: Optional[pulumi.Input[_builtins.int]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]
    ): ...

class SecretObjectArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, SecretObjectType]]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecretObjectArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, SecretObjectType]]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecretObjectType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecretObjectType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SetValueArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    is_secret: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class SetValueArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        is_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isSecret")
    def is_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_secret.setter
    def is_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__, *, name: pulumi.Input[Union[_builtins.str, SkuName]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...

class SoftDeletePolicyArgsDict(TypedDict):
    retention_days: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PolicyStatus]]]

@pulumi.input_type
class SoftDeletePolicyArgs:
    def __init__(
        __self__,
        *,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]
    ): ...

class SourcePropertiesArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]
    source_control_type: pulumi.Input[Union[_builtins.str, SourceControlType]]
    branch: NotRequired[pulumi.Input[_builtins.str]]
    source_control_auth_properties: NotRequired[pulumi.Input[AuthInfoArgsDict]]

@pulumi.input_type
class SourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        repository_url: pulumi.Input[_builtins.str],
        source_control_type: pulumi.Input[Union[_builtins.str, SourceControlType]],
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        source_control_auth_properties: Optional[pulumi.Input[AuthInfoArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]: ...
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceControlType")
    def source_control_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SourceControlType]]: ...
    @source_control_type.setter
    def source_control_type(
        self, value: pulumi.Input[Union[_builtins.str, SourceControlType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceControlAuthProperties")
    def source_control_auth_properties(
        self,
    ) -> Optional[pulumi.Input[AuthInfoArgs]]: ...
    @source_control_auth_properties.setter
    def source_control_auth_properties(
        self, value: Optional[pulumi.Input[AuthInfoArgs]]
    ): ...

class SourceRegistryCredentialsArgsDict(TypedDict):
    login_mode: NotRequired[pulumi.Input[Union[_builtins.str, SourceRegistryLoginMode]]]

@pulumi.input_type
class SourceRegistryCredentialsArgs:
    def __init__(
        __self__,
        *,
        login_mode: Optional[
            pulumi.Input[Union[_builtins.str, SourceRegistryLoginMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginMode")
    def login_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SourceRegistryLoginMode]]]: ...
    @login_mode.setter
    def login_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, SourceRegistryLoginMode]]],
    ): ...

class SourceTriggerArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    source_repository: pulumi.Input[SourcePropertiesArgsDict]
    source_trigger_events: pulumi.Input[
        Sequence[pulumi.Input[Union[_builtins.str, SourceTriggerEvent]]]
    ]
    status: NotRequired[pulumi.Input[Union[_builtins.str, TriggerStatus]]]

@pulumi.input_type
class SourceTriggerArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        source_repository: pulumi.Input[SourcePropertiesArgs],
        source_trigger_events: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, SourceTriggerEvent]]]
        ],
        status: Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> pulumi.Input[SourcePropertiesArgs]: ...
    @source_repository.setter
    def source_repository(self, value: pulumi.Input[SourcePropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="sourceTriggerEvents")
    def source_trigger_events(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[Union[_builtins.str, SourceTriggerEvent]]]
    ]: ...
    @source_trigger_events.setter
    def source_trigger_events(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, SourceTriggerEvent]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]]
    ): ...

class SyncPropertiesArgsDict(TypedDict):
    message_ttl: pulumi.Input[_builtins.str]
    token_id: pulumi.Input[_builtins.str]
    schedule: NotRequired[pulumi.Input[_builtins.str]]
    sync_window: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SyncPropertiesArgs:
    def __init__(
        __self__,
        *,
        message_ttl: pulumi.Input[_builtins.str],
        token_id: pulumi.Input[_builtins.str],
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_window: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageTtl")
    def message_ttl(self) -> pulumi.Input[_builtins.str]: ...
    @message_ttl.setter
    def message_ttl(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tokenId")
    def token_id(self) -> pulumi.Input[_builtins.str]: ...
    @token_id.setter
    def token_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="syncWindow")
    def sync_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sync_window.setter
    def sync_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskRunRequestArgsDict(TypedDict):
    task_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    agent_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_template: NotRequired[pulumi.Input[_builtins.str]]
    override_task_step_properties: NotRequired[
        pulumi.Input[OverrideTaskStepPropertiesArgsDict]
    ]

@pulumi.input_type
class TaskRunRequestArgs:
    def __init__(
        __self__,
        *,
        task_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_template: Optional[pulumi.Input[_builtins.str]] = ...,
        override_task_step_properties: Optional[
            pulumi.Input[OverrideTaskStepPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> pulumi.Input[_builtins.str]: ...
    @task_id.setter
    def task_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_pool_name.setter
    def agent_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_template.setter
    def log_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overrideTaskStepProperties")
    def override_task_step_properties(
        self,
    ) -> Optional[pulumi.Input[OverrideTaskStepPropertiesArgs]]: ...
    @override_task_step_properties.setter
    def override_task_step_properties(
        self, value: Optional[pulumi.Input[OverrideTaskStepPropertiesArgs]]
    ): ...

class TimerTriggerArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    schedule: pulumi.Input[_builtins.str]
    status: NotRequired[pulumi.Input[Union[_builtins.str, TriggerStatus]]]

@pulumi.input_type
class TimerTriggerArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        schedule: pulumi.Input[_builtins.str],
        status: Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[_builtins.str]: ...
    @schedule.setter
    def schedule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TriggerStatus]]]
    ): ...

class TokenCertificateArgsDict(TypedDict):
    encoded_pem_certificate: NotRequired[pulumi.Input[_builtins.str]]
    expiry: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[Union[_builtins.str, TokenCertificateName]]]
    thumbprint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TokenCertificateArgs:
    def __init__(
        __self__,
        *,
        encoded_pem_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[Union[_builtins.str, TokenCertificateName]]] = ...,
        thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encodedPemCertificate")
    def encoded_pem_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoded_pem_certificate.setter
    def encoded_pem_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expiry(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry.setter
    def expiry(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TokenCertificateName]]]: ...
    @name.setter
    def name(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TokenCertificateName]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TokenCredentialsPropertiesArgsDict(TypedDict):
    certificates: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TokenCertificateArgsDict]]]
    ]
    passwords: NotRequired[pulumi.Input[Sequence[pulumi.Input[TokenPasswordArgsDict]]]]

@pulumi.input_type
class TokenCredentialsPropertiesArgs:
    def __init__(
        __self__,
        *,
        certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[TokenCertificateArgs]]]
        ] = ...,
        passwords: Optional[
            pulumi.Input[Sequence[pulumi.Input[TokenPasswordArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TokenCertificateArgs]]]]: ...
    @certificates.setter
    def certificates(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TokenCertificateArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def passwords(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TokenPasswordArgs]]]]: ...
    @passwords.setter
    def passwords(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TokenPasswordArgs]]]]
    ): ...

class TokenPasswordArgsDict(TypedDict):
    creation_time: NotRequired[pulumi.Input[_builtins.str]]
    expiry: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[Union[_builtins.str, TokenPasswordName]]]

@pulumi.input_type
class TokenPasswordArgs:
    def __init__(
        __self__,
        *,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[Union[_builtins.str, TokenPasswordName]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expiry(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry.setter
    def expiry(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TokenPasswordName]]]: ...
    @name.setter
    def name(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TokenPasswordName]]]
    ): ...

class TriggerPropertiesArgsDict(TypedDict):
    base_image_trigger: NotRequired[pulumi.Input[BaseImageTriggerArgsDict]]
    source_triggers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SourceTriggerArgsDict]]]
    ]
    timer_triggers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TimerTriggerArgsDict]]]
    ]

@pulumi.input_type
class TriggerPropertiesArgs:
    def __init__(
        __self__,
        *,
        base_image_trigger: Optional[pulumi.Input[BaseImageTriggerArgs]] = ...,
        source_triggers: Optional[
            pulumi.Input[Sequence[pulumi.Input[SourceTriggerArgs]]]
        ] = ...,
        timer_triggers: Optional[
            pulumi.Input[Sequence[pulumi.Input[TimerTriggerArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseImageTrigger")
    def base_image_trigger(self) -> Optional[pulumi.Input[BaseImageTriggerArgs]]: ...
    @base_image_trigger.setter
    def base_image_trigger(
        self, value: Optional[pulumi.Input[BaseImageTriggerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceTriggers")
    def source_triggers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SourceTriggerArgs]]]]: ...
    @source_triggers.setter
    def source_triggers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SourceTriggerArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timerTriggers")
    def timer_triggers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TimerTriggerArgs]]]]: ...
    @timer_triggers.setter
    def timer_triggers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TimerTriggerArgs]]]]
    ): ...

class TrustPolicyArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[Union[_builtins.str, PolicyStatus]]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, TrustPolicyType]]]

@pulumi.input_type
class TrustPolicyArgs:
    def __init__(
        __self__,
        *,
        status: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, TrustPolicyType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, TrustPolicyType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TrustPolicyType]]]
    ): ...

class UserIdentityPropertiesArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserIdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
