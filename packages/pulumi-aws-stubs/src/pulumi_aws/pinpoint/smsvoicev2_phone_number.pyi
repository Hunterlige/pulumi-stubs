import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["Smsvoicev2PhoneNumberArgs", "Smsvoicev2PhoneNumber"]

@pulumi.input_type
class Smsvoicev2PhoneNumberArgs:
    def __init__(
        __self__,
        *,
        iso_country_code: pulumi.Input[_builtins.str],
        message_type: pulumi.Input[_builtins.str],
        number_capabilities: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        number_type: pulumi.Input[_builtins.str],
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        opt_out_list_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        self_managed_opt_outs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[Smsvoicev2PhoneNumberTimeoutsArgs]] = ...,
        two_way_channel_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        two_way_channel_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        two_way_channel_role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isoCountryCode")
    def iso_country_code(self) -> pulumi.Input[_builtins.str]: ...
    @iso_country_code.setter
    def iso_country_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="messageType")
    def message_type(self) -> pulumi.Input[_builtins.str]: ...
    @message_type.setter
    def message_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="numberCapabilities")
    def number_capabilities(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @number_capabilities.setter
    def number_capabilities(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberType")
    def number_type(self) -> pulumi.Input[_builtins.str]: ...
    @number_type.setter
    def number_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="optOutListName")
    def opt_out_list_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opt_out_list_name.setter
    def opt_out_list_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationId")
    def registration_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_id.setter
    def registration_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfManagedOptOutsEnabled")
    def self_managed_opt_outs_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @self_managed_opt_outs_enabled.setter
    def self_managed_opt_outs_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
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
    def timeouts(self) -> Optional[pulumi.Input[Smsvoicev2PhoneNumberTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[Smsvoicev2PhoneNumberTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelArn")
    def two_way_channel_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @two_way_channel_arn.setter
    def two_way_channel_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelEnabled")
    def two_way_channel_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @two_way_channel_enabled.setter
    def two_way_channel_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelRole")
    def two_way_channel_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @two_way_channel_role.setter
    def two_way_channel_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _Smsvoicev2PhoneNumberState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        iso_country_code: Optional[pulumi.Input[_builtins.str]] = ...,
        message_type: Optional[pulumi.Input[_builtins.str]] = ...,
        monthly_leasing_price: Optional[pulumi.Input[_builtins.str]] = ...,
        number_capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        number_type: Optional[pulumi.Input[_builtins.str]] = ...,
        opt_out_list_name: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        self_managed_opt_outs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[Smsvoicev2PhoneNumberTimeoutsArgs]] = ...,
        two_way_channel_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        two_way_channel_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        two_way_channel_role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isoCountryCode")
    def iso_country_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iso_country_code.setter
    def iso_country_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="messageType")
    def message_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_type.setter
    def message_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monthlyLeasingPrice")
    def monthly_leasing_price(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monthly_leasing_price.setter
    def monthly_leasing_price(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberCapabilities")
    def number_capabilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @number_capabilities.setter
    def number_capabilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberType")
    def number_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @number_type.setter
    def number_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="optOutListName")
    def opt_out_list_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opt_out_list_name.setter
    def opt_out_list_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationId")
    def registration_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_id.setter
    def registration_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfManagedOptOutsEnabled")
    def self_managed_opt_outs_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @self_managed_opt_outs_enabled.setter
    def self_managed_opt_outs_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
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
    def timeouts(self) -> Optional[pulumi.Input[Smsvoicev2PhoneNumberTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[Smsvoicev2PhoneNumberTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelArn")
    def two_way_channel_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @two_way_channel_arn.setter
    def two_way_channel_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelEnabled")
    def two_way_channel_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @two_way_channel_enabled.setter
    def two_way_channel_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelRole")
    def two_way_channel_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @two_way_channel_role.setter
    def two_way_channel_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class Smsvoicev2PhoneNumber(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        iso_country_code: Optional[pulumi.Input[_builtins.str]] = ...,
        message_type: Optional[pulumi.Input[_builtins.str]] = ...,
        number_capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        number_type: Optional[pulumi.Input[_builtins.str]] = ...,
        opt_out_list_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        self_managed_opt_outs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    Smsvoicev2PhoneNumberTimeoutsArgs,
                    Smsvoicev2PhoneNumberTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        two_way_channel_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        two_way_channel_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        two_way_channel_role: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Smsvoicev2PhoneNumberArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        iso_country_code: Optional[pulumi.Input[_builtins.str]] = ...,
        message_type: Optional[pulumi.Input[_builtins.str]] = ...,
        monthly_leasing_price: Optional[pulumi.Input[_builtins.str]] = ...,
        number_capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        number_type: Optional[pulumi.Input[_builtins.str]] = ...,
        opt_out_list_name: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        self_managed_opt_outs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    Smsvoicev2PhoneNumberTimeoutsArgs,
                    Smsvoicev2PhoneNumberTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        two_way_channel_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        two_way_channel_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        two_way_channel_role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Smsvoicev2PhoneNumber: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isoCountryCode")
    def iso_country_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="messageType")
    def message_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monthlyLeasingPrice")
    def monthly_leasing_price(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberCapabilities")
    def number_capabilities(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="numberType")
    def number_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="optOutListName")
    def opt_out_list_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationId")
    def registration_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selfManagedOptOutsEnabled")
    def self_managed_opt_outs_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.Smsvoicev2PhoneNumberTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelArn")
    def two_way_channel_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelEnabled")
    def two_way_channel_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="twoWayChannelRole")
    def two_way_channel_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
