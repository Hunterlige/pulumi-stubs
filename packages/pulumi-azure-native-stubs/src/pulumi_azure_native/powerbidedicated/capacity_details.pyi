import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CapacityDetailsArgs", "CapacityDetails"]

@pulumi.input_type
class CapacityDetailsArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[CapacitySkuArgs],
        administration: Optional[
            pulumi.Input[DedicatedCapacityAdministratorsArgs]
        ] = ...,
        dedicated_capacity_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, Mode]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[CapacitySkuArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[CapacitySkuArgs]): ...
    @_builtins.property
    @pulumi.getter
    def administration(
        self,
    ) -> Optional[pulumi.Input[DedicatedCapacityAdministratorsArgs]]: ...
    @administration.setter
    def administration(
        self, value: Optional[pulumi.Input[DedicatedCapacityAdministratorsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedCapacityName")
    def dedicated_capacity_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dedicated_capacity_name.setter
    def dedicated_capacity_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, Mode]]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, Mode]]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:powerbidedicated:CapacityDetails")
class CapacityDetails(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        administration: Optional[
            pulumi.Input[
                Union[
                    DedicatedCapacityAdministratorsArgs,
                    DedicatedCapacityAdministratorsArgsDict,
                ]
            ]
        ] = ...,
        dedicated_capacity_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, Mode]]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[CapacitySkuArgs, CapacitySkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CapacityDetailsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CapacityDetails: ...
    @_builtins.property
    @pulumi.getter
    def administration(
        self,
    ) -> pulumi.Output[Optional[outputs.DedicatedCapacityAdministratorsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.CapacitySkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
