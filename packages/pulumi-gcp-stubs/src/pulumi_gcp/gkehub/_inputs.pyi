

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FeatureFleetDefaultMemberConfigArgs', 'FeatureFleetDefaultMemberConfigArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'FeatureFleetDefaultMemberConfigMeshArgs', 'FeatureFleetDefaultMemberConfigMeshArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FeatureIamBindingConditionArgs', 'FeatureIamBindingConditionArgsDict', 'FeatureIamMemberConditionArgs', 'FeatureIamMemberConditionArgsDict', 'FeatureMembershipConfigmanagementArgs', 'FeatureMembershipConfigmanagementArgsDict', 'FeatureMembershipConfigmanagementConfigSyncArgs', ..., ..., ..., ..., ..., 'FeatureMembershipConfigmanagementConfigSyncGitArgs', ..., 'FeatureMembershipConfigmanagementConfigSyncOciArgs', ..., ..., ..., ..., ..., ..., ..., 'FeatureMembershipMeshArgs', 'FeatureMembershipMeshArgsDict', 'FeatureMembershipPolicycontrollerArgs', 'FeatureMembershipPolicycontrollerArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FeatureResourceStateArgs', 'FeatureResourceStateArgsDict', 'FeatureSpecArgs', 'FeatureSpecArgsDict', 'FeatureSpecClusterupgradeArgs', 'FeatureSpecClusterupgradeArgsDict', 'FeatureSpecClusterupgradeGkeUpgradeOverrideArgs', ..., ..., ..., ..., ..., 'FeatureSpecClusterupgradePostConditionsArgs', 'FeatureSpecClusterupgradePostConditionsArgsDict', 'FeatureSpecFleetobservabilityArgs', 'FeatureSpecFleetobservabilityArgsDict', 'FeatureSpecFleetobservabilityLoggingConfigArgs', 'FeatureSpecFleetobservabilityLoggingConfigArgsDict', ..., ..., ..., ..., 'FeatureSpecMulticlusteringressArgs', 'FeatureSpecMulticlusteringressArgsDict', 'FeatureSpecRbacrolebindingactuationArgs', 'FeatureSpecRbacrolebindingactuationArgsDict', 'FeatureSpecWorkloadidentityArgs', 'FeatureSpecWorkloadidentityArgsDict', 'FeatureStateArgs', 'FeatureStateArgsDict', 'FeatureStateStateArgs', 'FeatureStateStateArgsDict', 'FleetDefaultClusterConfigArgs', 'FleetDefaultClusterConfigArgsDict', ..., ..., ..., ..., 'FleetDefaultClusterConfigSecurityPostureConfigArgs', ..., 'FleetStateArgs', 'FleetStateArgsDict', 'MembershipAuthorityArgs', 'MembershipAuthorityArgsDict', 'MembershipBindingStateArgs', 'MembershipBindingStateArgsDict', 'MembershipEndpointArgs', 'MembershipEndpointArgsDict', 'MembershipEndpointGkeClusterArgs', 'MembershipEndpointGkeClusterArgsDict', 'MembershipIamBindingConditionArgs', 'MembershipIamBindingConditionArgsDict', 'MembershipIamMemberConditionArgs', 'MembershipIamMemberConditionArgsDict', 'MembershipRbacRoleBindingRoleArgs', 'MembershipRbacRoleBindingRoleArgsDict', 'MembershipRbacRoleBindingStateArgs', 'MembershipRbacRoleBindingStateArgsDict', 'NamespaceStateArgs', 'NamespaceStateArgsDict', 'RolloutSequenceStageArgs', 'RolloutSequenceStageArgsDict', 'RolloutSequenceStageClusterSelectorArgs', 'RolloutSequenceStageClusterSelectorArgsDict', 'ScopeIamBindingConditionArgs', 'ScopeIamBindingConditionArgsDict', 'ScopeIamMemberConditionArgs', 'ScopeIamMemberConditionArgsDict', 'ScopeRbacRoleBindingRoleArgs', 'ScopeRbacRoleBindingRoleArgsDict', 'ScopeRbacRoleBindingStateArgs', 'ScopeRbacRoleBindingStateArgsDict', 'ScopeStateArgs', 'ScopeStateArgsDict']
class FeatureFleetDefaultMemberConfigArgsDict(TypedDict):
    configmanagement: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementArgsDict]]
    mesh: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigMeshArgsDict]]
    policycontroller: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerArgsDict]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigArgs:
    def __init__(__self__, *, configmanagement: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementArgs]] = ..., mesh: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigMeshArgs]] = ..., policycontroller: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configmanagement(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementArgs]]:
        
        ...
    
    @configmanagement.setter
    def configmanagement(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mesh(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigMeshArgs]]:
        
        ...
    
    @mesh.setter
    def mesh(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigMeshArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policycontroller(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerArgs]]:
        
        ...
    
    @policycontroller.setter
    def policycontroller(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerArgs]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigConfigmanagementArgsDict(TypedDict):
    config_sync: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncArgsDict]]
    management: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigConfigmanagementArgs:
    def __init__(__self__, *, config_sync: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncArgs]] = ..., management: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configSync")
    def config_sync(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncArgs]]:
        
        ...
    
    @config_sync.setter
    def config_sync(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @management.setter
    def management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    git: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitArgsDict]]
    metrics_gcp_service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    oci: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciArgsDict]]
    prevent_drift: NotRequired[pulumi.Input[_builtins.bool]]
    source_format: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., git: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitArgs]] = ..., metrics_gcp_service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., oci: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciArgs]] = ..., prevent_drift: Optional[pulumi.Input[_builtins.bool]] = ..., source_format: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def git(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitArgs]]:
        
        ...
    
    @git.setter
    def git(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsGcpServiceAccountEmail")
    def metrics_gcp_service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metrics_gcp_service_account_email.setter
    def metrics_gcp_service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def oci(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciArgs]]:
        
        ...
    
    @oci.setter
    def oci(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preventDrift")
    def prevent_drift(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @prevent_drift.setter
    def prevent_drift(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_format.setter
    def source_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitArgsDict(TypedDict):
    secret_type: pulumi.Input[_builtins.str]
    gcp_service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    https_proxy: NotRequired[pulumi.Input[_builtins.str]]
    policy_dir: NotRequired[pulumi.Input[_builtins.str]]
    sync_branch: NotRequired[pulumi.Input[_builtins.str]]
    sync_repo: NotRequired[pulumi.Input[_builtins.str]]
    sync_rev: NotRequired[pulumi.Input[_builtins.str]]
    sync_wait_secs: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitArgs:
    def __init__(__self__, *, secret_type: pulumi.Input[_builtins.str], gcp_service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., https_proxy: Optional[pulumi.Input[_builtins.str]] = ..., policy_dir: Optional[pulumi.Input[_builtins.str]] = ..., sync_branch: Optional[pulumi.Input[_builtins.str]] = ..., sync_repo: Optional[pulumi.Input[_builtins.str]] = ..., sync_rev: Optional[pulumi.Input[_builtins.str]] = ..., sync_wait_secs: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_type.setter
    def secret_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcp_service_account_email.setter
    def gcp_service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @https_proxy.setter
    def https_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_dir.setter
    def policy_dir(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncBranch")
    def sync_branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_branch.setter
    def sync_branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_repo.setter
    def sync_repo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncRev")
    def sync_rev(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_rev.setter
    def sync_rev(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_wait_secs.setter
    def sync_wait_secs(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciArgsDict(TypedDict):
    secret_type: pulumi.Input[_builtins.str]
    gcp_service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    policy_dir: NotRequired[pulumi.Input[_builtins.str]]
    sync_repo: NotRequired[pulumi.Input[_builtins.str]]
    sync_wait_secs: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciArgs:
    def __init__(__self__, *, secret_type: pulumi.Input[_builtins.str], gcp_service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., policy_dir: Optional[pulumi.Input[_builtins.str]] = ..., sync_repo: Optional[pulumi.Input[_builtins.str]] = ..., sync_wait_secs: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_type.setter
    def secret_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcp_service_account_email.setter
    def gcp_service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_dir.setter
    def policy_dir(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_repo.setter
    def sync_repo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_wait_secs.setter
    def sync_wait_secs(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigMeshArgsDict(TypedDict):
    management: pulumi.Input[_builtins.str]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigMeshArgs:
    def __init__(__self__, *, management: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def management(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @management.setter
    def management(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerArgsDict(TypedDict):
    policy_controller_hub_config: pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigArgsDict]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerArgs:
    def __init__(__self__, *, policy_controller_hub_config: pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigArgs], version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyControllerHubConfig")
    def policy_controller_hub_config(self) -> pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigArgs]:
        
        ...
    
    @policy_controller_hub_config.setter
    def policy_controller_hub_config(self, value: pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigArgsDict(TypedDict):
    install_spec: pulumi.Input[_builtins.str]
    audit_interval_seconds: NotRequired[pulumi.Input[_builtins.int]]
    constraint_violation_limit: NotRequired[pulumi.Input[_builtins.int]]
    deployment_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgsDict]]]]
    exemptable_namespaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    log_denies_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    monitoring: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringArgsDict]]
    mutation_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    policy_content: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentArgsDict]]
    referential_rules_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigArgs:
    def __init__(__self__, *, install_spec: pulumi.Input[_builtins.str], audit_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ..., constraint_violation_limit: Optional[pulumi.Input[_builtins.int]] = ..., deployment_configs: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgs]]]] = ..., exemptable_namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_denies_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., monitoring: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringArgs]] = ..., mutation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy_content: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentArgs]] = ..., referential_rules_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installSpec")
    def install_spec(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @install_spec.setter
    def install_spec(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditIntervalSeconds")
    def audit_interval_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @audit_interval_seconds.setter
    def audit_interval_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="constraintViolationLimit")
    def constraint_violation_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @constraint_violation_limit.setter
    def constraint_violation_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigs")
    def deployment_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgs]]]]:
        
        ...
    
    @deployment_configs.setter
    def deployment_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptableNamespaces")
    def exemptable_namespaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exemptable_namespaces.setter
    def exemptable_namespaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDeniesEnabled")
    def log_denies_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_denies_enabled.setter
    def log_denies_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringArgs]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutationEnabled")
    def mutation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @mutation_enabled.setter
    def mutation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyContent")
    def policy_content(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentArgs]]:
        
        ...
    
    @policy_content.setter
    def policy_content(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referentialRulesEnabled")
    def referential_rules_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @referential_rules_enabled.setter
    def referential_rules_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgsDict(TypedDict):
    component: pulumi.Input[_builtins.str]
    container_resources: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgsDict]]
    pod_affinity: NotRequired[pulumi.Input[_builtins.str]]
    pod_tolerations: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgsDict]]]]
    replica_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgs:
    def __init__(__self__, *, component: pulumi.Input[_builtins.str], container_resources: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgs]] = ..., pod_affinity: Optional[pulumi.Input[_builtins.str]] = ..., pod_tolerations: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgs]]]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def component(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @component.setter
    def component(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerResources")
    def container_resources(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgs]]:
        
        ...
    
    @container_resources.setter
    def container_resources(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAffinity")
    def pod_affinity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pod_affinity.setter
    def pod_affinity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podTolerations")
    def pod_tolerations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgs]]]]:
        
        ...
    
    @pod_tolerations.setter
    def pod_tolerations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgsDict(TypedDict):
    limits: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgsDict]]
    requests: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgsDict]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgs:
    def __init__(__self__, *, limits: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgs]] = ..., requests: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgs]]:
        
        ...
    
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgs]]:
        
        ...
    
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgs]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.str]]
    memory: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgs:
    def __init__(__self__, *, cpu: Optional[pulumi.Input[_builtins.str]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.str]]
    memory: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgs:
    def __init__(__self__, *, cpu: Optional[pulumi.Input[_builtins.str]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgsDict(TypedDict):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    operator: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgs:
    def __init__(__self__, *, effect: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., operator: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringArgsDict(TypedDict):
    backends: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringArgs:
    def __init__(__self__, *, backends: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @backends.setter
    def backends(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentArgsDict(TypedDict):
    bundles: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgsDict]]]]
    template_library: NotRequired[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgsDict]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentArgs:
    def __init__(__self__, *, bundles: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgs]]]] = ..., template_library: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bundles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgs]]]]:
        
        ...
    
    @bundles.setter
    def bundles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateLibrary")
    def template_library(self) -> Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgs]]:
        
        ...
    
    @template_library.setter
    def template_library(self, value: Optional[pulumi.Input[FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgs]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgsDict(TypedDict):
    bundle: pulumi.Input[_builtins.str]
    exempted_namespaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgs:
    def __init__(__self__, *, bundle: pulumi.Input[_builtins.str], exempted_namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bundle(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bundle.setter
    def bundle(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptedNamespaces")
    def exempted_namespaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exempted_namespaces.setter
    def exempted_namespaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgsDict(TypedDict):
    installation: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgs:
    def __init__(__self__, *, installation: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def installation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @installation.setter
    def installation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementArgsDict(TypedDict):
    config_sync: NotRequired[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncArgsDict]]
    hierarchy_controller: NotRequired[pulumi.Input[FeatureMembershipConfigmanagementHierarchyControllerArgsDict]]
    management: NotRequired[pulumi.Input[_builtins.str]]
    policy_controller: NotRequired[pulumi.Input[FeatureMembershipConfigmanagementPolicyControllerArgsDict]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipConfigmanagementArgs:
    def __init__(__self__, *, config_sync: Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncArgs]] = ..., hierarchy_controller: Optional[pulumi.Input[FeatureMembershipConfigmanagementHierarchyControllerArgs]] = ..., management: Optional[pulumi.Input[_builtins.str]] = ..., policy_controller: Optional[pulumi.Input[FeatureMembershipConfigmanagementPolicyControllerArgs]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configSync")
    def config_sync(self) -> Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncArgs]]:
        
        ...
    
    @config_sync.setter
    def config_sync(self, value: Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchyController")
    def hierarchy_controller(self) -> Optional[pulumi.Input[FeatureMembershipConfigmanagementHierarchyControllerArgs]]:
        
        ...
    
    @hierarchy_controller.setter
    def hierarchy_controller(self, value: Optional[pulumi.Input[FeatureMembershipConfigmanagementHierarchyControllerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @management.setter
    def management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyController")
    def policy_controller(self) -> Optional[pulumi.Input[FeatureMembershipConfigmanagementPolicyControllerArgs]]:
        
        ...
    
    @policy_controller.setter
    def policy_controller(self, value: Optional[pulumi.Input[FeatureMembershipConfigmanagementPolicyControllerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementConfigSyncArgsDict(TypedDict):
    deployment_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideArgsDict]]]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    git: NotRequired[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncGitArgsDict]]
    metrics_gcp_service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    oci: NotRequired[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncOciArgsDict]]
    prevent_drift: NotRequired[pulumi.Input[_builtins.bool]]
    source_format: NotRequired[pulumi.Input[_builtins.str]]
    stop_syncing: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FeatureMembershipConfigmanagementConfigSyncArgs:
    def __init__(__self__, *, deployment_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideArgs]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., git: Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncGitArgs]] = ..., metrics_gcp_service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., oci: Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncOciArgs]] = ..., prevent_drift: Optional[pulumi.Input[_builtins.bool]] = ..., source_format: Optional[pulumi.Input[_builtins.str]] = ..., stop_syncing: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentOverrides")
    def deployment_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideArgs]]]]:
        
        ...
    
    @deployment_overrides.setter
    def deployment_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def git(self) -> Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncGitArgs]]:
        
        ...
    
    @git.setter
    def git(self, value: Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncGitArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsGcpServiceAccountEmail")
    def metrics_gcp_service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metrics_gcp_service_account_email.setter
    def metrics_gcp_service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def oci(self) -> Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncOciArgs]]:
        
        ...
    
    @oci.setter
    def oci(self, value: Optional[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncOciArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preventDrift")
    def prevent_drift(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @prevent_drift.setter
    def prevent_drift(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_format.setter
    def source_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stopSyncing")
    def stop_syncing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @stop_syncing.setter
    def stop_syncing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideArgsDict(TypedDict):
    containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainerArgsDict]]]]
    deployment_name: NotRequired[pulumi.Input[_builtins.str]]
    deployment_namespace: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideArgs:
    def __init__(__self__, *, containers: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainerArgs]]]] = ..., deployment_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_namespace: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainerArgs]]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentNamespace")
    def deployment_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_namespace.setter
    def deployment_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainerArgsDict(TypedDict):
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    cpu_limit: NotRequired[pulumi.Input[_builtins.str]]
    cpu_request: NotRequired[pulumi.Input[_builtins.str]]
    memory_limit: NotRequired[pulumi.Input[_builtins.str]]
    memory_request: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainerArgs:
    def __init__(__self__, *, container_name: Optional[pulumi.Input[_builtins.str]] = ..., cpu_limit: Optional[pulumi.Input[_builtins.str]] = ..., cpu_request: Optional[pulumi.Input[_builtins.str]] = ..., memory_limit: Optional[pulumi.Input[_builtins.str]] = ..., memory_request: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuLimit")
    def cpu_limit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu_limit.setter
    def cpu_limit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuRequest")
    def cpu_request(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu_request.setter
    def cpu_request(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryLimit")
    def memory_limit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory_limit.setter
    def memory_limit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryRequest")
    def memory_request(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory_request.setter
    def memory_request(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementConfigSyncGitArgsDict(TypedDict):
    gcp_service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    https_proxy: NotRequired[pulumi.Input[_builtins.str]]
    policy_dir: NotRequired[pulumi.Input[_builtins.str]]
    secret_type: NotRequired[pulumi.Input[_builtins.str]]
    sync_branch: NotRequired[pulumi.Input[_builtins.str]]
    sync_repo: NotRequired[pulumi.Input[_builtins.str]]
    sync_rev: NotRequired[pulumi.Input[_builtins.str]]
    sync_wait_secs: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipConfigmanagementConfigSyncGitArgs:
    def __init__(__self__, *, gcp_service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., https_proxy: Optional[pulumi.Input[_builtins.str]] = ..., policy_dir: Optional[pulumi.Input[_builtins.str]] = ..., secret_type: Optional[pulumi.Input[_builtins.str]] = ..., sync_branch: Optional[pulumi.Input[_builtins.str]] = ..., sync_repo: Optional[pulumi.Input[_builtins.str]] = ..., sync_rev: Optional[pulumi.Input[_builtins.str]] = ..., sync_wait_secs: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcp_service_account_email.setter
    def gcp_service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @https_proxy.setter
    def https_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_dir.setter
    def policy_dir(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_type.setter
    def secret_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncBranch")
    def sync_branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_branch.setter
    def sync_branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_repo.setter
    def sync_repo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncRev")
    def sync_rev(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_rev.setter
    def sync_rev(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_wait_secs.setter
    def sync_wait_secs(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementConfigSyncOciArgsDict(TypedDict):
    gcp_service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    policy_dir: NotRequired[pulumi.Input[_builtins.str]]
    secret_type: NotRequired[pulumi.Input[_builtins.str]]
    sync_repo: NotRequired[pulumi.Input[_builtins.str]]
    sync_wait_secs: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipConfigmanagementConfigSyncOciArgs:
    def __init__(__self__, *, gcp_service_account_email: Optional[pulumi.Input[_builtins.str]] = ..., policy_dir: Optional[pulumi.Input[_builtins.str]] = ..., secret_type: Optional[pulumi.Input[_builtins.str]] = ..., sync_repo: Optional[pulumi.Input[_builtins.str]] = ..., sync_wait_secs: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcp_service_account_email.setter
    def gcp_service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_dir.setter
    def policy_dir(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_type.setter
    def secret_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_repo.setter
    def sync_repo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_wait_secs.setter
    def sync_wait_secs(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementHierarchyControllerArgsDict(TypedDict):
    enable_hierarchical_resource_quota: NotRequired[pulumi.Input[_builtins.bool]]
    enable_pod_tree_labels: NotRequired[pulumi.Input[_builtins.bool]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FeatureMembershipConfigmanagementHierarchyControllerArgs:
    def __init__(__self__, *, enable_hierarchical_resource_quota: Optional[pulumi.Input[_builtins.bool]] = ..., enable_pod_tree_labels: Optional[pulumi.Input[_builtins.bool]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHierarchicalResourceQuota")
    def enable_hierarchical_resource_quota(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_hierarchical_resource_quota.setter
    def enable_hierarchical_resource_quota(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePodTreeLabels")
    def enable_pod_tree_labels(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_pod_tree_labels.setter
    def enable_pod_tree_labels(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementPolicyControllerArgsDict(TypedDict):
    audit_interval_seconds: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    exemptable_namespaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    log_denies_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    monitoring: NotRequired[pulumi.Input[FeatureMembershipConfigmanagementPolicyControllerMonitoringArgsDict]]
    mutation_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    referential_rules_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    template_library_installed: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FeatureMembershipConfigmanagementPolicyControllerArgs:
    def __init__(__self__, *, audit_interval_seconds: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., exemptable_namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_denies_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., monitoring: Optional[pulumi.Input[FeatureMembershipConfigmanagementPolicyControllerMonitoringArgs]] = ..., mutation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., referential_rules_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., template_library_installed: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditIntervalSeconds")
    def audit_interval_seconds(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @audit_interval_seconds.setter
    def audit_interval_seconds(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptableNamespaces")
    def exemptable_namespaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exemptable_namespaces.setter
    def exemptable_namespaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDeniesEnabled")
    def log_denies_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_denies_enabled.setter
    def log_denies_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[FeatureMembershipConfigmanagementPolicyControllerMonitoringArgs]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[FeatureMembershipConfigmanagementPolicyControllerMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutationEnabled")
    def mutation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @mutation_enabled.setter
    def mutation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referentialRulesEnabled")
    def referential_rules_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @referential_rules_enabled.setter
    def referential_rules_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateLibraryInstalled")
    def template_library_installed(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @template_library_installed.setter
    def template_library_installed(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FeatureMembershipConfigmanagementPolicyControllerMonitoringArgsDict(TypedDict):
    backends: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FeatureMembershipConfigmanagementPolicyControllerMonitoringArgs:
    def __init__(__self__, *, backends: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @backends.setter
    def backends(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FeatureMembershipMeshArgsDict(TypedDict):
    control_plane: NotRequired[pulumi.Input[_builtins.str]]
    management: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipMeshArgs:
    def __init__(__self__, *, control_plane: Optional[pulumi.Input[_builtins.str]] = ..., management: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    @_utilities.deprecated("""Deprecated in favor of the `management` field""")
    def control_plane(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @management.setter
    def management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerArgsDict(TypedDict):
    policy_controller_hub_config: pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigArgsDict]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerArgs:
    def __init__(__self__, *, policy_controller_hub_config: pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigArgs], version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyControllerHubConfig")
    def policy_controller_hub_config(self) -> pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigArgs]:
        
        ...
    
    @policy_controller_hub_config.setter
    def policy_controller_hub_config(self, value: pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigArgsDict(TypedDict):
    audit_interval_seconds: NotRequired[pulumi.Input[_builtins.int]]
    constraint_violation_limit: NotRequired[pulumi.Input[_builtins.int]]
    deployment_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgsDict]]]]
    exemptable_namespaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    install_spec: NotRequired[pulumi.Input[_builtins.str]]
    log_denies_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    monitoring: NotRequired[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoringArgsDict]]
    mutation_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    policy_content: NotRequired[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentArgsDict]]
    referential_rules_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigArgs:
    def __init__(__self__, *, audit_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ..., constraint_violation_limit: Optional[pulumi.Input[_builtins.int]] = ..., deployment_configs: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgs]]]] = ..., exemptable_namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., install_spec: Optional[pulumi.Input[_builtins.str]] = ..., log_denies_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., monitoring: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoringArgs]] = ..., mutation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policy_content: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentArgs]] = ..., referential_rules_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditIntervalSeconds")
    def audit_interval_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @audit_interval_seconds.setter
    def audit_interval_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="constraintViolationLimit")
    def constraint_violation_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @constraint_violation_limit.setter
    def constraint_violation_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfigs")
    def deployment_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgs]]]]:
        
        ...
    
    @deployment_configs.setter
    def deployment_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptableNamespaces")
    def exemptable_namespaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exemptable_namespaces.setter
    def exemptable_namespaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="installSpec")
    def install_spec(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @install_spec.setter
    def install_spec(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDeniesEnabled")
    def log_denies_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_denies_enabled.setter
    def log_denies_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoringArgs]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutationEnabled")
    def mutation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @mutation_enabled.setter
    def mutation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyContent")
    def policy_content(self) -> Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentArgs]]:
        
        ...
    
    @policy_content.setter
    def policy_content(self, value: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referentialRulesEnabled")
    def referential_rules_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @referential_rules_enabled.setter
    def referential_rules_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgsDict(TypedDict):
    component_name: pulumi.Input[_builtins.str]
    container_resources: NotRequired[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgsDict]]
    pod_affinity: NotRequired[pulumi.Input[_builtins.str]]
    pod_tolerations: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgsDict]]]]
    replica_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigArgs:
    def __init__(__self__, *, component_name: pulumi.Input[_builtins.str], container_resources: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgs]] = ..., pod_affinity: Optional[pulumi.Input[_builtins.str]] = ..., pod_tolerations: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgs]]]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @component_name.setter
    def component_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerResources")
    def container_resources(self) -> Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgs]]:
        
        ...
    
    @container_resources.setter
    def container_resources(self, value: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAffinity")
    def pod_affinity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pod_affinity.setter
    def pod_affinity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podTolerations")
    def pod_tolerations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgs]]]]:
        
        ...
    
    @pod_tolerations.setter
    def pod_tolerations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgsDict(TypedDict):
    limits: NotRequired[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgsDict]]
    requests: NotRequired[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgsDict]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesArgs:
    def __init__(__self__, *, limits: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgs]] = ..., requests: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgs]]:
        
        ...
    
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgs]]:
        
        ...
    
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgs]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.str]]
    memory: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimitsArgs:
    def __init__(__self__, *, cpu: Optional[pulumi.Input[_builtins.str]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.str]]
    memory: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequestsArgs:
    def __init__(__self__, *, cpu: Optional[pulumi.Input[_builtins.str]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgsDict(TypedDict):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    operator: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationArgs:
    def __init__(__self__, *, effect: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., operator: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoringArgsDict(TypedDict):
    backends: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoringArgs:
    def __init__(__self__, *, backends: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @backends.setter
    def backends(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentArgsDict(TypedDict):
    bundles: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgsDict]]]]
    template_library: NotRequired[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgsDict]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentArgs:
    def __init__(__self__, *, bundles: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgs]]]] = ..., template_library: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bundles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgs]]]]:
        
        ...
    
    @bundles.setter
    def bundles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateLibrary")
    def template_library(self) -> Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgs]]:
        
        ...
    
    @template_library.setter
    def template_library(self, value: Optional[pulumi.Input[FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgs]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgsDict(TypedDict):
    bundle_name: pulumi.Input[_builtins.str]
    exempted_namespaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundleArgs:
    def __init__(__self__, *, bundle_name: pulumi.Input[_builtins.str], exempted_namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleName")
    def bundle_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bundle_name.setter
    def bundle_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptedNamespaces")
    def exempted_namespaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exempted_namespaces.setter
    def exempted_namespaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgsDict(TypedDict):
    installation: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryArgs:
    def __init__(__self__, *, installation: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def installation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @installation.setter
    def installation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureResourceStateArgsDict(TypedDict):
    has_resources: NotRequired[pulumi.Input[_builtins.bool]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureResourceStateArgs:
    def __init__(__self__, *, has_resources: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasResources")
    def has_resources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @has_resources.setter
    def has_resources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureSpecArgsDict(TypedDict):
    clusterupgrade: NotRequired[pulumi.Input[FeatureSpecClusterupgradeArgsDict]]
    fleetobservability: NotRequired[pulumi.Input[FeatureSpecFleetobservabilityArgsDict]]
    multiclusteringress: NotRequired[pulumi.Input[FeatureSpecMulticlusteringressArgsDict]]
    rbacrolebindingactuation: NotRequired[pulumi.Input[FeatureSpecRbacrolebindingactuationArgsDict]]
    workloadidentity: NotRequired[pulumi.Input[FeatureSpecWorkloadidentityArgsDict]]


@pulumi.input_type
class FeatureSpecArgs:
    def __init__(__self__, *, clusterupgrade: Optional[pulumi.Input[FeatureSpecClusterupgradeArgs]] = ..., fleetobservability: Optional[pulumi.Input[FeatureSpecFleetobservabilityArgs]] = ..., multiclusteringress: Optional[pulumi.Input[FeatureSpecMulticlusteringressArgs]] = ..., rbacrolebindingactuation: Optional[pulumi.Input[FeatureSpecRbacrolebindingactuationArgs]] = ..., workloadidentity: Optional[pulumi.Input[FeatureSpecWorkloadidentityArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusterupgrade(self) -> Optional[pulumi.Input[FeatureSpecClusterupgradeArgs]]:
        
        ...
    
    @clusterupgrade.setter
    def clusterupgrade(self, value: Optional[pulumi.Input[FeatureSpecClusterupgradeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleetobservability(self) -> Optional[pulumi.Input[FeatureSpecFleetobservabilityArgs]]:
        
        ...
    
    @fleetobservability.setter
    def fleetobservability(self, value: Optional[pulumi.Input[FeatureSpecFleetobservabilityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def multiclusteringress(self) -> Optional[pulumi.Input[FeatureSpecMulticlusteringressArgs]]:
        
        ...
    
    @multiclusteringress.setter
    def multiclusteringress(self, value: Optional[pulumi.Input[FeatureSpecMulticlusteringressArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rbacrolebindingactuation(self) -> Optional[pulumi.Input[FeatureSpecRbacrolebindingactuationArgs]]:
        
        ...
    
    @rbacrolebindingactuation.setter
    def rbacrolebindingactuation(self, value: Optional[pulumi.Input[FeatureSpecRbacrolebindingactuationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def workloadidentity(self) -> Optional[pulumi.Input[FeatureSpecWorkloadidentityArgs]]:
        
        ...
    
    @workloadidentity.setter
    def workloadidentity(self, value: Optional[pulumi.Input[FeatureSpecWorkloadidentityArgs]]): # -> None:
        ...
    


class FeatureSpecClusterupgradeArgsDict(TypedDict):
    upstream_fleets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    gke_upgrade_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverrideArgsDict]]]]
    post_conditions: NotRequired[pulumi.Input[FeatureSpecClusterupgradePostConditionsArgsDict]]


@pulumi.input_type
class FeatureSpecClusterupgradeArgs:
    def __init__(__self__, *, upstream_fleets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], gke_upgrade_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverrideArgs]]]] = ..., post_conditions: Optional[pulumi.Input[FeatureSpecClusterupgradePostConditionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upstreamFleets")
    def upstream_fleets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @upstream_fleets.setter
    def upstream_fleets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeUpgradeOverrides")
    def gke_upgrade_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverrideArgs]]]]:
        
        ...
    
    @gke_upgrade_overrides.setter
    def gke_upgrade_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverrideArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postConditions")
    def post_conditions(self) -> Optional[pulumi.Input[FeatureSpecClusterupgradePostConditionsArgs]]:
        
        ...
    
    @post_conditions.setter
    def post_conditions(self, value: Optional[pulumi.Input[FeatureSpecClusterupgradePostConditionsArgs]]): # -> None:
        ...
    


class FeatureSpecClusterupgradeGkeUpgradeOverrideArgsDict(TypedDict):
    post_conditions: pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverridePostConditionsArgsDict]
    upgrade: pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeArgsDict]


@pulumi.input_type
class FeatureSpecClusterupgradeGkeUpgradeOverrideArgs:
    def __init__(__self__, *, post_conditions: pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverridePostConditionsArgs], upgrade: pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postConditions")
    def post_conditions(self) -> pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverridePostConditionsArgs]:
        
        ...
    
    @post_conditions.setter
    def post_conditions(self, value: pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverridePostConditionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def upgrade(self) -> pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeArgs]:
        
        ...
    
    @upgrade.setter
    def upgrade(self, value: pulumi.Input[FeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeArgs]): # -> None:
        ...
    


class FeatureSpecClusterupgradeGkeUpgradeOverridePostConditionsArgsDict(TypedDict):
    soaking: pulumi.Input[_builtins.str]


@pulumi.input_type
class FeatureSpecClusterupgradeGkeUpgradeOverridePostConditionsArgs:
    def __init__(__self__, *, soaking: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def soaking(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @soaking.setter
    def soaking(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]


@pulumi.input_type
class FeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], version: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FeatureSpecClusterupgradePostConditionsArgsDict(TypedDict):
    soaking: pulumi.Input[_builtins.str]


@pulumi.input_type
class FeatureSpecClusterupgradePostConditionsArgs:
    def __init__(__self__, *, soaking: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def soaking(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @soaking.setter
    def soaking(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FeatureSpecFleetobservabilityArgsDict(TypedDict):
    logging_config: NotRequired[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigArgsDict]]


@pulumi.input_type
class FeatureSpecFleetobservabilityArgs:
    def __init__(__self__, *, logging_config: Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigArgs]]): # -> None:
        ...
    


class FeatureSpecFleetobservabilityLoggingConfigArgsDict(TypedDict):
    default_config: NotRequired[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigDefaultConfigArgsDict]]
    fleet_scope_logs_config: NotRequired[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigArgsDict]]


@pulumi.input_type
class FeatureSpecFleetobservabilityLoggingConfigArgs:
    def __init__(__self__, *, default_config: Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigDefaultConfigArgs]] = ..., fleet_scope_logs_config: Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultConfig")
    def default_config(self) -> Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigDefaultConfigArgs]]:
        
        ...
    
    @default_config.setter
    def default_config(self, value: Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigDefaultConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetScopeLogsConfig")
    def fleet_scope_logs_config(self) -> Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigArgs]]:
        
        ...
    
    @fleet_scope_logs_config.setter
    def fleet_scope_logs_config(self, value: Optional[pulumi.Input[FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigArgs]]): # -> None:
        ...
    


class FeatureSpecFleetobservabilityLoggingConfigDefaultConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureSpecFleetobservabilityLoggingConfigDefaultConfigArgs:
    def __init__(__self__, *, mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigArgs:
    def __init__(__self__, *, mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureSpecMulticlusteringressArgsDict(TypedDict):
    config_membership: pulumi.Input[_builtins.str]


@pulumi.input_type
class FeatureSpecMulticlusteringressArgs:
    def __init__(__self__, *, config_membership: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configMembership")
    def config_membership(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @config_membership.setter
    def config_membership(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FeatureSpecRbacrolebindingactuationArgsDict(TypedDict):
    allowed_custom_roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FeatureSpecRbacrolebindingactuationArgs:
    def __init__(__self__, *, allowed_custom_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedCustomRoles")
    def allowed_custom_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_custom_roles.setter
    def allowed_custom_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FeatureSpecWorkloadidentityArgsDict(TypedDict):
    scope_tenancy_pool: pulumi.Input[_builtins.str]


@pulumi.input_type
class FeatureSpecWorkloadidentityArgs:
    def __init__(__self__, *, scope_tenancy_pool: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeTenancyPool")
    def scope_tenancy_pool(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope_tenancy_pool.setter
    def scope_tenancy_pool(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FeatureStateArgsDict(TypedDict):
    states: NotRequired[pulumi.Input[Sequence[pulumi.Input[FeatureStateStateArgsDict]]]]


@pulumi.input_type
class FeatureStateArgs:
    def __init__(__self__, *, states: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureStateStateArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def states(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureStateStateArgs]]]]:
        
        ...
    
    @states.setter
    def states(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureStateStateArgs]]]]): # -> None:
        ...
    


class FeatureStateStateArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureStateStateArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetDefaultClusterConfigArgsDict(TypedDict):
    binary_authorization_config: NotRequired[pulumi.Input[FleetDefaultClusterConfigBinaryAuthorizationConfigArgsDict]]
    security_posture_config: NotRequired[pulumi.Input[FleetDefaultClusterConfigSecurityPostureConfigArgsDict]]


@pulumi.input_type
class FleetDefaultClusterConfigArgs:
    def __init__(__self__, *, binary_authorization_config: Optional[pulumi.Input[FleetDefaultClusterConfigBinaryAuthorizationConfigArgs]] = ..., security_posture_config: Optional[pulumi.Input[FleetDefaultClusterConfigSecurityPostureConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizationConfig")
    def binary_authorization_config(self) -> Optional[pulumi.Input[FleetDefaultClusterConfigBinaryAuthorizationConfigArgs]]:
        
        ...
    
    @binary_authorization_config.setter
    def binary_authorization_config(self, value: Optional[pulumi.Input[FleetDefaultClusterConfigBinaryAuthorizationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPostureConfig")
    def security_posture_config(self) -> Optional[pulumi.Input[FleetDefaultClusterConfigSecurityPostureConfigArgs]]:
        
        ...
    
    @security_posture_config.setter
    def security_posture_config(self, value: Optional[pulumi.Input[FleetDefaultClusterConfigSecurityPostureConfigArgs]]): # -> None:
        ...
    


class FleetDefaultClusterConfigBinaryAuthorizationConfigArgsDict(TypedDict):
    evaluation_mode: NotRequired[pulumi.Input[_builtins.str]]
    policy_bindings: NotRequired[pulumi.Input[Sequence[pulumi.Input[FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBindingArgsDict]]]]


@pulumi.input_type
class FleetDefaultClusterConfigBinaryAuthorizationConfigArgs:
    def __init__(__self__, *, evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ..., policy_bindings: Optional[pulumi.Input[Sequence[pulumi.Input[FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBindingArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @evaluation_mode.setter
    def evaluation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyBindings")
    def policy_bindings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBindingArgs]]]]:
        
        ...
    
    @policy_bindings.setter
    def policy_bindings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBindingArgs]]]]): # -> None:
        ...
    


class FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBindingArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBindingArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetDefaultClusterConfigSecurityPostureConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]
    vulnerability_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FleetDefaultClusterConfigSecurityPostureConfigArgs:
    def __init__(__self__, *, mode: Optional[pulumi.Input[_builtins.str]] = ..., vulnerability_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityMode")
    def vulnerability_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vulnerability_mode.setter
    def vulnerability_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetStateArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FleetStateArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MembershipAuthorityArgsDict(TypedDict):
    issuer: pulumi.Input[_builtins.str]


@pulumi.input_type
class MembershipAuthorityArgs:
    def __init__(__self__, *, issuer: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MembershipBindingStateArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MembershipBindingStateArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MembershipEndpointArgsDict(TypedDict):
    gke_cluster: NotRequired[pulumi.Input[MembershipEndpointGkeClusterArgsDict]]


@pulumi.input_type
class MembershipEndpointArgs:
    def __init__(__self__, *, gke_cluster: Optional[pulumi.Input[MembershipEndpointGkeClusterArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeCluster")
    def gke_cluster(self) -> Optional[pulumi.Input[MembershipEndpointGkeClusterArgs]]:
        
        ...
    
    @gke_cluster.setter
    def gke_cluster(self, value: Optional[pulumi.Input[MembershipEndpointGkeClusterArgs]]): # -> None:
        ...
    


class MembershipEndpointGkeClusterArgsDict(TypedDict):
    resource_link: pulumi.Input[_builtins.str]


@pulumi.input_type
class MembershipEndpointGkeClusterArgs:
    def __init__(__self__, *, resource_link: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLink")
    def resource_link(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_link.setter
    def resource_link(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MembershipIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MembershipIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MembershipIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MembershipIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MembershipRbacRoleBindingRoleArgsDict(TypedDict):
    predefined_role: pulumi.Input[_builtins.str]


@pulumi.input_type
class MembershipRbacRoleBindingRoleArgs:
    def __init__(__self__, *, predefined_role: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedRole")
    def predefined_role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @predefined_role.setter
    def predefined_role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MembershipRbacRoleBindingStateArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MembershipRbacRoleBindingStateArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NamespaceStateArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NamespaceStateArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RolloutSequenceStageArgsDict(TypedDict):
    fleet_projects: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    cluster_selector: NotRequired[pulumi.Input[RolloutSequenceStageClusterSelectorArgsDict]]
    soak_duration: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RolloutSequenceStageArgs:
    def __init__(__self__, *, fleet_projects: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], cluster_selector: Optional[pulumi.Input[RolloutSequenceStageClusterSelectorArgs]] = ..., soak_duration: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetProjects")
    def fleet_projects(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @fleet_projects.setter
    def fleet_projects(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSelector")
    def cluster_selector(self) -> Optional[pulumi.Input[RolloutSequenceStageClusterSelectorArgs]]:
        
        ...
    
    @cluster_selector.setter
    def cluster_selector(self, value: Optional[pulumi.Input[RolloutSequenceStageClusterSelectorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="soakDuration")
    def soak_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @soak_duration.setter
    def soak_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RolloutSequenceStageClusterSelectorArgsDict(TypedDict):
    label_selector: pulumi.Input[_builtins.str]


@pulumi.input_type
class RolloutSequenceStageClusterSelectorArgs:
    def __init__(__self__, *, label_selector: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelSelector")
    def label_selector(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @label_selector.setter
    def label_selector(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ScopeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScopeIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScopeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScopeIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScopeRbacRoleBindingRoleArgsDict(TypedDict):
    custom_role: NotRequired[pulumi.Input[_builtins.str]]
    predefined_role: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScopeRbacRoleBindingRoleArgs:
    def __init__(__self__, *, custom_role: Optional[pulumi.Input[_builtins.str]] = ..., predefined_role: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRole")
    def custom_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_role.setter
    def custom_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedRole")
    def predefined_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @predefined_role.setter
    def predefined_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScopeRbacRoleBindingStateArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScopeRbacRoleBindingStateArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScopeStateArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScopeStateArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


