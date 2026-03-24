import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApiConfigGatewayConfigArgs",
    "ApiConfigGatewayConfigArgsDict",
    "ApiConfigGatewayConfigBackendConfigArgs",
    "ApiConfigGatewayConfigBackendConfigArgsDict",
    "ApiConfigGrpcServiceArgs",
    "ApiConfigGrpcServiceArgsDict",
    "ApiConfigGrpcServiceFileDescriptorSetArgs",
    "ApiConfigGrpcServiceFileDescriptorSetArgsDict",
    "ApiConfigGrpcServiceSourceArgs",
    "ApiConfigGrpcServiceSourceArgsDict",
    "ApiConfigIamBindingConditionArgs",
    "ApiConfigIamBindingConditionArgsDict",
    "ApiConfigIamMemberConditionArgs",
    "ApiConfigIamMemberConditionArgsDict",
    "ApiConfigManagedServiceConfigArgs",
    "ApiConfigManagedServiceConfigArgsDict",
    "ApiConfigOpenapiDocumentArgs",
    "ApiConfigOpenapiDocumentArgsDict",
    "ApiConfigOpenapiDocumentDocumentArgs",
    "ApiConfigOpenapiDocumentDocumentArgsDict",
    "ApiIamBindingConditionArgs",
    "ApiIamBindingConditionArgsDict",
    "ApiIamMemberConditionArgs",
    "ApiIamMemberConditionArgsDict",
    "GatewayIamBindingConditionArgs",
    "GatewayIamBindingConditionArgsDict",
    "GatewayIamMemberConditionArgs",
    "GatewayIamMemberConditionArgsDict",
]

class ApiConfigGatewayConfigArgsDict(TypedDict):
    backend_config: pulumi.Input[ApiConfigGatewayConfigBackendConfigArgsDict]
    ...

@pulumi.input_type
class ApiConfigGatewayConfigArgs:
    def __init__(
        __self__,
        *,
        backend_config: pulumi.Input[ApiConfigGatewayConfigBackendConfigArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendConfig")
    def backend_config(
        self,
    ) -> pulumi.Input[ApiConfigGatewayConfigBackendConfigArgs]: ...
    @backend_config.setter
    def backend_config(
        self, value: pulumi.Input[ApiConfigGatewayConfigBackendConfigArgs]
    ): ...

class ApiConfigGatewayConfigBackendConfigArgsDict(TypedDict):
    google_service_account: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ApiConfigGatewayConfigBackendConfigArgs:
    def __init__(
        __self__, *, google_service_account: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="googleServiceAccount")
    def google_service_account(self) -> pulumi.Input[_builtins.str]: ...
    @google_service_account.setter
    def google_service_account(self, value: pulumi.Input[_builtins.str]): ...

class ApiConfigGrpcServiceArgsDict(TypedDict):
    file_descriptor_set: pulumi.Input[ApiConfigGrpcServiceFileDescriptorSetArgsDict]
    sources: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceSourceArgsDict]]]
    ]
    ...

@pulumi.input_type
class ApiConfigGrpcServiceArgs:
    def __init__(
        __self__,
        *,
        file_descriptor_set: pulumi.Input[ApiConfigGrpcServiceFileDescriptorSetArgs],
        sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceSourceArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileDescriptorSet")
    def file_descriptor_set(
        self,
    ) -> pulumi.Input[ApiConfigGrpcServiceFileDescriptorSetArgs]: ...
    @file_descriptor_set.setter
    def file_descriptor_set(
        self, value: pulumi.Input[ApiConfigGrpcServiceFileDescriptorSetArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceSourceArgs]]]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceSourceArgs]]]
        ],
    ): ...

class ApiConfigGrpcServiceFileDescriptorSetArgsDict(TypedDict):
    contents: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ApiConfigGrpcServiceFileDescriptorSetArgs:
    def __init__(
        __self__,
        *,
        contents: pulumi.Input[_builtins.str],
        path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def contents(self) -> pulumi.Input[_builtins.str]: ...
    @contents.setter
    def contents(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class ApiConfigGrpcServiceSourceArgsDict(TypedDict):
    contents: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ApiConfigGrpcServiceSourceArgs:
    def __init__(
        __self__,
        *,
        contents: pulumi.Input[_builtins.str],
        path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def contents(self) -> pulumi.Input[_builtins.str]: ...
    @contents.setter
    def contents(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class ApiConfigIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApiConfigIamBindingConditionArgs:
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

class ApiConfigIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApiConfigIamMemberConditionArgs:
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

class ApiConfigManagedServiceConfigArgsDict(TypedDict):
    contents: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ApiConfigManagedServiceConfigArgs:
    def __init__(
        __self__,
        *,
        contents: pulumi.Input[_builtins.str],
        path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def contents(self) -> pulumi.Input[_builtins.str]: ...
    @contents.setter
    def contents(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class ApiConfigOpenapiDocumentArgsDict(TypedDict):
    document: pulumi.Input[ApiConfigOpenapiDocumentDocumentArgsDict]
    ...

@pulumi.input_type
class ApiConfigOpenapiDocumentArgs:
    def __init__(
        __self__, *, document: pulumi.Input[ApiConfigOpenapiDocumentDocumentArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def document(self) -> pulumi.Input[ApiConfigOpenapiDocumentDocumentArgs]: ...
    @document.setter
    def document(self, value: pulumi.Input[ApiConfigOpenapiDocumentDocumentArgs]): ...

class ApiConfigOpenapiDocumentDocumentArgsDict(TypedDict):
    contents: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ApiConfigOpenapiDocumentDocumentArgs:
    def __init__(
        __self__,
        *,
        contents: pulumi.Input[_builtins.str],
        path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def contents(self) -> pulumi.Input[_builtins.str]: ...
    @contents.setter
    def contents(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class ApiIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApiIamBindingConditionArgs:
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

class ApiIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApiIamMemberConditionArgs:
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

class GatewayIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GatewayIamBindingConditionArgs:
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

class GatewayIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GatewayIamMemberConditionArgs:
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
