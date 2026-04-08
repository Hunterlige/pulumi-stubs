import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceResult",
    "AwaitableGetInstanceResult",
    "get_instance",
    "get_instance_output",
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(
        __self__,
        account_name=...,
        azure_api_version=...,
        diagnostic_storage_properties=...,
        enable_diagnostics=...,
        id=...,
        iot_hubs=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticStorageProperties")
    def diagnostic_storage_properties(
        self,
    ) -> Optional[outputs.DiagnosticStoragePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="enableDiagnostics")
    def enable_diagnostics(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> Optional[Sequence[outputs.IotHubSettingsResponse]]: ...
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

class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): ...

def get_instance(
    account_name: Optional[_builtins.str] = ...,
    instance_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceResult: ...
def get_instance_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceResult]: ...
