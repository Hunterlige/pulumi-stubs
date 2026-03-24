

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListAgriServiceAvailableSolutionsResult', 'AwaitableListAgriServiceAvailableSolutionsResult', 'list_agri_service_available_solutions', 'list_agri_service_available_solutions_output']
@pulumi.output_type
class ListAgriServiceAvailableSolutionsResult:
    
    def __init__(__self__, solutions=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def solutions(self) -> Sequence[outputs.DataManagerForAgricultureSolutionResponse]:
        
        ...
    


class AwaitableListAgriServiceAvailableSolutionsResult(ListAgriServiceAvailableSolutionsResult):
    def __await__(self): # -> Generator[Never, Any, ListAgriServiceAvailableSolutionsResult]:
        ...
    


def list_agri_service_available_solutions(agri_service_resource_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListAgriServiceAvailableSolutionsResult:
    
    ...

def list_agri_service_available_solutions_output(agri_service_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListAgriServiceAvailableSolutionsResult]:
    
    ...

