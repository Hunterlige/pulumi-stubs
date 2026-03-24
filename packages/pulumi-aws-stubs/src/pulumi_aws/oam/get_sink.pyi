

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSinkResult', 'AwaitableGetSinkResult', 'get_sink', 'get_sink_output']
@pulumi.output_type
class GetSinkResult:
    
    def __init__(__self__, arn=..., id=..., name=..., region=..., sink_id=..., sink_identifier=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
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
    @pulumi.getter(name="sinkId")
    def sink_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkIdentifier")
    def sink_identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetSinkResult(GetSinkResult):
    def __await__(self): # -> Generator[Never, Any, GetSinkResult]:
        ...
    


def get_sink(region: Optional[_builtins.str] = ..., sink_identifier: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSinkResult:
    
    ...

def get_sink_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., sink_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSinkResult]:
    
    ...

