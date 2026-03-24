import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EndpointServicePrivateDnsVerificationArgs",
    "EndpointServicePrivateDnsVerification",
]

@pulumi.input_type
class EndpointServicePrivateDnsVerificationArgs:
    def __init__(
        __self__,
        *,
        service_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[EndpointServicePrivateDnsVerificationTimeoutsArgs]
        ] = ...,
        wait_for_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Input[_builtins.str]: ...
    @service_id.setter
    def service_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[EndpointServicePrivateDnsVerificationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[
            pulumi.Input[EndpointServicePrivateDnsVerificationTimeoutsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForVerification")
    def wait_for_verification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_verification.setter
    def wait_for_verification(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _EndpointServicePrivateDnsVerificationState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[EndpointServicePrivateDnsVerificationTimeoutsArgs]
        ] = ...,
        wait_for_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[EndpointServicePrivateDnsVerificationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[
            pulumi.Input[EndpointServicePrivateDnsVerificationTimeoutsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForVerification")
    def wait_for_verification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_verification.setter
    def wait_for_verification(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token(...)
class EndpointServicePrivateDnsVerification(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    EndpointServicePrivateDnsVerificationTimeoutsArgs,
                    EndpointServicePrivateDnsVerificationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        wait_for_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EndpointServicePrivateDnsVerificationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    EndpointServicePrivateDnsVerificationTimeoutsArgs,
                    EndpointServicePrivateDnsVerificationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        wait_for_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> EndpointServicePrivateDnsVerification: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[
        Optional[outputs.EndpointServicePrivateDnsVerificationTimeouts]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="waitForVerification")
    def wait_for_verification(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
