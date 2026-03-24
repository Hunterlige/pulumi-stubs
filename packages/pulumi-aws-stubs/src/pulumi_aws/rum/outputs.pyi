import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppMonitorAppMonitorConfiguration", "AppMonitorCustomEvents"]

@pulumi.output_type
class AppMonitorAppMonitorConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_cookies: Optional[_builtins.bool] = ...,
        enable_xray: Optional[_builtins.bool] = ...,
        excluded_pages: Optional[Sequence[_builtins.str]] = ...,
        favorite_pages: Optional[Sequence[_builtins.str]] = ...,
        guest_role_arn: Optional[_builtins.str] = ...,
        identity_pool_id: Optional[_builtins.str] = ...,
        included_pages: Optional[Sequence[_builtins.str]] = ...,
        session_sample_rate: Optional[_builtins.float] = ...,
        telemetries: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCookies")
    def allow_cookies(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableXray")
    def enable_xray(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludedPages")
    def excluded_pages(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="favoritePages")
    def favorite_pages(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="guestRoleArn")
    def guest_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includedPages")
    def included_pages(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sessionSampleRate")
    def session_sample_rate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def telemetries(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AppMonitorCustomEvents(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
