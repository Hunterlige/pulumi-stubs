import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ContactChannelArgs", "ContactChannel"]

@pulumi.input_type
class ContactChannelArgs:
    def __init__(
        __self__,
        *,
        contact_id: pulumi.Input[_builtins.str],
        delivery_address: pulumi.Input[ContactChannelDeliveryAddressArgs],
        type: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> pulumi.Input[_builtins.str]: ...
    @contact_id.setter
    def contact_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryAddress")
    def delivery_address(self) -> pulumi.Input[ContactChannelDeliveryAddressArgs]: ...
    @delivery_address.setter
    def delivery_address(
        self, value: pulumi.Input[ContactChannelDeliveryAddressArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
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

@pulumi.input_type
class _ContactChannelState:
    def __init__(
        __self__,
        *,
        activation_status: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        contact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_address: Optional[
            pulumi.Input[ContactChannelDeliveryAddressArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activationStatus")
    def activation_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @activation_status.setter
    def activation_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @contact_id.setter
    def contact_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryAddress")
    def delivery_address(
        self,
    ) -> Optional[pulumi.Input[ContactChannelDeliveryAddressArgs]]: ...
    @delivery_address.setter
    def delivery_address(
        self, value: Optional[pulumi.Input[ContactChannelDeliveryAddressArgs]]
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ssmcontacts/contactChannel:ContactChannel")
class ContactChannel(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        contact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_address: Optional[
            pulumi.Input[
                Union[
                    ContactChannelDeliveryAddressArgs,
                    ContactChannelDeliveryAddressArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ContactChannelArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        activation_status: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        contact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_address: Optional[
            pulumi.Input[
                Union[
                    ContactChannelDeliveryAddressArgs,
                    ContactChannelDeliveryAddressArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ContactChannel: ...
    @_builtins.property
    @pulumi.getter(name="activationStatus")
    def activation_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryAddress")
    def delivery_address(
        self,
    ) -> pulumi.Output[outputs.ContactChannelDeliveryAddress]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
