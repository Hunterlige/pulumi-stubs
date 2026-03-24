import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FloorsettingArgs", "Floorsetting"]

@pulumi.input_type
class FloorsettingArgs:
    def __init__(
        __self__,
        *,
        filter_config: pulumi.Input[FloorsettingFilterConfigArgs],
        location: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        ai_platform_floor_setting: Optional[
            pulumi.Input[FloorsettingAiPlatformFloorSettingArgs]
        ] = ...,
        enable_floor_setting_enforcement: Optional[pulumi.Input[_builtins.bool]] = ...,
        floor_setting_metadata: Optional[
            pulumi.Input[FloorsettingFloorSettingMetadataArgs]
        ] = ...,
        google_mcp_server_floor_setting: Optional[
            pulumi.Input[FloorsettingGoogleMcpServerFloorSettingArgs]
        ] = ...,
        integrated_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterConfig")
    def filter_config(self) -> pulumi.Input[FloorsettingFilterConfigArgs]: ...
    @filter_config.setter
    def filter_config(self, value: pulumi.Input[FloorsettingFilterConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="aiPlatformFloorSetting")
    def ai_platform_floor_setting(
        self,
    ) -> Optional[pulumi.Input[FloorsettingAiPlatformFloorSettingArgs]]: ...
    @ai_platform_floor_setting.setter
    def ai_platform_floor_setting(
        self, value: Optional[pulumi.Input[FloorsettingAiPlatformFloorSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableFloorSettingEnforcement")
    def enable_floor_setting_enforcement(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_floor_setting_enforcement.setter
    def enable_floor_setting_enforcement(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="floorSettingMetadata")
    def floor_setting_metadata(
        self,
    ) -> Optional[pulumi.Input[FloorsettingFloorSettingMetadataArgs]]: ...
    @floor_setting_metadata.setter
    def floor_setting_metadata(
        self, value: Optional[pulumi.Input[FloorsettingFloorSettingMetadataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleMcpServerFloorSetting")
    def google_mcp_server_floor_setting(
        self,
    ) -> Optional[pulumi.Input[FloorsettingGoogleMcpServerFloorSettingArgs]]: ...
    @google_mcp_server_floor_setting.setter
    def google_mcp_server_floor_setting(
        self, value: Optional[pulumi.Input[FloorsettingGoogleMcpServerFloorSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="integratedServices")
    def integrated_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @integrated_services.setter
    def integrated_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _FloorsettingState:
    def __init__(
        __self__,
        *,
        ai_platform_floor_setting: Optional[
            pulumi.Input[FloorsettingAiPlatformFloorSettingArgs]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_floor_setting_enforcement: Optional[pulumi.Input[_builtins.bool]] = ...,
        filter_config: Optional[pulumi.Input[FloorsettingFilterConfigArgs]] = ...,
        floor_setting_metadata: Optional[
            pulumi.Input[FloorsettingFloorSettingMetadataArgs]
        ] = ...,
        google_mcp_server_floor_setting: Optional[
            pulumi.Input[FloorsettingGoogleMcpServerFloorSettingArgs]
        ] = ...,
        integrated_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aiPlatformFloorSetting")
    def ai_platform_floor_setting(
        self,
    ) -> Optional[pulumi.Input[FloorsettingAiPlatformFloorSettingArgs]]: ...
    @ai_platform_floor_setting.setter
    def ai_platform_floor_setting(
        self, value: Optional[pulumi.Input[FloorsettingAiPlatformFloorSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableFloorSettingEnforcement")
    def enable_floor_setting_enforcement(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_floor_setting_enforcement.setter
    def enable_floor_setting_enforcement(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterConfig")
    def filter_config(self) -> Optional[pulumi.Input[FloorsettingFilterConfigArgs]]: ...
    @filter_config.setter
    def filter_config(
        self, value: Optional[pulumi.Input[FloorsettingFilterConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="floorSettingMetadata")
    def floor_setting_metadata(
        self,
    ) -> Optional[pulumi.Input[FloorsettingFloorSettingMetadataArgs]]: ...
    @floor_setting_metadata.setter
    def floor_setting_metadata(
        self, value: Optional[pulumi.Input[FloorsettingFloorSettingMetadataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleMcpServerFloorSetting")
    def google_mcp_server_floor_setting(
        self,
    ) -> Optional[pulumi.Input[FloorsettingGoogleMcpServerFloorSettingArgs]]: ...
    @google_mcp_server_floor_setting.setter
    def google_mcp_server_floor_setting(
        self, value: Optional[pulumi.Input[FloorsettingGoogleMcpServerFloorSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="integratedServices")
    def integrated_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @integrated_services.setter
    def integrated_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:modelarmor/floorsetting:Floorsetting")
class Floorsetting(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ai_platform_floor_setting: Optional[
            pulumi.Input[
                Union[
                    FloorsettingAiPlatformFloorSettingArgs,
                    FloorsettingAiPlatformFloorSettingArgsDict,
                ]
            ]
        ] = ...,
        enable_floor_setting_enforcement: Optional[pulumi.Input[_builtins.bool]] = ...,
        filter_config: Optional[
            pulumi.Input[
                Union[FloorsettingFilterConfigArgs, FloorsettingFilterConfigArgsDict]
            ]
        ] = ...,
        floor_setting_metadata: Optional[
            pulumi.Input[
                Union[
                    FloorsettingFloorSettingMetadataArgs,
                    FloorsettingFloorSettingMetadataArgsDict,
                ]
            ]
        ] = ...,
        google_mcp_server_floor_setting: Optional[
            pulumi.Input[
                Union[
                    FloorsettingGoogleMcpServerFloorSettingArgs,
                    FloorsettingGoogleMcpServerFloorSettingArgsDict,
                ]
            ]
        ] = ...,
        integrated_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FloorsettingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        ai_platform_floor_setting: Optional[
            pulumi.Input[
                Union[
                    FloorsettingAiPlatformFloorSettingArgs,
                    FloorsettingAiPlatformFloorSettingArgsDict,
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_floor_setting_enforcement: Optional[pulumi.Input[_builtins.bool]] = ...,
        filter_config: Optional[
            pulumi.Input[
                Union[FloorsettingFilterConfigArgs, FloorsettingFilterConfigArgsDict]
            ]
        ] = ...,
        floor_setting_metadata: Optional[
            pulumi.Input[
                Union[
                    FloorsettingFloorSettingMetadataArgs,
                    FloorsettingFloorSettingMetadataArgsDict,
                ]
            ]
        ] = ...,
        google_mcp_server_floor_setting: Optional[
            pulumi.Input[
                Union[
                    FloorsettingGoogleMcpServerFloorSettingArgs,
                    FloorsettingGoogleMcpServerFloorSettingArgsDict,
                ]
            ]
        ] = ...,
        integrated_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Floorsetting: ...
    @_builtins.property
    @pulumi.getter(name="aiPlatformFloorSetting")
    def ai_platform_floor_setting(
        self,
    ) -> pulumi.Output[Optional[outputs.FloorsettingAiPlatformFloorSetting]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableFloorSettingEnforcement")
    def enable_floor_setting_enforcement(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="filterConfig")
    def filter_config(self) -> pulumi.Output[outputs.FloorsettingFilterConfig]: ...
    @_builtins.property
    @pulumi.getter(name="floorSettingMetadata")
    def floor_setting_metadata(
        self,
    ) -> pulumi.Output[Optional[outputs.FloorsettingFloorSettingMetadata]]: ...
    @_builtins.property
    @pulumi.getter(name="googleMcpServerFloorSetting")
    def google_mcp_server_floor_setting(
        self,
    ) -> pulumi.Output[Optional[outputs.FloorsettingGoogleMcpServerFloorSetting]]: ...
    @_builtins.property
    @pulumi.getter(name="integratedServices")
    def integrated_services(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
