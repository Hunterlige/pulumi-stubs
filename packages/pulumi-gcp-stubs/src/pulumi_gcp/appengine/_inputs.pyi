import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationFeatureSettingsArgs",
    "ApplicationFeatureSettingsArgsDict",
    "ApplicationIapArgs",
    "ApplicationIapArgsDict",
    "ApplicationUrlDispatchRuleArgs",
    "ApplicationUrlDispatchRuleArgsDict",
    "ApplicationUrlDispatchRulesDispatchRuleArgs",
    "ApplicationUrlDispatchRulesDispatchRuleArgsDict",
    "DomainMappingResourceRecordArgs",
    "DomainMappingResourceRecordArgsDict",
    "DomainMappingSslSettingsArgs",
    "DomainMappingSslSettingsArgsDict",
    "EngineSplitTrafficSplitArgs",
    "EngineSplitTrafficSplitArgsDict",
    "FlexibleAppVersionApiConfigArgs",
    "FlexibleAppVersionApiConfigArgsDict",
    "FlexibleAppVersionAutomaticScalingArgs",
    "FlexibleAppVersionAutomaticScalingArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FlexibleAppVersionDeploymentArgs",
    "FlexibleAppVersionDeploymentArgsDict",
    "FlexibleAppVersionDeploymentCloudBuildOptionsArgs",
    ...,
    "FlexibleAppVersionDeploymentContainerArgs",
    "FlexibleAppVersionDeploymentContainerArgsDict",
    "FlexibleAppVersionDeploymentFileArgs",
    "FlexibleAppVersionDeploymentFileArgsDict",
    "FlexibleAppVersionDeploymentZipArgs",
    "FlexibleAppVersionDeploymentZipArgsDict",
    "FlexibleAppVersionEndpointsApiServiceArgs",
    "FlexibleAppVersionEndpointsApiServiceArgsDict",
    "FlexibleAppVersionEntrypointArgs",
    "FlexibleAppVersionEntrypointArgsDict",
    "FlexibleAppVersionFlexibleRuntimeSettingsArgs",
    "FlexibleAppVersionFlexibleRuntimeSettingsArgsDict",
    "FlexibleAppVersionHandlerArgs",
    "FlexibleAppVersionHandlerArgsDict",
    "FlexibleAppVersionHandlerScriptArgs",
    "FlexibleAppVersionHandlerScriptArgsDict",
    "FlexibleAppVersionHandlerStaticFilesArgs",
    "FlexibleAppVersionHandlerStaticFilesArgsDict",
    "FlexibleAppVersionLivenessCheckArgs",
    "FlexibleAppVersionLivenessCheckArgsDict",
    "FlexibleAppVersionManualScalingArgs",
    "FlexibleAppVersionManualScalingArgsDict",
    "FlexibleAppVersionNetworkArgs",
    "FlexibleAppVersionNetworkArgsDict",
    "FlexibleAppVersionReadinessCheckArgs",
    "FlexibleAppVersionReadinessCheckArgsDict",
    "FlexibleAppVersionResourcesArgs",
    "FlexibleAppVersionResourcesArgsDict",
    "FlexibleAppVersionResourcesVolumeArgs",
    "FlexibleAppVersionResourcesVolumeArgsDict",
    "FlexibleAppVersionVpcAccessConnectorArgs",
    "FlexibleAppVersionVpcAccessConnectorArgsDict",
    "ServiceNetworkSettingsNetworkSettingsArgs",
    "ServiceNetworkSettingsNetworkSettingsArgsDict",
    "StandardAppVersionAutomaticScalingArgs",
    "StandardAppVersionAutomaticScalingArgsDict",
    ...,
    ...,
    "StandardAppVersionBasicScalingArgs",
    "StandardAppVersionBasicScalingArgsDict",
    "StandardAppVersionDeploymentArgs",
    "StandardAppVersionDeploymentArgsDict",
    "StandardAppVersionDeploymentFileArgs",
    "StandardAppVersionDeploymentFileArgsDict",
    "StandardAppVersionDeploymentZipArgs",
    "StandardAppVersionDeploymentZipArgsDict",
    "StandardAppVersionEntrypointArgs",
    "StandardAppVersionEntrypointArgsDict",
    "StandardAppVersionHandlerArgs",
    "StandardAppVersionHandlerArgsDict",
    "StandardAppVersionHandlerScriptArgs",
    "StandardAppVersionHandlerScriptArgsDict",
    "StandardAppVersionHandlerStaticFilesArgs",
    "StandardAppVersionHandlerStaticFilesArgsDict",
    "StandardAppVersionLibraryArgs",
    "StandardAppVersionLibraryArgsDict",
    "StandardAppVersionManualScalingArgs",
    "StandardAppVersionManualScalingArgsDict",
    "StandardAppVersionVpcAccessConnectorArgs",
    "StandardAppVersionVpcAccessConnectorArgsDict",
]

