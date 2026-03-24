import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LogDeliveryConfigurationArgs", "LogDeliveryConfiguration"]

@pulumi.input_type
class LogDeliveryConfigurationArgs:
    def __init__(
        __self__,
        *,
        log_configurations: pulumi.Input[
            Sequence[pulumi.Input[LogDeliveryConfigurationLogConfigurationArgs]]
        ],
        user_pool_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logConfigurations")
    def log_configurations(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LogDeliveryConfigurationLogConfigurationArgs]]
    ]: ...
    @log_configurations.setter
    def log_configurations(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LogDeliveryConfigurationLogConfigurationArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LogDeliveryConfigurationState:
    def __init__(
        __self__,
        *,
        log_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogDeliveryConfigurationLogConfigurationArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logConfigurations")
    def log_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogDeliveryConfigurationLogConfigurationArgs]]
        ]
    ]: ...
    @log_configurations.setter
    def log_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogDeliveryConfigurationLogConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_pool_id.setter
    def user_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class LogDeliveryConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        log_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LogDeliveryConfigurationLogConfigurationArgs,
                            LogDeliveryConfigurationLogConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LogDeliveryConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        log_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LogDeliveryConfigurationLogConfigurationArgs,
                            LogDeliveryConfigurationLogConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LogDeliveryConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="logConfigurations")
    def log_configurations(
        self,
    ) -> pulumi.Output[Sequence[outputs.LogDeliveryConfigurationLogConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[_builtins.str]: ...
