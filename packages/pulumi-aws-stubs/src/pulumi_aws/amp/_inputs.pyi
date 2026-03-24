

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['QueryLoggingConfigurationDestinationArgs', 'QueryLoggingConfigurationDestinationArgsDict', ..., ..., 'QueryLoggingConfigurationDestinationFiltersArgs', ..., 'QueryLoggingConfigurationTimeoutsArgs', 'QueryLoggingConfigurationTimeoutsArgsDict', 'ResourcePolicyTimeoutsArgs', 'ResourcePolicyTimeoutsArgsDict', 'ScraperDestinationArgs', 'ScraperDestinationArgsDict', 'ScraperDestinationAmpArgs', 'ScraperDestinationAmpArgsDict', 'ScraperRoleConfigurationArgs', 'ScraperRoleConfigurationArgsDict', 'ScraperSourceArgs', 'ScraperSourceArgsDict', 'ScraperSourceEksArgs', 'ScraperSourceEksArgsDict', 'ScraperTimeoutsArgs', 'ScraperTimeoutsArgsDict', 'WorkspaceConfigurationLimitsPerLabelSetArgs', 'WorkspaceConfigurationLimitsPerLabelSetArgsDict', 'WorkspaceConfigurationLimitsPerLabelSetLimitsArgs', ..., 'WorkspaceConfigurationTimeoutsArgs', 'WorkspaceConfigurationTimeoutsArgsDict', 'WorkspaceLoggingConfigurationArgs', 'WorkspaceLoggingConfigurationArgsDict']
class QueryLoggingConfigurationDestinationArgsDict(TypedDict):
    cloudwatch_logs: pulumi.Input[QueryLoggingConfigurationDestinationCloudwatchLogsArgsDict]
    filters: pulumi.Input[QueryLoggingConfigurationDestinationFiltersArgsDict]


@pulumi.input_type
class QueryLoggingConfigurationDestinationArgs:
    def __init__(__self__, *, cloudwatch_logs: pulumi.Input[QueryLoggingConfigurationDestinationCloudwatchLogsArgs], filters: pulumi.Input[QueryLoggingConfigurationDestinationFiltersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> pulumi.Input[QueryLoggingConfigurationDestinationCloudwatchLogsArgs]:
        
        ...
    
    @cloudwatch_logs.setter
    def cloudwatch_logs(self, value: pulumi.Input[QueryLoggingConfigurationDestinationCloudwatchLogsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Input[QueryLoggingConfigurationDestinationFiltersArgs]:
        
        ...
    
    @filters.setter
    def filters(self, value: pulumi.Input[QueryLoggingConfigurationDestinationFiltersArgs]): # -> None:
        ...
    


class QueryLoggingConfigurationDestinationCloudwatchLogsArgsDict(TypedDict):
    log_group_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class QueryLoggingConfigurationDestinationCloudwatchLogsArgs:
    def __init__(__self__, *, log_group_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_group_arn.setter
    def log_group_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class QueryLoggingConfigurationDestinationFiltersArgsDict(TypedDict):
    qsp_threshold: pulumi.Input[_builtins.int]


@pulumi.input_type
class QueryLoggingConfigurationDestinationFiltersArgs:
    def __init__(__self__, *, qsp_threshold: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qspThreshold")
    def qsp_threshold(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @qsp_threshold.setter
    def qsp_threshold(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class QueryLoggingConfigurationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class QueryLoggingConfigurationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourcePolicyTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourcePolicyTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScraperDestinationArgsDict(TypedDict):
    amp: NotRequired[pulumi.Input[ScraperDestinationAmpArgsDict]]


@pulumi.input_type
class ScraperDestinationArgs:
    def __init__(__self__, *, amp: Optional[pulumi.Input[ScraperDestinationAmpArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amp(self) -> Optional[pulumi.Input[ScraperDestinationAmpArgs]]:
        
        ...
    
    @amp.setter
    def amp(self, value: Optional[pulumi.Input[ScraperDestinationAmpArgs]]): # -> None:
        ...
    


class ScraperDestinationAmpArgsDict(TypedDict):
    workspace_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ScraperDestinationAmpArgs:
    def __init__(__self__, *, workspace_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceArn")
    def workspace_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_arn.setter
    def workspace_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ScraperRoleConfigurationArgsDict(TypedDict):
    source_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    target_role_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScraperRoleConfigurationArgs:
    def __init__(__self__, *, source_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., target_role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRoleArn")
    def source_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_role_arn.setter
    def source_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRoleArn")
    def target_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_role_arn.setter
    def target_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScraperSourceArgsDict(TypedDict):
    eks: pulumi.Input[ScraperSourceEksArgsDict]


@pulumi.input_type
class ScraperSourceArgs:
    def __init__(__self__, *, eks: pulumi.Input[ScraperSourceEksArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eks(self) -> pulumi.Input[ScraperSourceEksArgs]:
        
        ...
    
    @eks.setter
    def eks(self, value: pulumi.Input[ScraperSourceEksArgs]): # -> None:
        ...
    


class ScraperSourceEksArgsDict(TypedDict):
    cluster_arn: pulumi.Input[_builtins.str]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ScraperSourceEksArgs:
    def __init__(__self__, *, cluster_arn: pulumi.Input[_builtins.str], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @cluster_arn.setter
    def cluster_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ScraperTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScraperTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkspaceConfigurationLimitsPerLabelSetArgsDict(TypedDict):
    label_set: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    limits: pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetLimitsArgsDict]


@pulumi.input_type
class WorkspaceConfigurationLimitsPerLabelSetArgs:
    def __init__(__self__, *, label_set: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], limits: pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetLimitsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelSet")
    def label_set(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @label_set.setter
    def label_set(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetLimitsArgs]:
        
        ...
    
    @limits.setter
    def limits(self, value: pulumi.Input[WorkspaceConfigurationLimitsPerLabelSetLimitsArgs]): # -> None:
        ...
    


class WorkspaceConfigurationLimitsPerLabelSetLimitsArgsDict(TypedDict):
    max_series: pulumi.Input[_builtins.int]


@pulumi.input_type
class WorkspaceConfigurationLimitsPerLabelSetLimitsArgs:
    def __init__(__self__, *, max_series: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSeries")
    def max_series(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_series.setter
    def max_series(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class WorkspaceConfigurationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkspaceConfigurationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkspaceLoggingConfigurationArgsDict(TypedDict):
    log_group_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkspaceLoggingConfigurationArgs:
    def __init__(__self__, *, log_group_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_group_arn.setter
    def log_group_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


