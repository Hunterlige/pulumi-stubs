import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountVdmAttributesArgs", "AccountVdmAttributes"]

@pulumi.input_type
class AccountVdmAttributesArgs:
    def __init__(
        __self__,
        *,
        vdm_enabled: pulumi.Input[_builtins.str],
        dashboard_attributes: Optional[
            pulumi.Input[AccountVdmAttributesDashboardAttributesArgs]
        ] = ...,
        guardian_attributes: Optional[
            pulumi.Input[AccountVdmAttributesGuardianAttributesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vdmEnabled")
    def vdm_enabled(self) -> pulumi.Input[_builtins.str]: ...
    @vdm_enabled.setter
    def vdm_enabled(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dashboardAttributes")
    def dashboard_attributes(
        self,
    ) -> Optional[pulumi.Input[AccountVdmAttributesDashboardAttributesArgs]]: ...
    @dashboard_attributes.setter
    def dashboard_attributes(
        self, value: Optional[pulumi.Input[AccountVdmAttributesDashboardAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="guardianAttributes")
    def guardian_attributes(
        self,
    ) -> Optional[pulumi.Input[AccountVdmAttributesGuardianAttributesArgs]]: ...
    @guardian_attributes.setter
    def guardian_attributes(
        self, value: Optional[pulumi.Input[AccountVdmAttributesGuardianAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AccountVdmAttributesState:
    def __init__(
        __self__,
        *,
        dashboard_attributes: Optional[
            pulumi.Input[AccountVdmAttributesDashboardAttributesArgs]
        ] = ...,
        guardian_attributes: Optional[
            pulumi.Input[AccountVdmAttributesGuardianAttributesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vdm_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dashboardAttributes")
    def dashboard_attributes(
        self,
    ) -> Optional[pulumi.Input[AccountVdmAttributesDashboardAttributesArgs]]: ...
    @dashboard_attributes.setter
    def dashboard_attributes(
        self, value: Optional[pulumi.Input[AccountVdmAttributesDashboardAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="guardianAttributes")
    def guardian_attributes(
        self,
    ) -> Optional[pulumi.Input[AccountVdmAttributesGuardianAttributesArgs]]: ...
    @guardian_attributes.setter
    def guardian_attributes(
        self, value: Optional[pulumi.Input[AccountVdmAttributesGuardianAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vdmEnabled")
    def vdm_enabled(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vdm_enabled.setter
    def vdm_enabled(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class AccountVdmAttributes(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dashboard_attributes: Optional[
            pulumi.Input[
                Union[
                    AccountVdmAttributesDashboardAttributesArgs,
                    AccountVdmAttributesDashboardAttributesArgsDict,
                ]
            ]
        ] = ...,
        guardian_attributes: Optional[
            pulumi.Input[
                Union[
                    AccountVdmAttributesGuardianAttributesArgs,
                    AccountVdmAttributesGuardianAttributesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vdm_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccountVdmAttributesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        dashboard_attributes: Optional[
            pulumi.Input[
                Union[
                    AccountVdmAttributesDashboardAttributesArgs,
                    AccountVdmAttributesDashboardAttributesArgsDict,
                ]
            ]
        ] = ...,
        guardian_attributes: Optional[
            pulumi.Input[
                Union[
                    AccountVdmAttributesGuardianAttributesArgs,
                    AccountVdmAttributesGuardianAttributesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vdm_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AccountVdmAttributes: ...
    @_builtins.property
    @pulumi.getter(name="dashboardAttributes")
    def dashboard_attributes(
        self,
    ) -> pulumi.Output[outputs.AccountVdmAttributesDashboardAttributes]: ...
    @_builtins.property
    @pulumi.getter(name="guardianAttributes")
    def guardian_attributes(
        self,
    ) -> pulumi.Output[outputs.AccountVdmAttributesGuardianAttributes]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vdmEnabled")
    def vdm_enabled(self) -> pulumi.Output[_builtins.str]: ...
