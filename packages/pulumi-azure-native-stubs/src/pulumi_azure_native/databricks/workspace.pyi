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
        managed_resource_group_id: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        access_connector: Optional[
            pulumi.Input[WorkspacePropertiesAccessConnectorArgs]
        ] = ...,
        authorizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkspaceProviderAuthorizationArgs]]]
        ] = ...,
        default_catalog: Optional[pulumi.Input[DefaultCatalogPropertiesArgs]] = ...,
        default_storage_firewall: Optional[
            pulumi.Input[Union[_builtins.str, DefaultStorageFirewall]]
        ] = ...,
        encryption: Optional[pulumi.Input[WorkspacePropertiesEncryptionArgs]] = ...,
        enhanced_security_compliance: Optional[
            pulumi.Input[EnhancedSecurityComplianceDefinitionArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[pulumi.Input[WorkspaceCustomParametersArgs]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        required_nsg_rules: Optional[
            pulumi.Input[Union[_builtins.str, RequiredNsgRules]]
        ] = ...,
        sku: Optional[pulumi.Input[SkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        ui_definition_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupId")
    def managed_resource_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @managed_resource_group_id.setter
    def managed_resource_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessConnector")
    def access_connector(
        self,
    ) -> Optional[pulumi.Input[WorkspacePropertiesAccessConnectorArgs]]: ...
    @access_connector.setter
    def access_connector(
        self, value: Optional[pulumi.Input[WorkspacePropertiesAccessConnectorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def authorizations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkspaceProviderAuthorizationArgs]]]
    ]: ...
    @authorizations.setter
    def authorizations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkspaceProviderAuthorizationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultCatalog")
    def default_catalog(
        self,
    ) -> Optional[pulumi.Input[DefaultCatalogPropertiesArgs]]: ...
    @default_catalog.setter
    def default_catalog(
        self, value: Optional[pulumi.Input[DefaultCatalogPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageFirewall")
    def default_storage_firewall(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DefaultStorageFirewall]]]: ...
    @default_storage_firewall.setter
    def default_storage_firewall(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DefaultStorageFirewall]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> Optional[pulumi.Input[WorkspacePropertiesEncryptionArgs]]: ...
    @encryption.setter
    def encryption(
        self, value: Optional[pulumi.Input[WorkspacePropertiesEncryptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enhancedSecurityCompliance")
    def enhanced_security_compliance(
        self,
    ) -> Optional[pulumi.Input[EnhancedSecurityComplianceDefinitionArgs]]: ...
    @enhanced_security_compliance.setter
    def enhanced_security_compliance(
        self, value: Optional[pulumi.Input[EnhancedSecurityComplianceDefinitionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[WorkspaceCustomParametersArgs]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[WorkspaceCustomParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredNsgRules")
    def required_nsg_rules(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RequiredNsgRules]]]: ...
    @required_nsg_rules.setter
    def required_nsg_rules(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RequiredNsgRules]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): ...
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
    @pulumi.getter(name="uiDefinitionUri")
    def ui_definition_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ui_definition_uri.setter
    def ui_definition_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:databricks:Workspace")
class Workspace(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_connector: Optional[
            pulumi.Input[
                Union[
                    WorkspacePropertiesAccessConnectorArgs,
                    WorkspacePropertiesAccessConnectorArgsDict,
                ]
            ]
        ] = ...,
        authorizations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkspaceProviderAuthorizationArgs,
                            WorkspaceProviderAuthorizationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        default_catalog: Optional[
            pulumi.Input[
                Union[DefaultCatalogPropertiesArgs, DefaultCatalogPropertiesArgsDict]
            ]
        ] = ...,
        default_storage_firewall: Optional[
            pulumi.Input[Union[_builtins.str, DefaultStorageFirewall]]
        ] = ...,
        encryption: Optional[
            pulumi.Input[
                Union[
                    WorkspacePropertiesEncryptionArgs,
                    WorkspacePropertiesEncryptionArgsDict,
                ]
            ]
        ] = ...,
        enhanced_security_compliance: Optional[
            pulumi.Input[
                Union[
                    EnhancedSecurityComplianceDefinitionArgs,
                    EnhancedSecurityComplianceDefinitionArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_resource_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Union[WorkspaceCustomParametersArgs, WorkspaceCustomParametersArgsDict]
            ]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        required_nsg_rules: Optional[
            pulumi.Input[Union[_builtins.str, RequiredNsgRules]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        ui_definition_uri: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="accessConnector")
    def access_connector(
        self,
    ) -> pulumi.Output[
        Optional[outputs.WorkspacePropertiesResponseAccessConnector]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def authorizations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.WorkspaceProviderAuthorizationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional[outputs.CreatedByResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultCatalog")
    def default_catalog(
        self,
    ) -> pulumi.Output[Optional[outputs.DefaultCatalogPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageFirewall")
    def default_storage_firewall(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkspacePropertiesResponseEncryption]]: ...
    @_builtins.property
    @pulumi.getter(name="enhancedSecurityCompliance")
    def enhanced_security_compliance(
        self,
    ) -> pulumi.Output[
        Optional[outputs.EnhancedSecurityComplianceDefinitionResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="isUcEnabled")
    def is_uc_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedDiskIdentity")
    def managed_disk_identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedIdentityConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupId")
    def managed_resource_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkspaceCustomParametersResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredNsgRules")
    def required_nsg_rules(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountIdentity")
    def storage_account_identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedIdentityConfigurationResponse]]: ...
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
    @pulumi.getter(name="uiDefinitionUri")
    def ui_definition_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[Optional[outputs.CreatedByResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceUrl")
    def workspace_url(self) -> pulumi.Output[_builtins.str]: ...
