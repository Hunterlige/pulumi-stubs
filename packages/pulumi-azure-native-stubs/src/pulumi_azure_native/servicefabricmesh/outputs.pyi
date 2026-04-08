import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AddRemoveReplicaScalingMechanismResponse",
    ...,
    "ApplicationScopedVolumeResponse",
    "AutoScalingPolicyResponse",
    "AutoScalingResourceMetricResponse",
    "AverageLoadScalingTriggerResponse",
    ...,
    "ContainerCodePackagePropertiesResponse",
    "ContainerEventResponse",
    "ContainerInstanceViewResponse",
    "ContainerLabelResponse",
    "ContainerStateResponse",
    "DiagnosticsDescriptionResponse",
    "DiagnosticsRefResponse",
    "EndpointPropertiesResponse",
    "EndpointRefResponse",
    "EnvironmentVariableResponse",
    "GatewayDestinationResponse",
    "HttpConfigResponse",
    "HttpHostConfigResponse",
    "HttpRouteConfigResponse",
    "HttpRouteMatchHeaderResponse",
    "HttpRouteMatchPathResponse",
    "HttpRouteMatchRuleResponse",
    "ImageRegistryCredentialResponse",
    "NetworkRefResponse",
    "NetworkResourcePropertiesResponse",
    "ReliableCollectionsRefResponse",
    "ResourceLimitsResponse",
    "ResourceRequestsResponse",
    "ResourceRequirementsResponse",
    "SecretResourcePropertiesResponse",
    "ServiceResourceDescriptionResponse",
    "SettingResponse",
    "TcpConfigResponse",
    "VolumeProviderParametersAzureFileResponse",
    "VolumeReferenceResponse",
]

@pulumi.output_type
class AddRemoveReplicaScalingMechanismResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        max_count: _builtins.int,
        min_count: _builtins.int,
        scale_increment: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scaleIncrement")
    def scale_increment(self) -> _builtins.int: ...

