import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ComponentCurrentBillingFeatureArgs", "ComponentCurrentBillingFeature"]

@pulumi.input_type
class ComponentCurrentBillingFeatureArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        current_billing_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        data_volume_cap: Optional[
            pulumi.Input[ApplicationInsightsComponentDataVolumeCapArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="currentBillingFeatures")
    def current_billing_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @current_billing_features.setter
    def current_billing_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataVolumeCap")
    def data_volume_cap(
        self,
    ) -> Optional[pulumi.Input[ApplicationInsightsComponentDataVolumeCapArgs]]: ...
    @data_volume_cap.setter
    def data_volume_cap(
        self,
        value: Optional[pulumi.Input[ApplicationInsightsComponentDataVolumeCapArgs]],
    ): ...

@pulumi.type_token(...)
class ComponentCurrentBillingFeature(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        current_billing_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        data_volume_cap: Optional[
            pulumi.Input[
                Union[
                    ApplicationInsightsComponentDataVolumeCapArgs,
                    ApplicationInsightsComponentDataVolumeCapArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ComponentCurrentBillingFeatureArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ComponentCurrentBillingFeature: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentBillingFeatures")
    def current_billing_features(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="dataVolumeCap")
    def data_volume_cap(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ApplicationInsightsComponentDataVolumeCapResponse]
    ]: ...
