

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConfigurationProfileValidatorArgs', 'ConfigurationProfileValidatorArgsDict', 'EnvironmentMonitorArgs', 'EnvironmentMonitorArgsDict', 'EventIntegrationEventFilterArgs', 'EventIntegrationEventFilterArgsDict', 'ExtensionActionPointArgs', 'ExtensionActionPointArgsDict', 'ExtensionActionPointActionArgs', 'ExtensionActionPointActionArgsDict', 'ExtensionParameterArgs', 'ExtensionParameterArgsDict']
class ConfigurationProfileValidatorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    content: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigurationProfileValidatorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], content: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentMonitorArgsDict(TypedDict):
    alarm_arn: pulumi.Input[_builtins.str]
    alarm_role_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentMonitorArgs:
    def __init__(__self__, *, alarm_arn: pulumi.Input[_builtins.str], alarm_role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmArn")
    def alarm_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @alarm_arn.setter
    def alarm_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmRoleArn")
    def alarm_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alarm_role_arn.setter
    def alarm_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EventIntegrationEventFilterArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]


@pulumi.input_type
class EventIntegrationEventFilterArgs:
    def __init__(__self__, *, source: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ExtensionActionPointArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[ExtensionActionPointActionArgsDict]]]
    point: pulumi.Input[_builtins.str]


@pulumi.input_type
class ExtensionActionPointArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[ExtensionActionPointActionArgs]]], point: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[ExtensionActionPointActionArgs]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[ExtensionActionPointActionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def point(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @point.setter
    def point(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ExtensionActionPointActionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ExtensionActionPointActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], uri: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExtensionParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ExtensionParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., required: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


