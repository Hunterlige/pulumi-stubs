import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StreamArgs", "Stream"]

@pulumi.input_type
class StreamArgs:
    def __init__(
        __self__,
        *,
        destination_config: pulumi.Input[StreamDestinationConfigArgs],
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        source_config: pulumi.Input[StreamSourceConfigArgs],
        stream_id: pulumi.Input[_builtins.str],
        backfill_all: Optional[pulumi.Input[StreamBackfillAllArgs]] = ...,
        backfill_none: Optional[pulumi.Input[StreamBackfillNoneArgs]] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        customer_managed_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_sets: Optional[
            pulumi.Input[Sequence[pulumi.Input[StreamRuleSetArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> pulumi.Input[StreamDestinationConfigArgs]: ...
    @destination_config.setter
    def destination_config(self, value: pulumi.Input[StreamDestinationConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfig")
    def source_config(self) -> pulumi.Input[StreamSourceConfigArgs]: ...
    @source_config.setter
    def source_config(self, value: pulumi.Input[StreamSourceConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="streamId")
    def stream_id(self) -> pulumi.Input[_builtins.str]: ...
    @stream_id.setter
    def stream_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backfillAll")
    def backfill_all(self) -> Optional[pulumi.Input[StreamBackfillAllArgs]]: ...
    @backfill_all.setter
    def backfill_all(self, value: Optional[pulumi.Input[StreamBackfillAllArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="backfillNone")
    def backfill_none(self) -> Optional[pulumi.Input[StreamBackfillNoneArgs]]: ...
    @backfill_none.setter
    def backfill_none(self, value: Optional[pulumi.Input[StreamBackfillNoneArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_without_validation.setter
    def create_without_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptionKey")
    def customer_managed_encryption_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_managed_encryption_key.setter
    def customer_managed_encryption_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[StreamRuleSetArgs]]]]: ...
    @rule_sets.setter
    def rule_sets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StreamRuleSetArgs]]]]
    ): ...

@pulumi.input_type
class _StreamState:
    def __init__(
        __self__,
        *,
        backfill_all: Optional[pulumi.Input[StreamBackfillAllArgs]] = ...,
        backfill_none: Optional[pulumi.Input[StreamBackfillNoneArgs]] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        customer_managed_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_config: Optional[pulumi.Input[StreamDestinationConfigArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        rule_sets: Optional[
            pulumi.Input[Sequence[pulumi.Input[StreamRuleSetArgs]]]
        ] = ...,
        source_config: Optional[pulumi.Input[StreamSourceConfigArgs]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backfillAll")
    def backfill_all(self) -> Optional[pulumi.Input[StreamBackfillAllArgs]]: ...
    @backfill_all.setter
    def backfill_all(self, value: Optional[pulumi.Input[StreamBackfillAllArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="backfillNone")
    def backfill_none(self) -> Optional[pulumi.Input[StreamBackfillNoneArgs]]: ...
    @backfill_none.setter
    def backfill_none(self, value: Optional[pulumi.Input[StreamBackfillNoneArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_without_validation.setter
    def create_without_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptionKey")
    def customer_managed_encryption_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_managed_encryption_key.setter
    def customer_managed_encryption_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(
        self,
    ) -> Optional[pulumi.Input[StreamDestinationConfigArgs]]: ...
    @destination_config.setter
    def destination_config(
        self, value: Optional[pulumi.Input[StreamDestinationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[StreamRuleSetArgs]]]]: ...
    @rule_sets.setter
    def rule_sets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StreamRuleSetArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfig")
    def source_config(self) -> Optional[pulumi.Input[StreamSourceConfigArgs]]: ...
    @source_config.setter
    def source_config(self, value: Optional[pulumi.Input[StreamSourceConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamId")
    def stream_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_id.setter
    def stream_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:datastream/stream:Stream")
class Stream(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backfill_all: Optional[
            pulumi.Input[Union[StreamBackfillAllArgs, StreamBackfillAllArgsDict]]
        ] = ...,
        backfill_none: Optional[
            pulumi.Input[Union[StreamBackfillNoneArgs, StreamBackfillNoneArgsDict]]
        ] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        customer_managed_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_config: Optional[
            pulumi.Input[
                Union[StreamDestinationConfigArgs, StreamDestinationConfigArgsDict]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_sets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[StreamRuleSetArgs, StreamRuleSetArgsDict]]]
            ]
        ] = ...,
        source_config: Optional[
            pulumi.Input[Union[StreamSourceConfigArgs, StreamSourceConfigArgsDict]]
        ] = ...,
        stream_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StreamArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        backfill_all: Optional[
            pulumi.Input[Union[StreamBackfillAllArgs, StreamBackfillAllArgsDict]]
        ] = ...,
        backfill_none: Optional[
            pulumi.Input[Union[StreamBackfillNoneArgs, StreamBackfillNoneArgsDict]]
        ] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        customer_managed_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_config: Optional[
            pulumi.Input[
                Union[StreamDestinationConfigArgs, StreamDestinationConfigArgsDict]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        rule_sets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[StreamRuleSetArgs, StreamRuleSetArgsDict]]]
            ]
        ] = ...,
        source_config: Optional[
            pulumi.Input[Union[StreamSourceConfigArgs, StreamSourceConfigArgsDict]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Stream: ...
    @_builtins.property
    @pulumi.getter(name="backfillAll")
    def backfill_all(self) -> pulumi.Output[Optional[outputs.StreamBackfillAll]]: ...
    @_builtins.property
    @pulumi.getter(name="backfillNone")
    def backfill_none(self) -> pulumi.Output[Optional[outputs.StreamBackfillNone]]: ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptionKey")
    def customer_managed_encryption_key(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> pulumi.Output[outputs.StreamDestinationConfig]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> pulumi.Output[Optional[Sequence[outputs.StreamRuleSet]]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceConfig")
    def source_config(self) -> pulumi.Output[outputs.StreamSourceConfig]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamId")
    def stream_id(self) -> pulumi.Output[_builtins.str]: ...
