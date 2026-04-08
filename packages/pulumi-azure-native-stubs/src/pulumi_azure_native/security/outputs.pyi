import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessTokenAuthenticationResponse",
    "ActionableRemediationResponse",
    "AdditionalWorkspacesPropertiesResponse",
    "AllowlistCustomAlertRuleResponse",
    "ArcAutoProvisioningResponseConfiguration",
    "AssessmentLinksResponse",
    "AssessmentStatusResponseResponse",
    "AssignedAssessmentItemResponse",
    "AssignedComponentItemResponse",
    "AssignedStandardItemResponse",
    "AssignmentPropertiesResponseAdditionalData",
    "AttestationEvidenceResponse",
    "AuthorizationResponse",
    "AutomationActionEventHubResponse",
    "AutomationActionLogicAppResponse",
    "AutomationActionWorkspaceResponse",
    "AutomationRuleSetResponse",
    "AutomationScopeResponse",
    "AutomationSourceResponse",
    "AutomationTriggeringRuleResponse",
    "AwsEnvironmentDataResponse",
    "AwsOrganizationalDataMasterResponse",
    "AwsOrganizationalDataMemberResponse",
    "AzureDevOpsOrgPropertiesResponse",
    "AzureDevOpsOrgResponse",
    "AzureDevOpsScopeEnvironmentDataResponse",
    "AzureResourceDetailsResponse",
    "CategoryConfigurationResponse",
    "CspmMonitorAwsOfferingResponse",
    ...,
    "CspmMonitorAzureDevOpsOfferingResponse",
    "CspmMonitorDockerHubOfferingResponse",
    "CspmMonitorGcpOfferingResponse",
    ...,
    "CspmMonitorGitLabOfferingResponse",
    "CspmMonitorGithubOfferingResponse",
    "CspmMonitorJFrogOfferingResponse",
    "DefenderCspmAwsOfferingResponse",
    "DefenderCspmAwsOfferingResponseCiem",
    "DefenderCspmAwsOfferingResponseCiemDiscovery",
    "DefenderCspmAwsOfferingResponseCiemOidc",
    ...,
    "DefenderCspmAwsOfferingResponseDatabasesDspm",
    ...,
    ...,
    "DefenderCspmAwsOfferingResponseVmScanners",
    "DefenderCspmDockerHubOfferingResponse",
    "DefenderCspmGcpOfferingResponse",
    "DefenderCspmGcpOfferingResponseCiemDiscovery",
    ...,
    ...,
    ...,
    "DefenderCspmGcpOfferingResponseVmScanners",
    "DefenderCspmJFrogOfferingResponse",
    ...,
    "DefenderFoDatabasesAwsOfferingResponse",
    ...,
    ...,
    "DefenderFoDatabasesAwsOfferingResponseRds",
    "DefenderForContainersAwsOfferingResponse",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DefenderForContainersAwsOfferingResponseVmScanners",
    "DefenderForContainersDockerHubOfferingResponse",
    "DefenderForContainersGcpOfferingResponse",
    ...,
    ...,
    ...,
    ...,
    "DefenderForContainersGcpOfferingResponseVmScanners",
    "DefenderForContainersJFrogOfferingResponse",
    "DefenderForDatabasesGcpOfferingResponse",
    ...,
    ...,
    "DefenderForServersAwsOfferingResponse",
    ...,
    "DefenderForServersAwsOfferingResponseConfiguration",
    ...,
    ...,
    "DefenderForServersAwsOfferingResponseSubPlan",
    ...,
    "DefenderForServersAwsOfferingResponseVmScanners",
    "DefenderForServersGcpOfferingResponse",
    ...,
    "DefenderForServersGcpOfferingResponseConfiguration",
    ...,
    ...,
    "DefenderForServersGcpOfferingResponseSubPlan",
    ...,
    "DefenderForServersGcpOfferingResponseVmScanners",
    "DefenderForStorageSettingPropertiesResponse",
    "DenylistCustomAlertRuleResponse",
    "DevOpsCapabilityResponse",
    "DevOpsConfigurationPropertiesResponse",
    "DockerHubEnvironmentDataResponse",
    "ExtensionResponse",
    "GcpOrganizationalDataMemberResponse",
    "GcpOrganizationalDataOrganizationResponse",
    "GcpProjectDetailsResponse",
    "GcpProjectEnvironmentDataResponse",
    "GitHubOwnerPropertiesResponse",
    "GitHubOwnerResponse",
    "GitLabGroupPropertiesResponse",
    "GitLabGroupResponse",
    "GithubScopeEnvironmentDataResponse",
    "GitlabScopeEnvironmentDataResponse",
    "GovernanceAssignmentAdditionalDataResponse",
    "GovernanceEmailNotificationResponse",
    "GovernanceRuleEmailNotificationResponse",
    "GovernanceRuleMetadataResponse",
    "GovernanceRuleOwnerSourceResponse",
    "IdentityResponse",
    "JFrogEnvironmentDataResponse",
    "JitNetworkAccessPolicyVirtualMachineResponse",
    "JitNetworkAccessPortRuleResponse",
    "JitNetworkAccessRequestPortResponse",
    "JitNetworkAccessRequestResponse",
    "JitNetworkAccessRequestVirtualMachineResponse",
    "MalwareScanningPropertiesResponse",
    "NotificationsSourceAlertResponse",
    "NotificationsSourceAttackPathResponse",
    "OnPremiseResourceDetailsResponse",
    "OnPremiseSqlResourceDetailsResponse",
    "OnUploadPropertiesResponse",
    "OperationStatusResponse",
    "PartialAssessmentPropertiesResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkResourceResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "RecommendationConfigurationPropertiesResponse",
    "RemediationEtaResponse",
    "RuleResultsPropertiesResponse",
    "ScopeElementResponse",
    "SecurityAssessmentMetadataPartnerDataResponse",
    "SecurityAssessmentMetadataPropertiesResponse",
    ...,
    "SecurityAssessmentPartnerDataResponse",
    ...,
    "SensitiveDataDiscoveryPropertiesResponse",
    "StandardAssignmentMetadataResponse",
    ...,
    "StandardAssignmentPropertiesResponseExemptionData",
    "StandardComponentPropertiesResponse",
    "StandardMetadataResponse",
    "SuppressionAlertsScopeResponse",
    "SystemDataResponse",
    "TargetBranchConfigurationResponse",
    "ThresholdCustomAlertRuleResponse",
    "TimeWindowCustomAlertRuleResponse",
    "UserDefinedResourcesPropertiesResponse",
    "VmScannersBaseResponseConfiguration",
]

