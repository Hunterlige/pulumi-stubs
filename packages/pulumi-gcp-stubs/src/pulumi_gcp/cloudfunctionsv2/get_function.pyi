

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFunctionResult', 'AwaitableGetFunctionResult', 'get_function', 'get_function_output']
@pulumi.output_type
class GetFunctionResult:
    
    def __init__(__self__, build_configs=..., description=..., effective_labels=..., environment=..., event_triggers=..., id=..., kms_key_name=..., labels=..., location=..., name=..., project=..., pulumi_labels=..., service_configs=..., state=..., update_time=..., url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildConfigs")
    def build_configs(self) -> Sequence[outputs.GetFunctionBuildConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTriggers")
    def event_triggers(self) -> Sequence[outputs.GetFunctionEventTriggerResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConfigs")
    def service_configs(self) -> Sequence[outputs.GetFunctionServiceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        ...
    


class AwaitableGetFunctionResult(GetFunctionResult):
    def __await__(self): # -> Generator[Never, Any, GetFunctionResult]:
        ...
    


def get_function(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFunctionResult:
    
    ...

def get_function_output(location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFunctionResult]:
    
    ...

