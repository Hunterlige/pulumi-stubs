

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFileShareUsageDataResult', 'AwaitableGetFileShareUsageDataResult', 'get_file_share_usage_data', 'get_file_share_usage_data_output']
@pulumi.output_type
class GetFileShareUsageDataResult:
    
    def __init__(__self__, properties=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.FileShareUsageDataOutputResponse:
        
        ...
    


class AwaitableGetFileShareUsageDataResult(GetFileShareUsageDataResult):
    def __await__(self): # -> Generator[Never, Any, GetFileShareUsageDataResult]:
        ...
    


def get_file_share_usage_data(location: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFileShareUsageDataResult:
    
    ...

def get_file_share_usage_data_output(location: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFileShareUsageDataResult]:
    
    ...

