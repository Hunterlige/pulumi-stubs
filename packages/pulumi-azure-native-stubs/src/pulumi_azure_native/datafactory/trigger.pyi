import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TriggerArgs", "Trigger"]

@pulumi.input_type
class TriggerArgs:
    def __init__(
        __self__,
        *,
        factory_name: pulumi.Input[_builtins.str],
        properties: pulumi.Input[
            Union[
                BlobEventsTriggerArgs,
                BlobTriggerArgs,
                ChainingTriggerArgs,
                CustomEventsTriggerArgs,
                MultiplePipelineTriggerArgs,
                RerunTumblingWindowTriggerArgs,
                ScheduleTriggerArgs,
                TumblingWindowTriggerArgs,
            ]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        trigger_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[_builtins.str]: ...
    @factory_name.setter
    def factory_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Input[
        Union[
            BlobEventsTriggerArgs,
            BlobTriggerArgs,
            ChainingTriggerArgs,
            CustomEventsTriggerArgs,
            MultiplePipelineTriggerArgs,
            RerunTumblingWindowTriggerArgs,
            ScheduleTriggerArgs,
            TumblingWindowTriggerArgs,
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: pulumi.Input[
            Union[
                BlobEventsTriggerArgs,
                BlobTriggerArgs,
                ChainingTriggerArgs,
                CustomEventsTriggerArgs,
                MultiplePipelineTriggerArgs,
                RerunTumblingWindowTriggerArgs,
                ScheduleTriggerArgs,
                TumblingWindowTriggerArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_name.setter
    def trigger_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:datafactory:Trigger")
class Trigger(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    Union[BlobEventsTriggerArgs, BlobEventsTriggerArgsDict],
                    Union[BlobTriggerArgs, BlobTriggerArgsDict],
                    Union[ChainingTriggerArgs, ChainingTriggerArgsDict],
                    Union[CustomEventsTriggerArgs, CustomEventsTriggerArgsDict],
                    Union[MultiplePipelineTriggerArgs, MultiplePipelineTriggerArgsDict],
                    Union[
                        RerunTumblingWindowTriggerArgs,
                        RerunTumblingWindowTriggerArgsDict,
                    ],
                    Union[ScheduleTriggerArgs, ScheduleTriggerArgsDict],
                    Union[TumblingWindowTriggerArgs, TumblingWindowTriggerArgsDict],
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TriggerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Trigger: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
