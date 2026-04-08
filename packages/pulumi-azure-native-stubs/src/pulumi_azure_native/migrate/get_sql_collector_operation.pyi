import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSqlCollectorOperationResult",
    "AwaitableGetSqlCollectorOperationResult",
    "get_sql_collector_operation",
    "get_sql_collector_operation_output",
]

@pulumi.output_type
class GetSqlCollectorOperationResult:
    def __init__(
        __self__,
        agent_properties=...,
        azure_api_version=...,
        created_timestamp=...,
        discovery_site_id=...,
        id=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        type=...,
        updated_timestamp=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentProperties")
    def agent_properties(
        self,
    ) -> Optional[outputs.CollectorAgentPropertiesBaseResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str: ...

class AwaitableGetSqlCollectorOperationResult(GetSqlCollectorOperationResult):
    def __await__(self): ...

def get_sql_collector_operation(
    collector_name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSqlCollectorOperationResult: ...
def get_sql_collector_operation_output(
    collector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSqlCollectorOperationResult]: ...
