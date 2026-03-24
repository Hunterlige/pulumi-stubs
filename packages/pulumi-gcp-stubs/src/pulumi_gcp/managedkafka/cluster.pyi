import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClusterArgs", "Cluster"]

@pulumi.input_type
class ClusterArgs:
    def __init__(
        __self__,
        *,
        capacity_config: pulumi.Input[ClusterCapacityConfigArgs],
        cluster_id: pulumi.Input[_builtins.str],
        gcp_config: pulumi.Input[ClusterGcpConfigArgs],
        location: pulumi.Input[_builtins.str],
        broker_capacity_config: Optional[
            pulumi.Input[ClusterBrokerCapacityConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rebalance_config: Optional[pulumi.Input[ClusterRebalanceConfigArgs]] = ...,
        tls_config: Optional[pulumi.Input[ClusterTlsConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityConfig")
    def capacity_config(self) -> pulumi.Input[ClusterCapacityConfigArgs]: ...
    @capacity_config.setter
    def capacity_config(self, value: pulumi.Input[ClusterCapacityConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gcpConfig")
    def gcp_config(self) -> pulumi.Input[ClusterGcpConfigArgs]: ...
    @gcp_config.setter
    def gcp_config(self, value: pulumi.Input[ClusterGcpConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="brokerCapacityConfig")
    def broker_capacity_config(
        self,
    ) -> Optional[pulumi.Input[ClusterBrokerCapacityConfigArgs]]: ...
    @broker_capacity_config.setter
    def broker_capacity_config(
        self, value: Optional[pulumi.Input[ClusterBrokerCapacityConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rebalanceConfig")
    def rebalance_config(
        self,
    ) -> Optional[pulumi.Input[ClusterRebalanceConfigArgs]]: ...
    @rebalance_config.setter
    def rebalance_config(
        self, value: Optional[pulumi.Input[ClusterRebalanceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[ClusterTlsConfigArgs]]: ...
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[ClusterTlsConfigArgs]]): ...

@pulumi.input_type
class _ClusterState:
    def __init__(
        __self__,
        *,
        broker_capacity_config: Optional[
            pulumi.Input[ClusterBrokerCapacityConfigArgs]
        ] = ...,
        capacity_config: Optional[pulumi.Input[ClusterCapacityConfigArgs]] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        gcp_config: Optional[pulumi.Input[ClusterGcpConfigArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        rebalance_config: Optional[pulumi.Input[ClusterRebalanceConfigArgs]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tls_config: Optional[pulumi.Input[ClusterTlsConfigArgs]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="brokerCapacityConfig")
    def broker_capacity_config(
        self,
    ) -> Optional[pulumi.Input[ClusterBrokerCapacityConfigArgs]]: ...
    @broker_capacity_config.setter
    def broker_capacity_config(
        self, value: Optional[pulumi.Input[ClusterBrokerCapacityConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="capacityConfig")
    def capacity_config(self) -> Optional[pulumi.Input[ClusterCapacityConfigArgs]]: ...
    @capacity_config.setter
    def capacity_config(
        self, value: Optional[pulumi.Input[ClusterCapacityConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcpConfig")
    def gcp_config(self) -> Optional[pulumi.Input[ClusterGcpConfigArgs]]: ...
    @gcp_config.setter
    def gcp_config(self, value: Optional[pulumi.Input[ClusterGcpConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rebalanceConfig")
    def rebalance_config(
        self,
    ) -> Optional[pulumi.Input[ClusterRebalanceConfigArgs]]: ...
    @rebalance_config.setter
    def rebalance_config(
        self, value: Optional[pulumi.Input[ClusterRebalanceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[ClusterTlsConfigArgs]]: ...
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[ClusterTlsConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:managedkafka/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        broker_capacity_config: Optional[
            pulumi.Input[
                Union[
                    ClusterBrokerCapacityConfigArgs, ClusterBrokerCapacityConfigArgsDict
                ]
            ]
        ] = ...,
        capacity_config: Optional[
            pulumi.Input[
                Union[ClusterCapacityConfigArgs, ClusterCapacityConfigArgsDict]
            ]
        ] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gcp_config: Optional[
            pulumi.Input[Union[ClusterGcpConfigArgs, ClusterGcpConfigArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rebalance_config: Optional[
            pulumi.Input[
                Union[ClusterRebalanceConfigArgs, ClusterRebalanceConfigArgsDict]
            ]
        ] = ...,
        tls_config: Optional[
            pulumi.Input[Union[ClusterTlsConfigArgs, ClusterTlsConfigArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        broker_capacity_config: Optional[
            pulumi.Input[
                Union[
                    ClusterBrokerCapacityConfigArgs, ClusterBrokerCapacityConfigArgsDict
                ]
            ]
        ] = ...,
        capacity_config: Optional[
            pulumi.Input[
                Union[ClusterCapacityConfigArgs, ClusterCapacityConfigArgsDict]
            ]
        ] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        gcp_config: Optional[
            pulumi.Input[Union[ClusterGcpConfigArgs, ClusterGcpConfigArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        rebalance_config: Optional[
            pulumi.Input[
                Union[ClusterRebalanceConfigArgs, ClusterRebalanceConfigArgsDict]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tls_config: Optional[
            pulumi.Input[Union[ClusterTlsConfigArgs, ClusterTlsConfigArgsDict]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Cluster: ...
    @_builtins.property
    @pulumi.getter(name="brokerCapacityConfig")
    def broker_capacity_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterBrokerCapacityConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="capacityConfig")
    def capacity_config(self) -> pulumi.Output[outputs.ClusterCapacityConfig]: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gcpConfig")
    def gcp_config(self) -> pulumi.Output[outputs.ClusterGcpConfig]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="rebalanceConfig")
    def rebalance_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterRebalanceConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> pulumi.Output[outputs.ClusterTlsConfig]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
