import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIncidentTaskResult",
    "AwaitableGetIncidentTaskResult",
    "get_incident_task",
    "get_incident_task_output",
]

@pulumi.output_type
class GetIncidentTaskResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_by=...,
        created_time_utc=...,
        description=...,
        etag=...,
        id=...,
        last_modified_by=...,
        last_modified_time_utc=...,
        name=...,
        status=...,
        system_data=...,
        title=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[outputs.ClientInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[outputs.ClientInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetIncidentTaskResult(GetIncidentTaskResult):
    def __await__(self): ...

def get_incident_task(
    incident_id: Optional[_builtins.str] = ...,
    incident_task_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIncidentTaskResult: ...
def get_incident_task_output(
    incident_id: Optional[pulumi.Input[_builtins.str]] = ...,
    incident_task_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIncidentTaskResult]: ...
