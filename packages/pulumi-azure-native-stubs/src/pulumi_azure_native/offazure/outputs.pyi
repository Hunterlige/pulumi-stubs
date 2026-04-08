import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "HealthErrorDetailsResponse",
    "PrivateEndpointConnectionPropertiesResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "ResourceIdResponse",
    "SiteAgentPropertiesResponse",
    "SiteAppliancePropertiesResponse",
    "SiteHealthSummaryResponse",
    "SitePropertiesResponse",
    "SiteSpnPropertiesResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class HealthErrorDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        appliance_name: _builtins.str,
        code: _builtins.str,
        discovery_scope: _builtins.str,
        id: _builtins.float,
        message: _builtins.str,
        message_parameters: Mapping[str, _builtins.str],
        possible_causes: _builtins.str,
        recommended_action: _builtins.str,
        run_as_account_id: _builtins.str,
        severity: _builtins.str,
        source: _builtins.str,
        summary_message: _builtins.str,
        updated_time_stamp: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoveryScope")
    def discovery_scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messageParameters")
    def message_parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="summaryMessage")
    def summary_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedTimeStamp")
    def updated_time_stamp(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_endpoint: outputs.ResourceIdResponse,
        provisioning_state: _builtins.str,
        private_link_service_connection_state: Optional[
            outputs.PrivateLinkServiceConnectionStateResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.ResourceIdResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_ids: Sequence[_builtins.str],
        id: _builtins.str,
        name: _builtins.str,
        private_endpoint: outputs.ResourceIdResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_link_service_connection_state: Optional[
            outputs.PrivateLinkServiceConnectionStateResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.ResourceIdResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceIdResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class SiteAgentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        last_heart_beat_utc: _builtins.str,
        version: _builtins.str,
        key_vault_id: Optional[_builtins.str] = ...,
        key_vault_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastHeartBeatUtc")
    def last_heart_beat_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SiteAppliancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent_details: Optional[outputs.SiteAgentPropertiesResponse] = ...,
        appliance_name: Optional[_builtins.str] = ...,
        service_principal_identity_details: Optional[
            outputs.SiteSpnPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> Optional[outputs.SiteAgentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalIdentityDetails")
    def service_principal_identity_details(
        self,
    ) -> Optional[outputs.SiteSpnPropertiesResponse]: ...

@pulumi.output_type
class SiteHealthSummaryResponse(dict):
    def __init__(
        __self__,
        *,
        affected_resource_type: _builtins.str,
        appliance_name: _builtins.str,
        error_code: _builtins.str,
        error_id: _builtins.float,
        error_message: _builtins.str,
        remediation_guidance: _builtins.str,
        severity: _builtins.str,
        summary_message: _builtins.str,
        affected_objects_count: Optional[_builtins.float] = ...,
        affected_resources: Optional[Sequence[_builtins.str]] = ...,
        fabric_layout_update_sources: Optional[Sequence[_builtins.str]] = ...,
        hit_count: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="affectedResourceType")
    def affected_resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorId")
    def error_id(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remediationGuidance")
    def remediation_guidance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="summaryMessage")
    def summary_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="affectedObjectsCount")
    def affected_objects_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="affectedResources")
    def affected_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fabricLayoutUpdateSources")
    def fabric_layout_update_sources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hitCount")
    def hit_count(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class SitePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_endpoint: _builtins.str,
        agent_details: Optional[outputs.SiteAgentPropertiesResponse] = ...,
        appliance_name: Optional[_builtins.str] = ...,
        discovery_solution_id: Optional[_builtins.str] = ...,
        service_principal_identity_details: Optional[
            outputs.SiteSpnPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> Optional[outputs.SiteAgentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="discoverySolutionId")
    def discovery_solution_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalIdentityDetails")
    def service_principal_identity_details(
        self,
    ) -> Optional[outputs.SiteSpnPropertiesResponse]: ...

@pulumi.output_type
class SiteSpnPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aad_authority: Optional[_builtins.str] = ...,
        application_id: Optional[_builtins.str] = ...,
        audience: Optional[_builtins.str] = ...,
        object_id: Optional[_builtins.str] = ...,
        raw_cert_data: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadAuthority")
    def aad_authority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rawCertData")
    def raw_cert_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

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
