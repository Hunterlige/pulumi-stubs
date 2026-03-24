

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRouteCalculatorResult', 'AwaitableGetRouteCalculatorResult', 'get_route_calculator', 'get_route_calculator_output']
@pulumi.output_type
class GetRouteCalculatorResult:
    
    def __init__(__self__, calculator_arn=..., calculator_name=..., create_time=..., data_source=..., description=..., id=..., region=..., tags=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="calculatorArn")
    def calculator_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="calculatorName")
    def calculator_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRouteCalculatorResult(GetRouteCalculatorResult):
    def __await__(self): # -> Generator[Never, Any, GetRouteCalculatorResult]:
        ...
    


def get_route_calculator(calculator_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRouteCalculatorResult:
    
    ...

def get_route_calculator_output(calculator_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRouteCalculatorResult]:
    
    ...

