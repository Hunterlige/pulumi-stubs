import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterBrokerNodeGroupInfo",
    "ClusterBrokerNodeGroupInfoConnectivityInfo",
    ...,
    ...,
    ...,
    ...,
    "ClusterBrokerNodeGroupInfoStorageInfo",
    ...,
    ...,
    "ClusterClientAuthentication",
    "ClusterClientAuthenticationSasl",
    "ClusterClientAuthenticationTls",
    "ClusterConfigurationInfo",
    "ClusterEncryptionInfo",
    "ClusterEncryptionInfoEncryptionInTransit",
    "ClusterLoggingInfo",
    "ClusterLoggingInfoBrokerLogs",
    "ClusterLoggingInfoBrokerLogsCloudwatchLogs",
    "ClusterLoggingInfoBrokerLogsFirehose",
    "ClusterLoggingInfoBrokerLogsS3",
    "ClusterOpenMonitoring",
    "ClusterOpenMonitoringPrometheus",
    "ClusterOpenMonitoringPrometheusJmxExporter",
    "ClusterOpenMonitoringPrometheusNodeExporter",
    "ClusterRebalancing",
    "ReplicatorKafkaCluster",
    "ReplicatorKafkaClusterAmazonMskCluster",
    "ReplicatorKafkaClusterVpcConfig",
    "ReplicatorReplicationInfoList",
    ...,
    "ReplicatorReplicationInfoListTopicReplication",
    ...,
    ...,
    "ServerlessClusterClientAuthentication",
    "ServerlessClusterClientAuthenticationSasl",
    "ServerlessClusterClientAuthenticationSaslIam",
    "ServerlessClusterVpcConfig",
    "GetBrokerNodesNodeInfoListResult",
    "GetClusterBrokerNodeGroupInfoResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterBrokerNodeGroupInfoStorageInfoResult",
    ...,
    ...,
]

