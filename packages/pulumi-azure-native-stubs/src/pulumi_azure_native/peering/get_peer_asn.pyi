import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPeerAsnResult",
    "AwaitableGetPeerAsnResult",
    "get_peer_asn",
    "get_peer_asn_output",
]

@pulumi.output_type
class GetPeerAsnResult:
    def __init__(
        __self__,
        azure_api_version=...,
        error_message=...,
        id=...,
        name=...,
        peer_asn=...,
        peer_contact_detail=...,
        peer_name=...,
        type=...,
        validation_state=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="peerContactDetail")
    def peer_contact_detail(
        self,
    ) -> Optional[Sequence[outputs.ContactDetailResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="peerName")
    def peer_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validationState")
    def validation_state(self) -> _builtins.str: ...

class AwaitableGetPeerAsnResult(GetPeerAsnResult):
    def __await__(self): ...

def get_peer_asn(
    peer_asn_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPeerAsnResult: ...
def get_peer_asn_output(
    peer_asn_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPeerAsnResult]: ...
