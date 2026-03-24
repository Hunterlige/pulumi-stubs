import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LogTransformerArgs", "LogTransformer"]

@pulumi.input_type
class LogTransformerArgs:
    def __init__(
        __self__,
        *,
        log_group_arn: pulumi.Input[_builtins.str],
        transformer_configs: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigArgs]]
        ],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_arn.setter
    def log_group_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="transformerConfigs")
    def transformer_configs(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigArgs]]]: ...
    @transformer_configs.setter
    def transformer_configs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LogTransformerState:
    def __init__(
        __self__,
        *,
        log_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        transformer_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group_arn.setter
    def log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transformerConfigs")
    def transformer_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigArgs]]]
    ]: ...
    @transformer_configs.setter
    def transformer_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:cloudwatch/logTransformer:LogTransformer")
class LogTransformer(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        log_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        transformer_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LogTransformerTransformerConfigArgs,
                            LogTransformerTransformerConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LogTransformerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        log_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        transformer_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LogTransformerTransformerConfigArgs,
                            LogTransformerTransformerConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> LogTransformer: ...
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transformerConfigs")
    def transformer_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.LogTransformerTransformerConfig]]: ...
