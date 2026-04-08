import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerResult",
    "AwaitableGetServerResult",
    "get_server",
    "get_server_output",
]

@pulumi.output_type
class GetServerResult:
    def __init__(
        __self__,
        administrator_login=...,
        administrators=...,
        azure_api_version=...,
        external_governance_status=...,
        federated_client_id=...,
        fully_qualified_domain_name=...,
        id=...,
        identity=...,
        is_i_pv6_enabled=...,
        key_id=...,
        kind=...,
        location=...,
        minimal_tls_version=...,
        name=...,
        primary_user_assigned_identity_id=...,
        private_endpoint_connections=...,
        public_network_access=...,
        restrict_outbound_network_access=...,
        state=...,
        tags=...,
        type=...,
        version=...,
        workspace_feature=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def administrators(
        self,
    ) -> Optional[outputs.ServerExternalAdministratorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalGovernanceStatus")
    def external_governance_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="federatedClientId")
    def federated_client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ResourceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isIPv6Enabled")
    def is_i_pv6_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.ServerPrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restrictOutboundNetworkAccess")
    def restrict_outbound_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceFeature")
    def workspace_feature(self) -> _builtins.str: ...

class AwaitableGetServerResult(GetServerResult):
    def __await__(self): ...

def get_server(
    expand: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerResult: ...
def get_server_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerResult]: ...
