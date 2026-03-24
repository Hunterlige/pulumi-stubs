import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FeatureFleetDefaultMemberConfig",
    "FeatureFleetDefaultMemberConfigConfigmanagement",
    ...,
    ...,
    ...,
    "FeatureFleetDefaultMemberConfigMesh",
    "FeatureFleetDefaultMemberConfigPolicycontroller",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FeatureIamBindingCondition",
    "FeatureIamMemberCondition",
    "FeatureMembershipConfigmanagement",
    "FeatureMembershipConfigmanagementConfigSync",
    ...,
    ...,
    "FeatureMembershipConfigmanagementConfigSyncGit",
    "FeatureMembershipConfigmanagementConfigSyncOci",
    ...,
    "FeatureMembershipConfigmanagementPolicyController",
    ...,
    "FeatureMembershipMesh",
    "FeatureMembershipPolicycontroller",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FeatureResourceState",
    "FeatureSpec",
    "FeatureSpecClusterupgrade",
    "FeatureSpecClusterupgradeGkeUpgradeOverride",
    ...,
    "FeatureSpecClusterupgradeGkeUpgradeOverrideUpgrade",
    "FeatureSpecClusterupgradePostConditions",
    "FeatureSpecFleetobservability",
    "FeatureSpecFleetobservabilityLoggingConfig",
    ...,
    ...,
    "FeatureSpecMulticlusteringress",
    "FeatureSpecRbacrolebindingactuation",
    "FeatureSpecWorkloadidentity",
    "FeatureState",
    "FeatureStateState",
    "FleetDefaultClusterConfig",
    "FleetDefaultClusterConfigBinaryAuthorizationConfig",
    ...,
    "FleetDefaultClusterConfigSecurityPostureConfig",
    "FleetState",
    "MembershipAuthority",
    "MembershipBindingState",
    "MembershipEndpoint",
    "MembershipEndpointGkeCluster",
    "MembershipIamBindingCondition",
    "MembershipIamMemberCondition",
    "MembershipRbacRoleBindingRole",
    "MembershipRbacRoleBindingState",
    "NamespaceState",
    "RolloutSequenceStage",
    "RolloutSequenceStageClusterSelector",
    "ScopeIamBindingCondition",
    "ScopeIamMemberCondition",
    "ScopeRbacRoleBindingRole",
    "ScopeRbacRoleBindingState",
    "ScopeState",
    "GetFeatureFleetDefaultMemberConfigResult",
    ...,
    ...,
    ...,
    ...,
    "GetFeatureFleetDefaultMemberConfigMeshResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetFeatureResourceStateResult",
    "GetFeatureSpecResult",
    "GetFeatureSpecClusterupgradeResult",
    ...,
    ...,
    ...,
    "GetFeatureSpecClusterupgradePostConditionResult",
    "GetFeatureSpecFleetobservabilityResult",
    ...,
    ...,
    ...,
    "GetFeatureSpecMulticlusteringressResult",
    "GetFeatureSpecRbacrolebindingactuationResult",
    "GetFeatureSpecWorkloadidentityResult",
    "GetFeatureStateResult",
    "GetFeatureStateStateResult",
    "GetMembershipAuthorityResult",
    "GetMembershipBindingStateResult",
    "GetMembershipEndpointResult",
    "GetMembershipEndpointGkeClusterResult",
]

