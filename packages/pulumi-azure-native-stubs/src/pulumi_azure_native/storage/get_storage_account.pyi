import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStorageAccountResult",
    "AwaitableGetStorageAccountResult",
    "get_storage_account",
    "get_storage_account_output",
]

@pulumi.output_type
class GetStorageAccountResult:
    def __init__(
        __self__,
        access_tier=...,
        account_migration_in_progress=...,
        allow_blob_public_access=...,
        allow_cross_tenant_replication=...,
        allow_shared_key_access=...,
        allowed_copy_scope=...,
        azure_api_version=...,
        azure_files_identity_based_authentication=...,
        blob_restore_status=...,
        creation_time=...,
        custom_domain=...,
        default_to_o_auth_authentication=...,
        dns_endpoint_type=...,
        enable_extended_groups=...,
        enable_https_traffic_only=...,
        enable_nfs_v3=...,
        encryption=...,
        extended_location=...,
        failover_in_progress=...,
        geo_replication_stats=...,
        id=...,
        identity=...,
        immutable_storage_with_versioning=...,
        is_hns_enabled=...,
        is_local_user_enabled=...,
        is_sftp_enabled=...,
        is_sku_conversion_blocked=...,
        key_creation_time=...,
        key_policy=...,
        kind=...,
        large_file_shares_state=...,
        last_geo_failover_time=...,
        location=...,
        minimum_tls_version=...,
        name=...,
        network_rule_set=...,
        primary_endpoints=...,
        primary_location=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        public_network_access=...,
        routing_preference=...,
        sas_policy=...,
        secondary_endpoints=...,
        secondary_location=...,
        sku=...,
        status_of_primary=...,
        status_of_secondary=...,
        storage_account_sku_conversion_status=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountMigrationInProgress")
    def account_migration_in_progress(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowBlobPublicAccess")
    def allow_blob_public_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowCrossTenantReplication")
    def allow_cross_tenant_replication(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowSharedKeyAccess")
    def allow_shared_key_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowedCopyScope")
    def allowed_copy_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureFilesIdentityBasedAuthentication")
    def azure_files_identity_based_authentication(
        self,
    ) -> Optional[outputs.AzureFilesIdentityBasedAuthenticationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="blobRestoreStatus")
    def blob_restore_status(self) -> outputs.BlobRestoreStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> outputs.CustomDomainResponse: ...
    @_builtins.property
    @pulumi.getter(name="defaultToOAuthAuthentication")
    def default_to_o_auth_authentication(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dnsEndpointType")
    def dns_endpoint_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableExtendedGroups")
    def enable_extended_groups(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableHttpsTrafficOnly")
    def enable_https_traffic_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableNfsV3")
    def enable_nfs_v3(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> outputs.EncryptionResponse: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="failoverInProgress")
    def failover_in_progress(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="geoReplicationStats")
    def geo_replication_stats(self) -> outputs.GeoReplicationStatsResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="immutableStorageWithVersioning")
    def immutable_storage_with_versioning(
        self,
    ) -> Optional[outputs.ImmutableStorageAccountResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isHnsEnabled")
    def is_hns_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isLocalUserEnabled")
    def is_local_user_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isSftpEnabled")
    def is_sftp_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isSkuConversionBlocked")
    def is_sku_conversion_blocked(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="keyCreationTime")
    def key_creation_time(self) -> outputs.KeyCreationTimeResponse: ...
    @_builtins.property
    @pulumi.getter(name="keyPolicy")
    def key_policy(self) -> outputs.KeyPolicyResponse: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="largeFileSharesState")
    def large_file_shares_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastGeoFailoverTime")
    def last_geo_failover_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkRuleSet")
    def network_rule_set(self) -> outputs.NetworkRuleSetResponse: ...
    @_builtins.property
    @pulumi.getter(name="primaryEndpoints")
    def primary_endpoints(self) -> outputs.EndpointsResponse: ...
    @_builtins.property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingPreference")
    def routing_preference(self) -> Optional[outputs.RoutingPreferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sasPolicy")
    def sas_policy(self) -> outputs.SasPolicyResponse: ...
    @_builtins.property
    @pulumi.getter(name="secondaryEndpoints")
    def secondary_endpoints(self) -> outputs.EndpointsResponse: ...
    @_builtins.property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter(name="statusOfPrimary")
    def status_of_primary(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusOfSecondary")
    def status_of_secondary(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSkuConversionStatus")
    def storage_account_sku_conversion_status(
        self,
    ) -> Optional[outputs.StorageAccountSkuConversionStatusResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetStorageAccountResult(GetStorageAccountResult):
    def __await__(self): ...

def get_storage_account(
    account_name: Optional[_builtins.str] = ...,
    expand: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStorageAccountResult: ...
def get_storage_account_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStorageAccountResult]: ...
