

import builtins as _builtins
import sys
import pulumi
from typing import Any

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataIntegrationScheduleConfig', 'GetEventIntegrationEventFilterResult']
@pulumi.output_type
class DataIntegrationScheduleConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, first_execution_from: _builtins.str, object: _builtins.str, schedule_expression: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstExecutionFrom")
    def first_execution_from(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEventIntegrationEventFilterResult(dict):
    def __init__(__self__, *, source: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    


