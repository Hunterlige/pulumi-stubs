import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkspaceResult",
    "AwaitableGetWorkspaceResult",
    "get_workspace",
    "get_workspace_output",
]

@pulumi.output_type
class GetWorkspaceResult:
    def __init__(
        __self__,
        allow_public_access_when_behind_vnet=...,
        application_insights=...,
        associated_workspaces=...,
        azure_api_version=...,
        container_registry=...,
        description=...,
        discovery_url=...,
        enable_data_isolation=...,
        enable_service_side_cmk_encryption=...,
        encryption=...,
        feature_store_settings=...,
        friendly_name=...,
        hbi_workspace=...,
        hub_resource_id=...,
        id=...,
        identity=...,
        image_build_compute=...,
        key_vault=...,
        kind=...,
        location=...,
        managed_network=...,
        ml_flow_tracking_uri=...,
        name=...,
        notebook_info=...,
        primary_user_assigned_identity=...,
        private_endpoint_connections=...,
        private_link_count=...,
        provision_network_now=...,
        provisioning_state=...,
        public_network_access=...,
        serverless_compute_settings=...,
        service_managed_resources_settings=...,
        service_provisioned_resource_group=...,
        shared_private_link_resources=...,
        sku=...,
        storage_account=...,
        storage_hns_enabled=...,
        system_data=...,
        system_datastores_auth_mode=...,
        tags=...,
        tenant_id=...,
        type=...,
        v1_legacy_mode=...,
        workspace_hub_config=...,
        workspace_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPublicAccessWhenBehindVnet")
    def allow_public_access_when_behind_vnet(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="applicationInsights")
    def application_insights(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associatedWorkspaces")
    def associated_workspaces(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerRegistry")
    def container_registry(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableDataIsolation")
    def enable_data_isolation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableServiceSideCMKEncryption")
    def enable_service_side_cmk_encryption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionPropertyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="featureStoreSettings")
    def feature_store_settings(
        self,
    ) -> Optional[outputs.FeatureStoreSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hbiWorkspace")
    def hbi_workspace(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="hubResourceId")
    def hub_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="imageBuildCompute")
    def image_build_compute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedNetwork")
    def managed_network(self) -> Optional[outputs.ManagedNetworkSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="mlFlowTrackingUri")
    def ml_flow_tracking_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notebookInfo")
    def notebook_info(self) -> outputs.NotebookResourceInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentity")
    def primary_user_assigned_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkCount")
    def private_link_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisionNetworkNow")
    def provision_network_now(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverlessComputeSettings")
    def serverless_compute_settings(
        self,
    ) -> Optional[outputs.ServerlessComputeSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="serviceManagedResourcesSettings")
    def service_managed_resources_settings(
        self,
    ) -> Optional[outputs.ServiceManagedResourcesSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="serviceProvisionedResourceGroup")
    def service_provisioned_resource_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sharedPrivateLinkResources")
    def shared_private_link_resources(
        self,
    ) -> Optional[Sequence[outputs.SharedPrivateLinkResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageHnsEnabled")
    def storage_hns_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemDatastoresAuthMode")
    def system_datastores_auth_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="v1LegacyMode")
    def v1_legacy_mode(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceHubConfig")
    def workspace_hub_config(self) -> Optional[outputs.WorkspaceHubConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str: ...

class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    def __await__(self): ...

def get_workspace(
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkspaceResult: ...
def get_workspace_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkspaceResult]: ...
