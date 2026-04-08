import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKustoTableDataSetMappingResult",
    "AwaitableGetKustoTableDataSetMappingResult",
    "get_kusto_table_data_set_mapping",
    "get_kusto_table_data_set_mapping_output",
]

@pulumi.output_type
class GetKustoTableDataSetMappingResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_set_id=...,
        data_set_mapping_status=...,
        id=...,
        kind=...,
        kusto_cluster_resource_id=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetMappingStatus")
    def data_set_mapping_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kustoClusterResourceId")
    def kusto_cluster_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetKustoTableDataSetMappingResult(GetKustoTableDataSetMappingResult):
    def __await__(self): ...

def get_kusto_table_data_set_mapping(
    account_name: Optional[_builtins.str] = ...,
    data_set_mapping_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    share_subscription_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKustoTableDataSetMappingResult: ...
def get_kusto_table_data_set_mapping_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    data_set_mapping_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    share_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKustoTableDataSetMappingResult]: ...
