

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConfigurationProfileValidator', 'EnvironmentMonitor', 'EventIntegrationEventFilter', 'ExtensionActionPoint', 'ExtensionActionPointAction', 'ExtensionParameter', 'GetConfigurationProfileValidatorResult', 'GetEnvironmentMonitorResult']
@pulumi.output_type
class ConfigurationProfileValidator(dict):
    def __init__(__self__, *, type: _builtins.str, content: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentMonitor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alarm_arn: _builtins.str, alarm_role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmArn")
    def alarm_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmRoleArn")
    def alarm_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EventIntegrationEventFilter(dict):
    def __init__(__self__, *, source: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExtensionActionPoint(dict):
    def __init__(__self__, *, actions: Sequence[outputs.ExtensionActionPointAction], point: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.ExtensionActionPointAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def point(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExtensionActionPointAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, uri: _builtins.str, description: Optional[_builtins.str] = ..., role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExtensionParameter(dict):
    def __init__(__self__, *, name: _builtins.str, description: Optional[_builtins.str] = ..., required: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GetConfigurationProfileValidatorResult(dict):
    def __init__(__self__, *, content: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentMonitorResult(dict):
    def __init__(__self__, *, alarm_arn: _builtins.str, alarm_role_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmArn")
    def alarm_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmRoleArn")
    def alarm_role_arn(self) -> _builtins.str:
        
        ...
    


