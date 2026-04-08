import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSqlResourceSqlTriggerResult",
    "AwaitableGetSqlResourceSqlTriggerResult",
    "get_sql_resource_sql_trigger",
    "get_sql_resource_sql_trigger_output",
]

@pulumi.output_type
class GetSqlResourceSqlTriggerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        resource=...,
        tags=...,
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
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[outputs.SqlTriggerGetPropertiesResponseResource]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSqlResourceSqlTriggerResult(GetSqlResourceSqlTriggerResult):
    def __await__(self): ...

def get_sql_resource_sql_trigger(
    account_name: Optional[_builtins.str] = ...,
    container_name: Optional[_builtins.str] = ...,
    database_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    trigger_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSqlResourceSqlTriggerResult: ...
def get_sql_resource_sql_trigger_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    container_name: Optional[pulumi.Input[_builtins.str]] = ...,
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    trigger_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSqlResourceSqlTriggerResult]: ...
