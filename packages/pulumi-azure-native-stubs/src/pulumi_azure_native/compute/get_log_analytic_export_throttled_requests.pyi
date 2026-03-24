

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLogAnalyticExportThrottledRequestsResult', ..., 'get_log_analytic_export_throttled_requests', 'get_log_analytic_export_throttled_requests_output']
@pulumi.output_type
class GetLogAnalyticExportThrottledRequestsResult:
    
    def __init__(__self__, properties=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.LogAnalyticsOutputResponse:
        
        ...
    


class AwaitableGetLogAnalyticExportThrottledRequestsResult(GetLogAnalyticExportThrottledRequestsResult):
    def __await__(self): # -> Generator[Never, Any, GetLogAnalyticExportThrottledRequestsResult]:
        ...
    


def get_log_analytic_export_throttled_requests(blob_container_sas_uri: Optional[_builtins.str] = ..., from_time: Optional[_builtins.str] = ..., group_by_client_application_id: Optional[_builtins.bool] = ..., group_by_operation_name: Optional[_builtins.bool] = ..., group_by_resource_name: Optional[_builtins.bool] = ..., group_by_throttle_policy: Optional[_builtins.bool] = ..., group_by_user_agent: Optional[_builtins.bool] = ..., location: Optional[_builtins.str] = ..., to_time: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLogAnalyticExportThrottledRequestsResult:
    
    ...

def get_log_analytic_export_throttled_requests_output(blob_container_sas_uri: Optional[pulumi.Input[_builtins.str]] = ..., from_time: Optional[pulumi.Input[_builtins.str]] = ..., group_by_client_application_id: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., group_by_operation_name: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., group_by_resource_name: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., group_by_throttle_policy: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., group_by_user_agent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., to_time: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLogAnalyticExportThrottledRequestsResult]:
    
    ...

