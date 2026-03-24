

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListOrderDCAccessCodeResult', 'AwaitableListOrderDCAccessCodeResult', 'list_order_dc_access_code', 'list_order_dc_access_code_output']
@pulumi.output_type
class ListOrderDCAccessCodeResult:
    
    def __init__(__self__, auth_code=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListOrderDCAccessCodeResult(ListOrderDCAccessCodeResult):
    def __await__(self): # -> Generator[Never, Any, ListOrderDCAccessCodeResult]:
        ...
    


def list_order_dc_access_code(device_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListOrderDCAccessCodeResult:
    
    ...

def list_order_dc_access_code_output(device_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListOrderDCAccessCodeResult]:
    
    ...

