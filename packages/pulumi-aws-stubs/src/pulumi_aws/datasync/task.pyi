

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TaskArgs', 'Task']
@pulumi.input_type
class TaskArgs:
    def __init__(__self__, *, destination_location_arn: pulumi.Input[_builtins.str], source_location_arn: pulumi.Input[_builtins.str], cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., excludes: Optional[pulumi.Input[TaskExcludesArgs]] = ..., includes: Optional[pulumi.Input[TaskIncludesArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[TaskOptionsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[TaskScheduleArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_mode: Optional[pulumi.Input[_builtins.str]] = ..., task_report_config: Optional[pulumi.Input[TaskTaskReportConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationLocationArn")
    def destination_location_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_location_arn.setter
    def destination_location_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocationArn")
    def source_location_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_location_arn.setter
    def source_location_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[pulumi.Input[TaskExcludesArgs]]:
        
        ...
    
    @excludes.setter
    def excludes(self, value: Optional[pulumi.Input[TaskExcludesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[pulumi.Input[TaskIncludesArgs]]:
        
        ...
    
    @includes.setter
    def includes(self, value: Optional[pulumi.Input[TaskIncludesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[TaskOptionsArgs]]:
        
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[TaskOptionsArgs]]): # -> None:
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
    def schedule(self) -> Optional[pulumi.Input[TaskScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[TaskScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskMode")
    def task_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_mode.setter
    def task_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskReportConfig")
    def task_report_config(self) -> Optional[pulumi.Input[TaskTaskReportConfigArgs]]:
        
        ...
    
    @task_report_config.setter
    def task_report_config(self, value: Optional[pulumi.Input[TaskTaskReportConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TaskState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_location_arn: Optional[pulumi.Input[_builtins.str]] = ..., excludes: Optional[pulumi.Input[TaskExcludesArgs]] = ..., includes: Optional[pulumi.Input[TaskIncludesArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[TaskOptionsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[TaskScheduleArgs]] = ..., source_location_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_mode: Optional[pulumi.Input[_builtins.str]] = ..., task_report_config: Optional[pulumi.Input[TaskTaskReportConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationLocationArn")
    def destination_location_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_location_arn.setter
    def destination_location_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[pulumi.Input[TaskExcludesArgs]]:
        
        ...
    
    @excludes.setter
    def excludes(self, value: Optional[pulumi.Input[TaskExcludesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[pulumi.Input[TaskIncludesArgs]]:
        
        ...
    
    @includes.setter
    def includes(self, value: Optional[pulumi.Input[TaskIncludesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[TaskOptionsArgs]]:
        
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[TaskOptionsArgs]]): # -> None:
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
    def schedule(self) -> Optional[pulumi.Input[TaskScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[TaskScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocationArn")
    def source_location_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_location_arn.setter
    def source_location_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="taskMode")
    def task_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_mode.setter
    def task_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskReportConfig")
    def task_report_config(self) -> Optional[pulumi.Input[TaskTaskReportConfigArgs]]:
        
        ...
    
    @task_report_config.setter
    def task_report_config(self, value: Optional[pulumi.Input[TaskTaskReportConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:datasync/task:Task")
class Task(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_location_arn: Optional[pulumi.Input[_builtins.str]] = ..., excludes: Optional[pulumi.Input[Union[TaskExcludesArgs, TaskExcludesArgsDict]]] = ..., includes: Optional[pulumi.Input[Union[TaskIncludesArgs, TaskIncludesArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Union[TaskOptionsArgs, TaskOptionsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[Union[TaskScheduleArgs, TaskScheduleArgsDict]]] = ..., source_location_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_mode: Optional[pulumi.Input[_builtins.str]] = ..., task_report_config: Optional[pulumi.Input[Union[TaskTaskReportConfigArgs, TaskTaskReportConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TaskArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_location_arn: Optional[pulumi.Input[_builtins.str]] = ..., excludes: Optional[pulumi.Input[Union[TaskExcludesArgs, TaskExcludesArgsDict]]] = ..., includes: Optional[pulumi.Input[Union[TaskIncludesArgs, TaskIncludesArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Union[TaskOptionsArgs, TaskOptionsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[Union[TaskScheduleArgs, TaskScheduleArgsDict]]] = ..., source_location_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_mode: Optional[pulumi.Input[_builtins.str]] = ..., task_report_config: Optional[pulumi.Input[Union[TaskTaskReportConfigArgs, TaskTaskReportConfigArgsDict]]] = ...) -> Task:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationLocationArn")
    def destination_location_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> pulumi.Output[Optional[outputs.TaskExcludes]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def includes(self) -> pulumi.Output[Optional[outputs.TaskIncludes]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Output[Optional[outputs.TaskOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[outputs.TaskSchedule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocationArn")
    def source_location_arn(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="taskMode")
    def task_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskReportConfig")
    def task_report_config(self) -> pulumi.Output[Optional[outputs.TaskTaskReportConfig]]:
        
        ...
    


