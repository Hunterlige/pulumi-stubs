import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ChannelHlsIngestArgs",
    "ChannelHlsIngestArgsDict",
    "ChannelHlsIngestIngestEndpointArgs",
    "ChannelHlsIngestIngestEndpointArgsDict",
]

class ChannelHlsIngestArgsDict(TypedDict):
    ingest_endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ChannelHlsIngestIngestEndpointArgsDict]]]
    ]

@pulumi.input_type
class ChannelHlsIngestArgs:
    def __init__(
        __self__,
        *,
        ingest_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ChannelHlsIngestIngestEndpointArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestEndpoints")
    def ingest_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ChannelHlsIngestIngestEndpointArgs]]]
    ]: ...
    @ingest_endpoints.setter
    def ingest_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ChannelHlsIngestIngestEndpointArgs]]]
        ],
    ): ...

class ChannelHlsIngestIngestEndpointArgsDict(TypedDict):
    password: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelHlsIngestIngestEndpointArgs:
    def __init__(
        __self__,
        *,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
