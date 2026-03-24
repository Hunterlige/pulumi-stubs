

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
__all__ = ['FlowDefinitionArgs', 'FlowDefinition']
@pulumi.input_type
class FlowDefinitionArgs:
    def __init__(__self__, *, flow_definition_name: pulumi.Input[_builtins.str], human_loop_config: pulumi.Input[FlowDefinitionHumanLoopConfigArgs], output_config: pulumi.Input[FlowDefinitionOutputConfigArgs], role_arn: pulumi.Input[_builtins.str], human_loop_activation_config: Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigArgs]] = ..., human_loop_request_source: Optional[pulumi.Input[FlowDefinitionHumanLoopRequestSourceArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowDefinitionName")
    def flow_definition_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @flow_definition_name.setter
    def flow_definition_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopConfig")
    def human_loop_config(self) -> pulumi.Input[FlowDefinitionHumanLoopConfigArgs]:
        
        ...
    
    @human_loop_config.setter
    def human_loop_config(self, value: pulumi.Input[FlowDefinitionHumanLoopConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> pulumi.Input[FlowDefinitionOutputConfigArgs]:
        
        ...
    
    @output_config.setter
    def output_config(self, value: pulumi.Input[FlowDefinitionOutputConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopActivationConfig")
    def human_loop_activation_config(self) -> Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigArgs]]:
        
        ...
    
    @human_loop_activation_config.setter
    def human_loop_activation_config(self, value: Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopRequestSource")
    def human_loop_request_source(self) -> Optional[pulumi.Input[FlowDefinitionHumanLoopRequestSourceArgs]]:
        
        ...
    
    @human_loop_request_source.setter
    def human_loop_request_source(self, value: Optional[pulumi.Input[FlowDefinitionHumanLoopRequestSourceArgs]]): # -> None:
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
class _FlowDefinitionState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., flow_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., human_loop_activation_config: Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigArgs]] = ..., human_loop_config: Optional[pulumi.Input[FlowDefinitionHumanLoopConfigArgs]] = ..., human_loop_request_source: Optional[pulumi.Input[FlowDefinitionHumanLoopRequestSourceArgs]] = ..., output_config: Optional[pulumi.Input[FlowDefinitionOutputConfigArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowDefinitionName")
    def flow_definition_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @flow_definition_name.setter
    def flow_definition_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopActivationConfig")
    def human_loop_activation_config(self) -> Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigArgs]]:
        
        ...
    
    @human_loop_activation_config.setter
    def human_loop_activation_config(self, value: Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopConfig")
    def human_loop_config(self) -> Optional[pulumi.Input[FlowDefinitionHumanLoopConfigArgs]]:
        
        ...
    
    @human_loop_config.setter
    def human_loop_config(self, value: Optional[pulumi.Input[FlowDefinitionHumanLoopConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopRequestSource")
    def human_loop_request_source(self) -> Optional[pulumi.Input[FlowDefinitionHumanLoopRequestSourceArgs]]:
        
        ...
    
    @human_loop_request_source.setter
    def human_loop_request_source(self, value: Optional[pulumi.Input[FlowDefinitionHumanLoopRequestSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> Optional[pulumi.Input[FlowDefinitionOutputConfigArgs]]:
        
        ...
    
    @output_config.setter
    def output_config(self, value: Optional[pulumi.Input[FlowDefinitionOutputConfigArgs]]): # -> None:
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
    


@pulumi.type_token("aws:sagemaker/flowDefinition:FlowDefinition")
class FlowDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., flow_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., human_loop_activation_config: Optional[pulumi.Input[Union[FlowDefinitionHumanLoopActivationConfigArgs, FlowDefinitionHumanLoopActivationConfigArgsDict]]] = ..., human_loop_config: Optional[pulumi.Input[Union[FlowDefinitionHumanLoopConfigArgs, FlowDefinitionHumanLoopConfigArgsDict]]] = ..., human_loop_request_source: Optional[pulumi.Input[Union[FlowDefinitionHumanLoopRequestSourceArgs, FlowDefinitionHumanLoopRequestSourceArgsDict]]] = ..., output_config: Optional[pulumi.Input[Union[FlowDefinitionOutputConfigArgs, FlowDefinitionOutputConfigArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FlowDefinitionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., flow_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., human_loop_activation_config: Optional[pulumi.Input[Union[FlowDefinitionHumanLoopActivationConfigArgs, FlowDefinitionHumanLoopActivationConfigArgsDict]]] = ..., human_loop_config: Optional[pulumi.Input[Union[FlowDefinitionHumanLoopConfigArgs, FlowDefinitionHumanLoopConfigArgsDict]]] = ..., human_loop_request_source: Optional[pulumi.Input[Union[FlowDefinitionHumanLoopRequestSourceArgs, FlowDefinitionHumanLoopRequestSourceArgsDict]]] = ..., output_config: Optional[pulumi.Input[Union[FlowDefinitionOutputConfigArgs, FlowDefinitionOutputConfigArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> FlowDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowDefinitionName")
    def flow_definition_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopActivationConfig")
    def human_loop_activation_config(self) -> pulumi.Output[Optional[outputs.FlowDefinitionHumanLoopActivationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopConfig")
    def human_loop_config(self) -> pulumi.Output[outputs.FlowDefinitionHumanLoopConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopRequestSource")
    def human_loop_request_source(self) -> pulumi.Output[Optional[outputs.FlowDefinitionHumanLoopRequestSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> pulumi.Output[outputs.FlowDefinitionOutputConfig]:
        
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