@pulumi.output_type
class AccessTokenAuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_type: _builtins.str,
        access_token: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ActionableRemediationResponse(dict):
    def __init__(
        __self__,
        *,
        branch_configuration: Optional[outputs.TargetBranchConfigurationResponse] = ...,
        category_configurations: Optional[
            Sequence[outputs.CategoryConfigurationResponse]
        ] = ...,
        inherit_from_parent_state: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchConfiguration")
    def branch_configuration(
        self,
    ) -> Optional[outputs.TargetBranchConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="categoryConfigurations")
    def category_configurations(
        self,
    ) -> Optional[Sequence[outputs.CategoryConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="inheritFromParentState")
    def inherit_from_parent_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AdditionalWorkspacesPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_types: Optional[Sequence[_builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
        workspace: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def workspace(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AllowlistCustomAlertRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowlist_values: Sequence[_builtins.str],
        description: _builtins.str,
        display_name: _builtins.str,
        is_enabled: _builtins.bool,
        rule_type: _builtins.str,
        value_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowlistValues")
    def allowlist_values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> _builtins.str: ...

@pulumi.output_type
class ArcAutoProvisioningResponseConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_link_scope: Optional[_builtins.str] = ...,
        proxy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkScope")
    def private_link_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssessmentLinksResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, azure_portal_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azurePortalUri")
    def azure_portal_uri(self) -> _builtins.str: ...

@pulumi.output_type
class AssessmentStatusResponseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        first_evaluation_date: _builtins.str,
        status_change_date: _builtins.str,
        cause: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firstEvaluationDate")
    def first_evaluation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusChangeDate")
    def status_change_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cause(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssignedAssessmentItemResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, assessment_key: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentKey")
    def assessment_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssignedComponentItemResponse(dict):
    def __init__(__self__, *, key: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssignedStandardItemResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssignmentPropertiesResponseAdditionalData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, exemption_category: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AttestationEvidenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        source_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AuthorizationResponse(dict):
    def __init__(__self__, *, code: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutomationActionEventHubResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_type: _builtins.str,
        sas_policy_name: _builtins.str,
        connection_string: Optional[_builtins.str] = ...,
        event_hub_resource_id: Optional[_builtins.str] = ...,
        is_trusted_service_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sasPolicyName")
    def sas_policy_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isTrustedServiceEnabled")
    def is_trusted_service_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AutomationActionLogicAppResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_type: _builtins.str,
        logic_app_resource_id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutomationActionWorkspaceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_type: _builtins.str,
        workspace_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutomationRuleSetResponse(dict):
    def __init__(
        __self__,
        *,
        rules: Optional[Sequence[outputs.AutomationTriggeringRuleResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.AutomationTriggeringRuleResponse]]: ...

@pulumi.output_type
class AutomationScopeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        scope_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scopePath")
    def scope_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutomationSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_source: Optional[_builtins.str] = ...,
        rule_sets: Optional[Sequence[outputs.AutomationRuleSetResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> Optional[Sequence[outputs.AutomationRuleSetResponse]]: ...

@pulumi.output_type
class AutomationTriggeringRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        expected_value: Optional[_builtins.str] = ...,
        operator: Optional[_builtins.str] = ...,
        property_j_path: Optional[_builtins.str] = ...,
        property_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expectedValue")
    def expected_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyJPath")
    def property_j_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyType")
    def property_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsEnvironmentDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_name: _builtins.str,
        environment_type: _builtins.str,
        organizational_data: Optional[Any] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
        scan_interval: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationalData")
    def organizational_data(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scanInterval")
    def scan_interval(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class AwsOrganizationalDataMasterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        organization_membership_type: _builtins.str,
        excluded_account_ids: Optional[Sequence[_builtins.str]] = ...,
        stackset_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="organizationMembershipType")
    def organization_membership_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="excludedAccountIds")
    def excluded_account_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stacksetName")
    def stackset_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsOrganizationalDataMemberResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        organization_membership_type: _builtins.str,
        parent_hierarchy_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="organizationMembershipType")
    def organization_membership_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parentHierarchyId")
    def parent_hierarchy_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureDevOpsOrgPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        provisioning_status_message: _builtins.str,
        provisioning_status_update_time_utc: _builtins.str,
        actionable_remediation: Optional[outputs.ActionableRemediationResponse] = ...,
        onboarding_state: Optional[_builtins.str] = ...,
        provisioning_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatusMessage")
    def provisioning_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatusUpdateTimeUtc")
    def provisioning_status_update_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actionableRemediation")
    def actionable_remediation(
        self,
    ) -> Optional[outputs.ActionableRemediationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="onboardingState")
    def onboarding_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureDevOpsOrgResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        properties: Optional[outputs.AzureDevOpsOrgPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.AzureDevOpsOrgPropertiesResponse]: ...

@pulumi.output_type
class AzureDevOpsScopeEnvironmentDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, environment_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str: ...

@pulumi.output_type
class AzureResourceDetailsResponse(dict):
    def __init__(__self__, *, id: _builtins.str, source: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...

@pulumi.output_type
class CategoryConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        category: Optional[_builtins.str] = ...,
        minimum_severity_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimumSeverityLevel")
    def minimum_severity_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CspmMonitorAwsOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        native_cloud_connection: Optional[
            outputs.CspmMonitorAwsOfferingResponseNativeCloudConnection
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nativeCloudConnection")
    def native_cloud_connection(
        self,
    ) -> Optional[outputs.CspmMonitorAwsOfferingResponseNativeCloudConnection]: ...

@pulumi.output_type
class CspmMonitorAwsOfferingResponseNativeCloudConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cloud_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CspmMonitorAzureDevOpsOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, description: _builtins.str, offering_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...

@pulumi.output_type
class CspmMonitorDockerHubOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, description: _builtins.str, offering_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...

@pulumi.output_type
class CspmMonitorGcpOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        native_cloud_connection: Optional[
            outputs.CspmMonitorGcpOfferingResponseNativeCloudConnection
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nativeCloudConnection")
    def native_cloud_connection(
        self,
    ) -> Optional[outputs.CspmMonitorGcpOfferingResponseNativeCloudConnection]: ...

@pulumi.output_type
class CspmMonitorGcpOfferingResponseNativeCloudConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CspmMonitorGitLabOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, description: _builtins.str, offering_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...

@pulumi.output_type
class CspmMonitorGithubOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, description: _builtins.str, offering_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...

@pulumi.output_type
class CspmMonitorJFrogOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, description: _builtins.str, offering_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        ciem: Optional[outputs.DefenderCspmAwsOfferingResponseCiem] = ...,
        data_sensitivity_discovery: Optional[
            outputs.DefenderCspmAwsOfferingResponseDataSensitivityDiscovery
        ] = ...,
        databases_dspm: Optional[
            outputs.DefenderCspmAwsOfferingResponseDatabasesDspm
        ] = ...,
        mdc_containers_agentless_discovery_k8s: Optional[
            outputs.DefenderCspmAwsOfferingResponseMdcContainersAgentlessDiscoveryK8s
        ] = ...,
        mdc_containers_image_assessment: Optional[
            outputs.DefenderCspmAwsOfferingResponseMdcContainersImageAssessment
        ] = ...,
        vm_scanners: Optional[outputs.DefenderCspmAwsOfferingResponseVmScanners] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ciem(self) -> Optional[outputs.DefenderCspmAwsOfferingResponseCiem]: ...
    @_builtins.property
    @pulumi.getter(name="dataSensitivityDiscovery")
    def data_sensitivity_discovery(
        self,
    ) -> Optional[outputs.DefenderCspmAwsOfferingResponseDataSensitivityDiscovery]: ...
    @_builtins.property
    @pulumi.getter(name="databasesDspm")
    def databases_dspm(
        self,
    ) -> Optional[outputs.DefenderCspmAwsOfferingResponseDatabasesDspm]: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersAgentlessDiscoveryK8s")
    def mdc_containers_agentless_discovery_k8s(
        self,
    ) -> Optional[
        outputs.DefenderCspmAwsOfferingResponseMdcContainersAgentlessDiscoveryK8s
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersImageAssessment")
    def mdc_containers_image_assessment(
        self,
    ) -> Optional[
        outputs.DefenderCspmAwsOfferingResponseMdcContainersImageAssessment
    ]: ...
    @_builtins.property
    @pulumi.getter(name="vmScanners")
    def vm_scanners(
        self,
    ) -> Optional[outputs.DefenderCspmAwsOfferingResponseVmScanners]: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponseCiem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ciem_discovery: Optional[
            outputs.DefenderCspmAwsOfferingResponseCiemDiscovery
        ] = ...,
        ciem_oidc: Optional[outputs.DefenderCspmAwsOfferingResponseCiemOidc] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ciemDiscovery")
    def ciem_discovery(
        self,
    ) -> Optional[outputs.DefenderCspmAwsOfferingResponseCiemDiscovery]: ...
    @_builtins.property
    @pulumi.getter(name="ciemOidc")
    def ciem_oidc(
        self,
    ) -> Optional[outputs.DefenderCspmAwsOfferingResponseCiemOidc]: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponseCiemDiscovery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cloud_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponseCiemOidc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_active_directory_app_name: Optional[_builtins.str] = ...,
        cloud_role_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectoryAppName")
    def azure_active_directory_app_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponseDataSensitivityDiscovery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponseDatabasesDspm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponseMdcContainersAgentlessDiscoveryK8s(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponseMdcContainersImageAssessment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderCspmAwsOfferingResponseVmScanners(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        configuration: Optional[outputs.VmScannersBaseResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.VmScannersBaseResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderCspmDockerHubOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, description: _builtins.str, offering_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...

@pulumi.output_type
class DefenderCspmGcpOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        ciem_discovery: Optional[
            outputs.DefenderCspmGcpOfferingResponseCiemDiscovery
        ] = ...,
        data_sensitivity_discovery: Optional[
            outputs.DefenderCspmGcpOfferingResponseDataSensitivityDiscovery
        ] = ...,
        mdc_containers_agentless_discovery_k8s: Optional[
            outputs.DefenderCspmGcpOfferingResponseMdcContainersAgentlessDiscoveryK8s
        ] = ...,
        mdc_containers_image_assessment: Optional[
            outputs.DefenderCspmGcpOfferingResponseMdcContainersImageAssessment
        ] = ...,
        vm_scanners: Optional[outputs.DefenderCspmGcpOfferingResponseVmScanners] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ciemDiscovery")
    def ciem_discovery(
        self,
    ) -> Optional[outputs.DefenderCspmGcpOfferingResponseCiemDiscovery]: ...
    @_builtins.property
    @pulumi.getter(name="dataSensitivityDiscovery")
    def data_sensitivity_discovery(
        self,
    ) -> Optional[outputs.DefenderCspmGcpOfferingResponseDataSensitivityDiscovery]: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersAgentlessDiscoveryK8s")
    def mdc_containers_agentless_discovery_k8s(
        self,
    ) -> Optional[
        outputs.DefenderCspmGcpOfferingResponseMdcContainersAgentlessDiscoveryK8s
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersImageAssessment")
    def mdc_containers_image_assessment(
        self,
    ) -> Optional[
        outputs.DefenderCspmGcpOfferingResponseMdcContainersImageAssessment
    ]: ...
    @_builtins.property
    @pulumi.getter(name="vmScanners")
    def vm_scanners(
        self,
    ) -> Optional[outputs.DefenderCspmGcpOfferingResponseVmScanners]: ...

@pulumi.output_type
class DefenderCspmGcpOfferingResponseCiemDiscovery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_active_directory_app_name: Optional[_builtins.str] = ...,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectoryAppName")
    def azure_active_directory_app_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderCspmGcpOfferingResponseDataSensitivityDiscovery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderCspmGcpOfferingResponseMdcContainersAgentlessDiscoveryK8s(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderCspmGcpOfferingResponseMdcContainersImageAssessment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderCspmGcpOfferingResponseVmScanners(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[outputs.VmScannersBaseResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.VmScannersBaseResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderCspmJFrogOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        mdc_containers_image_assessment: Optional[
            outputs.DefenderCspmJFrogOfferingResponseMdcContainersImageAssessment
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersImageAssessment")
    def mdc_containers_image_assessment(
        self,
    ) -> Optional[
        outputs.DefenderCspmJFrogOfferingResponseMdcContainersImageAssessment
    ]: ...

@pulumi.output_type
class DefenderCspmJFrogOfferingResponseMdcContainersImageAssessment(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderFoDatabasesAwsOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        arc_auto_provisioning: Optional[
            outputs.DefenderFoDatabasesAwsOfferingResponseArcAutoProvisioning
        ] = ...,
        databases_dspm: Optional[
            outputs.DefenderFoDatabasesAwsOfferingResponseDatabasesDspm
        ] = ...,
        rds: Optional[outputs.DefenderFoDatabasesAwsOfferingResponseRds] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arcAutoProvisioning")
    def arc_auto_provisioning(
        self,
    ) -> Optional[
        outputs.DefenderFoDatabasesAwsOfferingResponseArcAutoProvisioning
    ]: ...
    @_builtins.property
    @pulumi.getter(name="databasesDspm")
    def databases_dspm(
        self,
    ) -> Optional[outputs.DefenderFoDatabasesAwsOfferingResponseDatabasesDspm]: ...
    @_builtins.property
    @pulumi.getter
    def rds(self) -> Optional[outputs.DefenderFoDatabasesAwsOfferingResponseRds]: ...

@pulumi.output_type
class DefenderFoDatabasesAwsOfferingResponseArcAutoProvisioning(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        configuration: Optional[outputs.ArcAutoProvisioningResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.ArcAutoProvisioningResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderFoDatabasesAwsOfferingResponseDatabasesDspm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderFoDatabasesAwsOfferingResponseRds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForContainersAwsOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        cloud_watch_to_kinesis: Optional[
            outputs.DefenderForContainersAwsOfferingResponseCloudWatchToKinesis
        ] = ...,
        data_collection_external_id: Optional[_builtins.str] = ...,
        enable_audit_logs_auto_provisioning: Optional[_builtins.bool] = ...,
        enable_defender_agent_auto_provisioning: Optional[_builtins.bool] = ...,
        enable_policy_agent_auto_provisioning: Optional[_builtins.bool] = ...,
        kinesis_to_s3: Optional[
            outputs.DefenderForContainersAwsOfferingResponseKinesisToS3
        ] = ...,
        kube_audit_retention_time: Optional[_builtins.float] = ...,
        kubernetes_data_collection: Optional[
            outputs.DefenderForContainersAwsOfferingResponseKubernetesDataCollection
        ] = ...,
        kubernetes_service: Optional[
            outputs.DefenderForContainersAwsOfferingResponseKubernetesService
        ] = ...,
        mdc_containers_agentless_discovery_k8s: Optional[
            outputs.DefenderForContainersAwsOfferingResponseMdcContainersAgentlessDiscoveryK8s
        ] = ...,
        mdc_containers_image_assessment: Optional[
            outputs.DefenderForContainersAwsOfferingResponseMdcContainersImageAssessment
        ] = ...,
        vm_scanners: Optional[
            outputs.DefenderForContainersAwsOfferingResponseVmScanners
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchToKinesis")
    def cloud_watch_to_kinesis(
        self,
    ) -> Optional[
        outputs.DefenderForContainersAwsOfferingResponseCloudWatchToKinesis
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionExternalId")
    def data_collection_external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAuditLogsAutoProvisioning")
    def enable_audit_logs_auto_provisioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableDefenderAgentAutoProvisioning")
    def enable_defender_agent_auto_provisioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePolicyAgentAutoProvisioning")
    def enable_policy_agent_auto_provisioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisToS3")
    def kinesis_to_s3(
        self,
    ) -> Optional[outputs.DefenderForContainersAwsOfferingResponseKinesisToS3]: ...
    @_builtins.property
    @pulumi.getter(name="kubeAuditRetentionTime")
    def kube_audit_retention_time(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesDataCollection")
    def kubernetes_data_collection(
        self,
    ) -> Optional[
        outputs.DefenderForContainersAwsOfferingResponseKubernetesDataCollection
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesService")
    def kubernetes_service(
        self,
    ) -> Optional[
        outputs.DefenderForContainersAwsOfferingResponseKubernetesService
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersAgentlessDiscoveryK8s")
    def mdc_containers_agentless_discovery_k8s(
        self,
    ) -> Optional[
        outputs.DefenderForContainersAwsOfferingResponseMdcContainersAgentlessDiscoveryK8s
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersImageAssessment")
    def mdc_containers_image_assessment(
        self,
    ) -> Optional[
        outputs.DefenderForContainersAwsOfferingResponseMdcContainersImageAssessment
    ]: ...
    @_builtins.property
    @pulumi.getter(name="vmScanners")
    def vm_scanners(
        self,
    ) -> Optional[outputs.DefenderForContainersAwsOfferingResponseVmScanners]: ...

@pulumi.output_type
class DefenderForContainersAwsOfferingResponseCloudWatchToKinesis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cloud_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForContainersAwsOfferingResponseKinesisToS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cloud_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForContainersAwsOfferingResponseKubernetesDataCollection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cloud_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForContainersAwsOfferingResponseKubernetesService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cloud_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForContainersAwsOfferingResponseMdcContainersAgentlessDiscoveryK8s(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForContainersAwsOfferingResponseMdcContainersImageAssessment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForContainersAwsOfferingResponseVmScanners(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        configuration: Optional[outputs.VmScannersBaseResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.VmScannersBaseResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForContainersDockerHubOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, description: _builtins.str, offering_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...

@pulumi.output_type
class DefenderForContainersGcpOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        data_pipeline_native_cloud_connection: Optional[
            outputs.DefenderForContainersGcpOfferingResponseDataPipelineNativeCloudConnection
        ] = ...,
        enable_audit_logs_auto_provisioning: Optional[_builtins.bool] = ...,
        enable_defender_agent_auto_provisioning: Optional[_builtins.bool] = ...,
        enable_policy_agent_auto_provisioning: Optional[_builtins.bool] = ...,
        mdc_containers_agentless_discovery_k8s: Optional[
            outputs.DefenderForContainersGcpOfferingResponseMdcContainersAgentlessDiscoveryK8s
        ] = ...,
        mdc_containers_image_assessment: Optional[
            outputs.DefenderForContainersGcpOfferingResponseMdcContainersImageAssessment
        ] = ...,
        native_cloud_connection: Optional[
            outputs.DefenderForContainersGcpOfferingResponseNativeCloudConnection
        ] = ...,
        vm_scanners: Optional[
            outputs.DefenderForContainersGcpOfferingResponseVmScanners
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPipelineNativeCloudConnection")
    def data_pipeline_native_cloud_connection(
        self,
    ) -> Optional[
        outputs.DefenderForContainersGcpOfferingResponseDataPipelineNativeCloudConnection
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableAuditLogsAutoProvisioning")
    def enable_audit_logs_auto_provisioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableDefenderAgentAutoProvisioning")
    def enable_defender_agent_auto_provisioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePolicyAgentAutoProvisioning")
    def enable_policy_agent_auto_provisioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersAgentlessDiscoveryK8s")
    def mdc_containers_agentless_discovery_k8s(
        self,
    ) -> Optional[
        outputs.DefenderForContainersGcpOfferingResponseMdcContainersAgentlessDiscoveryK8s
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mdcContainersImageAssessment")
    def mdc_containers_image_assessment(
        self,
    ) -> Optional[
        outputs.DefenderForContainersGcpOfferingResponseMdcContainersImageAssessment
    ]: ...
    @_builtins.property
    @pulumi.getter(name="nativeCloudConnection")
    def native_cloud_connection(
        self,
    ) -> Optional[
        outputs.DefenderForContainersGcpOfferingResponseNativeCloudConnection
    ]: ...
    @_builtins.property
    @pulumi.getter(name="vmScanners")
    def vm_scanners(
        self,
    ) -> Optional[outputs.DefenderForContainersGcpOfferingResponseVmScanners]: ...

@pulumi.output_type
class DefenderForContainersGcpOfferingResponseDataPipelineNativeCloudConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForContainersGcpOfferingResponseMdcContainersAgentlessDiscoveryK8s(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForContainersGcpOfferingResponseMdcContainersImageAssessment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForContainersGcpOfferingResponseNativeCloudConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForContainersGcpOfferingResponseVmScanners(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[outputs.VmScannersBaseResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.VmScannersBaseResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForContainersJFrogOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, description: _builtins.str, offering_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...

@pulumi.output_type
class DefenderForDatabasesGcpOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        arc_auto_provisioning: Optional[
            outputs.DefenderForDatabasesGcpOfferingResponseArcAutoProvisioning
        ] = ...,
        defender_for_databases_arc_auto_provisioning: Optional[
            outputs.DefenderForDatabasesGcpOfferingResponseDefenderForDatabasesArcAutoProvisioning
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arcAutoProvisioning")
    def arc_auto_provisioning(
        self,
    ) -> Optional[
        outputs.DefenderForDatabasesGcpOfferingResponseArcAutoProvisioning
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defenderForDatabasesArcAutoProvisioning")
    def defender_for_databases_arc_auto_provisioning(
        self,
    ) -> Optional[
        outputs.DefenderForDatabasesGcpOfferingResponseDefenderForDatabasesArcAutoProvisioning
    ]: ...

@pulumi.output_type
class DefenderForDatabasesGcpOfferingResponseArcAutoProvisioning(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[outputs.ArcAutoProvisioningResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.ArcAutoProvisioningResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForDatabasesGcpOfferingResponseDefenderForDatabasesArcAutoProvisioning(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForServersAwsOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        arc_auto_provisioning: Optional[
            outputs.DefenderForServersAwsOfferingResponseArcAutoProvisioning
        ] = ...,
        defender_for_servers: Optional[
            outputs.DefenderForServersAwsOfferingResponseDefenderForServers
        ] = ...,
        mde_auto_provisioning: Optional[
            outputs.DefenderForServersAwsOfferingResponseMdeAutoProvisioning
        ] = ...,
        sub_plan: Optional[outputs.DefenderForServersAwsOfferingResponseSubPlan] = ...,
        va_auto_provisioning: Optional[
            outputs.DefenderForServersAwsOfferingResponseVaAutoProvisioning
        ] = ...,
        vm_scanners: Optional[
            outputs.DefenderForServersAwsOfferingResponseVmScanners
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arcAutoProvisioning")
    def arc_auto_provisioning(
        self,
    ) -> Optional[outputs.DefenderForServersAwsOfferingResponseArcAutoProvisioning]: ...
    @_builtins.property
    @pulumi.getter(name="defenderForServers")
    def defender_for_servers(
        self,
    ) -> Optional[outputs.DefenderForServersAwsOfferingResponseDefenderForServers]: ...
    @_builtins.property
    @pulumi.getter(name="mdeAutoProvisioning")
    def mde_auto_provisioning(
        self,
    ) -> Optional[outputs.DefenderForServersAwsOfferingResponseMdeAutoProvisioning]: ...
    @_builtins.property
    @pulumi.getter(name="subPlan")
    def sub_plan(
        self,
    ) -> Optional[outputs.DefenderForServersAwsOfferingResponseSubPlan]: ...
    @_builtins.property
    @pulumi.getter(name="vaAutoProvisioning")
    def va_auto_provisioning(
        self,
    ) -> Optional[outputs.DefenderForServersAwsOfferingResponseVaAutoProvisioning]: ...
    @_builtins.property
    @pulumi.getter(name="vmScanners")
    def vm_scanners(
        self,
    ) -> Optional[outputs.DefenderForServersAwsOfferingResponseVmScanners]: ...

@pulumi.output_type
class DefenderForServersAwsOfferingResponseArcAutoProvisioning(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        configuration: Optional[outputs.ArcAutoProvisioningResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.ArcAutoProvisioningResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForServersAwsOfferingResponseConfiguration(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForServersAwsOfferingResponseDefenderForServers(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cloud_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForServersAwsOfferingResponseMdeAutoProvisioning(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[Any] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForServersAwsOfferingResponseSubPlan(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForServersAwsOfferingResponseVaAutoProvisioning(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[
            outputs.DefenderForServersAwsOfferingResponseConfiguration
        ] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.DefenderForServersAwsOfferingResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForServersAwsOfferingResponseVmScanners(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_role_arn: Optional[_builtins.str] = ...,
        configuration: Optional[outputs.VmScannersBaseResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.VmScannersBaseResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForServersGcpOfferingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        offering_type: _builtins.str,
        arc_auto_provisioning: Optional[
            outputs.DefenderForServersGcpOfferingResponseArcAutoProvisioning
        ] = ...,
        defender_for_servers: Optional[
            outputs.DefenderForServersGcpOfferingResponseDefenderForServers
        ] = ...,
        mde_auto_provisioning: Optional[
            outputs.DefenderForServersGcpOfferingResponseMdeAutoProvisioning
        ] = ...,
        sub_plan: Optional[outputs.DefenderForServersGcpOfferingResponseSubPlan] = ...,
        va_auto_provisioning: Optional[
            outputs.DefenderForServersGcpOfferingResponseVaAutoProvisioning
        ] = ...,
        vm_scanners: Optional[
            outputs.DefenderForServersGcpOfferingResponseVmScanners
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arcAutoProvisioning")
    def arc_auto_provisioning(
        self,
    ) -> Optional[outputs.DefenderForServersGcpOfferingResponseArcAutoProvisioning]: ...
    @_builtins.property
    @pulumi.getter(name="defenderForServers")
    def defender_for_servers(
        self,
    ) -> Optional[outputs.DefenderForServersGcpOfferingResponseDefenderForServers]: ...
    @_builtins.property
    @pulumi.getter(name="mdeAutoProvisioning")
    def mde_auto_provisioning(
        self,
    ) -> Optional[outputs.DefenderForServersGcpOfferingResponseMdeAutoProvisioning]: ...
    @_builtins.property
    @pulumi.getter(name="subPlan")
    def sub_plan(
        self,
    ) -> Optional[outputs.DefenderForServersGcpOfferingResponseSubPlan]: ...
    @_builtins.property
    @pulumi.getter(name="vaAutoProvisioning")
    def va_auto_provisioning(
        self,
    ) -> Optional[outputs.DefenderForServersGcpOfferingResponseVaAutoProvisioning]: ...
    @_builtins.property
    @pulumi.getter(name="vmScanners")
    def vm_scanners(
        self,
    ) -> Optional[outputs.DefenderForServersGcpOfferingResponseVmScanners]: ...

@pulumi.output_type
class DefenderForServersGcpOfferingResponseArcAutoProvisioning(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[outputs.ArcAutoProvisioningResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.ArcAutoProvisioningResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForServersGcpOfferingResponseConfiguration(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForServersGcpOfferingResponseDefenderForServers(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForServersGcpOfferingResponseMdeAutoProvisioning(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[Any] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForServersGcpOfferingResponseSubPlan(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefenderForServersGcpOfferingResponseVaAutoProvisioning(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[
            outputs.DefenderForServersGcpOfferingResponseConfiguration
        ] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.DefenderForServersGcpOfferingResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForServersGcpOfferingResponseVmScanners(dict):
    def __init__(
        __self__,
        *,
        configuration: Optional[outputs.VmScannersBaseResponseConfiguration] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.VmScannersBaseResponseConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefenderForStorageSettingPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_enabled: Optional[_builtins.bool] = ...,
        malware_scanning: Optional[outputs.MalwareScanningPropertiesResponse] = ...,
        override_subscription_level_settings: Optional[_builtins.bool] = ...,
        sensitive_data_discovery: Optional[
            outputs.SensitiveDataDiscoveryPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="malwareScanning")
    def malware_scanning(
        self,
    ) -> Optional[outputs.MalwareScanningPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="overrideSubscriptionLevelSettings")
    def override_subscription_level_settings(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sensitiveDataDiscovery")
    def sensitive_data_discovery(
        self,
    ) -> Optional[outputs.SensitiveDataDiscoveryPropertiesResponse]: ...

@pulumi.output_type
class DenylistCustomAlertRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        denylist_values: Sequence[_builtins.str],
        description: _builtins.str,
        display_name: _builtins.str,
        is_enabled: _builtins.bool,
        rule_type: _builtins.str,
        value_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="denylistValues")
    def denylist_values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> _builtins.str: ...

@pulumi.output_type
class DevOpsCapabilityResponse(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class DevOpsConfigurationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capabilities: Sequence[outputs.DevOpsCapabilityResponse],
        provisioning_status_message: _builtins.str,
        provisioning_status_update_time_utc: _builtins.str,
        authorization: Optional[outputs.AuthorizationResponse] = ...,
        auto_discovery: Optional[_builtins.str] = ...,
        provisioning_state: Optional[_builtins.str] = ...,
        top_level_inventory_list: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Sequence[outputs.DevOpsCapabilityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatusMessage")
    def provisioning_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatusUpdateTimeUtc")
    def provisioning_status_update_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> Optional[outputs.AuthorizationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="autoDiscovery")
    def auto_discovery(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topLevelInventoryList")
    def top_level_inventory_list(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DockerHubEnvironmentDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        environment_type: _builtins.str,
        authentication: Optional[outputs.AccessTokenAuthenticationResponse] = ...,
        scan_interval: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.AccessTokenAuthenticationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scanInterval")
    def scan_interval(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ExtensionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_enabled: _builtins.str,
        name: _builtins.str,
        operation_status: outputs.OperationStatusResponse,
        additional_extension_properties: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> outputs.OperationStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensionProperties")
    def additional_extension_properties(self) -> Optional[Any]: ...

@pulumi.output_type
class GcpOrganizationalDataMemberResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        organization_membership_type: _builtins.str,
        management_project_number: Optional[_builtins.str] = ...,
        parent_hierarchy_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="organizationMembershipType")
    def organization_membership_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managementProjectNumber")
    def management_project_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parentHierarchyId")
    def parent_hierarchy_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GcpOrganizationalDataOrganizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        organization_membership_type: _builtins.str,
        organization_name: _builtins.str,
        excluded_project_numbers: Optional[Sequence[_builtins.str]] = ...,
        service_account_email_address: Optional[_builtins.str] = ...,
        workload_identity_provider_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="organizationMembershipType")
    def organization_membership_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="excludedProjectNumbers")
    def excluded_project_numbers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GcpProjectDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        project_name: _builtins.str,
        workload_identity_pool_id: _builtins.str,
        project_id: Optional[_builtins.str] = ...,
        project_number: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GcpProjectEnvironmentDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        environment_type: _builtins.str,
        organizational_data: Optional[Any] = ...,
        project_details: Optional[outputs.GcpProjectDetailsResponse] = ...,
        scan_interval: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationalData")
    def organizational_data(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="projectDetails")
    def project_details(self) -> Optional[outputs.GcpProjectDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scanInterval")
    def scan_interval(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class GitHubOwnerPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        git_hub_internal_id: _builtins.str,
        owner_url: _builtins.str,
        provisioning_status_message: _builtins.str,
        provisioning_status_update_time_utc: _builtins.str,
        onboarding_state: Optional[_builtins.str] = ...,
        provisioning_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitHubInternalId")
    def git_hub_internal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ownerUrl")
    def owner_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatusMessage")
    def provisioning_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatusUpdateTimeUtc")
    def provisioning_status_update_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onboardingState")
    def onboarding_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GitHubOwnerResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        properties: Optional[outputs.GitHubOwnerPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.GitHubOwnerPropertiesResponse]: ...

@pulumi.output_type
class GitLabGroupPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        fully_qualified_friendly_name: _builtins.str,
        fully_qualified_name: _builtins.str,
        provisioning_status_message: _builtins.str,
        provisioning_status_update_time_utc: _builtins.str,
        url: _builtins.str,
        onboarding_state: Optional[_builtins.str] = ...,
        provisioning_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedFriendlyName")
    def fully_qualified_friendly_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedName")
    def fully_qualified_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatusMessage")
    def provisioning_status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatusUpdateTimeUtc")
    def provisioning_status_update_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onboardingState")
    def onboarding_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GitLabGroupResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        properties: Optional[outputs.GitLabGroupPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.GitLabGroupPropertiesResponse]: ...

@pulumi.output_type
class GithubScopeEnvironmentDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, environment_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str: ...

@pulumi.output_type
class GitlabScopeEnvironmentDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, environment_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str: ...

@pulumi.output_type
class GovernanceAssignmentAdditionalDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ticket_link: Optional[_builtins.str] = ...,
        ticket_number: Optional[_builtins.int] = ...,
        ticket_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ticketLink")
    def ticket_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ticketNumber")
    def ticket_number(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ticketStatus")
    def ticket_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GovernanceEmailNotificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_manager_email_notification: Optional[_builtins.bool] = ...,
        disable_owner_email_notification: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableManagerEmailNotification")
    def disable_manager_email_notification(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableOwnerEmailNotification")
    def disable_owner_email_notification(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GovernanceRuleEmailNotificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_manager_email_notification: Optional[_builtins.bool] = ...,
        disable_owner_email_notification: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableManagerEmailNotification")
    def disable_manager_email_notification(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableOwnerEmailNotification")
    def disable_owner_email_notification(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GovernanceRuleMetadataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_by: _builtins.str,
        created_on: _builtins.str,
        updated_by: _builtins.str,
        updated_on: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedOn")
    def updated_on(self) -> _builtins.str: ...

@pulumi.output_type
class GovernanceRuleOwnerSourceResponse(dict):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JFrogEnvironmentDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        environment_type: _builtins.str,
        scan_interval: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanInterval")
    def scan_interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JitNetworkAccessPolicyVirtualMachineResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        ports: Sequence[outputs.JitNetworkAccessPortRuleResponse],
        public_ip_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[outputs.JitNetworkAccessPortRuleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JitNetworkAccessPortRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_request_access_duration: _builtins.str,
        number: _builtins.int,
        protocol: _builtins.str,
        allowed_source_address_prefix: Optional[_builtins.str] = ...,
        allowed_source_address_prefixes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequestAccessDuration")
    def max_request_access_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedSourceAddressPrefix")
    def allowed_source_address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedSourceAddressPrefixes")
    def allowed_source_address_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class JitNetworkAccessRequestPortResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time_utc: _builtins.str,
        number: _builtins.int,
        status: _builtins.str,
        status_reason: _builtins.str,
        allowed_source_address_prefix: Optional[_builtins.str] = ...,
        allowed_source_address_prefixes: Optional[Sequence[_builtins.str]] = ...,
        mapped_port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedSourceAddressPrefix")
    def allowed_source_address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedSourceAddressPrefixes")
    def allowed_source_address_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="mappedPort")
    def mapped_port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JitNetworkAccessRequestResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        requestor: _builtins.str,
        start_time_utc: _builtins.str,
        virtual_machines: Sequence[
            outputs.JitNetworkAccessRequestVirtualMachineResponse
        ],
        justification: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def requestor(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(
        self,
    ) -> Sequence[outputs.JitNetworkAccessRequestVirtualMachineResponse]: ...
    @_builtins.property
    @pulumi.getter
    def justification(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JitNetworkAccessRequestVirtualMachineResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        ports: Sequence[outputs.JitNetworkAccessRequestPortResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[outputs.JitNetworkAccessRequestPortResponse]: ...

@pulumi.output_type
class MalwareScanningPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operation_status: outputs.OperationStatusResponse,
        on_upload: Optional[outputs.OnUploadPropertiesResponse] = ...,
        scan_results_event_grid_topic_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> outputs.OperationStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="onUpload")
    def on_upload(self) -> Optional[outputs.OnUploadPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scanResultsEventGridTopicResourceId")
    def scan_results_event_grid_topic_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NotificationsSourceAlertResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_type: _builtins.str,
        minimal_severity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimalSeverity")
    def minimal_severity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NotificationsSourceAttackPathResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_type: _builtins.str,
        minimal_risk_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimalRiskLevel")
    def minimal_risk_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OnPremiseResourceDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        machine_name: _builtins.str,
        source: _builtins.str,
        source_computer_id: _builtins.str,
        vmuuid: _builtins.str,
        workspace_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceComputerId")
    def source_computer_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vmuuid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str: ...

@pulumi.output_type
class OnPremiseSqlResourceDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        machine_name: _builtins.str,
        server_name: _builtins.str,
        source: _builtins.str,
        source_computer_id: _builtins.str,
        vmuuid: _builtins.str,
        workspace_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceComputerId")
    def source_computer_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vmuuid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str: ...

@pulumi.output_type
class OnUploadPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cap_gb_per_month: Optional[_builtins.int] = ...,
        is_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capGBPerMonth")
    def cap_gb_per_month(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class OperationStatusResponse(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PartialAssessmentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, assessment_key: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentKey")
    def assessment_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_ids: Sequence[_builtins.str],
        id: _builtins.str,
        name: _builtins.str,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkResourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_id: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        required_members: Sequence[_builtins.str],
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        required_zone_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiredMembers")
    def required_members(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiredZoneNames")
    def required_zone_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecommendationConfigurationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        recommendation_type: _builtins.str,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recommendationType")
    def recommendation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class RemediationEtaResponse(dict):
    def __init__(
        __self__, *, eta: _builtins.str, justification: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eta(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def justification(self) -> _builtins.str: ...

@pulumi.output_type
class RuleResultsPropertiesResponse(dict):
    def __init__(
        __self__, *, results: Optional[Sequence[Sequence[_builtins.str]]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def results(self) -> Optional[Sequence[Sequence[_builtins.str]]]: ...

@pulumi.output_type
class ScopeElementResponse(dict):
    def __init__(__self__, *, field: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecurityAssessmentMetadataPartnerDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partner_name: _builtins.str,
        secret: _builtins.str,
        product_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecurityAssessmentMetadataPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assessment_type: _builtins.str,
        display_name: _builtins.str,
        policy_definition_id: _builtins.str,
        severity: _builtins.str,
        categories: Optional[Sequence[_builtins.str]] = ...,
        description: Optional[_builtins.str] = ...,
        implementation_effort: Optional[_builtins.str] = ...,
        partner_data: Optional[
            outputs.SecurityAssessmentMetadataPartnerDataResponse
        ] = ...,
        preview: Optional[_builtins.bool] = ...,
        remediation_description: Optional[_builtins.str] = ...,
        threats: Optional[Sequence[_builtins.str]] = ...,
        user_impact: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerData")
    def partner_data(
        self,
    ) -> Optional[outputs.SecurityAssessmentMetadataPartnerDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def threats(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userImpact")
    def user_impact(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecurityAssessmentMetadataPropertiesResponseResponsePublishDates(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, public: _builtins.str, g_a: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def public(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gA")
    def g_a(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecurityAssessmentPartnerDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, partner_name: _builtins.str, secret: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str: ...

@pulumi.output_type
class SecurityContactPropertiesResponseNotificationsByRole(dict):
    def __init__(
        __self__,
        *,
        roles: Optional[Sequence[_builtins.str]] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SensitiveDataDiscoveryPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operation_status: outputs.OperationStatusResponse,
        is_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> outputs.OperationStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StandardAssignmentMetadataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_by: _builtins.str,
        created_on: _builtins.str,
        last_updated_by: _builtins.str,
        last_updated_on: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedBy")
    def last_updated_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> _builtins.str: ...

@pulumi.output_type
class StandardAssignmentPropertiesResponseAttestationData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compliance_date: _builtins.str,
        assigned_assessment: Optional[outputs.AssignedAssessmentItemResponse] = ...,
        compliance_state: Optional[_builtins.str] = ...,
        evidence: Optional[Sequence[outputs.AttestationEvidenceResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceDate")
    def compliance_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="assignedAssessment")
    def assigned_assessment(
        self,
    ) -> Optional[outputs.AssignedAssessmentItemResponse]: ...
    @_builtins.property
    @pulumi.getter(name="complianceState")
    def compliance_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def evidence(self) -> Optional[Sequence[outputs.AttestationEvidenceResponse]]: ...

@pulumi.output_type
class StandardAssignmentPropertiesResponseExemptionData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assigned_assessment: Optional[outputs.AssignedAssessmentItemResponse] = ...,
        exemption_category: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignedAssessment")
    def assigned_assessment(
        self,
    ) -> Optional[outputs.AssignedAssessmentItemResponse]: ...
    @_builtins.property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StandardComponentPropertiesResponse(dict):
    def __init__(__self__, *, key: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StandardMetadataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_by: _builtins.str,
        created_on: _builtins.str,
        last_updated_by: _builtins.str,
        last_updated_on: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedBy")
    def last_updated_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> _builtins.str: ...

@pulumi.output_type
class SuppressionAlertsScopeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, all_of: Sequence[outputs.ScopeElementResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Sequence[outputs.ScopeElementResponse]: ...

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
class TargetBranchConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        annotate_default_branch: Optional[_builtins.str] = ...,
        branch_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="annotateDefaultBranch")
    def annotate_default_branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="branchNames")
    def branch_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ThresholdCustomAlertRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        display_name: _builtins.str,
        is_enabled: _builtins.bool,
        max_threshold: _builtins.int,
        min_threshold: _builtins.int,
        rule_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxThreshold")
    def max_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minThreshold")
    def min_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str: ...

@pulumi.output_type
class TimeWindowCustomAlertRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        display_name: _builtins.str,
        is_enabled: _builtins.bool,
        max_threshold: _builtins.int,
        min_threshold: _builtins.int,
        rule_type: _builtins.str,
        time_window_size: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxThreshold")
    def max_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minThreshold")
    def min_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeWindowSize")
    def time_window_size(self) -> _builtins.str: ...

@pulumi.output_type
class UserDefinedResourcesPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, query: _builtins.str, query_subscriptions: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="querySubscriptions")
    def query_subscriptions(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VmScannersBaseResponseConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exclusion_tags: Optional[Mapping[str, _builtins.str]] = ...,
        scanning_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exclusionTags")
    def exclusion_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scanningMode")
    def scanning_mode(self) -> Optional[_builtins.str]: ...
