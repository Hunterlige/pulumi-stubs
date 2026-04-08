import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatastoreResult",
    "AwaitableGetDatastoreResult",
    "get_datastore",
    "get_datastore_output",
]

@pulumi.output_type
class GetDatastoreResult:
    def __init__(
        __self__,
        azure_api_version=...,
        disk_pool_volume=...,
        elastic_san_volume=...,
        id=...,
        name=...,
        net_app_volume=...,
        provisioning_state=...,
        status=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskPoolVolume")
    def disk_pool_volume(self) -> Optional[outputs.DiskPoolVolumeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="elasticSanVolume")
    def elastic_san_volume(self) -> Optional[outputs.ElasticSanVolumeResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="netAppVolume")
    def net_app_volume(self) -> Optional[outputs.NetAppVolumeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDatastoreResult(GetDatastoreResult):
    def __await__(self): ...

def get_datastore(
    cluster_name: Optional[_builtins.str] = ...,
    datastore_name: Optional[_builtins.str] = ...,
    private_cloud_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatastoreResult: ...
def get_datastore_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    datastore_name: Optional[pulumi.Input[_builtins.str]] = ...,
    private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatastoreResult]: ...
