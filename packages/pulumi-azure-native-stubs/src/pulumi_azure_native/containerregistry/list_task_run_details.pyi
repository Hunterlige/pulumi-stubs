import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListTaskRunDetailsResult",
    "AwaitableListTaskRunDetailsResult",
    "list_task_run_details",
    "list_task_run_details_output",
]

@pulumi.output_type
class ListTaskRunDetailsResult:
    def __init__(
        __self__,
        force_update_tag=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        provisioning_state=...,
        run_request=...,
        run_result=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runRequest")
    def run_request(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="runResult")
    def run_result(self) -> outputs.RunResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableListTaskRunDetailsResult(ListTaskRunDetailsResult):
    def __await__(self): ...

def list_task_run_details(
    registry_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    task_run_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListTaskRunDetailsResult: ...
def list_task_run_details_output(
    registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    task_run_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListTaskRunDetailsResult]: ...
