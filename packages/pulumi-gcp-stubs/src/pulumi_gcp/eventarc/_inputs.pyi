import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GoogleApiSourceLoggingConfigArgs",
    "GoogleApiSourceLoggingConfigArgsDict",
    "MessageBusLoggingConfigArgs",
    "MessageBusLoggingConfigArgsDict",
    "PipelineDestinationArgs",
    "PipelineDestinationArgsDict",
    "PipelineDestinationAuthenticationConfigArgs",
    "PipelineDestinationAuthenticationConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "PipelineDestinationHttpEndpointArgs",
    "PipelineDestinationHttpEndpointArgsDict",
    "PipelineDestinationNetworkConfigArgs",
    "PipelineDestinationNetworkConfigArgsDict",
    "PipelineDestinationOutputPayloadFormatArgs",
    "PipelineDestinationOutputPayloadFormatArgsDict",
    "PipelineDestinationOutputPayloadFormatAvroArgs",
    "PipelineDestinationOutputPayloadFormatAvroArgsDict",
    "PipelineDestinationOutputPayloadFormatJsonArgs",
    "PipelineDestinationOutputPayloadFormatJsonArgsDict",
    "PipelineDestinationOutputPayloadFormatProtobufArgs",
    ...,
    "PipelineInputPayloadFormatArgs",
    "PipelineInputPayloadFormatArgsDict",
    "PipelineInputPayloadFormatAvroArgs",
    "PipelineInputPayloadFormatAvroArgsDict",
    "PipelineInputPayloadFormatJsonArgs",
    "PipelineInputPayloadFormatJsonArgsDict",
    "PipelineInputPayloadFormatProtobufArgs",
    "PipelineInputPayloadFormatProtobufArgsDict",
    "PipelineLoggingConfigArgs",
    "PipelineLoggingConfigArgsDict",
    "PipelineMediationArgs",
    "PipelineMediationArgsDict",
    "PipelineMediationTransformationArgs",
    "PipelineMediationTransformationArgsDict",
    "PipelineRetryPolicyArgs",
    "PipelineRetryPolicyArgsDict",
    "TriggerDestinationArgs",
    "TriggerDestinationArgsDict",
    "TriggerDestinationCloudRunServiceArgs",
    "TriggerDestinationCloudRunServiceArgsDict",
    "TriggerDestinationGkeArgs",
    "TriggerDestinationGkeArgsDict",
    "TriggerDestinationHttpEndpointArgs",
    "TriggerDestinationHttpEndpointArgsDict",
    "TriggerDestinationNetworkConfigArgs",
    "TriggerDestinationNetworkConfigArgsDict",
    "TriggerMatchingCriteriaArgs",
    "TriggerMatchingCriteriaArgsDict",
    "TriggerRetryPolicyArgs",
    "TriggerRetryPolicyArgsDict",
    "TriggerTransportArgs",
    "TriggerTransportArgsDict",
    "TriggerTransportPubsubArgs",
    "TriggerTransportPubsubArgsDict",
]