@pulumi.output_type
class FeatureFleetDefaultMemberConfig(dict):
    def __init__(
        __self__,
        *,
        configmanagement: Optional[
            outputs.FeatureFleetDefaultMemberConfigConfigmanagement
        ] = ...,
        mesh: Optional[outputs.FeatureFleetDefaultMemberConfigMesh] = ...,
        policycontroller: Optional[
            outputs.FeatureFleetDefaultMemberConfigPolicycontroller
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configmanagement(
        self,
    ) -> Optional[outputs.FeatureFleetDefaultMemberConfigConfigmanagement]: ...
    @_builtins.property
    @pulumi.getter
    def mesh(self) -> Optional[outputs.FeatureFleetDefaultMemberConfigMesh]: ...
    @_builtins.property
    @pulumi.getter
    def policycontroller(
        self,
    ) -> Optional[outputs.FeatureFleetDefaultMemberConfigPolicycontroller]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigConfigmanagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        config_sync: Optional[
            outputs.FeatureFleetDefaultMemberConfigConfigmanagementConfigSync
        ] = ...,
        management: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configSync")
    def config_sync(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigConfigmanagementConfigSync
    ]: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigConfigmanagementConfigSync(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        git: Optional[
            outputs.FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGit
        ] = ...,
        metrics_gcp_service_account_email: Optional[_builtins.str] = ...,
        oci: Optional[
            outputs.FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOci
        ] = ...,
        prevent_drift: Optional[_builtins.bool] = ...,
        source_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def git(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGit
    ]: ...
    @_builtins.property
    @pulumi.getter(name="metricsGcpServiceAccountEmail")
    def metrics_gcp_service_account_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def oci(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOci
    ]: ...
    @_builtins.property
    @pulumi.getter(name="preventDrift")
    def prevent_drift(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGit(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_type: _builtins.str,
        gcp_service_account_email: Optional[_builtins.str] = ...,
        https_proxy: Optional[_builtins.str] = ...,
        policy_dir: Optional[_builtins.str] = ...,
        sync_branch: Optional[_builtins.str] = ...,
        sync_repo: Optional[_builtins.str] = ...,
        sync_rev: Optional[_builtins.str] = ...,
        sync_wait_secs: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncBranch")
    def sync_branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncRev")
    def sync_rev(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOci(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_type: _builtins.str,
        gcp_service_account_email: Optional[_builtins.str] = ...,
        policy_dir: Optional[_builtins.str] = ...,
        sync_repo: Optional[_builtins.str] = ...,
        sync_wait_secs: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigMesh(dict):
    def __init__(__self__, *, management: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> _builtins.str: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontroller(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        policy_controller_hub_config: outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfig,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyControllerHubConfig")
    def policy_controller_hub_config(
        self,
    ) -> (
        outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfig
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        install_spec: _builtins.str,
        audit_interval_seconds: Optional[_builtins.int] = ...,
        constraint_violation_limit: Optional[_builtins.int] = ...,
        deployment_configs: Optional[
            Sequence[
                outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfig
            ]
        ] = ...,
        exemptable_namespaces: Optional[Sequence[_builtins.str]] = ...,
        log_denies_enabled: Optional[_builtins.bool] = ...,
        monitoring: Optional[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoring
        ] = ...,
        mutation_enabled: Optional[_builtins.bool] = ...,
        policy_content: Optional[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContent
        ] = ...,
        referential_rules_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="installSpec")
    def install_spec(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="auditIntervalSeconds")
    def audit_interval_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="constraintViolationLimit")
    def constraint_violation_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentConfigs")
    def deployment_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfig
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="exemptableNamespaces")
    def exemptable_namespaces(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logDeniesEnabled")
    def log_denies_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def monitoring(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoring
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mutationEnabled")
    def mutation_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="policyContent")
    def policy_content(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContent
    ]: ...
    @_builtins.property
    @pulumi.getter(name="referentialRulesEnabled")
    def referential_rules_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component: _builtins.str,
        container_resources: Optional[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResources
        ] = ...,
        pod_affinity: Optional[_builtins.str] = ...,
        pod_tolerations: Optional[
            Sequence[
                outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodToleration
            ]
        ] = ...,
        replica_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def component(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerResources")
    def container_resources(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResources
    ]: ...
    @_builtins.property
    @pulumi.getter(name="podAffinity")
    def pod_affinity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="podTolerations")
    def pod_tolerations(
        self,
    ) -> Optional[
        Sequence[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodToleration
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResources(
    dict
):
    def __init__(
        __self__,
        *,
        limits: Optional[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimits
        ] = ...,
        requests: Optional[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequests
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimits
    ]: ...
    @_builtins.property
    @pulumi.getter
    def requests(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequests
    ]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimits(
    dict
):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequests(
    dict
):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodToleration(
    dict
):
    def __init__(
        __self__,
        *,
        effect: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        operator: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoring(
    dict
):
    def __init__(
        __self__, *, backends: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContent(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bundles: Optional[
            Sequence[
                outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundle
            ]
        ] = ...,
        template_library: Optional[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibrary
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bundles(
        self,
    ) -> Optional[
        Sequence[
            outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundle
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="templateLibrary")
    def template_library(
        self,
    ) -> Optional[
        outputs.FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibrary
    ]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundle(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bundle: _builtins.str,
        exempted_namespaces: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bundle(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exemptedNamespaces")
    def exempted_namespaces(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibrary(
    dict
):
    def __init__(__self__, *, installation: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def installation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        config_sync: Optional[
            outputs.FeatureMembershipConfigmanagementConfigSync
        ] = ...,
        hierarchy_controller: Optional[
            outputs.FeatureMembershipConfigmanagementHierarchyController
        ] = ...,
        management: Optional[_builtins.str] = ...,
        policy_controller: Optional[
            outputs.FeatureMembershipConfigmanagementPolicyController
        ] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configSync")
    def config_sync(
        self,
    ) -> Optional[outputs.FeatureMembershipConfigmanagementConfigSync]: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyController")
    def hierarchy_controller(
        self,
    ) -> Optional[outputs.FeatureMembershipConfigmanagementHierarchyController]: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyController")
    def policy_controller(
        self,
    ) -> Optional[outputs.FeatureMembershipConfigmanagementPolicyController]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagementConfigSync(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deployment_overrides: Optional[
            Sequence[
                outputs.FeatureMembershipConfigmanagementConfigSyncDeploymentOverride
            ]
        ] = ...,
        enabled: Optional[_builtins.bool] = ...,
        git: Optional[outputs.FeatureMembershipConfigmanagementConfigSyncGit] = ...,
        metrics_gcp_service_account_email: Optional[_builtins.str] = ...,
        oci: Optional[outputs.FeatureMembershipConfigmanagementConfigSyncOci] = ...,
        prevent_drift: Optional[_builtins.bool] = ...,
        source_format: Optional[_builtins.str] = ...,
        stop_syncing: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentOverrides")
    def deployment_overrides(
        self,
    ) -> Optional[
        Sequence[outputs.FeatureMembershipConfigmanagementConfigSyncDeploymentOverride]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def git(
        self,
    ) -> Optional[outputs.FeatureMembershipConfigmanagementConfigSyncGit]: ...
    @_builtins.property
    @pulumi.getter(name="metricsGcpServiceAccountEmail")
    def metrics_gcp_service_account_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def oci(
        self,
    ) -> Optional[outputs.FeatureMembershipConfigmanagementConfigSyncOci]: ...
    @_builtins.property
    @pulumi.getter(name="preventDrift")
    def prevent_drift(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stopSyncing")
    def stop_syncing(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagementConfigSyncDeploymentOverride(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        containers: Optional[
            Sequence[
                outputs.FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainer
            ]
        ] = ...,
        deployment_name: Optional[_builtins.str] = ...,
        deployment_namespace: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[
        Sequence[
            outputs.FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainer
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentNamespace")
    def deployment_namespace(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagementConfigSyncDeploymentOverrideContainer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_name: Optional[_builtins.str] = ...,
        cpu_limit: Optional[_builtins.str] = ...,
        cpu_request: Optional[_builtins.str] = ...,
        memory_limit: Optional[_builtins.str] = ...,
        memory_request: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuLimit")
    def cpu_limit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuRequest")
    def cpu_request(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryLimit")
    def memory_limit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryRequest")
    def memory_request(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagementConfigSyncGit(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gcp_service_account_email: Optional[_builtins.str] = ...,
        https_proxy: Optional[_builtins.str] = ...,
        policy_dir: Optional[_builtins.str] = ...,
        secret_type: Optional[_builtins.str] = ...,
        sync_branch: Optional[_builtins.str] = ...,
        sync_repo: Optional[_builtins.str] = ...,
        sync_rev: Optional[_builtins.str] = ...,
        sync_wait_secs: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncBranch")
    def sync_branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncRev")
    def sync_rev(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagementConfigSyncOci(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gcp_service_account_email: Optional[_builtins.str] = ...,
        policy_dir: Optional[_builtins.str] = ...,
        secret_type: Optional[_builtins.str] = ...,
        sync_repo: Optional[_builtins.str] = ...,
        sync_wait_secs: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagementHierarchyController(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_hierarchical_resource_quota: Optional[_builtins.bool] = ...,
        enable_pod_tree_labels: Optional[_builtins.bool] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableHierarchicalResourceQuota")
    def enable_hierarchical_resource_quota(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePodTreeLabels")
    def enable_pod_tree_labels(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagementPolicyController(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audit_interval_seconds: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        exemptable_namespaces: Optional[Sequence[_builtins.str]] = ...,
        log_denies_enabled: Optional[_builtins.bool] = ...,
        monitoring: Optional[
            outputs.FeatureMembershipConfigmanagementPolicyControllerMonitoring
        ] = ...,
        mutation_enabled: Optional[_builtins.bool] = ...,
        referential_rules_enabled: Optional[_builtins.bool] = ...,
        template_library_installed: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditIntervalSeconds")
    def audit_interval_seconds(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exemptableNamespaces")
    def exemptable_namespaces(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logDeniesEnabled")
    def log_denies_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def monitoring(
        self,
    ) -> Optional[
        outputs.FeatureMembershipConfigmanagementPolicyControllerMonitoring
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mutationEnabled")
    def mutation_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="referentialRulesEnabled")
    def referential_rules_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="templateLibraryInstalled")
    def template_library_installed(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FeatureMembershipConfigmanagementPolicyControllerMonitoring(dict):
    def __init__(
        __self__, *, backends: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FeatureMembershipMesh(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        control_plane: Optional[_builtins.str] = ...,
        management: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    @_utilities.deprecated("""Deprecated in favor of the `management` field""")
    def control_plane(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipPolicycontroller(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        policy_controller_hub_config: outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfig,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyControllerHubConfig")
    def policy_controller_hub_config(
        self,
    ) -> outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfig: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audit_interval_seconds: Optional[_builtins.int] = ...,
        constraint_violation_limit: Optional[_builtins.int] = ...,
        deployment_configs: Optional[
            Sequence[
                outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfig
            ]
        ] = ...,
        exemptable_namespaces: Optional[Sequence[_builtins.str]] = ...,
        install_spec: Optional[_builtins.str] = ...,
        log_denies_enabled: Optional[_builtins.bool] = ...,
        monitoring: Optional[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoring
        ] = ...,
        mutation_enabled: Optional[_builtins.bool] = ...,
        policy_content: Optional[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContent
        ] = ...,
        referential_rules_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditIntervalSeconds")
    def audit_interval_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="constraintViolationLimit")
    def constraint_violation_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentConfigs")
    def deployment_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfig
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="exemptableNamespaces")
    def exemptable_namespaces(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="installSpec")
    def install_spec(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logDeniesEnabled")
    def log_denies_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def monitoring(
        self,
    ) -> Optional[
        outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoring
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mutationEnabled")
    def mutation_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="policyContent")
    def policy_content(
        self,
    ) -> Optional[
        outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContent
    ]: ...
    @_builtins.property
    @pulumi.getter(name="referentialRulesEnabled")
    def referential_rules_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_name: _builtins.str,
        container_resources: Optional[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResources
        ] = ...,
        pod_affinity: Optional[_builtins.str] = ...,
        pod_tolerations: Optional[
            Sequence[
                outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodToleration
            ]
        ] = ...,
        replica_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerResources")
    def container_resources(
        self,
    ) -> Optional[
        outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResources
    ]: ...
    @_builtins.property
    @pulumi.getter(name="podAffinity")
    def pod_affinity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="podTolerations")
    def pod_tolerations(
        self,
    ) -> Optional[
        Sequence[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodToleration
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResources(
    dict
):
    def __init__(
        __self__,
        *,
        limits: Optional[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimits
        ] = ...,
        requests: Optional[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequests
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[
        outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimits
    ]: ...
    @_builtins.property
    @pulumi.getter
    def requests(
        self,
    ) -> Optional[
        outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequests
    ]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesLimits(
    dict
):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourcesRequests(
    dict
):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodToleration(
    dict
):
    def __init__(
        __self__,
        *,
        effect: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        operator: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigMonitoring(dict):
    def __init__(
        __self__, *, backends: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bundles: Optional[
            Sequence[
                outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundle
            ]
        ] = ...,
        template_library: Optional[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibrary
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bundles(
        self,
    ) -> Optional[
        Sequence[
            outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundle
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="templateLibrary")
    def template_library(
        self,
    ) -> Optional[
        outputs.FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibrary
    ]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentBundle(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bundle_name: _builtins.str,
        exempted_namespaces: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bundleName")
    def bundle_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exemptedNamespaces")
    def exempted_namespaces(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FeatureMembershipPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibrary(
    dict
):
    def __init__(__self__, *, installation: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def installation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureResourceState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        has_resources: Optional[_builtins.bool] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hasResources")
    def has_resources(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureSpec(dict):
    def __init__(
        __self__,
        *,
        clusterupgrade: Optional[outputs.FeatureSpecClusterupgrade] = ...,
        fleetobservability: Optional[outputs.FeatureSpecFleetobservability] = ...,
        multiclusteringress: Optional[outputs.FeatureSpecMulticlusteringress] = ...,
        rbacrolebindingactuation: Optional[
            outputs.FeatureSpecRbacrolebindingactuation
        ] = ...,
        workloadidentity: Optional[outputs.FeatureSpecWorkloadidentity] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def clusterupgrade(self) -> Optional[outputs.FeatureSpecClusterupgrade]: ...
    @_builtins.property
    @pulumi.getter
    def fleetobservability(self) -> Optional[outputs.FeatureSpecFleetobservability]: ...
    @_builtins.property
    @pulumi.getter
    def multiclusteringress(
        self,
    ) -> Optional[outputs.FeatureSpecMulticlusteringress]: ...
    @_builtins.property
    @pulumi.getter
    def rbacrolebindingactuation(
        self,
    ) -> Optional[outputs.FeatureSpecRbacrolebindingactuation]: ...
    @_builtins.property
    @pulumi.getter
    def workloadidentity(self) -> Optional[outputs.FeatureSpecWorkloadidentity]: ...

@pulumi.output_type
class FeatureSpecClusterupgrade(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        upstream_fleets: Sequence[_builtins.str],
        gke_upgrade_overrides: Optional[
            Sequence[outputs.FeatureSpecClusterupgradeGkeUpgradeOverride]
        ] = ...,
        post_conditions: Optional[
            outputs.FeatureSpecClusterupgradePostConditions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="upstreamFleets")
    def upstream_fleets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gkeUpgradeOverrides")
    def gke_upgrade_overrides(
        self,
    ) -> Optional[Sequence[outputs.FeatureSpecClusterupgradeGkeUpgradeOverride]]: ...
    @_builtins.property
    @pulumi.getter(name="postConditions")
    def post_conditions(
        self,
    ) -> Optional[outputs.FeatureSpecClusterupgradePostConditions]: ...

@pulumi.output_type
class FeatureSpecClusterupgradeGkeUpgradeOverride(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        post_conditions: outputs.FeatureSpecClusterupgradeGkeUpgradeOverridePostConditions,
        upgrade: outputs.FeatureSpecClusterupgradeGkeUpgradeOverrideUpgrade,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postConditions")
    def post_conditions(
        self,
    ) -> outputs.FeatureSpecClusterupgradeGkeUpgradeOverridePostConditions: ...
    @_builtins.property
    @pulumi.getter
    def upgrade(self) -> outputs.FeatureSpecClusterupgradeGkeUpgradeOverrideUpgrade: ...

@pulumi.output_type
class FeatureSpecClusterupgradeGkeUpgradeOverridePostConditions(dict):
    def __init__(__self__, *, soaking: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def soaking(self) -> _builtins.str: ...

@pulumi.output_type
class FeatureSpecClusterupgradeGkeUpgradeOverrideUpgrade(dict):
    def __init__(__self__, *, name: _builtins.str, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class FeatureSpecClusterupgradePostConditions(dict):
    def __init__(__self__, *, soaking: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def soaking(self) -> _builtins.str: ...

@pulumi.output_type
class FeatureSpecFleetobservability(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        logging_config: Optional[
            outputs.FeatureSpecFleetobservabilityLoggingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[outputs.FeatureSpecFleetobservabilityLoggingConfig]: ...

@pulumi.output_type
class FeatureSpecFleetobservabilityLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_config: Optional[
            outputs.FeatureSpecFleetobservabilityLoggingConfigDefaultConfig
        ] = ...,
        fleet_scope_logs_config: Optional[
            outputs.FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultConfig")
    def default_config(
        self,
    ) -> Optional[outputs.FeatureSpecFleetobservabilityLoggingConfigDefaultConfig]: ...
    @_builtins.property
    @pulumi.getter(name="fleetScopeLogsConfig")
    def fleet_scope_logs_config(
        self,
    ) -> Optional[
        outputs.FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfig
    ]: ...

@pulumi.output_type
class FeatureSpecFleetobservabilityLoggingConfigDefaultConfig(dict):
    def __init__(__self__, *, mode: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfig(dict):
    def __init__(__self__, *, mode: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureSpecMulticlusteringress(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, config_membership: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configMembership")
    def config_membership(self) -> _builtins.str: ...

@pulumi.output_type
class FeatureSpecRbacrolebindingactuation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_custom_roles: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedCustomRoles")
    def allowed_custom_roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FeatureSpecWorkloadidentity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, scope_tenancy_pool: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scopeTenancyPool")
    def scope_tenancy_pool(self) -> _builtins.str: ...

@pulumi.output_type
class FeatureState(dict):
    def __init__(
        __self__, *, states: Optional[Sequence[outputs.FeatureStateState]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def states(self) -> Optional[Sequence[outputs.FeatureStateState]]: ...

@pulumi.output_type
class FeatureStateState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FleetDefaultClusterConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        binary_authorization_config: Optional[
            outputs.FleetDefaultClusterConfigBinaryAuthorizationConfig
        ] = ...,
        security_posture_config: Optional[
            outputs.FleetDefaultClusterConfigSecurityPostureConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizationConfig")
    def binary_authorization_config(
        self,
    ) -> Optional[outputs.FleetDefaultClusterConfigBinaryAuthorizationConfig]: ...
    @_builtins.property
    @pulumi.getter(name="securityPostureConfig")
    def security_posture_config(
        self,
    ) -> Optional[outputs.FleetDefaultClusterConfigSecurityPostureConfig]: ...

@pulumi.output_type
class FleetDefaultClusterConfigBinaryAuthorizationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        evaluation_mode: Optional[_builtins.str] = ...,
        policy_bindings: Optional[
            Sequence[
                outputs.FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBinding
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyBindings")
    def policy_bindings(
        self,
    ) -> Optional[
        Sequence[
            outputs.FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBinding
        ]
    ]: ...

@pulumi.output_type
class FleetDefaultClusterConfigBinaryAuthorizationConfigPolicyBinding(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FleetDefaultClusterConfigSecurityPostureConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mode: Optional[_builtins.str] = ...,
        vulnerability_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityMode")
    def vulnerability_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FleetState(dict):
    def __init__(__self__, *, code: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MembershipAuthority(dict):
    def __init__(__self__, *, issuer: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...

@pulumi.output_type
class MembershipBindingState(dict):
    def __init__(__self__, *, code: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MembershipEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gke_cluster: Optional[outputs.MembershipEndpointGkeCluster] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gkeCluster")
    def gke_cluster(self) -> Optional[outputs.MembershipEndpointGkeCluster]: ...

@pulumi.output_type
class MembershipEndpointGkeCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_link: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceLink")
    def resource_link(self) -> _builtins.str: ...

@pulumi.output_type
class MembershipIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MembershipIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MembershipRbacRoleBindingRole(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, predefined_role: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedRole")
    def predefined_role(self) -> _builtins.str: ...

@pulumi.output_type
class MembershipRbacRoleBindingState(dict):
    def __init__(__self__, *, code: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceState(dict):
    def __init__(__self__, *, code: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RolloutSequenceStage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fleet_projects: Sequence[_builtins.str],
        cluster_selector: Optional[outputs.RolloutSequenceStageClusterSelector] = ...,
        soak_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fleetProjects")
    def fleet_projects(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterSelector")
    def cluster_selector(
        self,
    ) -> Optional[outputs.RolloutSequenceStageClusterSelector]: ...
    @_builtins.property
    @pulumi.getter(name="soakDuration")
    def soak_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RolloutSequenceStageClusterSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, label_selector: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labelSelector")
    def label_selector(self) -> _builtins.str: ...

@pulumi.output_type
class ScopeIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScopeIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScopeRbacRoleBindingRole(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_role: Optional[_builtins.str] = ...,
        predefined_role: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRole")
    def custom_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="predefinedRole")
    def predefined_role(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScopeRbacRoleBindingState(dict):
    def __init__(__self__, *, code: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScopeState(dict):
    def __init__(__self__, *, code: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigResult(dict):
    def __init__(
        __self__,
        *,
        configmanagements: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigConfigmanagementResult
        ],
        meshes: Sequence[outputs.GetFeatureFleetDefaultMemberConfigMeshResult],
        policycontrollers: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configmanagements(
        self,
    ) -> Sequence[outputs.GetFeatureFleetDefaultMemberConfigConfigmanagementResult]: ...
    @_builtins.property
    @pulumi.getter
    def meshes(
        self,
    ) -> Sequence[outputs.GetFeatureFleetDefaultMemberConfigMeshResult]: ...
    @_builtins.property
    @pulumi.getter
    def policycontrollers(
        self,
    ) -> Sequence[outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerResult]: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigConfigmanagementResult(dict):
    def __init__(
        __self__,
        *,
        config_syncs: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncResult
        ],
        management: _builtins.str,
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configSyncs")
    def config_syncs(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        gits: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitResult
        ],
        metrics_gcp_service_account_email: _builtins.str,
        ocis: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciResult
        ],
        prevent_drift: _builtins.bool,
        source_format: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def gits(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="metricsGcpServiceAccountEmail")
    def metrics_gcp_service_account_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocis(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="preventDrift")
    def prevent_drift(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncGitResult(dict):
    def __init__(
        __self__,
        *,
        gcp_service_account_email: _builtins.str,
        https_proxy: _builtins.str,
        policy_dir: _builtins.str,
        secret_type: _builtins.str,
        sync_branch: _builtins.str,
        sync_repo: _builtins.str,
        sync_rev: _builtins.str,
        sync_wait_secs: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncBranch")
    def sync_branch(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncRev")
    def sync_rev(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigConfigmanagementConfigSyncOciResult(dict):
    def __init__(
        __self__,
        *,
        gcp_service_account_email: _builtins.str,
        policy_dir: _builtins.str,
        secret_type: _builtins.str,
        sync_repo: _builtins.str,
        sync_wait_secs: _builtins.str,
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccountEmail")
    def gcp_service_account_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyDir")
    def policy_dir(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretType")
    def secret_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncRepo")
    def sync_repo(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncWaitSecs")
    def sync_wait_secs(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigMeshResult(dict):
    def __init__(__self__, *, management: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerResult(dict):
    def __init__(
        __self__,
        *,
        policy_controller_hub_configs: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigResult
        ],
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyControllerHubConfigs")
    def policy_controller_hub_configs(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        audit_interval_seconds: _builtins.int,
        constraint_violation_limit: _builtins.int,
        deployment_configs: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigResult
        ],
        exemptable_namespaces: Sequence[_builtins.str],
        install_spec: _builtins.str,
        log_denies_enabled: _builtins.bool,
        monitorings: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringResult
        ],
        mutation_enabled: _builtins.bool,
        policy_contents: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentResult
        ],
        referential_rules_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditIntervalSeconds")
    def audit_interval_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="constraintViolationLimit")
    def constraint_violation_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="deploymentConfigs")
    def deployment_configs(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="exemptableNamespaces")
    def exemptable_namespaces(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="installSpec")
    def install_spec(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logDeniesEnabled")
    def log_denies_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def monitorings(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mutationEnabled")
    def mutation_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="policyContents")
    def policy_contents(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="referentialRulesEnabled")
    def referential_rules_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        component: _builtins.str,
        container_resources: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceResult
        ],
        pod_affinity: _builtins.str,
        pod_tolerations: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationResult
        ],
        replica_count: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def component(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerResources")
    def container_resources(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="podAffinity")
    def pod_affinity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="podTolerations")
    def pod_tolerations(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceResult(
    dict
):
    def __init__(
        __self__,
        *,
        limits: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceLimitResult
        ],
        requests: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceRequestResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceLimitResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def requests(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceRequestResult
    ]: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceLimitResult(
    dict
):
    def __init__(__self__, *, cpu: _builtins.str, memory: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigContainerResourceRequestResult(
    dict
):
    def __init__(__self__, *, cpu: _builtins.str, memory: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigDeploymentConfigPodTolerationResult(
    dict
):
    def __init__(
        __self__,
        *,
        effect: _builtins.str,
        key: _builtins.str,
        operator: _builtins.str,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigMonitoringResult(
    dict
):
    def __init__(__self__, *, backends: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentResult(
    dict
):
    def __init__(
        __self__,
        *,
        bundles: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleResult
        ],
        template_libraries: Sequence[
            outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bundles(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="templateLibraries")
    def template_libraries(
        self,
    ) -> Sequence[
        outputs.GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryResult
    ]: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentBundleResult(
    dict
):
    def __init__(
        __self__, *, bundle: _builtins.str, exempted_namespaces: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bundle(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exemptedNamespaces")
    def exempted_namespaces(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetFeatureFleetDefaultMemberConfigPolicycontrollerPolicyControllerHubConfigPolicyContentTemplateLibraryResult(
    dict
):
    def __init__(__self__, *, installation: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def installation(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureResourceStateResult(dict):
    def __init__(
        __self__, *, has_resources: _builtins.bool, state: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hasResources")
    def has_resources(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureSpecResult(dict):
    def __init__(
        __self__,
        *,
        clusterupgrades: Sequence[outputs.GetFeatureSpecClusterupgradeResult],
        fleetobservabilities: Sequence[outputs.GetFeatureSpecFleetobservabilityResult],
        multiclusteringresses: Sequence[
            outputs.GetFeatureSpecMulticlusteringressResult
        ],
        rbacrolebindingactuations: Sequence[
            outputs.GetFeatureSpecRbacrolebindingactuationResult
        ],
        workloadidentities: Sequence[outputs.GetFeatureSpecWorkloadidentityResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def clusterupgrades(
        self,
    ) -> Sequence[outputs.GetFeatureSpecClusterupgradeResult]: ...
    @_builtins.property
    @pulumi.getter
    def fleetobservabilities(
        self,
    ) -> Sequence[outputs.GetFeatureSpecFleetobservabilityResult]: ...
    @_builtins.property
    @pulumi.getter
    def multiclusteringresses(
        self,
    ) -> Sequence[outputs.GetFeatureSpecMulticlusteringressResult]: ...
    @_builtins.property
    @pulumi.getter
    def rbacrolebindingactuations(
        self,
    ) -> Sequence[outputs.GetFeatureSpecRbacrolebindingactuationResult]: ...
    @_builtins.property
    @pulumi.getter
    def workloadidentities(
        self,
    ) -> Sequence[outputs.GetFeatureSpecWorkloadidentityResult]: ...

@pulumi.output_type
class GetFeatureSpecClusterupgradeResult(dict):
    def __init__(
        __self__,
        *,
        gke_upgrade_overrides: Sequence[
            outputs.GetFeatureSpecClusterupgradeGkeUpgradeOverrideResult
        ],
        post_conditions: Sequence[
            outputs.GetFeatureSpecClusterupgradePostConditionResult
        ],
        upstream_fleets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gkeUpgradeOverrides")
    def gke_upgrade_overrides(
        self,
    ) -> Sequence[outputs.GetFeatureSpecClusterupgradeGkeUpgradeOverrideResult]: ...
    @_builtins.property
    @pulumi.getter(name="postConditions")
    def post_conditions(
        self,
    ) -> Sequence[outputs.GetFeatureSpecClusterupgradePostConditionResult]: ...
    @_builtins.property
    @pulumi.getter(name="upstreamFleets")
    def upstream_fleets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetFeatureSpecClusterupgradeGkeUpgradeOverrideResult(dict):
    def __init__(
        __self__,
        *,
        post_conditions: Sequence[
            outputs.GetFeatureSpecClusterupgradeGkeUpgradeOverridePostConditionResult
        ],
        upgrades: Sequence[
            outputs.GetFeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postConditions")
    def post_conditions(
        self,
    ) -> Sequence[
        outputs.GetFeatureSpecClusterupgradeGkeUpgradeOverridePostConditionResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def upgrades(
        self,
    ) -> Sequence[
        outputs.GetFeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeResult
    ]: ...

@pulumi.output_type
class GetFeatureSpecClusterupgradeGkeUpgradeOverridePostConditionResult(dict):
    def __init__(__self__, *, soaking: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def soaking(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureSpecClusterupgradeGkeUpgradeOverrideUpgradeResult(dict):
    def __init__(__self__, *, name: _builtins.str, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureSpecClusterupgradePostConditionResult(dict):
    def __init__(__self__, *, soaking: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def soaking(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureSpecFleetobservabilityResult(dict):
    def __init__(
        __self__,
        *,
        logging_configs: Sequence[
            outputs.GetFeatureSpecFleetobservabilityLoggingConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfigs")
    def logging_configs(
        self,
    ) -> Sequence[outputs.GetFeatureSpecFleetobservabilityLoggingConfigResult]: ...

@pulumi.output_type
class GetFeatureSpecFleetobservabilityLoggingConfigResult(dict):
    def __init__(
        __self__,
        *,
        default_configs: Sequence[
            outputs.GetFeatureSpecFleetobservabilityLoggingConfigDefaultConfigResult
        ],
        fleet_scope_logs_configs: Sequence[
            outputs.GetFeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultConfigs")
    def default_configs(
        self,
    ) -> Sequence[
        outputs.GetFeatureSpecFleetobservabilityLoggingConfigDefaultConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fleetScopeLogsConfigs")
    def fleet_scope_logs_configs(
        self,
    ) -> Sequence[
        outputs.GetFeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigResult
    ]: ...

@pulumi.output_type
class GetFeatureSpecFleetobservabilityLoggingConfigDefaultConfigResult(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureSpecFleetobservabilityLoggingConfigFleetScopeLogsConfigResult(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureSpecMulticlusteringressResult(dict):
    def __init__(__self__, *, config_membership: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configMembership")
    def config_membership(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureSpecRbacrolebindingactuationResult(dict):
    def __init__(
        __self__, *, allowed_custom_roles: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedCustomRoles")
    def allowed_custom_roles(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetFeatureSpecWorkloadidentityResult(dict):
    def __init__(__self__, *, scope_tenancy_pool: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scopeTenancyPool")
    def scope_tenancy_pool(self) -> _builtins.str: ...

@pulumi.output_type
class GetFeatureStateResult(dict):
    def __init__(
        __self__, *, states: Sequence[outputs.GetFeatureStateStateResult]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def states(self) -> Sequence[outputs.GetFeatureStateStateResult]: ...

@pulumi.output_type
class GetFeatureStateStateResult(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        description: _builtins.str,
        update_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetMembershipAuthorityResult(dict):
    def __init__(__self__, *, issuer: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...

@pulumi.output_type
class GetMembershipBindingStateResult(dict):
    def __init__(__self__, *, code: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...

@pulumi.output_type
class GetMembershipEndpointResult(dict):
    def __init__(
        __self__,
        *,
        gke_clusters: Sequence[outputs.GetMembershipEndpointGkeClusterResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(
        self,
    ) -> Sequence[outputs.GetMembershipEndpointGkeClusterResult]: ...

@pulumi.output_type
class GetMembershipEndpointGkeClusterResult(dict):
    def __init__(__self__, *, resource_link: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceLink")
    def resource_link(self) -> _builtins.str: ...
