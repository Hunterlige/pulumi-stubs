import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFleetspaceAccountResult",
    "AwaitableGetFleetspaceAccountResult",
    "get_fleetspace_account",
    "get_fleetspace_account_output",
]

@pulumi.output_type
class GetFleetspaceAccountResult:
    def __init__(
        __self__,
        azure_api_version=...,
        global_database_account_properties=...,
        id=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="globalDatabaseAccountProperties")
    def global_database_account_properties(
        self,
    ) -> Optional[
        outputs.FleetspaceAccountPropertiesResponseGlobalDatabaseAccountProperties
    ]: ...
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFleetspaceAccountResult(GetFleetspaceAccountResult):
    def __await__(self): ...

def get_fleetspace_account(
    fleet_name: Optional[_builtins.str] = ...,
    fleetspace_account_name: Optional[_builtins.str] = ...,
    fleetspace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFleetspaceAccountResult: ...
def get_fleetspace_account_output(
    fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
    fleetspace_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    fleetspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFleetspaceAccountResult]: ...
