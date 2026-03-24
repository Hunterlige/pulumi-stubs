

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegexPatternSetResult', 'AwaitableGetRegexPatternSetResult', 'get_regex_pattern_set', 'get_regex_pattern_set_output']
@pulumi.output_type
class GetRegexPatternSetResult:
    
    def __init__(__self__, arn=..., description=..., id=..., name=..., region=..., regular_expressions=..., scope=...) -> None:
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
    @pulumi.getter(name="regularExpressions")
    def regular_expressions(self) -> Sequence[outputs.GetRegexPatternSetRegularExpressionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        ...
    


class AwaitableGetRegexPatternSetResult(GetRegexPatternSetResult):
    def __await__(self): # -> Generator[Never, Any, GetRegexPatternSetResult]:
        ...
    


def get_regex_pattern_set(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegexPatternSetResult:
    
    ...

def get_regex_pattern_set_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegexPatternSetResult]:
    
    ...

