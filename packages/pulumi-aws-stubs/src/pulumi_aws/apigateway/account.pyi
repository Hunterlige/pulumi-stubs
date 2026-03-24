import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountArgs", "Account"]

@pulumi.input_type
class AccountArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchRoleArn")
    def cloudwatch_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_role_arn.setter
    def cloudwatch_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AccountState:
    def __init__(
        __self__,
        *,
        api_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        features: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        throttle_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccountThrottleSettingArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyVersion")
    def api_key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_version.setter
    def api_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchRoleArn")
    def cloudwatch_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_role_arn.setter
    def cloudwatch_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @features.setter
    def features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="throttleSettings")
    def throttle_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccountThrottleSettingArgs]]]]: ...
    @throttle_settings.setter
    def throttle_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccountThrottleSettingArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:apigateway/account:Account")
class Account(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cloudwatch_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AccountArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        features: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        throttle_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AccountThrottleSettingArgs, AccountThrottleSettingArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> Account: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyVersion")
    def api_key_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchRoleArn")
    def cloudwatch_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def features(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="throttleSettings")
    def throttle_settings(
        self,
    ) -> pulumi.Output[Sequence[outputs.AccountThrottleSetting]]: ...
