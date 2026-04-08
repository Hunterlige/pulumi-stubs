import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecretSyncResult",
    "AwaitableGetSecretSyncResult",
    "get_secret_sync",
    "get_secret_sync_output",
]

@pulumi.output_type
class GetSecretSyncResult:
    def __init__(
        __self__,
        azure_api_version=...,
        extended_location=...,
        force_synchronization=...,
        id=...,
        kubernetes_secret_type=...,
        location=...,
        name=...,
        object_secret_mapping=...,
        provisioning_state=...,
        secret_provider_class_name=...,
        service_account_name=...,
        status=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> Optional[outputs.AzureResourceManagerCommonTypesExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="forceSynchronization")
    def force_synchronization(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesSecretType")
    def kubernetes_secret_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectSecretMapping")
    def object_secret_mapping(
        self,
    ) -> Sequence[outputs.KubernetesSecretObjectMappingResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretProviderClassName")
    def secret_provider_class_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.SecretSyncStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSecretSyncResult(GetSecretSyncResult):
    def __await__(self): ...

def get_secret_sync(
    resource_group_name: Optional[_builtins.str] = ...,
    secret_sync_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecretSyncResult: ...
def get_secret_sync_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    secret_sync_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecretSyncResult]: ...
