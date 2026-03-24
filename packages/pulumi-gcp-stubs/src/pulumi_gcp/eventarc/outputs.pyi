

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GoogleApiSourceLoggingConfig', 'MessageBusLoggingConfig', 'PipelineDestination', 'PipelineDestinationAuthenticationConfig', 'PipelineDestinationAuthenticationConfigGoogleOidc', 'PipelineDestinationAuthenticationConfigOauthToken', 'PipelineDestinationHttpEndpoint', 'PipelineDestinationNetworkConfig', 'PipelineDestinationOutputPayloadFormat', 'PipelineDestinationOutputPayloadFormatAvro', 'PipelineDestinationOutputPayloadFormatJson', 'PipelineDestinationOutputPayloadFormatProtobuf', 'PipelineInputPayloadFormat', 'PipelineInputPayloadFormatAvro', 'PipelineInputPayloadFormatJson', 'PipelineInputPayloadFormatProtobuf', 'PipelineLoggingConfig', 'PipelineMediation', 'PipelineMediationTransformation', 'PipelineRetryPolicy', 'TriggerDestination', 'TriggerDestinationCloudRunService', 'TriggerDestinationGke', 'TriggerDestinationHttpEndpoint', 'TriggerDestinationNetworkConfig', 'TriggerMatchingCriteria', 'TriggerRetryPolicy', 'TriggerTransport', 'TriggerTransportPubsub']
@pulumi.output_type
class GoogleApiSourceLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_severity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logSeverity")
    def log_severity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MessageBusLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_severity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logSeverity")
    def log_severity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication_config: Optional[outputs.PipelineDestinationAuthenticationConfig] = ..., http_endpoint: Optional[outputs.PipelineDestinationHttpEndpoint] = ..., message_bus: Optional[_builtins.str] = ..., network_config: Optional[outputs.PipelineDestinationNetworkConfig] = ..., output_payload_format: Optional[outputs.PipelineDestinationOutputPayloadFormat] = ..., topic: Optional[_builtins.str] = ..., workflow: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationConfig")
    def authentication_config(self) -> Optional[outputs.PipelineDestinationAuthenticationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[outputs.PipelineDestinationHttpEndpoint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageBus")
    def message_bus(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[outputs.PipelineDestinationNetworkConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputPayloadFormat")
    def output_payload_format(self) -> Optional[outputs.PipelineDestinationOutputPayloadFormat]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workflow(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineDestinationAuthenticationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, google_oidc: Optional[outputs.PipelineDestinationAuthenticationConfigGoogleOidc] = ..., oauth_token: Optional[outputs.PipelineDestinationAuthenticationConfigOauthToken] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleOidc")
    def google_oidc(self) -> Optional[outputs.PipelineDestinationAuthenticationConfigGoogleOidc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> Optional[outputs.PipelineDestinationAuthenticationConfigOauthToken]:
        
        ...
    


@pulumi.output_type
class PipelineDestinationAuthenticationConfigGoogleOidc(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account: _builtins.str, audience: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineDestinationAuthenticationConfigOauthToken(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account: _builtins.str, scope: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineDestinationHttpEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, uri: _builtins.str, message_binding_template: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageBindingTemplate")
    def message_binding_template(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineDestinationNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_attachment: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineDestinationOutputPayloadFormat(dict):
    def __init__(__self__, *, avro: Optional[outputs.PipelineDestinationOutputPayloadFormatAvro] = ..., json: Optional[outputs.PipelineDestinationOutputPayloadFormatJson] = ..., protobuf: Optional[outputs.PipelineDestinationOutputPayloadFormatProtobuf] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def avro(self) -> Optional[outputs.PipelineDestinationOutputPayloadFormatAvro]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[outputs.PipelineDestinationOutputPayloadFormatJson]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protobuf(self) -> Optional[outputs.PipelineDestinationOutputPayloadFormatProtobuf]:
        
        ...
    


@pulumi.output_type
class PipelineDestinationOutputPayloadFormatAvro(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schema_definition: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineDestinationOutputPayloadFormatJson(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PipelineDestinationOutputPayloadFormatProtobuf(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schema_definition: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineInputPayloadFormat(dict):
    def __init__(__self__, *, avro: Optional[outputs.PipelineInputPayloadFormatAvro] = ..., json: Optional[outputs.PipelineInputPayloadFormatJson] = ..., protobuf: Optional[outputs.PipelineInputPayloadFormatProtobuf] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def avro(self) -> Optional[outputs.PipelineInputPayloadFormatAvro]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[outputs.PipelineInputPayloadFormatJson]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protobuf(self) -> Optional[outputs.PipelineInputPayloadFormatProtobuf]:
        
        ...
    


@pulumi.output_type
class PipelineInputPayloadFormatAvro(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schema_definition: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineInputPayloadFormatJson(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PipelineInputPayloadFormatProtobuf(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schema_definition: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_severity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logSeverity")
    def log_severity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineMediation(dict):
    def __init__(__self__, *, transformation: Optional[outputs.PipelineMediationTransformation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transformation(self) -> Optional[outputs.PipelineMediationTransformation]:
        
        ...
    


@pulumi.output_type
class PipelineMediationTransformation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, transformation_template: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transformationTemplate")
    def transformation_template(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_attempts: Optional[_builtins.int] = ..., max_retry_delay: Optional[_builtins.str] = ..., min_retry_delay: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetryDelay")
    def max_retry_delay(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minRetryDelay")
    def min_retry_delay(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_function: Optional[_builtins.str] = ..., cloud_run_service: Optional[outputs.TriggerDestinationCloudRunService] = ..., gke: Optional[outputs.TriggerDestinationGke] = ..., http_endpoint: Optional[outputs.TriggerDestinationHttpEndpoint] = ..., network_config: Optional[outputs.TriggerDestinationNetworkConfig] = ..., workflow: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRunService")
    def cloud_run_service(self) -> Optional[outputs.TriggerDestinationCloudRunService]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gke(self) -> Optional[outputs.TriggerDestinationGke]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[outputs.TriggerDestinationHttpEndpoint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[outputs.TriggerDestinationNetworkConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workflow(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerDestinationCloudRunService(dict):
    def __init__(__self__, *, service: _builtins.str, path: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerDestinationGke(dict):
    def __init__(__self__, *, cluster: _builtins.str, location: _builtins.str, namespace: _builtins.str, service: _builtins.str, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerDestinationHttpEndpoint(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TriggerDestinationNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_attachment: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TriggerMatchingCriteria(dict):
    def __init__(__self__, *, attribute: _builtins.str, value: _builtins.str, operator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_attempts: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TriggerTransport(dict):
    def __init__(__self__, *, pubsub: Optional[outputs.TriggerTransportPubsub] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pubsub(self) -> Optional[outputs.TriggerTransportPubsub]:
        
        ...
    


@pulumi.output_type
class TriggerTransportPubsub(dict):
    def __init__(__self__, *, subscription: Optional[_builtins.str] = ..., topic: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscription(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]:
        
        ...
    


