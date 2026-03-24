

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
__all__ = ['ModelArgs', 'Model']
@pulumi.input_type
class ModelArgs:
    def __init__(__self__, *, execution_role_arn: pulumi.Input[_builtins.str], containers: Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerArgs]]]] = ..., enable_network_isolation: Optional[pulumi.Input[_builtins.bool]] = ..., inference_execution_config: Optional[pulumi.Input[ModelInferenceExecutionConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., primary_container: Optional[pulumi.Input[ModelPrimaryContainerArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[ModelVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerArgs]]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_network_isolation.setter
    def enable_network_isolation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceExecutionConfig")
    def inference_execution_config(self) -> Optional[pulumi.Input[ModelInferenceExecutionConfigArgs]]:
        
        ...
    
    @inference_execution_config.setter
    def inference_execution_config(self, value: Optional[pulumi.Input[ModelInferenceExecutionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> Optional[pulumi.Input[ModelPrimaryContainerArgs]]:
        
        ...
    
    @primary_container.setter
    def primary_container(self, value: Optional[pulumi.Input[ModelPrimaryContainerArgs]]): # -> None:
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
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[ModelVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[ModelVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ModelState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., containers: Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerArgs]]]] = ..., enable_network_isolation: Optional[pulumi.Input[_builtins.bool]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., inference_execution_config: Optional[pulumi.Input[ModelInferenceExecutionConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., primary_container: Optional[pulumi.Input[ModelPrimaryContainerArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[ModelVpcConfigArgs]] = ...) -> None:
        
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
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerArgs]]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_network_isolation.setter
    def enable_network_isolation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceExecutionConfig")
    def inference_execution_config(self) -> Optional[pulumi.Input[ModelInferenceExecutionConfigArgs]]:
        
        ...
    
    @inference_execution_config.setter
    def inference_execution_config(self, value: Optional[pulumi.Input[ModelInferenceExecutionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> Optional[pulumi.Input[ModelPrimaryContainerArgs]]:
        
        ...
    
    @primary_container.setter
    def primary_container(self, value: Optional[pulumi.Input[ModelPrimaryContainerArgs]]): # -> None:
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
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[ModelVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[ModelVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:sagemaker/model:Model")
class Model(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ModelContainerArgs, ModelContainerArgsDict]]]]] = ..., enable_network_isolation: Optional[pulumi.Input[_builtins.bool]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., inference_execution_config: Optional[pulumi.Input[Union[ModelInferenceExecutionConfigArgs, ModelInferenceExecutionConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., primary_container: Optional[pulumi.Input[Union[ModelPrimaryContainerArgs, ModelPrimaryContainerArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[Union[ModelVpcConfigArgs, ModelVpcConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ModelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ModelContainerArgs, ModelContainerArgsDict]]]]] = ..., enable_network_isolation: Optional[pulumi.Input[_builtins.bool]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., inference_execution_config: Optional[pulumi.Input[Union[ModelInferenceExecutionConfigArgs, ModelInferenceExecutionConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., primary_container: Optional[pulumi.Input[Union[ModelPrimaryContainerArgs, ModelPrimaryContainerArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[Union[ModelVpcConfigArgs, ModelVpcConfigArgsDict]]] = ...) -> Model:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> pulumi.Output[Optional[Sequence[outputs.ModelContainer]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceExecutionConfig")
    def inference_execution_config(self) -> pulumi.Output[outputs.ModelInferenceExecutionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContainer")
    def primary_container(self) -> pulumi.Output[Optional[outputs.ModelPrimaryContainer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional[outputs.ModelVpcConfig]]:
        
        ...
    


