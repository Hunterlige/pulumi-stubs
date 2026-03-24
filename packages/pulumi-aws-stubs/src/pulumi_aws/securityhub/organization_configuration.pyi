import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OrganizationConfigurationArgs", "OrganizationConfiguration"]

@pulumi.input_type
class OrganizationConfigurationArgs:
    def __init__(
        __self__,
        *,
        auto_enable: pulumi.Input[_builtins.bool],
        auto_enable_standards: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_configuration: Optional[
            pulumi.Input[OrganizationConfigurationOrganizationConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Input[_builtins.bool]: ...
    @auto_enable.setter
    def auto_enable(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="autoEnableStandards")
    def auto_enable_standards(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_enable_standards.setter
    def auto_enable_standards(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationConfiguration")
    def organization_configuration(
        self,
    ) -> Optional[
        pulumi.Input[OrganizationConfigurationOrganizationConfigurationArgs]
    ]: ...
    @organization_configuration.setter
    def organization_configuration(
        self,
        value: Optional[
            pulumi.Input[OrganizationConfigurationOrganizationConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _OrganizationConfigurationState:
    def __init__(
        __self__,
        *,
        auto_enable: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_enable_standards: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_configuration: Optional[
            pulumi.Input[OrganizationConfigurationOrganizationConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_enable.setter
    def auto_enable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoEnableStandards")
    def auto_enable_standards(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_enable_standards.setter
    def auto_enable_standards(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationConfiguration")
    def organization_configuration(
        self,
    ) -> Optional[
        pulumi.Input[OrganizationConfigurationOrganizationConfigurationArgs]
    ]: ...
    @organization_configuration.setter
    def organization_configuration(
        self,
        value: Optional[
            pulumi.Input[OrganizationConfigurationOrganizationConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class OrganizationConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_enable: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_enable_standards: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_configuration: Optional[
            pulumi.Input[
                Union[
                    OrganizationConfigurationOrganizationConfigurationArgs,
                    OrganizationConfigurationOrganizationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OrganizationConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_enable: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_enable_standards: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_configuration: Optional[
            pulumi.Input[
                Union[
                    OrganizationConfigurationOrganizationConfigurationArgs,
                    OrganizationConfigurationOrganizationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OrganizationConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autoEnableStandards")
    def auto_enable_standards(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationConfiguration")
    def organization_configuration(
        self,
    ) -> pulumi.Output[outputs.OrganizationConfigurationOrganizationConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
