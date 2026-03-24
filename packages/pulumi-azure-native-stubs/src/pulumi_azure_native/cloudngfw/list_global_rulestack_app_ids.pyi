

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListGlobalRulestackAppIdsResult', 'AwaitableListGlobalRulestackAppIdsResult', 'list_global_rulestack_app_ids', 'list_global_rulestack_app_ids_output']
@pulumi.output_type
class ListGlobalRulestackAppIdsResult:
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
    


class AwaitableListGlobalRulestackAppIdsResult(ListGlobalRulestackAppIdsResult):
    def __await__(self): # -> Generator[Never, Any, ListGlobalRulestackAppIdsResult]:
        ...
    


def list_global_rulestack_app_ids(app_id_version: Optional[_builtins.str] = ..., app_prefix: Optional[_builtins.str] = ..., global_rulestack_name: Optional[_builtins.str] = ..., skip: Optional[_builtins.str] = ..., top: Optional[_builtins.int] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListGlobalRulestackAppIdsResult:
    
    ...

def list_global_rulestack_app_ids_output(app_id_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., app_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., global_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ..., skip: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., top: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListGlobalRulestackAppIdsResult]:
    
    ...

