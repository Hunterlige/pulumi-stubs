import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ModelCardArgs", "ModelCard"]

@pulumi.input_type
class ModelCardArgs:
    def __init__(
        __self__,
        *,
        content: pulumi.Input[_builtins.str],
        model_card_name: pulumi.Input[_builtins.str],
        model_card_status: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_config: Optional[pulumi.Input[ModelCardSecurityConfigArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[ModelCardTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[_builtins.str]: ...
    @content.setter
    def content(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelCardName")
    def model_card_name(self) -> pulumi.Input[_builtins.str]: ...
    @model_card_name.setter
    def model_card_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelCardStatus")
    def model_card_status(self) -> pulumi.Input[_builtins.str]: ...
    @model_card_status.setter
    def model_card_status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(
        self,
    ) -> Optional[pulumi.Input[ModelCardSecurityConfigArgs]]: ...
    @security_config.setter
    def security_config(
        self, value: Optional[pulumi.Input[ModelCardSecurityConfigArgs]]
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
    def timeouts(self) -> Optional[pulumi.Input[ModelCardTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ModelCardTimeoutsArgs]]): ...

@pulumi.input_type
class _ModelCardState:
    def __init__(
        __self__,
        *,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_config: Optional[pulumi.Input[ModelCardSecurityConfigArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[ModelCardTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelCardArn")
    def model_card_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_card_arn.setter
    def model_card_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelCardName")
    def model_card_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_card_name.setter
    def model_card_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelCardStatus")
    def model_card_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_card_status.setter
    def model_card_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(
        self,
    ) -> Optional[pulumi.Input[ModelCardSecurityConfigArgs]]: ...
    @security_config.setter
    def security_config(
        self, value: Optional[pulumi.Input[ModelCardSecurityConfigArgs]]
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ModelCardTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ModelCardTimeoutsArgs]]): ...

@pulumi.type_token("aws:sagemaker/modelCard:ModelCard")
class ModelCard(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_config: Optional[
            pulumi.Input[
                Union[ModelCardSecurityConfigArgs, ModelCardSecurityConfigArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ModelCardTimeoutsArgs, ModelCardTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ModelCardArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_config: Optional[
            pulumi.Input[
                Union[ModelCardSecurityConfigArgs, ModelCardSecurityConfigArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ModelCardTimeoutsArgs, ModelCardTimeoutsArgsDict]]
        ] = ...,
    ) -> ModelCard: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelCardArn")
    def model_card_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelCardName")
    def model_card_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelCardStatus")
    def model_card_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ModelCardSecurityConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ModelCardTimeouts]]: ...
