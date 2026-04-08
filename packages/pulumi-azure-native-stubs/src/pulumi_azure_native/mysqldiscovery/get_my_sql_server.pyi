import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMySQLServerResult",
    "AwaitableGetMySQLServerResult",
    "get_my_sql_server",
    "get_my_sql_server_output",
]

@pulumi.output_type
class GetMySQLServerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        edition=...,
        errors=...,
        host_ip=...,
        host_name=...,
        id=...,
        labels=...,
        machine_id=...,
        mysql_version=...,
        name=...,
        number_of_database=...,
        port_number=...,
        provisioning_state=...,
        support_end_in=...,
        support_status=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.ErrorResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="hostIp")
    def host_ip(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mysqlVersion")
    def mysql_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numberOfDatabase")
    def number_of_database(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportEndIn")
    def support_end_in(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportStatus")
    def support_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetMySQLServerResult(GetMySQLServerResult):
    def __await__(self): ...

def get_my_sql_server(
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    site_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMySQLServerResult: ...
def get_my_sql_server_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMySQLServerResult]: ...