class GoogleApiSourceLoggingConfigArgsDict(TypedDict):
    log_severity: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GoogleApiSourceLoggingConfigArgs:
    def __init__(
        __self__, *, log_severity: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logSeverity")
    def log_severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_severity.setter
    def log_severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MessageBusLoggingConfigArgsDict(TypedDict):
    log_severity: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MessageBusLoggingConfigArgs:
    def __init__(
        __self__, *, log_severity: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logSeverity")
    def log_severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_severity.setter
    def log_severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineDestinationArgsDict(TypedDict):
    authentication_config: NotRequired[
        pulumi.Input[PipelineDestinationAuthenticationConfigArgsDict]
    ]
    http_endpoint: NotRequired[pulumi.Input[PipelineDestinationHttpEndpointArgsDict]]
    message_bus: NotRequired[pulumi.Input[_builtins.str]]
    network_config: NotRequired[pulumi.Input[PipelineDestinationNetworkConfigArgsDict]]
    output_payload_format: NotRequired[
        pulumi.Input[PipelineDestinationOutputPayloadFormatArgsDict]
    ]
    topic: NotRequired[pulumi.Input[_builtins.str]]
    workflow: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineDestinationArgs:
    def __init__(
        __self__,
        *,
        authentication_config: Optional[
            pulumi.Input[PipelineDestinationAuthenticationConfigArgs]
        ] = ...,
        http_endpoint: Optional[
            pulumi.Input[PipelineDestinationHttpEndpointArgs]
        ] = ...,
        message_bus: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[PipelineDestinationNetworkConfigArgs]
        ] = ...,
        output_payload_format: Optional[
            pulumi.Input[PipelineDestinationOutputPayloadFormatArgs]
        ] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfig")
    def authentication_config(
        self,
    ) -> Optional[pulumi.Input[PipelineDestinationAuthenticationConfigArgs]]: ...
    @authentication_config.setter
    def authentication_config(
        self, value: Optional[pulumi.Input[PipelineDestinationAuthenticationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(
        self,
    ) -> Optional[pulumi.Input[PipelineDestinationHttpEndpointArgs]]: ...
    @http_endpoint.setter
    def http_endpoint(
        self, value: Optional[pulumi.Input[PipelineDestinationHttpEndpointArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageBus")
    def message_bus(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_bus.setter
    def message_bus(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[PipelineDestinationNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[PipelineDestinationNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputPayloadFormat")
    def output_payload_format(
        self,
    ) -> Optional[pulumi.Input[PipelineDestinationOutputPayloadFormatArgs]]: ...
    @output_payload_format.setter
    def output_payload_format(
        self, value: Optional[pulumi.Input[PipelineDestinationOutputPayloadFormatArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workflow(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workflow.setter
    def workflow(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineDestinationAuthenticationConfigArgsDict(TypedDict):
    google_oidc: NotRequired[
        pulumi.Input[PipelineDestinationAuthenticationConfigGoogleOidcArgsDict]
    ]
    oauth_token: NotRequired[
        pulumi.Input[PipelineDestinationAuthenticationConfigOauthTokenArgsDict]
    ]
    ...

@pulumi.input_type
class PipelineDestinationAuthenticationConfigArgs:
    def __init__(
        __self__,
        *,
        google_oidc: Optional[
            pulumi.Input[PipelineDestinationAuthenticationConfigGoogleOidcArgs]
        ] = ...,
        oauth_token: Optional[
            pulumi.Input[PipelineDestinationAuthenticationConfigOauthTokenArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="googleOidc")
    def google_oidc(
        self,
    ) -> Optional[
        pulumi.Input[PipelineDestinationAuthenticationConfigGoogleOidcArgs]
    ]: ...
    @google_oidc.setter
    def google_oidc(
        self,
        value: Optional[
            pulumi.Input[PipelineDestinationAuthenticationConfigGoogleOidcArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(
        self,
    ) -> Optional[
        pulumi.Input[PipelineDestinationAuthenticationConfigOauthTokenArgs]
    ]: ...
    @oauth_token.setter
    def oauth_token(
        self,
        value: Optional[
            pulumi.Input[PipelineDestinationAuthenticationConfigOauthTokenArgs]
        ],
    ): ...

class PipelineDestinationAuthenticationConfigGoogleOidcArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineDestinationAuthenticationConfigGoogleOidcArgs:
    def __init__(
        __self__,
        *,
        service_account: pulumi.Input[_builtins.str],
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]: ...
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineDestinationAuthenticationConfigOauthTokenArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineDestinationAuthenticationConfigOauthTokenArgs:
    def __init__(
        __self__,
        *,
        service_account: pulumi.Input[_builtins.str],
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]: ...
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineDestinationHttpEndpointArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    message_binding_template: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineDestinationHttpEndpointArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        message_binding_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="messageBindingTemplate")
    def message_binding_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_binding_template.setter
    def message_binding_template(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PipelineDestinationNetworkConfigArgsDict(TypedDict):
    network_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineDestinationNetworkConfigArgs:
    def __init__(
        __self__, *, network_attachment: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_attachment.setter
    def network_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineDestinationOutputPayloadFormatArgsDict(TypedDict):
    avro: NotRequired[pulumi.Input[PipelineDestinationOutputPayloadFormatAvroArgsDict]]
    json: NotRequired[pulumi.Input[PipelineDestinationOutputPayloadFormatJsonArgsDict]]
    protobuf: NotRequired[
        pulumi.Input[PipelineDestinationOutputPayloadFormatProtobufArgsDict]
    ]
    ...

@pulumi.input_type
class PipelineDestinationOutputPayloadFormatArgs:
    def __init__(
        __self__,
        *,
        avro: Optional[
            pulumi.Input[PipelineDestinationOutputPayloadFormatAvroArgs]
        ] = ...,
        json: Optional[
            pulumi.Input[PipelineDestinationOutputPayloadFormatJsonArgs]
        ] = ...,
        protobuf: Optional[
            pulumi.Input[PipelineDestinationOutputPayloadFormatProtobufArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def avro(
        self,
    ) -> Optional[pulumi.Input[PipelineDestinationOutputPayloadFormatAvroArgs]]: ...
    @avro.setter
    def avro(
        self,
        value: Optional[pulumi.Input[PipelineDestinationOutputPayloadFormatAvroArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def json(
        self,
    ) -> Optional[pulumi.Input[PipelineDestinationOutputPayloadFormatJsonArgs]]: ...
    @json.setter
    def json(
        self,
        value: Optional[pulumi.Input[PipelineDestinationOutputPayloadFormatJsonArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def protobuf(
        self,
    ) -> Optional[pulumi.Input[PipelineDestinationOutputPayloadFormatProtobufArgs]]: ...
    @protobuf.setter
    def protobuf(
        self,
        value: Optional[
            pulumi.Input[PipelineDestinationOutputPayloadFormatProtobufArgs]
        ],
    ): ...

class PipelineDestinationOutputPayloadFormatAvroArgsDict(TypedDict):
    schema_definition: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineDestinationOutputPayloadFormatAvroArgs:
    def __init__(
        __self__, *, schema_definition: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_definition.setter
    def schema_definition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineDestinationOutputPayloadFormatJsonArgsDict(TypedDict): ...

@pulumi.input_type
class PipelineDestinationOutputPayloadFormatJsonArgs:
    def __init__(__self__) -> None: ...

class PipelineDestinationOutputPayloadFormatProtobufArgsDict(TypedDict):
    schema_definition: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineDestinationOutputPayloadFormatProtobufArgs:
    def __init__(
        __self__, *, schema_definition: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_definition.setter
    def schema_definition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineInputPayloadFormatArgsDict(TypedDict):
    avro: NotRequired[pulumi.Input[PipelineInputPayloadFormatAvroArgsDict]]
    json: NotRequired[pulumi.Input[PipelineInputPayloadFormatJsonArgsDict]]
    protobuf: NotRequired[pulumi.Input[PipelineInputPayloadFormatProtobufArgsDict]]
    ...

@pulumi.input_type
class PipelineInputPayloadFormatArgs:
    def __init__(
        __self__,
        *,
        avro: Optional[pulumi.Input[PipelineInputPayloadFormatAvroArgs]] = ...,
        json: Optional[pulumi.Input[PipelineInputPayloadFormatJsonArgs]] = ...,
        protobuf: Optional[pulumi.Input[PipelineInputPayloadFormatProtobufArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def avro(self) -> Optional[pulumi.Input[PipelineInputPayloadFormatAvroArgs]]: ...
    @avro.setter
    def avro(
        self, value: Optional[pulumi.Input[PipelineInputPayloadFormatAvroArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[pulumi.Input[PipelineInputPayloadFormatJsonArgs]]: ...
    @json.setter
    def json(
        self, value: Optional[pulumi.Input[PipelineInputPayloadFormatJsonArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protobuf(
        self,
    ) -> Optional[pulumi.Input[PipelineInputPayloadFormatProtobufArgs]]: ...
    @protobuf.setter
    def protobuf(
        self, value: Optional[pulumi.Input[PipelineInputPayloadFormatProtobufArgs]]
    ): ...

class PipelineInputPayloadFormatAvroArgsDict(TypedDict):
    schema_definition: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineInputPayloadFormatAvroArgs:
    def __init__(
        __self__, *, schema_definition: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_definition.setter
    def schema_definition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineInputPayloadFormatJsonArgsDict(TypedDict): ...

@pulumi.input_type
class PipelineInputPayloadFormatJsonArgs:
    def __init__(__self__) -> None: ...

class PipelineInputPayloadFormatProtobufArgsDict(TypedDict):
    schema_definition: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineInputPayloadFormatProtobufArgs:
    def __init__(
        __self__, *, schema_definition: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_definition.setter
    def schema_definition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineLoggingConfigArgsDict(TypedDict):
    log_severity: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineLoggingConfigArgs:
    def __init__(
        __self__, *, log_severity: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logSeverity")
    def log_severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_severity.setter
    def log_severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineMediationArgsDict(TypedDict):
    transformation: NotRequired[pulumi.Input[PipelineMediationTransformationArgsDict]]
    ...

@pulumi.input_type
class PipelineMediationArgs:
    def __init__(
        __self__,
        *,
        transformation: Optional[
            pulumi.Input[PipelineMediationTransformationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def transformation(
        self,
    ) -> Optional[pulumi.Input[PipelineMediationTransformationArgs]]: ...
    @transformation.setter
    def transformation(
        self, value: Optional[pulumi.Input[PipelineMediationTransformationArgs]]
    ): ...

class PipelineMediationTransformationArgsDict(TypedDict):
    transformation_template: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineMediationTransformationArgs:
    def __init__(
        __self__,
        *,
        transformation_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transformationTemplate")
    def transformation_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transformation_template.setter
    def transformation_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineRetryPolicyArgsDict(TypedDict):
    max_attempts: NotRequired[pulumi.Input[_builtins.int]]
    max_retry_delay: NotRequired[pulumi.Input[_builtins.str]]
    min_retry_delay: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineRetryPolicyArgs:
    def __init__(
        __self__,
        *,
        max_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        max_retry_delay: Optional[pulumi.Input[_builtins.str]] = ...,
        min_retry_delay: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_attempts.setter
    def max_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetryDelay")
    def max_retry_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_retry_delay.setter
    def max_retry_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minRetryDelay")
    def min_retry_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_retry_delay.setter
    def min_retry_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerDestinationArgsDict(TypedDict):
    cloud_function: NotRequired[pulumi.Input[_builtins.str]]
    cloud_run_service: NotRequired[
        pulumi.Input[TriggerDestinationCloudRunServiceArgsDict]
    ]
    gke: NotRequired[pulumi.Input[TriggerDestinationGkeArgsDict]]
    http_endpoint: NotRequired[pulumi.Input[TriggerDestinationHttpEndpointArgsDict]]
    network_config: NotRequired[pulumi.Input[TriggerDestinationNetworkConfigArgsDict]]
    workflow: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerDestinationArgs:
    def __init__(
        __self__,
        *,
        cloud_function: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_run_service: Optional[
            pulumi.Input[TriggerDestinationCloudRunServiceArgs]
        ] = ...,
        gke: Optional[pulumi.Input[TriggerDestinationGkeArgs]] = ...,
        http_endpoint: Optional[pulumi.Input[TriggerDestinationHttpEndpointArgs]] = ...,
        network_config: Optional[
            pulumi.Input[TriggerDestinationNetworkConfigArgs]
        ] = ...,
        workflow: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_function.setter
    def cloud_function(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudRunService")
    def cloud_run_service(
        self,
    ) -> Optional[pulumi.Input[TriggerDestinationCloudRunServiceArgs]]: ...
    @cloud_run_service.setter
    def cloud_run_service(
        self, value: Optional[pulumi.Input[TriggerDestinationCloudRunServiceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gke(self) -> Optional[pulumi.Input[TriggerDestinationGkeArgs]]: ...
    @gke.setter
    def gke(self, value: Optional[pulumi.Input[TriggerDestinationGkeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(
        self,
    ) -> Optional[pulumi.Input[TriggerDestinationHttpEndpointArgs]]: ...
    @http_endpoint.setter
    def http_endpoint(
        self, value: Optional[pulumi.Input[TriggerDestinationHttpEndpointArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[TriggerDestinationNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[TriggerDestinationNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def workflow(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workflow.setter
    def workflow(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerDestinationCloudRunServiceArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerDestinationCloudRunServiceArgs:
    def __init__(
        __self__,
        *,
        service: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerDestinationGkeArgsDict(TypedDict):
    cluster: pulumi.Input[_builtins.str]
    location: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerDestinationGkeArgs:
    def __init__(
        __self__,
        *,
        cluster: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]: ...
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerDestinationHttpEndpointArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TriggerDestinationHttpEndpointArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class TriggerDestinationNetworkConfigArgsDict(TypedDict):
    network_attachment: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TriggerDestinationNetworkConfigArgs:
    def __init__(
        __self__, *, network_attachment: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> pulumi.Input[_builtins.str]: ...
    @network_attachment.setter
    def network_attachment(self, value: pulumi.Input[_builtins.str]): ...

class TriggerMatchingCriteriaArgsDict(TypedDict):
    attribute: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    operator: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerMatchingCriteriaArgs:
    def __init__(
        __self__,
        *,
        attribute: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        operator: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> pulumi.Input[_builtins.str]: ...
    @attribute.setter
    def attribute(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerRetryPolicyArgsDict(TypedDict):
    max_attempts: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class TriggerRetryPolicyArgs:
    def __init__(
        __self__, *, max_attempts: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_attempts.setter
    def max_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TriggerTransportArgsDict(TypedDict):
    pubsub: NotRequired[pulumi.Input[TriggerTransportPubsubArgsDict]]
    ...

@pulumi.input_type
class TriggerTransportArgs:
    def __init__(
        __self__, *, pubsub: Optional[pulumi.Input[TriggerTransportPubsubArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pubsub(self) -> Optional[pulumi.Input[TriggerTransportPubsubArgs]]: ...
    @pubsub.setter
    def pubsub(self, value: Optional[pulumi.Input[TriggerTransportPubsubArgs]]): ...

class TriggerTransportPubsubArgsDict(TypedDict):
    subscription: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerTransportPubsubArgs:
    def __init__(
        __self__,
        *,
        subscription: Optional[pulumi.Input[_builtins.str]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subscription(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription.setter
    def subscription(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
