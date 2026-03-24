import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClientOpenIdUserInfoResult",
    "AwaitableGetClientOpenIdUserInfoResult",
    "get_client_open_id_user_info",
    "get_client_open_id_user_info_output",
]

@pulumi.output_type
class GetClientOpenIdUserInfoResult:
    def __init__(__self__, email=..., id=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

class AwaitableGetClientOpenIdUserInfoResult(GetClientOpenIdUserInfoResult):
    def __await__(self): ...

def get_client_open_id_user_info(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClientOpenIdUserInfoResult: ...
def get_client_open_id_user_info_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClientOpenIdUserInfoResult]: ...
