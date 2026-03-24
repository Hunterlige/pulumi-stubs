

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkflowTemplateArgs', 'WorkflowTemplate']
@pulumi.input_type
class WorkflowTemplateArgs:
    def __init__(__self__, *, jobs: pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateJobArgs]]], location: pulumi.Input[_builtins.str], placement: pulumi.Input[WorkflowTemplatePlacementArgs], dag_timeout: Optional[pulumi.Input[_builtins.str]] = ..., encryption_config: Optional[pulumi.Input[WorkflowTemplateEncryptionConfigArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateParameterArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def jobs(self) -> pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateJobArgs]]]:
        
        ...
    
    @jobs.setter
    def jobs(self, value: pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateJobArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> pulumi.Input[WorkflowTemplatePlacementArgs]:
        
        ...
    
    @placement.setter
    def placement(self, value: pulumi.Input[WorkflowTemplatePlacementArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagTimeout")
    def dag_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dag_timeout.setter
    def dag_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[WorkflowTemplateEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[WorkflowTemplateEncryptionConfigArgs]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateParameterArgs]]]]): # -> None:
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
    @_utilities.deprecated(...)
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkflowTemplateState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., dag_timeout: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption_config: Optional[pulumi.Input[WorkflowTemplateEncryptionConfigArgs]] = ..., jobs: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateJobArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateParameterArgs]]]] = ..., placement: Optional[pulumi.Input[WorkflowTemplatePlacementArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagTimeout")
    def dag_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dag_timeout.setter
    def dag_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[WorkflowTemplateEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[WorkflowTemplateEncryptionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def jobs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateJobArgs]]]]:
        
        ...
    
    @jobs.setter
    def jobs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateJobArgs]]]]): # -> None:
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkflowTemplateParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[pulumi.Input[WorkflowTemplatePlacementArgs]]:
        
        ...
    
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[WorkflowTemplatePlacementArgs]]): # -> None:
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dataproc/workflowTemplate:WorkflowTemplate")
class WorkflowTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dag_timeout: Optional[pulumi.Input[_builtins.str]] = ..., encryption_config: Optional[pulumi.Input[Union[WorkflowTemplateEncryptionConfigArgs, WorkflowTemplateEncryptionConfigArgsDict]]] = ..., jobs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkflowTemplateJobArgs, WorkflowTemplateJobArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkflowTemplateParameterArgs, WorkflowTemplateParameterArgsDict]]]]] = ..., placement: Optional[pulumi.Input[Union[WorkflowTemplatePlacementArgs, WorkflowTemplatePlacementArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkflowTemplateArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dag_timeout: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption_config: Optional[pulumi.Input[Union[WorkflowTemplateEncryptionConfigArgs, WorkflowTemplateEncryptionConfigArgsDict]]] = ..., jobs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkflowTemplateJobArgs, WorkflowTemplateJobArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkflowTemplateParameterArgs, WorkflowTemplateParameterArgsDict]]]]] = ..., placement: Optional[pulumi.Input[Union[WorkflowTemplatePlacementArgs, WorkflowTemplatePlacementArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> WorkflowTemplate:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagTimeout")
    def dag_timeout(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output[Optional[outputs.WorkflowTemplateEncryptionConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def jobs(self) -> pulumi.Output[Sequence[outputs.WorkflowTemplateJob]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence[outputs.WorkflowTemplateParameter]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> pulumi.Output[outputs.WorkflowTemplatePlacement]:
        
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


