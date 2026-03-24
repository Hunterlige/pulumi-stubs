import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcOriginArgs", "VpcOrigin"]

@pulumi.input_type
class VpcOriginArgs:
    def __init__(
        __self__,
        *,
        vpc_origin_endpoint_config: pulumi.Input[VpcOriginVpcOriginEndpointConfigArgs],
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[VpcOriginTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcOriginEndpointConfig")
    def vpc_origin_endpoint_config(
        self,
    ) -> pulumi.Input[VpcOriginVpcOriginEndpointConfigArgs]: ...
    @vpc_origin_endpoint_config.setter
    def vpc_origin_endpoint_config(
        self, value: pulumi.Input[VpcOriginVpcOriginEndpointConfigArgs]
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[VpcOriginTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[VpcOriginTimeoutsArgs]]): ...

@pulumi.input_type
class _VpcOriginState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[VpcOriginTimeoutsArgs]] = ...,
        vpc_origin_endpoint_config: Optional[
            pulumi.Input[VpcOriginVpcOriginEndpointConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def timeouts(self) -> Optional[pulumi.Input[VpcOriginTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[VpcOriginTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcOriginEndpointConfig")
    def vpc_origin_endpoint_config(
        self,
    ) -> Optional[pulumi.Input[VpcOriginVpcOriginEndpointConfigArgs]]: ...
    @vpc_origin_endpoint_config.setter
    def vpc_origin_endpoint_config(
        self, value: Optional[pulumi.Input[VpcOriginVpcOriginEndpointConfigArgs]]
    ): ...

@pulumi.type_token("aws:cloudfront/vpcOrigin:VpcOrigin")
class VpcOrigin(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[VpcOriginTimeoutsArgs, VpcOriginTimeoutsArgsDict]]
        ] = ...,
        vpc_origin_endpoint_config: Optional[
            pulumi.Input[
                Union[
                    VpcOriginVpcOriginEndpointConfigArgs,
                    VpcOriginVpcOriginEndpointConfigArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcOriginArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[VpcOriginTimeoutsArgs, VpcOriginTimeoutsArgsDict]]
        ] = ...,
        vpc_origin_endpoint_config: Optional[
            pulumi.Input[
                Union[
                    VpcOriginVpcOriginEndpointConfigArgs,
                    VpcOriginVpcOriginEndpointConfigArgsDict,
                ]
            ]
        ] = ...,
    ) -> VpcOrigin: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.VpcOriginTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcOriginEndpointConfig")
    def vpc_origin_endpoint_config(
        self,
    ) -> pulumi.Output[outputs.VpcOriginVpcOriginEndpointConfig]: ...
