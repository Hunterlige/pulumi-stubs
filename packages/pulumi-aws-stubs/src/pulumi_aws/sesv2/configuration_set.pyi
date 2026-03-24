import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
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
        configuration_set_name: pulumi.Input[_builtins.str],
        delivery_options: Optional[
            pulumi.Input[ConfigurationSetDeliveryOptionsArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reputation_options: Optional[
            pulumi.Input[ConfigurationSetReputationOptionsArgs]
        ] = ...,
        sending_options: Optional[
            pulumi.Input[ConfigurationSetSendingOptionsArgs]
        ] = ...,
        suppression_options: Optional[
            pulumi.Input[ConfigurationSetSuppressionOptionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tracking_options: Optional[
            pulumi.Input[ConfigurationSetTrackingOptionsArgs]
        ] = ...,
        vdm_options: Optional[pulumi.Input[ConfigurationSetVdmOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_set_name.setter
    def configuration_set_name(self, value: pulumi.Input[_builtins.str]): ...
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetReputationOptionsArgs]]: ...
    @reputation_options.setter
    def reputation_options(
        self, value: Optional[pulumi.Input[ConfigurationSetReputationOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sendingOptions")
    def sending_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetSendingOptionsArgs]]: ...
    @sending_options.setter
    def sending_options(
        self, value: Optional[pulumi.Input[ConfigurationSetSendingOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="suppressionOptions")
    def suppression_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetSuppressionOptionsArgs]]: ...
    @suppression_options.setter
    def suppression_options(
        self, value: Optional[pulumi.Input[ConfigurationSetSuppressionOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetTrackingOptionsArgs]]: ...
    @tracking_options.setter
    def tracking_options(
        self, value: Optional[pulumi.Input[ConfigurationSetTrackingOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vdmOptions")
    def vdm_options(self) -> Optional[pulumi.Input[ConfigurationSetVdmOptionsArgs]]: ...
    @vdm_options.setter
    def vdm_options(
        self, value: Optional[pulumi.Input[ConfigurationSetVdmOptionsArgs]]
    ): ...

@pulumi.input_type
class _ConfigurationSetState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_options: Optional[
            pulumi.Input[ConfigurationSetDeliveryOptionsArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reputation_options: Optional[
            pulumi.Input[ConfigurationSetReputationOptionsArgs]
        ] = ...,
        sending_options: Optional[
            pulumi.Input[ConfigurationSetSendingOptionsArgs]
        ] = ...,
        suppression_options: Optional[
            pulumi.Input[ConfigurationSetSuppressionOptionsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tracking_options: Optional[
            pulumi.Input[ConfigurationSetTrackingOptionsArgs]
        ] = ...,
        vdm_options: Optional[pulumi.Input[ConfigurationSetVdmOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_set_name.setter
    def configuration_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetReputationOptionsArgs]]: ...
    @reputation_options.setter
    def reputation_options(
        self, value: Optional[pulumi.Input[ConfigurationSetReputationOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sendingOptions")
    def sending_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetSendingOptionsArgs]]: ...
    @sending_options.setter
    def sending_options(
        self, value: Optional[pulumi.Input[ConfigurationSetSendingOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="suppressionOptions")
    def suppression_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetSuppressionOptionsArgs]]: ...
    @suppression_options.setter
    def suppression_options(
        self, value: Optional[pulumi.Input[ConfigurationSetSuppressionOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(
        self,
    ) -> Optional[pulumi.Input[ConfigurationSetTrackingOptionsArgs]]: ...
    @tracking_options.setter
    def tracking_options(
        self, value: Optional[pulumi.Input[ConfigurationSetTrackingOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vdmOptions")
    def vdm_options(self) -> Optional[pulumi.Input[ConfigurationSetVdmOptionsArgs]]: ...
    @vdm_options.setter
    def vdm_options(
        self, value: Optional[pulumi.Input[ConfigurationSetVdmOptionsArgs]]
    ): ...

@pulumi.type_token("aws:sesv2/configurationSet:ConfigurationSet")
class ConfigurationSet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetDeliveryOptionsArgs,
                    ConfigurationSetDeliveryOptionsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reputation_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetReputationOptionsArgs,
                    ConfigurationSetReputationOptionsArgsDict,
                ]
            ]
        ] = ...,
        sending_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetSendingOptionsArgs,
                    ConfigurationSetSendingOptionsArgsDict,
                ]
            ]
        ] = ...,
        suppression_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetSuppressionOptionsArgs,
                    ConfigurationSetSuppressionOptionsArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tracking_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetTrackingOptionsArgs,
                    ConfigurationSetTrackingOptionsArgsDict,
                ]
            ]
        ] = ...,
        vdm_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetVdmOptionsArgs, ConfigurationSetVdmOptionsArgsDict
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConfigurationSetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetDeliveryOptionsArgs,
                    ConfigurationSetDeliveryOptionsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reputation_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetReputationOptionsArgs,
                    ConfigurationSetReputationOptionsArgsDict,
                ]
            ]
        ] = ...,
        sending_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetSendingOptionsArgs,
                    ConfigurationSetSendingOptionsArgsDict,
                ]
            ]
        ] = ...,
        suppression_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetSuppressionOptionsArgs,
                    ConfigurationSetSuppressionOptionsArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tracking_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetTrackingOptionsArgs,
                    ConfigurationSetTrackingOptionsArgsDict,
                ]
            ]
        ] = ...,
        vdm_options: Optional[
            pulumi.Input[
                Union[
                    ConfigurationSetVdmOptionsArgs, ConfigurationSetVdmOptionsArgsDict
                ]
            ]
        ] = ...,
    ) -> ConfigurationSet: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigurationSetDeliveryOptions]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(
        self,
    ) -> pulumi.Output[outputs.ConfigurationSetReputationOptions]: ...
    @_builtins.property
    @pulumi.getter(name="sendingOptions")
    def sending_options(
        self,
    ) -> pulumi.Output[outputs.ConfigurationSetSendingOptions]: ...
    @_builtins.property
    @pulumi.getter(name="suppressionOptions")
    def suppression_options(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigurationSetSuppressionOptions]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigurationSetTrackingOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="vdmOptions")
    def vdm_options(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigurationSetVdmOptions]]: ...
