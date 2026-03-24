

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRoute53HealthChecksResult', 'AwaitableGetRoute53HealthChecksResult', 'get_route53_health_checks', 'get_route53_health_checks_output']
@pulumi.output_type
class GetRoute53HealthChecksResult:
    
    def __init__(__self__, health_checks=..., id=..., plan_arn=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Sequence[outputs.GetRoute53HealthChecksHealthCheckResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planArn")
    def plan_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def region(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRoute53HealthChecksResult(GetRoute53HealthChecksResult):
    def __await__(self): # -> Generator[Never, Any, GetRoute53HealthChecksResult]:
        ...
    


def get_route53_health_checks(plan_arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRoute53HealthChecksResult:
    
    ...

def get_route53_health_checks_output(plan_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRoute53HealthChecksResult]:
    
    ...

