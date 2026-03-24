

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTestBaseAccountFileUploadUrlResult', 'AwaitableGetTestBaseAccountFileUploadUrlResult', 'get_test_base_account_file_upload_url', 'get_test_base_account_file_upload_url_output']
@pulumi.output_type
class GetTestBaseAccountFileUploadUrlResult:
    
    def __init__(__self__, blob_path=..., upload_url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobPath")
    def blob_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadUrl")
    def upload_url(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTestBaseAccountFileUploadUrlResult(GetTestBaseAccountFileUploadUrlResult):
    def __await__(self): # -> Generator[Never, Any, GetTestBaseAccountFileUploadUrlResult]:
        ...
    


def get_test_base_account_file_upload_url(blob_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_type: Optional[Union[_builtins.str, FileUploadResourceType]] = ..., test_base_account_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTestBaseAccountFileUploadUrlResult:
    
    ...

def get_test_base_account_file_upload_url_output(blob_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[Optional[Union[_builtins.str, FileUploadResourceType]]]] = ..., test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTestBaseAccountFileUploadUrlResult]:
    
    ...

