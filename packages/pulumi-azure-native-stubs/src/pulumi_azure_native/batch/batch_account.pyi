import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BatchAccountArgs", "BatchAccount"]

@pulumi.input_type
class BatchAccountArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        allowed_authentication_modes: Optional[
            pulumi.Input[Sequence[pulumi.Input[AuthenticationMode]]]
        ] = ...,
        auto_storage: Optional[pulumi.Input[AutoStorageBasePropertiesArgs]] = ...,
        encryption: Optional[pulumi.Input[EncryptionPropertiesArgs]] = ...,
        identity: Optional[pulumi.Input[BatchAccountIdentityArgs]] = ...,
        key_vault_reference: Optional[pulumi.Input[KeyVaultReferenceArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ...,
        pool_allocation_mode: Optional[pulumi.Input[PoolAllocationMode]] = ...,
        public_network_access: Optional[pulumi.Input[PublicNetworkAccessType]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allowedAuthenticationModes")
    def allowed_authentication_modes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthenticationMode]]]]: ...
    @allowed_authentication_modes.setter
    def allowed_authentication_modes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthenticationMode]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoStorage")
    def auto_storage(self) -> Optional[pulumi.Input[AutoStorageBasePropertiesArgs]]: ...
    @auto_storage.setter
    def auto_storage(
        self, value: Optional[pulumi.Input[AutoStorageBasePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionPropertiesArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[BatchAccountIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[BatchAccountIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultReference")
    def key_vault_reference(self) -> Optional[pulumi.Input[KeyVaultReferenceArgs]]: ...
    @key_vault_reference.setter
    def key_vault_reference(
        self, value: Optional[pulumi.Input[KeyVaultReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="poolAllocationMode")
    def pool_allocation_mode(self) -> Optional[pulumi.Input[PoolAllocationMode]]: ...
    @pool_allocation_mode.setter
    def pool_allocation_mode(
        self, value: Optional[pulumi.Input[PoolAllocationMode]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[PublicNetworkAccessType]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[PublicNetworkAccessType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:batch:BatchAccount")
class BatchAccount(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        allowed_authentication_modes: Optional[
            pulumi.Input[Sequence[pulumi.Input[AuthenticationMode]]]
        ] = ...,
        auto_storage: Optional[
            pulumi.Input[
                Union[AutoStorageBasePropertiesArgs, AutoStorageBasePropertiesArgsDict]
            ]
        ] = ...,
        encryption: Optional[
            pulumi.Input[Union[EncryptionPropertiesArgs, EncryptionPropertiesArgsDict]]
        ] = ...,
        identity: Optional[
            pulumi.Input[Union[BatchAccountIdentityArgs, BatchAccountIdentityArgsDict]]
        ] = ...,
        key_vault_reference: Optional[
            pulumi.Input[Union[KeyVaultReferenceArgs, KeyVaultReferenceArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[
            pulumi.Input[Union[NetworkProfileArgs, NetworkProfileArgsDict]]
        ] = ...,
        pool_allocation_mode: Optional[pulumi.Input[PoolAllocationMode]] = ...,
        public_network_access: Optional[pulumi.Input[PublicNetworkAccessType]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BatchAccountArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> BatchAccount: ...
    @_builtins.property
    @pulumi.getter(name="accountEndpoint")
    def account_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="activeJobAndJobScheduleQuota")
    def active_job_and_job_schedule_quota(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="allowedAuthenticationModes")
    def allowed_authentication_modes(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="autoStorage")
    def auto_storage(self) -> pulumi.Output[outputs.AutoStoragePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedCoreQuota")
    def dedicated_core_quota(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedCoreQuotaPerVMFamily")
    def dedicated_core_quota_per_vm_family(
        self,
    ) -> pulumi.Output[Sequence[outputs.VirtualMachineFamilyCoreQuotaResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedCoreQuotaPerVMFamilyEnforced")
    def dedicated_core_quota_per_vm_family_enforced(
        self,
    ) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[outputs.EncryptionPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.BatchAccountIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultReference")
    def key_vault_reference(
        self,
    ) -> pulumi.Output[outputs.KeyVaultReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lowPriorityCoreQuota")
    def low_priority_core_quota(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.NetworkProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeManagementEndpoint")
    def node_management_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="poolAllocationMode")
    def pool_allocation_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="poolQuota")
    def pool_quota(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
