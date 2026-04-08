import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConsoleResult",
    "AwaitableGetConsoleResult",
    "get_console",
    "get_console_output",
]

@pulumi.output_type
class GetConsoleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        detailed_status=...,
        detailed_status_message=...,
        enabled=...,
        etag=...,
        expiration=...,
        extended_location=...,
        id=...,
        location=...,
        name=...,
        private_link_service_id=...,
        provisioning_state=...,
        ssh_public_key=...,
        system_data=...,
        tags=...,
        type=...,
        virtual_machine_access_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse: ...
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
    @pulumi.getter(name="privateLinkServiceId")
    def private_link_service_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> outputs.SshPublicKeyResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineAccessId")
    def virtual_machine_access_id(self) -> _builtins.str: ...

class AwaitableGetConsoleResult(GetConsoleResult):
    def __await__(self): ...

def get_console(
    console_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_machine_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConsoleResult: ...
def get_console_output(
    console_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConsoleResult]: ...
