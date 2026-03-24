

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterBrokerNodeGroupInfoArgs', 'ClusterBrokerNodeGroupInfoArgsDict', 'ClusterBrokerNodeGroupInfoConnectivityInfoArgs', 'ClusterBrokerNodeGroupInfoConnectivityInfoArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'ClusterBrokerNodeGroupInfoStorageInfoArgs', 'ClusterBrokerNodeGroupInfoStorageInfoArgsDict', ..., ..., ..., ..., 'ClusterClientAuthenticationArgs', 'ClusterClientAuthenticationArgsDict', 'ClusterClientAuthenticationSaslArgs', 'ClusterClientAuthenticationSaslArgsDict', 'ClusterClientAuthenticationTlsArgs', 'ClusterClientAuthenticationTlsArgsDict', 'ClusterConfigurationInfoArgs', 'ClusterConfigurationInfoArgsDict', 'ClusterEncryptionInfoArgs', 'ClusterEncryptionInfoArgsDict', 'ClusterEncryptionInfoEncryptionInTransitArgs', 'ClusterEncryptionInfoEncryptionInTransitArgsDict', 'ClusterLoggingInfoArgs', 'ClusterLoggingInfoArgsDict', 'ClusterLoggingInfoBrokerLogsArgs', 'ClusterLoggingInfoBrokerLogsArgsDict', 'ClusterLoggingInfoBrokerLogsCloudwatchLogsArgs', 'ClusterLoggingInfoBrokerLogsCloudwatchLogsArgsDict', 'ClusterLoggingInfoBrokerLogsFirehoseArgs', 'ClusterLoggingInfoBrokerLogsFirehoseArgsDict', 'ClusterLoggingInfoBrokerLogsS3Args', 'ClusterLoggingInfoBrokerLogsS3ArgsDict', 'ClusterOpenMonitoringArgs', 'ClusterOpenMonitoringArgsDict', 'ClusterOpenMonitoringPrometheusArgs', 'ClusterOpenMonitoringPrometheusArgsDict', 'ClusterOpenMonitoringPrometheusJmxExporterArgs', 'ClusterOpenMonitoringPrometheusJmxExporterArgsDict', 'ClusterOpenMonitoringPrometheusNodeExporterArgs', ..., 'ClusterRebalancingArgs', 'ClusterRebalancingArgsDict', 'ReplicatorKafkaClusterArgs', 'ReplicatorKafkaClusterArgsDict', 'ReplicatorKafkaClusterAmazonMskClusterArgs', 'ReplicatorKafkaClusterAmazonMskClusterArgsDict', 'ReplicatorKafkaClusterVpcConfigArgs', 'ReplicatorKafkaClusterVpcConfigArgsDict', 'ReplicatorReplicationInfoListArgs', 'ReplicatorReplicationInfoListArgsDict', ..., ..., 'ReplicatorReplicationInfoListTopicReplicationArgs', ..., ..., ..., ..., ..., 'ServerlessClusterClientAuthenticationArgs', 'ServerlessClusterClientAuthenticationArgsDict', 'ServerlessClusterClientAuthenticationSaslArgs', 'ServerlessClusterClientAuthenticationSaslArgsDict', 'ServerlessClusterClientAuthenticationSaslIamArgs', ..., 'ServerlessClusterVpcConfigArgs', 'ServerlessClusterVpcConfigArgsDict']
class ClusterBrokerNodeGroupInfoArgsDict(TypedDict):
    client_subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    instance_type: pulumi.Input[_builtins.str]
    security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    az_distribution: NotRequired[pulumi.Input[_builtins.str]]
    connectivity_info: NotRequired[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoArgsDict]]
    storage_info: NotRequired[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoArgsDict]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoArgs:
    def __init__(__self__, *, client_subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], instance_type: pulumi.Input[_builtins.str], security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], az_distribution: Optional[pulumi.Input[_builtins.str]] = ..., connectivity_info: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoArgs]] = ..., storage_info: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSubnets")
    def client_subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @client_subnets.setter
    def client_subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azDistribution")
    def az_distribution(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @az_distribution.setter
    def az_distribution(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityInfo")
    def connectivity_info(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoArgs]]:
        
        ...
    
    @connectivity_info.setter
    def connectivity_info(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageInfo")
    def storage_info(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoArgs]]:
        
        ...
    
    @storage_info.setter
    def storage_info(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoArgs]]): # -> None:
        ...
    


