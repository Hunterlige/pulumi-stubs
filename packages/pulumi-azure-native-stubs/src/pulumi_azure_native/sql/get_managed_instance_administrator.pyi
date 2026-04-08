import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedInstanceAdministratorResult",
    "AwaitableGetManagedInstanceAdministratorResult",
    "get_managed_instance_administrator",
    "get_managed_instance_administrator_output",
]

@pulumi.output_type
class GetManagedInstanceAdministratorResult:
    def __init__(
        __self__,
        administrator_type=...,
        azure_api_version=...,
        id=...,
        login=...,
        name=...,
        sid=...,
        tenant_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetManagedInstanceAdministratorResult(
    GetManagedInstanceAdministratorResult
):
    def __await__(self): ...

def get_managed_instance_administrator(
    administrator_name: Optional[_builtins.str] = ...,
    managed_instance_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedInstanceAdministratorResult: ...
def get_managed_instance_administrator_output(
    administrator_name: Optional[pulumi.Input[_builtins.str]] = ...,
    managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedInstanceAdministratorResult]: ...
