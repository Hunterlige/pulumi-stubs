import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAmlFilesystemResult",
    "AwaitableGetAmlFilesystemResult",
    "get_aml_filesystem",
    "get_aml_filesystem_output",
]

@pulumi.output_type
class GetAmlFilesystemResult:
    def __init__(
        __self__,
        azure_api_version=...,
        client_info=...,
        encryption_settings=...,
        filesystem_subnet=...,
        health=...,
        hsm=...,
        id=...,
        identity=...,
        location=...,
        maintenance_window=...,
        name=...,
        provisioning_state=...,
        root_squash_settings=...,
        sku=...,
        storage_capacity_ti_b=...,
        system_data=...,
        tags=...,
        throughput_provisioned_m_bps=...,
        type=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientInfo")
    def client_info(self) -> outputs.AmlFilesystemClientInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(
        self,
    ) -> Optional[outputs.AmlFilesystemEncryptionSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="filesystemSubnet")
    def filesystem_subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def health(self) -> outputs.AmlFilesystemHealthResponse: ...
    @_builtins.property
    @pulumi.getter
    def hsm(self) -> Optional[outputs.AmlFilesystemResponseHsm]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.AmlFilesystemIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> outputs.AmlFilesystemResponseMaintenanceWindow: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootSquashSettings")
    def root_squash_settings(
        self,
    ) -> Optional[outputs.AmlFilesystemRootSquashSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuNameResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacityTiB")
    def storage_capacity_ti_b(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="throughputProvisionedMBps")
    def throughput_provisioned_m_bps(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetAmlFilesystemResult(GetAmlFilesystemResult):
    def __await__(self): ...

def get_aml_filesystem(
    aml_filesystem_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAmlFilesystemResult: ...
def get_aml_filesystem_output(
    aml_filesystem_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAmlFilesystemResult]: ...
