import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCloudEndpointResult",
    "AwaitableGetCloudEndpointResult",
    "get_cloud_endpoint",
    "get_cloud_endpoint_output",
]

@pulumi.output_type
class GetCloudEndpointResult:
    def __init__(
        __self__,
        azure_api_version=...,
        azure_file_share_name=...,
        backup_enabled=...,
        change_enumeration_status=...,
        friendly_name=...,
        id=...,
        last_operation_name=...,
        last_workflow_id=...,
        name=...,
        partnership_id=...,
        provisioning_state=...,
        storage_account_resource_id=...,
        storage_account_tenant_id=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareName")
    def azure_file_share_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupEnabled")
    def backup_enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="changeEnumerationStatus")
    def change_enumeration_status(
        self,
    ) -> outputs.CloudEndpointChangeEnumerationStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastOperationName")
    def last_operation_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastWorkflowId")
    def last_workflow_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnershipId")
    def partnership_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountTenantId")
    def storage_account_tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCloudEndpointResult(GetCloudEndpointResult):
    def __await__(self): ...

def get_cloud_endpoint(
    cloud_endpoint_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    storage_sync_service_name: Optional[_builtins.str] = ...,
    sync_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCloudEndpointResult: ...
def get_cloud_endpoint_output(
    cloud_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    storage_sync_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    sync_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCloudEndpointResult]: ...
