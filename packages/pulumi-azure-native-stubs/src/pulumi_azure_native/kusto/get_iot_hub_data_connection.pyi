import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIotHubDataConnectionResult",
    "AwaitableGetIotHubDataConnectionResult",
    "get_iot_hub_data_connection",
    "get_iot_hub_data_connection_output",
]

@pulumi.output_type
class GetIotHubDataConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        consumer_group=...,
        data_format=...,
        database_routing=...,
        event_system_properties=...,
        id=...,
        iot_hub_resource_id=...,
        kind=...,
        location=...,
        mapping_rule_name=...,
        name=...,
        provisioning_state=...,
        retrieval_start_date=...,
        shared_access_policy_name=...,
        table_name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseRouting")
    def database_routing(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventSystemProperties")
    def event_system_properties(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iotHubResourceId")
    def iot_hub_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetIotHubDataConnectionResult(GetIotHubDataConnectionResult):
    def __await__(self): ...

def get_iot_hub_data_connection(
    cluster_name: Optional[_builtins.str] = ...,
    data_connection_name: Optional[_builtins.str] = ...,
    database_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIotHubDataConnectionResult: ...
def get_iot_hub_data_connection_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    data_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIotHubDataConnectionResult]: ...
