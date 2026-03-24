import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "QueryLoggingConfigurationDestination",
    "QueryLoggingConfigurationDestinationCloudwatchLogs",
    "QueryLoggingConfigurationDestinationFilters",
    "QueryLoggingConfigurationTimeouts",
    "ResourcePolicyTimeouts",
    "ScraperDestination",
    "ScraperDestinationAmp",
    "ScraperRoleConfiguration",
    "ScraperSource",
    "ScraperSourceEks",
    "ScraperTimeouts",
    "WorkspaceConfigurationLimitsPerLabelSet",
    "WorkspaceConfigurationLimitsPerLabelSetLimits",
    "WorkspaceConfigurationTimeouts",
    "WorkspaceLoggingConfiguration",
]

@pulumi.output_type
class QueryLoggingConfigurationDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_logs: outputs.QueryLoggingConfigurationDestinationCloudwatchLogs,
        filters: outputs.QueryLoggingConfigurationDestinationFilters,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> outputs.QueryLoggingConfigurationDestinationCloudwatchLogs: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> outputs.QueryLoggingConfigurationDestinationFilters: ...

@pulumi.output_type
class QueryLoggingConfigurationDestinationCloudwatchLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, log_group_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> _builtins.str: ...

@pulumi.output_type
class QueryLoggingConfigurationDestinationFilters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, qsp_threshold: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="qspThreshold")
    def qsp_threshold(self) -> _builtins.int: ...

@pulumi.output_type
class QueryLoggingConfigurationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourcePolicyTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScraperDestination(dict):
    def __init__(
        __self__, *, amp: Optional[outputs.ScraperDestinationAmp] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amp(self) -> Optional[outputs.ScraperDestinationAmp]: ...

@pulumi.output_type
class ScraperDestinationAmp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, workspace_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workspaceArn")
    def workspace_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ScraperRoleConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_role_arn: Optional[_builtins.str] = ...,
        target_role_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceRoleArn")
    def source_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetRoleArn")
    def target_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScraperSource(dict):
    def __init__(__self__, *, eks: outputs.ScraperSourceEks) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eks(self) -> outputs.ScraperSourceEks: ...

@pulumi.output_type
class ScraperSourceEks(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_arn: _builtins.str,
        subnet_ids: Sequence[_builtins.str],
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ScraperTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkspaceConfigurationLimitsPerLabelSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        label_set: Mapping[str, _builtins.str],
        limits: outputs.WorkspaceConfigurationLimitsPerLabelSetLimits,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labelSet")
    def label_set(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> outputs.WorkspaceConfigurationLimitsPerLabelSetLimits: ...

@pulumi.output_type
class WorkspaceConfigurationLimitsPerLabelSetLimits(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_series: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxSeries")
    def max_series(self) -> _builtins.int: ...

@pulumi.output_type
class WorkspaceConfigurationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkspaceLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, log_group_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> _builtins.str: ...
