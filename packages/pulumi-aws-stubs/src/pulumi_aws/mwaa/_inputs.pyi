

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EnvironmentLastUpdatedArgs', 'EnvironmentLastUpdatedArgsDict', 'EnvironmentLastUpdatedErrorArgs', 'EnvironmentLastUpdatedErrorArgsDict', 'EnvironmentLoggingConfigurationArgs', 'EnvironmentLoggingConfigurationArgsDict', ..., ..., 'EnvironmentLoggingConfigurationSchedulerLogsArgs', ..., 'EnvironmentLoggingConfigurationTaskLogsArgs', 'EnvironmentLoggingConfigurationTaskLogsArgsDict', 'EnvironmentLoggingConfigurationWebserverLogsArgs', ..., 'EnvironmentLoggingConfigurationWorkerLogsArgs', 'EnvironmentLoggingConfigurationWorkerLogsArgsDict', 'EnvironmentNetworkConfigurationArgs', 'EnvironmentNetworkConfigurationArgsDict']
class EnvironmentLastUpdatedArgsDict(TypedDict):
    created_at: NotRequired[pulumi.Input[_builtins.str]]
    errors: NotRequired[pulumi.Input[Sequence[pulumi.Input[EnvironmentLastUpdatedErrorArgsDict]]]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentLastUpdatedArgs:
    def __init__(__self__, *, created_at: Optional[pulumi.Input[_builtins.str]] = ..., errors: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentLastUpdatedErrorArgs]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentLastUpdatedErrorArgs]]]]:
        ...
    
    @errors.setter
    def errors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentLastUpdatedErrorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentLastUpdatedErrorArgsDict(TypedDict):
    error_code: NotRequired[pulumi.Input[_builtins.str]]
    error_message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentLastUpdatedErrorArgs:
    def __init__(__self__, *, error_code: Optional[pulumi.Input[_builtins.str]] = ..., error_message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @error_code.setter
    def error_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentLoggingConfigurationArgsDict(TypedDict):
    dag_processing_logs: NotRequired[pulumi.Input[EnvironmentLoggingConfigurationDagProcessingLogsArgsDict]]
    scheduler_logs: NotRequired[pulumi.Input[EnvironmentLoggingConfigurationSchedulerLogsArgsDict]]
    task_logs: NotRequired[pulumi.Input[EnvironmentLoggingConfigurationTaskLogsArgsDict]]
    webserver_logs: NotRequired[pulumi.Input[EnvironmentLoggingConfigurationWebserverLogsArgsDict]]
    worker_logs: NotRequired[pulumi.Input[EnvironmentLoggingConfigurationWorkerLogsArgsDict]]


@pulumi.input_type
class EnvironmentLoggingConfigurationArgs:
    def __init__(__self__, *, dag_processing_logs: Optional[pulumi.Input[EnvironmentLoggingConfigurationDagProcessingLogsArgs]] = ..., scheduler_logs: Optional[pulumi.Input[EnvironmentLoggingConfigurationSchedulerLogsArgs]] = ..., task_logs: Optional[pulumi.Input[EnvironmentLoggingConfigurationTaskLogsArgs]] = ..., webserver_logs: Optional[pulumi.Input[EnvironmentLoggingConfigurationWebserverLogsArgs]] = ..., worker_logs: Optional[pulumi.Input[EnvironmentLoggingConfigurationWorkerLogsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagProcessingLogs")
    def dag_processing_logs(self) -> Optional[pulumi.Input[EnvironmentLoggingConfigurationDagProcessingLogsArgs]]:
        
        ...
    
    @dag_processing_logs.setter
    def dag_processing_logs(self, value: Optional[pulumi.Input[EnvironmentLoggingConfigurationDagProcessingLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulerLogs")
    def scheduler_logs(self) -> Optional[pulumi.Input[EnvironmentLoggingConfigurationSchedulerLogsArgs]]:
        
        ...
    
    @scheduler_logs.setter
    def scheduler_logs(self, value: Optional[pulumi.Input[EnvironmentLoggingConfigurationSchedulerLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskLogs")
    def task_logs(self) -> Optional[pulumi.Input[EnvironmentLoggingConfigurationTaskLogsArgs]]:
        
        ...
    
    @task_logs.setter
    def task_logs(self, value: Optional[pulumi.Input[EnvironmentLoggingConfigurationTaskLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webserverLogs")
    def webserver_logs(self) -> Optional[pulumi.Input[EnvironmentLoggingConfigurationWebserverLogsArgs]]:
        
        ...
    
    @webserver_logs.setter
    def webserver_logs(self, value: Optional[pulumi.Input[EnvironmentLoggingConfigurationWebserverLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerLogs")
    def worker_logs(self) -> Optional[pulumi.Input[EnvironmentLoggingConfigurationWorkerLogsArgs]]:
        
        ...
    
    @worker_logs.setter
    def worker_logs(self, value: Optional[pulumi.Input[EnvironmentLoggingConfigurationWorkerLogsArgs]]): # -> None:
        ...
    


class EnvironmentLoggingConfigurationDagProcessingLogsArgsDict(TypedDict):
    cloud_watch_log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentLoggingConfigurationDagProcessingLogsArgs:
    def __init__(__self__, *, cloud_watch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_watch_log_group_arn.setter
    def cloud_watch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentLoggingConfigurationSchedulerLogsArgsDict(TypedDict):
    cloud_watch_log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentLoggingConfigurationSchedulerLogsArgs:
    def __init__(__self__, *, cloud_watch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_watch_log_group_arn.setter
    def cloud_watch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentLoggingConfigurationTaskLogsArgsDict(TypedDict):
    cloud_watch_log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentLoggingConfigurationTaskLogsArgs:
    def __init__(__self__, *, cloud_watch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_watch_log_group_arn.setter
    def cloud_watch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentLoggingConfigurationWebserverLogsArgsDict(TypedDict):
    cloud_watch_log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentLoggingConfigurationWebserverLogsArgs:
    def __init__(__self__, *, cloud_watch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_watch_log_group_arn.setter
    def cloud_watch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentLoggingConfigurationWorkerLogsArgsDict(TypedDict):
    cloud_watch_log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentLoggingConfigurationWorkerLogsArgs:
    def __init__(__self__, *, cloud_watch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_watch_log_group_arn.setter
    def cloud_watch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentNetworkConfigurationArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class EnvironmentNetworkConfigurationArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


