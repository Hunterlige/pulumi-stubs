

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetHostedZoneIdResult', 'AwaitableGetHostedZoneIdResult', 'get_hosted_zone_id', 'get_hosted_zone_id_output']
@pulumi.output_type
class GetHostedZoneIdResult:
    
    def __init__(__self__, id=..., load_balancer_type=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetHostedZoneIdResult(GetHostedZoneIdResult):
    def __await__(self): # -> Generator[Never, Any, GetHostedZoneIdResult]:
        ...
    


def get_hosted_zone_id(load_balancer_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetHostedZoneIdResult:
    
    ...

def get_hosted_zone_id_output(load_balancer_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetHostedZoneIdResult]:
    
    ...

