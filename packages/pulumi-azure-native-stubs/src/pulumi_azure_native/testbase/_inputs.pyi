import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CommandArgs",
    "CommandArgsDict",
    "DistributionGroupListReceiverValueArgs",
    "DistributionGroupListReceiverValueArgsDict",
    "DraftPackageIntuneAppMetadataItemArgs",
    "DraftPackageIntuneAppMetadataItemArgsDict",
    "DraftPackageIntuneAppMetadataArgs",
    "DraftPackageIntuneAppMetadataArgsDict",
    "EnrolledIntuneAppArgs",
    "EnrolledIntuneAppArgsDict",
    "FirstPartyAppDefinitionArgs",
    "FirstPartyAppDefinitionArgsDict",
    "GalleryAppDefinitionArgs",
    "GalleryAppDefinitionArgsDict",
    "HighlightedFileArgs",
    "HighlightedFileArgsDict",
    "InplaceUpgradeOSInfoArgs",
    "InplaceUpgradeOSInfoArgsDict",
    "IntuneEnrollmentMetadataArgs",
    "IntuneEnrollmentMetadataArgsDict",
    "NotificationEventReceiverArgs",
    "NotificationEventReceiverArgsDict",
    "NotificationReceiverValueArgs",
    "NotificationReceiverValueArgsDict",
    "OsPropertiesArgs",
    "OsPropertiesArgsDict",
    "PreReleaseAccessRequestSpecArgs",
    "PreReleaseAccessRequestSpecArgsDict",
    "ReleasePropertiesArgs",
    "ReleasePropertiesArgsDict",
    "SubscriptionReceiverValueArgs",
    "SubscriptionReceiverValueArgsDict",
    "SystemAssignedServiceIdentityArgs",
    "SystemAssignedServiceIdentityArgsDict",
    "TabStateArgs",
    "TabStateArgsDict",
    "TargetOSInfoArgs",
    "TargetOSInfoArgsDict",
    "TestBaseAccountSKUArgs",
    "TestBaseAccountSKUArgsDict",
    "TestArgs",
    "TestArgsDict",
    "UserObjectReceiverValueArgs",
    "UserObjectReceiverValueArgsDict",
]

