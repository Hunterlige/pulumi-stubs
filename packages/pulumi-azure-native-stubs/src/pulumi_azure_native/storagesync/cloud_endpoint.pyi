import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CloudEndpointArgs", "CloudEndpoint"]

@pulumi.input_type
class CloudEndpointArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        storage_sync_service_name: pulumi.Input[_builtins.str],
        sync_group_name: pulumi.Input[_builtins.str],
        azure_file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageSyncServiceName")
    def storage_sync_service_name(self) -> pulumi.Input[_builtins.str]: ...
    @storage_sync_service_name.setter
    def storage_sync_service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="syncGroupName")
    def sync_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @sync_group_name.setter
    def sync_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareName")
    def azure_file_share_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_file_share_name.setter
    def azure_file_share_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudEndpointName")
    def cloud_endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_endpoint_name.setter
    def cloud_endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_resource_id.setter
    def storage_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountTenantId")
    def storage_account_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_tenant_id.setter
    def storage_account_tenant_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:storagesync:CloudEndpoint")
class CloudEndpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        azure_file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_sync_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CloudEndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CloudEndpoint: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareName")
    def azure_file_share_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="backupEnabled")
    def backup_enabled(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="changeEnumerationStatus")
    def change_enumeration_status(
        self,
    ) -> pulumi.Output[outputs.CloudEndpointChangeEnumerationStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastOperationName")
    def last_operation_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastWorkflowId")
    def last_workflow_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnershipId")
    def partnership_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountTenantId")
    def storage_account_tenant_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
