import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RepositoryExternalConnectionsArgs",
    "RepositoryExternalConnectionsArgsDict",
    "RepositoryUpstreamArgs",
    "RepositoryUpstreamArgsDict",
]

class RepositoryExternalConnectionsArgsDict(TypedDict):
    external_connection_name: pulumi.Input[_builtins.str]
    package_format: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RepositoryExternalConnectionsArgs:
    def __init__(
        __self__,
        *,
        external_connection_name: pulumi.Input[_builtins.str],
        package_format: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalConnectionName")
    def external_connection_name(self) -> pulumi.Input[_builtins.str]: ...
    @external_connection_name.setter
    def external_connection_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="packageFormat")
    def package_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_format.setter
    def package_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryUpstreamArgsDict(TypedDict):
    repository_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class RepositoryUpstreamArgs:
    def __init__(__self__, *, repository_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Input[_builtins.str]: ...
    @repository_name.setter
    def repository_name(self, value: pulumi.Input[_builtins.str]): ...
