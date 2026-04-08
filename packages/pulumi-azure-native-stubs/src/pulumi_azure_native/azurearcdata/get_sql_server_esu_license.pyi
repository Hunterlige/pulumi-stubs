import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSqlServerEsuLicenseResult",
    "AwaitableGetSqlServerEsuLicenseResult",
    "get_sql_server_esu_license",
    "get_sql_server_esu_license_output",
]

@pulumi.output_type
class GetSqlServerEsuLicenseResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        properties=...,
        system_data=...,
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
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.SqlServerEsuLicensePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSqlServerEsuLicenseResult(GetSqlServerEsuLicenseResult):
    def __await__(self): ...

def get_sql_server_esu_license(
    resource_group_name: Optional[_builtins.str] = ...,
    sql_server_esu_license_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSqlServerEsuLicenseResult: ...
def get_sql_server_esu_license_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    sql_server_esu_license_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSqlServerEsuLicenseResult]: ...
