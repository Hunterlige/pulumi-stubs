import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GuestPoliciesAssignment",
    "GuestPoliciesAssignmentGroupLabel",
    "GuestPoliciesAssignmentOsType",
    "GuestPoliciesPackage",
    "GuestPoliciesPackageRepository",
    "GuestPoliciesPackageRepositoryApt",
    "GuestPoliciesPackageRepositoryGoo",
    "GuestPoliciesPackageRepositoryYum",
    "GuestPoliciesPackageRepositoryZypper",
    "GuestPoliciesRecipe",
    "GuestPoliciesRecipeArtifact",
    "GuestPoliciesRecipeArtifactGcs",
    "GuestPoliciesRecipeArtifactRemote",
    "GuestPoliciesRecipeInstallStep",
    "GuestPoliciesRecipeInstallStepArchiveExtraction",
    "GuestPoliciesRecipeInstallStepDpkgInstallation",
    "GuestPoliciesRecipeInstallStepFileCopy",
    "GuestPoliciesRecipeInstallStepFileExec",
    "GuestPoliciesRecipeInstallStepMsiInstallation",
    "GuestPoliciesRecipeInstallStepRpmInstallation",
    "GuestPoliciesRecipeInstallStepScriptRun",
    "GuestPoliciesRecipeUpdateStep",
    "GuestPoliciesRecipeUpdateStepArchiveExtraction",
    "GuestPoliciesRecipeUpdateStepDpkgInstallation",
    "GuestPoliciesRecipeUpdateStepFileCopy",
    "GuestPoliciesRecipeUpdateStepFileExec",
    "GuestPoliciesRecipeUpdateStepMsiInstallation",
    "GuestPoliciesRecipeUpdateStepRpmInstallation",
    "GuestPoliciesRecipeUpdateStepScriptRun",
    "OsPolicyAssignmentInstanceFilter",
    "OsPolicyAssignmentInstanceFilterExclusionLabel",
    "OsPolicyAssignmentInstanceFilterInclusionLabel",
    "OsPolicyAssignmentInstanceFilterInventory",
    "OsPolicyAssignmentOsPolicy",
    "OsPolicyAssignmentOsPolicyResourceGroup",
    ...,
    "OsPolicyAssignmentOsPolicyResourceGroupResource",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "OsPolicyAssignmentOsPolicyResourceGroupResourcePkg",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "OsPolicyAssignmentRollout",
    "OsPolicyAssignmentRolloutDisruptionBudget",
    "PatchDeploymentInstanceFilter",
    "PatchDeploymentInstanceFilterGroupLabel",
    "PatchDeploymentOneTimeSchedule",
    "PatchDeploymentPatchConfig",
    "PatchDeploymentPatchConfigApt",
    "PatchDeploymentPatchConfigGoo",
    "PatchDeploymentPatchConfigPostStep",
    ...,
    ...,
    ...,
    ...,
    "PatchDeploymentPatchConfigPreStep",
    ...,
    ...,
    ...,
    ...,
    "PatchDeploymentPatchConfigWindowsUpdate",
    "PatchDeploymentPatchConfigYum",
    "PatchDeploymentPatchConfigZypper",
    "PatchDeploymentRecurringSchedule",
    "PatchDeploymentRecurringScheduleMonthly",
    ...,
    "PatchDeploymentRecurringScheduleTimeOfDay",
    "PatchDeploymentRecurringScheduleTimeZone",
    "PatchDeploymentRecurringScheduleWeekly",
    "PatchDeploymentRollout",
    "PatchDeploymentRolloutDisruptionBudget",
    "V2PolicyOrchestratorForFolderOrchestratedResource",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "V2PolicyOrchestratorForFolderOrchestrationScope",
    ...,
    ...,
    ...,
    "V2PolicyOrchestratorForFolderOrchestrationState",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "V2PolicyOrchestratorOrchestratedResource",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "V2PolicyOrchestratorOrchestrationScope",
    "V2PolicyOrchestratorOrchestrationScopeSelector",
    ...,
    ...,
    "V2PolicyOrchestratorOrchestrationState",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

