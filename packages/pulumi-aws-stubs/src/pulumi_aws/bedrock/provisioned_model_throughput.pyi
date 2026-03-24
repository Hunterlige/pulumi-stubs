import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProvisionedModelThroughputArgs", "ProvisionedModelThroughput"]

@pulumi.input_type
class ProvisionedModelThroughputArgs:
    def __init__(
        __self__,
        *,
        model_arn: pulumi.Input[_builtins.str],
        model_units: pulumi.Input[_builtins.int],
        provisioned_model_name: pulumi.Input[_builtins.str],
        commitment_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[ProvisionedModelThroughputTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> pulumi.Input[_builtins.str]: ...
    @model_arn.setter
    def model_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelUnits")
    def model_units(self) -> pulumi.Input[_builtins.int]: ...
    @model_units.setter
    def model_units(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedModelName")
    def provisioned_model_name(self) -> pulumi.Input[_builtins.str]: ...
    @provisioned_model_name.setter
    def provisioned_model_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="commitmentDuration")
    def commitment_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commitment_duration.setter
    def commitment_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[ProvisionedModelThroughputTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[ProvisionedModelThroughputTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _ProvisionedModelThroughputState:
    def __init__(
        __self__,
        *,
        commitment_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        model_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        model_units: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_model_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[ProvisionedModelThroughputTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commitmentDuration")
    def commitment_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commitment_duration.setter
    def commitment_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_arn.setter
    def model_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelUnits")
    def model_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @model_units.setter
    def model_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedModelArn")
    def provisioned_model_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioned_model_arn.setter
    def provisioned_model_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedModelName")
    def provisioned_model_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioned_model_name.setter
    def provisioned_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[ProvisionedModelThroughputTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[ProvisionedModelThroughputTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class ProvisionedModelThroughput(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        commitment_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        model_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        model_units: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ProvisionedModelThroughputTimeoutsArgs,
                    ProvisionedModelThroughputTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProvisionedModelThroughputArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        commitment_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        model_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        model_units: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_model_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ProvisionedModelThroughputTimeoutsArgs,
                    ProvisionedModelThroughputTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> ProvisionedModelThroughput: ...
    @_builtins.property
    @pulumi.getter(name="commitmentDuration")
    def commitment_duration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelUnits")
    def model_units(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedModelArn")
    def provisioned_model_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedModelName")
    def provisioned_model_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.ProvisionedModelThroughputTimeouts]]: ...
