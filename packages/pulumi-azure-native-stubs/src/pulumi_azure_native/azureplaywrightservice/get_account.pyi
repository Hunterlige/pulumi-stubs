import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccountResult",
    "AwaitableGetAccountResult",
    "get_account",
    "get_account_output",
]

@pulumi.output_type
class GetAccountResult:
    def __init__(
        __self__,
        azure_api_version=...,
        dashboard_uri=...,
        id=...,
        local_auth=...,
        location=...,
        name=...,
        provisioning_state=...,
        regional_affinity=...,
        reporting=...,
        scalable_execution=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dashboardUri")
    def dashboard_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localAuth")
    def local_auth(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionalAffinity")
    def regional_affinity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reporting(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalableExecution")
    def scalable_execution(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAccountResult(GetAccountResult):
    def __await__(self): ...

def get_account(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAccountResult: ...
def get_account_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccountResult]: ...
