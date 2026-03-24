import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkProfileArgs", "NetworkProfile"]

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(
        __self__,
        *,
        project_arn: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        downlink_bandwidth_bits: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_jitter_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_loss_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uplink_bandwidth_bits: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_jitter_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_loss_percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectArn")
    def project_arn(self) -> pulumi.Input[_builtins.str]: ...
    @project_arn.setter
    def project_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="downlinkBandwidthBits")
    def downlink_bandwidth_bits(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @downlink_bandwidth_bits.setter
    def downlink_bandwidth_bits(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="downlinkDelayMs")
    def downlink_delay_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @downlink_delay_ms.setter
    def downlink_delay_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="downlinkJitterMs")
    def downlink_jitter_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @downlink_jitter_ms.setter
    def downlink_jitter_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="downlinkLossPercent")
    def downlink_loss_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @downlink_loss_percent.setter
    def downlink_loss_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uplinkBandwidthBits")
    def uplink_bandwidth_bits(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uplink_bandwidth_bits.setter
    def uplink_bandwidth_bits(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="uplinkDelayMs")
    def uplink_delay_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uplink_delay_ms.setter
    def uplink_delay_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="uplinkJitterMs")
    def uplink_jitter_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uplink_jitter_ms.setter
    def uplink_jitter_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="uplinkLossPercent")
    def uplink_loss_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uplink_loss_percent.setter
    def uplink_loss_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _NetworkProfileState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        downlink_bandwidth_bits: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_jitter_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_loss_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uplink_bandwidth_bits: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_jitter_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_loss_percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="downlinkBandwidthBits")
    def downlink_bandwidth_bits(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @downlink_bandwidth_bits.setter
    def downlink_bandwidth_bits(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="downlinkDelayMs")
    def downlink_delay_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @downlink_delay_ms.setter
    def downlink_delay_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="downlinkJitterMs")
    def downlink_jitter_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @downlink_jitter_ms.setter
    def downlink_jitter_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="downlinkLossPercent")
    def downlink_loss_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @downlink_loss_percent.setter
    def downlink_loss_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectArn")
    def project_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_arn.setter
    def project_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uplinkBandwidthBits")
    def uplink_bandwidth_bits(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uplink_bandwidth_bits.setter
    def uplink_bandwidth_bits(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="uplinkDelayMs")
    def uplink_delay_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uplink_delay_ms.setter
    def uplink_delay_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="uplinkJitterMs")
    def uplink_jitter_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uplink_jitter_ms.setter
    def uplink_jitter_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="uplinkLossPercent")
    def uplink_loss_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uplink_loss_percent.setter
    def uplink_loss_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("aws:devicefarm/networkProfile:NetworkProfile")
class NetworkProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        downlink_bandwidth_bits: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_jitter_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_loss_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uplink_bandwidth_bits: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_jitter_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_loss_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        downlink_bandwidth_bits: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_jitter_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        downlink_loss_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uplink_bandwidth_bits: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_jitter_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        uplink_loss_percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> NetworkProfile: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="downlinkBandwidthBits")
    def downlink_bandwidth_bits(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="downlinkDelayMs")
    def downlink_delay_ms(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="downlinkJitterMs")
    def downlink_jitter_ms(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="downlinkLossPercent")
    def downlink_loss_percent(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectArn")
    def project_arn(self) -> pulumi.Output[_builtins.str]: ...
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
    def type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="uplinkBandwidthBits")
    def uplink_bandwidth_bits(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="uplinkDelayMs")
    def uplink_delay_ms(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="uplinkJitterMs")
    def uplink_jitter_ms(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="uplinkLossPercent")
    def uplink_loss_percent(self) -> pulumi.Output[Optional[_builtins.int]]: ...
