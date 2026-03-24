import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectorCapacityArgs",
    "ConnectorCapacityArgsDict",
    "ConnectorCapacityAutoscalingArgs",
    "ConnectorCapacityAutoscalingArgsDict",
    "ConnectorCapacityAutoscalingScaleInPolicyArgs",
    "ConnectorCapacityAutoscalingScaleInPolicyArgsDict",
    "ConnectorCapacityAutoscalingScaleOutPolicyArgs",
    "ConnectorCapacityAutoscalingScaleOutPolicyArgsDict",
    "ConnectorCapacityProvisionedCapacityArgs",
    "ConnectorCapacityProvisionedCapacityArgsDict",
    "ConnectorKafkaClusterArgs",
    "ConnectorKafkaClusterArgsDict",
    "ConnectorKafkaClusterApacheKafkaClusterArgs",
    "ConnectorKafkaClusterApacheKafkaClusterArgsDict",
    "ConnectorKafkaClusterApacheKafkaClusterVpcArgs",
    "ConnectorKafkaClusterApacheKafkaClusterVpcArgsDict",
    "ConnectorKafkaClusterClientAuthenticationArgs",
    "ConnectorKafkaClusterClientAuthenticationArgsDict",
    "ConnectorKafkaClusterEncryptionInTransitArgs",
    "ConnectorKafkaClusterEncryptionInTransitArgsDict",
    "ConnectorLogDeliveryArgs",
    "ConnectorLogDeliveryArgsDict",
    "ConnectorLogDeliveryWorkerLogDeliveryArgs",
    "ConnectorLogDeliveryWorkerLogDeliveryArgsDict",
    ...,
    ...,
    "ConnectorLogDeliveryWorkerLogDeliveryFirehoseArgs",
    ...,
    "ConnectorLogDeliveryWorkerLogDeliveryS3Args",
    "ConnectorLogDeliveryWorkerLogDeliveryS3ArgsDict",
    "ConnectorPluginArgs",
    "ConnectorPluginArgsDict",
    "ConnectorPluginCustomPluginArgs",
    "ConnectorPluginCustomPluginArgsDict",
    "ConnectorWorkerConfigurationArgs",
    "ConnectorWorkerConfigurationArgsDict",
    "CustomPluginLocationArgs",
    "CustomPluginLocationArgsDict",
    "CustomPluginLocationS3Args",
    "CustomPluginLocationS3ArgsDict",
]

class ConnectorCapacityArgsDict(TypedDict):
    autoscaling: NotRequired[pulumi.Input[ConnectorCapacityAutoscalingArgsDict]]
    provisioned_capacity: NotRequired[
        pulumi.Input[ConnectorCapacityProvisionedCapacityArgsDict]
    ]
    ...

