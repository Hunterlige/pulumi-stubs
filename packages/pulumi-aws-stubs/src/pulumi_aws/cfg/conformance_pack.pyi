import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConformancePackArgs", "ConformancePack"]

@pulumi.input_type
class ConformancePackArgs:
    def __init__(
        __self__,
        *,
        delivery_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        input_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConformancePackInputParameterArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        template_body: Optional[pulumi.Input[_builtins.str]] = ...,
        template_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConformancePackInputParameterArgs]]]
    ]: ...
    @input_parameters.setter
    def input_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConformancePackInputParameterArgs]]]
        ],
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
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateS3Uri")
    def template_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_s3_uri.setter
    def template_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ConformancePackState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        input_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConformancePackInputParameterArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        template_body: Optional[pulumi.Input[_builtins.str]] = ...,
        template_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConformancePackInputParameterArgs]]]
    ]: ...
    @input_parameters.setter
    def input_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConformancePackInputParameterArgs]]]
        ],
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
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateS3Uri")
    def template_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_s3_uri.setter
    def template_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:cfg/conformancePack:ConformancePack")
class ConformancePack(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        delivery_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        input_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConformancePackInputParameterArgs,
                            ConformancePackInputParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        template_body: Optional[pulumi.Input[_builtins.str]] = ...,
        template_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ConformancePackArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        input_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConformancePackInputParameterArgs,
                            ConformancePackInputParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        template_body: Optional[pulumi.Input[_builtins.str]] = ...,
        template_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ConformancePack: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ConformancePackInputParameter]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="templateS3Uri")
    def template_s3_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