@pulumi.output_type
class ClusterBrokerNodeGroupInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_subnets: Sequence[_builtins.str],
        instance_type: _builtins.str,
        security_groups: Sequence[_builtins.str],
        az_distribution: Optional[_builtins.str] = ...,
        connectivity_info: Optional[
            outputs.ClusterBrokerNodeGroupInfoConnectivityInfo
        ] = ...,
        storage_info: Optional[outputs.ClusterBrokerNodeGroupInfoStorageInfo] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSubnets")
    def client_subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azDistribution")
    def az_distribution(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectivityInfo")
    def connectivity_info(
        self,
    ) -> Optional[outputs.ClusterBrokerNodeGroupInfoConnectivityInfo]: ...
    @_builtins.property
    @pulumi.getter(name="storageInfo")
    def storage_info(
        self,
    ) -> Optional[outputs.ClusterBrokerNodeGroupInfoStorageInfo]: ...

@pulumi.output_type
class ClusterBrokerNodeGroupInfoConnectivityInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        public_access: Optional[
            outputs.ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess
        ] = ...,
        vpc_connectivity: Optional[
            outputs.ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivity
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicAccess")
    def public_access(
        self,
    ) -> Optional[outputs.ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectivity")
    def vpc_connectivity(
        self,
    ) -> Optional[
        outputs.ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivity
    ]: ...

@pulumi.output_type
class ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_authentication: Optional[
            outputs.ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthentication
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(
        self,
    ) -> Optional[
        outputs.ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthentication
    ]: ...

@pulumi.output_type
class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthentication(
    dict
):
    def __init__(
        __self__,
        *,
        sasl: Optional[
            outputs.ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSasl
        ] = ...,
        tls: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def sasl(
        self,
    ) -> Optional[
        outputs.ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSasl
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSasl(
    dict
):
    def __init__(
        __self__,
        *,
        iam: Optional[_builtins.bool] = ...,
        scram: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iam(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scram(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterBrokerNodeGroupInfoStorageInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ebs_storage_info: Optional[
            outputs.ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsStorageInfo")
    def ebs_storage_info(
        self,
    ) -> Optional[outputs.ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo]: ...

@pulumi.output_type
class ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioned_throughput: Optional[
            outputs.ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput
        ] = ...,
        volume_size: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(
        self,
    ) -> Optional[
        outputs.ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput
    ]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        volume_throughput: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="volumeThroughput")
    def volume_throughput(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterClientAuthentication(dict):
    def __init__(
        __self__,
        *,
        sasl: Optional[outputs.ClusterClientAuthenticationSasl] = ...,
        tls: Optional[outputs.ClusterClientAuthenticationTls] = ...,
        unauthenticated: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def sasl(self) -> Optional[outputs.ClusterClientAuthenticationSasl]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[outputs.ClusterClientAuthenticationTls]: ...
    @_builtins.property
    @pulumi.getter
    def unauthenticated(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterClientAuthenticationSasl(dict):
    def __init__(
        __self__,
        *,
        iam: Optional[_builtins.bool] = ...,
        scram: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iam(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scram(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterClientAuthenticationTls(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_authority_arns: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterConfigurationInfo(dict):
    def __init__(__self__, *, arn: _builtins.str, revision: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterEncryptionInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_at_rest_kms_key_arn: Optional[_builtins.str] = ...,
        encryption_in_transit: Optional[
            outputs.ClusterEncryptionInfoEncryptionInTransit
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtRestKmsKeyArn")
    def encryption_at_rest_kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionInTransit")
    def encryption_in_transit(
        self,
    ) -> Optional[outputs.ClusterEncryptionInfoEncryptionInTransit]: ...

@pulumi.output_type
class ClusterEncryptionInfoEncryptionInTransit(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_broker: Optional[_builtins.str] = ...,
        in_cluster: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientBroker")
    def client_broker(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inCluster")
    def in_cluster(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterLoggingInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, broker_logs: outputs.ClusterLoggingInfoBrokerLogs
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="brokerLogs")
    def broker_logs(self) -> outputs.ClusterLoggingInfoBrokerLogs: ...

@pulumi.output_type
class ClusterLoggingInfoBrokerLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            outputs.ClusterLoggingInfoBrokerLogsCloudwatchLogs
        ] = ...,
        firehose: Optional[outputs.ClusterLoggingInfoBrokerLogsFirehose] = ...,
        s3: Optional[outputs.ClusterLoggingInfoBrokerLogsS3] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[outputs.ClusterLoggingInfoBrokerLogsCloudwatchLogs]: ...
    @_builtins.property
    @pulumi.getter
    def firehose(self) -> Optional[outputs.ClusterLoggingInfoBrokerLogsFirehose]: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[outputs.ClusterLoggingInfoBrokerLogsS3]: ...

@pulumi.output_type
class ClusterLoggingInfoBrokerLogsCloudwatchLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enabled: _builtins.bool, log_group: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterLoggingInfoBrokerLogsFirehose(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        delivery_stream: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStream")
    def delivery_stream(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterLoggingInfoBrokerLogsS3(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        bucket: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterOpenMonitoring(dict):
    def __init__(
        __self__, *, prometheus: outputs.ClusterOpenMonitoringPrometheus
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prometheus(self) -> outputs.ClusterOpenMonitoringPrometheus: ...

@pulumi.output_type
class ClusterOpenMonitoringPrometheus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        jmx_exporter: Optional[
            outputs.ClusterOpenMonitoringPrometheusJmxExporter
        ] = ...,
        node_exporter: Optional[
            outputs.ClusterOpenMonitoringPrometheusNodeExporter
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jmxExporter")
    def jmx_exporter(
        self,
    ) -> Optional[outputs.ClusterOpenMonitoringPrometheusJmxExporter]: ...
    @_builtins.property
    @pulumi.getter(name="nodeExporter")
    def node_exporter(
        self,
    ) -> Optional[outputs.ClusterOpenMonitoringPrometheusNodeExporter]: ...

@pulumi.output_type
class ClusterOpenMonitoringPrometheusJmxExporter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enabled_in_broker: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledInBroker")
    def enabled_in_broker(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterOpenMonitoringPrometheusNodeExporter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enabled_in_broker: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledInBroker")
    def enabled_in_broker(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterRebalancing(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class ReplicatorKafkaCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amazon_msk_cluster: outputs.ReplicatorKafkaClusterAmazonMskCluster,
        vpc_config: outputs.ReplicatorKafkaClusterVpcConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonMskCluster")
    def amazon_msk_cluster(self) -> outputs.ReplicatorKafkaClusterAmazonMskCluster: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> outputs.ReplicatorKafkaClusterVpcConfig: ...

@pulumi.output_type
class ReplicatorKafkaClusterAmazonMskCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, msk_cluster_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mskClusterArn")
    def msk_cluster_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ReplicatorKafkaClusterVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnet_ids: Sequence[_builtins.str],
        security_groups_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupsIds")
    def security_groups_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ReplicatorReplicationInfoList(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_group_replications: Sequence[
            outputs.ReplicatorReplicationInfoListConsumerGroupReplication
        ],
        source_kafka_cluster_arn: _builtins.str,
        target_compression_type: _builtins.str,
        target_kafka_cluster_arn: _builtins.str,
        topic_replications: Sequence[
            outputs.ReplicatorReplicationInfoListTopicReplication
        ],
        source_kafka_cluster_alias: Optional[_builtins.str] = ...,
        target_kafka_cluster_alias: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupReplications")
    def consumer_group_replications(
        self,
    ) -> Sequence[outputs.ReplicatorReplicationInfoListConsumerGroupReplication]: ...
    @_builtins.property
    @pulumi.getter(name="sourceKafkaClusterArn")
    def source_kafka_cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetCompressionType")
    def target_compression_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetKafkaClusterArn")
    def target_kafka_cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="topicReplications")
    def topic_replications(
        self,
    ) -> Sequence[outputs.ReplicatorReplicationInfoListTopicReplication]: ...
    @_builtins.property
    @pulumi.getter(name="sourceKafkaClusterAlias")
    def source_kafka_cluster_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetKafkaClusterAlias")
    def target_kafka_cluster_alias(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReplicatorReplicationInfoListConsumerGroupReplication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_groups_to_replicates: Sequence[_builtins.str],
        consumer_groups_to_excludes: Optional[Sequence[_builtins.str]] = ...,
        detect_and_copy_new_consumer_groups: Optional[_builtins.bool] = ...,
        synchronise_consumer_group_offsets: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupsToReplicates")
    def consumer_groups_to_replicates(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupsToExcludes")
    def consumer_groups_to_excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="detectAndCopyNewConsumerGroups")
    def detect_and_copy_new_consumer_groups(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="synchroniseConsumerGroupOffsets")
    def synchronise_consumer_group_offsets(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ReplicatorReplicationInfoListTopicReplication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        topics_to_replicates: Sequence[_builtins.str],
        copy_access_control_lists_for_topics: Optional[_builtins.bool] = ...,
        copy_topic_configurations: Optional[_builtins.bool] = ...,
        detect_and_copy_new_topics: Optional[_builtins.bool] = ...,
        starting_position: Optional[
            outputs.ReplicatorReplicationInfoListTopicReplicationStartingPosition
        ] = ...,
        topic_name_configuration: Optional[
            outputs.ReplicatorReplicationInfoListTopicReplicationTopicNameConfiguration
        ] = ...,
        topics_to_excludes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicsToReplicates")
    def topics_to_replicates(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="copyAccessControlListsForTopics")
    def copy_access_control_lists_for_topics(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="copyTopicConfigurations")
    def copy_topic_configurations(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="detectAndCopyNewTopics")
    def detect_and_copy_new_topics(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(
        self,
    ) -> Optional[
        outputs.ReplicatorReplicationInfoListTopicReplicationStartingPosition
    ]: ...
    @_builtins.property
    @pulumi.getter(name="topicNameConfiguration")
    def topic_name_configuration(
        self,
    ) -> Optional[
        outputs.ReplicatorReplicationInfoListTopicReplicationTopicNameConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="topicsToExcludes")
    def topics_to_excludes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ReplicatorReplicationInfoListTopicReplicationStartingPosition(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReplicatorReplicationInfoListTopicReplicationTopicNameConfiguration(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServerlessClusterClientAuthentication(dict):
    def __init__(
        __self__, *, sasl: outputs.ServerlessClusterClientAuthenticationSasl
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def sasl(self) -> outputs.ServerlessClusterClientAuthenticationSasl: ...

@pulumi.output_type
class ServerlessClusterClientAuthenticationSasl(dict):
    def __init__(
        __self__, *, iam: outputs.ServerlessClusterClientAuthenticationSaslIam
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iam(self) -> outputs.ServerlessClusterClientAuthenticationSaslIam: ...

@pulumi.output_type
class ServerlessClusterClientAuthenticationSaslIam(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ServerlessClusterVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnet_ids: Sequence[_builtins.str],
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetBrokerNodesNodeInfoListResult(dict):
    def __init__(
        __self__,
        *,
        attached_eni_id: _builtins.str,
        broker_id: _builtins.float,
        client_subnet: _builtins.str,
        client_vpc_ip_address: _builtins.str,
        endpoints: Sequence[_builtins.str],
        node_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachedEniId")
    def attached_eni_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="brokerId")
    def broker_id(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="clientSubnet")
    def client_subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientVpcIpAddress")
    def client_vpc_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeArn")
    def node_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoResult(dict):
    def __init__(
        __self__,
        *,
        az_distribution: _builtins.str,
        client_subnets: Sequence[_builtins.str],
        connectivity_infos: Sequence[
            outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoResult
        ],
        instance_type: _builtins.str,
        security_groups: Sequence[_builtins.str],
        storage_infos: Sequence[outputs.GetClusterBrokerNodeGroupInfoStorageInfoResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azDistribution")
    def az_distribution(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSubnets")
    def client_subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectivityInfos")
    def connectivity_infos(
        self,
    ) -> Sequence[outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoResult]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageInfos")
    def storage_infos(
        self,
    ) -> Sequence[outputs.GetClusterBrokerNodeGroupInfoStorageInfoResult]: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoConnectivityInfoResult(dict):
    def __init__(
        __self__,
        *,
        public_accesses: Sequence[
            outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessResult
        ],
        vpc_connectivities: Sequence[
            outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicAccesses")
    def public_accesses(
        self,
    ) -> Sequence[
        outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectivities")
    def vpc_connectivities(
        self,
    ) -> Sequence[
        outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityResult
    ]: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessResult(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityResult(dict):
    def __init__(
        __self__,
        *,
        client_authentications: Sequence[
            outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuthentications")
    def client_authentications(
        self,
    ) -> Sequence[
        outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationResult
    ]: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationResult(
    dict
):
    def __init__(
        __self__,
        *,
        sasls: Sequence[
            outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslResult
        ],
        tls: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def sasls(
        self,
    ) -> Sequence[
        outputs.GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslResult(
    dict
):
    def __init__(__self__, *, iam: _builtins.bool, scram: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iam(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def scram(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoStorageInfoResult(dict):
    def __init__(
        __self__,
        *,
        ebs_storage_infos: Sequence[
            outputs.GetClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsStorageInfos")
    def ebs_storage_infos(
        self,
    ) -> Sequence[
        outputs.GetClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoResult
    ]: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoResult(dict):
    def __init__(
        __self__,
        *,
        provisioned_throughputs: Sequence[
            outputs.GetClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputResult
        ],
        volume_size: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputs")
    def provisioned_throughputs(
        self,
    ) -> Sequence[
        outputs.GetClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputResult(
    dict
):
    def __init__(
        __self__, *, enabled: _builtins.bool, volume_throughput: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="volumeThroughput")
    def volume_throughput(self) -> _builtins.int: ...
