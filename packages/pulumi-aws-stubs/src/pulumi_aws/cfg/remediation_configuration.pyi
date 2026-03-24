

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RemediationConfigurationArgs', 'RemediationConfiguration']
@pulumi.input_type
class RemediationConfigurationArgs:
    def __init__(__self__, *, config_rule_name: pulumi.Input[_builtins.str], target_id: pulumi.Input[_builtins.str], target_type: pulumi.Input[_builtins.str], automatic: Optional[pulumi.Input[_builtins.bool]] = ..., execution_controls: Optional[pulumi.Input[RemediationConfigurationExecutionControlsArgs]] = ..., maximum_automatic_attempts: Optional[pulumi.Input[_builtins.int]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[RemediationConfigurationParameterArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., retry_attempt_seconds: Optional[pulumi.Input[_builtins.int]] = ..., target_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configRuleName")
    def config_rule_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @config_rule_name.setter
    def config_rule_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_id.setter
    def target_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def automatic(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatic.setter
    def automatic(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionControls")
    def execution_controls(self) -> Optional[pulumi.Input[RemediationConfigurationExecutionControlsArgs]]:
        
        ...
    
    @execution_controls.setter
    def execution_controls(self, value: Optional[pulumi.Input[RemediationConfigurationExecutionControlsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumAutomaticAttempts")
    def maximum_automatic_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_automatic_attempts.setter
    def maximum_automatic_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RemediationConfigurationParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RemediationConfigurationParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryAttemptSeconds")
    def retry_attempt_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_attempt_seconds.setter
    def retry_attempt_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_version.setter
    def target_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RemediationConfigurationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., automatic: Optional[pulumi.Input[_builtins.bool]] = ..., config_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., execution_controls: Optional[pulumi.Input[RemediationConfigurationExecutionControlsArgs]] = ..., maximum_automatic_attempts: Optional[pulumi.Input[_builtins.int]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[RemediationConfigurationParameterArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., retry_attempt_seconds: Optional[pulumi.Input[_builtins.int]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., target_type: Optional[pulumi.Input[_builtins.str]] = ..., target_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def automatic(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatic.setter
    def automatic(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configRuleName")
    def config_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @config_rule_name.setter
    def config_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionControls")
    def execution_controls(self) -> Optional[pulumi.Input[RemediationConfigurationExecutionControlsArgs]]:
        
        ...
    
    @execution_controls.setter
    def execution_controls(self, value: Optional[pulumi.Input[RemediationConfigurationExecutionControlsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumAutomaticAttempts")
    def maximum_automatic_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_automatic_attempts.setter
    def maximum_automatic_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RemediationConfigurationParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RemediationConfigurationParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryAttemptSeconds")
    def retry_attempt_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_attempt_seconds.setter
    def retry_attempt_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_version.setter
    def target_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RemediationConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., automatic: Optional[pulumi.Input[_builtins.bool]] = ..., config_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., execution_controls: Optional[pulumi.Input[Union[RemediationConfigurationExecutionControlsArgs, RemediationConfigurationExecutionControlsArgsDict]]] = ..., maximum_automatic_attempts: Optional[pulumi.Input[_builtins.int]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RemediationConfigurationParameterArgs, RemediationConfigurationParameterArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., retry_attempt_seconds: Optional[pulumi.Input[_builtins.int]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., target_type: Optional[pulumi.Input[_builtins.str]] = ..., target_version: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RemediationConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., automatic: Optional[pulumi.Input[_builtins.bool]] = ..., config_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., execution_controls: Optional[pulumi.Input[Union[RemediationConfigurationExecutionControlsArgs, RemediationConfigurationExecutionControlsArgsDict]]] = ..., maximum_automatic_attempts: Optional[pulumi.Input[_builtins.int]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RemediationConfigurationParameterArgs, RemediationConfigurationParameterArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., retry_attempt_seconds: Optional[pulumi.Input[_builtins.int]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., target_type: Optional[pulumi.Input[_builtins.str]] = ..., target_version: Optional[pulumi.Input[_builtins.str]] = ...) -> RemediationConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def automatic(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configRuleName")
    def config_rule_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionControls")
    def execution_controls(self) -> pulumi.Output[Optional[outputs.RemediationConfigurationExecutionControls]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumAutomaticAttempts")
    def maximum_automatic_attempts(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence[outputs.RemediationConfigurationParameter]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryAttemptSeconds")
    def retry_attempt_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


