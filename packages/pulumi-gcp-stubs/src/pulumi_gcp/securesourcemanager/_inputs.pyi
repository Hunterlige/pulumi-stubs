import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "HookPushOptionArgs",
    "HookPushOptionArgsDict",
    "InstanceHostConfigArgs",
    "InstanceHostConfigArgsDict",
    "InstanceIamBindingConditionArgs",
    "InstanceIamBindingConditionArgsDict",
    "InstanceIamMemberConditionArgs",
    "InstanceIamMemberConditionArgsDict",
    "InstancePrivateConfigArgs",
    "InstancePrivateConfigArgsDict",
    "InstanceWorkforceIdentityFederationConfigArgs",
    "InstanceWorkforceIdentityFederationConfigArgsDict",
    "RepositoryIamBindingConditionArgs",
    "RepositoryIamBindingConditionArgsDict",
    "RepositoryIamMemberConditionArgs",
    "RepositoryIamMemberConditionArgsDict",
    "RepositoryInitialConfigArgs",
    "RepositoryInitialConfigArgsDict",
    "RepositoryUriArgs",
    "RepositoryUriArgsDict",
]

class HookPushOptionArgsDict(TypedDict):
    branch_filter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HookPushOptionArgs:
    def __init__(
        __self__, *, branch_filter: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchFilter")
    def branch_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_filter.setter
    def branch_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceHostConfigArgsDict(TypedDict):
    api: NotRequired[pulumi.Input[_builtins.str]]
    git_http: NotRequired[pulumi.Input[_builtins.str]]
    git_ssh: NotRequired[pulumi.Input[_builtins.str]]
    html: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceHostConfigArgs:
    def __init__(
        __self__,
        *,
        api: Optional[pulumi.Input[_builtins.str]] = ...,
        git_http: Optional[pulumi.Input[_builtins.str]] = ...,
        git_ssh: Optional[pulumi.Input[_builtins.str]] = ...,
        html: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api.setter
    def api(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitHttp")
    def git_http(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_http.setter
    def git_http(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitSsh")
    def git_ssh(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_ssh.setter
    def git_ssh(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def html(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @html.setter
    def html(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstancePrivateConfigArgsDict(TypedDict):
    is_private: pulumi.Input[_builtins.bool]
    ca_pool: NotRequired[pulumi.Input[_builtins.str]]
    http_service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ssh_service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePrivateConfigArgs:
    def __init__(
        __self__,
        *,
        is_private: pulumi.Input[_builtins.bool],
        ca_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        http_service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh_service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> pulumi.Input[_builtins.bool]: ...
    @is_private.setter
    def is_private(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_pool.setter
    def ca_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpServiceAttachment")
    def http_service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_service_attachment.setter
    def http_service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sshServiceAttachment")
    def ssh_service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssh_service_attachment.setter
    def ssh_service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceWorkforceIdentityFederationConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class InstanceWorkforceIdentityFederationConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class RepositoryIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryInitialConfigArgsDict(TypedDict):
    default_branch: NotRequired[pulumi.Input[_builtins.str]]
    gitignores: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    license: NotRequired[pulumi.Input[_builtins.str]]
    readme: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryInitialConfigArgs:
    def __init__(
        __self__,
        *,
        default_branch: Optional[pulumi.Input[_builtins.str]] = ...,
        gitignores: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        license: Optional[pulumi.Input[_builtins.str]] = ...,
        readme: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_branch.setter
    def default_branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gitignores(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gitignores.setter
    def gitignores(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def license(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license.setter
    def license(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def readme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @readme.setter
    def readme(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryUriArgsDict(TypedDict):
    api: NotRequired[pulumi.Input[_builtins.str]]
    git_https: NotRequired[pulumi.Input[_builtins.str]]
    html: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryUriArgs:
    def __init__(
        __self__,
        *,
        api: Optional[pulumi.Input[_builtins.str]] = ...,
        git_https: Optional[pulumi.Input[_builtins.str]] = ...,
        html: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api.setter
    def api(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitHttps")
    def git_https(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_https.setter
    def git_https(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def html(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @html.setter
    def html(self, value: Optional[pulumi.Input[_builtins.str]]): ...
