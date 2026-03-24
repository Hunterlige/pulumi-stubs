

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListGlobalRulestackSecurityServicesResult', 'AwaitableListGlobalRulestackSecurityServicesResult', 'list_global_rulestack_security_services', 'list_global_rulestack_security_services_output']
@pulumi.output_type
class ListGlobalRulestackSecurityServicesResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> outputs.SecurityServicesTypeListResponse:
        
        ...
    


class AwaitableListGlobalRulestackSecurityServicesResult(ListGlobalRulestackSecurityServicesResult):
    def __await__(self): # -> Generator[Never, Any, ListGlobalRulestackSecurityServicesResult]:
        ...
    


def list_global_rulestack_security_services(global_rulestack_name: Optional[_builtins.str] = ..., skip: Optional[_builtins.str] = ..., top: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListGlobalRulestackSecurityServicesResult:
    
    ...

def list_global_rulestack_security_services_output(global_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ..., skip: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., top: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListGlobalRulestackSecurityServicesResult]:
    
    ...

