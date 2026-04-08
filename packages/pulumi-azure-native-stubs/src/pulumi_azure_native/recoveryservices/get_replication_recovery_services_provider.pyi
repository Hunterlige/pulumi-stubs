import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReplicationRecoveryServicesProviderResult",
    ...,
    "get_replication_recovery_services_provider",
    "get_replication_recovery_services_provider_output",
]

@pulumi.output_type
class GetReplicationRecoveryServicesProviderResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        properties=...,
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
    def properties(self) -> outputs.RecoveryServicesProviderPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetReplicationRecoveryServicesProviderResult(
    GetReplicationRecoveryServicesProviderResult
):
    def __await__(self): ...

def get_replication_recovery_services_provider(
    fabric_name: Optional[_builtins.str] = ...,
    provider_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReplicationRecoveryServicesProviderResult: ...
def get_replication_recovery_services_provider_output(
    fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
    provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReplicationRecoveryServicesProviderResult]: ...