class CommandArgsDict(TypedDict):
    action: pulumi.Input[Union[_builtins.str, Action]]
    content: pulumi.Input[_builtins.str]
    content_type: pulumi.Input[Union[_builtins.str, ContentType]]
    name: pulumi.Input[_builtins.str]
    always_run: NotRequired[pulumi.Input[_builtins.bool]]
    apply_update_before: NotRequired[pulumi.Input[_builtins.bool]]
    enroll_intune_before: NotRequired[pulumi.Input[_builtins.bool]]
    install1_p_app_before: NotRequired[pulumi.Input[_builtins.bool]]
    max_run_time: NotRequired[pulumi.Input[_builtins.int]]
    post_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    pre_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    restart_after: NotRequired[pulumi.Input[_builtins.bool]]
    run_as_interactive: NotRequired[pulumi.Input[_builtins.bool]]
    run_elevated: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class CommandArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[Union[_builtins.str, Action]],
        content: pulumi.Input[_builtins.str],
        content_type: pulumi.Input[Union[_builtins.str, ContentType]],
        name: pulumi.Input[_builtins.str],
        always_run: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_update_before: Optional[pulumi.Input[_builtins.bool]] = ...,
        enroll_intune_before: Optional[pulumi.Input[_builtins.bool]] = ...,
        install1_p_app_before: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_run_time: Optional[pulumi.Input[_builtins.int]] = ...,
        post_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        pre_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        restart_after: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_as_interactive: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_elevated: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, Action]]: ...
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, Action]]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[_builtins.str]: ...
    @content.setter
    def content(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[Union[_builtins.str, ContentType]]: ...
    @content_type.setter
    def content_type(self, value: pulumi.Input[Union[_builtins.str, ContentType]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="alwaysRun")
    def always_run(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @always_run.setter
    def always_run(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="applyUpdateBefore")
    def apply_update_before(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_update_before.setter
    def apply_update_before(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enrollIntuneBefore")
    def enroll_intune_before(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enroll_intune_before.setter
    def enroll_intune_before(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="install1PAppBefore")
    def install1_p_app_before(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @install1_p_app_before.setter
    def install1_p_app_before(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRunTime")
    def max_run_time(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_run_time.setter
    def max_run_time(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="postUpgrade")
    def post_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @post_upgrade.setter
    def post_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="preUpgrade")
    def pre_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pre_upgrade.setter
    def pre_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="restartAfter")
    def restart_after(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @restart_after.setter
    def restart_after(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runAsInteractive")
    def run_as_interactive(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_as_interactive.setter
    def run_as_interactive(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runElevated")
    def run_elevated(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_elevated.setter
    def run_elevated(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DistributionGroupListReceiverValueArgsDict(TypedDict):
    distribution_groups: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DistributionGroupListReceiverValueArgs:
    def __init__(
        __self__,
        *,
        distribution_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributionGroups")
    def distribution_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @distribution_groups.setter
    def distribution_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DraftPackageIntuneAppMetadataItemArgsDict(TypedDict):
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    app_name: NotRequired[pulumi.Input[_builtins.str]]
    create_date: NotRequired[pulumi.Input[_builtins.str]]
    dependency_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dependent_app_count: NotRequired[pulumi.Input[_builtins.int]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    expected_exit_codes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    install_command: NotRequired[pulumi.Input[_builtins.str]]
    last_processed: NotRequired[pulumi.Input[_builtins.float]]
    minimum_supported_os: NotRequired[pulumi.Input[_builtins.str]]
    owner: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    setup_file: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, IntuneExtractStatus]]]
    uninstall_command: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DraftPackageIntuneAppMetadataItemArgs:
    def __init__(
        __self__,
        *,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_date: Optional[pulumi.Input[_builtins.str]] = ...,
        dependency_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dependent_app_count: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_exit_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        install_command: Optional[pulumi.Input[_builtins.str]] = ...,
        last_processed: Optional[pulumi.Input[_builtins.float]] = ...,
        minimum_supported_os: Optional[pulumi.Input[_builtins.str]] = ...,
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        setup_file: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, IntuneExtractStatus]]] = ...,
        uninstall_command: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_name.setter
    def app_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_date.setter
    def create_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dependencyIds")
    def dependency_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dependency_ids.setter
    def dependency_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependentAppCount")
    def dependent_app_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dependent_app_count.setter
    def dependent_app_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedExitCodes")
    def expected_exit_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expected_exit_codes.setter
    def expected_exit_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="installCommand")
    def install_command(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @install_command.setter
    def install_command(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastProcessed")
    def last_processed(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @last_processed.setter
    def last_processed(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumSupportedOS")
    def minimum_supported_os(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_supported_os.setter
    def minimum_supported_os(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="setupFile")
    def setup_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @setup_file.setter
    def setup_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IntuneExtractStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IntuneExtractStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uninstallCommand")
    def uninstall_command(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uninstall_command.setter
    def uninstall_command(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DraftPackageIntuneAppMetadataArgsDict(TypedDict):
    intune_app: NotRequired[pulumi.Input[DraftPackageIntuneAppMetadataItemArgsDict]]
    intune_app_dependencies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DraftPackageIntuneAppMetadataItemArgsDict]]]
    ]

@pulumi.input_type
class DraftPackageIntuneAppMetadataArgs:
    def __init__(
        __self__,
        *,
        intune_app: Optional[pulumi.Input[DraftPackageIntuneAppMetadataItemArgs]] = ...,
        intune_app_dependencies: Optional[
            pulumi.Input[Sequence[pulumi.Input[DraftPackageIntuneAppMetadataItemArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intuneApp")
    def intune_app(
        self,
    ) -> Optional[pulumi.Input[DraftPackageIntuneAppMetadataItemArgs]]: ...
    @intune_app.setter
    def intune_app(
        self, value: Optional[pulumi.Input[DraftPackageIntuneAppMetadataItemArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="intuneAppDependencies")
    def intune_app_dependencies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DraftPackageIntuneAppMetadataItemArgs]]]
    ]: ...
    @intune_app_dependencies.setter
    def intune_app_dependencies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DraftPackageIntuneAppMetadataItemArgs]]]
        ],
    ): ...

class EnrolledIntuneAppArgsDict(TypedDict):
    app_id: pulumi.Input[_builtins.str]
    app_name: pulumi.Input[_builtins.str]
    expected_installation_path: pulumi.Input[_builtins.str]

@pulumi.input_type
class EnrolledIntuneAppArgs:
    def __init__(
        __self__,
        *,
        app_id: pulumi.Input[_builtins.str],
        app_name: pulumi.Input[_builtins.str],
        expected_installation_path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]: ...
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Input[_builtins.str]: ...
    @app_name.setter
    def app_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="expectedInstallationPath")
    def expected_installation_path(self) -> pulumi.Input[_builtins.str]: ...
    @expected_installation_path.setter
    def expected_installation_path(self, value: pulumi.Input[_builtins.str]): ...

class FirstPartyAppDefinitionArgsDict(TypedDict):
    architecture: NotRequired[pulumi.Input[Union[_builtins.str, Architecture]]]
    channel: NotRequired[pulumi.Input[_builtins.str]]
    interop_execution_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, InteropExecutionMode]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ring: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FirstPartyAppDefinitionArgs:
    def __init__(
        __self__,
        *,
        architecture: Optional[pulumi.Input[Union[_builtins.str, Architecture]]] = ...,
        channel: Optional[pulumi.Input[_builtins.str]] = ...,
        interop_execution_mode: Optional[
            pulumi.Input[Union[_builtins.str, InteropExecutionMode]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ring: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def architecture(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, Architecture]]]: ...
    @architecture.setter
    def architecture(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Architecture]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="interopExecutionMode")
    def interop_execution_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InteropExecutionMode]]]: ...
    @interop_execution_mode.setter
    def interop_execution_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InteropExecutionMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ring(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ring.setter
    def ring(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GalleryAppDefinitionArgsDict(TypedDict):
    sku_id: pulumi.Input[_builtins.str]
    is_consented: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GalleryAppDefinitionArgs:
    def __init__(
        __self__,
        *,
        sku_id: pulumi.Input[_builtins.str],
        is_consented: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> pulumi.Input[_builtins.str]: ...
    @sku_id.setter
    def sku_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isConsented")
    def is_consented(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_consented.setter
    def is_consented(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class HighlightedFileArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    sections: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    visited: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class HighlightedFileArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        sections: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        visited: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @sections.setter
    def sections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def visited(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @visited.setter
    def visited(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InplaceUpgradeOSInfoArgsDict(TypedDict):
    baseline_os: NotRequired[pulumi.Input[OsPropertiesArgsDict]]
    target_os: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InplaceUpgradeOSInfoArgs:
    def __init__(
        __self__,
        *,
        baseline_os: Optional[pulumi.Input[OsPropertiesArgs]] = ...,
        target_os: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baselineOS")
    def baseline_os(self) -> Optional[pulumi.Input[OsPropertiesArgs]]: ...
    @baseline_os.setter
    def baseline_os(self, value: Optional[pulumi.Input[OsPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetOS")
    def target_os(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_os.setter
    def target_os(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IntuneEnrollmentMetadataArgsDict(TypedDict):
    app_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EnrolledIntuneAppArgsDict]]]
    ]
    credential_id: NotRequired[pulumi.Input[_builtins.str]]
    expected_deployment_duration_in_minute: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class IntuneEnrollmentMetadataArgs:
    def __init__(
        __self__,
        *,
        app_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnrolledIntuneAppArgs]]]
        ] = ...,
        credential_id: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_deployment_duration_in_minute: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appList")
    def app_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnrolledIntuneAppArgs]]]]: ...
    @app_list.setter
    def app_list(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EnrolledIntuneAppArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="credentialId")
    def credential_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_id.setter
    def credential_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedDeploymentDurationInMinute")
    def expected_deployment_duration_in_minute(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @expected_deployment_duration_in_minute.setter
    def expected_deployment_duration_in_minute(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class NotificationEventReceiverArgsDict(TypedDict):
    receiver_type: NotRequired[pulumi.Input[_builtins.str]]
    receiver_value: NotRequired[pulumi.Input[NotificationReceiverValueArgsDict]]

@pulumi.input_type
class NotificationEventReceiverArgs:
    def __init__(
        __self__,
        *,
        receiver_type: Optional[pulumi.Input[_builtins.str]] = ...,
        receiver_value: Optional[pulumi.Input[NotificationReceiverValueArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="receiverType")
    def receiver_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @receiver_type.setter
    def receiver_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="receiverValue")
    def receiver_value(
        self,
    ) -> Optional[pulumi.Input[NotificationReceiverValueArgs]]: ...
    @receiver_value.setter
    def receiver_value(
        self, value: Optional[pulumi.Input[NotificationReceiverValueArgs]]
    ): ...

class NotificationReceiverValueArgsDict(TypedDict):
    distribution_group_list_receiver_value: NotRequired[
        pulumi.Input[DistributionGroupListReceiverValueArgsDict]
    ]
    subscription_receiver_value: NotRequired[
        pulumi.Input[SubscriptionReceiverValueArgsDict]
    ]
    user_object_receiver_value: NotRequired[
        pulumi.Input[UserObjectReceiverValueArgsDict]
    ]

@pulumi.input_type
class NotificationReceiverValueArgs:
    def __init__(
        __self__,
        *,
        distribution_group_list_receiver_value: Optional[
            pulumi.Input[DistributionGroupListReceiverValueArgs]
        ] = ...,
        subscription_receiver_value: Optional[
            pulumi.Input[SubscriptionReceiverValueArgs]
        ] = ...,
        user_object_receiver_value: Optional[
            pulumi.Input[UserObjectReceiverValueArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributionGroupListReceiverValue")
    def distribution_group_list_receiver_value(
        self,
    ) -> Optional[pulumi.Input[DistributionGroupListReceiverValueArgs]]: ...
    @distribution_group_list_receiver_value.setter
    def distribution_group_list_receiver_value(
        self, value: Optional[pulumi.Input[DistributionGroupListReceiverValueArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionReceiverValue")
    def subscription_receiver_value(
        self,
    ) -> Optional[pulumi.Input[SubscriptionReceiverValueArgs]]: ...
    @subscription_receiver_value.setter
    def subscription_receiver_value(
        self, value: Optional[pulumi.Input[SubscriptionReceiverValueArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userObjectReceiverValue")
    def user_object_receiver_value(
        self,
    ) -> Optional[pulumi.Input[UserObjectReceiverValueArgs]]: ...
    @user_object_receiver_value.setter
    def user_object_receiver_value(
        self, value: Optional[pulumi.Input[UserObjectReceiverValueArgs]]
    ): ...

class OsPropertiesArgsDict(TypedDict):
    custom_image_id: NotRequired[pulumi.Input[_builtins.str]]
    os_name: NotRequired[pulumi.Input[_builtins.str]]
    release_properties: NotRequired[pulumi.Input[ReleasePropertiesArgsDict]]

@pulumi.input_type
class OsPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        os_name: Optional[pulumi.Input[_builtins.str]] = ...,
        release_properties: Optional[pulumi.Input[ReleasePropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_image_id.setter
    def custom_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_name.setter
    def os_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseProperties")
    def release_properties(self) -> Optional[pulumi.Input[ReleasePropertiesArgs]]: ...
    @release_properties.setter
    def release_properties(
        self, value: Optional[pulumi.Input[ReleasePropertiesArgs]]
    ): ...

class PreReleaseAccessRequestSpecArgsDict(TypedDict):
    city: NotRequired[pulumi.Input[_builtins.str]]
    company_website: NotRequired[pulumi.Input[_builtins.str]]
    country_and_region: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    engagements: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Engagements]]]]
    ]
    organization_name: NotRequired[pulumi.Input[_builtins.str]]
    state_or_province: NotRequired[pulumi.Input[_builtins.str]]
    street_address: NotRequired[pulumi.Input[_builtins.str]]
    zip_code: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PreReleaseAccessRequestSpecArgs:
    def __init__(
        __self__,
        *,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        company_website: Optional[pulumi.Input[_builtins.str]] = ...,
        country_and_region: Optional[pulumi.Input[_builtins.str]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        engagements: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Engagements]]]]
        ] = ...,
        organization_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state_or_province: Optional[pulumi.Input[_builtins.str]] = ...,
        street_address: Optional[pulumi.Input[_builtins.str]] = ...,
        zip_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="companyWebsite")
    def company_website(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @company_website.setter
    def company_website(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="countryAndRegion")
    def country_and_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country_and_region.setter
    def country_and_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def engagements(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Engagements]]]]
    ]: ...
    @engagements.setter
    def engagements(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Engagements]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_or_province.setter
    def state_or_province(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @street_address.setter
    def street_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReleasePropertiesArgsDict(TypedDict):
    build_number: NotRequired[pulumi.Input[_builtins.str]]
    build_revision: NotRequired[pulumi.Input[_builtins.str]]
    release_name: NotRequired[pulumi.Input[_builtins.str]]
    release_version_date: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReleasePropertiesArgs:
    def __init__(
        __self__,
        *,
        build_number: Optional[pulumi.Input[_builtins.str]] = ...,
        build_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        release_name: Optional[pulumi.Input[_builtins.str]] = ...,
        release_version_date: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="buildNumber")
    def build_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_number.setter
    def build_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="buildRevision")
    def build_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_revision.setter
    def build_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseName")
    def release_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_name.setter
    def release_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseVersionDate")
    def release_version_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_version_date.setter
    def release_version_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubscriptionReceiverValueArgsDict(TypedDict):
    role: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    subscription_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubscriptionReceiverValueArgs:
    def __init__(
        __self__,
        *,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_name.setter
    def subscription_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SystemAssignedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]]

@pulumi.input_type
class SystemAssignedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]]: ...
    @type.setter
    def type(
        self,
        value: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]],
    ): ...

class TabStateArgsDict(TypedDict):
    current_tab: NotRequired[pulumi.Input[Union[_builtins.str, PackageStudioTabs]]]
    visited_tabs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PackageStudioTabs]]]]
    ]

