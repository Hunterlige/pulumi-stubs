import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureMonitorConfigurationResponse",
    "AzureMonitorInformationResponse",
    "ChangeTrackingConfigurationResponse",
    "ChangeTrackingInformationResponse",
    "DefenderCspmInformationResponse",
    "DefenderForServersInformationResponse",
    "DesiredConfigurationResponse",
    "GuestConfigurationInformationResponse",
    "ManagedOpsPropertiesResponse",
    "PolicyAssignmentPropertiesResponse",
    "ServiceInformationResponse",
    "SkuResponse",
    "SystemDataResponse",
    "UpdateManagerInformationResponse",
]

@pulumi.output_type
class AzureMonitorConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, azure_monitor_workspace_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceId")
    def azure_monitor_workspace_id(self) -> _builtins.str: ...

@pulumi.output_type
class AzureMonitorInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dcr_id: _builtins.str, enablement_status: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dcrId")
    def dcr_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enablementStatus")
    def enablement_status(self) -> _builtins.str: ...

@pulumi.output_type
class ChangeTrackingConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, log_analytics_workspace_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChangeTrackingInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dcr_id: _builtins.str, enablement_status: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dcrId")
    def dcr_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enablementStatus")
    def enablement_status(self) -> _builtins.str: ...

@pulumi.output_type
class DefenderCspmInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enablement_status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablementStatus")
    def enablement_status(self) -> _builtins.str: ...

@pulumi.output_type
class DefenderForServersInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enablement_status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablementStatus")
    def enablement_status(self) -> _builtins.str: ...

@pulumi.output_type
class DesiredConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_monitor_insights: outputs.AzureMonitorConfigurationResponse,
        change_tracking_and_inventory: outputs.ChangeTrackingConfigurationResponse,
        user_assigned_managed_identity_id: _builtins.str,
        defender_cspm: Optional[_builtins.str] = ...,
        defender_for_servers: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorInsights")
    def azure_monitor_insights(self) -> outputs.AzureMonitorConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="changeTrackingAndInventory")
    def change_tracking_and_inventory(
        self,
    ) -> outputs.ChangeTrackingConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedManagedIdentityId")
    def user_assigned_managed_identity_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defenderCspm")
    def defender_cspm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defenderForServers")
    def defender_for_servers(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestConfigurationInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enablement_status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablementStatus")
    def enablement_status(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedOpsPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        desired_configuration: outputs.DesiredConfigurationResponse,
        policy_assignment_properties: outputs.PolicyAssignmentPropertiesResponse,
        provisioning_state: _builtins.str,
        services: outputs.ServiceInformationResponse,
        sku: outputs.SkuResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredConfiguration")
    def desired_configuration(self) -> outputs.DesiredConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="policyAssignmentProperties")
    def policy_assignment_properties(
        self,
    ) -> outputs.PolicyAssignmentPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def services(self) -> outputs.ServiceInformationResponse: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...

@pulumi.output_type
class PolicyAssignmentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, policy_initiative_assignment_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyInitiativeAssignmentId")
    def policy_initiative_assignment_id(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_monitor_insights: outputs.AzureMonitorInformationResponse,
        azure_policy_and_machine_configuration: outputs.GuestConfigurationInformationResponse,
        azure_update_manager: outputs.UpdateManagerInformationResponse,
        change_tracking_and_inventory: outputs.ChangeTrackingInformationResponse,
        defender_cspm: outputs.DefenderCspmInformationResponse,
        defender_for_servers: outputs.DefenderForServersInformationResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorInsights")
    def azure_monitor_insights(self) -> outputs.AzureMonitorInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="azurePolicyAndMachineConfiguration")
    def azure_policy_and_machine_configuration(
        self,
    ) -> outputs.GuestConfigurationInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="azureUpdateManager")
    def azure_update_manager(self) -> outputs.UpdateManagerInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="changeTrackingAndInventory")
    def change_tracking_and_inventory(
        self,
    ) -> outputs.ChangeTrackingInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="defenderCspm")
    def defender_cspm(self) -> outputs.DefenderCspmInformationResponse: ...
    @_builtins.property
    @pulumi.getter(name="defenderForServers")
    def defender_for_servers(self) -> outputs.DefenderForServersInformationResponse: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *, name: _builtins.str, tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str: ...

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
class UpdateManagerInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enablement_status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablementStatus")
    def enablement_status(self) -> _builtins.str: ...
