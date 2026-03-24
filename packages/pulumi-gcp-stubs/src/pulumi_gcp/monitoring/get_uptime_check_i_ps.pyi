

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUptimeCheckIPsResult', 'AwaitableGetUptimeCheckIPsResult', 'get_uptime_check_i_ps', 'get_uptime_check_i_ps_output']
@pulumi.output_type
class GetUptimeCheckIPsResult:
    
    def __init__(__self__, id=..., uptime_check_ips=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uptimeCheckIps")
    def uptime_check_ips(self) -> Sequence[outputs.GetUptimeCheckIPsUptimeCheckIpResult]:
        
        ...
    


class AwaitableGetUptimeCheckIPsResult(GetUptimeCheckIPsResult):
    def __await__(self): # -> Generator[Never, Any, GetUptimeCheckIPsResult]:
        ...
    


def get_uptime_check_i_ps(opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUptimeCheckIPsResult:
    
    ...

def get_uptime_check_i_ps_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUptimeCheckIPsResult]:
    
    ...

