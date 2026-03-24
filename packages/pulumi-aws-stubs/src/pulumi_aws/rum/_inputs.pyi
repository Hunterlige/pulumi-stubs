import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppMonitorAppMonitorConfigurationArgs",
    "AppMonitorAppMonitorConfigurationArgsDict",
    "AppMonitorCustomEventsArgs",
    "AppMonitorCustomEventsArgsDict",
]

class AppMonitorAppMonitorConfigurationArgsDict(TypedDict):
    allow_cookies: NotRequired[pulumi.Input[_builtins.bool]]
    enable_xray: NotRequired[pulumi.Input[_builtins.bool]]
    excluded_pages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    favorite_pages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    guest_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    identity_pool_id: NotRequired[pulumi.Input[_builtins.str]]
    included_pages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    session_sample_rate: NotRequired[pulumi.Input[_builtins.float]]
    telemetries: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AppMonitorAppMonitorConfigurationArgs:
    def __init__(
        __self__,
        *,
        allow_cookies: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_xray: Optional[pulumi.Input[_builtins.bool]] = ...,
        excluded_pages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        favorite_pages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        guest_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        included_pages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        session_sample_rate: Optional[pulumi.Input[_builtins.float]] = ...,
        telemetries: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCookies")
    def allow_cookies(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_cookies.setter
    def allow_cookies(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableXray")
    def enable_xray(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_xray.setter
    def enable_xray(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="excludedPages")
    def excluded_pages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_pages.setter
    def excluded_pages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="favoritePages")
    def favorite_pages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @favorite_pages.setter
    def favorite_pages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="guestRoleArn")
    def guest_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @guest_role_arn.setter
    def guest_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_pool_id.setter
    def identity_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includedPages")
    def included_pages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_pages.setter
    def included_pages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sessionSampleRate")
    def session_sample_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @session_sample_rate.setter
    def session_sample_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def telemetries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @telemetries.setter
    def telemetries(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AppMonitorCustomEventsArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppMonitorCustomEventsArgs:
    def __init__(
        __self__, *, status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
