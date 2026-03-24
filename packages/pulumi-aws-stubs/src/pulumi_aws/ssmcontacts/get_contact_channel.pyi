import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContactChannelResult",
    "AwaitableGetContactChannelResult",
    "get_contact_channel",
    "get_contact_channel_output",
]

@pulumi.output_type
class GetContactChannelResult:
    def __init__(
        __self__,
        activation_status=...,
        arn=...,
        contact_id=...,
        delivery_addresses=...,
        id=...,
        name=...,
        region=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activationStatus")
    def activation_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deliveryAddresses")
    def delivery_addresses(
        self,
    ) -> Sequence[outputs.GetContactChannelDeliveryAddressResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetContactChannelResult(GetContactChannelResult):
    def __await__(self): ...

def get_contact_channel(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContactChannelResult: ...
def get_contact_channel_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContactChannelResult]: ...