class ClusterBrokerNodeGroupInfoConnectivityInfoArgsDict(TypedDict):
    public_access: NotRequired[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessArgsDict]]
    vpc_connectivity: NotRequired[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityArgsDict]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoConnectivityInfoArgs:
    def __init__(__self__, *, public_access: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessArgs]] = ..., vpc_connectivity: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessArgs]]:
        
        ...
    
    @public_access.setter
    def public_access(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnectivity")
    def vpc_connectivity(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityArgs]]:
        
        ...
    
    @vpc_connectivity.setter
    def vpc_connectivity(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityArgs]]): # -> None:
        ...
    


class ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityArgsDict(TypedDict):
    client_authentication: NotRequired[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationArgsDict]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityArgs:
    def __init__(__self__, *, client_authentication: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationArgs]]:
        
        ...
    
    @client_authentication.setter
    def client_authentication(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationArgs]]): # -> None:
        ...
    


class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationArgsDict(TypedDict):
    sasl: NotRequired[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslArgsDict]]
    tls: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationArgs:
    def __init__(__self__, *, sasl: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslArgs]] = ..., tls: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sasl(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslArgs]]:
        
        ...
    
    @sasl.setter
    def sasl(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tls.setter
    def tls(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslArgsDict(TypedDict):
    iam: NotRequired[pulumi.Input[_builtins.bool]]
    scram: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoConnectivityInfoVpcConnectivityClientAuthenticationSaslArgs:
    def __init__(__self__, *, iam: Optional[pulumi.Input[_builtins.bool]] = ..., scram: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iam(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @iam.setter
    def iam(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scram(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @scram.setter
    def scram(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ClusterBrokerNodeGroupInfoStorageInfoArgsDict(TypedDict):
    ebs_storage_info: NotRequired[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoArgsDict]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoStorageInfoArgs:
    def __init__(__self__, *, ebs_storage_info: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsStorageInfo")
    def ebs_storage_info(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoArgs]]:
        
        ...
    
    @ebs_storage_info.setter
    def ebs_storage_info(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoArgs]]): # -> None:
        ...
    


class ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoArgsDict(TypedDict):
    provisioned_throughput: NotRequired[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputArgsDict]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoArgs:
    def __init__(__self__, *, provisioned_throughput: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputArgs]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputArgs]]:
        
        ...
    
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    volume_throughput: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., volume_throughput: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeThroughput")
    def volume_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_throughput.setter
    def volume_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ClusterClientAuthenticationArgsDict(TypedDict):
    sasl: NotRequired[pulumi.Input[ClusterClientAuthenticationSaslArgsDict]]
    tls: NotRequired[pulumi.Input[ClusterClientAuthenticationTlsArgsDict]]
    unauthenticated: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ClusterClientAuthenticationArgs:
    def __init__(__self__, *, sasl: Optional[pulumi.Input[ClusterClientAuthenticationSaslArgs]] = ..., tls: Optional[pulumi.Input[ClusterClientAuthenticationTlsArgs]] = ..., unauthenticated: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sasl(self) -> Optional[pulumi.Input[ClusterClientAuthenticationSaslArgs]]:
        
        ...
    
    @sasl.setter
    def sasl(self, value: Optional[pulumi.Input[ClusterClientAuthenticationSaslArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input[ClusterClientAuthenticationTlsArgs]]:
        
        ...
    
    @tls.setter
    def tls(self, value: Optional[pulumi.Input[ClusterClientAuthenticationTlsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unauthenticated(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @unauthenticated.setter
    def unauthenticated(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ClusterClientAuthenticationSaslArgsDict(TypedDict):
    iam: NotRequired[pulumi.Input[_builtins.bool]]
    scram: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ClusterClientAuthenticationSaslArgs:
    def __init__(__self__, *, iam: Optional[pulumi.Input[_builtins.bool]] = ..., scram: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iam(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @iam.setter
    def iam(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scram(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @scram.setter
    def scram(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ClusterClientAuthenticationTlsArgsDict(TypedDict):
    certificate_authority_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ClusterClientAuthenticationTlsArgs:
    def __init__(__self__, *, certificate_authority_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @certificate_authority_arns.setter
    def certificate_authority_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ClusterConfigurationInfoArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    revision: pulumi.Input[_builtins.int]


@pulumi.input_type
class ClusterConfigurationInfoArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str], revision: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @revision.setter
    def revision(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class ClusterEncryptionInfoArgsDict(TypedDict):
    encryption_at_rest_kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    encryption_in_transit: NotRequired[pulumi.Input[ClusterEncryptionInfoEncryptionInTransitArgsDict]]


@pulumi.input_type
class ClusterEncryptionInfoArgs:
    def __init__(__self__, *, encryption_at_rest_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., encryption_in_transit: Optional[pulumi.Input[ClusterEncryptionInfoEncryptionInTransitArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtRestKmsKeyArn")
    def encryption_at_rest_kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_at_rest_kms_key_arn.setter
    def encryption_at_rest_kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionInTransit")
    def encryption_in_transit(self) -> Optional[pulumi.Input[ClusterEncryptionInfoEncryptionInTransitArgs]]:
        
        ...
    
    @encryption_in_transit.setter
    def encryption_in_transit(self, value: Optional[pulumi.Input[ClusterEncryptionInfoEncryptionInTransitArgs]]): # -> None:
        ...
    


class ClusterEncryptionInfoEncryptionInTransitArgsDict(TypedDict):
    client_broker: NotRequired[pulumi.Input[_builtins.str]]
    in_cluster: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ClusterEncryptionInfoEncryptionInTransitArgs:
    def __init__(__self__, *, client_broker: Optional[pulumi.Input[_builtins.str]] = ..., in_cluster: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientBroker")
    def client_broker(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_broker.setter
    def client_broker(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inCluster")
    def in_cluster(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @in_cluster.setter
    def in_cluster(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ClusterLoggingInfoArgsDict(TypedDict):
    broker_logs: pulumi.Input[ClusterLoggingInfoBrokerLogsArgsDict]


@pulumi.input_type
class ClusterLoggingInfoArgs:
    def __init__(__self__, *, broker_logs: pulumi.Input[ClusterLoggingInfoBrokerLogsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerLogs")
    def broker_logs(self) -> pulumi.Input[ClusterLoggingInfoBrokerLogsArgs]:
        
        ...
    
    @broker_logs.setter
    def broker_logs(self, value: pulumi.Input[ClusterLoggingInfoBrokerLogsArgs]): # -> None:
        ...
    


class ClusterLoggingInfoBrokerLogsArgsDict(TypedDict):
    cloudwatch_logs: NotRequired[pulumi.Input[ClusterLoggingInfoBrokerLogsCloudwatchLogsArgsDict]]
    firehose: NotRequired[pulumi.Input[ClusterLoggingInfoBrokerLogsFirehoseArgsDict]]
    s3: NotRequired[pulumi.Input[ClusterLoggingInfoBrokerLogsS3ArgsDict]]


@pulumi.input_type
class ClusterLoggingInfoBrokerLogsArgs:
    def __init__(__self__, *, cloudwatch_logs: Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsCloudwatchLogsArgs]] = ..., firehose: Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsFirehoseArgs]] = ..., s3: Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsS3Args]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsCloudwatchLogsArgs]]:
        
        ...
    
    @cloudwatch_logs.setter
    def cloudwatch_logs(self, value: Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsCloudwatchLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def firehose(self) -> Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsFirehoseArgs]]:
        
        ...
    
    @firehose.setter
    def firehose(self, value: Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsFirehoseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsS3Args]]:
        
        ...
    
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[ClusterLoggingInfoBrokerLogsS3Args]]): # -> None:
        ...
    


class ClusterLoggingInfoBrokerLogsCloudwatchLogsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    log_group: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterLoggingInfoBrokerLogsCloudwatchLogsArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], log_group: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group.setter
    def log_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterLoggingInfoBrokerLogsFirehoseArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    delivery_stream: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterLoggingInfoBrokerLogsFirehoseArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], delivery_stream: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryStream")
    def delivery_stream(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_stream.setter
    def delivery_stream(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterLoggingInfoBrokerLogsS3ArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterLoggingInfoBrokerLogsS3Args:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], bucket: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterOpenMonitoringArgsDict(TypedDict):
    prometheus: pulumi.Input[ClusterOpenMonitoringPrometheusArgsDict]


@pulumi.input_type
class ClusterOpenMonitoringArgs:
    def __init__(__self__, *, prometheus: pulumi.Input[ClusterOpenMonitoringPrometheusArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prometheus(self) -> pulumi.Input[ClusterOpenMonitoringPrometheusArgs]:
        
        ...
    
    @prometheus.setter
    def prometheus(self, value: pulumi.Input[ClusterOpenMonitoringPrometheusArgs]): # -> None:
        ...
    


class ClusterOpenMonitoringPrometheusArgsDict(TypedDict):
    jmx_exporter: NotRequired[pulumi.Input[ClusterOpenMonitoringPrometheusJmxExporterArgsDict]]
    node_exporter: NotRequired[pulumi.Input[ClusterOpenMonitoringPrometheusNodeExporterArgsDict]]


@pulumi.input_type
class ClusterOpenMonitoringPrometheusArgs:
    def __init__(__self__, *, jmx_exporter: Optional[pulumi.Input[ClusterOpenMonitoringPrometheusJmxExporterArgs]] = ..., node_exporter: Optional[pulumi.Input[ClusterOpenMonitoringPrometheusNodeExporterArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jmxExporter")
    def jmx_exporter(self) -> Optional[pulumi.Input[ClusterOpenMonitoringPrometheusJmxExporterArgs]]:
        
        ...
    
    @jmx_exporter.setter
    def jmx_exporter(self, value: Optional[pulumi.Input[ClusterOpenMonitoringPrometheusJmxExporterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeExporter")
    def node_exporter(self) -> Optional[pulumi.Input[ClusterOpenMonitoringPrometheusNodeExporterArgs]]:
        
        ...
    
    @node_exporter.setter
    def node_exporter(self, value: Optional[pulumi.Input[ClusterOpenMonitoringPrometheusNodeExporterArgs]]): # -> None:
        ...
    


class ClusterOpenMonitoringPrometheusJmxExporterArgsDict(TypedDict):
    enabled_in_broker: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ClusterOpenMonitoringPrometheusJmxExporterArgs:
    def __init__(__self__, *, enabled_in_broker: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledInBroker")
    def enabled_in_broker(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled_in_broker.setter
    def enabled_in_broker(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ClusterOpenMonitoringPrometheusNodeExporterArgsDict(TypedDict):
    enabled_in_broker: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ClusterOpenMonitoringPrometheusNodeExporterArgs:
    def __init__(__self__, *, enabled_in_broker: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledInBroker")
    def enabled_in_broker(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled_in_broker.setter
    def enabled_in_broker(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ClusterRebalancingArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClusterRebalancingArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ReplicatorKafkaClusterArgsDict(TypedDict):
    amazon_msk_cluster: pulumi.Input[ReplicatorKafkaClusterAmazonMskClusterArgsDict]
    vpc_config: pulumi.Input[ReplicatorKafkaClusterVpcConfigArgsDict]


@pulumi.input_type
class ReplicatorKafkaClusterArgs:
    def __init__(__self__, *, amazon_msk_cluster: pulumi.Input[ReplicatorKafkaClusterAmazonMskClusterArgs], vpc_config: pulumi.Input[ReplicatorKafkaClusterVpcConfigArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonMskCluster")
    def amazon_msk_cluster(self) -> pulumi.Input[ReplicatorKafkaClusterAmazonMskClusterArgs]:
        
        ...
    
    @amazon_msk_cluster.setter
    def amazon_msk_cluster(self, value: pulumi.Input[ReplicatorKafkaClusterAmazonMskClusterArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Input[ReplicatorKafkaClusterVpcConfigArgs]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: pulumi.Input[ReplicatorKafkaClusterVpcConfigArgs]): # -> None:
        ...
    


class ReplicatorKafkaClusterAmazonMskClusterArgsDict(TypedDict):
    msk_cluster_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ReplicatorKafkaClusterAmazonMskClusterArgs:
    def __init__(__self__, *, msk_cluster_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mskClusterArn")
    def msk_cluster_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @msk_cluster_arn.setter
    def msk_cluster_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ReplicatorKafkaClusterVpcConfigArgsDict(TypedDict):
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    security_groups_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ReplicatorKafkaClusterVpcConfigArgs:
    def __init__(__self__, *, subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], security_groups_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupsIds")
    def security_groups_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups_ids.setter
    def security_groups_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ReplicatorReplicationInfoListArgsDict(TypedDict):
    consumer_group_replications: pulumi.Input[Sequence[pulumi.Input[ReplicatorReplicationInfoListConsumerGroupReplicationArgsDict]]]
    source_kafka_cluster_arn: pulumi.Input[_builtins.str]
    target_compression_type: pulumi.Input[_builtins.str]
    target_kafka_cluster_arn: pulumi.Input[_builtins.str]
    topic_replications: pulumi.Input[Sequence[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationArgsDict]]]
    source_kafka_cluster_alias: NotRequired[pulumi.Input[_builtins.str]]
    target_kafka_cluster_alias: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReplicatorReplicationInfoListArgs:
    def __init__(__self__, *, consumer_group_replications: pulumi.Input[Sequence[pulumi.Input[ReplicatorReplicationInfoListConsumerGroupReplicationArgs]]], source_kafka_cluster_arn: pulumi.Input[_builtins.str], target_compression_type: pulumi.Input[_builtins.str], target_kafka_cluster_arn: pulumi.Input[_builtins.str], topic_replications: pulumi.Input[Sequence[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationArgs]]], source_kafka_cluster_alias: Optional[pulumi.Input[_builtins.str]] = ..., target_kafka_cluster_alias: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroupReplications")
    def consumer_group_replications(self) -> pulumi.Input[Sequence[pulumi.Input[ReplicatorReplicationInfoListConsumerGroupReplicationArgs]]]:
        
        ...
    
    @consumer_group_replications.setter
    def consumer_group_replications(self, value: pulumi.Input[Sequence[pulumi.Input[ReplicatorReplicationInfoListConsumerGroupReplicationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceKafkaClusterArn")
    def source_kafka_cluster_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_kafka_cluster_arn.setter
    def source_kafka_cluster_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCompressionType")
    def target_compression_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_compression_type.setter
    def target_compression_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetKafkaClusterArn")
    def target_kafka_cluster_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_kafka_cluster_arn.setter
    def target_kafka_cluster_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicReplications")
    def topic_replications(self) -> pulumi.Input[Sequence[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationArgs]]]:
        
        ...
    
    @topic_replications.setter
    def topic_replications(self, value: pulumi.Input[Sequence[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceKafkaClusterAlias")
    def source_kafka_cluster_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @source_kafka_cluster_alias.setter
    def source_kafka_cluster_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetKafkaClusterAlias")
    def target_kafka_cluster_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @target_kafka_cluster_alias.setter
    def target_kafka_cluster_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ReplicatorReplicationInfoListConsumerGroupReplicationArgsDict(TypedDict):
    consumer_groups_to_replicates: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    consumer_groups_to_excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    detect_and_copy_new_consumer_groups: NotRequired[pulumi.Input[_builtins.bool]]
    synchronise_consumer_group_offsets: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ReplicatorReplicationInfoListConsumerGroupReplicationArgs:
    def __init__(__self__, *, consumer_groups_to_replicates: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], consumer_groups_to_excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., detect_and_copy_new_consumer_groups: Optional[pulumi.Input[_builtins.bool]] = ..., synchronise_consumer_group_offsets: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroupsToReplicates")
    def consumer_groups_to_replicates(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @consumer_groups_to_replicates.setter
    def consumer_groups_to_replicates(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroupsToExcludes")
    def consumer_groups_to_excludes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @consumer_groups_to_excludes.setter
    def consumer_groups_to_excludes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectAndCopyNewConsumerGroups")
    def detect_and_copy_new_consumer_groups(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @detect_and_copy_new_consumer_groups.setter
    def detect_and_copy_new_consumer_groups(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchroniseConsumerGroupOffsets")
    def synchronise_consumer_group_offsets(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @synchronise_consumer_group_offsets.setter
    def synchronise_consumer_group_offsets(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ReplicatorReplicationInfoListTopicReplicationArgsDict(TypedDict):
    topics_to_replicates: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    copy_access_control_lists_for_topics: NotRequired[pulumi.Input[_builtins.bool]]
    copy_topic_configurations: NotRequired[pulumi.Input[_builtins.bool]]
    detect_and_copy_new_topics: NotRequired[pulumi.Input[_builtins.bool]]
    starting_position: NotRequired[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationStartingPositionArgsDict]]
    topic_name_configuration: NotRequired[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationTopicNameConfigurationArgsDict]]
    topics_to_excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ReplicatorReplicationInfoListTopicReplicationArgs:
    def __init__(__self__, *, topics_to_replicates: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], copy_access_control_lists_for_topics: Optional[pulumi.Input[_builtins.bool]] = ..., copy_topic_configurations: Optional[pulumi.Input[_builtins.bool]] = ..., detect_and_copy_new_topics: Optional[pulumi.Input[_builtins.bool]] = ..., starting_position: Optional[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationStartingPositionArgs]] = ..., topic_name_configuration: Optional[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationTopicNameConfigurationArgs]] = ..., topics_to_excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicsToReplicates")
    def topics_to_replicates(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @topics_to_replicates.setter
    def topics_to_replicates(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyAccessControlListsForTopics")
    def copy_access_control_lists_for_topics(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_access_control_lists_for_topics.setter
    def copy_access_control_lists_for_topics(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTopicConfigurations")
    def copy_topic_configurations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_topic_configurations.setter
    def copy_topic_configurations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectAndCopyNewTopics")
    def detect_and_copy_new_topics(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @detect_and_copy_new_topics.setter
    def detect_and_copy_new_topics(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationStartingPositionArgs]]:
        
        ...
    
    @starting_position.setter
    def starting_position(self, value: Optional[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationStartingPositionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicNameConfiguration")
    def topic_name_configuration(self) -> Optional[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationTopicNameConfigurationArgs]]:
        
        ...
    
    @topic_name_configuration.setter
    def topic_name_configuration(self, value: Optional[pulumi.Input[ReplicatorReplicationInfoListTopicReplicationTopicNameConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicsToExcludes")
    def topics_to_excludes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @topics_to_excludes.setter
    def topics_to_excludes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ReplicatorReplicationInfoListTopicReplicationStartingPositionArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReplicatorReplicationInfoListTopicReplicationStartingPositionArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ReplicatorReplicationInfoListTopicReplicationTopicNameConfigurationArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReplicatorReplicationInfoListTopicReplicationTopicNameConfigurationArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServerlessClusterClientAuthenticationArgsDict(TypedDict):
    sasl: pulumi.Input[ServerlessClusterClientAuthenticationSaslArgsDict]


@pulumi.input_type
class ServerlessClusterClientAuthenticationArgs:
    def __init__(__self__, *, sasl: pulumi.Input[ServerlessClusterClientAuthenticationSaslArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sasl(self) -> pulumi.Input[ServerlessClusterClientAuthenticationSaslArgs]:
        
        ...
    
    @sasl.setter
    def sasl(self, value: pulumi.Input[ServerlessClusterClientAuthenticationSaslArgs]): # -> None:
        ...
    


class ServerlessClusterClientAuthenticationSaslArgsDict(TypedDict):
    iam: pulumi.Input[ServerlessClusterClientAuthenticationSaslIamArgsDict]


@pulumi.input_type
class ServerlessClusterClientAuthenticationSaslArgs:
    def __init__(__self__, *, iam: pulumi.Input[ServerlessClusterClientAuthenticationSaslIamArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iam(self) -> pulumi.Input[ServerlessClusterClientAuthenticationSaslIamArgs]:
        
        ...
    
    @iam.setter
    def iam(self, value: pulumi.Input[ServerlessClusterClientAuthenticationSaslIamArgs]): # -> None:
        ...
    


class ServerlessClusterClientAuthenticationSaslIamArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ServerlessClusterClientAuthenticationSaslIamArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ServerlessClusterVpcConfigArgsDict(TypedDict):
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ServerlessClusterVpcConfigArgs:
    def __init__(__self__, *, subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


