import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetACSSBackupConnectionResult",
    "AwaitableGetACSSBackupConnectionResult",
    "get_acss_backup_connection",
    "get_acss_backup_connection_output",
]

@pulumi.output_type
class GetACSSBackupConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        backup_data=...,
        errors=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupData")
    def backup_data(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.ConnectorErrorDefinitionResponse: ...
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetACSSBackupConnectionResult(GetACSSBackupConnectionResult):
    def __await__(self): ...

def get_acss_backup_connection(
    backup_name: Optional[_builtins.str] = ...,
    connector_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetACSSBackupConnectionResult: ...
def get_acss_backup_connection_output(
    backup_name: Optional[pulumi.Input[_builtins.str]] = ...,
    connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetACSSBackupConnectionResult]: ...
