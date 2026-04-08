import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReportByBillingAccountResult",
    "AwaitableGetReportByBillingAccountResult",
    "get_report_by_billing_account",
    "get_report_by_billing_account_output",
]

@pulumi.output_type
class GetReportByBillingAccountResult:
    def __init__(
        __self__,
        azure_api_version=...,
        definition=...,
        delivery_info=...,
        format=...,
        id=...,
        name=...,
        schedule=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> outputs.ReportDefinitionResponse: ...
    @_builtins.property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> outputs.ReportDeliveryInfoResponse: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[outputs.ReportScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetReportByBillingAccountResult(GetReportByBillingAccountResult):
    def __await__(self): ...

def get_report_by_billing_account(
    billing_account_id: Optional[_builtins.str] = ...,
    report_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReportByBillingAccountResult: ...
def get_report_by_billing_account_output(
    billing_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
    report_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReportByBillingAccountResult]: ...
