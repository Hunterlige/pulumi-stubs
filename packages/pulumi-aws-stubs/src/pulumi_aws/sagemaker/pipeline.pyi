

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
__all__ = ['PipelineArgs', 'Pipeline']
@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *, pipeline_display_name: pulumi.Input[_builtins.str], pipeline_name: pulumi.Input[_builtins.str], parallelism_configuration: Optional[pulumi.Input[PipelineParallelismConfigurationArgs]] = ..., pipeline_definition: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_definition_s3_location: Optional[pulumi.Input[PipelinePipelineDefinitionS3LocationArgs]] = ..., pipeline_description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDisplayName")
    def pipeline_display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pipeline_display_name.setter
    def pipeline_display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pipeline_name.setter
    def pipeline_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelismConfiguration")
    def parallelism_configuration(self) -> Optional[pulumi.Input[PipelineParallelismConfigurationArgs]]:
        
        ...
    
    @parallelism_configuration.setter
    def parallelism_configuration(self, value: Optional[pulumi.Input[PipelineParallelismConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDefinition")
    def pipeline_definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_definition.setter
    def pipeline_definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDefinitionS3Location")
    def pipeline_definition_s3_location(self) -> Optional[pulumi.Input[PipelinePipelineDefinitionS3LocationArgs]]:
        
        ...
    
    @pipeline_definition_s3_location.setter
    def pipeline_definition_s3_location(self, value: Optional[pulumi.Input[PipelinePipelineDefinitionS3LocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDescription")
    def pipeline_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_description.setter
    def pipeline_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _PipelineState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., parallelism_configuration: Optional[pulumi.Input[PipelineParallelismConfigurationArgs]] = ..., pipeline_definition: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_definition_s3_location: Optional[pulumi.Input[PipelinePipelineDefinitionS3LocationArgs]] = ..., pipeline_description: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_display_name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelismConfiguration")
    def parallelism_configuration(self) -> Optional[pulumi.Input[PipelineParallelismConfigurationArgs]]:
        
        ...
    
    @parallelism_configuration.setter
    def parallelism_configuration(self, value: Optional[pulumi.Input[PipelineParallelismConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDefinition")
    def pipeline_definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_definition.setter
    def pipeline_definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDefinitionS3Location")
    def pipeline_definition_s3_location(self) -> Optional[pulumi.Input[PipelinePipelineDefinitionS3LocationArgs]]:
        
        ...
    
    @pipeline_definition_s3_location.setter
    def pipeline_definition_s3_location(self, value: Optional[pulumi.Input[PipelinePipelineDefinitionS3LocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDescription")
    def pipeline_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_description.setter
    def pipeline_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDisplayName")
    def pipeline_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_display_name.setter
    def pipeline_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_name.setter
    def pipeline_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:sagemaker/pipeline:Pipeline")
class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., parallelism_configuration: Optional[pulumi.Input[Union[PipelineParallelismConfigurationArgs, PipelineParallelismConfigurationArgsDict]]] = ..., pipeline_definition: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_definition_s3_location: Optional[pulumi.Input[Union[PipelinePipelineDefinitionS3LocationArgs, PipelinePipelineDefinitionS3LocationArgsDict]]] = ..., pipeline_description: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_display_name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PipelineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., parallelism_configuration: Optional[pulumi.Input[Union[PipelineParallelismConfigurationArgs, PipelineParallelismConfigurationArgsDict]]] = ..., pipeline_definition: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_definition_s3_location: Optional[pulumi.Input[Union[PipelinePipelineDefinitionS3LocationArgs, PipelinePipelineDefinitionS3LocationArgsDict]]] = ..., pipeline_description: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_display_name: Optional[pulumi.Input[_builtins.str]] = ..., pipeline_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Pipeline:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelismConfiguration")
    def parallelism_configuration(self) -> pulumi.Output[Optional[outputs.PipelineParallelismConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDefinition")
    def pipeline_definition(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDefinitionS3Location")
    def pipeline_definition_s3_location(self) -> pulumi.Output[Optional[outputs.PipelinePipelineDefinitionS3Location]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDescription")
    def pipeline_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineDisplayName")
    def pipeline_display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


