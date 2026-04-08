import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterResult",
    "AwaitableGetClusterResult",
    "get_cluster",
    "get_cluster_output",
]

@pulumi.output_type
class GetClusterResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cluster_id=...,
        cluster_size=...,
        hosts=...,
        id=...,
        name=...,
        provisioning_state=...,
        sku=...,
        system_data=...,
        type=...,
        vsan_datastore_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="clusterSize")
    def cluster_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vsanDatastoreName")
    def vsan_datastore_name(self) -> Optional[_builtins.str]: ...

class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): ...

def get_cluster(
    cluster_name: Optional[_builtins.str] = ...,
    private_cloud_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterResult: ...
def get_cluster_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterResult]: ...
