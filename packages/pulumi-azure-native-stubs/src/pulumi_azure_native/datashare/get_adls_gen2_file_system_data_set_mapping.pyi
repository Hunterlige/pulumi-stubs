import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetADLSGen2FileSystemDataSetMappingResult",
    "AwaitableGetADLSGen2FileSystemDataSetMappingResult",
    "get_adls_gen2_file_system_data_set_mapping",
    "get_adls_gen2_file_system_data_set_mapping_output",
]

@pulumi.output_type
class GetADLSGen2FileSystemDataSetMappingResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_set_id=...,
        data_set_mapping_status=...,
        file_system=...,
        id=...,
        kind=...,
        name=...,
        provisioning_state=...,
        resource_group=...,
        storage_account_name=...,
        subscription_id=...,
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
    @pulumi.getter(name="fileSystem")
    def file_system(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetADLSGen2FileSystemDataSetMappingResult(
    GetADLSGen2FileSystemDataSetMappingResult
):
    def __await__(self): ...

def get_adls_gen2_file_system_data_set_mapping(
    account_name: Optional[_builtins.str] = ...,
    data_set_mapping_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    share_subscription_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetADLSGen2FileSystemDataSetMappingResult: ...
def get_adls_gen2_file_system_data_set_mapping_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    data_set_mapping_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    share_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetADLSGen2FileSystemDataSetMappingResult]: ...
