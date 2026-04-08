import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterResult",
    "AwaitableGetClusterResult",
    "get_cluster",
    "get_cluster_output",
]

@pulumi.output_type
class GetClusterResult:
    def __init__(
        __self__,
        aad_application_object_id=...,
        aad_client_id=...,
        aad_service_principal_object_id=...,
        aad_tenant_id=...,
        azure_api_version=...,
        billing_model=...,
        cloud_id=...,
        cloud_management_endpoint=...,
        connectivity_status=...,
        desired_properties=...,
        id=...,
        isolated_vm_attestation_configuration=...,
        last_billing_timestamp=...,
        last_sync_timestamp=...,
        location=...,
        log_collection_properties=...,
        name=...,
        principal_id=...,
        provisioning_state=...,
        registration_timestamp=...,
        remote_support_properties=...,
        reported_properties=...,
        resource_provider_object_id=...,
        service_endpoint=...,
        software_assurance_properties=...,
        status=...,
        system_data=...,
        tags=...,
        tenant_id=...,
        trial_days_remaining=...,
        type=...,
        user_assigned_identities=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadApplicationObjectId")
    def aad_application_object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aadClientId")
    def aad_client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aadServicePrincipalObjectId")
    def aad_service_principal_object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudManagementEndpoint")
    def cloud_management_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectivityStatus")
    def connectivity_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="desiredProperties")
    def desired_properties(
        self,
    ) -> Optional[outputs.ClusterDesiredPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isolatedVmAttestationConfiguration")
    def isolated_vm_attestation_configuration(
        self,
    ) -> outputs.IsolatedVmAttestationConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="lastBillingTimestamp")
    def last_billing_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastSyncTimestamp")
    def last_sync_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logCollectionProperties")
    def log_collection_properties(
        self,
    ) -> Optional[outputs.LogCollectionPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registrationTimestamp")
    def registration_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remoteSupportProperties")
    def remote_support_properties(
        self,
    ) -> Optional[outputs.RemoteSupportPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="reportedProperties")
    def reported_properties(self) -> outputs.ClusterReportedPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderObjectId")
    def resource_provider_object_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceProperties")
    def software_assurance_properties(
        self,
    ) -> Optional[outputs.SoftwareAssurancePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trialDaysRemaining")
    def trial_days_remaining(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): ...

def get_cluster(
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterResult: ...
def get_cluster_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterResult]: ...
