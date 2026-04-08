import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HypervHostControllerArgs", "HypervHostController"]

@pulumi.input_type
class HypervHostControllerArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        site_name: pulumi.Input[_builtins.str],
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
        run_as_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[_builtins.str]: ...
    @site_name.setter
    def site_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:offazure:HypervHostController")
class HypervHostController(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        run_as_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        site_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HypervHostControllerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> HypervHostController: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[outputs.HealthErrorDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
