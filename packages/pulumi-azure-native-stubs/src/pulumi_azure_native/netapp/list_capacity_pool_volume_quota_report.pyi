

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListCapacityPoolVolumeQuotaReportResult', 'AwaitableListCapacityPoolVolumeQuotaReportResult', 'list_capacity_pool_volume_quota_report', 'list_capacity_pool_volume_quota_report_output']
@pulumi.output_type
class ListCapacityPoolVolumeQuotaReportResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.QuotaReportResponse]]:
        
        ...
    


class AwaitableListCapacityPoolVolumeQuotaReportResult(ListCapacityPoolVolumeQuotaReportResult):
    def __await__(self): # -> Generator[Never, Any, ListCapacityPoolVolumeQuotaReportResult]:
        ...
    


def list_capacity_pool_volume_quota_report(account_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., volume_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListCapacityPoolVolumeQuotaReportResult:
    
    ...

def list_capacity_pool_volume_quota_report_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListCapacityPoolVolumeQuotaReportResult]:
    
    ...

