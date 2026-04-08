import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOfferAccessTokenResult",
    "AwaitableGetOfferAccessTokenResult",
    "get_offer_access_token",
    "get_offer_access_token_output",
]

@pulumi.output_type
class GetOfferAccessTokenResult:
    def __init__(__self__, access_token=..., disk_id=..., status=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

class AwaitableGetOfferAccessTokenResult(GetOfferAccessTokenResult):
    def __await__(self): ...

def get_offer_access_token(
    offer_id: Optional[_builtins.str] = ...,
    request_id: Optional[_builtins.str] = ...,
    resource_uri: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOfferAccessTokenResult: ...
def get_offer_access_token_output(
    offer_id: Optional[pulumi.Input[_builtins.str]] = ...,
    request_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOfferAccessTokenResult]: ...
