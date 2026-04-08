import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UpdateSummaryArgs", "UpdateSummary"]

@pulumi.input_type
class UpdateSummaryArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        current_oem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        current_sbe_version: Optional[pulumi.Input[_builtins.str]] = ...,
        current_version: Optional[pulumi.Input[_builtins.str]] = ...,
        hardware_model: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_date: Optional[pulumi.Input[_builtins.str]] = ...,
        last_checked: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        oem_family: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[
            pulumi.Input[Union[_builtins.str, UpdateSummariesPropertiesState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="currentOemVersion")
    def current_oem_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @current_oem_version.setter
    def current_oem_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="currentSbeVersion")
    def current_sbe_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @current_sbe_version.setter
    def current_sbe_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @current_version.setter
    def current_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hardwareModel")
    def hardware_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hardware_model.setter
    def hardware_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_date.setter
    def health_check_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_checked.setter
    def last_checked(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oemFamily")
    def oem_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oem_family.setter
    def oem_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, UpdateSummariesPropertiesState]]
    ]: ...
    @state.setter
    def state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, UpdateSummariesPropertiesState]]
        ],
    ): ...

@pulumi.type_token("azure-native:azurestackhci:UpdateSummary")
class UpdateSummary(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        current_oem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        current_sbe_version: Optional[pulumi.Input[_builtins.str]] = ...,
        current_version: Optional[pulumi.Input[_builtins.str]] = ...,
        hardware_model: Optional[pulumi.Input[_builtins.str]] = ...,
        health_check_date: Optional[pulumi.Input[_builtins.str]] = ...,
        last_checked: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        oem_family: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[
            pulumi.Input[Union[_builtins.str, UpdateSummariesPropertiesState]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UpdateSummaryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> UpdateSummary: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentOemVersion")
    def current_oem_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="currentSbeVersion")
    def current_sbe_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareModel")
    def hardware_model(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oemFamily")
    def oem_family(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