@pulumi.output_type
class ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        size_disk: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sizeDisk")
    def size_disk(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationScopedVolumeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        creation_parameters: outputs.ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskResponse,
        destination_path: _builtins.str,
        name: _builtins.str,
        read_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationParameters")
    def creation_parameters(
        self,
    ) -> (
        outputs.ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskResponse
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPath")
    def destination_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AutoScalingPolicyResponse(dict):
    def __init__(
        __self__,
        *,
        mechanism: outputs.AddRemoveReplicaScalingMechanismResponse,
        name: _builtins.str,
        trigger: outputs.AverageLoadScalingTriggerResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mechanism(self) -> outputs.AddRemoveReplicaScalingMechanismResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> outputs.AverageLoadScalingTriggerResponse: ...

@pulumi.output_type
class AutoScalingResourceMetricResponse(dict):
    def __init__(__self__, *, kind: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AverageLoadScalingTriggerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        lower_load_threshold: _builtins.float,
        metric: outputs.AutoScalingResourceMetricResponse,
        scale_interval_in_seconds: _builtins.int,
        upper_load_threshold: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lowerLoadThreshold")
    def lower_load_threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def metric(self) -> outputs.AutoScalingResourceMetricResponse: ...
    @_builtins.property
    @pulumi.getter(name="scaleIntervalInSeconds")
    def scale_interval_in_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="upperLoadThreshold")
    def upper_load_threshold(self) -> _builtins.float: ...

@pulumi.output_type
class AzureInternalMonitoringPipelineSinkDescriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        account_name: Optional[_builtins.str] = ...,
        auto_key_config_url: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        fluentd_config_url: Optional[Any] = ...,
        ma_config_url: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        namespace: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoKeyConfigUrl")
    def auto_key_config_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fluentdConfigUrl")
    def fluentd_config_url(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="maConfigUrl")
    def ma_config_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContainerCodePackagePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image: _builtins.str,
        instance_view: outputs.ContainerInstanceViewResponse,
        name: _builtins.str,
        resources: outputs.ResourceRequirementsResponse,
        commands: Optional[Sequence[_builtins.str]] = ...,
        diagnostics: Optional[outputs.DiagnosticsRefResponse] = ...,
        endpoints: Optional[Sequence[outputs.EndpointPropertiesResponse]] = ...,
        entrypoint: Optional[_builtins.str] = ...,
        environment_variables: Optional[
            Sequence[outputs.EnvironmentVariableResponse]
        ] = ...,
        image_registry_credential: Optional[
            outputs.ImageRegistryCredentialResponse
        ] = ...,
        labels: Optional[Sequence[outputs.ContainerLabelResponse]] = ...,
        reliable_collections_refs: Optional[
            Sequence[outputs.ReliableCollectionsRefResponse]
        ] = ...,
        settings: Optional[Sequence[outputs.SettingResponse]] = ...,
        volume_refs: Optional[Sequence[outputs.VolumeReferenceResponse]] = ...,
        volumes: Optional[Sequence[outputs.ApplicationScopedVolumeResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.ContainerInstanceViewResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> outputs.ResourceRequirementsResponse: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[outputs.DiagnosticsRefResponse]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[outputs.EndpointPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[Sequence[outputs.EnvironmentVariableResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="imageRegistryCredential")
    def image_registry_credential(
        self,
    ) -> Optional[outputs.ImageRegistryCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[outputs.ContainerLabelResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="reliableCollectionsRefs")
    def reliable_collections_refs(
        self,
    ) -> Optional[Sequence[outputs.ReliableCollectionsRefResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Sequence[outputs.SettingResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="volumeRefs")
    def volume_refs(self) -> Optional[Sequence[outputs.VolumeReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[Sequence[outputs.ApplicationScopedVolumeResponse]]: ...

@pulumi.output_type
class ContainerEventResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: Optional[_builtins.int] = ...,
        first_timestamp: Optional[_builtins.str] = ...,
        last_timestamp: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="firstTimestamp")
    def first_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastTimestamp")
    def last_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContainerInstanceViewResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_state: Optional[outputs.ContainerStateResponse] = ...,
        events: Optional[Sequence[outputs.ContainerEventResponse]] = ...,
        previous_state: Optional[outputs.ContainerStateResponse] = ...,
        restart_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentState")
    def current_state(self) -> Optional[outputs.ContainerStateResponse]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.ContainerEventResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="previousState")
    def previous_state(self) -> Optional[outputs.ContainerStateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="restartCount")
    def restart_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ContainerLabelResponse(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ContainerStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        detail_status: Optional[_builtins.str] = ...,
        exit_code: Optional[_builtins.str] = ...,
        finish_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detailStatus")
    def detail_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exitCode")
    def exit_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DiagnosticsDescriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_sink_refs: Optional[Sequence[_builtins.str]] = ...,
        enabled: Optional[_builtins.bool] = ...,
        sinks: Optional[
            Sequence[outputs.AzureInternalMonitoringPipelineSinkDescriptionResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultSinkRefs")
    def default_sink_refs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def sinks(
        self,
    ) -> Optional[
        Sequence[outputs.AzureInternalMonitoringPipelineSinkDescriptionResponse]
    ]: ...

@pulumi.output_type
class DiagnosticsRefResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        sink_refs: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sinkRefs")
    def sink_refs(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EndpointPropertiesResponse(dict):
    def __init__(
        __self__, *, name: _builtins.str, port: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointRefResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentVariableResponse(dict):
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
class GatewayDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_name: _builtins.str,
        endpoint_name: _builtins.str,
        service_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...

@pulumi.output_type
class HttpConfigResponse(dict):
    def __init__(
        __self__,
        *,
        hosts: Sequence[outputs.HttpHostConfigResponse],
        name: _builtins.str,
        port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Sequence[outputs.HttpHostConfigResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class HttpHostConfigResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        routes: Sequence[outputs.HttpRouteConfigResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Sequence[outputs.HttpRouteConfigResponse]: ...

@pulumi.output_type
class HttpRouteConfigResponse(dict):
    def __init__(
        __self__,
        *,
        destination: outputs.GatewayDestinationResponse,
        match: outputs.HttpRouteMatchRuleResponse,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> outputs.GatewayDestinationResponse: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> outputs.HttpRouteMatchRuleResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class HttpRouteMatchHeaderResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpRouteMatchPathResponse(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        value: _builtins.str,
        rewrite: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rewrite(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpRouteMatchRuleResponse(dict):
    def __init__(
        __self__,
        *,
        path: outputs.HttpRouteMatchPathResponse,
        headers: Optional[Sequence[outputs.HttpRouteMatchHeaderResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> outputs.HttpRouteMatchPathResponse: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.HttpRouteMatchHeaderResponse]]: ...

@pulumi.output_type
class ImageRegistryCredentialResponse(dict):
    def __init__(
        __self__,
        *,
        server: _builtins.str,
        username: _builtins.str,
        password: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkRefResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_refs: Optional[Sequence[outputs.EndpointRefResponse]] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointRefs")
    def endpoint_refs(self) -> Optional[Sequence[outputs.EndpointRefResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        provisioning_state: _builtins.str,
        status: _builtins.str,
        status_details: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReliableCollectionsRefResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        do_not_persist_state: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="doNotPersistState")
    def do_not_persist_state(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ResourceLimitsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.float] = ...,
        memory_in_gb: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="memoryInGB")
    def memory_in_gb(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ResourceRequestsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cpu: _builtins.float, memory_in_gb: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="memoryInGB")
    def memory_in_gb(self) -> _builtins.float: ...

@pulumi.output_type
class ResourceRequirementsResponse(dict):
    def __init__(
        __self__,
        *,
        requests: outputs.ResourceRequestsResponse,
        limits: Optional[outputs.ResourceLimitsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> outputs.ResourceRequestsResponse: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[outputs.ResourceLimitsResponse]: ...

@pulumi.output_type
class SecretResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        provisioning_state: _builtins.str,
        status: _builtins.str,
        status_details: _builtins.str,
        content_type: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceResourceDescriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code_packages: Sequence[outputs.ContainerCodePackagePropertiesResponse],
        health_state: _builtins.str,
        id: _builtins.str,
        os_type: _builtins.str,
        provisioning_state: _builtins.str,
        status: _builtins.str,
        status_details: _builtins.str,
        type: _builtins.str,
        unhealthy_evaluation: _builtins.str,
        auto_scaling_policies: Optional[
            Sequence[outputs.AutoScalingPolicyResponse]
        ] = ...,
        description: Optional[_builtins.str] = ...,
        diagnostics: Optional[outputs.DiagnosticsRefResponse] = ...,
        name: Optional[_builtins.str] = ...,
        network_refs: Optional[Sequence[outputs.NetworkRefResponse]] = ...,
        replica_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codePackages")
    def code_packages(
        self,
    ) -> Sequence[outputs.ContainerCodePackagePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyEvaluation")
    def unhealthy_evaluation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingPolicies")
    def auto_scaling_policies(
        self,
    ) -> Optional[Sequence[outputs.AutoScalingPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[outputs.DiagnosticsRefResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkRefs")
    def network_refs(self) -> Optional[Sequence[outputs.NetworkRefResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SettingResponse(dict):
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
class TcpConfigResponse(dict):
    def __init__(
        __self__,
        *,
        destination: outputs.GatewayDestinationResponse,
        name: _builtins.str,
        port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> outputs.GatewayDestinationResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class VolumeProviderParametersAzureFileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_name: _builtins.str,
        share_name: _builtins.str,
        account_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VolumeReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_path: _builtins.str,
        name: _builtins.str,
        read_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationPath")
    def destination_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...
