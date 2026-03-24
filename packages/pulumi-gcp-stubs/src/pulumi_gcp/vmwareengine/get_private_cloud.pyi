import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrivateCloudResult",
    "AwaitableGetPrivateCloudResult",
    "get_private_cloud",
    "get_private_cloud_output",
]

@pulumi.output_type
class GetPrivateCloudResult:
    def __init__(
        __self__,
        create_time=...,
        delete_time=...,
        deletion_delay_hours=...,
        description=...,
        expire_time=...,
        hcxes=...,
        id=...,
        location=...,
        management_clusters=...,
        name=...,
        network_configs=...,
        nsxes=...,
        project=...,
        send_deletion_delay_hours_if_zero=...,
        state=...,
        type=...,
        uid=...,
        update_time=...,
        vcenters=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionDelayHours")
    def deletion_delay_hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hcxes(self) -> Sequence[outputs.GetPrivateCloudHcxResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementClusters")
    def management_clusters(
        self,
    ) -> Sequence[outputs.GetPrivateCloudManagementClusterResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(
        self,
    ) -> Sequence[outputs.GetPrivateCloudNetworkConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def nsxes(self) -> Sequence[outputs.GetPrivateCloudNsxResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sendDeletionDelayHoursIfZero")
    def send_deletion_delay_hours_if_zero(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vcenters(self) -> Sequence[outputs.GetPrivateCloudVcenterResult]: ...

class AwaitableGetPrivateCloudResult(GetPrivateCloudResult):
    def __await__(self): ...

def get_private_cloud(
    location: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrivateCloudResult: ...
def get_private_cloud_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrivateCloudResult]: ...
