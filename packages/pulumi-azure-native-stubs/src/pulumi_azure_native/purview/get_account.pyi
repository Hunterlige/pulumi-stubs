import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccountResult",
    "AwaitableGetAccountResult",
    "get_account",
    "get_account_output",
]

@pulumi.output_type
class GetAccountResult:
    def __init__(
        __self__,
        account_status=...,
        azure_api_version=...,
        cloud_connectors=...,
        created_at=...,
        created_by=...,
        created_by_object_id=...,
        default_domain=...,
        endpoints=...,
        friendly_name=...,
        id=...,
        identity=...,
        ingestion_storage=...,
        location=...,
        managed_event_hub_state=...,
        managed_resource_group_name=...,
        managed_resources=...,
        managed_resources_public_network_access=...,
        merge_info=...,
        name=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        public_network_access=...,
        sku=...,
        system_data=...,
        tags=...,
        tenant_endpoint_state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountStatus")
    def account_status(self) -> outputs.AccountPropertiesAccountStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudConnectors")
    def cloud_connectors(self) -> Optional[outputs.CloudConnectorsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdByObjectId")
    def created_by_object_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> outputs.AccountPropertiesEndpointsResponse: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="ingestionStorage")
    def ingestion_storage(self) -> Optional[outputs.IngestionStorageResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedEventHubState")
    def managed_event_hub_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedResources")
    def managed_resources(
        self,
    ) -> outputs.AccountPropertiesManagedResourcesResponse: ...
    @_builtins.property
    @pulumi.getter(name="managedResourcesPublicNetworkAccess")
    def managed_resources_public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mergeInfo")
    def merge_info(self) -> Optional[outputs.AccountMergeInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.AccountSkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantEndpointState")
    def tenant_endpoint_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAccountResult(GetAccountResult):
    def __await__(self): ...

def get_account(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAccountResult: ...
def get_account_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccountResult]: ...
