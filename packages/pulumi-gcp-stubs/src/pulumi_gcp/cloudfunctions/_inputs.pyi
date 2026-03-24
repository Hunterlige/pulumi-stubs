import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FunctionAutomaticUpdatePolicyArgs",
    "FunctionAutomaticUpdatePolicyArgsDict",
    "FunctionEventTriggerArgs",
    "FunctionEventTriggerArgsDict",
    "FunctionEventTriggerFailurePolicyArgs",
    "FunctionEventTriggerFailurePolicyArgsDict",
    "FunctionIamBindingConditionArgs",
    "FunctionIamBindingConditionArgsDict",
    "FunctionIamMemberConditionArgs",
    "FunctionIamMemberConditionArgsDict",
    "FunctionOnDeployUpdatePolicyArgs",
    "FunctionOnDeployUpdatePolicyArgsDict",
    "FunctionSecretEnvironmentVariableArgs",
    "FunctionSecretEnvironmentVariableArgsDict",
    "FunctionSecretVolumeArgs",
    "FunctionSecretVolumeArgsDict",
    "FunctionSecretVolumeVersionArgs",
    "FunctionSecretVolumeVersionArgsDict",
    "FunctionSourceRepositoryArgs",
    "FunctionSourceRepositoryArgsDict",
]

class FunctionAutomaticUpdatePolicyArgsDict(TypedDict): ...

@pulumi.input_type
class FunctionAutomaticUpdatePolicyArgs:
    def __init__(__self__) -> None: ...

class FunctionEventTriggerArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    resource: pulumi.Input[_builtins.str]
    failure_policy: NotRequired[pulumi.Input[FunctionEventTriggerFailurePolicyArgsDict]]
    ...

@pulumi.input_type
class FunctionEventTriggerArgs:
    def __init__(
        __self__,
        *,
        event_type: pulumi.Input[_builtins.str],
        resource: pulumi.Input[_builtins.str],
        failure_policy: Optional[
            pulumi.Input[FunctionEventTriggerFailurePolicyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]: ...
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]: ...
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failurePolicy")
    def failure_policy(
        self,
    ) -> Optional[pulumi.Input[FunctionEventTriggerFailurePolicyArgs]]: ...
    @failure_policy.setter
    def failure_policy(
        self, value: Optional[pulumi.Input[FunctionEventTriggerFailurePolicyArgs]]
    ): ...

class FunctionEventTriggerFailurePolicyArgsDict(TypedDict):
    retry: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class FunctionEventTriggerFailurePolicyArgs:
    def __init__(__self__, *, retry: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def retry(self) -> pulumi.Input[_builtins.bool]: ...
    @retry.setter
    def retry(self, value: pulumi.Input[_builtins.bool]): ...

class FunctionIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionIamBindingConditionArgs:
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

class FunctionIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionIamMemberConditionArgs:
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

class FunctionOnDeployUpdatePolicyArgsDict(TypedDict):
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionOnDeployUpdatePolicyArgs:
    def __init__(
        __self__, *, runtime_version: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionSecretEnvironmentVariableArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    secret: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionSecretEnvironmentVariableArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        secret: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionSecretVolumeArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    secret: pulumi.Input[_builtins.str]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    versions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeVersionArgsDict]]]
    ]
    ...

@pulumi.input_type
class FunctionSecretVolumeArgs:
    def __init__(
        __self__,
        *,
        mount_path: pulumi.Input[_builtins.str],
        secret: pulumi.Input[_builtins.str],
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeVersionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def versions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeVersionArgs]]]
    ]: ...
    @versions.setter
    def versions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FunctionSecretVolumeVersionArgs]]]
        ],
    ): ...

class FunctionSecretVolumeVersionArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FunctionSecretVolumeVersionArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...

class FunctionSourceRepositoryArgsDict(TypedDict):
    url: pulumi.Input[_builtins.str]
    deployed_url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionSourceRepositoryArgs:
    def __init__(
        __self__,
        *,
        url: pulumi.Input[_builtins.str],
        deployed_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deployedUrl")
    def deployed_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployed_url.setter
    def deployed_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
