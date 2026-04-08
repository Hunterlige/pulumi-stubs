import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssignmentLockSettingsArgs",
    "AssignmentLockSettingsArgsDict",
    "KeyVaultReferenceArgs",
    "KeyVaultReferenceArgsDict",
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "ParameterDefinitionArgs",
    "ParameterDefinitionArgsDict",
    "ParameterValueArgs",
    "ParameterValueArgsDict",
    "ResourceGroupDefinitionArgs",
    "ResourceGroupDefinitionArgsDict",
    "ResourceGroupValueArgs",
    "ResourceGroupValueArgsDict",
    "SecretValueReferenceArgs",
    "SecretValueReferenceArgsDict",
    "UserAssignedIdentityArgs",
    "UserAssignedIdentityArgsDict",
]

class AssignmentLockSettingsArgsDict(TypedDict):
    excluded_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_principals: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, AssignmentLockMode]]]

@pulumi.input_type
class AssignmentLockSettingsArgs:
    def __init__(
        __self__,
        *,
        excluded_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_principals: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, AssignmentLockMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludedActions")
    def excluded_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_actions.setter
    def excluded_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedPrincipals")
    def excluded_principals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_principals.setter
    def excluded_principals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AssignmentLockMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AssignmentLockMode]]]
    ): ...

class KeyVaultReferenceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class KeyVaultReferenceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class ManagedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgsDict]]]
    ]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
    ]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserAssignedIdentityArgs]]]
        ],
    ): ...

class ParameterDefinitionArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, TemplateParameterType]]
    allowed_values: NotRequired[pulumi.Input[Sequence[Any]]]
    default_value: NotRequired[Any]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    strong_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ParameterDefinitionArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, TemplateParameterType]],
        allowed_values: Optional[pulumi.Input[Sequence[Any]]] = ...,
        default_value: Optional[Any] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, TemplateParameterType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, TemplateParameterType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[pulumi.Input[Sequence[Any]]]: ...
    @allowed_values.setter
    def allowed_values(self, value: Optional[pulumi.Input[Sequence[Any]]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[Any]: ...
    @default_value.setter
    def default_value(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strongType")
    def strong_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strong_type.setter
    def strong_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ParameterValueArgsDict(TypedDict):
    reference: NotRequired[pulumi.Input[SecretValueReferenceArgsDict]]
    value: NotRequired[Any]

@pulumi.input_type
class ParameterValueArgs:
    def __init__(
        __self__,
        *,
        reference: Optional[pulumi.Input[SecretValueReferenceArgs]] = ...,
        value: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reference(self) -> Optional[pulumi.Input[SecretValueReferenceArgs]]: ...
    @reference.setter
    def reference(self, value: Optional[pulumi.Input[SecretValueReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...
    @value.setter
    def value(self, value: Optional[Any]): ...

class ResourceGroupDefinitionArgsDict(TypedDict):
    depends_on: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    strong_type: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ResourceGroupDefinitionArgs:
    def __init__(
        __self__,
        *,
        depends_on: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @depends_on.setter
    def depends_on(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strongType")
    def strong_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strong_type.setter
    def strong_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceGroupValueArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceGroupValueArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecretValueReferenceArgsDict(TypedDict):
    key_vault: pulumi.Input[KeyVaultReferenceArgsDict]
    secret_name: pulumi.Input[_builtins.str]
    secret_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecretValueReferenceArgs:
    def __init__(
        __self__,
        *,
        key_vault: pulumi.Input[KeyVaultReferenceArgs],
        secret_name: pulumi.Input[_builtins.str],
        secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> pulumi.Input[KeyVaultReferenceArgs]: ...
    @key_vault.setter
    def key_vault(self, value: pulumi.Input[KeyVaultReferenceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_version.setter
    def secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserAssignedIdentityArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAssignedIdentityArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
