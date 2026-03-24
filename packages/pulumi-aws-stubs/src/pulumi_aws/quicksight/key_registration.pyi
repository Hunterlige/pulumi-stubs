import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeyRegistrationArgs", "KeyRegistration"]

@pulumi.input_type
class KeyRegistrationArgs:
    def __init__(
        __self__,
        *,
        key_registrations: pulumi.Input[
            Sequence[pulumi.Input[KeyRegistrationKeyRegistrationArgs]]
        ],
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyRegistrations")
    def key_registrations(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[KeyRegistrationKeyRegistrationArgs]]]: ...
    @key_registrations.setter
    def key_registrations(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[KeyRegistrationKeyRegistrationArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _KeyRegistrationState:
    def __init__(
        __self__,
        *,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_registrations: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyRegistrationKeyRegistrationArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyRegistrations")
    def key_registrations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KeyRegistrationKeyRegistrationArgs]]]
    ]: ...
    @key_registrations.setter
    def key_registrations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyRegistrationKeyRegistrationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:quicksight/keyRegistration:KeyRegistration")
class KeyRegistration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_registrations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeyRegistrationKeyRegistrationArgs,
                            KeyRegistrationKeyRegistrationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeyRegistrationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_registrations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeyRegistrationKeyRegistrationArgs,
                            KeyRegistrationKeyRegistrationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> KeyRegistration: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyRegistrations")
    def key_registrations(
        self,
    ) -> pulumi.Output[Sequence[outputs.KeyRegistrationKeyRegistration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
