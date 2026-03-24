

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBusinessCaseOperationReportDownloadUrlResult', ..., 'get_business_case_operation_report_download_url', ...]
@pulumi.output_type
class GetBusinessCaseOperationReportDownloadUrlResult:
    
    def __init__(__self__, business_case_report_url=..., expiration_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessCaseReportUrl")
    def business_case_report_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBusinessCaseOperationReportDownloadUrlResult(GetBusinessCaseOperationReportDownloadUrlResult):
    def __await__(self): # -> Generator[Never, Any, GetBusinessCaseOperationReportDownloadUrlResult]:
        ...
    


def get_business_case_operation_report_download_url(business_case_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBusinessCaseOperationReportDownloadUrlResult:
    
    ...

def get_business_case_operation_report_download_url_output(business_case_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBusinessCaseOperationReportDownloadUrlResult]:
    
    ...

