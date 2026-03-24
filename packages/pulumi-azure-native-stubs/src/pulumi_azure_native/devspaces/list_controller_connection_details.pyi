

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListControllerConnectionDetailsResult', 'AwaitableListControllerConnectionDetailsResult', 'list_controller_connection_details', 'list_controller_connection_details_output']
@pulumi.output_type
class ListControllerConnectionDetailsResult:
    def __init__(__self__, connection_details_list=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionDetailsList")
    def connection_details_list(self) -> Optional[Sequence[outputs.ControllerConnectionDetailsResponse]]:
        
        ...
    


class AwaitableListControllerConnectionDetailsResult(ListControllerConnectionDetailsResult):
    def __await__(self): # -> Generator[Never, Any, ListControllerConnectionDetailsResult]:
        ...
    


def list_controller_connection_details(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., target_container_host_resource_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListControllerConnectionDetailsResult:
    
    ...

def list_controller_connection_details_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., target_container_host_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListControllerConnectionDetailsResult]:
    
    ...

