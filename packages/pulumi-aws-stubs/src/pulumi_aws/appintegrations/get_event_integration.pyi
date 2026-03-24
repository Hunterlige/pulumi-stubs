

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEventIntegrationResult', 'AwaitableGetEventIntegrationResult', 'get_event_integration', 'get_event_integration_output']
@pulumi.output_type
class GetEventIntegrationResult:
    
    def __init__(__self__, arn=..., description=..., event_filters=..., eventbridge_bus=..., id=..., name=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventFilters")
    def event_filters(self) -> Sequence[outputs.GetEventIntegrationEventFilterResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventbridgeBus")
    def eventbridge_bus(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetEventIntegrationResult(GetEventIntegrationResult):
    def __await__(self): # -> Generator[Never, Any, GetEventIntegrationResult]:
        ...
    


def get_event_integration(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEventIntegrationResult:
    
    ...

def get_event_integration_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEventIntegrationResult]:
    
    ...

