import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
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
        arn=...,
        bootstrap_brokers=...,
        bootstrap_brokers_public_sasl_iam=...,
        bootstrap_brokers_public_sasl_scram=...,
        bootstrap_brokers_public_tls=...,
        bootstrap_brokers_sasl_iam=...,
        bootstrap_brokers_sasl_scram=...,
        bootstrap_brokers_tls=...,
        broker_node_group_infos=...,
        cluster_name=...,
        cluster_uuid=...,
        id=...,
        kafka_version=...,
        number_of_broker_nodes=...,
        region=...,
        tags=...,
        zookeeper_connect_string=...,
        zookeeper_connect_string_tls=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokers")
    def bootstrap_brokers(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicSaslIam")
    def bootstrap_brokers_public_sasl_iam(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicSaslScram")
    def bootstrap_brokers_public_sasl_scram(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicTls")
    def bootstrap_brokers_public_tls(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslIam")
    def bootstrap_brokers_sasl_iam(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslScram")
    def bootstrap_brokers_sasl_scram(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersTls")
    def bootstrap_brokers_tls(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="brokerNodeGroupInfos")
    def broker_node_group_infos(
        self,
    ) -> Sequence[outputs.GetClusterBrokerNodeGroupInfoResult]: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kafkaVersion")
    def kafka_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zookeeperConnectString")
    def zookeeper_connect_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="zookeeperConnectStringTls")
    def zookeeper_connect_string_tls(self) -> _builtins.str: ...

class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): ...

def get_cluster(
    cluster_name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterResult: ...
def get_cluster_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterResult]: ...
