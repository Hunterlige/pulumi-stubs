

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
__all__ = ['StateMachineArgs', 'StateMachine']
@pulumi.input_type
class StateMachineArgs:
    def __init__(__self__, *, definition: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], encryption_configuration: Optional[pulumi.Input[StateMachineEncryptionConfigurationArgs]] = ..., logging_configuration: Optional[pulumi.Input[StateMachineLoggingConfigurationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracing_configuration: Optional[pulumi.Input[StateMachineTracingConfigurationArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @definition.setter
    def definition(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[StateMachineEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[StateMachineEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> Optional[pulumi.Input[StateMachineLoggingConfigurationArgs]]:
        
        ...
    
    @logging_configuration.setter
    def logging_configuration(self, value: Optional[pulumi.Input[StateMachineLoggingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publish(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publish.setter
    def publish(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="tracingConfiguration")
    def tracing_configuration(self) -> Optional[pulumi.Input[StateMachineTracingConfigurationArgs]]:
        
        ...
    
    @tracing_configuration.setter
    def tracing_configuration(self, value: Optional[pulumi.Input[StateMachineTracingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _StateMachineState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., definition: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[StateMachineEncryptionConfigurationArgs]] = ..., logging_configuration: Optional[pulumi.Input[StateMachineLoggingConfigurationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revision_id: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., state_machine_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracing_configuration: Optional[pulumi.Input[StateMachineTracingConfigurationArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., version_description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @definition.setter
    def definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[StateMachineEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[StateMachineEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> Optional[pulumi.Input[StateMachineLoggingConfigurationArgs]]:
        
        ...
    
    @logging_configuration.setter
    def logging_configuration(self, value: Optional[pulumi.Input[StateMachineLoggingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publish(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publish.setter
    def publish(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @revision_id.setter
    def revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMachineVersionArn")
    def state_machine_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_machine_version_arn.setter
    def state_machine_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="tracingConfiguration")
    def tracing_configuration(self) -> Optional[pulumi.Input[StateMachineTracingConfigurationArgs]]:
        
        ...
    
    @tracing_configuration.setter
    def tracing_configuration(self, value: Optional[pulumi.Input[StateMachineTracingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @version_description.setter
    def version_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:sfn/stateMachine:StateMachine")
class StateMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., definition: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[Union[StateMachineEncryptionConfigurationArgs, StateMachineEncryptionConfigurationArgsDict]]] = ..., logging_configuration: Optional[pulumi.Input[Union[StateMachineLoggingConfigurationArgs, StateMachineLoggingConfigurationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracing_configuration: Optional[pulumi.Input[Union[StateMachineTracingConfigurationArgs, StateMachineTracingConfigurationArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StateMachineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., definition: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[Union[StateMachineEncryptionConfigurationArgs, StateMachineEncryptionConfigurationArgsDict]]] = ..., logging_configuration: Optional[pulumi.Input[Union[StateMachineLoggingConfigurationArgs, StateMachineLoggingConfigurationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., publish: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revision_id: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., state_machine_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracing_configuration: Optional[pulumi.Input[Union[StateMachineTracingConfigurationArgs, StateMachineTracingConfigurationArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., version_description: Optional[pulumi.Input[_builtins.str]] = ...) -> StateMachine:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output[outputs.StateMachineEncryptionConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> pulumi.Output[outputs.StateMachineLoggingConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publish(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMachineVersionArn")
    def state_machine_version_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="tracingConfiguration")
    def tracing_configuration(self) -> pulumi.Output[outputs.StateMachineTracingConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> pulumi.Output[_builtins.str]:
        ...
    


