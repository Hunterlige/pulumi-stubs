

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from .. import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPlanResult', 'AwaitableGetPlanResult', 'get_plan', 'get_plan_output']
@pulumi.output_type
class GetPlanResult:
    
    def __init__(__self__, arn=..., description=..., execution_role=..., id=..., name=..., owner=..., primary_region=..., recovery_approach=..., recovery_time_objective_minutes=..., region=..., regions=..., tags=..., updated_at=..., version=...) -> None:
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
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> _builtins.str:
        
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
    def owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryRegion")
    def primary_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryApproach")
    def recovery_approach(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryTimeObjectiveMinutes")
    def recovery_time_objective_minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPlanResult(GetPlanResult):
    def __await__(self): # -> Generator[Never, Any, GetPlanResult]:
        ...
    


def get_plan(arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPlanResult:
    
    ...

def get_plan_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPlanResult]:
    
    ...

