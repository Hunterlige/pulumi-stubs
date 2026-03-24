

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationAutoStartConfiguration', 'ApplicationAutoStopConfiguration', 'ApplicationImageConfiguration', 'ApplicationInitialCapacity', 'ApplicationInitialCapacityInitialCapacityConfig', ..., 'ApplicationInteractiveConfiguration', 'ApplicationJobLevelCostAllocationConfiguration', 'ApplicationMaximumCapacity', 'ApplicationMonitoringConfiguration', ..., ..., ..., ..., ..., 'ApplicationNetworkConfiguration', 'ApplicationRuntimeConfiguration', 'ApplicationSchedulerConfiguration']
@pulumi.output_type
class ApplicationAutoStartConfiguration(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ApplicationAutoStopConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., idle_timeout_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutMinutes")
    def idle_timeout_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ApplicationImageConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApplicationInitialCapacity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, initial_capacity_type: _builtins.str, initial_capacity_config: Optional[outputs.ApplicationInitialCapacityInitialCapacityConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialCapacityType")
    def initial_capacity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialCapacityConfig")
    def initial_capacity_config(self) -> Optional[outputs.ApplicationInitialCapacityInitialCapacityConfig]:
        
        ...
    


@pulumi.output_type
class ApplicationInitialCapacityInitialCapacityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, worker_count: _builtins.int, worker_configuration: Optional[outputs.ApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(self) -> Optional[outputs.ApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration]:
        
        ...
    


@pulumi.output_type
class ApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration(dict):
    def __init__(__self__, *, cpu: _builtins.str, memory: _builtins.str, disk: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disk(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationInteractiveConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, livy_endpoint_enabled: Optional[_builtins.bool] = ..., studio_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="livyEndpointEnabled")
    def livy_endpoint_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioEnabled")
    def studio_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ApplicationJobLevelCostAllocationConfiguration(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class ApplicationMaximumCapacity(dict):
    def __init__(__self__, *, cpu: _builtins.str, memory: _builtins.str, disk: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disk(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationMonitoringConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_logging_configuration: Optional[outputs.ApplicationMonitoringConfigurationCloudwatchLoggingConfiguration] = ..., managed_persistence_monitoring_configuration: Optional[outputs.ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfiguration] = ..., prometheus_monitoring_configuration: Optional[outputs.ApplicationMonitoringConfigurationPrometheusMonitoringConfiguration] = ..., s3_monitoring_configuration: Optional[outputs.ApplicationMonitoringConfigurationS3MonitoringConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingConfiguration")
    def cloudwatch_logging_configuration(self) -> Optional[outputs.ApplicationMonitoringConfigurationCloudwatchLoggingConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPersistenceMonitoringConfiguration")
    def managed_persistence_monitoring_configuration(self) -> Optional[outputs.ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prometheusMonitoringConfiguration")
    def prometheus_monitoring_configuration(self) -> Optional[outputs.ApplicationMonitoringConfigurationPrometheusMonitoringConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3MonitoringConfiguration")
    def s3_monitoring_configuration(self) -> Optional[outputs.ApplicationMonitoringConfigurationS3MonitoringConfiguration]:
        
        ...
    


@pulumi.output_type
class ApplicationMonitoringConfigurationCloudwatchLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, encryption_key_arn: Optional[_builtins.str] = ..., log_group_name: Optional[_builtins.str] = ..., log_stream_name_prefix: Optional[_builtins.str] = ..., log_types: Optional[Sequence[outputs.ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamNamePrefix")
    def log_stream_name_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logTypes")
    def log_types(self) -> Optional[Sequence[outputs.ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogType]]:
        
        ...
    


@pulumi.output_type
class ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogType(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., encryption_key_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationMonitoringConfigurationPrometheusMonitoringConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, remote_write_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteWriteUrl")
    def remote_write_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationMonitoringConfigurationS3MonitoringConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encryption_key_arn: Optional[_builtins.str] = ..., log_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logUri")
    def log_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, security_group_ids: Optional[Sequence[_builtins.str]] = ..., subnet_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ApplicationRuntimeConfiguration(dict):
    def __init__(__self__, *, classification: _builtins.str, properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ApplicationSchedulerConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_concurrent_runs: Optional[_builtins.int] = ..., queue_timeout_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueTimeoutMinutes")
    def queue_timeout_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


