import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGroupsOperationResult",
    "AwaitableGetGroupsOperationResult",
    "get_groups_operation",
    "get_groups_operation_output",
]

@pulumi.output_type
class GetGroupsOperationResult:
    def __init__(
        __self__,
        are_assessments_running=...,
        assessments=...,
        azure_api_version=...,
        created_timestamp=...,
        group_status=...,
        group_type=...,
        id=...,
        machine_count=...,
        name=...,
        provisioning_state=...,
        supported_assessment_types=...,
        system_data=...,
        type=...,
        updated_timestamp=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="areAssessmentsRunning")
    def are_assessments_running(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def assessments(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupStatus")
    def group_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineCount")
    def machine_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedAssessmentTypes")
    def supported_assessment_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str: ...

class AwaitableGetGroupsOperationResult(GetGroupsOperationResult):
    def __await__(self): ...

def get_groups_operation(
    group_name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGroupsOperationResult: ...
def get_groups_operation_output(
    group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGroupsOperationResult]: ...
