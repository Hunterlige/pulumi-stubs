

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
__all__ = ['WorkflowArgs', 'Workflow']
@pulumi.input_type
class WorkflowArgs:
    def __init__(__self__, *, steps: pulumi.Input[Sequence[pulumi.Input[WorkflowStepArgs]]], description: Optional[pulumi.Input[_builtins.str]] = ..., on_exception_steps: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowOnExceptionStepArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def steps(self) -> pulumi.Input[Sequence[pulumi.Input[WorkflowStepArgs]]]:
        
        ...
    
    @steps.setter
    def steps(self, value: pulumi.Input[Sequence[pulumi.Input[WorkflowStepArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onExceptionSteps")
    def on_exception_steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowOnExceptionStepArgs]]]]:
        
        ...
    
    @on_exception_steps.setter
    def on_exception_steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowOnExceptionStepArgs]]]]): # -> None:
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
    


@pulumi.input_type
class _WorkflowState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., on_exception_steps: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowOnExceptionStepArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., steps: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowStepArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onExceptionSteps")
    def on_exception_steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowOnExceptionStepArgs]]]]:
        
        ...
    
    @on_exception_steps.setter
    def on_exception_steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowOnExceptionStepArgs]]]]): # -> None:
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
    def steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowStepArgs]]]]:
        
        ...
    
    @steps.setter
    def steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowStepArgs]]]]): # -> None:
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
    


@pulumi.type_token("aws:transfer/workflow:Workflow")
class Workflow(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., on_exception_steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkflowOnExceptionStepArgs, WorkflowOnExceptionStepArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkflowStepArgs, WorkflowStepArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkflowArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., on_exception_steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkflowOnExceptionStepArgs, WorkflowOnExceptionStepArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkflowStepArgs, WorkflowStepArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Workflow:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onExceptionSteps")
    def on_exception_steps(self) -> pulumi.Output[Optional[Sequence[outputs.WorkflowOnExceptionStep]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def steps(self) -> pulumi.Output[Sequence[outputs.WorkflowStep]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


