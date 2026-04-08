import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConfigurationPropertiesArgs",
    "ConfigurationPropertiesArgsDict",
    "ConsoleCreatePropertiesArgs",
    "ConsoleCreatePropertiesArgsDict",
    "DashboardLensArgs",
    "DashboardLensArgsDict",
    "DashboardPartMetadataArgs",
    "DashboardPartMetadataArgsDict",
    "DashboardPartsPositionArgs",
    "DashboardPartsPositionArgsDict",
    "DashboardPartsArgs",
    "DashboardPartsArgsDict",
    "DashboardPropertiesWithProvisioningStateArgs",
    "DashboardPropertiesWithProvisioningStateArgsDict",
    "StorageProfileArgs",
    "StorageProfileArgsDict",
    "TerminalSettingsArgs",
    "TerminalSettingsArgsDict",
    "UserPropertiesArgs",
    "UserPropertiesArgsDict",
]

class ConfigurationPropertiesArgsDict(TypedDict):
    enforce_private_markdown_storage: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConfigurationPropertiesArgs:
    def __init__(
        __self__,
        *,
        enforce_private_markdown_storage: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enforcePrivateMarkdownStorage")
    def enforce_private_markdown_storage(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce_private_markdown_storage.setter
    def enforce_private_markdown_storage(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ConsoleCreatePropertiesArgsDict(TypedDict):
    os_type: pulumi.Input[Union[_builtins.str, OsType]]
    provisioning_state: NotRequired[
        pulumi.Input[Union[_builtins.str, ProvisioningState]]
    ]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConsoleCreatePropertiesArgs:
    def __init__(
        __self__,
        *,
        os_type: pulumi.Input[Union[_builtins.str, OsType]],
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[Union[_builtins.str, OsType]]: ...
    @os_type.setter
    def os_type(self, value: pulumi.Input[Union[_builtins.str, OsType]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]: ...
    @provisioning_state.setter
    def provisioning_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardLensArgsDict(TypedDict):
    order: pulumi.Input[_builtins.int]
    parts: pulumi.Input[Sequence[pulumi.Input[DashboardPartsArgsDict]]]
    metadata: NotRequired[Any]

@pulumi.input_type
class DashboardLensArgs:
    def __init__(
        __self__,
        *,
        order: pulumi.Input[_builtins.int],
        parts: pulumi.Input[Sequence[pulumi.Input[DashboardPartsArgs]]],
        metadata: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Input[_builtins.int]: ...
    @order.setter
    def order(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def parts(self) -> pulumi.Input[Sequence[pulumi.Input[DashboardPartsArgs]]]: ...
    @parts.setter
    def parts(
        self, value: pulumi.Input[Sequence[pulumi.Input[DashboardPartsArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @metadata.setter
    def metadata(self, value: Optional[Any]): ...

class DashboardPartMetadataArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    inputs: NotRequired[pulumi.Input[Sequence[Any]]]
    settings: NotRequired[pulumi.Input[Mapping[str, Any]]]

@pulumi.input_type
class DashboardPartMetadataArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        inputs: Optional[pulumi.Input[Sequence[Any]]] = ...,
        settings: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[Any]]]: ...
    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[Any]]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Mapping[str, Any]]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Mapping[str, Any]]]): ...

class DashboardPartsPositionArgsDict(TypedDict):
    col_span: pulumi.Input[_builtins.int]
    row_span: pulumi.Input[_builtins.int]
    x: pulumi.Input[_builtins.int]
    y: pulumi.Input[_builtins.int]
    metadata: NotRequired[Any]

@pulumi.input_type
class DashboardPartsPositionArgs:
    def __init__(
        __self__,
        *,
        col_span: pulumi.Input[_builtins.int],
        row_span: pulumi.Input[_builtins.int],
        x: pulumi.Input[_builtins.int],
        y: pulumi.Input[_builtins.int],
        metadata: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="colSpan")
    def col_span(self) -> pulumi.Input[_builtins.int]: ...
    @col_span.setter
    def col_span(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="rowSpan")
    def row_span(self) -> pulumi.Input[_builtins.int]: ...
    @row_span.setter
    def row_span(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def x(self) -> pulumi.Input[_builtins.int]: ...
    @x.setter
    def x(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def y(self) -> pulumi.Input[_builtins.int]: ...
    @y.setter
    def y(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @metadata.setter
    def metadata(self, value: Optional[Any]): ...

class DashboardPartsArgsDict(TypedDict):
    position: pulumi.Input[DashboardPartsPositionArgsDict]
    metadata: NotRequired[pulumi.Input[DashboardPartMetadataArgsDict]]

@pulumi.input_type
class DashboardPartsArgs:
    def __init__(
        __self__,
        *,
        position: pulumi.Input[DashboardPartsPositionArgs],
        metadata: Optional[pulumi.Input[DashboardPartMetadataArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> pulumi.Input[DashboardPartsPositionArgs]: ...
    @position.setter
    def position(self, value: pulumi.Input[DashboardPartsPositionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[DashboardPartMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[DashboardPartMetadataArgs]]): ...

class DashboardPropertiesWithProvisioningStateArgsDict(TypedDict):
    lenses: NotRequired[pulumi.Input[Sequence[pulumi.Input[DashboardLensArgsDict]]]]
    metadata: NotRequired[Any]

@pulumi.input_type
class DashboardPropertiesWithProvisioningStateArgs:
    def __init__(
        __self__,
        *,
        lenses: Optional[pulumi.Input[Sequence[pulumi.Input[DashboardLensArgs]]]] = ...,
        metadata: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def lenses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DashboardLensArgs]]]]: ...
    @lenses.setter
    def lenses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DashboardLensArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @metadata.setter
    def metadata(self, value: Optional[Any]): ...

class StorageProfileArgsDict(TypedDict):
    disk_size_in_gb: NotRequired[pulumi.Input[_builtins.int]]
    file_share_name: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageProfileArgs:
    def __init__(
        __self__,
        *,
        disk_size_in_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeInGB")
    def disk_size_in_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_in_gb.setter
    def disk_size_in_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_share_name.setter
    def file_share_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_resource_id.setter
    def storage_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class TerminalSettingsArgsDict(TypedDict):
    font_size: NotRequired[pulumi.Input[Union[_builtins.str, FontSize]]]
    font_style: NotRequired[pulumi.Input[Union[_builtins.str, FontStyle]]]

@pulumi.input_type
class TerminalSettingsArgs:
    def __init__(
        __self__,
        *,
        font_size: Optional[pulumi.Input[Union[_builtins.str, FontSize]]] = ...,
        font_style: Optional[pulumi.Input[Union[_builtins.str, FontStyle]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fontSize")
    def font_size(self) -> Optional[pulumi.Input[Union[_builtins.str, FontSize]]]: ...
    @font_size.setter
    def font_size(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FontSize]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fontStyle")
    def font_style(self) -> Optional[pulumi.Input[Union[_builtins.str, FontStyle]]]: ...
    @font_style.setter
    def font_style(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FontStyle]]]
    ): ...

class UserPropertiesArgsDict(TypedDict):
    preferred_location: pulumi.Input[_builtins.str]
    preferred_os_type: pulumi.Input[Union[_builtins.str, OsType]]
    preferred_shell_type: pulumi.Input[Union[_builtins.str, ShellType]]
    storage_profile: pulumi.Input[StorageProfileArgsDict]
    terminal_settings: pulumi.Input[TerminalSettingsArgsDict]

@pulumi.input_type
class UserPropertiesArgs:
    def __init__(
        __self__,
        *,
        preferred_location: pulumi.Input[_builtins.str],
        preferred_os_type: pulumi.Input[Union[_builtins.str, OsType]],
        preferred_shell_type: pulumi.Input[Union[_builtins.str, ShellType]],
        storage_profile: pulumi.Input[StorageProfileArgs],
        terminal_settings: pulumi.Input[TerminalSettingsArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredLocation")
    def preferred_location(self) -> pulumi.Input[_builtins.str]: ...
    @preferred_location.setter
    def preferred_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="preferredOsType")
    def preferred_os_type(self) -> pulumi.Input[Union[_builtins.str, OsType]]: ...
    @preferred_os_type.setter
    def preferred_os_type(self, value: pulumi.Input[Union[_builtins.str, OsType]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredShellType")
    def preferred_shell_type(self) -> pulumi.Input[Union[_builtins.str, ShellType]]: ...
    @preferred_shell_type.setter
    def preferred_shell_type(
        self, value: pulumi.Input[Union[_builtins.str, ShellType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Input[StorageProfileArgs]: ...
    @storage_profile.setter
    def storage_profile(self, value: pulumi.Input[StorageProfileArgs]): ...
    @_builtins.property
    @pulumi.getter(name="terminalSettings")
    def terminal_settings(self) -> pulumi.Input[TerminalSettingsArgs]: ...
    @terminal_settings.setter
    def terminal_settings(self, value: pulumi.Input[TerminalSettingsArgs]): ...
