import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ...]

@pulumi.input_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleArgs:
    def __init__(
        __self__,
        *,
        organization: pulumi.Input[_builtins.str],
        custom_config: Optional[
            pulumi.Input[
                ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enablement_state: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]: ...
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customConfig")
    def custom_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs
        ]
    ]: ...
    @custom_config.setter
    def custom_config(
        self,
        value: Optional[
            pulumi.Input[
                ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enablement_state.setter
    def enablement_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ManagementOrganizationSecurityHealthAnalyticsCustomModuleState:
    def __init__(
        __self__,
        *,
        ancestor_module: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_config: Optional[
            pulumi.Input[
                ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enablement_state: Optional[pulumi.Input[_builtins.str]] = ...,
        last_editor: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ancestorModule")
    def ancestor_module(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ancestor_module.setter
    def ancestor_module(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customConfig")
    def custom_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs
        ]
    ]: ...
    @custom_config.setter
    def custom_config(
        self,
        value: Optional[
            pulumi.Input[
                ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enablement_state.setter
    def enablement_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastEditor")
    def last_editor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_editor.setter
    def last_editor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ManagementOrganizationSecurityHealthAnalyticsCustomModule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        custom_config: Optional[
            pulumi.Input[
                Union[
                    ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs,
                    ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgsDict,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enablement_state: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagementOrganizationSecurityHealthAnalyticsCustomModuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        ancestor_module: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_config: Optional[
            pulumi.Input[
                Union[
                    ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs,
                    ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgsDict,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enablement_state: Optional[pulumi.Input[_builtins.str]] = ...,
        last_editor: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ManagementOrganizationSecurityHealthAnalyticsCustomModule: ...
    @_builtins.property
    @pulumi.getter(name="ancestorModule")
    def ancestor_module(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customConfig")
    def custom_config(
        self,
    ) -> pulumi.Output[
        Optional[
            outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfig
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastEditor")
    def last_editor(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
