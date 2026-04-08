import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBatchAccountResult",
    "AwaitableGetBatchAccountResult",
    "get_batch_account",
    "get_batch_account_output",
]

@pulumi.output_type
class GetBatchAccountResult:
    def __init__(
        __self__,
        account_endpoint=...,
        active_job_and_job_schedule_quota=...,
        allowed_authentication_modes=...,
        auto_storage=...,
        azure_api_version=...,
        dedicated_core_quota=...,
        dedicated_core_quota_per_vm_family=...,
        dedicated_core_quota_per_vm_family_enforced=...,
        encryption=...,
        id=...,
        identity=...,
        key_vault_reference=...,
        location=...,
        low_priority_core_quota=...,
        name=...,
        network_profile=...,
        node_management_endpoint=...,
        pool_allocation_mode=...,
        pool_quota=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        public_network_access=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountEndpoint")
    def account_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="activeJobAndJobScheduleQuota")
    def active_job_and_job_schedule_quota(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="allowedAuthenticationModes")
    def allowed_authentication_modes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoStorage")
    def auto_storage(self) -> outputs.AutoStoragePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedCoreQuota")
    def dedicated_core_quota(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedCoreQuotaPerVMFamily")
    def dedicated_core_quota_per_vm_family(
        self,
    ) -> Sequence[outputs.VirtualMachineFamilyCoreQuotaResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedCoreQuotaPerVMFamilyEnforced")
    def dedicated_core_quota_per_vm_family_enforced(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> outputs.EncryptionPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.BatchAccountIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultReference")
    def key_vault_reference(self) -> outputs.KeyVaultReferenceResponse: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lowPriorityCoreQuota")
    def low_priority_core_quota(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="nodeManagementEndpoint")
    def node_management_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="poolAllocationMode")
    def pool_allocation_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="poolQuota")
    def pool_quota(self) -> _builtins.int: ...
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetBatchAccountResult(GetBatchAccountResult):
    def __await__(self): ...

def get_batch_account(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBatchAccountResult: ...
def get_batch_account_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBatchAccountResult]: ...
