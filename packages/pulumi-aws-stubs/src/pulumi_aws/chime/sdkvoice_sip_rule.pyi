import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SdkvoiceSipRuleArgs", "SdkvoiceSipRule"]

@pulumi.input_type
class SdkvoiceSipRuleArgs:
    def __init__(
        __self__,
        *,
        target_applications: pulumi.Input[
            Sequence[pulumi.Input[SdkvoiceSipRuleTargetApplicationArgs]]
        ],
        trigger_type: pulumi.Input[_builtins.str],
        trigger_value: pulumi.Input[_builtins.str],
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetApplications")
    def target_applications(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[SdkvoiceSipRuleTargetApplicationArgs]]]: ...
    @target_applications.setter
    def target_applications(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[SdkvoiceSipRuleTargetApplicationArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_type.setter
    def trigger_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="triggerValue")
    def trigger_value(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_value.setter
    def trigger_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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

@pulumi.input_type
class _SdkvoiceSipRuleState:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[SdkvoiceSipRuleTargetApplicationArgs]]]
        ] = ...,
        trigger_type: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="targetApplications")
    def target_applications(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SdkvoiceSipRuleTargetApplicationArgs]]]
    ]: ...
    @target_applications.setter
    def target_applications(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SdkvoiceSipRuleTargetApplicationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_type.setter
    def trigger_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerValue")
    def trigger_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_value.setter
    def trigger_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:chime/sdkvoiceSipRule:SdkvoiceSipRule")
class SdkvoiceSipRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_applications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SdkvoiceSipRuleTargetApplicationArgs,
                            SdkvoiceSipRuleTargetApplicationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        trigger_type: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_value: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SdkvoiceSipRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_applications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SdkvoiceSipRuleTargetApplicationArgs,
                            SdkvoiceSipRuleTargetApplicationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        trigger_type: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SdkvoiceSipRule: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetApplications")
    def target_applications(
        self,
    ) -> pulumi.Output[Sequence[outputs.SdkvoiceSipRuleTargetApplication]]: ...
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerValue")
    def trigger_value(self) -> pulumi.Output[_builtins.str]: ...
