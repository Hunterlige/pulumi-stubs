

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
__all__ = ['TaskArgs', 'Task']
@pulumi.input_type
class TaskArgs:
    def __init__(__self__, *, execution_spec: pulumi.Input[TaskExecutionSpecArgs], trigger_spec: pulumi.Input[TaskTriggerSpecArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., notebook: Optional[pulumi.Input[TaskNotebookArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., spark: Optional[pulumi.Input[TaskSparkArgs]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionSpec")
    def execution_spec(self) -> pulumi.Input[TaskExecutionSpecArgs]:
        
        ...
    
    @execution_spec.setter
    def execution_spec(self, value: pulumi.Input[TaskExecutionSpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerSpec")
    def trigger_spec(self) -> pulumi.Input[TaskTriggerSpecArgs]:
        
        ...
    
    @trigger_spec.setter
    def trigger_spec(self, value: pulumi.Input[TaskTriggerSpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lake.setter
    def lake(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notebook(self) -> Optional[pulumi.Input[TaskNotebookArgs]]:
        
        ...
    
    @notebook.setter
    def notebook(self, value: Optional[pulumi.Input[TaskNotebookArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def spark(self) -> Optional[pulumi.Input[TaskSparkArgs]]:
        
        ...
    
    @spark.setter
    def spark(self, value: Optional[pulumi.Input[TaskSparkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_id.setter
    def task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TaskState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., execution_spec: Optional[pulumi.Input[TaskExecutionSpecArgs]] = ..., execution_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[TaskExecutionStatusArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notebook: Optional[pulumi.Input[TaskNotebookArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., spark: Optional[pulumi.Input[TaskSparkArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ..., trigger_spec: Optional[pulumi.Input[TaskTriggerSpecArgs]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionSpec")
    def execution_spec(self) -> Optional[pulumi.Input[TaskExecutionSpecArgs]]:
        
        ...
    
    @execution_spec.setter
    def execution_spec(self, value: Optional[pulumi.Input[TaskExecutionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStatuses")
    def execution_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TaskExecutionStatusArgs]]]]:
        
        ...
    
    @execution_statuses.setter
    def execution_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TaskExecutionStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lake.setter
    def lake(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def notebook(self) -> Optional[pulumi.Input[TaskNotebookArgs]]:
        
        ...
    
    @notebook.setter
    def notebook(self, value: Optional[pulumi.Input[TaskNotebookArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def spark(self) -> Optional[pulumi.Input[TaskSparkArgs]]:
        
        ...
    
    @spark.setter
    def spark(self, value: Optional[pulumi.Input[TaskSparkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_id.setter
    def task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerSpec")
    def trigger_spec(self) -> Optional[pulumi.Input[TaskTriggerSpecArgs]]:
        
        ...
    
    @trigger_spec.setter
    def trigger_spec(self, value: Optional[pulumi.Input[TaskTriggerSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dataplex/task:Task")
class Task(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., execution_spec: Optional[pulumi.Input[Union[TaskExecutionSpecArgs, TaskExecutionSpecArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., notebook: Optional[pulumi.Input[Union[TaskNotebookArgs, TaskNotebookArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., spark: Optional[pulumi.Input[Union[TaskSparkArgs, TaskSparkArgsDict]]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ..., trigger_spec: Optional[pulumi.Input[Union[TaskTriggerSpecArgs, TaskTriggerSpecArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TaskArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., execution_spec: Optional[pulumi.Input[Union[TaskExecutionSpecArgs, TaskExecutionSpecArgsDict]]] = ..., execution_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TaskExecutionStatusArgs, TaskExecutionStatusArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notebook: Optional[pulumi.Input[Union[TaskNotebookArgs, TaskNotebookArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., spark: Optional[pulumi.Input[Union[TaskSparkArgs, TaskSparkArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ..., trigger_spec: Optional[pulumi.Input[Union[TaskTriggerSpecArgs, TaskTriggerSpecArgsDict]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Task:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionSpec")
    def execution_spec(self) -> pulumi.Output[outputs.TaskExecutionSpec]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionStatuses")
    def execution_statuses(self) -> pulumi.Output[Sequence[outputs.TaskExecutionStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lake(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notebook(self) -> pulumi.Output[Optional[outputs.TaskNotebook]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spark(self) -> pulumi.Output[Optional[outputs.TaskSpark]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerSpec")
    def trigger_spec(self) -> pulumi.Output[outputs.TaskTriggerSpec]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


