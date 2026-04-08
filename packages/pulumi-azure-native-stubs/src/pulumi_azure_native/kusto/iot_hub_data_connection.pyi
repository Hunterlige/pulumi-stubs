import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IotHubDataConnectionArgs", "IotHubDataConnection"]

@pulumi.input_type
class IotHubDataConnectionArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        consumer_group: pulumi.Input[_builtins.str],
        database_name: pulumi.Input[_builtins.str],
        iot_hub_resource_id: pulumi.Input[_builtins.str],
        kind: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        shared_access_policy_name: pulumi.Input[_builtins.str],
        data_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        data_format: Optional[
            pulumi.Input[Union[_builtins.str, IotHubDataFormat]]
        ] = ...,
        database_routing: Optional[
            pulumi.Input[Union[_builtins.str, DatabaseRouting]]
        ] = ...,
        event_system_properties: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mapping_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retrieval_start_date: Optional[pulumi.Input[_builtins.str]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Input[_builtins.str]: ...
    @consumer_group.setter
    def consumer_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="iotHubResourceId")
    def iot_hub_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @iot_hub_resource_id.setter
    def iot_hub_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> pulumi.Input[_builtins.str]: ...
    @shared_access_policy_name.setter
    def shared_access_policy_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataConnectionName")
    def data_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_connection_name.setter
    def data_connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IotHubDataFormat]]]: ...
    @data_format.setter
    def data_format(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IotHubDataFormat]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseRouting")
    def database_routing(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DatabaseRouting]]]: ...
    @database_routing.setter
    def database_routing(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DatabaseRouting]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventSystemProperties")
    def event_system_properties(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @event_system_properties.setter
    def event_system_properties(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mapping_rule_name.setter
    def mapping_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retrieval_start_date.setter
    def retrieval_start_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:kusto:IotHubDataConnection")
class IotHubDataConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        consumer_group: Optional[pulumi.Input[_builtins.str]] = ...,
        data_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        data_format: Optional[
            pulumi.Input[Union[_builtins.str, IotHubDataFormat]]
        ] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        database_routing: Optional[
            pulumi.Input[Union[_builtins.str, DatabaseRouting]]
        ] = ...,
        event_system_properties: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        iot_hub_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mapping_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retrieval_start_date: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_access_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IotHubDataConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> IotHubDataConnection: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="databaseRouting")
    def database_routing(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventSystemProperties")
    def event_system_properties(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="iotHubResourceId")
    def iot_hub_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
