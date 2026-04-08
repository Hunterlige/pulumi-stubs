import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKafkaConnectorTopicMapResult",
    "AwaitableGetKafkaConnectorTopicMapResult",
    "get_kafka_connector_topic_map",
    "get_kafka_connector_topic_map_output",
]

@pulumi.output_type
class GetKafkaConnectorTopicMapResult:
    def __init__(
        __self__,
        azure_api_version=...,
        batching=...,
        compression=...,
        copy_mqtt_properties=...,
        extended_location=...,
        id=...,
        kafka_connector_ref=...,
        location=...,
        name=...,
        partition_key_property=...,
        partition_strategy=...,
        provisioning_state=...,
        routes=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def batching(self) -> Optional[outputs.KafkaTopicMapBatchingResponse]: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="copyMqttProperties")
    def copy_mqtt_properties(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationPropertyResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kafkaConnectorRef")
    def kafka_connector_ref(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeyProperty")
    def partition_key_property(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionStrategy")
    def partition_strategy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Sequence[outputs.KafkaRoutesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetKafkaConnectorTopicMapResult(GetKafkaConnectorTopicMapResult):
    def __await__(self): ...

def get_kafka_connector_topic_map(
    kafka_connector_name: Optional[_builtins.str] = ...,
    mq_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    topic_map_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKafkaConnectorTopicMapResult: ...
def get_kafka_connector_topic_map_output(
    kafka_connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    mq_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    topic_map_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKafkaConnectorTopicMapResult]: ...
