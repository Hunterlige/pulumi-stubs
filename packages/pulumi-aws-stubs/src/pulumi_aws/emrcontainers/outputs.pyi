

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JobTemplateJobTemplateData', 'JobTemplateJobTemplateDataConfigurationOverrides', ..., ..., ..., ..., ..., 'JobTemplateJobTemplateDataJobDriver', ..., ..., 'VirtualClusterContainerProvider', 'VirtualClusterContainerProviderInfo', 'VirtualClusterContainerProviderInfoEksInfo', 'GetVirtualClusterContainerProviderResult', 'GetVirtualClusterContainerProviderInfoResult', ...]
@pulumi.output_type
class JobTemplateJobTemplateData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_role_arn: _builtins.str, job_driver: outputs.JobTemplateJobTemplateDataJobDriver, release_label: _builtins.str, configuration_overrides: Optional[outputs.JobTemplateJobTemplateDataConfigurationOverrides] = ..., job_tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobDriver")
    def job_driver(self) -> outputs.JobTemplateJobTemplateDataJobDriver:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationOverrides")
    def configuration_overrides(self) -> Optional[outputs.JobTemplateJobTemplateDataConfigurationOverrides]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobTags")
    def job_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataConfigurationOverrides(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_configurations: Optional[Sequence[outputs.JobTemplateJobTemplateDataConfigurationOverridesApplicationConfiguration]] = ..., monitoring_configuration: Optional[outputs.JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationConfigurations")
    def application_configurations(self) -> Optional[Sequence[outputs.JobTemplateJobTemplateDataConfigurationOverridesApplicationConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(self) -> Optional[outputs.JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfiguration]:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataConfigurationOverridesApplicationConfiguration(dict):
    def __init__(__self__, *, classification: _builtins.str, configurations: Optional[Sequence[outputs.JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfiguration]] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfiguration(dict):
    def __init__(__self__, *, classification: Optional[_builtins.str] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_watch_monitoring_configuration: Optional[outputs.JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfiguration] = ..., persistent_app_ui: Optional[_builtins.str] = ..., s3_monitoring_configuration: Optional[outputs.JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchMonitoringConfiguration")
    def cloud_watch_monitoring_configuration(self) -> Optional[outputs.JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentAppUi")
    def persistent_app_ui(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3MonitoringConfiguration")
    def s3_monitoring_configuration(self) -> Optional[outputs.JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfiguration]:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_name: _builtins.str, log_stream_name_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamNamePrefix")
    def log_stream_name_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logUri")
    def log_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataJobDriver(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, spark_sql_job_driver: Optional[outputs.JobTemplateJobTemplateDataJobDriverSparkSqlJobDriver] = ..., spark_submit_job_driver: Optional[outputs.JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriver] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkSqlJobDriver")
    def spark_sql_job_driver(self) -> Optional[outputs.JobTemplateJobTemplateDataJobDriverSparkSqlJobDriver]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkSubmitJobDriver")
    def spark_submit_job_driver(self) -> Optional[outputs.JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriver]:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataJobDriverSparkSqlJobDriver(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, entry_point: Optional[_builtins.str] = ..., spark_sql_parameters: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkSqlParameters")
    def spark_sql_parameters(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriver(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, entry_point: _builtins.str, entry_point_arguments: Optional[Sequence[_builtins.str]] = ..., spark_submit_parameters: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryPointArguments")
    def entry_point_arguments(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkSubmitParameters")
    def spark_submit_parameters(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualClusterContainerProvider(dict):
    def __init__(__self__, *, id: _builtins.str, info: outputs.VirtualClusterContainerProviderInfo, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def info(self) -> outputs.VirtualClusterContainerProviderInfo:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VirtualClusterContainerProviderInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, eks_info: outputs.VirtualClusterContainerProviderInfoEksInfo) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eksInfo")
    def eks_info(self) -> outputs.VirtualClusterContainerProviderInfoEksInfo:
        
        ...
    


@pulumi.output_type
class VirtualClusterContainerProviderInfoEksInfo(dict):
    def __init__(__self__, *, namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVirtualClusterContainerProviderResult(dict):
    def __init__(__self__, *, id: _builtins.str, infos: Sequence[outputs.GetVirtualClusterContainerProviderInfoResult], type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def infos(self) -> Sequence[outputs.GetVirtualClusterContainerProviderInfoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVirtualClusterContainerProviderInfoResult(dict):
    def __init__(__self__, *, eks_infos: Sequence[outputs.GetVirtualClusterContainerProviderInfoEksInfoResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eksInfos")
    def eks_infos(self) -> Sequence[outputs.GetVirtualClusterContainerProviderInfoEksInfoResult]:
        
        ...
    


@pulumi.output_type
class GetVirtualClusterContainerProviderInfoEksInfoResult(dict):
    def __init__(__self__, *, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


