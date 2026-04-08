import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApprovalSettingsResponse",
    "ApproverResponse",
    "CommunityEndpointDestinationRuleResponse",
    "EnclaveAddressSpacesModelResponse",
    "EnclaveDefaultSettingsModelResponse",
    "EnclaveEndpointDestinationRuleResponse",
    "EnclaveVirtualNetworkModelResponse",
    "GovernedServiceItemResponse",
    "MaintenanceModeConfigurationModelResponse",
    "ManagedOnBehalfOfConfigurationResponse",
    "ManagedServiceIdentityResponse",
    "MandatoryApproverResponse",
    "MoboBrokerResourceResponse",
    "PrincipalResponse",
    "RequestMetadataResponse",
    "RoleAssignmentItemResponse",
    "SubnetConfigurationResponse",
    "SystemDataResponse",
    "TransitOptionParamsResponse",
    "TransitOptionResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class ApprovalSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_creation: Optional[_builtins.str] = ...,
        connection_deletion: Optional[_builtins.str] = ...,
        connection_update: Optional[_builtins.str] = ...,
        enclave_creation: Optional[_builtins.str] = ...,
        enclave_deletion: Optional[_builtins.str] = ...,
        endpoint_creation: Optional[_builtins.str] = ...,
        endpoint_deletion: Optional[_builtins.str] = ...,
        endpoint_update: Optional[_builtins.str] = ...,
        maintenance_mode: Optional[_builtins.str] = ...,
        mandatory_approvers: Optional[
            Sequence[outputs.MandatoryApproverResponse]
        ] = ...,
        minimum_approvers_required: Optional[_builtins.float] = ...,
        notification_on_approval_action: Optional[_builtins.str] = ...,
        notification_on_approval_creation: Optional[_builtins.str] = ...,
        notification_on_approval_deletion: Optional[_builtins.str] = ...,
        service_catalog_deployment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionCreation")
    def connection_creation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionDeletion")
    def connection_deletion(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionUpdate")
    def connection_update(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enclaveCreation")
    def enclave_creation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enclaveDeletion")
    def enclave_deletion(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointCreation")
    def endpoint_creation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointDeletion")
    def endpoint_deletion(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUpdate")
    def endpoint_update(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceMode")
    def maintenance_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mandatoryApprovers")
    def mandatory_approvers(
        self,
    ) -> Optional[Sequence[outputs.MandatoryApproverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="minimumApproversRequired")
    def minimum_approvers_required(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="notificationOnApprovalAction")
    def notification_on_approval_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationOnApprovalCreation")
    def notification_on_approval_creation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationOnApprovalDeletion")
    def notification_on_approval_deletion(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceCatalogDeployment")
    def service_catalog_deployment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApproverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        approver_entra_id: _builtins.str,
        last_updated_at: _builtins.str,
        action_performed: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approverEntraId")
    def approver_entra_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actionPerformed")
    def action_performed(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CommunityEndpointDestinationRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: Optional[_builtins.str] = ...,
        destination_type: Optional[_builtins.str] = ...,
        endpoint_rule_name: Optional[_builtins.str] = ...,
        ports: Optional[_builtins.str] = ...,
        protocols: Optional[Sequence[_builtins.str]] = ...,
        transit_hub_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointRuleName")
    def endpoint_rule_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitHubResourceId")
    def transit_hub_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnclaveAddressSpacesModelResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enclave_address_space: Optional[_builtins.str] = ...,
        managed_address_space: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enclaveAddressSpace")
    def enclave_address_space(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedAddressSpace")
    def managed_address_space(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnclaveDefaultSettingsModelResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_vault_resource_id: _builtins.str,
        log_analytics_resource_id_collection: Sequence[_builtins.str],
        storage_account_resource_id: _builtins.str,
        diagnostic_destination: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsResourceIdCollection")
    def log_analytics_resource_id_collection(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticDestination")
    def diagnostic_destination(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnclaveEndpointDestinationRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: Optional[_builtins.str] = ...,
        endpoint_rule_name: Optional[_builtins.str] = ...,
        ports: Optional[_builtins.str] = ...,
        protocols: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointRuleName")
    def endpoint_rule_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EnclaveVirtualNetworkModelResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_subnet_communication: Optional[_builtins.bool] = ...,
        custom_cidr_range: Optional[_builtins.str] = ...,
        network_name: Optional[_builtins.str] = ...,
        network_size: Optional[_builtins.str] = ...,
        subnet_configurations: Optional[
            Sequence[outputs.SubnetConfigurationResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowSubnetCommunication")
    def allow_subnet_communication(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="customCidrRange")
    def custom_cidr_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkSize")
    def network_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetConfigurations")
    def subnet_configurations(
        self,
    ) -> Optional[Sequence[outputs.SubnetConfigurationResponse]]: ...

@pulumi.output_type
class GovernedServiceItemResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        initiatives: Sequence[_builtins.str],
        service_id: _builtins.str,
        service_name: _builtins.str,
        enforcement: Optional[_builtins.str] = ...,
        option: Optional[_builtins.str] = ...,
        policy_action: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def initiatives(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enforcement(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyAction")
    def policy_action(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MaintenanceModeConfigurationModelResponse(dict):
    def __init__(
        __self__,
        *,
        mode: Optional[_builtins.str] = ...,
        justification: Optional[_builtins.str] = ...,
        principals: Optional[Sequence[outputs.PrincipalResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def justification(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[Sequence[outputs.PrincipalResponse]]: ...

@pulumi.output_type
class ManagedOnBehalfOfConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mobo_broker_resources: Optional[
            Sequence[outputs.MoboBrokerResourceResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="moboBrokerResources")
    def mobo_broker_resources(
        self,
    ) -> Optional[Sequence[outputs.MoboBrokerResourceResponse]]: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class MandatoryApproverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, approver_entra_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approverEntraId")
    def approver_entra_id(self) -> _builtins.str: ...

@pulumi.output_type
class MoboBrokerResourceResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrincipalResponse(dict):
    def __init__(__self__, *, id: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class RequestMetadataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_action: _builtins.str,
        approval_callback_payload: Optional[_builtins.str] = ...,
        approval_callback_route: Optional[_builtins.str] = ...,
        approval_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceAction")
    def resource_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="approvalCallbackPayload")
    def approval_callback_payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="approvalCallbackRoute")
    def approval_callback_route(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="approvalStatus")
    def approval_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoleAssignmentItemResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        role_definition_id: _builtins.str,
        principals: Optional[Sequence[outputs.PrincipalResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[Sequence[outputs.PrincipalResponse]]: ...

@pulumi.output_type
class SubnetConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address_prefix: _builtins.str,
        network_prefix_size: _builtins.int,
        network_security_group_resource_id: _builtins.str,
        subnet_name: _builtins.str,
        subnet_resource_id: _builtins.str,
        subnet_delegation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkPrefixSize")
    def network_prefix_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroupResourceId")
    def network_security_group_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetName")
    def subnet_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetDelegation")
    def subnet_delegation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TransitOptionParamsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        remote_virtual_network_id: Optional[_builtins.str] = ...,
        scale_units: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetworkId")
    def remote_virtual_network_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scaleUnits")
    def scale_units(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class TransitOptionResponse(dict):
    def __init__(
        __self__,
        *,
        params: Optional[outputs.TransitOptionParamsResponse] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[outputs.TransitOptionParamsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
