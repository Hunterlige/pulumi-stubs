import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GuestPoliciesAssignmentArgs",
    "GuestPoliciesAssignmentArgsDict",
    "GuestPoliciesAssignmentGroupLabelArgs",
    "GuestPoliciesAssignmentGroupLabelArgsDict",
    "GuestPoliciesAssignmentOsTypeArgs",
    "GuestPoliciesAssignmentOsTypeArgsDict",
    "GuestPoliciesPackageArgs",
    "GuestPoliciesPackageArgsDict",
    "GuestPoliciesPackageRepositoryArgs",
    "GuestPoliciesPackageRepositoryArgsDict",
    "GuestPoliciesPackageRepositoryAptArgs",
    "GuestPoliciesPackageRepositoryAptArgsDict",
    "GuestPoliciesPackageRepositoryGooArgs",
    "GuestPoliciesPackageRepositoryGooArgsDict",
    "GuestPoliciesPackageRepositoryYumArgs",
    "GuestPoliciesPackageRepositoryYumArgsDict",
    "GuestPoliciesPackageRepositoryZypperArgs",
    "GuestPoliciesPackageRepositoryZypperArgsDict",
    "GuestPoliciesRecipeArgs",
    "GuestPoliciesRecipeArgsDict",
    "GuestPoliciesRecipeArtifactArgs",
    "GuestPoliciesRecipeArtifactArgsDict",
    "GuestPoliciesRecipeArtifactGcsArgs",
    "GuestPoliciesRecipeArtifactGcsArgsDict",
    "GuestPoliciesRecipeArtifactRemoteArgs",
    "GuestPoliciesRecipeArtifactRemoteArgsDict",
    "GuestPoliciesRecipeInstallStepArgs",
    "GuestPoliciesRecipeInstallStepArgsDict",
    ...,
    ...,
    "GuestPoliciesRecipeInstallStepDpkgInstallationArgs",
    ...,
    "GuestPoliciesRecipeInstallStepFileCopyArgs",
    "GuestPoliciesRecipeInstallStepFileCopyArgsDict",
    "GuestPoliciesRecipeInstallStepFileExecArgs",
    "GuestPoliciesRecipeInstallStepFileExecArgsDict",
    "GuestPoliciesRecipeInstallStepMsiInstallationArgs",
    ...,
    "GuestPoliciesRecipeInstallStepRpmInstallationArgs",
    ...,
    "GuestPoliciesRecipeInstallStepScriptRunArgs",
    "GuestPoliciesRecipeInstallStepScriptRunArgsDict",
    "GuestPoliciesRecipeUpdateStepArgs",
    "GuestPoliciesRecipeUpdateStepArgsDict",
    "GuestPoliciesRecipeUpdateStepArchiveExtractionArgs",
    ...,
    "GuestPoliciesRecipeUpdateStepDpkgInstallationArgs",
    ...,
    "GuestPoliciesRecipeUpdateStepFileCopyArgs",
    "GuestPoliciesRecipeUpdateStepFileCopyArgsDict",
    "GuestPoliciesRecipeUpdateStepFileExecArgs",
    "GuestPoliciesRecipeUpdateStepFileExecArgsDict",
    "GuestPoliciesRecipeUpdateStepMsiInstallationArgs",
    ...,
    "GuestPoliciesRecipeUpdateStepRpmInstallationArgs",
    ...,
    "GuestPoliciesRecipeUpdateStepScriptRunArgs",
    "GuestPoliciesRecipeUpdateStepScriptRunArgsDict",
    "OsPolicyAssignmentInstanceFilterArgs",
    "OsPolicyAssignmentInstanceFilterArgsDict",
    "OsPolicyAssignmentInstanceFilterExclusionLabelArgs",
    ...,
    "OsPolicyAssignmentInstanceFilterInclusionLabelArgs",
    ...,
    "OsPolicyAssignmentInstanceFilterInventoryArgs",
    "OsPolicyAssignmentInstanceFilterInventoryArgsDict",
    "OsPolicyAssignmentOsPolicyArgs",
    "OsPolicyAssignmentOsPolicyArgsDict",
    "OsPolicyAssignmentOsPolicyResourceGroupArgs",
    "OsPolicyAssignmentOsPolicyResourceGroupArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "OsPolicyAssignmentRolloutArgs",
    "OsPolicyAssignmentRolloutArgsDict",
    "OsPolicyAssignmentRolloutDisruptionBudgetArgs",
    "OsPolicyAssignmentRolloutDisruptionBudgetArgsDict",
    "PatchDeploymentInstanceFilterArgs",
    "PatchDeploymentInstanceFilterArgsDict",
    "PatchDeploymentInstanceFilterGroupLabelArgs",
    "PatchDeploymentInstanceFilterGroupLabelArgsDict",
    "PatchDeploymentOneTimeScheduleArgs",
    "PatchDeploymentOneTimeScheduleArgsDict",
    "PatchDeploymentPatchConfigArgs",
    "PatchDeploymentPatchConfigArgsDict",
    "PatchDeploymentPatchConfigAptArgs",
    "PatchDeploymentPatchConfigAptArgsDict",
    "PatchDeploymentPatchConfigGooArgs",
    "PatchDeploymentPatchConfigGooArgsDict",
    "PatchDeploymentPatchConfigPostStepArgs",
    "PatchDeploymentPatchConfigPostStepArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PatchDeploymentPatchConfigPreStepArgs",
    "PatchDeploymentPatchConfigPreStepArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PatchDeploymentPatchConfigWindowsUpdateArgs",
    "PatchDeploymentPatchConfigWindowsUpdateArgsDict",
    "PatchDeploymentPatchConfigYumArgs",
    "PatchDeploymentPatchConfigYumArgsDict",
    "PatchDeploymentPatchConfigZypperArgs",
    "PatchDeploymentPatchConfigZypperArgsDict",
    "PatchDeploymentRecurringScheduleArgs",
    "PatchDeploymentRecurringScheduleArgsDict",
    "PatchDeploymentRecurringScheduleMonthlyArgs",
    "PatchDeploymentRecurringScheduleMonthlyArgsDict",
    ...,
    ...,
    "PatchDeploymentRecurringScheduleTimeOfDayArgs",
    "PatchDeploymentRecurringScheduleTimeOfDayArgsDict",
    "PatchDeploymentRecurringScheduleTimeZoneArgs",
    "PatchDeploymentRecurringScheduleTimeZoneArgsDict",
    "PatchDeploymentRecurringScheduleWeeklyArgs",
    "PatchDeploymentRecurringScheduleWeeklyArgsDict",
    "PatchDeploymentRolloutArgs",
    "PatchDeploymentRolloutArgsDict",
    "PatchDeploymentRolloutDisruptionBudgetArgs",
    "PatchDeploymentRolloutDisruptionBudgetArgsDict",
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
    ...,
    "V2PolicyOrchestratorOrchestratedResourceArgs",
    "V2PolicyOrchestratorOrchestratedResourceArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    "V2PolicyOrchestratorOrchestrationScopeArgs",
    "V2PolicyOrchestratorOrchestrationScopeArgsDict",
    "V2PolicyOrchestratorOrchestrationScopeSelectorArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "V2PolicyOrchestratorOrchestrationStateArgs",
    "V2PolicyOrchestratorOrchestrationStateArgsDict",
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
    ...,
]

