

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointCidrOptionsArgs', 'EndpointCidrOptionsArgsDict', 'EndpointCidrOptionsPortRangeArgs', 'EndpointCidrOptionsPortRangeArgsDict', 'EndpointLoadBalancerOptionsArgs', 'EndpointLoadBalancerOptionsArgsDict', 'EndpointLoadBalancerOptionsPortRangeArgs', 'EndpointLoadBalancerOptionsPortRangeArgsDict', 'EndpointNetworkInterfaceOptionsArgs', 'EndpointNetworkInterfaceOptionsArgsDict', 'EndpointNetworkInterfaceOptionsPortRangeArgs', 'EndpointNetworkInterfaceOptionsPortRangeArgsDict', 'EndpointRdsOptionsArgs', 'EndpointRdsOptionsArgsDict', 'EndpointSseSpecificationArgs', 'EndpointSseSpecificationArgsDict', 'GroupSseConfigurationArgs', 'GroupSseConfigurationArgsDict', 'InstanceLoggingConfigurationAccessLogsArgs', 'InstanceLoggingConfigurationAccessLogsArgsDict', ..., ..., ..., ..., 'InstanceLoggingConfigurationAccessLogsS3Args', 'InstanceLoggingConfigurationAccessLogsS3ArgsDict', 'InstanceVerifiedAccessTrustProviderArgs', 'InstanceVerifiedAccessTrustProviderArgsDict', 'TrustProviderDeviceOptionsArgs', 'TrustProviderDeviceOptionsArgsDict', 'TrustProviderNativeApplicationOidcOptionsArgs', 'TrustProviderNativeApplicationOidcOptionsArgsDict', 'TrustProviderOidcOptionsArgs', 'TrustProviderOidcOptionsArgsDict', 'TrustProviderSseSpecificationArgs', 'TrustProviderSseSpecificationArgsDict']
class EndpointCidrOptionsArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]
    port_ranges: pulumi.Input[Sequence[pulumi.Input[EndpointCidrOptionsPortRangeArgsDict]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class EndpointCidrOptionsArgs:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str], port_ranges: pulumi.Input[Sequence[pulumi.Input[EndpointCidrOptionsPortRangeArgs]]], protocol: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> pulumi.Input[Sequence[pulumi.Input[EndpointCidrOptionsPortRangeArgs]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: pulumi.Input[Sequence[pulumi.Input[EndpointCidrOptionsPortRangeArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class EndpointCidrOptionsPortRangeArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]


@pulumi.input_type
class EndpointCidrOptionsPortRangeArgs:
    def __init__(__self__, *, from_port: pulumi.Input[_builtins.int], to_port: pulumi.Input[_builtins.int]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class EndpointLoadBalancerOptionsArgsDict(TypedDict):
    load_balancer_arn: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointLoadBalancerOptionsPortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class EndpointLoadBalancerOptionsArgs:
    def __init__(__self__, *, load_balancer_arn: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointLoadBalancerOptionsPortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @load_balancer_arn.setter
    def load_balancer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointLoadBalancerOptionsPortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointLoadBalancerOptionsPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class EndpointLoadBalancerOptionsPortRangeArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]


@pulumi.input_type
class EndpointLoadBalancerOptionsPortRangeArgs:
    def __init__(__self__, *, from_port: pulumi.Input[_builtins.int], to_port: pulumi.Input[_builtins.int]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class EndpointNetworkInterfaceOptionsArgsDict(TypedDict):
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointNetworkInterfaceOptionsPortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointNetworkInterfaceOptionsArgs:
    def __init__(__self__, *, network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointNetworkInterfaceOptionsPortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointNetworkInterfaceOptionsPortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointNetworkInterfaceOptionsPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointNetworkInterfaceOptionsPortRangeArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]


@pulumi.input_type
class EndpointNetworkInterfaceOptionsPortRangeArgs:
    def __init__(__self__, *, from_port: pulumi.Input[_builtins.int], to_port: pulumi.Input[_builtins.int]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class EndpointRdsOptionsArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    rds_db_cluster_arn: NotRequired[pulumi.Input[_builtins.str]]
    rds_db_instance_arn: NotRequired[pulumi.Input[_builtins.str]]
    rds_db_proxy_arn: NotRequired[pulumi.Input[_builtins.str]]
    rds_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class EndpointRdsOptionsArgs:
    def __init__(__self__, *, port: Optional[pulumi.Input[_builtins.int]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., rds_db_cluster_arn: Optional[pulumi.Input[_builtins.str]] = ..., rds_db_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., rds_db_proxy_arn: Optional[pulumi.Input[_builtins.str]] = ..., rds_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdsDbClusterArn")
    def rds_db_cluster_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @rds_db_cluster_arn.setter
    def rds_db_cluster_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdsDbInstanceArn")
    def rds_db_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @rds_db_instance_arn.setter
    def rds_db_instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdsDbProxyArn")
    def rds_db_proxy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @rds_db_proxy_arn.setter
    def rds_db_proxy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdsEndpoint")
    def rds_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @rds_endpoint.setter
    def rds_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class EndpointSseSpecificationArgsDict(TypedDict):
    customer_managed_key_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointSseSpecificationArgs:
    def __init__(__self__, *, customer_managed_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEnabled")
    def customer_managed_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @customer_managed_key_enabled.setter
    def customer_managed_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GroupSseConfigurationArgsDict(TypedDict):
    customer_managed_key_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GroupSseConfigurationArgs:
    def __init__(__self__, *, customer_managed_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEnabled")
    def customer_managed_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @customer_managed_key_enabled.setter
    def customer_managed_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceLoggingConfigurationAccessLogsArgsDict(TypedDict):
    cloudwatch_logs: NotRequired[pulumi.Input[InstanceLoggingConfigurationAccessLogsCloudwatchLogsArgsDict]]
    include_trust_context: NotRequired[pulumi.Input[_builtins.bool]]
    kinesis_data_firehose: NotRequired[pulumi.Input[InstanceLoggingConfigurationAccessLogsKinesisDataFirehoseArgsDict]]
    log_version: NotRequired[pulumi.Input[_builtins.str]]
    s3: NotRequired[pulumi.Input[InstanceLoggingConfigurationAccessLogsS3ArgsDict]]


@pulumi.input_type
class InstanceLoggingConfigurationAccessLogsArgs:
    def __init__(__self__, *, cloudwatch_logs: Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsCloudwatchLogsArgs]] = ..., include_trust_context: Optional[pulumi.Input[_builtins.bool]] = ..., kinesis_data_firehose: Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsKinesisDataFirehoseArgs]] = ..., log_version: Optional[pulumi.Input[_builtins.str]] = ..., s3: Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsS3Args]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsCloudwatchLogsArgs]]:
        
        ...
    
    @cloudwatch_logs.setter
    def cloudwatch_logs(self, value: Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsCloudwatchLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTrustContext")
    def include_trust_context(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_trust_context.setter
    def include_trust_context(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisDataFirehose")
    def kinesis_data_firehose(self) -> Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsKinesisDataFirehoseArgs]]:
        
        ...
    
    @kinesis_data_firehose.setter
    def kinesis_data_firehose(self, value: Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsKinesisDataFirehoseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logVersion")
    def log_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_version.setter
    def log_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsS3Args]]:
        
        ...
    
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsS3Args]]): # -> None:
        ...
    


class InstanceLoggingConfigurationAccessLogsCloudwatchLogsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    log_group: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceLoggingConfigurationAccessLogsCloudwatchLogsArgs:
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
    


class InstanceLoggingConfigurationAccessLogsKinesisDataFirehoseArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    delivery_stream: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceLoggingConfigurationAccessLogsKinesisDataFirehoseArgs:
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
    


class InstanceLoggingConfigurationAccessLogsS3ArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_owner: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceLoggingConfigurationAccessLogsS3Args:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_owner.setter
    def bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceVerifiedAccessTrustProviderArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    device_trust_provider_type: NotRequired[pulumi.Input[_builtins.str]]
    trust_provider_type: NotRequired[pulumi.Input[_builtins.str]]
    user_trust_provider_type: NotRequired[pulumi.Input[_builtins.str]]
    verified_access_trust_provider_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceVerifiedAccessTrustProviderArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., device_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., user_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., verified_access_trust_provider_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTrustProviderType")
    def device_trust_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_trust_provider_type.setter
    def device_trust_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustProviderType")
    def trust_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_provider_type.setter
    def trust_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTrustProviderType")
    def user_trust_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_trust_provider_type.setter
    def user_trust_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedAccessTrustProviderId")
    def verified_access_trust_provider_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @verified_access_trust_provider_id.setter
    def verified_access_trust_provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TrustProviderDeviceOptionsArgsDict(TypedDict):
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TrustProviderDeviceOptionsArgs:
    def __init__(__self__, *, tenant_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TrustProviderNativeApplicationOidcOptionsArgsDict(TypedDict):
    client_secret: pulumi.Input[_builtins.str]
    authorization_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    public_signing_key_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    token_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    user_info_endpoint: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TrustProviderNativeApplicationOidcOptionsArgs:
    def __init__(__self__, *, client_secret: pulumi.Input[_builtins.str], authorization_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., issuer: Optional[pulumi.Input[_builtins.str]] = ..., public_signing_key_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., token_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., user_info_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicSigningKeyEndpoint")
    def public_signing_key_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @public_signing_key_endpoint.setter
    def public_signing_key_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @user_info_endpoint.setter
    def user_info_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TrustProviderOidcOptionsArgsDict(TypedDict):
    client_secret: pulumi.Input[_builtins.str]
    authorization_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    token_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    user_info_endpoint: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TrustProviderOidcOptionsArgs:
    def __init__(__self__, *, client_secret: pulumi.Input[_builtins.str], authorization_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., issuer: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., token_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., user_info_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @user_info_endpoint.setter
    def user_info_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TrustProviderSseSpecificationArgsDict(TypedDict):
    customer_managed_key_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TrustProviderSseSpecificationArgs:
    def __init__(__self__, *, customer_managed_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEnabled")
    def customer_managed_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @customer_managed_key_enabled.setter
    def customer_managed_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


