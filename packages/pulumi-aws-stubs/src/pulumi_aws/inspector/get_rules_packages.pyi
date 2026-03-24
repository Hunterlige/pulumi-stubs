

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRulesPackagesResult', 'AwaitableGetRulesPackagesResult', 'get_rules_packages', 'get_rules_packages_output']
@pulumi.output_type
class GetRulesPackagesResult:
    
    def __init__(__self__, arns=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetRulesPackagesResult(GetRulesPackagesResult):
    def __await__(self): # -> Generator[Never, Any, GetRulesPackagesResult]:
        ...
    


def get_rules_packages(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRulesPackagesResult:
    
    ...

def get_rules_packages_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRulesPackagesResult]:
    
    ...

