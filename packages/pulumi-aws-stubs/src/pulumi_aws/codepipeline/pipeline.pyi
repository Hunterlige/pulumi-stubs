

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
__all__ = ['PipelineArgs', 'Pipeline']
@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *, artifact_stores: pulumi.Input[Sequence[pulumi.Input[PipelineArtifactStoreArgs]]], role_arn: pulumi.Input[_builtins.str], stages: pulumi.Input[Sequence[pulumi.Input[PipelineStageArgs]]], execution_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., triggers: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerArgs]]]] = ..., variables: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineVariableArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactStores")
    def artifact_stores(self) -> pulumi.Input[Sequence[pulumi.Input[PipelineArtifactStoreArgs]]]:
        
        ...
    
    @artifact_stores.setter
    def artifact_stores(self, value: pulumi.Input[Sequence[pulumi.Input[PipelineArtifactStoreArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stages(self) -> pulumi.Input[Sequence[pulumi.Input[PipelineStageArgs]]]:
        
        ...
    
    @stages.setter
    def stages(self, value: pulumi.Input[Sequence[pulumi.Input[PipelineStageArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionMode")
    def execution_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_mode.setter
    def execution_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineType")
    def pipeline_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_type.setter
    def pipeline_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerArgs]]]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineVariableArgs]]]]:
        
        ...
    
    @variables.setter
    def variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineVariableArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _PipelineState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., artifact_stores: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineArtifactStoreArgs]]]] = ..., execution_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., stages: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineStageArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trigger_alls: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerAllArgs]]]] = ..., triggers: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerArgs]]]] = ..., variables: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineVariableArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactStores")
    def artifact_stores(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineArtifactStoreArgs]]]]:
        
        ...
    
    @artifact_stores.setter
    def artifact_stores(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineArtifactStoreArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionMode")
    def execution_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_mode.setter
    def execution_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineType")
    def pipeline_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_type.setter
    def pipeline_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineStageArgs]]]]:
        
        ...
    
    @stages.setter
    def stages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineStageArgs]]]]): # -> None:
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
    @pulumi.getter(name="triggerAlls")
    def trigger_alls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerAllArgs]]]]:
        
        ...
    
    @trigger_alls.setter
    def trigger_alls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerAllArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerArgs]]]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineTriggerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineVariableArgs]]]]:
        
        ...
    
    @variables.setter
    def variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineVariableArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:codepipeline/pipeline:Pipeline")
class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., artifact_stores: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineArtifactStoreArgs, PipelineArtifactStoreArgsDict]]]]] = ..., execution_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., stages: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineStageArgs, PipelineStageArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., triggers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineTriggerArgs, PipelineTriggerArgsDict]]]]] = ..., variables: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineVariableArgs, PipelineVariableArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PipelineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., artifact_stores: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineArtifactStoreArgs, PipelineArtifactStoreArgsDict]]]]] = ..., execution_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., stages: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineStageArgs, PipelineStageArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trigger_alls: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineTriggerAllArgs, PipelineTriggerAllArgsDict]]]]] = ..., triggers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineTriggerArgs, PipelineTriggerArgsDict]]]]] = ..., variables: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PipelineVariableArgs, PipelineVariableArgsDict]]]]] = ...) -> Pipeline:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactStores")
    def artifact_stores(self) -> pulumi.Output[Sequence[outputs.PipelineArtifactStore]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionMode")
    def execution_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineType")
    def pipeline_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stages(self) -> pulumi.Output[Sequence[outputs.PipelineStage]]:
        
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
    @pulumi.getter(name="triggerAlls")
    def trigger_alls(self) -> pulumi.Output[Sequence[outputs.PipelineTriggerAll]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Sequence[outputs.PipelineTrigger]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variables(self) -> pulumi.Output[Optional[Sequence[outputs.PipelineVariable]]]:
        
        ...
    


