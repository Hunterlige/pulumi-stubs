

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualMachineRdpFileContentsResult', 'AwaitableGetVirtualMachineRdpFileContentsResult', 'get_virtual_machine_rdp_file_contents', 'get_virtual_machine_rdp_file_contents_output']
@pulumi.output_type
class GetVirtualMachineRdpFileContentsResult:
    
    def __init__(__self__, contents=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def contents(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetVirtualMachineRdpFileContentsResult(GetVirtualMachineRdpFileContentsResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualMachineRdpFileContentsResult]:
        ...
    


def get_virtual_machine_rdp_file_contents(lab_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualMachineRdpFileContentsResult:
    
    ...

def get_virtual_machine_rdp_file_contents_output(lab_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualMachineRdpFileContentsResult]:
    
    ...

