import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkInsightsPathArgs", "NetworkInsightsPath"]

@pulumi.input_type
class NetworkInsightsPathArgs:
    def __init__(
        __self__,
        *,
        protocol: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_port: Optional[pulumi.Input[_builtins.int]] = ...,
        filter_at_destination: Optional[
            pulumi.Input[NetworkInsightsPathFilterAtDestinationArgs]
        ] = ...,
        filter_at_source: Optional[
            pulumi.Input[NetworkInsightsPathFilterAtSourceArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_ip.setter
    def destination_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="filterAtDestination")
    def filter_at_destination(
        self,
    ) -> Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationArgs]]: ...
    @filter_at_destination.setter
    def filter_at_destination(
        self, value: Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterAtSource")
    def filter_at_source(
        self,
    ) -> Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceArgs]]: ...
    @filter_at_source.setter
    def filter_at_source(
        self, value: Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _NetworkInsightsPathState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_port: Optional[pulumi.Input[_builtins.int]] = ...,
        filter_at_destination: Optional[
            pulumi.Input[NetworkInsightsPathFilterAtDestinationArgs]
        ] = ...,
        filter_at_source: Optional[
            pulumi.Input[NetworkInsightsPathFilterAtSourceArgs]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_arn.setter
    def destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_ip.setter
    def destination_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="filterAtDestination")
    def filter_at_destination(
        self,
    ) -> Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationArgs]]: ...
    @filter_at_destination.setter
    def filter_at_destination(
        self, value: Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterAtSource")
    def filter_at_source(
        self,
    ) -> Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceArgs]]: ...
    @filter_at_source.setter
    def filter_at_source(
        self, value: Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_arn.setter
    def source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:ec2/networkInsightsPath:NetworkInsightsPath")
class NetworkInsightsPath(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_port: Optional[pulumi.Input[_builtins.int]] = ...,
        filter_at_destination: Optional[
            pulumi.Input[
                Union[
                    NetworkInsightsPathFilterAtDestinationArgs,
                    NetworkInsightsPathFilterAtDestinationArgsDict,
                ]
            ]
        ] = ...,
        filter_at_source: Optional[
            pulumi.Input[
                Union[
                    NetworkInsightsPathFilterAtSourceArgs,
                    NetworkInsightsPathFilterAtSourceArgsDict,
                ]
            ]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkInsightsPathArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_port: Optional[pulumi.Input[_builtins.int]] = ...,
        filter_at_destination: Optional[
            pulumi.Input[
                Union[
                    NetworkInsightsPathFilterAtDestinationArgs,
                    NetworkInsightsPathFilterAtDestinationArgsDict,
                ]
            ]
        ] = ...,
        filter_at_source: Optional[
            pulumi.Input[
                Union[
                    NetworkInsightsPathFilterAtSourceArgs,
                    NetworkInsightsPathFilterAtSourceArgsDict,
                ]
            ]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> NetworkInsightsPath: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="filterAtDestination")
    def filter_at_destination(
        self,
    ) -> pulumi.Output[outputs.NetworkInsightsPathFilterAtDestination]: ...
    @_builtins.property
    @pulumi.getter(name="filterAtSource")
    def filter_at_source(
        self,
    ) -> pulumi.Output[outputs.NetworkInsightsPathFilterAtSource]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
