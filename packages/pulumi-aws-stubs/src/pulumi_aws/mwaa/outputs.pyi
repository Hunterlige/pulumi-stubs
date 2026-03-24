import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EnvironmentLastUpdated",
    "EnvironmentLastUpdatedError",
    "EnvironmentLoggingConfiguration",
    "EnvironmentLoggingConfigurationDagProcessingLogs",
    "EnvironmentLoggingConfigurationSchedulerLogs",
    "EnvironmentLoggingConfigurationTaskLogs",
    "EnvironmentLoggingConfigurationWebserverLogs",
    "EnvironmentLoggingConfigurationWorkerLogs",
    "EnvironmentNetworkConfiguration",
]

@pulumi.output_type
class EnvironmentLastUpdated(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        errors: Optional[Sequence[outputs.EnvironmentLastUpdatedError]] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.EnvironmentLastUpdatedError]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentLastUpdatedError(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_code: Optional[_builtins.str] = ...,
        error_message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dag_processing_logs: Optional[
            outputs.EnvironmentLoggingConfigurationDagProcessingLogs
        ] = ...,
        scheduler_logs: Optional[
            outputs.EnvironmentLoggingConfigurationSchedulerLogs
        ] = ...,
        task_logs: Optional[outputs.EnvironmentLoggingConfigurationTaskLogs] = ...,
        webserver_logs: Optional[
            outputs.EnvironmentLoggingConfigurationWebserverLogs
        ] = ...,
        worker_logs: Optional[outputs.EnvironmentLoggingConfigurationWorkerLogs] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dagProcessingLogs")
    def dag_processing_logs(
        self,
    ) -> Optional[outputs.EnvironmentLoggingConfigurationDagProcessingLogs]: ...
    @_builtins.property
    @pulumi.getter(name="schedulerLogs")
    def scheduler_logs(
        self,
    ) -> Optional[outputs.EnvironmentLoggingConfigurationSchedulerLogs]: ...
    @_builtins.property
    @pulumi.getter(name="taskLogs")
    def task_logs(
        self,
    ) -> Optional[outputs.EnvironmentLoggingConfigurationTaskLogs]: ...
    @_builtins.property
    @pulumi.getter(name="webserverLogs")
    def webserver_logs(
        self,
    ) -> Optional[outputs.EnvironmentLoggingConfigurationWebserverLogs]: ...
    @_builtins.property
    @pulumi.getter(name="workerLogs")
    def worker_logs(
        self,
    ) -> Optional[outputs.EnvironmentLoggingConfigurationWorkerLogs]: ...

@pulumi.output_type
class EnvironmentLoggingConfigurationDagProcessingLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_watch_log_group_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentLoggingConfigurationSchedulerLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_watch_log_group_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentLoggingConfigurationTaskLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_watch_log_group_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentLoggingConfigurationWebserverLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_watch_log_group_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentLoggingConfigurationWorkerLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_watch_log_group_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupArn")
    def cloud_watch_log_group_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
