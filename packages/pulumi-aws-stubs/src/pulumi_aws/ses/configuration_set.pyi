import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConfigurationSetArgs", "ConfigurationSet"]

@pulumi.input_type
class ConfigurationSetArgs:
    def __init__(
        __self__,
        *,
        delivery_options: Optional[
            pulumi.Input[ConfigurationSetDeliveryOptionsArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reputation_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sending_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tracking_options: Optional[
            pulumi.Input[ConfigurationSetTrackingOptionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetDeliveryOptionsArgs]]: ...
    @delivery_options.setter
    def delivery_options(
        self, value: Optional[pulumi.Input[ConfigurationSetDeliveryOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reputationMetricsEnabled")
    def reputation_metrics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reputation_metrics_enabled.setter
    def reputation_metrics_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sendingEnabled")
    def sending_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sending_enabled.setter
    def sending_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetTrackingOptionsArgs]]: ...
    @tracking_options.setter
    def tracking_options(
        self, value: Optional[pulumi.Input[ConfigurationSetTrackingOptionsArgs]]
    ): ...

@pulumi.input_type
class _ConfigurationSetState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_options: Optional[
            pulumi.Input[ConfigurationSetDeliveryOptionsArgs]
        ] = ...,
        last_fresh_start: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reputation_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sending_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tracking_options: Optional[
            pulumi.Input[ConfigurationSetTrackingOptionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetDeliveryOptionsArgs]]: ...
    @delivery_options.setter
    def delivery_options(
        self, value: Optional[pulumi.Input[ConfigurationSetDeliveryOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastFreshStart")
    def last_fresh_start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_fresh_start.setter
    def last_fresh_start(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reputationMetricsEnabled")
    def reputation_metrics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reputation_metrics_enabled.setter
    def reputation_metrics_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sendingEnabled")
    def sending_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sending_enabled.setter
    def sending_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetTrackingOptionsArgs]]: ...
    @tracking_options.setter
    def tracking_options(
        self, value: Optional[pulumi.Input[ConfigurationSetTrackingOptionsArgs]]
    ): ...

@pulumi.type_token("aws:ses/configurationSet:ConfigurationSet")
class ConfigurationSet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        delivery_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetDeliveryOptionsArgs,
                    ConfigurationSetDeliveryOptionsArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reputation_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sending_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tracking_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetTrackingOptionsArgs,
                    ConfigurationSetTrackingOptionsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ConfigurationSetArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetDeliveryOptionsArgs,
                    ConfigurationSetDeliveryOptionsArgsDict,
                ]
            ]
        ] = ...,
        last_fresh_start: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reputation_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sending_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tracking_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetTrackingOptionsArgs,
                    ConfigurationSetTrackingOptionsArgsDict,
                ]
            ]
        ] = ...,
    ) -> ConfigurationSet: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigurationSetDeliveryOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="lastFreshStart")
    def last_fresh_start(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reputationMetricsEnabled")
    def reputation_metrics_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="sendingEnabled")
    def sending_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigurationSetTrackingOptions]]: ...
