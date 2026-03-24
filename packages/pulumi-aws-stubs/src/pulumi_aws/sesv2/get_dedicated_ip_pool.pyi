

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDedicatedIpPoolResult', 'AwaitableGetDedicatedIpPoolResult', 'get_dedicated_ip_pool', 'get_dedicated_ip_pool_output']
@pulumi.output_type
class GetDedicatedIpPoolResult:
    
    def __init__(__self__, arn=..., dedicated_ips=..., id=..., pool_name=..., region=..., scaling_mode=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedIps")
    def dedicated_ips(self) -> Sequence[outputs.GetDedicatedIpPoolDedicatedIpResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetDedicatedIpPoolResult(GetDedicatedIpPoolResult):
    def __await__(self): # -> Generator[Never, Any, GetDedicatedIpPoolResult]:
        ...
    


def get_dedicated_ip_pool(pool_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDedicatedIpPoolResult:
    
    ...

def get_dedicated_ip_pool_output(pool_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDedicatedIpPoolResult]:
    
    ...