class ApplicationFeatureSettingsArgsDict(TypedDict):
    split_health_checks: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class ApplicationFeatureSettingsArgs:
    def __init__(
        __self__, *, split_health_checks: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="splitHealthChecks")
    def split_health_checks(self) -> pulumi.Input[_builtins.bool]: ...
    @split_health_checks.setter
    def split_health_checks(self, value: pulumi.Input[_builtins.bool]): ...

class ApplicationIapArgsDict(TypedDict):
    oauth2_client_id: pulumi.Input[_builtins.str]
    oauth2_client_secret: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    oauth2_client_secret_sha256: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApplicationIapArgs:
    def __init__(
        __self__,
        *,
        oauth2_client_id: pulumi.Input[_builtins.str],
        oauth2_client_secret: pulumi.Input[_builtins.str],
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        oauth2_client_secret_sha256: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientId")
    def oauth2_client_id(self) -> pulumi.Input[_builtins.str]: ...
    @oauth2_client_id.setter
    def oauth2_client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientSecret")
    def oauth2_client_secret(self) -> pulumi.Input[_builtins.str]: ...
    @oauth2_client_secret.setter
    def oauth2_client_secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientSecretSha256")
    def oauth2_client_secret_sha256(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oauth2_client_secret_sha256.setter
    def oauth2_client_secret_sha256(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ApplicationUrlDispatchRuleArgsDict(TypedDict):
    domain: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApplicationUrlDispatchRuleArgs:
    def __init__(
        __self__,
        *,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationUrlDispatchRulesDispatchRuleArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApplicationUrlDispatchRulesDispatchRuleArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainMappingResourceRecordArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    rrdata: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainMappingResourceRecordArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        rrdata: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rrdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rrdata.setter
    def rrdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainMappingSslSettingsArgsDict(TypedDict):
    ssl_management_type: pulumi.Input[_builtins.str]
    certificate_id: NotRequired[pulumi.Input[_builtins.str]]
    pending_managed_certificate_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainMappingSslSettingsArgs:
    def __init__(
        __self__,
        *,
        ssl_management_type: pulumi.Input[_builtins.str],
        certificate_id: Optional[pulumi.Input[_builtins.str]] = ...,
        pending_managed_certificate_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sslManagementType")
    def ssl_management_type(self) -> pulumi.Input[_builtins.str]: ...
    @ssl_management_type.setter
    def ssl_management_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pendingManagedCertificateId")
    def pending_managed_certificate_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pending_managed_certificate_id.setter
    def pending_managed_certificate_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EngineSplitTrafficSplitArgsDict(TypedDict):
    allocations: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    shard_by: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EngineSplitTrafficSplitArgs:
    def __init__(
        __self__,
        *,
        allocations: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        shard_by: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allocations(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @allocations.setter
    def allocations(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shardBy")
    def shard_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shard_by.setter
    def shard_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionApiConfigArgsDict(TypedDict):
    script: pulumi.Input[_builtins.str]
    auth_fail_action: NotRequired[pulumi.Input[_builtins.str]]
    login: NotRequired[pulumi.Input[_builtins.str]]
    security_level: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionApiConfigArgs:
    def __init__(
        __self__,
        *,
        script: pulumi.Input[_builtins.str],
        auth_fail_action: Optional[pulumi.Input[_builtins.str]] = ...,
        login: Optional[pulumi.Input[_builtins.str]] = ...,
        security_level: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> pulumi.Input[_builtins.str]: ...
    @script.setter
    def script(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authFailAction")
    def auth_fail_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_fail_action.setter
    def auth_fail_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login.setter
    def login(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityLevel")
    def security_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_level.setter
    def security_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionAutomaticScalingArgsDict(TypedDict):
    cpu_utilization: pulumi.Input[
        FlexibleAppVersionAutomaticScalingCpuUtilizationArgsDict
    ]
    cool_down_period: NotRequired[pulumi.Input[_builtins.str]]
    disk_utilization: NotRequired[
        pulumi.Input[FlexibleAppVersionAutomaticScalingDiskUtilizationArgsDict]
    ]
    max_concurrent_requests: NotRequired[pulumi.Input[_builtins.int]]
    max_idle_instances: NotRequired[pulumi.Input[_builtins.int]]
    max_pending_latency: NotRequired[pulumi.Input[_builtins.str]]
    max_total_instances: NotRequired[pulumi.Input[_builtins.int]]
    min_idle_instances: NotRequired[pulumi.Input[_builtins.int]]
    min_pending_latency: NotRequired[pulumi.Input[_builtins.str]]
    min_total_instances: NotRequired[pulumi.Input[_builtins.int]]
    network_utilization: NotRequired[
        pulumi.Input[FlexibleAppVersionAutomaticScalingNetworkUtilizationArgsDict]
    ]
    request_utilization: NotRequired[
        pulumi.Input[FlexibleAppVersionAutomaticScalingRequestUtilizationArgsDict]
    ]
    ...

@pulumi.input_type
class FlexibleAppVersionAutomaticScalingArgs:
    def __init__(
        __self__,
        *,
        cpu_utilization: pulumi.Input[
            FlexibleAppVersionAutomaticScalingCpuUtilizationArgs
        ],
        cool_down_period: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_utilization: Optional[
            pulumi.Input[FlexibleAppVersionAutomaticScalingDiskUtilizationArgs]
        ] = ...,
        max_concurrent_requests: Optional[pulumi.Input[_builtins.int]] = ...,
        max_idle_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        max_pending_latency: Optional[pulumi.Input[_builtins.str]] = ...,
        max_total_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        min_idle_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        min_pending_latency: Optional[pulumi.Input[_builtins.str]] = ...,
        min_total_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        network_utilization: Optional[
            pulumi.Input[FlexibleAppVersionAutomaticScalingNetworkUtilizationArgs]
        ] = ...,
        request_utilization: Optional[
            pulumi.Input[FlexibleAppVersionAutomaticScalingRequestUtilizationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuUtilization")
    def cpu_utilization(
        self,
    ) -> pulumi.Input[FlexibleAppVersionAutomaticScalingCpuUtilizationArgs]: ...
    @cpu_utilization.setter
    def cpu_utilization(
        self, value: pulumi.Input[FlexibleAppVersionAutomaticScalingCpuUtilizationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="coolDownPeriod")
    def cool_down_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cool_down_period.setter
    def cool_down_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskUtilization")
    def disk_utilization(
        self,
    ) -> Optional[
        pulumi.Input[FlexibleAppVersionAutomaticScalingDiskUtilizationArgs]
    ]: ...
    @disk_utilization.setter
    def disk_utilization(
        self,
        value: Optional[
            pulumi.Input[FlexibleAppVersionAutomaticScalingDiskUtilizationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRequests")
    def max_concurrent_requests(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_requests.setter
    def max_concurrent_requests(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxIdleInstances")
    def max_idle_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_idle_instances.setter
    def max_idle_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPendingLatency")
    def max_pending_latency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_pending_latency.setter
    def max_pending_latency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxTotalInstances")
    def max_total_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_total_instances.setter
    def max_total_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minIdleInstances")
    def min_idle_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_idle_instances.setter
    def min_idle_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minPendingLatency")
    def min_pending_latency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_pending_latency.setter
    def min_pending_latency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minTotalInstances")
    def min_total_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_total_instances.setter
    def min_total_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="networkUtilization")
    def network_utilization(
        self,
    ) -> Optional[
        pulumi.Input[FlexibleAppVersionAutomaticScalingNetworkUtilizationArgs]
    ]: ...
    @network_utilization.setter
    def network_utilization(
        self,
        value: Optional[
            pulumi.Input[FlexibleAppVersionAutomaticScalingNetworkUtilizationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestUtilization")
    def request_utilization(
        self,
    ) -> Optional[
        pulumi.Input[FlexibleAppVersionAutomaticScalingRequestUtilizationArgs]
    ]: ...
    @request_utilization.setter
    def request_utilization(
        self,
        value: Optional[
            pulumi.Input[FlexibleAppVersionAutomaticScalingRequestUtilizationArgs]
        ],
    ): ...

class FlexibleAppVersionAutomaticScalingCpuUtilizationArgsDict(TypedDict):
    target_utilization: pulumi.Input[_builtins.float]
    aggregation_window_length: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionAutomaticScalingCpuUtilizationArgs:
    def __init__(
        __self__,
        *,
        target_utilization: pulumi.Input[_builtins.float],
        aggregation_window_length: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetUtilization")
    def target_utilization(self) -> pulumi.Input[_builtins.float]: ...
    @target_utilization.setter
    def target_utilization(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="aggregationWindowLength")
    def aggregation_window_length(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aggregation_window_length.setter
    def aggregation_window_length(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FlexibleAppVersionAutomaticScalingDiskUtilizationArgsDict(TypedDict):
    target_read_bytes_per_second: NotRequired[pulumi.Input[_builtins.int]]
    target_read_ops_per_second: NotRequired[pulumi.Input[_builtins.int]]
    target_write_bytes_per_second: NotRequired[pulumi.Input[_builtins.int]]
    target_write_ops_per_second: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class FlexibleAppVersionAutomaticScalingDiskUtilizationArgs:
    def __init__(
        __self__,
        *,
        target_read_bytes_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        target_read_ops_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        target_write_bytes_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        target_write_ops_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetReadBytesPerSecond")
    def target_read_bytes_per_second(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_read_bytes_per_second.setter
    def target_read_bytes_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetReadOpsPerSecond")
    def target_read_ops_per_second(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_read_ops_per_second.setter
    def target_read_ops_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetWriteBytesPerSecond")
    def target_write_bytes_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_write_bytes_per_second.setter
    def target_write_bytes_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetWriteOpsPerSecond")
    def target_write_ops_per_second(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_write_ops_per_second.setter
    def target_write_ops_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class FlexibleAppVersionAutomaticScalingNetworkUtilizationArgsDict(TypedDict):
    target_received_bytes_per_second: NotRequired[pulumi.Input[_builtins.int]]
    target_received_packets_per_second: NotRequired[pulumi.Input[_builtins.int]]
    target_sent_bytes_per_second: NotRequired[pulumi.Input[_builtins.int]]
    target_sent_packets_per_second: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class FlexibleAppVersionAutomaticScalingNetworkUtilizationArgs:
    def __init__(
        __self__,
        *,
        target_received_bytes_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        target_received_packets_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        target_sent_bytes_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        target_sent_packets_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetReceivedBytesPerSecond")
    def target_received_bytes_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_received_bytes_per_second.setter
    def target_received_bytes_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetReceivedPacketsPerSecond")
    def target_received_packets_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_received_packets_per_second.setter
    def target_received_packets_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSentBytesPerSecond")
    def target_sent_bytes_per_second(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_sent_bytes_per_second.setter
    def target_sent_bytes_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSentPacketsPerSecond")
    def target_sent_packets_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_sent_packets_per_second.setter
    def target_sent_packets_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class FlexibleAppVersionAutomaticScalingRequestUtilizationArgsDict(TypedDict):
    target_concurrent_requests: NotRequired[pulumi.Input[_builtins.float]]
    target_request_count_per_second: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionAutomaticScalingRequestUtilizationArgs:
    def __init__(
        __self__,
        *,
        target_concurrent_requests: Optional[pulumi.Input[_builtins.float]] = ...,
        target_request_count_per_second: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetConcurrentRequests")
    def target_concurrent_requests(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @target_concurrent_requests.setter
    def target_concurrent_requests(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetRequestCountPerSecond")
    def target_request_count_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_request_count_per_second.setter
    def target_request_count_per_second(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FlexibleAppVersionDeploymentArgsDict(TypedDict):
    cloud_build_options: NotRequired[
        pulumi.Input[FlexibleAppVersionDeploymentCloudBuildOptionsArgsDict]
    ]
    container: NotRequired[pulumi.Input[FlexibleAppVersionDeploymentContainerArgsDict]]
    files: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionDeploymentFileArgsDict]]]
    ]
    zip: NotRequired[pulumi.Input[FlexibleAppVersionDeploymentZipArgsDict]]
    ...

@pulumi.input_type
class FlexibleAppVersionDeploymentArgs:
    def __init__(
        __self__,
        *,
        cloud_build_options: Optional[
            pulumi.Input[FlexibleAppVersionDeploymentCloudBuildOptionsArgs]
        ] = ...,
        container: Optional[
            pulumi.Input[FlexibleAppVersionDeploymentContainerArgs]
        ] = ...,
        files: Optional[
            pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionDeploymentFileArgs]]]
        ] = ...,
        zip: Optional[pulumi.Input[FlexibleAppVersionDeploymentZipArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudBuildOptions")
    def cloud_build_options(
        self,
    ) -> Optional[pulumi.Input[FlexibleAppVersionDeploymentCloudBuildOptionsArgs]]: ...
    @cloud_build_options.setter
    def cloud_build_options(
        self,
        value: Optional[
            pulumi.Input[FlexibleAppVersionDeploymentCloudBuildOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def container(
        self,
    ) -> Optional[pulumi.Input[FlexibleAppVersionDeploymentContainerArgs]]: ...
    @container.setter
    def container(
        self, value: Optional[pulumi.Input[FlexibleAppVersionDeploymentContainerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionDeploymentFileArgs]]]
    ]: ...
    @files.setter
    def files(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionDeploymentFileArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zip(self) -> Optional[pulumi.Input[FlexibleAppVersionDeploymentZipArgs]]: ...
    @zip.setter
    def zip(
        self, value: Optional[pulumi.Input[FlexibleAppVersionDeploymentZipArgs]]
    ): ...

class FlexibleAppVersionDeploymentCloudBuildOptionsArgsDict(TypedDict):
    app_yaml_path: pulumi.Input[_builtins.str]
    cloud_build_timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionDeploymentCloudBuildOptionsArgs:
    def __init__(
        __self__,
        *,
        app_yaml_path: pulumi.Input[_builtins.str],
        cloud_build_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appYamlPath")
    def app_yaml_path(self) -> pulumi.Input[_builtins.str]: ...
    @app_yaml_path.setter
    def app_yaml_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cloudBuildTimeout")
    def cloud_build_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_build_timeout.setter
    def cloud_build_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionDeploymentContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FlexibleAppVersionDeploymentContainerArgs:
    def __init__(__self__, *, image: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]: ...
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): ...

class FlexibleAppVersionDeploymentFileArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    source_url: pulumi.Input[_builtins.str]
    sha1_sum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionDeploymentFileArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        source_url: pulumi.Input[_builtins.str],
        sha1_sum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> pulumi.Input[_builtins.str]: ...
    @source_url.setter
    def source_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha1Sum")
    def sha1_sum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha1_sum.setter
    def sha1_sum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionDeploymentZipArgsDict(TypedDict):
    source_url: pulumi.Input[_builtins.str]
    files_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class FlexibleAppVersionDeploymentZipArgs:
    def __init__(
        __self__,
        *,
        source_url: pulumi.Input[_builtins.str],
        files_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> pulumi.Input[_builtins.str]: ...
    @source_url.setter
    def source_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="filesCount")
    def files_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @files_count.setter
    def files_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class FlexibleAppVersionEndpointsApiServiceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    config_id: NotRequired[pulumi.Input[_builtins.str]]
    disable_trace_sampling: NotRequired[pulumi.Input[_builtins.bool]]
    rollout_strategy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionEndpointsApiServiceArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_trace_sampling: Optional[pulumi.Input[_builtins.bool]] = ...,
        rollout_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @config_id.setter
    def config_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableTraceSampling")
    def disable_trace_sampling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_trace_sampling.setter
    def disable_trace_sampling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutStrategy")
    def rollout_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_strategy.setter
    def rollout_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionEntrypointArgsDict(TypedDict):
    shell: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FlexibleAppVersionEntrypointArgs:
    def __init__(__self__, *, shell: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def shell(self) -> pulumi.Input[_builtins.str]: ...
    @shell.setter
    def shell(self, value: pulumi.Input[_builtins.str]): ...

class FlexibleAppVersionFlexibleRuntimeSettingsArgsDict(TypedDict):
    operating_system: NotRequired[pulumi.Input[_builtins.str]]
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionFlexibleRuntimeSettingsArgs:
    def __init__(
        __self__,
        *,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionHandlerArgsDict(TypedDict):
    auth_fail_action: NotRequired[pulumi.Input[_builtins.str]]
    login: NotRequired[pulumi.Input[_builtins.str]]
    redirect_http_response_code: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[FlexibleAppVersionHandlerScriptArgsDict]]
    security_level: NotRequired[pulumi.Input[_builtins.str]]
    static_files: NotRequired[
        pulumi.Input[FlexibleAppVersionHandlerStaticFilesArgsDict]
    ]
    url_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionHandlerArgs:
    def __init__(
        __self__,
        *,
        auth_fail_action: Optional[pulumi.Input[_builtins.str]] = ...,
        login: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_http_response_code: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[FlexibleAppVersionHandlerScriptArgs]] = ...,
        security_level: Optional[pulumi.Input[_builtins.str]] = ...,
        static_files: Optional[
            pulumi.Input[FlexibleAppVersionHandlerStaticFilesArgs]
        ] = ...,
        url_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authFailAction")
    def auth_fail_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_fail_action.setter
    def auth_fail_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login.setter
    def login(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectHttpResponseCode")
    def redirect_http_response_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_http_response_code.setter
    def redirect_http_response_code(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[FlexibleAppVersionHandlerScriptArgs]]: ...
    @script.setter
    def script(
        self, value: Optional[pulumi.Input[FlexibleAppVersionHandlerScriptArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityLevel")
    def security_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_level.setter
    def security_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="staticFiles")
    def static_files(
        self,
    ) -> Optional[pulumi.Input[FlexibleAppVersionHandlerStaticFilesArgs]]: ...
    @static_files.setter
    def static_files(
        self, value: Optional[pulumi.Input[FlexibleAppVersionHandlerStaticFilesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlRegex")
    def url_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url_regex.setter
    def url_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionHandlerScriptArgsDict(TypedDict):
    script_path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FlexibleAppVersionHandlerScriptArgs:
    def __init__(__self__, *, script_path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scriptPath")
    def script_path(self) -> pulumi.Input[_builtins.str]: ...
    @script_path.setter
    def script_path(self, value: pulumi.Input[_builtins.str]): ...

class FlexibleAppVersionHandlerStaticFilesArgsDict(TypedDict):
    application_readable: NotRequired[pulumi.Input[_builtins.bool]]
    expiration: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    mime_type: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    require_matching_file: NotRequired[pulumi.Input[_builtins.bool]]
    upload_path_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionHandlerStaticFilesArgs:
    def __init__(
        __self__,
        *,
        application_readable: Optional[pulumi.Input[_builtins.bool]] = ...,
        expiration: Optional[pulumi.Input[_builtins.str]] = ...,
        http_headers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        mime_type: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        require_matching_file: Optional[pulumi.Input[_builtins.bool]] = ...,
        upload_path_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationReadable")
    def application_readable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @application_readable.setter
    def application_readable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @http_headers.setter
    def http_headers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mime_type.setter
    def mime_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requireMatchingFile")
    def require_matching_file(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_matching_file.setter
    def require_matching_file(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="uploadPathRegex")
    def upload_path_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upload_path_regex.setter
    def upload_path_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionLivenessCheckArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    check_interval: NotRequired[pulumi.Input[_builtins.str]]
    failure_threshold: NotRequired[pulumi.Input[_builtins.float]]
    host: NotRequired[pulumi.Input[_builtins.str]]
    initial_delay: NotRequired[pulumi.Input[_builtins.str]]
    success_threshold: NotRequired[pulumi.Input[_builtins.float]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionLivenessCheckArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        check_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_delay: Optional[pulumi.Input[_builtins.str]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="checkInterval")
    def check_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @check_interval.setter
    def check_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialDelay")
    def initial_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_delay.setter
    def initial_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionManualScalingArgsDict(TypedDict):
    instances: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class FlexibleAppVersionManualScalingArgs:
    def __init__(__self__, *, instances: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> pulumi.Input[_builtins.int]: ...
    @instances.setter
    def instances(self, value: pulumi.Input[_builtins.int]): ...

class FlexibleAppVersionNetworkArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    forwarded_ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    instance_ip_mode: NotRequired[pulumi.Input[_builtins.str]]
    instance_tag: NotRequired[pulumi.Input[_builtins.str]]
    session_affinity: NotRequired[pulumi.Input[_builtins.bool]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionNetworkArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        forwarded_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_ip_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.bool]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="forwardedPorts")
    def forwarded_ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @forwarded_ports.setter
    def forwarded_ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceIpMode")
    def instance_ip_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_ip_mode.setter
    def instance_ip_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceTag")
    def instance_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_tag.setter
    def instance_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @session_affinity.setter
    def session_affinity(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionReadinessCheckArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    app_start_timeout: NotRequired[pulumi.Input[_builtins.str]]
    check_interval: NotRequired[pulumi.Input[_builtins.str]]
    failure_threshold: NotRequired[pulumi.Input[_builtins.float]]
    host: NotRequired[pulumi.Input[_builtins.str]]
    success_threshold: NotRequired[pulumi.Input[_builtins.float]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FlexibleAppVersionReadinessCheckArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        app_start_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        check_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appStartTimeout")
    def app_start_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_start_timeout.setter
    def app_start_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checkInterval")
    def check_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @check_interval.setter
    def check_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlexibleAppVersionResourcesArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.int]]
    disk_gb: NotRequired[pulumi.Input[_builtins.int]]
    memory_gb: NotRequired[pulumi.Input[_builtins.float]]
    volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionResourcesVolumeArgsDict]]]
    ]
    ...

@pulumi.input_type
class FlexibleAppVersionResourcesArgs:
    def __init__(
        __self__,
        *,
        cpu: Optional[pulumi.Input[_builtins.int]] = ...,
        disk_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        memory_gb: Optional[pulumi.Input[_builtins.float]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionResourcesVolumeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_gb.setter
    def disk_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @memory_gb.setter
    def memory_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionResourcesVolumeArgs]]]
    ]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FlexibleAppVersionResourcesVolumeArgs]]]
        ],
    ): ...

class FlexibleAppVersionResourcesVolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    size_gb: pulumi.Input[_builtins.int]
    volume_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FlexibleAppVersionResourcesVolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        size_gb: pulumi.Input[_builtins.int],
        volume_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Input[_builtins.int]: ...
    @size_gb.setter
    def size_gb(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Input[_builtins.str]: ...
    @volume_type.setter
    def volume_type(self, value: pulumi.Input[_builtins.str]): ...

class FlexibleAppVersionVpcAccessConnectorArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FlexibleAppVersionVpcAccessConnectorArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ServiceNetworkSettingsNetworkSettingsArgsDict(TypedDict):
    ingress_traffic_allowed: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceNetworkSettingsNetworkSettingsArgs:
    def __init__(
        __self__,
        *,
        ingress_traffic_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressTrafficAllowed")
    def ingress_traffic_allowed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingress_traffic_allowed.setter
    def ingress_traffic_allowed(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StandardAppVersionAutomaticScalingArgsDict(TypedDict):
    max_concurrent_requests: NotRequired[pulumi.Input[_builtins.int]]
    max_idle_instances: NotRequired[pulumi.Input[_builtins.int]]
    max_pending_latency: NotRequired[pulumi.Input[_builtins.str]]
    min_idle_instances: NotRequired[pulumi.Input[_builtins.int]]
    min_pending_latency: NotRequired[pulumi.Input[_builtins.str]]
    standard_scheduler_settings: NotRequired[
        pulumi.Input[
            StandardAppVersionAutomaticScalingStandardSchedulerSettingsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class StandardAppVersionAutomaticScalingArgs:
    def __init__(
        __self__,
        *,
        max_concurrent_requests: Optional[pulumi.Input[_builtins.int]] = ...,
        max_idle_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        max_pending_latency: Optional[pulumi.Input[_builtins.str]] = ...,
        min_idle_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        min_pending_latency: Optional[pulumi.Input[_builtins.str]] = ...,
        standard_scheduler_settings: Optional[
            pulumi.Input[
                StandardAppVersionAutomaticScalingStandardSchedulerSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRequests")
    def max_concurrent_requests(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_requests.setter
    def max_concurrent_requests(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxIdleInstances")
    def max_idle_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_idle_instances.setter
    def max_idle_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPendingLatency")
    def max_pending_latency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_pending_latency.setter
    def max_pending_latency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minIdleInstances")
    def min_idle_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_idle_instances.setter
    def min_idle_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minPendingLatency")
    def min_pending_latency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_pending_latency.setter
    def min_pending_latency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="standardSchedulerSettings")
    def standard_scheduler_settings(
        self,
    ) -> Optional[
        pulumi.Input[StandardAppVersionAutomaticScalingStandardSchedulerSettingsArgs]
    ]: ...
    @standard_scheduler_settings.setter
    def standard_scheduler_settings(
        self,
        value: Optional[
            pulumi.Input[
                StandardAppVersionAutomaticScalingStandardSchedulerSettingsArgs
            ]
        ],
    ): ...

class StandardAppVersionAutomaticScalingStandardSchedulerSettingsArgsDict(TypedDict):
    max_instances: NotRequired[pulumi.Input[_builtins.int]]
    min_instances: NotRequired[pulumi.Input[_builtins.int]]
    target_cpu_utilization: NotRequired[pulumi.Input[_builtins.float]]
    target_throughput_utilization: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class StandardAppVersionAutomaticScalingStandardSchedulerSettingsArgs:
    def __init__(
        __self__,
        *,
        max_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        target_cpu_utilization: Optional[pulumi.Input[_builtins.float]] = ...,
        target_throughput_utilization: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instances.setter
    def max_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instances.setter
    def min_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetCpuUtilization")
    def target_cpu_utilization(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @target_cpu_utilization.setter
    def target_cpu_utilization(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetThroughputUtilization")
    def target_throughput_utilization(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @target_throughput_utilization.setter
    def target_throughput_utilization(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class StandardAppVersionBasicScalingArgsDict(TypedDict):
    max_instances: pulumi.Input[_builtins.int]
    idle_timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StandardAppVersionBasicScalingArgs:
    def __init__(
        __self__,
        *,
        max_instances: pulumi.Input[_builtins.int],
        idle_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> pulumi.Input[_builtins.int]: ...
    @max_instances.setter
    def max_instances(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StandardAppVersionDeploymentArgsDict(TypedDict):
    files: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StandardAppVersionDeploymentFileArgsDict]]]
    ]
    zip: NotRequired[pulumi.Input[StandardAppVersionDeploymentZipArgsDict]]
    ...

@pulumi.input_type
class StandardAppVersionDeploymentArgs:
    def __init__(
        __self__,
        *,
        files: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionDeploymentFileArgs]]]
        ] = ...,
        zip: Optional[pulumi.Input[StandardAppVersionDeploymentZipArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StandardAppVersionDeploymentFileArgs]]]
    ]: ...
    @files.setter
    def files(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StandardAppVersionDeploymentFileArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zip(self) -> Optional[pulumi.Input[StandardAppVersionDeploymentZipArgs]]: ...
    @zip.setter
    def zip(
        self, value: Optional[pulumi.Input[StandardAppVersionDeploymentZipArgs]]
    ): ...

class StandardAppVersionDeploymentFileArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    source_url: pulumi.Input[_builtins.str]
    sha1_sum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StandardAppVersionDeploymentFileArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        source_url: pulumi.Input[_builtins.str],
        sha1_sum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> pulumi.Input[_builtins.str]: ...
    @source_url.setter
    def source_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha1Sum")
    def sha1_sum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha1_sum.setter
    def sha1_sum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StandardAppVersionDeploymentZipArgsDict(TypedDict):
    source_url: pulumi.Input[_builtins.str]
    files_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StandardAppVersionDeploymentZipArgs:
    def __init__(
        __self__,
        *,
        source_url: pulumi.Input[_builtins.str],
        files_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> pulumi.Input[_builtins.str]: ...
    @source_url.setter
    def source_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="filesCount")
    def files_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @files_count.setter
    def files_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StandardAppVersionEntrypointArgsDict(TypedDict):
    shell: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StandardAppVersionEntrypointArgs:
    def __init__(__self__, *, shell: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def shell(self) -> pulumi.Input[_builtins.str]: ...
    @shell.setter
    def shell(self, value: pulumi.Input[_builtins.str]): ...

class StandardAppVersionHandlerArgsDict(TypedDict):
    auth_fail_action: NotRequired[pulumi.Input[_builtins.str]]
    login: NotRequired[pulumi.Input[_builtins.str]]
    redirect_http_response_code: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[StandardAppVersionHandlerScriptArgsDict]]
    security_level: NotRequired[pulumi.Input[_builtins.str]]
    static_files: NotRequired[
        pulumi.Input[StandardAppVersionHandlerStaticFilesArgsDict]
    ]
    url_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StandardAppVersionHandlerArgs:
    def __init__(
        __self__,
        *,
        auth_fail_action: Optional[pulumi.Input[_builtins.str]] = ...,
        login: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_http_response_code: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[StandardAppVersionHandlerScriptArgs]] = ...,
        security_level: Optional[pulumi.Input[_builtins.str]] = ...,
        static_files: Optional[
            pulumi.Input[StandardAppVersionHandlerStaticFilesArgs]
        ] = ...,
        url_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authFailAction")
    def auth_fail_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_fail_action.setter
    def auth_fail_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login.setter
    def login(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectHttpResponseCode")
    def redirect_http_response_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_http_response_code.setter
    def redirect_http_response_code(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[StandardAppVersionHandlerScriptArgs]]: ...
    @script.setter
    def script(
        self, value: Optional[pulumi.Input[StandardAppVersionHandlerScriptArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityLevel")
    def security_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_level.setter
    def security_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="staticFiles")
    def static_files(
        self,
    ) -> Optional[pulumi.Input[StandardAppVersionHandlerStaticFilesArgs]]: ...
    @static_files.setter
    def static_files(
        self, value: Optional[pulumi.Input[StandardAppVersionHandlerStaticFilesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlRegex")
    def url_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url_regex.setter
    def url_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StandardAppVersionHandlerScriptArgsDict(TypedDict):
    script_path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StandardAppVersionHandlerScriptArgs:
    def __init__(__self__, *, script_path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scriptPath")
    def script_path(self) -> pulumi.Input[_builtins.str]: ...
    @script_path.setter
    def script_path(self, value: pulumi.Input[_builtins.str]): ...

class StandardAppVersionHandlerStaticFilesArgsDict(TypedDict):
    application_readable: NotRequired[pulumi.Input[_builtins.bool]]
    expiration: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    mime_type: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    require_matching_file: NotRequired[pulumi.Input[_builtins.bool]]
    upload_path_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StandardAppVersionHandlerStaticFilesArgs:
    def __init__(
        __self__,
        *,
        application_readable: Optional[pulumi.Input[_builtins.bool]] = ...,
        expiration: Optional[pulumi.Input[_builtins.str]] = ...,
        http_headers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        mime_type: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        require_matching_file: Optional[pulumi.Input[_builtins.bool]] = ...,
        upload_path_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationReadable")
    def application_readable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @application_readable.setter
    def application_readable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @http_headers.setter
    def http_headers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mime_type.setter
    def mime_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requireMatchingFile")
    def require_matching_file(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_matching_file.setter
    def require_matching_file(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="uploadPathRegex")
    def upload_path_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upload_path_regex.setter
    def upload_path_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StandardAppVersionLibraryArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StandardAppVersionLibraryArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StandardAppVersionManualScalingArgsDict(TypedDict):
    instances: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class StandardAppVersionManualScalingArgs:
    def __init__(__self__, *, instances: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> pulumi.Input[_builtins.int]: ...
    @instances.setter
    def instances(self, value: pulumi.Input[_builtins.int]): ...

class StandardAppVersionVpcAccessConnectorArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    egress_setting: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StandardAppVersionVpcAccessConnectorArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        egress_setting: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="egressSetting")
    def egress_setting(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @egress_setting.setter
    def egress_setting(self, value: Optional[pulumi.Input[_builtins.str]]): ...
