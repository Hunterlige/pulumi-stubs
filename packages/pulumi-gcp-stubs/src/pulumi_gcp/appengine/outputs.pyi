

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationFeatureSettings', 'ApplicationIap', 'ApplicationUrlDispatchRule', 'ApplicationUrlDispatchRulesDispatchRule', 'DomainMappingResourceRecord', 'DomainMappingSslSettings', 'EngineSplitTrafficSplit', 'FlexibleAppVersionApiConfig', 'FlexibleAppVersionAutomaticScaling', 'FlexibleAppVersionAutomaticScalingCpuUtilization', 'FlexibleAppVersionAutomaticScalingDiskUtilization', ..., ..., 'FlexibleAppVersionDeployment', 'FlexibleAppVersionDeploymentCloudBuildOptions', 'FlexibleAppVersionDeploymentContainer', 'FlexibleAppVersionDeploymentFile', 'FlexibleAppVersionDeploymentZip', 'FlexibleAppVersionEndpointsApiService', 'FlexibleAppVersionEntrypoint', 'FlexibleAppVersionFlexibleRuntimeSettings', 'FlexibleAppVersionHandler', 'FlexibleAppVersionHandlerScript', 'FlexibleAppVersionHandlerStaticFiles', 'FlexibleAppVersionLivenessCheck', 'FlexibleAppVersionManualScaling', 'FlexibleAppVersionNetwork', 'FlexibleAppVersionReadinessCheck', 'FlexibleAppVersionResources', 'FlexibleAppVersionResourcesVolume', 'FlexibleAppVersionVpcAccessConnector', 'ServiceNetworkSettingsNetworkSettings', 'StandardAppVersionAutomaticScaling', ..., 'StandardAppVersionBasicScaling', 'StandardAppVersionDeployment', 'StandardAppVersionDeploymentFile', 'StandardAppVersionDeploymentZip', 'StandardAppVersionEntrypoint', 'StandardAppVersionHandler', 'StandardAppVersionHandlerScript', 'StandardAppVersionHandlerStaticFiles', 'StandardAppVersionLibrary', 'StandardAppVersionManualScaling', 'StandardAppVersionVpcAccessConnector']
@pulumi.output_type
class ApplicationFeatureSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, split_health_checks: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="splitHealthChecks")
    def split_health_checks(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class ApplicationIap(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oauth2_client_id: _builtins.str, oauth2_client_secret: _builtins.str, enabled: Optional[_builtins.bool] = ..., oauth2_client_secret_sha256: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2ClientId")
    def oauth2_client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2ClientSecret")
    def oauth2_client_secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2ClientSecretSha256")
    def oauth2_client_secret_sha256(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationUrlDispatchRule(dict):
    def __init__(__self__, *, domain: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ..., service: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ApplicationUrlDispatchRulesDispatchRule(dict):
    def __init__(__self__, *, path: _builtins.str, service: _builtins.str, domain: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainMappingResourceRecord(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., rrdata: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdata(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainMappingSslSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ssl_management_type: _builtins.str, certificate_id: Optional[_builtins.str] = ..., pending_managed_certificate_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslManagementType")
    def ssl_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingManagedCertificateId")
    def pending_managed_certificate_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EngineSplitTrafficSplit(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocations: Mapping[str, _builtins.str], shard_by: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allocations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardBy")
    def shard_by(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionApiConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, script: _builtins.str, auth_fail_action: Optional[_builtins.str] = ..., login: Optional[_builtins.str] = ..., security_level: Optional[_builtins.str] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authFailAction")
    def auth_fail_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityLevel")
    def security_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionAutomaticScaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_utilization: outputs.FlexibleAppVersionAutomaticScalingCpuUtilization, cool_down_period: Optional[_builtins.str] = ..., disk_utilization: Optional[outputs.FlexibleAppVersionAutomaticScalingDiskUtilization] = ..., max_concurrent_requests: Optional[_builtins.int] = ..., max_idle_instances: Optional[_builtins.int] = ..., max_pending_latency: Optional[_builtins.str] = ..., max_total_instances: Optional[_builtins.int] = ..., min_idle_instances: Optional[_builtins.int] = ..., min_pending_latency: Optional[_builtins.str] = ..., min_total_instances: Optional[_builtins.int] = ..., network_utilization: Optional[outputs.FlexibleAppVersionAutomaticScalingNetworkUtilization] = ..., request_utilization: Optional[outputs.FlexibleAppVersionAutomaticScalingRequestUtilization] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuUtilization")
    def cpu_utilization(self) -> outputs.FlexibleAppVersionAutomaticScalingCpuUtilization:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolDownPeriod")
    def cool_down_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskUtilization")
    def disk_utilization(self) -> Optional[outputs.FlexibleAppVersionAutomaticScalingDiskUtilization]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRequests")
    def max_concurrent_requests(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIdleInstances")
    def max_idle_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPendingLatency")
    def max_pending_latency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTotalInstances")
    def max_total_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minIdleInstances")
    def min_idle_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPendingLatency")
    def min_pending_latency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTotalInstances")
    def min_total_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUtilization")
    def network_utilization(self) -> Optional[outputs.FlexibleAppVersionAutomaticScalingNetworkUtilization]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestUtilization")
    def request_utilization(self) -> Optional[outputs.FlexibleAppVersionAutomaticScalingRequestUtilization]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionAutomaticScalingCpuUtilization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_utilization: _builtins.float, aggregation_window_length: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUtilization")
    def target_utilization(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregationWindowLength")
    def aggregation_window_length(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionAutomaticScalingDiskUtilization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_read_bytes_per_second: Optional[_builtins.int] = ..., target_read_ops_per_second: Optional[_builtins.int] = ..., target_write_bytes_per_second: Optional[_builtins.int] = ..., target_write_ops_per_second: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetReadBytesPerSecond")
    def target_read_bytes_per_second(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetReadOpsPerSecond")
    def target_read_ops_per_second(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetWriteBytesPerSecond")
    def target_write_bytes_per_second(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetWriteOpsPerSecond")
    def target_write_ops_per_second(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionAutomaticScalingNetworkUtilization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_received_bytes_per_second: Optional[_builtins.int] = ..., target_received_packets_per_second: Optional[_builtins.int] = ..., target_sent_bytes_per_second: Optional[_builtins.int] = ..., target_sent_packets_per_second: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetReceivedBytesPerSecond")
    def target_received_bytes_per_second(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetReceivedPacketsPerSecond")
    def target_received_packets_per_second(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSentBytesPerSecond")
    def target_sent_bytes_per_second(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSentPacketsPerSecond")
    def target_sent_packets_per_second(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionAutomaticScalingRequestUtilization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_concurrent_requests: Optional[_builtins.float] = ..., target_request_count_per_second: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConcurrentRequests")
    def target_concurrent_requests(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRequestCountPerSecond")
    def target_request_count_per_second(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionDeployment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_build_options: Optional[outputs.FlexibleAppVersionDeploymentCloudBuildOptions] = ..., container: Optional[outputs.FlexibleAppVersionDeploymentContainer] = ..., files: Optional[Sequence[outputs.FlexibleAppVersionDeploymentFile]] = ..., zip: Optional[outputs.FlexibleAppVersionDeploymentZip] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudBuildOptions")
    def cloud_build_options(self) -> Optional[outputs.FlexibleAppVersionDeploymentCloudBuildOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[outputs.FlexibleAppVersionDeploymentContainer]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def files(self) -> Optional[Sequence[outputs.FlexibleAppVersionDeploymentFile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zip(self) -> Optional[outputs.FlexibleAppVersionDeploymentZip]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionDeploymentCloudBuildOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_yaml_path: _builtins.str, cloud_build_timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appYamlPath")
    def app_yaml_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudBuildTimeout")
    def cloud_build_timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionDeploymentContainer(dict):
    def __init__(__self__, *, image: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionDeploymentFile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, source_url: _builtins.str, sha1_sum: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha1Sum")
    def sha1_sum(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionDeploymentZip(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_url: _builtins.str, files_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesCount")
    def files_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionEndpointsApiService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, config_id: Optional[_builtins.str] = ..., disable_trace_sampling: Optional[_builtins.bool] = ..., rollout_strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableTraceSampling")
    def disable_trace_sampling(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloutStrategy")
    def rollout_strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionEntrypoint(dict):
    def __init__(__self__, *, shell: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shell(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionFlexibleRuntimeSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, operating_system: Optional[_builtins.str] = ..., runtime_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionHandler(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_fail_action: Optional[_builtins.str] = ..., login: Optional[_builtins.str] = ..., redirect_http_response_code: Optional[_builtins.str] = ..., script: Optional[outputs.FlexibleAppVersionHandlerScript] = ..., security_level: Optional[_builtins.str] = ..., static_files: Optional[outputs.FlexibleAppVersionHandlerStaticFiles] = ..., url_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authFailAction")
    def auth_fail_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectHttpResponseCode")
    def redirect_http_response_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[outputs.FlexibleAppVersionHandlerScript]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityLevel")
    def security_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticFiles")
    def static_files(self) -> Optional[outputs.FlexibleAppVersionHandlerStaticFiles]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlRegex")
    def url_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionHandlerScript(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, script_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptPath")
    def script_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionHandlerStaticFiles(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_readable: Optional[_builtins.bool] = ..., expiration: Optional[_builtins.str] = ..., http_headers: Optional[Mapping[str, _builtins.str]] = ..., mime_type: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ..., require_matching_file: Optional[_builtins.bool] = ..., upload_path_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationReadable")
    def application_readable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireMatchingFile")
    def require_matching_file(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadPathRegex")
    def upload_path_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionLivenessCheck(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, check_interval: Optional[_builtins.str] = ..., failure_threshold: Optional[_builtins.float] = ..., host: Optional[_builtins.str] = ..., initial_delay: Optional[_builtins.str] = ..., success_threshold: Optional[_builtins.float] = ..., timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkInterval")
    def check_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelay")
    def initial_delay(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionManualScaling(dict):
    def __init__(__self__, *, instances: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionNetwork(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, forwarded_ports: Optional[Sequence[_builtins.str]] = ..., instance_ip_mode: Optional[_builtins.str] = ..., instance_tag: Optional[_builtins.str] = ..., session_affinity: Optional[_builtins.bool] = ..., subnetwork: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedPorts")
    def forwarded_ports(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceIpMode")
    def instance_ip_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTag")
    def instance_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionReadinessCheck(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, app_start_timeout: Optional[_builtins.str] = ..., check_interval: Optional[_builtins.str] = ..., failure_threshold: Optional[_builtins.float] = ..., host: Optional[_builtins.str] = ..., success_threshold: Optional[_builtins.float] = ..., timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appStartTimeout")
    def app_start_timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkInterval")
    def check_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionResources(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu: Optional[_builtins.int] = ..., disk_gb: Optional[_builtins.int] = ..., memory_gb: Optional[_builtins.float] = ..., volumes: Optional[Sequence[outputs.FlexibleAppVersionResourcesVolume]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.FlexibleAppVersionResourcesVolume]]:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionResourcesVolume(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, size_gb: _builtins.int, volume_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FlexibleAppVersionVpcAccessConnector(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceNetworkSettingsNetworkSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ingress_traffic_allowed: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressTrafficAllowed")
    def ingress_traffic_allowed(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionAutomaticScaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_concurrent_requests: Optional[_builtins.int] = ..., max_idle_instances: Optional[_builtins.int] = ..., max_pending_latency: Optional[_builtins.str] = ..., min_idle_instances: Optional[_builtins.int] = ..., min_pending_latency: Optional[_builtins.str] = ..., standard_scheduler_settings: Optional[outputs.StandardAppVersionAutomaticScalingStandardSchedulerSettings] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRequests")
    def max_concurrent_requests(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIdleInstances")
    def max_idle_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPendingLatency")
    def max_pending_latency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minIdleInstances")
    def min_idle_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPendingLatency")
    def min_pending_latency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardSchedulerSettings")
    def standard_scheduler_settings(self) -> Optional[outputs.StandardAppVersionAutomaticScalingStandardSchedulerSettings]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionAutomaticScalingStandardSchedulerSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_instances: Optional[_builtins.int] = ..., min_instances: Optional[_builtins.int] = ..., target_cpu_utilization: Optional[_builtins.float] = ..., target_throughput_utilization: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCpuUtilization")
    def target_cpu_utilization(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetThroughputUtilization")
    def target_throughput_utilization(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionBasicScaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_instances: _builtins.int, idle_timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionDeployment(dict):
    def __init__(__self__, *, files: Optional[Sequence[outputs.StandardAppVersionDeploymentFile]] = ..., zip: Optional[outputs.StandardAppVersionDeploymentZip] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def files(self) -> Optional[Sequence[outputs.StandardAppVersionDeploymentFile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zip(self) -> Optional[outputs.StandardAppVersionDeploymentZip]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionDeploymentFile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, source_url: _builtins.str, sha1_sum: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha1Sum")
    def sha1_sum(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionDeploymentZip(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_url: _builtins.str, files_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesCount")
    def files_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionEntrypoint(dict):
    def __init__(__self__, *, shell: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shell(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class StandardAppVersionHandler(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_fail_action: Optional[_builtins.str] = ..., login: Optional[_builtins.str] = ..., redirect_http_response_code: Optional[_builtins.str] = ..., script: Optional[outputs.StandardAppVersionHandlerScript] = ..., security_level: Optional[_builtins.str] = ..., static_files: Optional[outputs.StandardAppVersionHandlerStaticFiles] = ..., url_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authFailAction")
    def auth_fail_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectHttpResponseCode")
    def redirect_http_response_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[outputs.StandardAppVersionHandlerScript]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityLevel")
    def security_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticFiles")
    def static_files(self) -> Optional[outputs.StandardAppVersionHandlerStaticFiles]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlRegex")
    def url_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionHandlerScript(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, script_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptPath")
    def script_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class StandardAppVersionHandlerStaticFiles(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_readable: Optional[_builtins.bool] = ..., expiration: Optional[_builtins.str] = ..., http_headers: Optional[Mapping[str, _builtins.str]] = ..., mime_type: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ..., require_matching_file: Optional[_builtins.bool] = ..., upload_path_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationReadable")
    def application_readable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireMatchingFile")
    def require_matching_file(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadPathRegex")
    def upload_path_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionLibrary(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StandardAppVersionManualScaling(dict):
    def __init__(__self__, *, instances: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class StandardAppVersionVpcAccessConnector(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, egress_setting: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressSetting")
    def egress_setting(self) -> Optional[_builtins.str]:
        
        ...
    


