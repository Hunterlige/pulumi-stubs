import builtins as _builtins
import sys
import pulumi
from typing import Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["Batching", "ExternalCredentials"]

@pulumi.output_type
class Batching(dict):
    def __init__(
        __self__,
        *,
        enable_batching: Optional[_builtins.bool] = ...,
        send_after: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableBatching")
    def enable_batching(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sendAfter")
    def send_after(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExternalCredentials(dict):
    def __init__(
        __self__,
        *,
        audience: _builtins.str,
        identity_token: _builtins.str,
        service_account_email: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityToken")
    def identity_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str: ...
