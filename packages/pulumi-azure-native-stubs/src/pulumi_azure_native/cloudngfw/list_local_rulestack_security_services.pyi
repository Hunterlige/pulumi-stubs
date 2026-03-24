

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListLocalRulestackSecurityServicesResult', 'AwaitableListLocalRulestackSecurityServicesResult', 'list_local_rulestack_security_services', 'list_local_rulestack_security_services_output']
@pulumi.output_type
class ListLocalRulestackSecurityServicesResult:
    
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
    


class AwaitableListLocalRulestackSecurityServicesResult(ListLocalRulestackSecurityServicesResult):
    def __await__(self): # -> Generator[Never, Any, ListLocalRulestackSecurityServicesResult]:
        ...
    


def list_local_rulestack_security_services(local_rulestack_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., skip: Optional[_builtins.str] = ..., top: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListLocalRulestackSecurityServicesResult:
    
    ...

def list_local_rulestack_security_services_output(local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., skip: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., top: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListLocalRulestackSecurityServicesResult]:
    
    ...