@pulumi.input_type
class ConnectorCapacityArgs:
    def __init__(
        __self__,
        *,
        autoscaling: Optional[pulumi.Input[ConnectorCapacityAutoscalingArgs]] = ...,
        provisioned_capacity: Optional[
            pulumi.Input[ConnectorCapacityProvisionedCapacityArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(
        self,
    ) -> Optional[pulumi.Input[ConnectorCapacityAutoscalingArgs]]: ...
    @autoscaling.setter
    def autoscaling(
        self, value: Optional[pulumi.Input[ConnectorCapacityAutoscalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedCapacity")
    def provisioned_capacity(
        self,
    ) -> Optional[pulumi.Input[ConnectorCapacityProvisionedCapacityArgs]]: ...
    @provisioned_capacity.setter
    def provisioned_capacity(
        self, value: Optional[pulumi.Input[ConnectorCapacityProvisionedCapacityArgs]]
    ): ...

class ConnectorCapacityAutoscalingArgsDict(TypedDict):
    max_worker_count: pulumi.Input[_builtins.int]
    min_worker_count: pulumi.Input[_builtins.int]
    mcu_count: NotRequired[pulumi.Input[_builtins.int]]
    scale_in_policy: NotRequired[
        pulumi.Input[ConnectorCapacityAutoscalingScaleInPolicyArgsDict]
    ]
    scale_out_policy: NotRequired[
        pulumi.Input[ConnectorCapacityAutoscalingScaleOutPolicyArgsDict]
    ]
    ...

@pulumi.input_type
class ConnectorCapacityAutoscalingArgs:
    def __init__(
        __self__,
        *,
        max_worker_count: pulumi.Input[_builtins.int],
        min_worker_count: pulumi.Input[_builtins.int],
        mcu_count: Optional[pulumi.Input[_builtins.int]] = ...,
        scale_in_policy: Optional[
            pulumi.Input[ConnectorCapacityAutoscalingScaleInPolicyArgs]
        ] = ...,
        scale_out_policy: Optional[
            pulumi.Input[ConnectorCapacityAutoscalingScaleOutPolicyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxWorkerCount")
    def max_worker_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_worker_count.setter
    def max_worker_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minWorkerCount")
    def min_worker_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_worker_count.setter
    def min_worker_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="mcuCount")
    def mcu_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mcu_count.setter
    def mcu_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scaleInPolicy")
    def scale_in_policy(
        self,
    ) -> Optional[pulumi.Input[ConnectorCapacityAutoscalingScaleInPolicyArgs]]: ...
    @scale_in_policy.setter
    def scale_in_policy(
        self,
        value: Optional[pulumi.Input[ConnectorCapacityAutoscalingScaleInPolicyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleOutPolicy")
    def scale_out_policy(
        self,
    ) -> Optional[pulumi.Input[ConnectorCapacityAutoscalingScaleOutPolicyArgs]]: ...
    @scale_out_policy.setter
    def scale_out_policy(
        self,
        value: Optional[pulumi.Input[ConnectorCapacityAutoscalingScaleOutPolicyArgs]],
    ): ...

class ConnectorCapacityAutoscalingScaleInPolicyArgsDict(TypedDict):
    cpu_utilization_percentage: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ConnectorCapacityAutoscalingScaleInPolicyArgs:
    def __init__(
        __self__,
        *,
        cpu_utilization_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu_utilization_percentage.setter
    def cpu_utilization_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ConnectorCapacityAutoscalingScaleOutPolicyArgsDict(TypedDict):
    cpu_utilization_percentage: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ConnectorCapacityAutoscalingScaleOutPolicyArgs:
    def __init__(
        __self__,
        *,
        cpu_utilization_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu_utilization_percentage.setter
    def cpu_utilization_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ConnectorCapacityProvisionedCapacityArgsDict(TypedDict):
    worker_count: pulumi.Input[_builtins.int]
    mcu_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ConnectorCapacityProvisionedCapacityArgs:
    def __init__(
        __self__,
        *,
        worker_count: pulumi.Input[_builtins.int],
        mcu_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> pulumi.Input[_builtins.int]: ...
    @worker_count.setter
    def worker_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="mcuCount")
    def mcu_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mcu_count.setter
    def mcu_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ConnectorKafkaClusterArgsDict(TypedDict):
    apache_kafka_cluster: pulumi.Input[ConnectorKafkaClusterApacheKafkaClusterArgsDict]
    ...

@pulumi.input_type
class ConnectorKafkaClusterArgs:
    def __init__(
        __self__,
        *,
        apache_kafka_cluster: pulumi.Input[ConnectorKafkaClusterApacheKafkaClusterArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apacheKafkaCluster")
    def apache_kafka_cluster(
        self,
    ) -> pulumi.Input[ConnectorKafkaClusterApacheKafkaClusterArgs]: ...
    @apache_kafka_cluster.setter
    def apache_kafka_cluster(
        self, value: pulumi.Input[ConnectorKafkaClusterApacheKafkaClusterArgs]
    ): ...

class ConnectorKafkaClusterApacheKafkaClusterArgsDict(TypedDict):
    bootstrap_servers: pulumi.Input[_builtins.str]
    vpc: pulumi.Input[ConnectorKafkaClusterApacheKafkaClusterVpcArgsDict]
    ...

@pulumi.input_type
class ConnectorKafkaClusterApacheKafkaClusterArgs:
    def __init__(
        __self__,
        *,
        bootstrap_servers: pulumi.Input[_builtins.str],
        vpc: pulumi.Input[ConnectorKafkaClusterApacheKafkaClusterVpcArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapServers")
    def bootstrap_servers(self) -> pulumi.Input[_builtins.str]: ...
    @bootstrap_servers.setter
    def bootstrap_servers(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> pulumi.Input[ConnectorKafkaClusterApacheKafkaClusterVpcArgs]: ...
    @vpc.setter
    def vpc(
        self, value: pulumi.Input[ConnectorKafkaClusterApacheKafkaClusterVpcArgs]
    ): ...

class ConnectorKafkaClusterApacheKafkaClusterVpcArgsDict(TypedDict):
    security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class ConnectorKafkaClusterApacheKafkaClusterVpcArgs:
    def __init__(
        __self__,
        *,
        security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ConnectorKafkaClusterClientAuthenticationArgsDict(TypedDict):
    authentication_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectorKafkaClusterClientAuthenticationArgs:
    def __init__(
        __self__, *, authentication_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectorKafkaClusterEncryptionInTransitArgsDict(TypedDict):
    encryption_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectorKafkaClusterEncryptionInTransitArgs:
    def __init__(
        __self__, *, encryption_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectorLogDeliveryArgsDict(TypedDict):
    worker_log_delivery: pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryArgsDict]
    ...

@pulumi.input_type
class ConnectorLogDeliveryArgs:
    def __init__(
        __self__,
        *,
        worker_log_delivery: pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workerLogDelivery")
    def worker_log_delivery(
        self,
    ) -> pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryArgs]: ...
    @worker_log_delivery.setter
    def worker_log_delivery(
        self, value: pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryArgs]
    ): ...

class ConnectorLogDeliveryWorkerLogDeliveryArgsDict(TypedDict):
    cloudwatch_logs: NotRequired[
        pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsArgsDict]
    ]
    firehose: NotRequired[
        pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryFirehoseArgsDict]
    ]
    s3: NotRequired[pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryS3ArgsDict]]
    ...

@pulumi.input_type
class ConnectorLogDeliveryWorkerLogDeliveryArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsArgs]
        ] = ...,
        firehose: Optional[
            pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryFirehoseArgs]
        ] = ...,
        s3: Optional[pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryS3Args]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[
        pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsArgs]
    ]: ...
    @cloudwatch_logs.setter
    def cloudwatch_logs(
        self,
        value: Optional[
            pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def firehose(
        self,
    ) -> Optional[pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryFirehoseArgs]]: ...
    @firehose.setter
    def firehose(
        self,
        value: Optional[
            pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryFirehoseArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryS3Args]]: ...
    @s3.setter
    def s3(
        self, value: Optional[pulumi.Input[ConnectorLogDeliveryWorkerLogDeliveryS3Args]]
    ): ...

class ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    log_group: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        log_group: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group.setter
    def log_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectorLogDeliveryWorkerLogDeliveryFirehoseArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    delivery_stream: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectorLogDeliveryWorkerLogDeliveryFirehoseArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        delivery_stream: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryStream")
    def delivery_stream(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_stream.setter
    def delivery_stream(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectorLogDeliveryWorkerLogDeliveryS3ArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectorLogDeliveryWorkerLogDeliveryS3Args:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectorPluginArgsDict(TypedDict):
    custom_plugin: pulumi.Input[ConnectorPluginCustomPluginArgsDict]
    ...

@pulumi.input_type
class ConnectorPluginArgs:
    def __init__(
        __self__, *, custom_plugin: pulumi.Input[ConnectorPluginCustomPluginArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customPlugin")
    def custom_plugin(self) -> pulumi.Input[ConnectorPluginCustomPluginArgs]: ...
    @custom_plugin.setter
    def custom_plugin(self, value: pulumi.Input[ConnectorPluginCustomPluginArgs]): ...

class ConnectorPluginCustomPluginArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    revision: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class ConnectorPluginCustomPluginArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        revision: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Input[_builtins.int]: ...
    @revision.setter
    def revision(self, value: pulumi.Input[_builtins.int]): ...

class ConnectorWorkerConfigurationArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    revision: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class ConnectorWorkerConfigurationArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        revision: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Input[_builtins.int]: ...
    @revision.setter
    def revision(self, value: pulumi.Input[_builtins.int]): ...

class CustomPluginLocationArgsDict(TypedDict):
    s3: pulumi.Input[CustomPluginLocationS3ArgsDict]
    ...

@pulumi.input_type
class CustomPluginLocationArgs:
    def __init__(__self__, *, s3: pulumi.Input[CustomPluginLocationS3Args]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> pulumi.Input[CustomPluginLocationS3Args]: ...
    @s3.setter
    def s3(self, value: pulumi.Input[CustomPluginLocationS3Args]): ...

class CustomPluginLocationS3ArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    file_key: pulumi.Input[_builtins.str]
    object_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CustomPluginLocationS3Args:
    def __init__(
        __self__,
        *,
        bucket_arn: pulumi.Input[_builtins.str],
        file_key: pulumi.Input[_builtins.str],
        object_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> pulumi.Input[_builtins.str]: ...
    @file_key.setter
    def file_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_version.setter
    def object_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