@pulumi.input_type
class TabStateArgs:
    def __init__(
        __self__,
        *,
        current_tab: Optional[
            pulumi.Input[Union[_builtins.str, PackageStudioTabs]]
        ] = ...,
        visited_tabs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, PackageStudioTabs]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentTab")
    def current_tab(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PackageStudioTabs]]]: ...
    @current_tab.setter
    def current_tab(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PackageStudioTabs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="visitedTabs")
    def visited_tabs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PackageStudioTabs]]]]
    ]: ...
    @visited_tabs.setter
    def visited_tabs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, PackageStudioTabs]]]
            ]
        ],
    ): ...

class TargetOSInfoArgsDict(TypedDict):
    os_update_type: pulumi.Input[_builtins.str]
    baseline_oss: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    insider_channel_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    target_os_image_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    target_oss: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class TargetOSInfoArgs:
    def __init__(
        __self__,
        *,
        os_update_type: pulumi.Input[_builtins.str],
        baseline_oss: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        insider_channel_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_os_image_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_oss: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osUpdateType")
    def os_update_type(self) -> pulumi.Input[_builtins.str]: ...
    @os_update_type.setter
    def os_update_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="baselineOSs")
    def baseline_oss(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @baseline_oss.setter
    def baseline_oss(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="insiderChannelIds")
    def insider_channel_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @insider_channel_ids.setter
    def insider_channel_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetOSImageIds")
    def target_os_image_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_os_image_ids.setter
    def target_os_image_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetOSs")
    def target_oss(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_oss.setter
    def target_oss(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TestBaseAccountSKUArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    tier: pulumi.Input[Union[_builtins.str, Tier]]
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TestBaseAccountSKUArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        tier: pulumi.Input[Union[_builtins.str, Tier]],
        locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[_builtins.str, Tier]]: ...
    @tier.setter
    def tier(self, value: pulumi.Input[Union[_builtins.str, Tier]]): ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @locations.setter
    def locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TestArgsDict(TypedDict):
    commands: pulumi.Input[Sequence[pulumi.Input[CommandArgsDict]]]
    test_type: pulumi.Input[Union[_builtins.str, TestType]]
    is_active: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TestArgs:
    def __init__(
        __self__,
        *,
        commands: pulumi.Input[Sequence[pulumi.Input[CommandArgs]]],
        test_type: pulumi.Input[Union[_builtins.str, TestType]],
        is_active: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> pulumi.Input[Sequence[pulumi.Input[CommandArgs]]]: ...
    @commands.setter
    def commands(self, value: pulumi.Input[Sequence[pulumi.Input[CommandArgs]]]): ...
    @_builtins.property
    @pulumi.getter(name="testType")
    def test_type(self) -> pulumi.Input[Union[_builtins.str, TestType]]: ...
    @test_type.setter
    def test_type(self, value: pulumi.Input[Union[_builtins.str, TestType]]): ...
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_active.setter
    def is_active(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class UserObjectReceiverValueArgsDict(TypedDict):
    user_object_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class UserObjectReceiverValueArgs:
    def __init__(
        __self__,
        *,
        user_object_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userObjectIds")
    def user_object_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_object_ids.setter
    def user_object_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