class GuestPoliciesAssignmentArgsDict(TypedDict):
    group_labels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesAssignmentGroupLabelArgsDict]]]
    ]
    instance_name_prefixes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    instances: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    os_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesAssignmentOsTypeArgsDict]]]
    ]
    zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class GuestPoliciesAssignmentArgs:
    def __init__(
        __self__,
        *,
        group_labels: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesAssignmentGroupLabelArgs]]]
        ] = ...,
        instance_name_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        os_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesAssignmentOsTypeArgs]]]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupLabels")
    def group_labels(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesAssignmentGroupLabelArgs]]]
    ]: ...
    @group_labels.setter
    def group_labels(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesAssignmentGroupLabelArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceNamePrefixes")
    def instance_name_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_name_prefixes.setter
    def instance_name_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instances.setter
    def instances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osTypes")
    def os_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesAssignmentOsTypeArgs]]]
    ]: ...
    @os_types.setter
    def os_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesAssignmentOsTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GuestPoliciesAssignmentGroupLabelArgsDict(TypedDict):
    labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class GuestPoliciesAssignmentGroupLabelArgs:
    def __init__(
        __self__, *, labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @labels.setter
    def labels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class GuestPoliciesAssignmentOsTypeArgsDict(TypedDict):
    os_architecture: NotRequired[pulumi.Input[_builtins.str]]
    os_short_name: NotRequired[pulumi.Input[_builtins.str]]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesAssignmentOsTypeArgs:
    def __init__(
        __self__,
        *,
        os_architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        os_short_name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osArchitecture")
    def os_architecture(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_architecture.setter
    def os_architecture(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_short_name.setter
    def os_short_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesPackageArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    desired_state: NotRequired[pulumi.Input[_builtins.str]]
    manager: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesPackageArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        manager: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def manager(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manager.setter
    def manager(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesPackageRepositoryArgsDict(TypedDict):
    apt: NotRequired[pulumi.Input[GuestPoliciesPackageRepositoryAptArgsDict]]
    goo: NotRequired[pulumi.Input[GuestPoliciesPackageRepositoryGooArgsDict]]
    yum: NotRequired[pulumi.Input[GuestPoliciesPackageRepositoryYumArgsDict]]
    zypper: NotRequired[pulumi.Input[GuestPoliciesPackageRepositoryZypperArgsDict]]
    ...

@pulumi.input_type
class GuestPoliciesPackageRepositoryArgs:
    def __init__(
        __self__,
        *,
        apt: Optional[pulumi.Input[GuestPoliciesPackageRepositoryAptArgs]] = ...,
        goo: Optional[pulumi.Input[GuestPoliciesPackageRepositoryGooArgs]] = ...,
        yum: Optional[pulumi.Input[GuestPoliciesPackageRepositoryYumArgs]] = ...,
        zypper: Optional[pulumi.Input[GuestPoliciesPackageRepositoryZypperArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(self) -> Optional[pulumi.Input[GuestPoliciesPackageRepositoryAptArgs]]: ...
    @apt.setter
    def apt(
        self, value: Optional[pulumi.Input[GuestPoliciesPackageRepositoryAptArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def goo(self) -> Optional[pulumi.Input[GuestPoliciesPackageRepositoryGooArgs]]: ...
    @goo.setter
    def goo(
        self, value: Optional[pulumi.Input[GuestPoliciesPackageRepositoryGooArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(self) -> Optional[pulumi.Input[GuestPoliciesPackageRepositoryYumArgs]]: ...
    @yum.setter
    def yum(
        self, value: Optional[pulumi.Input[GuestPoliciesPackageRepositoryYumArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesPackageRepositoryZypperArgs]]: ...
    @zypper.setter
    def zypper(
        self, value: Optional[pulumi.Input[GuestPoliciesPackageRepositoryZypperArgs]]
    ): ...

class GuestPoliciesPackageRepositoryAptArgsDict(TypedDict):
    components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    distribution: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    archive_type: NotRequired[pulumi.Input[_builtins.str]]
    gpg_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesPackageRepositoryAptArgs:
    def __init__(
        __self__,
        *,
        components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        distribution: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        archive_type: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @components.setter
    def components(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Input[_builtins.str]: ...
    @distribution.setter
    def distribution(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @archive_type.setter
    def archive_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpg_key.setter
    def gpg_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesPackageRepositoryGooArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class GuestPoliciesPackageRepositoryGooArgs:
    def __init__(
        __self__, *, name: pulumi.Input[_builtins.str], url: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class GuestPoliciesPackageRepositoryYumArgsDict(TypedDict):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class GuestPoliciesPackageRepositoryYumArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GuestPoliciesPackageRepositoryZypperArgsDict(TypedDict):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class GuestPoliciesPackageRepositoryZypperArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GuestPoliciesRecipeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    artifacts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArtifactArgsDict]]]
    ]
    desired_state: NotRequired[pulumi.Input[_builtins.str]]
    install_steps: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeInstallStepArgsDict]]]
    ]
    update_steps: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeUpdateStepArgsDict]]]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArtifactArgs]]]
        ] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        install_steps: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeInstallStepArgs]]]
        ] = ...,
        update_steps: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeUpdateStepArgs]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArtifactArgs]]]
    ]: ...
    @artifacts.setter
    def artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArtifactArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="installSteps")
    def install_steps(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeInstallStepArgs]]]
    ]: ...
    @install_steps.setter
    def install_steps(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeInstallStepArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateSteps")
    def update_steps(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeUpdateStepArgs]]]
    ]: ...
    @update_steps.setter
    def update_steps(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeUpdateStepArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeArtifactArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[pulumi.Input[GuestPoliciesRecipeArtifactGcsArgsDict]]
    remote: NotRequired[pulumi.Input[GuestPoliciesRecipeArtifactRemoteArgsDict]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeArtifactArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[pulumi.Input[GuestPoliciesRecipeArtifactGcsArgs]] = ...,
        remote: Optional[pulumi.Input[GuestPoliciesRecipeArtifactRemoteArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Optional[pulumi.Input[GuestPoliciesRecipeArtifactGcsArgs]]: ...
    @gcs.setter
    def gcs(
        self, value: Optional[pulumi.Input[GuestPoliciesRecipeArtifactGcsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeArtifactRemoteArgs]]: ...
    @remote.setter
    def remote(
        self, value: Optional[pulumi.Input[GuestPoliciesRecipeArtifactRemoteArgs]]
    ): ...

class GuestPoliciesRecipeArtifactGcsArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    object: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeArtifactGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        object: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object.setter
    def object(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeArtifactRemoteArgsDict(TypedDict):
    check_sum: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeArtifactRemoteArgs:
    def __init__(
        __self__,
        *,
        check_sum: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkSum")
    def check_sum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @check_sum.setter
    def check_sum(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeInstallStepArgsDict(TypedDict):
    archive_extraction: NotRequired[
        pulumi.Input[GuestPoliciesRecipeInstallStepArchiveExtractionArgsDict]
    ]
    dpkg_installation: NotRequired[
        pulumi.Input[GuestPoliciesRecipeInstallStepDpkgInstallationArgsDict]
    ]
    file_copy: NotRequired[pulumi.Input[GuestPoliciesRecipeInstallStepFileCopyArgsDict]]
    file_exec: NotRequired[pulumi.Input[GuestPoliciesRecipeInstallStepFileExecArgsDict]]
    msi_installation: NotRequired[
        pulumi.Input[GuestPoliciesRecipeInstallStepMsiInstallationArgsDict]
    ]
    rpm_installation: NotRequired[
        pulumi.Input[GuestPoliciesRecipeInstallStepRpmInstallationArgsDict]
    ]
    script_run: NotRequired[
        pulumi.Input[GuestPoliciesRecipeInstallStepScriptRunArgsDict]
    ]
    ...

@pulumi.input_type
class GuestPoliciesRecipeInstallStepArgs:
    def __init__(
        __self__,
        *,
        archive_extraction: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepArchiveExtractionArgs]
        ] = ...,
        dpkg_installation: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepDpkgInstallationArgs]
        ] = ...,
        file_copy: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepFileCopyArgs]
        ] = ...,
        file_exec: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepFileExecArgs]
        ] = ...,
        msi_installation: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepMsiInstallationArgs]
        ] = ...,
        rpm_installation: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepRpmInstallationArgs]
        ] = ...,
        script_run: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepScriptRunArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveExtraction")
    def archive_extraction(
        self,
    ) -> Optional[
        pulumi.Input[GuestPoliciesRecipeInstallStepArchiveExtractionArgs]
    ]: ...
    @archive_extraction.setter
    def archive_extraction(
        self,
        value: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepArchiveExtractionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dpkgInstallation")
    def dpkg_installation(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeInstallStepDpkgInstallationArgs]]: ...
    @dpkg_installation.setter
    def dpkg_installation(
        self,
        value: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepDpkgInstallationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileCopy")
    def file_copy(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeInstallStepFileCopyArgs]]: ...
    @file_copy.setter
    def file_copy(
        self, value: Optional[pulumi.Input[GuestPoliciesRecipeInstallStepFileCopyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileExec")
    def file_exec(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeInstallStepFileExecArgs]]: ...
    @file_exec.setter
    def file_exec(
        self, value: Optional[pulumi.Input[GuestPoliciesRecipeInstallStepFileExecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="msiInstallation")
    def msi_installation(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeInstallStepMsiInstallationArgs]]: ...
    @msi_installation.setter
    def msi_installation(
        self,
        value: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepMsiInstallationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rpmInstallation")
    def rpm_installation(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeInstallStepRpmInstallationArgs]]: ...
    @rpm_installation.setter
    def rpm_installation(
        self,
        value: Optional[
            pulumi.Input[GuestPoliciesRecipeInstallStepRpmInstallationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptRun")
    def script_run(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeInstallStepScriptRunArgs]]: ...
    @script_run.setter
    def script_run(
        self, value: Optional[pulumi.Input[GuestPoliciesRecipeInstallStepScriptRunArgs]]
    ): ...

class GuestPoliciesRecipeInstallStepArchiveExtractionArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    destination: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeInstallStepArchiveExtractionArgs:
    def __init__(
        __self__,
        *,
        artifact_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeInstallStepDpkgInstallationArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class GuestPoliciesRecipeInstallStepDpkgInstallationArgs:
    def __init__(__self__, *, artifact_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...

class GuestPoliciesRecipeInstallStepFileCopyArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    destination: pulumi.Input[_builtins.str]
    overwrite: NotRequired[pulumi.Input[_builtins.bool]]
    permissions: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeInstallStepFileCopyArgs:
    def __init__(
        __self__,
        *,
        artifact_id: pulumi.Input[_builtins.str],
        destination: pulumi.Input[_builtins.str],
        overwrite: Optional[pulumi.Input[_builtins.bool]] = ...,
        permissions: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def overwrite(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @overwrite.setter
    def overwrite(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeInstallStepFileExecArgsDict(TypedDict):
    allowed_exit_codes: NotRequired[pulumi.Input[_builtins.str]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    artifact_id: NotRequired[pulumi.Input[_builtins.str]]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeInstallStepFileExecArgs:
    def __init__(
        __self__,
        *,
        allowed_exit_codes: Optional[pulumi.Input[_builtins.str]] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        artifact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allowed_exit_codes.setter
    def allowed_exit_codes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_id.setter
    def artifact_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeInstallStepMsiInstallationArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    allowed_exit_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    flags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeInstallStepMsiInstallationArgs:
    def __init__(
        __self__,
        *,
        artifact_id: pulumi.Input[_builtins.str],
        allowed_exit_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        flags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_exit_codes.setter
    def allowed_exit_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def flags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @flags.setter
    def flags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GuestPoliciesRecipeInstallStepRpmInstallationArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class GuestPoliciesRecipeInstallStepRpmInstallationArgs:
    def __init__(__self__, *, artifact_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...

class GuestPoliciesRecipeInstallStepScriptRunArgsDict(TypedDict):
    script: pulumi.Input[_builtins.str]
    allowed_exit_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    interpreter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeInstallStepScriptRunArgs:
    def __init__(
        __self__,
        *,
        script: pulumi.Input[_builtins.str],
        allowed_exit_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        interpreter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> pulumi.Input[_builtins.str]: ...
    @script.setter
    def script(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_exit_codes.setter
    def allowed_exit_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interpreter.setter
    def interpreter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeUpdateStepArgsDict(TypedDict):
    archive_extraction: NotRequired[
        pulumi.Input[GuestPoliciesRecipeUpdateStepArchiveExtractionArgsDict]
    ]
    dpkg_installation: NotRequired[
        pulumi.Input[GuestPoliciesRecipeUpdateStepDpkgInstallationArgsDict]
    ]
    file_copy: NotRequired[pulumi.Input[GuestPoliciesRecipeUpdateStepFileCopyArgsDict]]
    file_exec: NotRequired[pulumi.Input[GuestPoliciesRecipeUpdateStepFileExecArgsDict]]
    msi_installation: NotRequired[
        pulumi.Input[GuestPoliciesRecipeUpdateStepMsiInstallationArgsDict]
    ]
    rpm_installation: NotRequired[
        pulumi.Input[GuestPoliciesRecipeUpdateStepRpmInstallationArgsDict]
    ]
    script_run: NotRequired[
        pulumi.Input[GuestPoliciesRecipeUpdateStepScriptRunArgsDict]
    ]
    ...

@pulumi.input_type
class GuestPoliciesRecipeUpdateStepArgs:
    def __init__(
        __self__,
        *,
        archive_extraction: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepArchiveExtractionArgs]
        ] = ...,
        dpkg_installation: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepDpkgInstallationArgs]
        ] = ...,
        file_copy: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepFileCopyArgs]
        ] = ...,
        file_exec: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepFileExecArgs]
        ] = ...,
        msi_installation: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepMsiInstallationArgs]
        ] = ...,
        rpm_installation: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepRpmInstallationArgs]
        ] = ...,
        script_run: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepScriptRunArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveExtraction")
    def archive_extraction(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepArchiveExtractionArgs]]: ...
    @archive_extraction.setter
    def archive_extraction(
        self,
        value: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepArchiveExtractionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dpkgInstallation")
    def dpkg_installation(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepDpkgInstallationArgs]]: ...
    @dpkg_installation.setter
    def dpkg_installation(
        self,
        value: Optional[
            pulumi.Input[GuestPoliciesRecipeUpdateStepDpkgInstallationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileCopy")
    def file_copy(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepFileCopyArgs]]: ...
    @file_copy.setter
    def file_copy(
        self, value: Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepFileCopyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileExec")
    def file_exec(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepFileExecArgs]]: ...
    @file_exec.setter
    def file_exec(
        self, value: Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepFileExecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="msiInstallation")
    def msi_installation(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepMsiInstallationArgs]]: ...
    @msi_installation.setter
    def msi_installation(
        self,
        value: Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepMsiInstallationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rpmInstallation")
    def rpm_installation(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepRpmInstallationArgs]]: ...
    @rpm_installation.setter
    def rpm_installation(
        self,
        value: Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepRpmInstallationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptRun")
    def script_run(
        self,
    ) -> Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepScriptRunArgs]]: ...
    @script_run.setter
    def script_run(
        self, value: Optional[pulumi.Input[GuestPoliciesRecipeUpdateStepScriptRunArgs]]
    ): ...

class GuestPoliciesRecipeUpdateStepArchiveExtractionArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    destination: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeUpdateStepArchiveExtractionArgs:
    def __init__(
        __self__,
        *,
        artifact_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeUpdateStepDpkgInstallationArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class GuestPoliciesRecipeUpdateStepDpkgInstallationArgs:
    def __init__(__self__, *, artifact_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...

class GuestPoliciesRecipeUpdateStepFileCopyArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    destination: pulumi.Input[_builtins.str]
    overwrite: NotRequired[pulumi.Input[_builtins.bool]]
    permissions: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeUpdateStepFileCopyArgs:
    def __init__(
        __self__,
        *,
        artifact_id: pulumi.Input[_builtins.str],
        destination: pulumi.Input[_builtins.str],
        overwrite: Optional[pulumi.Input[_builtins.bool]] = ...,
        permissions: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def overwrite(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @overwrite.setter
    def overwrite(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeUpdateStepFileExecArgsDict(TypedDict):
    allowed_exit_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    artifact_id: NotRequired[pulumi.Input[_builtins.str]]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeUpdateStepFileExecArgs:
    def __init__(
        __self__,
        *,
        allowed_exit_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        artifact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_exit_codes.setter
    def allowed_exit_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_id.setter
    def artifact_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestPoliciesRecipeUpdateStepMsiInstallationArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    allowed_exit_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    flags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeUpdateStepMsiInstallationArgs:
    def __init__(
        __self__,
        *,
        artifact_id: pulumi.Input[_builtins.str],
        allowed_exit_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        flags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_exit_codes.setter
    def allowed_exit_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def flags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @flags.setter
    def flags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GuestPoliciesRecipeUpdateStepRpmInstallationArgsDict(TypedDict):
    artifact_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class GuestPoliciesRecipeUpdateStepRpmInstallationArgs:
    def __init__(__self__, *, artifact_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[_builtins.str]): ...

class GuestPoliciesRecipeUpdateStepScriptRunArgsDict(TypedDict):
    script: pulumi.Input[_builtins.str]
    allowed_exit_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    interpreter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuestPoliciesRecipeUpdateStepScriptRunArgs:
    def __init__(
        __self__,
        *,
        script: pulumi.Input[_builtins.str],
        allowed_exit_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        interpreter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> pulumi.Input[_builtins.str]: ...
    @script.setter
    def script(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_exit_codes.setter
    def allowed_exit_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interpreter.setter
    def interpreter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentInstanceFilterArgsDict(TypedDict):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    exclusion_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[OsPolicyAssignmentInstanceFilterExclusionLabelArgsDict]
            ]
        ]
    ]
    inclusion_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[OsPolicyAssignmentInstanceFilterInclusionLabelArgsDict]
            ]
        ]
    ]
    inventories: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentInstanceFilterInventoryArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentInstanceFilterArgs:
    def __init__(
        __self__,
        *,
        all: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusion_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[OsPolicyAssignmentInstanceFilterExclusionLabelArgs]
                ]
            ]
        ] = ...,
        inclusion_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[OsPolicyAssignmentInstanceFilterInclusionLabelArgs]
                ]
            ]
        ] = ...,
        inventories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[OsPolicyAssignmentInstanceFilterInventoryArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all.setter
    def all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionLabels")
    def exclusion_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentInstanceFilterExclusionLabelArgs]]
        ]
    ]: ...
    @exclusion_labels.setter
    def exclusion_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[OsPolicyAssignmentInstanceFilterExclusionLabelArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionLabels")
    def inclusion_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentInstanceFilterInclusionLabelArgs]]
        ]
    ]: ...
    @inclusion_labels.setter
    def inclusion_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[OsPolicyAssignmentInstanceFilterInclusionLabelArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inventories(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentInstanceFilterInventoryArgs]]
        ]
    ]: ...
    @inventories.setter
    def inventories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[OsPolicyAssignmentInstanceFilterInventoryArgs]]
            ]
        ],
    ): ...

