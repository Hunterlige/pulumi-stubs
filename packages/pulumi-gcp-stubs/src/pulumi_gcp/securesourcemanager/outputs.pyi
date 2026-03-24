import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "HookPushOption",
    "InstanceHostConfig",
    "InstanceIamBindingCondition",
    "InstanceIamMemberCondition",
    "InstancePrivateConfig",
    "InstanceWorkforceIdentityFederationConfig",
    "RepositoryIamBindingCondition",
    "RepositoryIamMemberCondition",
    "RepositoryInitialConfig",
    "RepositoryUri",
]

@pulumi.output_type
class HookPushOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, branch_filter: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchFilter")
    def branch_filter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceHostConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api: Optional[_builtins.str] = ...,
        git_http: Optional[_builtins.str] = ...,
        git_ssh: Optional[_builtins.str] = ...,
        html: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitHttp")
    def git_http(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitSsh")
    def git_ssh(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def html(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstancePrivateConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_private: _builtins.bool,
        ca_pool: Optional[_builtins.str] = ...,
        http_service_attachment: Optional[_builtins.str] = ...,
        ssh_service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpServiceAttachment")
    def http_service_attachment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sshServiceAttachment")
    def ssh_service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceWorkforceIdentityFederationConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class RepositoryIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RepositoryIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RepositoryInitialConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_branch: Optional[_builtins.str] = ...,
        gitignores: Optional[Sequence[_builtins.str]] = ...,
        license: Optional[_builtins.str] = ...,
        readme: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def gitignores(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def license(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def readme(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RepositoryUri(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api: Optional[_builtins.str] = ...,
        git_https: Optional[_builtins.str] = ...,
        html: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitHttps")
    def git_https(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def html(self) -> Optional[_builtins.str]: ...
