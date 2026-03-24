import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "TrustAnchorNotificationSettingArgs",
    "TrustAnchorNotificationSettingArgsDict",
    "TrustAnchorSourceArgs",
    "TrustAnchorSourceArgsDict",
    "TrustAnchorSourceSourceDataArgs",
    "TrustAnchorSourceSourceDataArgsDict",
]

class TrustAnchorNotificationSettingArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    configured_by: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    event: NotRequired[pulumi.Input[_builtins.str]]
    threshold: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class TrustAnchorNotificationSettingArgs:
    def __init__(
        __self__,
        *,
        channel: Optional[pulumi.Input[_builtins.str]] = ...,
        configured_by: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        event: Optional[pulumi.Input[_builtins.str]] = ...,
        threshold: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configuredBy")
    def configured_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configured_by.setter
    def configured_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event.setter
    def event(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TrustAnchorSourceArgsDict(TypedDict):
    source_data: pulumi.Input[TrustAnchorSourceSourceDataArgsDict]
    source_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TrustAnchorSourceArgs:
    def __init__(
        __self__,
        *,
        source_data: pulumi.Input[TrustAnchorSourceSourceDataArgs],
        source_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceData")
    def source_data(self) -> pulumi.Input[TrustAnchorSourceSourceDataArgs]: ...
    @source_data.setter
    def source_data(self, value: pulumi.Input[TrustAnchorSourceSourceDataArgs]): ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Input[_builtins.str]: ...
    @source_type.setter
    def source_type(self, value: pulumi.Input[_builtins.str]): ...

class TrustAnchorSourceSourceDataArgsDict(TypedDict):
    acm_pca_arn: NotRequired[pulumi.Input[_builtins.str]]
    x509_certificate_data: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TrustAnchorSourceSourceDataArgs:
    def __init__(
        __self__,
        *,
        acm_pca_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        x509_certificate_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acmPcaArn")
    def acm_pca_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acm_pca_arn.setter
    def acm_pca_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="x509CertificateData")
    def x509_certificate_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @x509_certificate_data.setter
    def x509_certificate_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