class OsPolicyAssignmentInstanceFilterExclusionLabelArgsDict(TypedDict):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class OsPolicyAssignmentInstanceFilterExclusionLabelArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class OsPolicyAssignmentInstanceFilterInclusionLabelArgsDict(TypedDict):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class OsPolicyAssignmentInstanceFilterInclusionLabelArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class OsPolicyAssignmentInstanceFilterInventoryArgsDict(TypedDict):
    os_short_name: pulumi.Input[_builtins.str]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentInstanceFilterInventoryArgs:
    def __init__(
        __self__,
        *,
        os_short_name: pulumi.Input[_builtins.str],
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> pulumi.Input[_builtins.str]: ...
    @os_short_name.setter
    def os_short_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    mode: pulumi.Input[_builtins.str]
    resource_groups: pulumi.Input[
        Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupArgsDict]]
    ]
    allow_no_resource_group_match: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        mode: pulumi.Input[_builtins.str],
        resource_groups: pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupArgs]]
        ],
        allow_no_resource_group_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupArgs]]
    ]: ...
    @resource_groups.setter
    def resource_groups(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowNoResourceGroupMatch")
    def allow_no_resource_group_match(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_no_resource_group_match.setter
    def allow_no_resource_group_match(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupArgsDict(TypedDict):
    resources: pulumi.Input[
        Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceArgsDict]]
    ]
    inventory_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    OsPolicyAssignmentOsPolicyResourceGroupInventoryFilterArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupArgs:
    def __init__(
        __self__,
        *,
        resources: pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceArgs]]
        ],
        inventory_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        OsPolicyAssignmentOsPolicyResourceGroupInventoryFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceArgs]]
    ]: ...
    @resources.setter
    def resources(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inventoryFilters")
    def inventory_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupInventoryFilterArgs]
            ]
        ]
    ]: ...
    @inventory_filters.setter
    def inventory_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        OsPolicyAssignmentOsPolicyResourceGroupInventoryFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupInventoryFilterArgsDict(TypedDict):
    os_short_name: pulumi.Input[_builtins.str]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupInventoryFilterArgs:
    def __init__(
        __self__,
        *,
        os_short_name: pulumi.Input[_builtins.str],
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> pulumi.Input[_builtins.str]: ...
    @os_short_name.setter
    def os_short_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    exec_: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecArgsDict]
    ]
    file: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileArgsDict]
    ]
    pkg: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgArgsDict]
    ]
    repository: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryArgsDict]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        exec_: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecArgs]
        ] = ...,
        file: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileArgs]
        ] = ...,
        pkg: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgArgs]
        ] = ...,
        repository: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecArgs]
    ]: ...
    @exec_.setter
    def exec_(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileArgs]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def pkg(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgArgs]
    ]: ...
    @pkg.setter
    def pkg(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryArgs]
    ]: ...
    @repository.setter
    def repository(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryArgs]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecArgsDict(TypedDict):
    validate: pulumi.Input[
        OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateArgsDict
    ]
    enforce: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceArgsDict]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecArgs:
    def __init__(
        __self__,
        *,
        validate: pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateArgs
        ],
        enforce: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> pulumi.Input[
        OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateArgs
    ]: ...
    @validate.setter
    def validate(
        self,
        value: pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enforce(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceArgs]
    ]: ...
    @enforce.setter
    def enforce(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceArgs]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceArgsDict(TypedDict):
    interpreter: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileArgsDict
        ]
    ]
    output_file_path: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceArgs:
    def __init__(
        __self__,
        *,
        interpreter: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileArgs
            ]
        ] = ...,
        output_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> pulumi.Input[_builtins.str]: ...
    @interpreter.setter
    def interpreter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileArgs]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_path.setter
    def output_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileArgsDict(TypedDict):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
            ]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateArgsDict(TypedDict):
    interpreter: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileArgsDict
        ]
    ]
    output_file_path: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateArgs:
    def __init__(
        __self__,
        *,
        interpreter: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileArgs
            ]
        ] = ...,
        output_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> pulumi.Input[_builtins.str]: ...
    @interpreter.setter
    def interpreter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_path.setter
    def output_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
            ]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceFileArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    content: NotRequired[pulumi.Input[_builtins.str]]
    file: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileArgsDict]
    ]
    permissions: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceFileArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        state: pulumi.Input[_builtins.str],
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        file: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileArgs]
        ] = ...,
        permissions: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileArgs]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileArgsDict(TypedDict):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcsArgsDict]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcsArgs]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcsArgs]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemoteArgs]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemoteArgs
            ]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemoteArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgArgsDict(TypedDict):
    desired_state: pulumi.Input[_builtins.str]
    apt: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgAptArgsDict]
    ]
    deb: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebArgsDict]
    ]
    googet: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGoogetArgsDict]
    ]
    msi: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiArgsDict]
    ]
    rpm: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmArgsDict]
    ]
    yum: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYumArgsDict]
    ]
    zypper: NotRequired[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypperArgsDict]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgArgs:
    def __init__(
        __self__,
        *,
        desired_state: pulumi.Input[_builtins.str],
        apt: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgAptArgs]
        ] = ...,
        deb: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebArgs]
        ] = ...,
        googet: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGoogetArgs]
        ] = ...,
        msi: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiArgs]
        ] = ...,
        rpm: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmArgs]
        ] = ...,
        yum: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYumArgs]
        ] = ...,
        zypper: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypperArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Input[_builtins.str]: ...
    @desired_state.setter
    def desired_state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgAptArgs]
    ]: ...
    @apt.setter
    def apt(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgAptArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def deb(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebArgs]
    ]: ...
    @deb.setter
    def deb(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def googet(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGoogetArgs]
    ]: ...
    @googet.setter
    def googet(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGoogetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def msi(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiArgs]
    ]: ...
    @msi.setter
    def msi(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rpm(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmArgs]
    ]: ...
    @rpm.setter
    def rpm(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYumArgs]
    ]: ...
    @yum.setter
    def yum(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYumArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypperArgs]
    ]: ...
    @zypper.setter
    def zypper(
        self,
        value: Optional[
            pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypperArgs]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgAptArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgAptArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebArgsDict(TypedDict):
    source: pulumi.Input[
        OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceArgsDict
    ]
    pull_deps: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceArgs
        ],
        pull_deps: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pull_deps.setter
    def pull_deps(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceArgsDict(TypedDict):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcsArgs]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
            ]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGoogetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGoogetArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiArgsDict(TypedDict):
    source: pulumi.Input[
        OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceArgsDict
    ]
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceArgs
        ],
        properties: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceArgsDict(TypedDict):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
            ]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmArgsDict(TypedDict):
    source: pulumi.Input[
        OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceArgsDict
    ]
    pull_deps: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceArgs
        ],
        pull_deps: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pull_deps.setter
    def pull_deps(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceArgsDict(TypedDict):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
            ]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYumArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYumArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypperArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypperArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryArgsDict(TypedDict):
    apt: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryAptArgsDict
        ]
    ]
    goo: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGooArgsDict
        ]
    ]
    yum: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYumArgsDict
        ]
    ]
    zypper: NotRequired[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypperArgsDict
        ]
    ]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryArgs:
    def __init__(
        __self__,
        *,
        apt: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryAptArgs
            ]
        ] = ...,
        goo: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGooArgs
            ]
        ] = ...,
        yum: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYumArgs
            ]
        ] = ...,
        zypper: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypperArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryAptArgs]
    ]: ...
    @apt.setter
    def apt(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryAptArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def goo(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGooArgs]
    ]: ...
    @goo.setter
    def goo(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGooArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        pulumi.Input[OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYumArgs]
    ]: ...
    @yum.setter
    def yum(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYumArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        pulumi.Input[
            OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypperArgs
        ]
    ]: ...
    @zypper.setter
    def zypper(
        self,
        value: Optional[
            pulumi.Input[
                OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypperArgs
            ]
        ],
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryAptArgsDict(TypedDict):
    archive_type: pulumi.Input[_builtins.str]
    components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    distribution: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    gpg_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryAptArgs:
    def __init__(
        __self__,
        *,
        archive_type: pulumi.Input[_builtins.str],
        components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        distribution: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        gpg_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> pulumi.Input[_builtins.str]: ...
    @archive_type.setter
    def archive_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @components.setter
    def components(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Input[_builtins.str]: ...
    @distribution.setter
    def distribution(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpg_key.setter
    def gpg_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGooArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGooArgs:
    def __init__(
        __self__, *, name: pulumi.Input[_builtins.str], url: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYumArgsDict(TypedDict):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYumArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypperArgsDict(
    TypedDict
):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypperArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OsPolicyAssignmentRolloutArgsDict(TypedDict):
    disruption_budget: pulumi.Input[OsPolicyAssignmentRolloutDisruptionBudgetArgsDict]
    min_wait_duration: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OsPolicyAssignmentRolloutArgs:
    def __init__(
        __self__,
        *,
        disruption_budget: pulumi.Input[OsPolicyAssignmentRolloutDisruptionBudgetArgs],
        min_wait_duration: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> pulumi.Input[OsPolicyAssignmentRolloutDisruptionBudgetArgs]: ...
    @disruption_budget.setter
    def disruption_budget(
        self, value: pulumi.Input[OsPolicyAssignmentRolloutDisruptionBudgetArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minWaitDuration")
    def min_wait_duration(self) -> pulumi.Input[_builtins.str]: ...
    @min_wait_duration.setter
    def min_wait_duration(self, value: pulumi.Input[_builtins.str]): ...

class OsPolicyAssignmentRolloutDisruptionBudgetArgsDict(TypedDict):
    fixed: NotRequired[pulumi.Input[_builtins.int]]
    percent: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class OsPolicyAssignmentRolloutDisruptionBudgetArgs:
    def __init__(
        __self__,
        *,
        fixed: Optional[pulumi.Input[_builtins.int]] = ...,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fixed.setter
    def fixed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PatchDeploymentInstanceFilterArgsDict(TypedDict):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    group_labels: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PatchDeploymentInstanceFilterGroupLabelArgsDict]]
        ]
    ]
    instance_name_prefixes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    instances: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PatchDeploymentInstanceFilterArgs:
    def __init__(
        __self__,
        *,
        all: Optional[pulumi.Input[_builtins.bool]] = ...,
        group_labels: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PatchDeploymentInstanceFilterGroupLabelArgs]]
            ]
        ] = ...,
        instance_name_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all.setter
    def all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="groupLabels")
    def group_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PatchDeploymentInstanceFilterGroupLabelArgs]]
        ]
    ]: ...
    @group_labels.setter
    def group_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PatchDeploymentInstanceFilterGroupLabelArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceNamePrefixes")
    def instance_name_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_name_prefixes.setter
    def instance_name_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instances.setter
    def instances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PatchDeploymentInstanceFilterGroupLabelArgsDict(TypedDict):
    labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PatchDeploymentInstanceFilterGroupLabelArgs:
    def __init__(
        __self__, *, labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @labels.setter
    def labels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class PatchDeploymentOneTimeScheduleArgsDict(TypedDict):
    execute_time: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PatchDeploymentOneTimeScheduleArgs:
    def __init__(__self__, *, execute_time: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executeTime")
    def execute_time(self) -> pulumi.Input[_builtins.str]: ...
    @execute_time.setter
    def execute_time(self, value: pulumi.Input[_builtins.str]): ...

class PatchDeploymentPatchConfigArgsDict(TypedDict):
    apt: NotRequired[pulumi.Input[PatchDeploymentPatchConfigAptArgsDict]]
    goo: NotRequired[pulumi.Input[PatchDeploymentPatchConfigGooArgsDict]]
    mig_instances_allowed: NotRequired[pulumi.Input[_builtins.bool]]
    post_step: NotRequired[pulumi.Input[PatchDeploymentPatchConfigPostStepArgsDict]]
    pre_step: NotRequired[pulumi.Input[PatchDeploymentPatchConfigPreStepArgsDict]]
    reboot_config: NotRequired[pulumi.Input[_builtins.str]]
    skip_unpatchable_vms: NotRequired[pulumi.Input[_builtins.bool]]
    windows_update: NotRequired[
        pulumi.Input[PatchDeploymentPatchConfigWindowsUpdateArgsDict]
    ]
    yum: NotRequired[pulumi.Input[PatchDeploymentPatchConfigYumArgsDict]]
    zypper: NotRequired[pulumi.Input[PatchDeploymentPatchConfigZypperArgsDict]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigArgs:
    def __init__(
        __self__,
        *,
        apt: Optional[pulumi.Input[PatchDeploymentPatchConfigAptArgs]] = ...,
        goo: Optional[pulumi.Input[PatchDeploymentPatchConfigGooArgs]] = ...,
        mig_instances_allowed: Optional[pulumi.Input[_builtins.bool]] = ...,
        post_step: Optional[pulumi.Input[PatchDeploymentPatchConfigPostStepArgs]] = ...,
        pre_step: Optional[pulumi.Input[PatchDeploymentPatchConfigPreStepArgs]] = ...,
        reboot_config: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_unpatchable_vms: Optional[pulumi.Input[_builtins.bool]] = ...,
        windows_update: Optional[
            pulumi.Input[PatchDeploymentPatchConfigWindowsUpdateArgs]
        ] = ...,
        yum: Optional[pulumi.Input[PatchDeploymentPatchConfigYumArgs]] = ...,
        zypper: Optional[pulumi.Input[PatchDeploymentPatchConfigZypperArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(self) -> Optional[pulumi.Input[PatchDeploymentPatchConfigAptArgs]]: ...
    @apt.setter
    def apt(self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigAptArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def goo(self) -> Optional[pulumi.Input[PatchDeploymentPatchConfigGooArgs]]: ...
    @goo.setter
    def goo(self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigGooArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="migInstancesAllowed")
    def mig_instances_allowed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @mig_instances_allowed.setter
    def mig_instances_allowed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="postStep")
    def post_step(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentPatchConfigPostStepArgs]]: ...
    @post_step.setter
    def post_step(
        self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigPostStepArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preStep")
    def pre_step(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentPatchConfigPreStepArgs]]: ...
    @pre_step.setter
    def pre_step(
        self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigPreStepArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rebootConfig")
    def reboot_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reboot_config.setter
    def reboot_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipUnpatchableVms")
    def skip_unpatchable_vms(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_unpatchable_vms.setter
    def skip_unpatchable_vms(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="windowsUpdate")
    def windows_update(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentPatchConfigWindowsUpdateArgs]]: ...
    @windows_update.setter
    def windows_update(
        self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigWindowsUpdateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(self) -> Optional[pulumi.Input[PatchDeploymentPatchConfigYumArgs]]: ...
    @yum.setter
    def yum(self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigYumArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentPatchConfigZypperArgs]]: ...
    @zypper.setter
    def zypper(
        self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigZypperArgs]]
    ): ...

class PatchDeploymentPatchConfigAptArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exclusive_packages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigAptArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        exclusive_packages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exclusivePackages")
    def exclusive_packages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusive_packages.setter
    def exclusive_packages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PatchDeploymentPatchConfigGooArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigGooArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class PatchDeploymentPatchConfigPostStepArgsDict(TypedDict):
    linux_exec_step_config: NotRequired[
        pulumi.Input[PatchDeploymentPatchConfigPostStepLinuxExecStepConfigArgsDict]
    ]
    windows_exec_step_config: NotRequired[
        pulumi.Input[PatchDeploymentPatchConfigPostStepWindowsExecStepConfigArgsDict]
    ]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPostStepArgs:
    def __init__(
        __self__,
        *,
        linux_exec_step_config: Optional[
            pulumi.Input[PatchDeploymentPatchConfigPostStepLinuxExecStepConfigArgs]
        ] = ...,
        windows_exec_step_config: Optional[
            pulumi.Input[PatchDeploymentPatchConfigPostStepWindowsExecStepConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxExecStepConfig")
    def linux_exec_step_config(
        self,
    ) -> Optional[
        pulumi.Input[PatchDeploymentPatchConfigPostStepLinuxExecStepConfigArgs]
    ]: ...
    @linux_exec_step_config.setter
    def linux_exec_step_config(
        self,
        value: Optional[
            pulumi.Input[PatchDeploymentPatchConfigPostStepLinuxExecStepConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsExecStepConfig")
    def windows_exec_step_config(
        self,
    ) -> Optional[
        pulumi.Input[PatchDeploymentPatchConfigPostStepWindowsExecStepConfigArgs]
    ]: ...
    @windows_exec_step_config.setter
    def windows_exec_step_config(
        self,
        value: Optional[
            pulumi.Input[PatchDeploymentPatchConfigPostStepWindowsExecStepConfigArgs]
        ],
    ): ...

class PatchDeploymentPatchConfigPostStepLinuxExecStepConfigArgsDict(TypedDict):
    allowed_success_codes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]
    gcs_object: NotRequired[
        pulumi.Input[
            PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectArgsDict
        ]
    ]
    interpreter: NotRequired[pulumi.Input[_builtins.str]]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPostStepLinuxExecStepConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_success_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        gcs_object: Optional[
            pulumi.Input[
                PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectArgs
            ]
        ] = ...,
        interpreter: Optional[pulumi.Input[_builtins.str]] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSuccessCodes")
    def allowed_success_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_success_codes.setter
    def allowed_success_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsObject")
    def gcs_object(
        self,
    ) -> Optional[
        pulumi.Input[PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectArgs]
    ]: ...
    @gcs_object.setter
    def gcs_object(
        self,
        value: Optional[
            pulumi.Input[
                PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interpreter.setter
    def interpreter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    generation_number: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObjectArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        generation_number: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="generationNumber")
    def generation_number(self) -> pulumi.Input[_builtins.str]: ...
    @generation_number.setter
    def generation_number(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...

class PatchDeploymentPatchConfigPostStepWindowsExecStepConfigArgsDict(TypedDict):
    allowed_success_codes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]
    gcs_object: NotRequired[
        pulumi.Input[
            PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectArgsDict
        ]
    ]
    interpreter: NotRequired[pulumi.Input[_builtins.str]]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPostStepWindowsExecStepConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_success_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        gcs_object: Optional[
            pulumi.Input[
                PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectArgs
            ]
        ] = ...,
        interpreter: Optional[pulumi.Input[_builtins.str]] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSuccessCodes")
    def allowed_success_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_success_codes.setter
    def allowed_success_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsObject")
    def gcs_object(
        self,
    ) -> Optional[
        pulumi.Input[
            PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectArgs
        ]
    ]: ...
    @gcs_object.setter
    def gcs_object(
        self,
        value: Optional[
            pulumi.Input[
                PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interpreter.setter
    def interpreter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    generation_number: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObjectArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        generation_number: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="generationNumber")
    def generation_number(self) -> pulumi.Input[_builtins.str]: ...
    @generation_number.setter
    def generation_number(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...

class PatchDeploymentPatchConfigPreStepArgsDict(TypedDict):
    linux_exec_step_config: NotRequired[
        pulumi.Input[PatchDeploymentPatchConfigPreStepLinuxExecStepConfigArgsDict]
    ]
    windows_exec_step_config: NotRequired[
        pulumi.Input[PatchDeploymentPatchConfigPreStepWindowsExecStepConfigArgsDict]
    ]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPreStepArgs:
    def __init__(
        __self__,
        *,
        linux_exec_step_config: Optional[
            pulumi.Input[PatchDeploymentPatchConfigPreStepLinuxExecStepConfigArgs]
        ] = ...,
        windows_exec_step_config: Optional[
            pulumi.Input[PatchDeploymentPatchConfigPreStepWindowsExecStepConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxExecStepConfig")
    def linux_exec_step_config(
        self,
    ) -> Optional[
        pulumi.Input[PatchDeploymentPatchConfigPreStepLinuxExecStepConfigArgs]
    ]: ...
    @linux_exec_step_config.setter
    def linux_exec_step_config(
        self,
        value: Optional[
            pulumi.Input[PatchDeploymentPatchConfigPreStepLinuxExecStepConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsExecStepConfig")
    def windows_exec_step_config(
        self,
    ) -> Optional[
        pulumi.Input[PatchDeploymentPatchConfigPreStepWindowsExecStepConfigArgs]
    ]: ...
    @windows_exec_step_config.setter
    def windows_exec_step_config(
        self,
        value: Optional[
            pulumi.Input[PatchDeploymentPatchConfigPreStepWindowsExecStepConfigArgs]
        ],
    ): ...

class PatchDeploymentPatchConfigPreStepLinuxExecStepConfigArgsDict(TypedDict):
    allowed_success_codes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]
    gcs_object: NotRequired[
        pulumi.Input[
            PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectArgsDict
        ]
    ]
    interpreter: NotRequired[pulumi.Input[_builtins.str]]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPreStepLinuxExecStepConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_success_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        gcs_object: Optional[
            pulumi.Input[
                PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectArgs
            ]
        ] = ...,
        interpreter: Optional[pulumi.Input[_builtins.str]] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSuccessCodes")
    def allowed_success_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_success_codes.setter
    def allowed_success_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsObject")
    def gcs_object(
        self,
    ) -> Optional[
        pulumi.Input[PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectArgs]
    ]: ...
    @gcs_object.setter
    def gcs_object(
        self,
        value: Optional[
            pulumi.Input[
                PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interpreter.setter
    def interpreter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    generation_number: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObjectArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        generation_number: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="generationNumber")
    def generation_number(self) -> pulumi.Input[_builtins.str]: ...
    @generation_number.setter
    def generation_number(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...

class PatchDeploymentPatchConfigPreStepWindowsExecStepConfigArgsDict(TypedDict):
    allowed_success_codes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]
    gcs_object: NotRequired[
        pulumi.Input[
            PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectArgsDict
        ]
    ]
    interpreter: NotRequired[pulumi.Input[_builtins.str]]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPreStepWindowsExecStepConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_success_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        gcs_object: Optional[
            pulumi.Input[
                PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectArgs
            ]
        ] = ...,
        interpreter: Optional[pulumi.Input[_builtins.str]] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSuccessCodes")
    def allowed_success_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allowed_success_codes.setter
    def allowed_success_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsObject")
    def gcs_object(
        self,
    ) -> Optional[
        pulumi.Input[
            PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectArgs
        ]
    ]: ...
    @gcs_object.setter
    def gcs_object(
        self,
        value: Optional[
            pulumi.Input[
                PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interpreter.setter
    def interpreter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    generation_number: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObjectArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        generation_number: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="generationNumber")
    def generation_number(self) -> pulumi.Input[_builtins.str]: ...
    @generation_number.setter
    def generation_number(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...

class PatchDeploymentPatchConfigWindowsUpdateArgsDict(TypedDict):
    classifications: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exclusive_patches: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigWindowsUpdateArgs:
    def __init__(
        __self__,
        *,
        classifications: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        exclusive_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classifications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @classifications.setter
    def classifications(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exclusivePatches")
    def exclusive_patches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusive_patches.setter
    def exclusive_patches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PatchDeploymentPatchConfigYumArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exclusive_packages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    minimal: NotRequired[pulumi.Input[_builtins.bool]]
    security: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigYumArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        exclusive_packages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        minimal: Optional[pulumi.Input[_builtins.bool]] = ...,
        security: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exclusivePackages")
    def exclusive_packages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusive_packages.setter
    def exclusive_packages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def minimal(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @minimal.setter
    def minimal(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def security(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @security.setter
    def security(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PatchDeploymentPatchConfigZypperArgsDict(TypedDict):
    categories: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exclusive_patches: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    severities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    with_optional: NotRequired[pulumi.Input[_builtins.bool]]
    with_update: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PatchDeploymentPatchConfigZypperArgs:
    def __init__(
        __self__,
        *,
        categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        exclusive_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        severities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        with_optional: Optional[pulumi.Input[_builtins.bool]] = ...,
        with_update: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def categories(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @categories.setter
    def categories(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exclusivePatches")
    def exclusive_patches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusive_patches.setter
    def exclusive_patches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def severities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @severities.setter
    def severities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="withOptional")
    def with_optional(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @with_optional.setter
    def with_optional(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="withUpdate")
    def with_update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @with_update.setter
    def with_update(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PatchDeploymentRecurringScheduleArgsDict(TypedDict):
    time_of_day: pulumi.Input[PatchDeploymentRecurringScheduleTimeOfDayArgsDict]
    time_zone: pulumi.Input[PatchDeploymentRecurringScheduleTimeZoneArgsDict]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    last_execute_time: NotRequired[pulumi.Input[_builtins.str]]
    monthly: NotRequired[pulumi.Input[PatchDeploymentRecurringScheduleMonthlyArgsDict]]
    next_execute_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    weekly: NotRequired[pulumi.Input[PatchDeploymentRecurringScheduleWeeklyArgsDict]]
    ...

@pulumi.input_type
class PatchDeploymentRecurringScheduleArgs:
    def __init__(
        __self__,
        *,
        time_of_day: pulumi.Input[PatchDeploymentRecurringScheduleTimeOfDayArgs],
        time_zone: pulumi.Input[PatchDeploymentRecurringScheduleTimeZoneArgs],
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_execute_time: Optional[pulumi.Input[_builtins.str]] = ...,
        monthly: Optional[
            pulumi.Input[PatchDeploymentRecurringScheduleMonthlyArgs]
        ] = ...,
        next_execute_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly: Optional[
            pulumi.Input[PatchDeploymentRecurringScheduleWeeklyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeOfDay")
    def time_of_day(
        self,
    ) -> pulumi.Input[PatchDeploymentRecurringScheduleTimeOfDayArgs]: ...
    @time_of_day.setter
    def time_of_day(
        self, value: pulumi.Input[PatchDeploymentRecurringScheduleTimeOfDayArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(
        self,
    ) -> pulumi.Input[PatchDeploymentRecurringScheduleTimeZoneArgs]: ...
    @time_zone.setter
    def time_zone(
        self, value: pulumi.Input[PatchDeploymentRecurringScheduleTimeZoneArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastExecuteTime")
    def last_execute_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_execute_time.setter
    def last_execute_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def monthly(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentRecurringScheduleMonthlyArgs]]: ...
    @monthly.setter
    def monthly(
        self, value: Optional[pulumi.Input[PatchDeploymentRecurringScheduleMonthlyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nextExecuteTime")
    def next_execute_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_execute_time.setter
    def next_execute_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weekly(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentRecurringScheduleWeeklyArgs]]: ...
    @weekly.setter
    def weekly(
        self, value: Optional[pulumi.Input[PatchDeploymentRecurringScheduleWeeklyArgs]]
    ): ...

class PatchDeploymentRecurringScheduleMonthlyArgsDict(TypedDict):
    month_day: NotRequired[pulumi.Input[_builtins.int]]
    week_day_of_month: NotRequired[
        pulumi.Input[PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthArgsDict]
    ]
    ...

@pulumi.input_type
class PatchDeploymentRecurringScheduleMonthlyArgs:
    def __init__(
        __self__,
        *,
        month_day: Optional[pulumi.Input[_builtins.int]] = ...,
        week_day_of_month: Optional[
            pulumi.Input[PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monthDay")
    def month_day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month_day.setter
    def month_day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="weekDayOfMonth")
    def week_day_of_month(
        self,
    ) -> Optional[
        pulumi.Input[PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthArgs]
    ]: ...
    @week_day_of_month.setter
    def week_day_of_month(
        self,
        value: Optional[
            pulumi.Input[PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthArgs]
        ],
    ): ...

class PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthArgsDict(TypedDict):
    day_of_week: pulumi.Input[_builtins.str]
    week_ordinal: pulumi.Input[_builtins.int]
    day_offset: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonthArgs:
    def __init__(
        __self__,
        *,
        day_of_week: pulumi.Input[_builtins.str],
        week_ordinal: pulumi.Input[_builtins.int],
        day_offset: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input[_builtins.str]: ...
    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="weekOrdinal")
    def week_ordinal(self) -> pulumi.Input[_builtins.int]: ...
    @week_ordinal.setter
    def week_ordinal(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="dayOffset")
    def day_offset(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day_offset.setter
    def day_offset(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PatchDeploymentRecurringScheduleTimeOfDayArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PatchDeploymentRecurringScheduleTimeOfDayArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PatchDeploymentRecurringScheduleTimeZoneArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PatchDeploymentRecurringScheduleTimeZoneArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PatchDeploymentRecurringScheduleWeeklyArgsDict(TypedDict):
    day_of_week: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PatchDeploymentRecurringScheduleWeeklyArgs:
    def __init__(__self__, *, day_of_week: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input[_builtins.str]: ...
    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input[_builtins.str]): ...

class PatchDeploymentRolloutArgsDict(TypedDict):
    disruption_budget: pulumi.Input[PatchDeploymentRolloutDisruptionBudgetArgsDict]
    mode: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PatchDeploymentRolloutArgs:
    def __init__(
        __self__,
        *,
        disruption_budget: pulumi.Input[PatchDeploymentRolloutDisruptionBudgetArgs],
        mode: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> pulumi.Input[PatchDeploymentRolloutDisruptionBudgetArgs]: ...
    @disruption_budget.setter
    def disruption_budget(
        self, value: pulumi.Input[PatchDeploymentRolloutDisruptionBudgetArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class PatchDeploymentRolloutDisruptionBudgetArgsDict(TypedDict):
    fixed: NotRequired[pulumi.Input[_builtins.int]]
    percentage: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PatchDeploymentRolloutDisruptionBudgetArgs:
    def __init__(
        __self__,
        *,
        fixed: Optional[pulumi.Input[_builtins.int]] = ...,
        percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fixed.setter
    def fixed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    os_policy_assignment_v1_payload: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        os_policy_assignment_v1_payload: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osPolicyAssignmentV1Payload")
    def os_policy_assignment_v1_payload(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
        ]
    ]: ...
    @os_policy_assignment_v1_payload.setter
    def os_policy_assignment_v1_payload(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadArgsDict(
    TypedDict
):
    instance_filter: pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgsDict
    ]
    os_policies: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgsDict
            ]
        ]
    ]
    rollout: pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgsDict
    ]
    baseline: NotRequired[pulumi.Input[_builtins.bool]]
    deleted: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    reconciling: NotRequired[pulumi.Input[_builtins.bool]]
    revision_create_time: NotRequired[pulumi.Input[_builtins.str]]
    revision_id: NotRequired[pulumi.Input[_builtins.str]]
    rollout_state: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadArgs:
    def __init__(
        __self__,
        *,
        instance_filter: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
        ],
        os_policies: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
                ]
            ]
        ],
        rollout: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
        ],
        baseline: Optional[pulumi.Input[_builtins.bool]] = ...,
        deleted: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision_create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_state: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
    ]: ...
    @instance_filter.setter
    def instance_filter(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
            ]
        ]
    ]: ...
    @os_policies.setter
    def os_policies(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rollout(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
    ]: ...
    @rollout.setter
    def rollout(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @baseline.setter
    def baseline(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deleted.setter
    def deleted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_create_time.setter
    def revision_create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_id.setter
    def revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_state.setter
    def rollout_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgsDict(
    TypedDict
):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    exclusion_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgsDict
                ]
            ]
        ]
    ]
    inclusion_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgsDict
                ]
            ]
        ]
    ]
    inventories: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs:
    def __init__(
        __self__,
        *,
        all: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusion_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                    ]
                ]
            ]
        ] = ...,
        inclusion_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                    ]
                ]
            ]
        ] = ...,
        inventories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all.setter
    def all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionLabels")
    def exclusion_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                ]
            ]
        ]
    ]: ...
    @exclusion_labels.setter
    def exclusion_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionLabels")
    def inclusion_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                ]
            ]
        ]
    ]: ...
    @inclusion_labels.setter
    def inclusion_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inventories(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                ]
            ]
        ]
    ]: ...
    @inventories.setter
    def inventories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgsDict(
    TypedDict
):
    os_short_name: pulumi.Input[_builtins.str]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs:
    def __init__(
        __self__,
        *,
        os_short_name: pulumi.Input[_builtins.str],
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> pulumi.Input[_builtins.str]: ...
    @os_short_name.setter
    def os_short_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    mode: pulumi.Input[_builtins.str]
    resource_groups: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgsDict
            ]
        ]
    ]
    allow_no_resource_group_match: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        mode: pulumi.Input[_builtins.str],
        resource_groups: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
                ]
            ]
        ],
        allow_no_resource_group_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
            ]
        ]
    ]: ...
    @resource_groups.setter
    def resource_groups(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowNoResourceGroupMatch")
    def allow_no_resource_group_match(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_no_resource_group_match.setter
    def allow_no_resource_group_match(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgsDict(
    TypedDict
):
    resources: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgsDict
            ]
        ]
    ]
    inventory_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs:
    def __init__(
        __self__,
        *,
        resources: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
                ]
            ]
        ],
        inventory_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
            ]
        ]
    ]: ...
    @resources.setter
    def resources(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inventoryFilters")
    def inventory_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                ]
            ]
        ]
    ]: ...
    @inventory_filters.setter
    def inventory_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgsDict(
    TypedDict
):
    os_short_name: pulumi.Input[_builtins.str]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs:
    def __init__(
        __self__,
        *,
        os_short_name: pulumi.Input[_builtins.str],
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> pulumi.Input[_builtins.str]: ...
    @os_short_name.setter
    def os_short_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    exec_: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgsDict
        ]
    ]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgsDict
        ]
    ]
    pkg: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgsDict
        ]
    ]
    repository: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        exec_: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
            ]
        ] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
            ]
        ] = ...,
        pkg: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
            ]
        ] = ...,
        repository: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
        ]
    ]: ...
    @exec_.setter
    def exec_(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def pkg(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
        ]
    ]: ...
    @pkg.setter
    def pkg(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
        ]
    ]: ...
    @repository.setter
    def repository(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgsDict(
    TypedDict
):
    validate: pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgsDict
    ]
    enforce: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs:
    def __init__(
        __self__,
        *,
        validate: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
        ],
        enforce: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
    ]: ...
    @validate.setter
    def validate(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enforce(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
        ]
    ]: ...
    @enforce.setter
    def enforce(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgsDict(
    TypedDict
):
    interpreter: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgsDict
        ]
    ]
    output_file_path: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs:
    def __init__(
        __self__,
        *,
        interpreter: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
            ]
        ] = ...,
        output_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> pulumi.Input[_builtins.str]: ...
    @interpreter.setter
    def interpreter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_path.setter
    def output_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgsDict(
    TypedDict
):
    interpreter: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgsDict
        ]
    ]
    output_file_path: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs:
    def __init__(
        __self__,
        *,
        interpreter: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
            ]
        ] = ...,
        output_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> pulumi.Input[_builtins.str]: ...
    @interpreter.setter
    def interpreter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_path.setter
    def output_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgsDict(
    TypedDict
):
    path: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    content: NotRequired[pulumi.Input[_builtins.str]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgsDict
        ]
    ]
    permissions: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        state: pulumi.Input[_builtins.str],
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
            ]
        ] = ...,
        permissions: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgsDict(
    TypedDict
):
    desired_state: pulumi.Input[_builtins.str]
    apt: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgsDict
        ]
    ]
    deb: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgsDict
        ]
    ]
    googet: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgsDict
        ]
    ]
    msi: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgsDict
        ]
    ]
    rpm: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgsDict
        ]
    ]
    yum: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgsDict
        ]
    ]
    zypper: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs:
    def __init__(
        __self__,
        *,
        desired_state: pulumi.Input[_builtins.str],
        apt: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
            ]
        ] = ...,
        deb: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
            ]
        ] = ...,
        googet: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
            ]
        ] = ...,
        msi: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
            ]
        ] = ...,
        rpm: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
            ]
        ] = ...,
        yum: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
            ]
        ] = ...,
        zypper: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Input[_builtins.str]: ...
    @desired_state.setter
    def desired_state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
        ]
    ]: ...
    @apt.setter
    def apt(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def deb(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
        ]
    ]: ...
    @deb.setter
    def deb(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def googet(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
        ]
    ]: ...
    @googet.setter
    def googet(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def msi(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
        ]
    ]: ...
    @msi.setter
    def msi(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rpm(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
        ]
    ]: ...
    @rpm.setter
    def rpm(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
        ]
    ]: ...
    @yum.setter
    def yum(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
        ]
    ]: ...
    @zypper.setter
    def zypper(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgsDict
    ]
    pull_deps: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
        ],
        pull_deps: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pull_deps.setter
    def pull_deps(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgsDict
    ]
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
        ],
        properties: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgsDict
    ]
    pull_deps: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
        ],
        pull_deps: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pull_deps.setter
    def pull_deps(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgsDict(
    TypedDict
):
    apt: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgsDict
        ]
    ]
    goo: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgsDict
        ]
    ]
    yum: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgsDict
        ]
    ]
    zypper: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs:
    def __init__(
        __self__,
        *,
        apt: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
            ]
        ] = ...,
        goo: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
            ]
        ] = ...,
        yum: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
            ]
        ] = ...,
        zypper: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
        ]
    ]: ...
    @apt.setter
    def apt(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def goo(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
        ]
    ]: ...
    @goo.setter
    def goo(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
        ]
    ]: ...
    @yum.setter
    def yum(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
        ]
    ]: ...
    @zypper.setter
    def zypper(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgsDict(
    TypedDict
):
    archive_type: pulumi.Input[_builtins.str]
    components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    distribution: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    gpg_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs:
    def __init__(
        __self__,
        *,
        archive_type: pulumi.Input[_builtins.str],
        components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        distribution: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        gpg_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> pulumi.Input[_builtins.str]: ...
    @archive_type.setter
    def archive_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @components.setter
    def components(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Input[_builtins.str]: ...
    @distribution.setter
    def distribution(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpg_key.setter
    def gpg_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs:
    def __init__(
        __self__, *, name: pulumi.Input[_builtins.str], url: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgsDict(
    TypedDict
):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgsDict(
    TypedDict
):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgsDict(
    TypedDict
):
    disruption_budget: pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgsDict
    ]
    min_wait_duration: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs:
    def __init__(
        __self__,
        *,
        disruption_budget: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
        ],
        min_wait_duration: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
    ]: ...
    @disruption_budget.setter
    def disruption_budget(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minWaitDuration")
    def min_wait_duration(self) -> pulumi.Input[_builtins.str]: ...
    @min_wait_duration.setter
    def min_wait_duration(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgsDict(
    TypedDict
):
    fixed: NotRequired[pulumi.Input[_builtins.int]]
    percent: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs:
    def __init__(
        __self__,
        *,
        fixed: Optional[pulumi.Input[_builtins.int]] = ...,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fixed.setter
    def fixed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class V2PolicyOrchestratorForFolderOrchestrationScopeArgsDict(TypedDict):
    selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationScopeSelectorArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationScopeArgs:
    def __init__(
        __self__,
        *,
        selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationScopeSelectorArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationScopeSelectorArgs
                ]
            ]
        ]
    ]: ...
    @selectors.setter
    def selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationScopeSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestrationScopeSelectorArgsDict(TypedDict):
    location_selector: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelectorArgsDict
        ]
    ]
    resource_hierarchy_selector: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelectorArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationScopeSelectorArgs:
    def __init__(
        __self__,
        *,
        location_selector: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelectorArgs
            ]
        ] = ...,
        resource_hierarchy_selector: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelectorArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationSelector")
    def location_selector(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelectorArgs
        ]
    ]: ...
    @location_selector.setter
    def location_selector(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelectorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceHierarchySelector")
    def resource_hierarchy_selector(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelectorArgs
        ]
    ]: ...
    @resource_hierarchy_selector.setter
    def resource_hierarchy_selector(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelectorArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelectorArgsDict(
    TypedDict
):
    included_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelectorArgs:
    def __init__(
        __self__,
        *,
        included_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedLocations")
    def included_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_locations.setter
    def included_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelectorArgsDict(
    TypedDict
):
    included_folders: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    included_projects: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelectorArgs:
    def __init__(
        __self__,
        *,
        included_folders: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        included_projects: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedFolders")
    def included_folders(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_folders.setter
    def included_folders(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedProjects")
    def included_projects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_projects.setter
    def included_projects(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForFolderOrchestrationStateArgsDict(TypedDict):
    current_iteration_states: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateArgsDict
                ]
            ]
        ]
    ]
    previous_iteration_states: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationStateArgs:
    def __init__(
        __self__,
        *,
        current_iteration_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateArgs
                    ]
                ]
            ]
        ] = ...,
        previous_iteration_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationStates")
    def current_iteration_states(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateArgs
                ]
            ]
        ]
    ]: ...
    @current_iteration_states.setter
    def current_iteration_states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="previousIterationStates")
    def previous_iteration_states(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateArgs
                ]
            ]
        ]
    ]: ...
    @previous_iteration_states.setter
    def previous_iteration_states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateArgsDict(
    TypedDict
):
    errors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorArgsDict
                ]
            ]
        ]
    ]
    failed_actions: NotRequired[pulumi.Input[_builtins.str]]
    finish_time: NotRequired[pulumi.Input[_builtins.str]]
    performed_actions: NotRequired[pulumi.Input[_builtins.str]]
    progress: NotRequired[pulumi.Input[_builtins.float]]
    rollout_resource: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateArgs:
    def __init__(
        __self__,
        *,
        errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorArgs
                    ]
                ]
            ]
        ] = ...,
        failed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        finish_time: Optional[pulumi.Input[_builtins.str]] = ...,
        performed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        progress: Optional[pulumi.Input[_builtins.float]] = ...,
        rollout_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorArgs
                ]
            ]
        ]
    ]: ...
    @errors.setter
    def errors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failed_actions.setter
    def failed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @finish_time.setter
    def finish_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performed_actions.setter
    def performed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @progress.setter
    def progress(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_resource.setter
    def rollout_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetailArgsDict
                ]
            ]
        ]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetailArgs
                ]
            ]
        ]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetailArgsDict(
    TypedDict
):
    type_url: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetailArgs:
    def __init__(
        __self__,
        *,
        type_url: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_url.setter
    def type_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateArgsDict(
    TypedDict
):
    errors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorArgsDict
                ]
            ]
        ]
    ]
    failed_actions: NotRequired[pulumi.Input[_builtins.str]]
    finish_time: NotRequired[pulumi.Input[_builtins.str]]
    performed_actions: NotRequired[pulumi.Input[_builtins.str]]
    progress: NotRequired[pulumi.Input[_builtins.float]]
    rollout_resource: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateArgs:
    def __init__(
        __self__,
        *,
        errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorArgs
                    ]
                ]
            ]
        ] = ...,
        failed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        finish_time: Optional[pulumi.Input[_builtins.str]] = ...,
        performed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        progress: Optional[pulumi.Input[_builtins.float]] = ...,
        rollout_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorArgs
                ]
            ]
        ]
    ]: ...
    @errors.setter
    def errors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failed_actions.setter
    def failed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @finish_time.setter
    def finish_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performed_actions.setter
    def performed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @progress.setter
    def progress(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_resource.setter
    def rollout_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetailArgsDict
                ]
            ]
        ]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetailArgs
                ]
            ]
        ]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetailArgsDict(
    TypedDict
):
    type_url: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetailArgs:
    def __init__(
        __self__,
        *,
        type_url: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_url.setter
    def type_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    os_policy_assignment_v1_payload: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        os_policy_assignment_v1_payload: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osPolicyAssignmentV1Payload")
    def os_policy_assignment_v1_payload(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
        ]
    ]: ...
    @os_policy_assignment_v1_payload.setter
    def os_policy_assignment_v1_payload(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadArgsDict(
    TypedDict
):
    instance_filter: pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgsDict
    ]
    os_policies: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgsDict
            ]
        ]
    ]
    rollout: pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgsDict
    ]
    baseline: NotRequired[pulumi.Input[_builtins.bool]]
    deleted: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    reconciling: NotRequired[pulumi.Input[_builtins.bool]]
    revision_create_time: NotRequired[pulumi.Input[_builtins.str]]
    revision_id: NotRequired[pulumi.Input[_builtins.str]]
    rollout_state: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadArgs:
    def __init__(
        __self__,
        *,
        instance_filter: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
        ],
        os_policies: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
                ]
            ]
        ],
        rollout: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
        ],
        baseline: Optional[pulumi.Input[_builtins.bool]] = ...,
        deleted: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision_create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_state: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
    ]: ...
    @instance_filter.setter
    def instance_filter(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
            ]
        ]
    ]: ...
    @os_policies.setter
    def os_policies(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rollout(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
    ]: ...
    @rollout.setter
    def rollout(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @baseline.setter
    def baseline(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deleted.setter
    def deleted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_create_time.setter
    def revision_create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_id.setter
    def revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_state.setter
    def rollout_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgsDict(
    TypedDict
):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    exclusion_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgsDict
                ]
            ]
        ]
    ]
    inclusion_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgsDict
                ]
            ]
        ]
    ]
    inventories: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs:
    def __init__(
        __self__,
        *,
        all: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusion_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                    ]
                ]
            ]
        ] = ...,
        inclusion_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                    ]
                ]
            ]
        ] = ...,
        inventories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all.setter
    def all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionLabels")
    def exclusion_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                ]
            ]
        ]
    ]: ...
    @exclusion_labels.setter
    def exclusion_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionLabels")
    def inclusion_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                ]
            ]
        ]
    ]: ...
    @inclusion_labels.setter
    def inclusion_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inventories(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                ]
            ]
        ]
    ]: ...
    @inventories.setter
    def inventories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgsDict(
    TypedDict
):
    os_short_name: pulumi.Input[_builtins.str]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs:
    def __init__(
        __self__,
        *,
        os_short_name: pulumi.Input[_builtins.str],
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> pulumi.Input[_builtins.str]: ...
    @os_short_name.setter
    def os_short_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    mode: pulumi.Input[_builtins.str]
    resource_groups: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgsDict
            ]
        ]
    ]
    allow_no_resource_group_match: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        mode: pulumi.Input[_builtins.str],
        resource_groups: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
                ]
            ]
        ],
        allow_no_resource_group_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
            ]
        ]
    ]: ...
    @resource_groups.setter
    def resource_groups(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowNoResourceGroupMatch")
    def allow_no_resource_group_match(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_no_resource_group_match.setter
    def allow_no_resource_group_match(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgsDict(
    TypedDict
):
    resources: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgsDict
            ]
        ]
    ]
    inventory_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs:
    def __init__(
        __self__,
        *,
        resources: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
                ]
            ]
        ],
        inventory_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
            ]
        ]
    ]: ...
    @resources.setter
    def resources(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inventoryFilters")
    def inventory_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                ]
            ]
        ]
    ]: ...
    @inventory_filters.setter
    def inventory_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgsDict(
    TypedDict
):
    os_short_name: pulumi.Input[_builtins.str]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs:
    def __init__(
        __self__,
        *,
        os_short_name: pulumi.Input[_builtins.str],
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> pulumi.Input[_builtins.str]: ...
    @os_short_name.setter
    def os_short_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    exec_: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgsDict
        ]
    ]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgsDict
        ]
    ]
    pkg: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgsDict
        ]
    ]
    repository: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        exec_: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
            ]
        ] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
            ]
        ] = ...,
        pkg: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
            ]
        ] = ...,
        repository: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
        ]
    ]: ...
    @exec_.setter
    def exec_(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def pkg(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
        ]
    ]: ...
    @pkg.setter
    def pkg(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
        ]
    ]: ...
    @repository.setter
    def repository(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgsDict(
    TypedDict
):
    validate: pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgsDict
    ]
    enforce: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs:
    def __init__(
        __self__,
        *,
        validate: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
        ],
        enforce: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
    ]: ...
    @validate.setter
    def validate(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enforce(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
        ]
    ]: ...
    @enforce.setter
    def enforce(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgsDict(
    TypedDict
):
    interpreter: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgsDict
        ]
    ]
    output_file_path: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs:
    def __init__(
        __self__,
        *,
        interpreter: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
            ]
        ] = ...,
        output_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> pulumi.Input[_builtins.str]: ...
    @interpreter.setter
    def interpreter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_path.setter
    def output_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgsDict(
    TypedDict
):
    interpreter: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgsDict
        ]
    ]
    output_file_path: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs:
    def __init__(
        __self__,
        *,
        interpreter: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
            ]
        ] = ...,
        output_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> pulumi.Input[_builtins.str]: ...
    @interpreter.setter
    def interpreter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_path.setter
    def output_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgsDict(
    TypedDict
):
    path: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    content: NotRequired[pulumi.Input[_builtins.str]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgsDict
        ]
    ]
    permissions: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        state: pulumi.Input[_builtins.str],
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
            ]
        ] = ...,
        permissions: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgsDict(
    TypedDict
):
    desired_state: pulumi.Input[_builtins.str]
    apt: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgsDict
        ]
    ]
    deb: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgsDict
        ]
    ]
    googet: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgsDict
        ]
    ]
    msi: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgsDict
        ]
    ]
    rpm: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgsDict
        ]
    ]
    yum: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgsDict
        ]
    ]
    zypper: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs:
    def __init__(
        __self__,
        *,
        desired_state: pulumi.Input[_builtins.str],
        apt: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
            ]
        ] = ...,
        deb: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
            ]
        ] = ...,
        googet: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
            ]
        ] = ...,
        msi: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
            ]
        ] = ...,
        rpm: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
            ]
        ] = ...,
        yum: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
            ]
        ] = ...,
        zypper: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Input[_builtins.str]: ...
    @desired_state.setter
    def desired_state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
        ]
    ]: ...
    @apt.setter
    def apt(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def deb(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
        ]
    ]: ...
    @deb.setter
    def deb(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def googet(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
        ]
    ]: ...
    @googet.setter
    def googet(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def msi(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
        ]
    ]: ...
    @msi.setter
    def msi(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rpm(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
        ]
    ]: ...
    @rpm.setter
    def rpm(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
        ]
    ]: ...
    @yum.setter
    def yum(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
        ]
    ]: ...
    @zypper.setter
    def zypper(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgsDict
    ]
    pull_deps: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
        ],
        pull_deps: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pull_deps.setter
    def pull_deps(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgsDict
    ]
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
        ],
        properties: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgsDict
    ]
    pull_deps: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
        ],
        pull_deps: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pull_deps.setter
    def pull_deps(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgsDict(
    TypedDict
):
    apt: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgsDict
        ]
    ]
    goo: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgsDict
        ]
    ]
    yum: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgsDict
        ]
    ]
    zypper: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs:
    def __init__(
        __self__,
        *,
        apt: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
            ]
        ] = ...,
        goo: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
            ]
        ] = ...,
        yum: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
            ]
        ] = ...,
        zypper: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
        ]
    ]: ...
    @apt.setter
    def apt(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def goo(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
        ]
    ]: ...
    @goo.setter
    def goo(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
        ]
    ]: ...
    @yum.setter
    def yum(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
        ]
    ]: ...
    @zypper.setter
    def zypper(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgsDict(
    TypedDict
):
    archive_type: pulumi.Input[_builtins.str]
    components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    distribution: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    gpg_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs:
    def __init__(
        __self__,
        *,
        archive_type: pulumi.Input[_builtins.str],
        components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        distribution: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        gpg_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> pulumi.Input[_builtins.str]: ...
    @archive_type.setter
    def archive_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @components.setter
    def components(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Input[_builtins.str]: ...
    @distribution.setter
    def distribution(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpg_key.setter
    def gpg_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs:
    def __init__(
        __self__, *, name: pulumi.Input[_builtins.str], url: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgsDict(
    TypedDict
):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgsDict(
    TypedDict
):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgsDict(
    TypedDict
):
    disruption_budget: pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgsDict
    ]
    min_wait_duration: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs:
    def __init__(
        __self__,
        *,
        disruption_budget: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
        ],
        min_wait_duration: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
    ]: ...
    @disruption_budget.setter
    def disruption_budget(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minWaitDuration")
    def min_wait_duration(self) -> pulumi.Input[_builtins.str]: ...
    @min_wait_duration.setter
    def min_wait_duration(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgsDict(
    TypedDict
):
    fixed: NotRequired[pulumi.Input[_builtins.int]]
    percent: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs:
    def __init__(
        __self__,
        *,
        fixed: Optional[pulumi.Input[_builtins.int]] = ...,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fixed.setter
    def fixed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class V2PolicyOrchestratorForOrganizationOrchestrationScopeArgsDict(TypedDict):
    selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationScopeArgs:
    def __init__(
        __self__,
        *,
        selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorArgs
                ]
            ]
        ]
    ]: ...
    @selectors.setter
    def selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorArgsDict(TypedDict):
    location_selector: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelectorArgsDict
        ]
    ]
    resource_hierarchy_selector: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelectorArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorArgs:
    def __init__(
        __self__,
        *,
        location_selector: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelectorArgs
            ]
        ] = ...,
        resource_hierarchy_selector: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelectorArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationSelector")
    def location_selector(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelectorArgs
        ]
    ]: ...
    @location_selector.setter
    def location_selector(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelectorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceHierarchySelector")
    def resource_hierarchy_selector(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelectorArgs
        ]
    ]: ...
    @resource_hierarchy_selector.setter
    def resource_hierarchy_selector(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelectorArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelectorArgsDict(
    TypedDict
):
    included_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelectorArgs:
    def __init__(
        __self__,
        *,
        included_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedLocations")
    def included_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_locations.setter
    def included_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelectorArgsDict(
    TypedDict
):
    included_folders: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    included_projects: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelectorArgs:
    def __init__(
        __self__,
        *,
        included_folders: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        included_projects: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedFolders")
    def included_folders(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_folders.setter
    def included_folders(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedProjects")
    def included_projects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_projects.setter
    def included_projects(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestrationStateArgsDict(TypedDict):
    current_iteration_states: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateArgsDict
                ]
            ]
        ]
    ]
    previous_iteration_state: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationStateArgs:
    def __init__(
        __self__,
        *,
        current_iteration_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateArgs
                    ]
                ]
            ]
        ] = ...,
        previous_iteration_state: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationStates")
    def current_iteration_states(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateArgs
                ]
            ]
        ]
    ]: ...
    @current_iteration_states.setter
    def current_iteration_states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="previousIterationState")
    def previous_iteration_state(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateArgs
        ]
    ]: ...
    @previous_iteration_state.setter
    def previous_iteration_state(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateArgsDict(
    TypedDict
):
    error: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorArgsDict
        ]
    ]
    failed_actions: NotRequired[pulumi.Input[_builtins.str]]
    finish_time: NotRequired[pulumi.Input[_builtins.str]]
    performed_actions: NotRequired[pulumi.Input[_builtins.str]]
    progress: NotRequired[pulumi.Input[_builtins.float]]
    rollout_resource: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateArgs:
    def __init__(
        __self__,
        *,
        error: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorArgs
            ]
        ] = ...,
        failed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        finish_time: Optional[pulumi.Input[_builtins.str]] = ...,
        performed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        progress: Optional[pulumi.Input[_builtins.float]] = ...,
        rollout_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorArgs
        ]
    ]: ...
    @error.setter
    def error(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failed_actions.setter
    def failed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @finish_time.setter
    def finish_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performed_actions.setter
    def performed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @progress.setter
    def progress(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_resource.setter
    def rollout_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetailArgsDict
                ]
            ]
        ]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetailArgs
                ]
            ]
        ]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetailArgsDict(
    TypedDict
):
    type_url: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetailArgs:
    def __init__(
        __self__,
        *,
        type_url: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_url.setter
    def type_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateArgsDict(
    TypedDict
):
    error: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorArgsDict
        ]
    ]
    failed_actions: NotRequired[pulumi.Input[_builtins.str]]
    finish_time: NotRequired[pulumi.Input[_builtins.str]]
    performed_actions: NotRequired[pulumi.Input[_builtins.str]]
    progress: NotRequired[pulumi.Input[_builtins.float]]
    rollout_resource: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateArgs:
    def __init__(
        __self__,
        *,
        error: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorArgs
            ]
        ] = ...,
        failed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        finish_time: Optional[pulumi.Input[_builtins.str]] = ...,
        performed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        progress: Optional[pulumi.Input[_builtins.float]] = ...,
        rollout_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorArgs
        ]
    ]: ...
    @error.setter
    def error(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failed_actions.setter
    def failed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @finish_time.setter
    def finish_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performed_actions.setter
    def performed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @progress.setter
    def progress(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_resource.setter
    def rollout_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetailArgsDict
                ]
            ]
        ]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetailArgs
                ]
            ]
        ]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetailArgsDict(
    TypedDict
):
    type_url: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetailArgs:
    def __init__(
        __self__,
        *,
        type_url: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_url.setter
    def type_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    os_policy_assignment_v1_payload: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        os_policy_assignment_v1_payload: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osPolicyAssignmentV1Payload")
    def os_policy_assignment_v1_payload(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
        ]
    ]: ...
    @os_policy_assignment_v1_payload.setter
    def os_policy_assignment_v1_payload(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadArgsDict(
    TypedDict
):
    instance_filter: pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgsDict
    ]
    os_policies: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgsDict
            ]
        ]
    ]
    rollout: pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgsDict
    ]
    baseline: NotRequired[pulumi.Input[_builtins.bool]]
    deleted: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    reconciling: NotRequired[pulumi.Input[_builtins.bool]]
    revision_create_time: NotRequired[pulumi.Input[_builtins.str]]
    revision_id: NotRequired[pulumi.Input[_builtins.str]]
    rollout_state: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadArgs:
    def __init__(
        __self__,
        *,
        instance_filter: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
        ],
        os_policies: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
                ]
            ]
        ],
        rollout: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
        ],
        baseline: Optional[pulumi.Input[_builtins.bool]] = ...,
        deleted: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision_create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout_state: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
    ]: ...
    @instance_filter.setter
    def instance_filter(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
            ]
        ]
    ]: ...
    @os_policies.setter
    def os_policies(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rollout(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
    ]: ...
    @rollout.setter
    def rollout(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @baseline.setter
    def baseline(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deleted.setter
    def deleted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_create_time.setter
    def revision_create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_id.setter
    def revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_state.setter
    def rollout_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgsDict(
    TypedDict
):
    all: NotRequired[pulumi.Input[_builtins.bool]]
    exclusion_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgsDict
                ]
            ]
        ]
    ]
    inclusion_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgsDict
                ]
            ]
        ]
    ]
    inventories: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterArgs:
    def __init__(
        __self__,
        *,
        all: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusion_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                    ]
                ]
            ]
        ] = ...,
        inclusion_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                    ]
                ]
            ]
        ] = ...,
        inventories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all.setter
    def all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionLabels")
    def exclusion_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                ]
            ]
        ]
    ]: ...
    @exclusion_labels.setter
    def exclusion_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionLabels")
    def inclusion_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                ]
            ]
        ]
    ]: ...
    @inclusion_labels.setter
    def inclusion_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inventories(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                ]
            ]
        ]
    ]: ...
    @inventories.setter
    def inventories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabelArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgsDict(
    TypedDict
):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabelArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgsDict(
    TypedDict
):
    os_short_name: pulumi.Input[_builtins.str]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventoryArgs:
    def __init__(
        __self__,
        *,
        os_short_name: pulumi.Input[_builtins.str],
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> pulumi.Input[_builtins.str]: ...
    @os_short_name.setter
    def os_short_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    mode: pulumi.Input[_builtins.str]
    resource_groups: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgsDict
            ]
        ]
    ]
    allow_no_resource_group_match: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        mode: pulumi.Input[_builtins.str],
        resource_groups: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
                ]
            ]
        ],
        allow_no_resource_group_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
            ]
        ]
    ]: ...
    @resource_groups.setter
    def resource_groups(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowNoResourceGroupMatch")
    def allow_no_resource_group_match(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_no_resource_group_match.setter
    def allow_no_resource_group_match(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgsDict(
    TypedDict
):
    resources: pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgsDict
            ]
        ]
    ]
    inventory_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupArgs:
    def __init__(
        __self__,
        *,
        resources: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
                ]
            ]
        ],
        inventory_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
            ]
        ]
    ]: ...
    @resources.setter
    def resources(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inventoryFilters")
    def inventory_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                ]
            ]
        ]
    ]: ...
    @inventory_filters.setter
    def inventory_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgsDict(
    TypedDict
):
    os_short_name: pulumi.Input[_builtins.str]
    os_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilterArgs:
    def __init__(
        __self__,
        *,
        os_short_name: pulumi.Input[_builtins.str],
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> pulumi.Input[_builtins.str]: ...
    @os_short_name.setter
    def os_short_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    exec_: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgsDict
        ]
    ]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgsDict
        ]
    ]
    pkg: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgsDict
        ]
    ]
    repository: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        exec_: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
            ]
        ] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
            ]
        ] = ...,
        pkg: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
            ]
        ] = ...,
        repository: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
        ]
    ]: ...
    @exec_.setter
    def exec_(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def pkg(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
        ]
    ]: ...
    @pkg.setter
    def pkg(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
        ]
    ]: ...
    @repository.setter
    def repository(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgsDict(
    TypedDict
):
    validate: pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgsDict
    ]
    enforce: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecArgs:
    def __init__(
        __self__,
        *,
        validate: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
        ],
        enforce: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
    ]: ...
    @validate.setter
    def validate(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enforce(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
        ]
    ]: ...
    @enforce.setter
    def enforce(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgsDict(
    TypedDict
):
    interpreter: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgsDict
        ]
    ]
    output_file_path: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceArgs:
    def __init__(
        __self__,
        *,
        interpreter: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
            ]
        ] = ...,
        output_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> pulumi.Input[_builtins.str]: ...
    @interpreter.setter
    def interpreter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_path.setter
    def output_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgsDict(
    TypedDict
):
    interpreter: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgsDict
        ]
    ]
    output_file_path: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateArgs:
    def __init__(
        __self__,
        *,
        interpreter: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
            ]
        ] = ...,
        output_file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> pulumi.Input[_builtins.str]: ...
    @interpreter.setter
    def interpreter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_path.setter
    def output_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgsDict(
    TypedDict
):
    path: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    content: NotRequired[pulumi.Input[_builtins.str]]
    file: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgsDict
        ]
    ]
    permissions: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        state: pulumi.Input[_builtins.str],
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        file: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
            ]
        ] = ...,
        permissions: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgsDict(
    TypedDict
):
    desired_state: pulumi.Input[_builtins.str]
    apt: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgsDict
        ]
    ]
    deb: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgsDict
        ]
    ]
    googet: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgsDict
        ]
    ]
    msi: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgsDict
        ]
    ]
    rpm: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgsDict
        ]
    ]
    yum: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgsDict
        ]
    ]
    zypper: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgArgs:
    def __init__(
        __self__,
        *,
        desired_state: pulumi.Input[_builtins.str],
        apt: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
            ]
        ] = ...,
        deb: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
            ]
        ] = ...,
        googet: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
            ]
        ] = ...,
        msi: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
            ]
        ] = ...,
        rpm: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
            ]
        ] = ...,
        yum: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
            ]
        ] = ...,
        zypper: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Input[_builtins.str]: ...
    @desired_state.setter
    def desired_state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
        ]
    ]: ...
    @apt.setter
    def apt(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def deb(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
        ]
    ]: ...
    @deb.setter
    def deb(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def googet(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
        ]
    ]: ...
    @googet.setter
    def googet(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def msi(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
        ]
    ]: ...
    @msi.setter
    def msi(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rpm(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
        ]
    ]: ...
    @rpm.setter
    def rpm(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
        ]
    ]: ...
    @yum.setter
    def yum(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
        ]
    ]: ...
    @zypper.setter
    def zypper(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgAptArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgsDict
    ]
    pull_deps: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
        ],
        pull_deps: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pull_deps.setter
    def pull_deps(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGoogetArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgsDict
    ]
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
        ],
        properties: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgsDict(
    TypedDict
):
    source: pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgsDict
    ]
    pull_deps: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
        ],
        pull_deps: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pull_deps.setter
    def pull_deps(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgsDict(
    TypedDict
):
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    gcs: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgsDict
        ]
    ]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    remote: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceArgs:
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcs: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
            ]
        ] = ...,
        local_path: Optional[pulumi.Input[_builtins.str]] = ...,
        remote: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
        ]
    ]: ...
    @gcs.setter
    def gcs(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
        ]
    ]: ...
    @remote.setter
    def remote(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    sha256_checksum: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemoteArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        sha256_checksum: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_checksum.setter
    def sha256_checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYumArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypperArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgsDict(
    TypedDict
):
    apt: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgsDict
        ]
    ]
    goo: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgsDict
        ]
    ]
    yum: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgsDict
        ]
    ]
    zypper: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryArgs:
    def __init__(
        __self__,
        *,
        apt: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
            ]
        ] = ...,
        goo: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
            ]
        ] = ...,
        yum: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
            ]
        ] = ...,
        zypper: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
        ]
    ]: ...
    @apt.setter
    def apt(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def goo(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
        ]
    ]: ...
    @goo.setter
    def goo(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
        ]
    ]: ...
    @yum.setter
    def yum(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
        ]
    ]: ...
    @zypper.setter
    def zypper(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgsDict(
    TypedDict
):
    archive_type: pulumi.Input[_builtins.str]
    components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    distribution: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    gpg_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryAptArgs:
    def __init__(
        __self__,
        *,
        archive_type: pulumi.Input[_builtins.str],
        components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        distribution: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        gpg_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> pulumi.Input[_builtins.str]: ...
    @archive_type.setter
    def archive_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @components.setter
    def components(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Input[_builtins.str]: ...
    @distribution.setter
    def distribution(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpg_key.setter
    def gpg_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGooArgs:
    def __init__(
        __self__, *, name: pulumi.Input[_builtins.str], url: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgsDict(
    TypedDict
):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYumArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgsDict(
    TypedDict
):
    base_url: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    gpg_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypperArgs:
    def __init__(
        __self__,
        *,
        base_url: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gpg_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[_builtins.str]: ...
    @base_url.setter
    def base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gpg_keys.setter
    def gpg_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgsDict(
    TypedDict
):
    disruption_budget: pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgsDict
    ]
    min_wait_duration: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutArgs:
    def __init__(
        __self__,
        *,
        disruption_budget: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
        ],
        min_wait_duration: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> pulumi.Input[
        V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
    ]: ...
    @disruption_budget.setter
    def disruption_budget(
        self,
        value: pulumi.Input[
            V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minWaitDuration")
    def min_wait_duration(self) -> pulumi.Input[_builtins.str]: ...
    @min_wait_duration.setter
    def min_wait_duration(self, value: pulumi.Input[_builtins.str]): ...

class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgsDict(
    TypedDict
):
    fixed: NotRequired[pulumi.Input[_builtins.int]]
    percent: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudgetArgs:
    def __init__(
        __self__,
        *,
        fixed: Optional[pulumi.Input[_builtins.int]] = ...,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fixed.setter
    def fixed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class V2PolicyOrchestratorOrchestrationScopeArgsDict(TypedDict):
    selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[V2PolicyOrchestratorOrchestrationScopeSelectorArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationScopeArgs:
    def __init__(
        __self__,
        *,
        selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[V2PolicyOrchestratorOrchestrationScopeSelectorArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[V2PolicyOrchestratorOrchestrationScopeSelectorArgs]]
        ]
    ]: ...
    @selectors.setter
    def selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[V2PolicyOrchestratorOrchestrationScopeSelectorArgs]
                ]
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestrationScopeSelectorArgsDict(TypedDict):
    location_selector: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelectorArgsDict
        ]
    ]
    resource_hierarchy_selector: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelectorArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationScopeSelectorArgs:
    def __init__(
        __self__,
        *,
        location_selector: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelectorArgs
            ]
        ] = ...,
        resource_hierarchy_selector: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelectorArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationSelector")
    def location_selector(
        self,
    ) -> Optional[
        pulumi.Input[V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelectorArgs]
    ]: ...
    @location_selector.setter
    def location_selector(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelectorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceHierarchySelector")
    def resource_hierarchy_selector(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelectorArgs
        ]
    ]: ...
    @resource_hierarchy_selector.setter
    def resource_hierarchy_selector(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelectorArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelectorArgsDict(TypedDict):
    included_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelectorArgs:
    def __init__(
        __self__,
        *,
        included_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedLocations")
    def included_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_locations.setter
    def included_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelectorArgsDict(
    TypedDict
):
    included_folders: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    included_projects: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelectorArgs:
    def __init__(
        __self__,
        *,
        included_folders: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        included_projects: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedFolders")
    def included_folders(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_folders.setter
    def included_folders(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedProjects")
    def included_projects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_projects.setter
    def included_projects(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class V2PolicyOrchestratorOrchestrationStateArgsDict(TypedDict):
    current_iteration_states: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestrationStateCurrentIterationStateArgsDict
                ]
            ]
        ]
    ]
    previous_iteration_state: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestrationStatePreviousIterationStateArgsDict
        ]
    ]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationStateArgs:
    def __init__(
        __self__,
        *,
        current_iteration_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestrationStateCurrentIterationStateArgs
                    ]
                ]
            ]
        ] = ...,
        previous_iteration_state: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationStatePreviousIterationStateArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationStates")
    def current_iteration_states(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestrationStateCurrentIterationStateArgs
                ]
            ]
        ]
    ]: ...
    @current_iteration_states.setter
    def current_iteration_states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestrationStateCurrentIterationStateArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="previousIterationState")
    def previous_iteration_state(
        self,
    ) -> Optional[
        pulumi.Input[V2PolicyOrchestratorOrchestrationStatePreviousIterationStateArgs]
    ]: ...
    @previous_iteration_state.setter
    def previous_iteration_state(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationStatePreviousIterationStateArgs
            ]
        ],
    ): ...