@pulumi.output_type
class GuestPoliciesAssignment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_labels: Optional[
            Sequence[outputs.GuestPoliciesAssignmentGroupLabel]
        ] = ...,
        instance_name_prefixes: Optional[Sequence[_builtins.str]] = ...,
        instances: Optional[Sequence[_builtins.str]] = ...,
        os_types: Optional[Sequence[outputs.GuestPoliciesAssignmentOsType]] = ...,
        zones: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupLabels")
    def group_labels(
        self,
    ) -> Optional[Sequence[outputs.GuestPoliciesAssignmentGroupLabel]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceNamePrefixes")
    def instance_name_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osTypes")
    def os_types(self) -> Optional[Sequence[outputs.GuestPoliciesAssignmentOsType]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GuestPoliciesAssignmentGroupLabel(dict):
    def __init__(__self__, *, labels: Mapping[str, _builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GuestPoliciesAssignmentOsType(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_architecture: Optional[_builtins.str] = ...,
        os_short_name: Optional[_builtins.str] = ...,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osArchitecture")
    def os_architecture(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesPackage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        desired_state: Optional[_builtins.str] = ...,
        manager: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def manager(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesPackageRepository(dict):
    def __init__(
        __self__,
        *,
        apt: Optional[outputs.GuestPoliciesPackageRepositoryApt] = ...,
        goo: Optional[outputs.GuestPoliciesPackageRepositoryGoo] = ...,
        yum: Optional[outputs.GuestPoliciesPackageRepositoryYum] = ...,
        zypper: Optional[outputs.GuestPoliciesPackageRepositoryZypper] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(self) -> Optional[outputs.GuestPoliciesPackageRepositoryApt]: ...
    @_builtins.property
    @pulumi.getter
    def goo(self) -> Optional[outputs.GuestPoliciesPackageRepositoryGoo]: ...
    @_builtins.property
    @pulumi.getter
    def yum(self) -> Optional[outputs.GuestPoliciesPackageRepositoryYum]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(self) -> Optional[outputs.GuestPoliciesPackageRepositoryZypper]: ...

@pulumi.output_type
class GuestPoliciesPackageRepositoryApt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        components: Sequence[_builtins.str],
        distribution: _builtins.str,
        uri: _builtins.str,
        archive_type: Optional[_builtins.str] = ...,
        gpg_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesPackageRepositoryGoo(dict):
    def __init__(__self__, *, name: _builtins.str, url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

@pulumi.output_type
class GuestPoliciesPackageRepositoryYum(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GuestPoliciesPackageRepositoryZypper(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GuestPoliciesRecipe(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        artifacts: Optional[Sequence[outputs.GuestPoliciesRecipeArtifact]] = ...,
        desired_state: Optional[_builtins.str] = ...,
        install_steps: Optional[Sequence[outputs.GuestPoliciesRecipeInstallStep]] = ...,
        update_steps: Optional[Sequence[outputs.GuestPoliciesRecipeUpdateStep]] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> Optional[Sequence[outputs.GuestPoliciesRecipeArtifact]]: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="installSteps")
    def install_steps(
        self,
    ) -> Optional[Sequence[outputs.GuestPoliciesRecipeInstallStep]]: ...
    @_builtins.property
    @pulumi.getter(name="updateSteps")
    def update_steps(
        self,
    ) -> Optional[Sequence[outputs.GuestPoliciesRecipeUpdateStep]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeArtifact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[outputs.GuestPoliciesRecipeArtifactGcs] = ...,
        remote: Optional[outputs.GuestPoliciesRecipeArtifactRemote] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Optional[outputs.GuestPoliciesRecipeArtifactGcs]: ...
    @_builtins.property
    @pulumi.getter
    def remote(self) -> Optional[outputs.GuestPoliciesRecipeArtifactRemote]: ...

@pulumi.output_type
class GuestPoliciesRecipeArtifactGcs(dict):
    def __init__(
        __self__,
        *,
        bucket: Optional[_builtins.str] = ...,
        generation: Optional[_builtins.int] = ...,
        object: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeArtifactRemote(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        check_sum: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkSum")
    def check_sum(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeInstallStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_extraction: Optional[
            outputs.GuestPoliciesRecipeInstallStepArchiveExtraction
        ] = ...,
        dpkg_installation: Optional[
            outputs.GuestPoliciesRecipeInstallStepDpkgInstallation
        ] = ...,
        file_copy: Optional[outputs.GuestPoliciesRecipeInstallStepFileCopy] = ...,
        file_exec: Optional[outputs.GuestPoliciesRecipeInstallStepFileExec] = ...,
        msi_installation: Optional[
            outputs.GuestPoliciesRecipeInstallStepMsiInstallation
        ] = ...,
        rpm_installation: Optional[
            outputs.GuestPoliciesRecipeInstallStepRpmInstallation
        ] = ...,
        script_run: Optional[outputs.GuestPoliciesRecipeInstallStepScriptRun] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveExtraction")
    def archive_extraction(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeInstallStepArchiveExtraction]: ...
    @_builtins.property
    @pulumi.getter(name="dpkgInstallation")
    def dpkg_installation(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeInstallStepDpkgInstallation]: ...
    @_builtins.property
    @pulumi.getter(name="fileCopy")
    def file_copy(self) -> Optional[outputs.GuestPoliciesRecipeInstallStepFileCopy]: ...
    @_builtins.property
    @pulumi.getter(name="fileExec")
    def file_exec(self) -> Optional[outputs.GuestPoliciesRecipeInstallStepFileExec]: ...
    @_builtins.property
    @pulumi.getter(name="msiInstallation")
    def msi_installation(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeInstallStepMsiInstallation]: ...
    @_builtins.property
    @pulumi.getter(name="rpmInstallation")
    def rpm_installation(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeInstallStepRpmInstallation]: ...
    @_builtins.property
    @pulumi.getter(name="scriptRun")
    def script_run(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeInstallStepScriptRun]: ...

@pulumi.output_type
class GuestPoliciesRecipeInstallStepArchiveExtraction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_id: _builtins.str,
        type: _builtins.str,
        destination: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeInstallStepDpkgInstallation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, artifact_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...

@pulumi.output_type
class GuestPoliciesRecipeInstallStepFileCopy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_id: _builtins.str,
        destination: _builtins.str,
        overwrite: Optional[_builtins.bool] = ...,
        permissions: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def overwrite(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeInstallStepFileExec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_exit_codes: Optional[_builtins.str] = ...,
        args: Optional[Sequence[_builtins.str]] = ...,
        artifact_id: Optional[_builtins.str] = ...,
        local_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeInstallStepMsiInstallation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_id: _builtins.str,
        allowed_exit_codes: Optional[Sequence[_builtins.int]] = ...,
        flags: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GuestPoliciesRecipeInstallStepRpmInstallation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, artifact_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...

@pulumi.output_type
class GuestPoliciesRecipeInstallStepScriptRun(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        script: _builtins.str,
        allowed_exit_codes: Optional[Sequence[_builtins.int]] = ...,
        interpreter: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeUpdateStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_extraction: Optional[
            outputs.GuestPoliciesRecipeUpdateStepArchiveExtraction
        ] = ...,
        dpkg_installation: Optional[
            outputs.GuestPoliciesRecipeUpdateStepDpkgInstallation
        ] = ...,
        file_copy: Optional[outputs.GuestPoliciesRecipeUpdateStepFileCopy] = ...,
        file_exec: Optional[outputs.GuestPoliciesRecipeUpdateStepFileExec] = ...,
        msi_installation: Optional[
            outputs.GuestPoliciesRecipeUpdateStepMsiInstallation
        ] = ...,
        rpm_installation: Optional[
            outputs.GuestPoliciesRecipeUpdateStepRpmInstallation
        ] = ...,
        script_run: Optional[outputs.GuestPoliciesRecipeUpdateStepScriptRun] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveExtraction")
    def archive_extraction(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeUpdateStepArchiveExtraction]: ...
    @_builtins.property
    @pulumi.getter(name="dpkgInstallation")
    def dpkg_installation(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeUpdateStepDpkgInstallation]: ...
    @_builtins.property
    @pulumi.getter(name="fileCopy")
    def file_copy(self) -> Optional[outputs.GuestPoliciesRecipeUpdateStepFileCopy]: ...
    @_builtins.property
    @pulumi.getter(name="fileExec")
    def file_exec(self) -> Optional[outputs.GuestPoliciesRecipeUpdateStepFileExec]: ...
    @_builtins.property
    @pulumi.getter(name="msiInstallation")
    def msi_installation(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeUpdateStepMsiInstallation]: ...
    @_builtins.property
    @pulumi.getter(name="rpmInstallation")
    def rpm_installation(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeUpdateStepRpmInstallation]: ...
    @_builtins.property
    @pulumi.getter(name="scriptRun")
    def script_run(
        self,
    ) -> Optional[outputs.GuestPoliciesRecipeUpdateStepScriptRun]: ...

@pulumi.output_type
class GuestPoliciesRecipeUpdateStepArchiveExtraction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_id: _builtins.str,
        type: _builtins.str,
        destination: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeUpdateStepDpkgInstallation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, artifact_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...

@pulumi.output_type
class GuestPoliciesRecipeUpdateStepFileCopy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_id: _builtins.str,
        destination: _builtins.str,
        overwrite: Optional[_builtins.bool] = ...,
        permissions: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def overwrite(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeUpdateStepFileExec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_exit_codes: Optional[Sequence[_builtins.int]] = ...,
        args: Optional[Sequence[_builtins.str]] = ...,
        artifact_id: Optional[_builtins.str] = ...,
        local_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestPoliciesRecipeUpdateStepMsiInstallation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_id: _builtins.str,
        allowed_exit_codes: Optional[Sequence[_builtins.int]] = ...,
        flags: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GuestPoliciesRecipeUpdateStepRpmInstallation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, artifact_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str: ...

@pulumi.output_type
class GuestPoliciesRecipeUpdateStepScriptRun(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        script: _builtins.str,
        allowed_exit_codes: Optional[Sequence[_builtins.int]] = ...,
        interpreter: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedExitCodes")
    def allowed_exit_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentInstanceFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        all: Optional[_builtins.bool] = ...,
        exclusion_labels: Optional[
            Sequence[outputs.OsPolicyAssignmentInstanceFilterExclusionLabel]
        ] = ...,
        inclusion_labels: Optional[
            Sequence[outputs.OsPolicyAssignmentInstanceFilterInclusionLabel]
        ] = ...,
        inventories: Optional[
            Sequence[outputs.OsPolicyAssignmentInstanceFilterInventory]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exclusionLabels")
    def exclusion_labels(
        self,
    ) -> Optional[Sequence[outputs.OsPolicyAssignmentInstanceFilterExclusionLabel]]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionLabels")
    def inclusion_labels(
        self,
    ) -> Optional[Sequence[outputs.OsPolicyAssignmentInstanceFilterInclusionLabel]]: ...
    @_builtins.property
    @pulumi.getter
    def inventories(
        self,
    ) -> Optional[Sequence[outputs.OsPolicyAssignmentInstanceFilterInventory]]: ...

@pulumi.output_type
class OsPolicyAssignmentInstanceFilterExclusionLabel(dict):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class OsPolicyAssignmentInstanceFilterInclusionLabel(dict):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class OsPolicyAssignmentInstanceFilterInventory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_short_name: _builtins.str,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        mode: _builtins.str,
        resource_groups: Sequence[outputs.OsPolicyAssignmentOsPolicyResourceGroup],
        allow_no_resource_group_match: Optional[_builtins.bool] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> Sequence[outputs.OsPolicyAssignmentOsPolicyResourceGroup]: ...
    @_builtins.property
    @pulumi.getter(name="allowNoResourceGroupMatch")
    def allow_no_resource_group_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resources: Sequence[outputs.OsPolicyAssignmentOsPolicyResourceGroupResource],
        inventory_filters: Optional[
            Sequence[outputs.OsPolicyAssignmentOsPolicyResourceGroupInventoryFilter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Sequence[outputs.OsPolicyAssignmentOsPolicyResourceGroupResource]: ...
    @_builtins.property
    @pulumi.getter(name="inventoryFilters")
    def inventory_filters(
        self,
    ) -> Optional[
        Sequence[outputs.OsPolicyAssignmentOsPolicyResourceGroupInventoryFilter]
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupInventoryFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_short_name: _builtins.str,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        exec_: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExec
        ] = ...,
        file: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceFile
        ] = ...,
        pkg: Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkg] = ...,
        repository: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepository
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExec]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceFile]: ...
    @_builtins.property
    @pulumi.getter
    def pkg(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkg]: ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepository
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExec(dict):
    def __init__(
        __self__,
        *,
        validate: outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidate,
        enforce: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforce
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidate: ...
    @_builtins.property
    @pulumi.getter
    def enforce(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforce
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforce(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interpreter: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        file: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFile
        ] = ...,
        output_file_path: Optional[_builtins.str] = ...,
        script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFile
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemote
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileGcs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecEnforceFileRemote(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interpreter: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        file: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFile
        ] = ...,
        output_file_path: Optional[_builtins.str] = ...,
        script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFile
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemote
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileGcs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceExecValidateFileRemote(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceFile(dict):
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        state: _builtins.str,
        content: Optional[_builtins.str] = ...,
        file: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceFileFile
        ] = ...,
        permissions: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceFileFile]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemote
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileGcs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceFileFileRemote(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkg(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        desired_state: _builtins.str,
        apt: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgApt
        ] = ...,
        deb: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDeb
        ] = ...,
        googet: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGooget
        ] = ...,
        msi: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsi
        ] = ...,
        rpm: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpm
        ] = ...,
        yum: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYum
        ] = ...,
        zypper: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypper
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgApt]: ...
    @_builtins.property
    @pulumi.getter
    def deb(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDeb]: ...
    @_builtins.property
    @pulumi.getter
    def googet(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGooget]: ...
    @_builtins.property
    @pulumi.getter
    def msi(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsi]: ...
    @_builtins.property
    @pulumi.getter
    def rpm(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpm]: ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYum]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypper]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgApt(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDeb(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSource,
        pull_deps: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSource: ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemote
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceGcs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgDebSourceRemote(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgGooget(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsi(dict):
    def __init__(
        __self__,
        *,
        source: outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSource,
        properties: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSource: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemote
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceGcs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgMsiSourceRemote(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSource,
        pull_deps: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSource: ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemote
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceGcs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgRpmSourceRemote(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgYum(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourcePkgZypper(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepository(dict):
    def __init__(
        __self__,
        *,
        apt: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryApt
        ] = ...,
        goo: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGoo
        ] = ...,
        yum: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYum
        ] = ...,
        zypper: Optional[
            outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypper
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryApt
    ]: ...
    @_builtins.property
    @pulumi.getter
    def goo(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGoo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYum
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        outputs.OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypper
    ]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryApt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_type: _builtins.str,
        components: Sequence[_builtins.str],
        distribution: _builtins.str,
        uri: _builtins.str,
        gpg_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryGoo(dict):
    def __init__(__self__, *, name: _builtins.str, url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryYum(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OsPolicyAssignmentOsPolicyResourceGroupResourceRepositoryZypper(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OsPolicyAssignmentRollout(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disruption_budget: outputs.OsPolicyAssignmentRolloutDisruptionBudget,
        min_wait_duration: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> outputs.OsPolicyAssignmentRolloutDisruptionBudget: ...
    @_builtins.property
    @pulumi.getter(name="minWaitDuration")
    def min_wait_duration(self) -> _builtins.str: ...

@pulumi.output_type
class OsPolicyAssignmentRolloutDisruptionBudget(dict):
    def __init__(
        __self__,
        *,
        fixed: Optional[_builtins.int] = ...,
        percent: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PatchDeploymentInstanceFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        all: Optional[_builtins.bool] = ...,
        group_labels: Optional[
            Sequence[outputs.PatchDeploymentInstanceFilterGroupLabel]
        ] = ...,
        instance_name_prefixes: Optional[Sequence[_builtins.str]] = ...,
        instances: Optional[Sequence[_builtins.str]] = ...,
        zones: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="groupLabels")
    def group_labels(
        self,
    ) -> Optional[Sequence[outputs.PatchDeploymentInstanceFilterGroupLabel]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceNamePrefixes")
    def instance_name_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PatchDeploymentInstanceFilterGroupLabel(dict):
    def __init__(__self__, *, labels: Mapping[str, _builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class PatchDeploymentOneTimeSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, execute_time: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executeTime")
    def execute_time(self) -> _builtins.str: ...

@pulumi.output_type
class PatchDeploymentPatchConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apt: Optional[outputs.PatchDeploymentPatchConfigApt] = ...,
        goo: Optional[outputs.PatchDeploymentPatchConfigGoo] = ...,
        mig_instances_allowed: Optional[_builtins.bool] = ...,
        post_step: Optional[outputs.PatchDeploymentPatchConfigPostStep] = ...,
        pre_step: Optional[outputs.PatchDeploymentPatchConfigPreStep] = ...,
        reboot_config: Optional[_builtins.str] = ...,
        skip_unpatchable_vms: Optional[_builtins.bool] = ...,
        windows_update: Optional[outputs.PatchDeploymentPatchConfigWindowsUpdate] = ...,
        yum: Optional[outputs.PatchDeploymentPatchConfigYum] = ...,
        zypper: Optional[outputs.PatchDeploymentPatchConfigZypper] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(self) -> Optional[outputs.PatchDeploymentPatchConfigApt]: ...
    @_builtins.property
    @pulumi.getter
    def goo(self) -> Optional[outputs.PatchDeploymentPatchConfigGoo]: ...
    @_builtins.property
    @pulumi.getter(name="migInstancesAllowed")
    def mig_instances_allowed(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="postStep")
    def post_step(self) -> Optional[outputs.PatchDeploymentPatchConfigPostStep]: ...
    @_builtins.property
    @pulumi.getter(name="preStep")
    def pre_step(self) -> Optional[outputs.PatchDeploymentPatchConfigPreStep]: ...
    @_builtins.property
    @pulumi.getter(name="rebootConfig")
    def reboot_config(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipUnpatchableVms")
    def skip_unpatchable_vms(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="windowsUpdate")
    def windows_update(
        self,
    ) -> Optional[outputs.PatchDeploymentPatchConfigWindowsUpdate]: ...
    @_builtins.property
    @pulumi.getter
    def yum(self) -> Optional[outputs.PatchDeploymentPatchConfigYum]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(self) -> Optional[outputs.PatchDeploymentPatchConfigZypper]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigApt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        exclusive_packages: Optional[Sequence[_builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exclusivePackages")
    def exclusive_packages(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigGoo(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPostStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linux_exec_step_config: Optional[
            outputs.PatchDeploymentPatchConfigPostStepLinuxExecStepConfig
        ] = ...,
        windows_exec_step_config: Optional[
            outputs.PatchDeploymentPatchConfigPostStepWindowsExecStepConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxExecStepConfig")
    def linux_exec_step_config(
        self,
    ) -> Optional[outputs.PatchDeploymentPatchConfigPostStepLinuxExecStepConfig]: ...
    @_builtins.property
    @pulumi.getter(name="windowsExecStepConfig")
    def windows_exec_step_config(
        self,
    ) -> Optional[outputs.PatchDeploymentPatchConfigPostStepWindowsExecStepConfig]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPostStepLinuxExecStepConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_success_codes: Optional[Sequence[_builtins.int]] = ...,
        gcs_object: Optional[
            outputs.PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject
        ] = ...,
        interpreter: Optional[_builtins.str] = ...,
        local_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSuccessCodes")
    def allowed_success_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="gcsObject")
    def gcs_object(
        self,
    ) -> Optional[
        outputs.PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject
    ]: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPostStepLinuxExecStepConfigGcsObject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        generation_number: _builtins.str,
        object: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="generationNumber")
    def generation_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPostStepWindowsExecStepConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_success_codes: Optional[Sequence[_builtins.int]] = ...,
        gcs_object: Optional[
            outputs.PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject
        ] = ...,
        interpreter: Optional[_builtins.str] = ...,
        local_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSuccessCodes")
    def allowed_success_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="gcsObject")
    def gcs_object(
        self,
    ) -> Optional[
        outputs.PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject
    ]: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPostStepWindowsExecStepConfigGcsObject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        generation_number: _builtins.str,
        object: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="generationNumber")
    def generation_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPreStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linux_exec_step_config: Optional[
            outputs.PatchDeploymentPatchConfigPreStepLinuxExecStepConfig
        ] = ...,
        windows_exec_step_config: Optional[
            outputs.PatchDeploymentPatchConfigPreStepWindowsExecStepConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxExecStepConfig")
    def linux_exec_step_config(
        self,
    ) -> Optional[outputs.PatchDeploymentPatchConfigPreStepLinuxExecStepConfig]: ...
    @_builtins.property
    @pulumi.getter(name="windowsExecStepConfig")
    def windows_exec_step_config(
        self,
    ) -> Optional[outputs.PatchDeploymentPatchConfigPreStepWindowsExecStepConfig]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPreStepLinuxExecStepConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_success_codes: Optional[Sequence[_builtins.int]] = ...,
        gcs_object: Optional[
            outputs.PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject
        ] = ...,
        interpreter: Optional[_builtins.str] = ...,
        local_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSuccessCodes")
    def allowed_success_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="gcsObject")
    def gcs_object(
        self,
    ) -> Optional[
        outputs.PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject
    ]: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPreStepLinuxExecStepConfigGcsObject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        generation_number: _builtins.str,
        object: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="generationNumber")
    def generation_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPreStepWindowsExecStepConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_success_codes: Optional[Sequence[_builtins.int]] = ...,
        gcs_object: Optional[
            outputs.PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject
        ] = ...,
        interpreter: Optional[_builtins.str] = ...,
        local_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSuccessCodes")
    def allowed_success_codes(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="gcsObject")
    def gcs_object(
        self,
    ) -> Optional[
        outputs.PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject
    ]: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigPreStepWindowsExecStepConfigGcsObject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        generation_number: _builtins.str,
        object: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="generationNumber")
    def generation_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class PatchDeploymentPatchConfigWindowsUpdate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        classifications: Optional[Sequence[_builtins.str]] = ...,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        exclusive_patches: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classifications(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exclusivePatches")
    def exclusive_patches(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigYum(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        exclusive_packages: Optional[Sequence[_builtins.str]] = ...,
        minimal: Optional[_builtins.bool] = ...,
        security: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exclusivePackages")
    def exclusive_packages(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def minimal(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def security(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PatchDeploymentPatchConfigZypper(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        categories: Optional[Sequence[_builtins.str]] = ...,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        exclusive_patches: Optional[Sequence[_builtins.str]] = ...,
        severities: Optional[Sequence[_builtins.str]] = ...,
        with_optional: Optional[_builtins.bool] = ...,
        with_update: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exclusivePatches")
    def exclusive_patches(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def severities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="withOptional")
    def with_optional(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="withUpdate")
    def with_update(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PatchDeploymentRecurringSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        time_of_day: outputs.PatchDeploymentRecurringScheduleTimeOfDay,
        time_zone: outputs.PatchDeploymentRecurringScheduleTimeZone,
        end_time: Optional[_builtins.str] = ...,
        last_execute_time: Optional[_builtins.str] = ...,
        monthly: Optional[outputs.PatchDeploymentRecurringScheduleMonthly] = ...,
        next_execute_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        weekly: Optional[outputs.PatchDeploymentRecurringScheduleWeekly] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeOfDay")
    def time_of_day(self) -> outputs.PatchDeploymentRecurringScheduleTimeOfDay: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> outputs.PatchDeploymentRecurringScheduleTimeZone: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastExecuteTime")
    def last_execute_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def monthly(self) -> Optional[outputs.PatchDeploymentRecurringScheduleMonthly]: ...
    @_builtins.property
    @pulumi.getter(name="nextExecuteTime")
    def next_execute_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weekly(self) -> Optional[outputs.PatchDeploymentRecurringScheduleWeekly]: ...

@pulumi.output_type
class PatchDeploymentRecurringScheduleMonthly(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        month_day: Optional[_builtins.int] = ...,
        week_day_of_month: Optional[
            outputs.PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monthDay")
    def month_day(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="weekDayOfMonth")
    def week_day_of_month(
        self,
    ) -> Optional[outputs.PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth]: ...

@pulumi.output_type
class PatchDeploymentRecurringScheduleMonthlyWeekDayOfMonth(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day_of_week: _builtins.str,
        week_ordinal: _builtins.int,
        day_offset: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weekOrdinal")
    def week_ordinal(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dayOffset")
    def day_offset(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PatchDeploymentRecurringScheduleTimeOfDay(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PatchDeploymentRecurringScheduleTimeZone(dict):
    def __init__(
        __self__, *, id: _builtins.str, version: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PatchDeploymentRecurringScheduleWeekly(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, day_of_week: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str: ...

@pulumi.output_type
class PatchDeploymentRollout(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disruption_budget: outputs.PatchDeploymentRolloutDisruptionBudget,
        mode: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(self) -> outputs.PatchDeploymentRolloutDisruptionBudget: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class PatchDeploymentRolloutDisruptionBudget(dict):
    def __init__(
        __self__,
        *,
        fixed: Optional[_builtins.int] = ...,
        percentage: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        os_policy_assignment_v1_payload: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1Payload
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osPolicyAssignmentV1Payload")
    def os_policy_assignment_v1_payload(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1Payload
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1Payload(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_filter: outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter,
        os_policies: Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy
        ],
        rollout: outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRollout,
        baseline: Optional[_builtins.bool] = ...,
        deleted: Optional[_builtins.bool] = ...,
        description: Optional[_builtins.str] = ...,
        etag: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        reconciling: Optional[_builtins.bool] = ...,
        revision_create_time: Optional[_builtins.str] = ...,
        revision_id: Optional[_builtins.str] = ...,
        rollout_state: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter: ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def rollout(
        self,
    ) -> outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRollout: ...
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        all: Optional[_builtins.bool] = ...,
        exclusion_labels: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel
            ]
        ] = ...,
        inclusion_labels: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel
            ]
        ] = ...,
        inventories: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exclusionLabels")
    def exclusion_labels(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionLabels")
    def inclusion_labels(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def inventories(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory
        ]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel(
    dict
):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel(
    dict
):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_short_name: _builtins.str,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        mode: _builtins.str,
        resource_groups: Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup
        ],
        allow_no_resource_group_match: Optional[_builtins.bool] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup
    ]: ...
    @_builtins.property
    @pulumi.getter(name="allowNoResourceGroupMatch")
    def allow_no_resource_group_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resources: Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource
        ],
        inventory_filters: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inventoryFilters")
    def inventory_filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter
        ]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_short_name: _builtins.str,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        exec_: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec
        ] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile
        ] = ...,
        pkg: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg
        ] = ...,
        repository: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec
    ]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def pkg(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg
    ]: ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec(
    dict
):
    def __init__(
        __self__,
        *,
        validate: outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate,
        enforce: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate: ...
    @_builtins.property
    @pulumi.getter
    def enforce(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interpreter: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile
        ] = ...,
        output_file_path: Optional[_builtins.str] = ...,
        script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interpreter: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile
        ] = ...,
        output_file_path: Optional[_builtins.str] = ...,
        script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile(
    dict
):
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        state: _builtins.str,
        content: Optional[_builtins.str] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile
        ] = ...,
        permissions: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        desired_state: _builtins.str,
        apt: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt
        ] = ...,
        deb: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb
        ] = ...,
        googet: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget
        ] = ...,
        msi: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi
        ] = ...,
        rpm: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm
        ] = ...,
        yum: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum
        ] = ...,
        zypper: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt
    ]: ...
    @_builtins.property
    @pulumi.getter
    def deb(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb
    ]: ...
    @_builtins.property
    @pulumi.getter
    def googet(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget
    ]: ...
    @_builtins.property
    @pulumi.getter
    def msi(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi
    ]: ...
    @_builtins.property
    @pulumi.getter
    def rpm(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm
    ]: ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource,
        pull_deps: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource: ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi(
    dict
):
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource,
        properties: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource,
        pull_deps: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource: ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository(
    dict
):
    def __init__(
        __self__,
        *,
        apt: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt
        ] = ...,
        goo: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo
        ] = ...,
        yum: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum
        ] = ...,
        zypper: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt
    ]: ...
    @_builtins.property
    @pulumi.getter
    def goo(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_type: _builtins.str,
        components: Sequence[_builtins.str],
        distribution: _builtins.str,
        uri: _builtins.str,
        gpg_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo(
    dict
):
    def __init__(__self__, *, name: _builtins.str, url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRollout(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disruption_budget: outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget,
        min_wait_duration: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> outputs.V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget: ...
    @_builtins.property
    @pulumi.getter(name="minWaitDuration")
    def min_wait_duration(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget(
    dict
):
    def __init__(
        __self__,
        *,
        fixed: Optional[_builtins.int] = ...,
        percent: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationScope(dict):
    def __init__(
        __self__,
        *,
        selectors: Optional[
            Sequence[outputs.V2PolicyOrchestratorForFolderOrchestrationScopeSelector]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> Optional[
        Sequence[outputs.V2PolicyOrchestratorForFolderOrchestrationScopeSelector]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationScopeSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location_selector: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelector
        ] = ...,
        resource_hierarchy_selector: Optional[
            outputs.V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelector
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationSelector")
    def location_selector(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelector
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceHierarchySelector")
    def resource_hierarchy_selector(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelector
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationScopeSelectorLocationSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, included_locations: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedLocations")
    def included_locations(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationScopeSelectorResourceHierarchySelector(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        included_folders: Optional[Sequence[_builtins.str]] = ...,
        included_projects: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedFolders")
    def included_folders(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includedProjects")
    def included_projects(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_iteration_states: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationState
            ]
        ] = ...,
        previous_iteration_states: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationState
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationStates")
    def current_iteration_states(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationState
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="previousIterationStates")
    def previous_iteration_states(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationState
        ]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        errors: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateError
            ]
        ] = ...,
        failed_actions: Optional[_builtins.str] = ...,
        finish_time: Optional[_builtins.str] = ...,
        performed_actions: Optional[_builtins.str] = ...,
        progress: Optional[_builtins.float] = ...,
        rollout_resource: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateError
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetail
            ]
        ] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetail
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationStateCurrentIterationStateErrorDetail(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type_url: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        errors: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateError
            ]
        ] = ...,
        failed_actions: Optional[_builtins.str] = ...,
        finish_time: Optional[_builtins.str] = ...,
        performed_actions: Optional[_builtins.str] = ...,
        progress: Optional[_builtins.float] = ...,
        rollout_resource: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateError
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetail
            ]
        ] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetail
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForFolderOrchestrationStatePreviousIterationStateErrorDetail(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type_url: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        os_policy_assignment_v1_payload: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1Payload
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osPolicyAssignmentV1Payload")
    def os_policy_assignment_v1_payload(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1Payload
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1Payload(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_filter: outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter,
        os_policies: Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy
        ],
        rollout: outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRollout,
        baseline: Optional[_builtins.bool] = ...,
        deleted: Optional[_builtins.bool] = ...,
        description: Optional[_builtins.str] = ...,
        etag: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        reconciling: Optional[_builtins.bool] = ...,
        revision_create_time: Optional[_builtins.str] = ...,
        revision_id: Optional[_builtins.str] = ...,
        rollout_state: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter: ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def rollout(
        self,
    ) -> outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRollout: ...
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        all: Optional[_builtins.bool] = ...,
        exclusion_labels: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel
            ]
        ] = ...,
        inclusion_labels: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel
            ]
        ] = ...,
        inventories: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exclusionLabels")
    def exclusion_labels(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionLabels")
    def inclusion_labels(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def inventories(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory
        ]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel(
    dict
):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel(
    dict
):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_short_name: _builtins.str,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        mode: _builtins.str,
        resource_groups: Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup
        ],
        allow_no_resource_group_match: Optional[_builtins.bool] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup
    ]: ...
    @_builtins.property
    @pulumi.getter(name="allowNoResourceGroupMatch")
    def allow_no_resource_group_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resources: Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource
        ],
        inventory_filters: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inventoryFilters")
    def inventory_filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter
        ]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_short_name: _builtins.str,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        exec_: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec
        ] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile
        ] = ...,
        pkg: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg
        ] = ...,
        repository: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec
    ]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def pkg(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg
    ]: ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec(
    dict
):
    def __init__(
        __self__,
        *,
        validate: outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate,
        enforce: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate: ...
    @_builtins.property
    @pulumi.getter
    def enforce(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interpreter: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile
        ] = ...,
        output_file_path: Optional[_builtins.str] = ...,
        script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interpreter: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile
        ] = ...,
        output_file_path: Optional[_builtins.str] = ...,
        script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile(
    dict
):
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        state: _builtins.str,
        content: Optional[_builtins.str] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile
        ] = ...,
        permissions: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        desired_state: _builtins.str,
        apt: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt
        ] = ...,
        deb: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb
        ] = ...,
        googet: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget
        ] = ...,
        msi: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi
        ] = ...,
        rpm: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm
        ] = ...,
        yum: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum
        ] = ...,
        zypper: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt
    ]: ...
    @_builtins.property
    @pulumi.getter
    def deb(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb
    ]: ...
    @_builtins.property
    @pulumi.getter
    def googet(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget
    ]: ...
    @_builtins.property
    @pulumi.getter
    def msi(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi
    ]: ...
    @_builtins.property
    @pulumi.getter
    def rpm(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm
    ]: ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource,
        pull_deps: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource: ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi(
    dict
):
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource,
        properties: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource,
        pull_deps: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource: ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository(
    dict
):
    def __init__(
        __self__,
        *,
        apt: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt
        ] = ...,
        goo: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo
        ] = ...,
        yum: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum
        ] = ...,
        zypper: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt
    ]: ...
    @_builtins.property
    @pulumi.getter
    def goo(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_type: _builtins.str,
        components: Sequence[_builtins.str],
        distribution: _builtins.str,
        uri: _builtins.str,
        gpg_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo(
    dict
):
    def __init__(__self__, *, name: _builtins.str, url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRollout(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disruption_budget: outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget,
        min_wait_duration: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> outputs.V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget: ...
    @_builtins.property
    @pulumi.getter(name="minWaitDuration")
    def min_wait_duration(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget(
    dict
):
    def __init__(
        __self__,
        *,
        fixed: Optional[_builtins.int] = ...,
        percent: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationScope(dict):
    def __init__(
        __self__,
        *,
        selectors: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForOrganizationOrchestrationScopeSelector
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> Optional[
        Sequence[outputs.V2PolicyOrchestratorForOrganizationOrchestrationScopeSelector]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location_selector: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelector
        ] = ...,
        resource_hierarchy_selector: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelector
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationSelector")
    def location_selector(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelector
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceHierarchySelector")
    def resource_hierarchy_selector(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelector
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorLocationSelector(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, included_locations: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedLocations")
    def included_locations(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationScopeSelectorResourceHierarchySelector(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        included_folders: Optional[Sequence[_builtins.str]] = ...,
        included_projects: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedFolders")
    def included_folders(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includedProjects")
    def included_projects(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_iteration_states: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationState
            ]
        ] = ...,
        previous_iteration_state: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationState
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationStates")
    def current_iteration_states(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationState
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="previousIterationState")
    def previous_iteration_state(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationState
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateError
        ] = ...,
        failed_actions: Optional[_builtins.str] = ...,
        finish_time: Optional[_builtins.str] = ...,
        performed_actions: Optional[_builtins.str] = ...,
        progress: Optional[_builtins.float] = ...,
        rollout_resource: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateError
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateError(
    dict
):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetail
            ]
        ] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetail
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationStateCurrentIterationStateErrorDetail(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type_url: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[
            outputs.V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateError
        ] = ...,
        failed_actions: Optional[_builtins.str] = ...,
        finish_time: Optional[_builtins.str] = ...,
        performed_actions: Optional[_builtins.str] = ...,
        progress: Optional[_builtins.float] = ...,
        rollout_resource: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateError
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateError(
    dict
):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetail
            ]
        ] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetail
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorForOrganizationOrchestrationStatePreviousIterationStateErrorDetail(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type_url: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        os_policy_assignment_v1_payload: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1Payload
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osPolicyAssignmentV1Payload")
    def os_policy_assignment_v1_payload(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1Payload
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1Payload(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_filter: outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter,
        os_policies: Sequence[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy
        ],
        rollout: outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRollout,
        baseline: Optional[_builtins.bool] = ...,
        deleted: Optional[_builtins.bool] = ...,
        description: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        reconciling: Optional[_builtins.bool] = ...,
        revision_create_time: Optional[_builtins.str] = ...,
        revision_id: Optional[_builtins.str] = ...,
        rollout_state: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter: ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def rollout(
        self,
    ) -> outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRollout: ...
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        all: Optional[_builtins.bool] = ...,
        exclusion_labels: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel
            ]
        ] = ...,
        inclusion_labels: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel
            ]
        ] = ...,
        inventories: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exclusionLabels")
    def exclusion_labels(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionLabels")
    def inclusion_labels(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def inventories(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory
        ]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterExclusionLabel(
    dict
):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInclusionLabel(
    dict
):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadInstanceFilterInventory(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_short_name: _builtins.str,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        mode: _builtins.str,
        resource_groups: Sequence[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup
        ],
        allow_no_resource_group_match: Optional[_builtins.bool] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup
    ]: ...
    @_builtins.property
    @pulumi.getter(name="allowNoResourceGroupMatch")
    def allow_no_resource_group_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroup(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resources: Sequence[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource
        ],
        inventory_filters: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Sequence[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inventoryFilters")
    def inventory_filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter
        ]
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupInventoryFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_short_name: _builtins.str,
        os_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osShortName")
    def os_short_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        exec_: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec
        ] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile
        ] = ...,
        pkg: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg
        ] = ...,
        repository: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec
    ]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def pkg(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg
    ]: ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExec(
    dict
):
    def __init__(
        __self__,
        *,
        validate: outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate,
        enforce: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate: ...
    @_builtins.property
    @pulumi.getter
    def enforce(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforce(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interpreter: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile
        ] = ...,
        output_file_path: Optional[_builtins.str] = ...,
        script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecEnforceFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidate(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interpreter: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile
        ] = ...,
        output_file_path: Optional[_builtins.str] = ...,
        script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interpreter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputFilePath")
    def output_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceExecValidateFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFile(
    dict
):
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        state: _builtins.str,
        content: Optional[_builtins.str] = ...,
        file: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile
        ] = ...,
        permissions: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFile(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceFileFileRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkg(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        desired_state: _builtins.str,
        apt: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt
        ] = ...,
        deb: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb
        ] = ...,
        googet: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget
        ] = ...,
        msi: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi
        ] = ...,
        rpm: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm
        ] = ...,
        yum: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum
        ] = ...,
        zypper: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt
    ]: ...
    @_builtins.property
    @pulumi.getter
    def deb(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb
    ]: ...
    @_builtins.property
    @pulumi.getter
    def googet(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget
    ]: ...
    @_builtins.property
    @pulumi.getter
    def msi(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi
    ]: ...
    @_builtins.property
    @pulumi.getter
    def rpm(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm
    ]: ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgApt(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDeb(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource,
        pull_deps: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource: ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgDebSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgGooget(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsi(
    dict
):
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource,
        properties: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgMsiSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpm(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource,
        pull_deps: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource: ...
    @_builtins.property
    @pulumi.getter(name="pullDeps")
    def pull_deps(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_insecure: Optional[_builtins.bool] = ...,
        gcs: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs
        ] = ...,
        local_path: Optional[_builtins.str] = ...,
        remote: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def gcs(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def remote(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceGcs(
    dict
):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object: _builtins.str,
        generation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgRpmSourceRemote(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, uri: _builtins.str, sha256_checksum: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha256Checksum")
    def sha256_checksum(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgYum(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourcePkgZypper(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepository(
    dict
):
    def __init__(
        __self__,
        *,
        apt: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt
        ] = ...,
        goo: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo
        ] = ...,
        yum: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum
        ] = ...,
        zypper: Optional[
            outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apt(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt
    ]: ...
    @_builtins.property
    @pulumi.getter
    def goo(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def yum(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zypper(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryApt(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_type: _builtins.str,
        components: Sequence[_builtins.str],
        distribution: _builtins.str,
        uri: _builtins.str,
        gpg_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveType")
    def archive_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpgKey")
    def gpg_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryGoo(
    dict
):
    def __init__(__self__, *, name: _builtins.str, url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryYum(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadOsPolicyResourceGroupResourceRepositoryZypper(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_url: _builtins.str,
        id: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        gpg_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpgKeys")
    def gpg_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRollout(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disruption_budget: outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget,
        min_wait_duration: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> outputs.V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget: ...
    @_builtins.property
    @pulumi.getter(name="minWaitDuration")
    def min_wait_duration(self) -> _builtins.str: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestratedResourceOsPolicyAssignmentV1PayloadRolloutDisruptionBudget(
    dict
):
    def __init__(
        __self__,
        *,
        fixed: Optional[_builtins.int] = ...,
        percent: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fixed(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationScope(dict):
    def __init__(
        __self__,
        *,
        selectors: Optional[
            Sequence[outputs.V2PolicyOrchestratorOrchestrationScopeSelector]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> Optional[Sequence[outputs.V2PolicyOrchestratorOrchestrationScopeSelector]]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationScopeSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location_selector: Optional[
            outputs.V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelector
        ] = ...,
        resource_hierarchy_selector: Optional[
            outputs.V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelector
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationSelector")
    def location_selector(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelector
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceHierarchySelector")
    def resource_hierarchy_selector(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelector
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationScopeSelectorLocationSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, included_locations: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedLocations")
    def included_locations(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationScopeSelectorResourceHierarchySelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        included_folders: Optional[Sequence[_builtins.str]] = ...,
        included_projects: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedFolders")
    def included_folders(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includedProjects")
    def included_projects(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_iteration_states: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorOrchestrationStateCurrentIterationState
            ]
        ] = ...,
        previous_iteration_state: Optional[
            outputs.V2PolicyOrchestratorOrchestrationStatePreviousIterationState
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationStates")
    def current_iteration_states(
        self,
    ) -> Optional[
        Sequence[outputs.V2PolicyOrchestratorOrchestrationStateCurrentIterationState]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="previousIterationState")
    def previous_iteration_state(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestrationStatePreviousIterationState
    ]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationStateCurrentIterationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[
            outputs.V2PolicyOrchestratorOrchestrationStateCurrentIterationStateError
        ] = ...,
        failed_actions: Optional[_builtins.str] = ...,
        finish_time: Optional[_builtins.str] = ...,
        performed_actions: Optional[_builtins.str] = ...,
        progress: Optional[_builtins.float] = ...,
        rollout_resource: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestrationStateCurrentIterationStateError
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationStateCurrentIterationStateError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetail
            ]
        ] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetail
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationStateCurrentIterationStateErrorDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type_url: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationStatePreviousIterationState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[
            outputs.V2PolicyOrchestratorOrchestrationStatePreviousIterationStateError
        ] = ...,
        failed_actions: Optional[_builtins.str] = ...,
        finish_time: Optional[_builtins.str] = ...,
        performed_actions: Optional[_builtins.str] = ...,
        progress: Optional[_builtins.float] = ...,
        rollout_resource: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[
        outputs.V2PolicyOrchestratorOrchestrationStatePreviousIterationStateError
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failedActions")
    def failed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishTime")
    def finish_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performedActions")
    def performed_actions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def progress(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutResource")
    def rollout_resource(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationStatePreviousIterationStateError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[
            Sequence[
                outputs.V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetail
            ]
        ] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        Sequence[
            outputs.V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetail
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2PolicyOrchestratorOrchestrationStatePreviousIterationStateErrorDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type_url: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeUrl")
    def type_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...
