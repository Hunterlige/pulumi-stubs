import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountResourceResponseProperties",
    "CorsRuleResponse",
    "EndpointAuthenticationResponse",
    "ManagedServiceIdentityResponse",
    "ModelingInputDataResponse",
    "ModelingResourceResponseProperties",
    "ServiceEndpointResourceResponseProperties",
    "SystemDataResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class AccountResourceResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        configuration: Optional[_builtins.str] = ...,
        cors: Optional[Sequence[outputs.CorsRuleResponse]] = ...,
        endpoint_authentications: Optional[
            Sequence[outputs.EndpointAuthenticationResponse]
        ] = ...,
        reports_connection_string: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[Sequence[outputs.CorsRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointAuthentications")
    def endpoint_authentications(
        self,
    ) -> Optional[Sequence[outputs.EndpointAuthenticationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="reportsConnectionString")
    def reports_connection_string(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CorsRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_origins: Sequence[_builtins.str],
        allowed_headers: Optional[Sequence[_builtins.str]] = ...,
        allowed_methods: Optional[Sequence[_builtins.str]] = ...,
        exposed_headers: Optional[Sequence[_builtins.str]] = ...,
        max_age_in_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exposedHeaders")
    def exposed_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointAuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aad_tenant_id: Optional[_builtins.str] = ...,
        principal_id: Optional[_builtins.str] = ...,
        principal_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadTenantID")
    def aad_tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalID")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class ModelingInputDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, connection_string: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ModelingResourceResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        features: Optional[_builtins.str] = ...,
        frequency: Optional[_builtins.str] = ...,
        input_data: Optional[outputs.ModelingInputDataResponse] = ...,
        size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def features(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputData")
    def input_data(self) -> Optional[outputs.ModelingInputDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceEndpointResourceResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        paired_location: _builtins.str,
        provisioning_state: _builtins.str,
        url: _builtins.str,
        pre_allocated_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pairedLocation")
    def paired_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preAllocatedCapacity")
    def pre_allocated_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
