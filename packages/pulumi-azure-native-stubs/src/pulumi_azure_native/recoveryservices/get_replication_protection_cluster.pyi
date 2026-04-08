import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReplicationProtectionClusterResult",
    "AwaitableGetReplicationProtectionClusterResult",
    "get_replication_protection_cluster",
    "get_replication_protection_cluster_output",
]

@pulumi.output_type
class GetReplicationProtectionClusterResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., properties=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ReplicationProtectionClusterPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetReplicationProtectionClusterResult(
    GetReplicationProtectionClusterResult
):
    def __await__(self): ...

def get_replication_protection_cluster(
    fabric_name: Optional[_builtins.str] = ...,
    protection_container_name: Optional[_builtins.str] = ...,
    replication_protection_cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReplicationProtectionClusterResult: ...
def get_replication_protection_cluster_output(
    fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
    protection_container_name: Optional[pulumi.Input[_builtins.str]] = ...,
    replication_protection_cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReplicationProtectionClusterResult]: ...
