import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBusinessCaseOperationResult",
    "AwaitableGetBusinessCaseOperationResult",
    "get_business_case_operation",
    "get_business_case_operation_output",
]

@pulumi.output_type
class GetBusinessCaseOperationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        provisioning_state=...,
        report_status_details=...,
        settings=...,
        state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reportStatusDetails")
    def report_status_details(self) -> Sequence[outputs.ReportDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.SettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetBusinessCaseOperationResult(GetBusinessCaseOperationResult):
    def __await__(self): ...

def get_business_case_operation(
    business_case_name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBusinessCaseOperationResult: ...
def get_business_case_operation_output(
    business_case_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBusinessCaseOperationResult]: ...
