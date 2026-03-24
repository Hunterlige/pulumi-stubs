import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DelegationSignerRecordArgs", "DelegationSignerRecord"]

@pulumi.input_type
class DelegationSignerRecordArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        signing_attributes: Optional[
            pulumi.Input[DelegationSignerRecordSigningAttributesArgs]
        ] = ...,
        timeouts: Optional[pulumi.Input[DelegationSignerRecordTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signingAttributes")
    def signing_attributes(
        self,
    ) -> Optional[pulumi.Input[DelegationSignerRecordSigningAttributesArgs]]: ...
    @signing_attributes.setter
    def signing_attributes(
        self, value: Optional[pulumi.Input[DelegationSignerRecordSigningAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[DelegationSignerRecordTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[DelegationSignerRecordTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _DelegationSignerRecordState:
    def __init__(
        __self__,
        *,
        dnssec_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_attributes: Optional[
            pulumi.Input[DelegationSignerRecordSigningAttributesArgs]
        ] = ...,
        timeouts: Optional[pulumi.Input[DelegationSignerRecordTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnssecKeyId")
    def dnssec_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dnssec_key_id.setter
    def dnssec_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signingAttributes")
    def signing_attributes(
        self,
    ) -> Optional[pulumi.Input[DelegationSignerRecordSigningAttributesArgs]]: ...
    @signing_attributes.setter
    def signing_attributes(
        self, value: Optional[pulumi.Input[DelegationSignerRecordSigningAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[DelegationSignerRecordTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[DelegationSignerRecordTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class DelegationSignerRecord(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_attributes: Optional[
            pulumi.Input[
                Union[
                    DelegationSignerRecordSigningAttributesArgs,
                    DelegationSignerRecordSigningAttributesArgsDict,
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    DelegationSignerRecordTimeoutsArgs,
                    DelegationSignerRecordTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DelegationSignerRecordArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        dnssec_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_attributes: Optional[
            pulumi.Input[
                Union[
                    DelegationSignerRecordSigningAttributesArgs,
                    DelegationSignerRecordSigningAttributesArgsDict,
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    DelegationSignerRecordTimeoutsArgs,
                    DelegationSignerRecordTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> DelegationSignerRecord: ...
    @_builtins.property
    @pulumi.getter(name="dnssecKeyId")
    def dnssec_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signingAttributes")
    def signing_attributes(
        self,
    ) -> pulumi.Output[Optional[outputs.DelegationSignerRecordSigningAttributes]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.DelegationSignerRecordTimeouts]]: ...
