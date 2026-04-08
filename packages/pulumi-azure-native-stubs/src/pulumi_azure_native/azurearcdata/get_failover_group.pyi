import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFailoverGroupResult",
    "AwaitableGetFailoverGroupResult",
    "get_failover_group",
    "get_failover_group_output",
]

@pulumi.output_type
class GetFailoverGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
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
    @pulumi.getter
    def properties(self) -> outputs.FailoverGroupPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFailoverGroupResult(GetFailoverGroupResult):
    def __await__(self): ...

def get_failover_group(
    failover_group_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    sql_managed_instance_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFailoverGroupResult: ...
def get_failover_group_output(
    failover_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    sql_managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFailoverGroupResult]: ...
