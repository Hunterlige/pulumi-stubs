

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListServiceGroupAncestorsResult', 'AwaitableListServiceGroupAncestorsResult', 'list_service_group_ancestors', 'list_service_group_ancestors_output']
@pulumi.output_type
class ListServiceGroupAncestorsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ServiceGroupResponse]]:
        
        ...
    


class AwaitableListServiceGroupAncestorsResult(ListServiceGroupAncestorsResult):
    def __await__(self): # -> Generator[Never, Any, ListServiceGroupAncestorsResult]:
        ...
    


def list_service_group_ancestors(service_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListServiceGroupAncestorsResult:
    
    ...

def list_service_group_ancestors_output(service_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListServiceGroupAncestorsResult]:
    
    ...

