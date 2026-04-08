import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssignmentLockSettingsResponse",
    "AssignmentStatusResponse",
    "BlueprintStatusResponse",
    "KeyVaultReferenceResponse",
    "ManagedServiceIdentityResponse",
    "ParameterDefinitionResponse",
    "ParameterValueResponse",
    "ResourceGroupDefinitionResponse",
    "ResourceGroupValueResponse",
    "SecretValueReferenceResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class AssignmentLockSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        excluded_actions: Optional[Sequence[_builtins.str]] = ...,
        excluded_principals: Optional[Sequence[_builtins.str]] = ...,
        mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludedActions")
    def excluded_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedPrincipals")
    def excluded_principals(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssignmentStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_modified: _builtins.str,
        managed_resources: Sequence[_builtins.str],
        time_created: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedResources")
    def managed_resources(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str: ...

@pulumi.output_type
class BlueprintStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, last_modified: _builtins.str, time_created: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str: ...

@pulumi.output_type
class KeyVaultReferenceResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        principal_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class ParameterDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        allowed_values: Optional[Sequence[Any]] = ...,
        default_value: Optional[Any] = ...,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        strong_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="strongType")
    def strong_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ParameterValueResponse(dict):
    def __init__(
        __self__,
        *,
        reference: Optional[outputs.SecretValueReferenceResponse] = ...,
        value: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reference(self) -> Optional[outputs.SecretValueReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...

@pulumi.output_type
class ResourceGroupDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        depends_on: Optional[Sequence[_builtins.str]] = ...,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        strong_type: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="strongType")
    def strong_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ResourceGroupValueResponse(dict):
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecretValueReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_vault: outputs.KeyVaultReferenceResponse,
        secret_name: _builtins.str,
        secret_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> outputs.KeyVaultReferenceResponse: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        principal_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
