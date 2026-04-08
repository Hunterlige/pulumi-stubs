import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKafkaConfigurationResult",
    "AwaitableGetKafkaConfigurationResult",
    "get_kafka_configuration",
    "get_kafka_configuration_output",
]

@pulumi.output_type
class GetKafkaConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        consumer_group=...,
        credentials=...,
        event_hub_partition_id=...,
        event_hub_resource_id=...,
        event_hub_type=...,
        event_streaming_state=...,
        event_streaming_type=...,
        id=...,
        name=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.CredentialsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubPartitionId")
    def event_hub_partition_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubType")
    def event_hub_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventStreamingState")
    def event_streaming_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventStreamingType")
    def event_streaming_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetKafkaConfigurationResult(GetKafkaConfigurationResult):
    def __await__(self): ...

def get_kafka_configuration(
    account_name: Optional[_builtins.str] = ...,
    kafka_configuration_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKafkaConfigurationResult: ...
def get_kafka_configuration_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    kafka_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKafkaConfigurationResult]: ...
