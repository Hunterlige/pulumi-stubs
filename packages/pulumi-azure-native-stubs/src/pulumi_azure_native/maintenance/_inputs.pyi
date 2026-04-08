import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConfigurationAssignmentFilterPropertiesArgs",
    "ConfigurationAssignmentFilterPropertiesArgsDict",
    "InputLinuxParametersArgs",
    "InputLinuxParametersArgsDict",
    "InputPatchConfigurationArgs",
    "InputPatchConfigurationArgsDict",
    "InputWindowsParametersArgs",
    "InputWindowsParametersArgsDict",
    "TagSettingsPropertiesArgs",
    "TagSettingsPropertiesArgsDict",
]

class ConfigurationAssignmentFilterPropertiesArgsDict(TypedDict):
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    os_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tag_settings: NotRequired[pulumi.Input[TagSettingsPropertiesArgsDict]]

@pulumi.input_type
class ConfigurationAssignmentFilterPropertiesArgs:
    def __init__(
        __self__,
        *,
        locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        os_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        resource_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_settings: Optional[pulumi.Input[TagSettingsPropertiesArgs]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="osTypes")
    def os_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @os_types.setter
    def os_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_groups.setter
    def resource_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_types.setter
    def resource_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagSettings")
    def tag_settings(self) -> Optional[pulumi.Input[TagSettingsPropertiesArgs]]: ...
    @tag_settings.setter
    def tag_settings(
        self, value: Optional[pulumi.Input[TagSettingsPropertiesArgs]]
    ): ...

class InputLinuxParametersArgsDict(TypedDict):
    classifications_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    package_name_masks_to_exclude: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    package_name_masks_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class InputLinuxParametersArgs:
    def __init__(
        __self__,
        *,
        classifications_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        package_name_masks_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        package_name_masks_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="classificationsToInclude")
    def classifications_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @classifications_to_include.setter
    def classifications_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="packageNameMasksToExclude")
    def package_name_masks_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @package_name_masks_to_exclude.setter
    def package_name_masks_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="packageNameMasksToInclude")
    def package_name_masks_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @package_name_masks_to_include.setter
    def package_name_masks_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class InputPatchConfigurationArgsDict(TypedDict):
    linux_parameters: NotRequired[pulumi.Input[InputLinuxParametersArgsDict]]
    reboot_setting: NotRequired[pulumi.Input[Union[_builtins.str, RebootOptions]]]
    windows_parameters: NotRequired[pulumi.Input[InputWindowsParametersArgsDict]]

@pulumi.input_type
class InputPatchConfigurationArgs:
    def __init__(
        __self__,
        *,
        linux_parameters: Optional[pulumi.Input[InputLinuxParametersArgs]] = ...,
        reboot_setting: Optional[
            pulumi.Input[Union[_builtins.str, RebootOptions]]
        ] = ...,
        windows_parameters: Optional[pulumi.Input[InputWindowsParametersArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxParameters")
    def linux_parameters(self) -> Optional[pulumi.Input[InputLinuxParametersArgs]]: ...
    @linux_parameters.setter
    def linux_parameters(
        self, value: Optional[pulumi.Input[InputLinuxParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RebootOptions]]]: ...
    @reboot_setting.setter
    def reboot_setting(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RebootOptions]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsParameters")
    def windows_parameters(
        self,
    ) -> Optional[pulumi.Input[InputWindowsParametersArgs]]: ...
    @windows_parameters.setter
    def windows_parameters(
        self, value: Optional[pulumi.Input[InputWindowsParametersArgs]]
    ): ...

class InputWindowsParametersArgsDict(TypedDict):
    classifications_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    exclude_kbs_requiring_reboot: NotRequired[pulumi.Input[_builtins.bool]]
    kb_numbers_to_exclude: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    kb_numbers_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class InputWindowsParametersArgs:
    def __init__(
        __self__,
        *,
        classifications_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        exclude_kbs_requiring_reboot: Optional[pulumi.Input[_builtins.bool]] = ...,
        kb_numbers_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kb_numbers_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="classificationsToInclude")
    def classifications_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @classifications_to_include.setter
    def classifications_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeKbsRequiringReboot")
    def exclude_kbs_requiring_reboot(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_kbs_requiring_reboot.setter
    def exclude_kbs_requiring_reboot(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kbNumbersToExclude")
    def kb_numbers_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @kb_numbers_to_exclude.setter
    def kb_numbers_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kbNumbersToInclude")
    def kb_numbers_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @kb_numbers_to_include.setter
    def kb_numbers_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TagSettingsPropertiesArgsDict(TypedDict):
    filter_operator: NotRequired[pulumi.Input[TagOperators]]
    tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]

@pulumi.input_type
class TagSettingsPropertiesArgs:
    def __init__(
        __self__,
        *,
        filter_operator: Optional[pulumi.Input[TagOperators]] = ...,
        tags: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterOperator")
    def filter_operator(self) -> Optional[pulumi.Input[TagOperators]]: ...
    @filter_operator.setter
    def filter_operator(self, value: Optional[pulumi.Input[TagOperators]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...
