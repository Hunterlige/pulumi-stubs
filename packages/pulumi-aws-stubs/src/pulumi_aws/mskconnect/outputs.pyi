import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectorCapacity",
    "ConnectorCapacityAutoscaling",
    "ConnectorCapacityAutoscalingScaleInPolicy",
    "ConnectorCapacityAutoscalingScaleOutPolicy",
    "ConnectorCapacityProvisionedCapacity",
    "ConnectorKafkaCluster",
    "ConnectorKafkaClusterApacheKafkaCluster",
    "ConnectorKafkaClusterApacheKafkaClusterVpc",
    "ConnectorKafkaClusterClientAuthentication",
    "ConnectorKafkaClusterEncryptionInTransit",
    "ConnectorLogDelivery",
    "ConnectorLogDeliveryWorkerLogDelivery",
    ...,
    "ConnectorLogDeliveryWorkerLogDeliveryFirehose",
    "ConnectorLogDeliveryWorkerLogDeliveryS3",
    "ConnectorPlugin",
    "ConnectorPluginCustomPlugin",
    "ConnectorWorkerConfiguration",
    "CustomPluginLocation",
    "CustomPluginLocationS3",
]

@pulumi.output_type
class ConnectorCapacity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        autoscaling: Optional[outputs.ConnectorCapacityAutoscaling] = ...,
        provisioned_capacity: Optional[
            outputs.ConnectorCapacityProvisionedCapacity
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> Optional[outputs.ConnectorCapacityAutoscaling]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedCapacity")
    def provisioned_capacity(
        self,
    ) -> Optional[outputs.ConnectorCapacityProvisionedCapacity]: ...

@pulumi.output_type
class ConnectorCapacityAutoscaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_worker_count: _builtins.int,
        min_worker_count: _builtins.int,
        mcu_count: Optional[_builtins.int] = ...,
        scale_in_policy: Optional[
            outputs.ConnectorCapacityAutoscalingScaleInPolicy
        ] = ...,
        scale_out_policy: Optional[
            outputs.ConnectorCapacityAutoscalingScaleOutPolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxWorkerCount")
    def max_worker_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minWorkerCount")
    def min_worker_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="mcuCount")
    def mcu_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scaleInPolicy")
    def scale_in_policy(
        self,
    ) -> Optional[outputs.ConnectorCapacityAutoscalingScaleInPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="scaleOutPolicy")
    def scale_out_policy(
        self,
    ) -> Optional[outputs.ConnectorCapacityAutoscalingScaleOutPolicy]: ...

@pulumi.output_type
class ConnectorCapacityAutoscalingScaleInPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cpu_utilization_percentage: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConnectorCapacityAutoscalingScaleOutPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cpu_utilization_percentage: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConnectorCapacityProvisionedCapacity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        worker_count: _builtins.int,
        mcu_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="mcuCount")
    def mcu_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConnectorKafkaCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apache_kafka_cluster: outputs.ConnectorKafkaClusterApacheKafkaCluster,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apacheKafkaCluster")
    def apache_kafka_cluster(
        self,
    ) -> outputs.ConnectorKafkaClusterApacheKafkaCluster: ...

@pulumi.output_type
class ConnectorKafkaClusterApacheKafkaCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bootstrap_servers: _builtins.str,
        vpc: outputs.ConnectorKafkaClusterApacheKafkaClusterVpc,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapServers")
    def bootstrap_servers(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> outputs.ConnectorKafkaClusterApacheKafkaClusterVpc: ...

@pulumi.output_type
class ConnectorKafkaClusterApacheKafkaClusterVpc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_groups: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ConnectorKafkaClusterClientAuthentication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, authentication_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorKafkaClusterEncryptionInTransit(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, encryption_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorLogDelivery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, worker_log_delivery: outputs.ConnectorLogDeliveryWorkerLogDelivery
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workerLogDelivery")
    def worker_log_delivery(self) -> outputs.ConnectorLogDeliveryWorkerLogDelivery: ...

@pulumi.output_type
class ConnectorLogDeliveryWorkerLogDelivery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            outputs.ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs
        ] = ...,
        firehose: Optional[outputs.ConnectorLogDeliveryWorkerLogDeliveryFirehose] = ...,
        s3: Optional[outputs.ConnectorLogDeliveryWorkerLogDeliveryS3] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[outputs.ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs]: ...
    @_builtins.property
    @pulumi.getter
    def firehose(
        self,
    ) -> Optional[outputs.ConnectorLogDeliveryWorkerLogDeliveryFirehose]: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[outputs.ConnectorLogDeliveryWorkerLogDeliveryS3]: ...

@pulumi.output_type
class ConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs(dict):
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
class ConnectorLogDeliveryWorkerLogDeliveryFirehose(dict):
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
class ConnectorLogDeliveryWorkerLogDeliveryS3(dict):
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
class ConnectorPlugin(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, custom_plugin: outputs.ConnectorPluginCustomPlugin
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customPlugin")
    def custom_plugin(self) -> outputs.ConnectorPluginCustomPlugin: ...

@pulumi.output_type
class ConnectorPluginCustomPlugin(dict):
    def __init__(__self__, *, arn: _builtins.str, revision: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.int: ...

@pulumi.output_type
class ConnectorWorkerConfiguration(dict):
    def __init__(__self__, *, arn: _builtins.str, revision: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.int: ...

@pulumi.output_type
class CustomPluginLocation(dict):
    def __init__(__self__, *, s3: outputs.CustomPluginLocationS3) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> outputs.CustomPluginLocationS3: ...

@pulumi.output_type
class CustomPluginLocationS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        file_key: _builtins.str,
        object_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[_builtins.str]: ...
