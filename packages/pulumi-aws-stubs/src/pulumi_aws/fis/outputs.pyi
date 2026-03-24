

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExperimentTemplateAction', 'ExperimentTemplateActionParameter', 'ExperimentTemplateActionTarget', 'ExperimentTemplateExperimentOptions', 'ExperimentTemplateExperimentReportConfiguration', ..., ..., ..., ..., 'ExperimentTemplateLogConfiguration', ..., 'ExperimentTemplateLogConfigurationS3Configuration', 'ExperimentTemplateStopCondition', 'ExperimentTemplateTarget', 'ExperimentTemplateTargetFilter', 'ExperimentTemplateTargetResourceTag']
@pulumi.output_type
class ExperimentTemplateAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_id: _builtins.str, name: _builtins.str, description: Optional[_builtins.str] = ..., parameters: Optional[Sequence[outputs.ExperimentTemplateActionParameter]] = ..., start_afters: Optional[Sequence[_builtins.str]] = ..., target: Optional[outputs.ExperimentTemplateActionTarget] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.ExperimentTemplateActionParameter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAfters")
    def start_afters(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.ExperimentTemplateActionTarget]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateActionParameter(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateActionTarget(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateExperimentOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_targeting: Optional[_builtins.str] = ..., empty_target_resolution_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountTargeting")
    def account_targeting(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emptyTargetResolutionMode")
    def empty_target_resolution_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateExperimentReportConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_sources: Optional[outputs.ExperimentTemplateExperimentReportConfigurationDataSources] = ..., outputs: Optional[outputs.ExperimentTemplateExperimentReportConfigurationOutputs] = ..., post_experiment_duration: Optional[_builtins.str] = ..., pre_experiment_duration: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Optional[outputs.ExperimentTemplateExperimentReportConfigurationDataSources]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> Optional[outputs.ExperimentTemplateExperimentReportConfigurationOutputs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postExperimentDuration")
    def post_experiment_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preExperimentDuration")
    def pre_experiment_duration(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateExperimentReportConfigurationDataSources(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_dashboards: Optional[Sequence[outputs.ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboard]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchDashboards")
    def cloudwatch_dashboards(self) -> Optional[Sequence[outputs.ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboard]]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dashboard_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dashboardArn")
    def dashboard_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateExperimentReportConfigurationOutputs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, s3_configuration: Optional[outputs.ExperimentTemplateExperimentReportConfigurationOutputsS3Configuration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> Optional[outputs.ExperimentTemplateExperimentReportConfigurationOutputsS3Configuration]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateExperimentReportConfigurationOutputsS3Configuration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateLogConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_schema_version: _builtins.int, cloudwatch_logs_configuration: Optional[outputs.ExperimentTemplateLogConfigurationCloudwatchLogsConfiguration] = ..., s3_configuration: Optional[outputs.ExperimentTemplateLogConfigurationS3Configuration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logSchemaVersion")
    def log_schema_version(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsConfiguration")
    def cloudwatch_logs_configuration(self) -> Optional[outputs.ExperimentTemplateLogConfigurationCloudwatchLogsConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> Optional[outputs.ExperimentTemplateLogConfigurationS3Configuration]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateLogConfigurationCloudwatchLogsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateLogConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateStopCondition(dict):
    def __init__(__self__, *, source: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, resource_type: _builtins.str, selection_mode: _builtins.str, filters: Optional[Sequence[outputs.ExperimentTemplateTargetFilter]] = ..., parameters: Optional[Mapping[str, _builtins.str]] = ..., resource_arns: Optional[Sequence[_builtins.str]] = ..., resource_tags: Optional[Sequence[outputs.ExperimentTemplateTargetResourceTag]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectionMode")
    def selection_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.ExperimentTemplateTargetFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArns")
    def resource_arns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[Sequence[outputs.ExperimentTemplateTargetResourceTag]]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateTargetFilter(dict):
    def __init__(__self__, *, path: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExperimentTemplateTargetResourceTag(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


