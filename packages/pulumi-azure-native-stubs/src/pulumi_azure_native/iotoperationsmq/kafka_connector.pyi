import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KafkaConnectorArgs", "KafkaConnector"]

@pulumi.input_type
class KafkaConnectorArgs:
    def __init__(
        __self__,
        *,
        extended_location: pulumi.Input[ExtendedLocationPropertyArgs],
        kafka_connection: pulumi.Input[KafkaRemoteBrokerConnectionSpecArgs],
        mq_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        client_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        image: Optional[pulumi.Input[ContainerImageArgs]] = ...,
        instances: Optional[pulumi.Input[_builtins.int]] = ...,
        kafka_connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        local_broker_connection: Optional[
            pulumi.Input[LocalBrokerConnectionSpecArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_level: Optional[pulumi.Input[_builtins.str]] = ...,
        node_tolerations: Optional[pulumi.Input[NodeTolerationsArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationPropertyArgs]: ...
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationPropertyArgs]): ...
    @_builtins.property
    @pulumi.getter(name="kafkaConnection")
    def kafka_connection(self) -> pulumi.Input[KafkaRemoteBrokerConnectionSpecArgs]: ...
    @kafka_connection.setter
    def kafka_connection(
        self, value: pulumi.Input[KafkaRemoteBrokerConnectionSpecArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mqName")
    def mq_name(self) -> pulumi.Input[_builtins.str]: ...
    @mq_name.setter
    def mq_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientIdPrefix")
    def client_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id_prefix.setter
    def client_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[ContainerImageArgs]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[ContainerImageArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instances.setter
    def instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kafkaConnectorName")
    def kafka_connector_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kafka_connector_name.setter
    def kafka_connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localBrokerConnection")
    def local_broker_connection(
        self,
    ) -> Optional[pulumi.Input[LocalBrokerConnectionSpecArgs]]: ...
    @local_broker_connection.setter
    def local_broker_connection(
        self, value: Optional[pulumi.Input[LocalBrokerConnectionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeTolerations")
    def node_tolerations(self) -> Optional[pulumi.Input[NodeTolerationsArgs]]: ...
    @node_tolerations.setter
    def node_tolerations(self, value: Optional[pulumi.Input[NodeTolerationsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:iotoperationsmq:KafkaConnector")
class KafkaConnector(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        client_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[
            pulumi.Input[
                Union[ExtendedLocationPropertyArgs, ExtendedLocationPropertyArgsDict]
            ]
        ] = ...,
        image: Optional[
            pulumi.Input[Union[ContainerImageArgs, ContainerImageArgsDict]]
        ] = ...,
        instances: Optional[pulumi.Input[_builtins.int]] = ...,
        kafka_connection: Optional[
            pulumi.Input[
                Union[
                    KafkaRemoteBrokerConnectionSpecArgs,
                    KafkaRemoteBrokerConnectionSpecArgsDict,
                ]
            ]
        ] = ...,
        kafka_connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        local_broker_connection: Optional[
            pulumi.Input[
                Union[LocalBrokerConnectionSpecArgs, LocalBrokerConnectionSpecArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_level: Optional[pulumi.Input[_builtins.str]] = ...,
        mq_name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_tolerations: Optional[
            pulumi.Input[Union[NodeTolerationsArgs, NodeTolerationsArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KafkaConnectorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> KafkaConnector: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientIdPrefix")
    def client_id_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[outputs.ExtendedLocationPropertyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Output[Optional[outputs.ContainerImageResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="kafkaConnection")
    def kafka_connection(
        self,
    ) -> pulumi.Output[outputs.KafkaRemoteBrokerConnectionSpecResponse]: ...
    @_builtins.property
    @pulumi.getter(name="localBrokerConnection")
    def local_broker_connection(
        self,
    ) -> pulumi.Output[Optional[outputs.LocalBrokerConnectionSpecResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeTolerations")
    def node_tolerations(
        self,
    ) -> pulumi.Output[Optional[outputs.NodeTolerationsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