class V2PolicyOrchestratorOrchestrationStateCurrentIterationStateArgsDict(TypedDict):
    error: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorArgsDict
        ]
    ]
    failed_actions: NotRequired[pulumi.Input[_builtins.str]]
    finish_time: NotRequired[pulumi.Input[_builtins.str]]
    performed_actions: NotRequired[pulumi.Input[_builtins.str]]
    progress: NotRequired[pulumi.Input[_builtins.float]]
    rollout_resource: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationStateCurrentIterationStateArgs:
    def __init__(
        __self__,
        *,
        error: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorArgs
            ]
        ] = ...,
        failed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        finish_time: Optional[pulumi.Input[_builtins.str]] = ...,
        performed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        progress: Optional[pulumi.Input[_builtins.float]] = ...,
        rollout_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorArgs
        ]
    ]: ...
    @error.setter
    def error(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failed_actions.setter
    def failed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @finish_time.setter
    def finish_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performed_actions.setter
    def performed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @progress.setter
    def progress(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_resource.setter
    def rollout_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetailArgsDict
                ]
            ]
        ]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetailArgs
                ]
            ]
        ]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetailArgsDict(
    TypedDict
):
    type_url: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetailArgs:
    def __init__(
        __self__,
        *,
        type_url: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_url.setter
    def type_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestrationStatePreviousIterationStateArgsDict(TypedDict):
    error: NotRequired[
        pulumi.Input[
            V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorArgsDict
        ]
    ]
    failed_actions: NotRequired[pulumi.Input[_builtins.str]]
    finish_time: NotRequired[pulumi.Input[_builtins.str]]
    performed_actions: NotRequired[pulumi.Input[_builtins.str]]
    progress: NotRequired[pulumi.Input[_builtins.float]]
    rollout_resource: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationStatePreviousIterationStateArgs:
    def __init__(
        __self__,
        *,
        error: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorArgs
            ]
        ] = ...,
        failed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        finish_time: Optional[pulumi.Input[_builtins.str]] = ...,
        performed_actions: Optional[pulumi.Input[_builtins.str]] = ...,
        progress: Optional[pulumi.Input[_builtins.float]] = ...,
        rollout_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[
        pulumi.Input[
            V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorArgs
        ]
    ]: ...
    @error.setter
    def error(
        self,
        value: Optional[
            pulumi.Input[
                V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failed_actions.setter
    def failed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @finish_time.setter
    def finish_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performed_actions.setter
    def performed_actions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @progress.setter
    def progress(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_resource.setter
    def rollout_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetailArgsDict
                ]
            ]
        ]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetailArgs
                ]
            ]
        ]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetailArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetailArgsDict(
    TypedDict
):
    type_url: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetailArgs:
    def __init__(
        __self__,
        *,
        type_url: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_url.setter
    def type_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
