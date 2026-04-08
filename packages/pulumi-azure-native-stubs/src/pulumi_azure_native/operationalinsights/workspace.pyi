import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceArgs", "Workspace"]

@pulumi.input_type
class WorkspaceArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        default_data_collection_rule_resource_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        features: Optional[pulumi.Input[WorkspaceFeaturesArgs]] = ...,
        force_cmk_for_query: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity: Optional[pulumi.Input[IdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access_for_ingestion: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]
        ] = ...,
        public_network_access_for_query: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]
        ] = ...,
        retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        sku: Optional[pulumi.Input[WorkspaceSkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workspace_capping: Optional[pulumi.Input[WorkspaceCappingArgs]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultDataCollectionRuleResourceId")
    def default_data_collection_rule_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_data_collection_rule_resource_id.setter
    def default_data_collection_rule_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input[WorkspaceFeaturesArgs]]: ...
    @features.setter
    def features(self, value: Optional[pulumi.Input[WorkspaceFeaturesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="forceCmkForQuery")
    def force_cmk_for_query(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_cmk_for_query.setter
    def force_cmk_for_query(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccessForIngestion")
    def public_network_access_for_ingestion(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]]: ...
    @public_network_access_for_ingestion.setter
    def public_network_access_for_ingestion(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccessForQuery")
    def public_network_access_for_query(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]]: ...
    @public_network_access_for_query.setter
    def public_network_access_for_query(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_in_days.setter
    def retention_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[WorkspaceSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[WorkspaceSkuArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceCapping")
    def workspace_capping(self) -> Optional[pulumi.Input[WorkspaceCappingArgs]]: ...
    @workspace_capping.setter
    def workspace_capping(
        self, value: Optional[pulumi.Input[WorkspaceCappingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:operationalinsights:Workspace")
class Workspace(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        default_data_collection_rule_resource_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        features: Optional[
            pulumi.Input[Union[WorkspaceFeaturesArgs, WorkspaceFeaturesArgsDict]]
        ] = ...,
        force_cmk_for_query: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access_for_ingestion: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]
        ] = ...,
        public_network_access_for_query: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        sku: Optional[
            pulumi.Input[Union[WorkspaceSkuArgs, WorkspaceSkuArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workspace_capping: Optional[
            pulumi.Input[Union[WorkspaceCappingArgs, WorkspaceCappingArgsDict]]
        ] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Workspace: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDataCollectionRuleResourceId")
    def default_data_collection_rule_resource_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkspaceFeaturesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="forceCmkForQuery")
    def force_cmk_for_query(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedDate")
    def modified_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkScopedResources")
    def private_link_scoped_resources(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateLinkScopedResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccessForIngestion")
    def public_network_access_for_ingestion(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccessForQuery")
    def public_network_access_for_query(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.WorkspaceSkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceCapping")
    def workspace_capping(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkspaceCappingResponse]]: ...
