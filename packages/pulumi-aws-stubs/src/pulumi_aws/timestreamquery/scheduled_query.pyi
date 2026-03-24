

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ScheduledQueryArgs', 'ScheduledQuery']
@pulumi.input_type
class ScheduledQueryArgs:
    def __init__(__self__, *, error_report_configuration: pulumi.Input[ScheduledQueryErrorReportConfigurationArgs], execution_role_arn: pulumi.Input[_builtins.str], notification_configuration: pulumi.Input[ScheduledQueryNotificationConfigurationArgs], query_string: pulumi.Input[_builtins.str], schedule_configuration: pulumi.Input[ScheduledQueryScheduleConfigurationArgs], target_configuration: pulumi.Input[ScheduledQueryTargetConfigurationArgs], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., last_run_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryLastRunSummaryArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., recently_failed_runs: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[ScheduledQueryTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorReportConfiguration")
    def error_report_configuration(self) -> pulumi.Input[ScheduledQueryErrorReportConfigurationArgs]:
        
        ...
    
    @error_report_configuration.setter
    def error_report_configuration(self, value: pulumi.Input[ScheduledQueryErrorReportConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(self) -> pulumi.Input[ScheduledQueryNotificationConfigurationArgs]:
        
        ...
    
    @notification_configuration.setter
    def notification_configuration(self, value: pulumi.Input[ScheduledQueryNotificationConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query_string.setter
    def query_string(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleConfiguration")
    def schedule_configuration(self) -> pulumi.Input[ScheduledQueryScheduleConfigurationArgs]:
        
        ...
    
    @schedule_configuration.setter
    def schedule_configuration(self, value: pulumi.Input[ScheduledQueryScheduleConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConfiguration")
    def target_configuration(self) -> pulumi.Input[ScheduledQueryTargetConfigurationArgs]:
        
        ...
    
    @target_configuration.setter
    def target_configuration(self, value: pulumi.Input[ScheduledQueryTargetConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRunSummaries")
    def last_run_summaries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryLastRunSummaryArgs]]]]:
        
        ...
    
    @last_run_summaries.setter
    def last_run_summaries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryLastRunSummaryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recentlyFailedRuns")
    def recently_failed_runs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunArgs]]]]:
        
        ...
    
    @recently_failed_runs.setter
    def recently_failed_runs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ScheduledQueryTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ScheduledQueryTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ScheduledQueryState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., error_report_configuration: Optional[pulumi.Input[ScheduledQueryErrorReportConfigurationArgs]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., last_run_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryLastRunSummaryArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., next_invocation_time: Optional[pulumi.Input[_builtins.str]] = ..., notification_configuration: Optional[pulumi.Input[ScheduledQueryNotificationConfigurationArgs]] = ..., previous_invocation_time: Optional[pulumi.Input[_builtins.str]] = ..., query_string: Optional[pulumi.Input[_builtins.str]] = ..., recently_failed_runs: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule_configuration: Optional[pulumi.Input[ScheduledQueryScheduleConfigurationArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_configuration: Optional[pulumi.Input[ScheduledQueryTargetConfigurationArgs]] = ..., timeouts: Optional[pulumi.Input[ScheduledQueryTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorReportConfiguration")
    def error_report_configuration(self) -> Optional[pulumi.Input[ScheduledQueryErrorReportConfigurationArgs]]:
        
        ...
    
    @error_report_configuration.setter
    def error_report_configuration(self, value: Optional[pulumi.Input[ScheduledQueryErrorReportConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRunSummaries")
    def last_run_summaries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryLastRunSummaryArgs]]]]:
        
        ...
    
    @last_run_summaries.setter
    def last_run_summaries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryLastRunSummaryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextInvocationTime")
    def next_invocation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @next_invocation_time.setter
    def next_invocation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(self) -> Optional[pulumi.Input[ScheduledQueryNotificationConfigurationArgs]]:
        
        ...
    
    @notification_configuration.setter
    def notification_configuration(self, value: Optional[pulumi.Input[ScheduledQueryNotificationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="previousInvocationTime")
    def previous_invocation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @previous_invocation_time.setter
    def previous_invocation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_string.setter
    def query_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recentlyFailedRuns")
    def recently_failed_runs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunArgs]]]]:
        
        ...
    
    @recently_failed_runs.setter
    def recently_failed_runs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleConfiguration")
    def schedule_configuration(self) -> Optional[pulumi.Input[ScheduledQueryScheduleConfigurationArgs]]:
        
        ...
    
    @schedule_configuration.setter
    def schedule_configuration(self, value: Optional[pulumi.Input[ScheduledQueryScheduleConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConfiguration")
    def target_configuration(self) -> Optional[pulumi.Input[ScheduledQueryTargetConfigurationArgs]]:
        
        ...
    
    @target_configuration.setter
    def target_configuration(self, value: Optional[pulumi.Input[ScheduledQueryTargetConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ScheduledQueryTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ScheduledQueryTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:timestreamquery/scheduledQuery:ScheduledQuery")
class ScheduledQuery(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., error_report_configuration: Optional[pulumi.Input[Union[ScheduledQueryErrorReportConfigurationArgs, ScheduledQueryErrorReportConfigurationArgsDict]]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., last_run_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ScheduledQueryLastRunSummaryArgs, ScheduledQueryLastRunSummaryArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_configuration: Optional[pulumi.Input[Union[ScheduledQueryNotificationConfigurationArgs, ScheduledQueryNotificationConfigurationArgsDict]]] = ..., query_string: Optional[pulumi.Input[_builtins.str]] = ..., recently_failed_runs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ScheduledQueryRecentlyFailedRunArgs, ScheduledQueryRecentlyFailedRunArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule_configuration: Optional[pulumi.Input[Union[ScheduledQueryScheduleConfigurationArgs, ScheduledQueryScheduleConfigurationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_configuration: Optional[pulumi.Input[Union[ScheduledQueryTargetConfigurationArgs, ScheduledQueryTargetConfigurationArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[ScheduledQueryTimeoutsArgs, ScheduledQueryTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScheduledQueryArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., error_report_configuration: Optional[pulumi.Input[Union[ScheduledQueryErrorReportConfigurationArgs, ScheduledQueryErrorReportConfigurationArgsDict]]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., last_run_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ScheduledQueryLastRunSummaryArgs, ScheduledQueryLastRunSummaryArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., next_invocation_time: Optional[pulumi.Input[_builtins.str]] = ..., notification_configuration: Optional[pulumi.Input[Union[ScheduledQueryNotificationConfigurationArgs, ScheduledQueryNotificationConfigurationArgsDict]]] = ..., previous_invocation_time: Optional[pulumi.Input[_builtins.str]] = ..., query_string: Optional[pulumi.Input[_builtins.str]] = ..., recently_failed_runs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ScheduledQueryRecentlyFailedRunArgs, ScheduledQueryRecentlyFailedRunArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule_configuration: Optional[pulumi.Input[Union[ScheduledQueryScheduleConfigurationArgs, ScheduledQueryScheduleConfigurationArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_configuration: Optional[pulumi.Input[Union[ScheduledQueryTargetConfigurationArgs, ScheduledQueryTargetConfigurationArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[ScheduledQueryTimeoutsArgs, ScheduledQueryTimeoutsArgsDict]]] = ...) -> ScheduledQuery:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorReportConfiguration")
    def error_report_configuration(self) -> pulumi.Output[outputs.ScheduledQueryErrorReportConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRunSummaries")
    def last_run_summaries(self) -> pulumi.Output[Optional[Sequence[outputs.ScheduledQueryLastRunSummary]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextInvocationTime")
    def next_invocation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(self) -> pulumi.Output[outputs.ScheduledQueryNotificationConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="previousInvocationTime")
    def previous_invocation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recentlyFailedRuns")
    def recently_failed_runs(self) -> pulumi.Output[Optional[Sequence[outputs.ScheduledQueryRecentlyFailedRun]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleConfiguration")
    def schedule_configuration(self) -> pulumi.Output[outputs.ScheduledQueryScheduleConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConfiguration")
    def target_configuration(self) -> pulumi.Output[outputs.ScheduledQueryTargetConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ScheduledQueryTimeouts]]:
        ...
    


