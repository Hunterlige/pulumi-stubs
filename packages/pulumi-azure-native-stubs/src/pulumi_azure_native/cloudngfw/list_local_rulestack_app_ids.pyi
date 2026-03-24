

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListLocalRulestackAppIdsResult', 'AwaitableListLocalRulestackAppIdsResult', 'list_local_rulestack_app_ids', 'list_local_rulestack_app_ids_output']
@pulumi.output_type
class ListLocalRulestackAppIdsResult:
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableListLocalRulestackAppIdsResult(ListLocalRulestackAppIdsResult):
    def __await__(self): # -> Generator[Never, Any, ListLocalRulestackAppIdsResult]:
        ...
    


def list_local_rulestack_app_ids(app_id_version: Optional[_builtins.str] = ..., app_prefix: Optional[_builtins.str] = ..., local_rulestack_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., skip: Optional[_builtins.str] = ..., top: Optional[_builtins.int] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListLocalRulestackAppIdsResult:
    
    ...

def list_local_rulestack_app_ids_output(app_id_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., app_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., skip: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., top: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListLocalRulestackAppIdsResult]:
    
    ...

