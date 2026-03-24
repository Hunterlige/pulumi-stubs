import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrivateCloudArgs", "PrivateCloud"]

@pulumi.input_type
class PrivateCloudArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        management_cluster: pulumi.Input[PrivateCloudManagementClusterArgs],
        network_config: pulumi.Input[PrivateCloudNetworkConfigArgs],
        deletion_delay_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        send_deletion_delay_hours_if_zero: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managementCluster")
    def management_cluster(self) -> pulumi.Input[PrivateCloudManagementClusterArgs]: ...
    @management_cluster.setter
    def management_cluster(
        self, value: pulumi.Input[PrivateCloudManagementClusterArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Input[PrivateCloudNetworkConfigArgs]: ...
    @network_config.setter
    def network_config(self, value: pulumi.Input[PrivateCloudNetworkConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="deletionDelayHours")
    def deletion_delay_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deletion_delay_hours.setter
    def deletion_delay_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sendDeletionDelayHoursIfZero")
    def send_deletion_delay_hours_if_zero(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_deletion_delay_hours_if_zero.setter
    def send_deletion_delay_hours_if_zero(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PrivateCloudState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_delay_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        hcxes: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateCloudHcxArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management_cluster: Optional[
            pulumi.Input[PrivateCloudManagementClusterArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[PrivateCloudNetworkConfigArgs]] = ...,
        nsxes: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateCloudNsxArgs]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        send_deletion_delay_hours_if_zero: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vcenters: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateCloudVcenterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionDelayHours")
    def deletion_delay_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deletion_delay_hours.setter
    def deletion_delay_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hcxes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateCloudHcxArgs]]]]: ...
    @hcxes.setter
    def hcxes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateCloudHcxArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managementCluster")
    def management_cluster(
        self,
    ) -> Optional[pulumi.Input[PrivateCloudManagementClusterArgs]]: ...
    @management_cluster.setter
    def management_cluster(
        self, value: Optional[pulumi.Input[PrivateCloudManagementClusterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[PrivateCloudNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[PrivateCloudNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def nsxes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateCloudNsxArgs]]]]: ...
    @nsxes.setter
    def nsxes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateCloudNsxArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sendDeletionDelayHoursIfZero")
    def send_deletion_delay_hours_if_zero(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_deletion_delay_hours_if_zero.setter
    def send_deletion_delay_hours_if_zero(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def vcenters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateCloudVcenterArgs]]]]: ...
    @vcenters.setter
    def vcenters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateCloudVcenterArgs]]]],
    ): ...

@pulumi.type_token("gcp:vmwareengine/privateCloud:PrivateCloud")
class PrivateCloud(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        deletion_delay_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management_cluster: Optional[
            pulumi.Input[
                Union[
                    PrivateCloudManagementClusterArgs,
                    PrivateCloudManagementClusterArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[PrivateCloudNetworkConfigArgs, PrivateCloudNetworkConfigArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        send_deletion_delay_hours_if_zero: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PrivateCloudArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_delay_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        hcxes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[PrivateCloudHcxArgs, PrivateCloudHcxArgsDict]]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management_cluster: Optional[
            pulumi.Input[
                Union[
                    PrivateCloudManagementClusterArgs,
                    PrivateCloudManagementClusterArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[PrivateCloudNetworkConfigArgs, PrivateCloudNetworkConfigArgsDict]
            ]
        ] = ...,
        nsxes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[PrivateCloudNsxArgs, PrivateCloudNsxArgsDict]]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        send_deletion_delay_hours_if_zero: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vcenters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PrivateCloudVcenterArgs, PrivateCloudVcenterArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> PrivateCloud: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionDelayHours")
    def deletion_delay_hours(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hcxes(self) -> pulumi.Output[Sequence[outputs.PrivateCloudHcx]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managementCluster")
    def management_cluster(
        self,
    ) -> pulumi.Output[outputs.PrivateCloudManagementCluster]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[outputs.PrivateCloudNetworkConfig]: ...
    @_builtins.property
    @pulumi.getter
    def nsxes(self) -> pulumi.Output[Sequence[outputs.PrivateCloudNsx]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sendDeletionDelayHoursIfZero")
    def send_deletion_delay_hours_if_zero(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def vcenters(self) -> pulumi.Output[Sequence[outputs.PrivateCloudVcenter]]: ...
