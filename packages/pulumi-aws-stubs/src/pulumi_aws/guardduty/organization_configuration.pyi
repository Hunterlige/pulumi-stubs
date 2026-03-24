import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from .. import _utilities
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
        auto_enable_organization_members: pulumi.Input[_builtins.str],
        detector_id: pulumi.Input[_builtins.str],
        datasources: Optional[
            pulumi.Input[OrganizationConfigurationDatasourcesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnableOrganizationMembers")
    def auto_enable_organization_members(self) -> pulumi.Input[_builtins.str]: ...
    @auto_enable_organization_members.setter
    def auto_enable_organization_members(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Input[_builtins.str]: ...
    @detector_id.setter
    def detector_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def datasources(
        self,
    ) -> Optional[pulumi.Input[OrganizationConfigurationDatasourcesArgs]]: ...
    @datasources.setter
    def datasources(
        self, value: Optional[pulumi.Input[OrganizationConfigurationDatasourcesArgs]]
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
        auto_enable_organization_members: Optional[pulumi.Input[_builtins.str]] = ...,
        datasources: Optional[
            pulumi.Input[OrganizationConfigurationDatasourcesArgs]
        ] = ...,
        detector_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnableOrganizationMembers")
    def auto_enable_organization_members(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_enable_organization_members.setter
    def auto_enable_organization_members(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def datasources(
        self,
    ) -> Optional[pulumi.Input[OrganizationConfigurationDatasourcesArgs]]: ...
    @datasources.setter
    def datasources(
        self, value: Optional[pulumi.Input[OrganizationConfigurationDatasourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detector_id.setter
    def detector_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
        auto_enable_organization_members: Optional[pulumi.Input[_builtins.str]] = ...,
        datasources: Optional[
            pulumi.Input[
                Union[
                    OrganizationConfigurationDatasourcesArgs,
                    OrganizationConfigurationDatasourcesArgsDict,
                ]
            ]
        ] = ...,
        detector_id: Optional[pulumi.Input[_builtins.str]] = ...,
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
        auto_enable_organization_members: Optional[pulumi.Input[_builtins.str]] = ...,
        datasources: Optional[
            pulumi.Input[
                Union[
                    OrganizationConfigurationDatasourcesArgs,
                    OrganizationConfigurationDatasourcesArgsDict,
                ]
            ]
        ] = ...,
        detector_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OrganizationConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="autoEnableOrganizationMembers")
    def auto_enable_organization_members(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def datasources(
        self,
    ) -> pulumi.Output[outputs.OrganizationConfigurationDatasources]: ...
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
