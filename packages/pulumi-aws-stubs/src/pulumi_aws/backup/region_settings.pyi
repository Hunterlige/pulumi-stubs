import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegionSettingsArgs", "RegionSettings"]

@pulumi.input_type
class RegionSettingsArgs:
    def __init__(
        __self__,
        *,
        resource_type_opt_in_preference: pulumi.Input[
            Mapping[str, pulumi.Input[_builtins.bool]]
        ],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type_management_preference: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeOptInPreference")
    def resource_type_opt_in_preference(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]: ...
    @resource_type_opt_in_preference.setter
    def resource_type_opt_in_preference(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeManagementPreference")
    def resource_type_management_preference(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]: ...
    @resource_type_management_preference.setter
    def resource_type_management_preference(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]
    ): ...

@pulumi.input_type
class _RegionSettingsState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type_management_preference: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]
        ] = ...,
        resource_type_opt_in_preference: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeManagementPreference")
    def resource_type_management_preference(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]: ...
    @resource_type_management_preference.setter
    def resource_type_management_preference(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeOptInPreference")
    def resource_type_opt_in_preference(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]: ...
    @resource_type_opt_in_preference.setter
    def resource_type_opt_in_preference(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]
    ): ...

@pulumi.type_token("aws:backup/regionSettings:RegionSettings")
class RegionSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type_management_preference: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]
        ] = ...,
        resource_type_opt_in_preference: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RegionSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type_management_preference: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]
        ] = ...,
        resource_type_opt_in_preference: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]
        ] = ...,
    ) -> RegionSettings: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeManagementPreference")
    def resource_type_management_preference(
        self,
    ) -> pulumi.Output[Mapping[str, _builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeOptInPreference")
    def resource_type_opt_in_preference(
        self,
    ) -> pulumi.Output[Mapping[str, _builtins.bool]]: ...
