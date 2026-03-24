

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRealtimeLogConfigResult', 'AwaitableGetRealtimeLogConfigResult', 'get_realtime_log_config', 'get_realtime_log_config_output']
@pulumi.output_type
class GetRealtimeLogConfigResult:
    
    def __init__(__self__, arn=..., endpoints=..., fields=..., id=..., name=..., sampling_rate=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[outputs.GetRealtimeLogConfigEndpointResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Sequence[_builtins.str]:
        
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
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> _builtins.int:
        
        ...
    


class AwaitableGetRealtimeLogConfigResult(GetRealtimeLogConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetRealtimeLogConfigResult]:
        ...
    


def get_realtime_log_config(name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRealtimeLogConfigResult:
    
    ...

def get_realtime_log_config_output(name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRealtimeLogConfigResult]:
    
    ...

