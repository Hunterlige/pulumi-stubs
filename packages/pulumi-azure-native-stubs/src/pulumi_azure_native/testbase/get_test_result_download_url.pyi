

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTestResultDownloadURLResult', 'AwaitableGetTestResultDownloadURLResult', 'get_test_result_download_url', 'get_test_result_download_url_output']
@pulumi.output_type
class GetTestResultDownloadURLResult:
    
    def __init__(__self__, download_url=..., expiration_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="downloadUrl")
    def download_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTestResultDownloadURLResult(GetTestResultDownloadURLResult):
    def __await__(self): # -> Generator[Never, Any, GetTestResultDownloadURLResult]:
        ...
    


def get_test_result_download_url(package_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., test_base_account_name: Optional[_builtins.str] = ..., test_result_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTestResultDownloadURLResult:
    
    ...

def get_test_result_download_url_output(package_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ..., test_result_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTestResultDownloadURLResult]:
    
    ...

