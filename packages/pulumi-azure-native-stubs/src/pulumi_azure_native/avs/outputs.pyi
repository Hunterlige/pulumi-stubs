

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AddonArcPropertiesResponse', 'AddonHcxPropertiesResponse', 'AddonSrmPropertiesResponse', 'AddonVrPropertiesResponse', 'AvailabilityPropertiesResponse', 'CircuitResponse', 'ClusterZoneResponse', 'DiskPoolVolumeResponse', 'ElasticSanVolumeResponse', 'EncryptionKeyVaultPropertiesResponse', 'EncryptionResponse', 'EndpointsResponse', 'IdentitySourceResponse', 'LabelResponse', 'ManagementClusterResponse', 'NetAppVolumeResponse', 'PSCredentialExecutionParameterResponse', 'ScriptSecureStringExecutionParameterResponse', 'ScriptStringExecutionParameterResponse', 'SkuResponse', 'SystemAssignedServiceIdentityResponse', 'SystemDataResponse', 'VmHostPlacementPolicyPropertiesResponse', 'VmVmPlacementPolicyPropertiesResponse', 'VmwareFirewallLicensePropertiesResponse', 'WorkloadNetworkDhcpRelayResponse', 'WorkloadNetworkDhcpServerResponse', 'WorkloadNetworkSegmentPortVifResponse', 'WorkloadNetworkSegmentSubnetResponse']
@pulumi.output_type
class AddonArcPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addon_type: _builtins.str, provisioning_state: _builtins.str, v_center: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonType")
    def addon_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenter")
    def v_center(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AddonHcxPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addon_type: _builtins.str, offer: _builtins.str, provisioning_state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonType")
    def addon_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AddonSrmPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addon_type: _builtins.str, provisioning_state: _builtins.str, license_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonType")
    def addon_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AddonVrPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addon_type: _builtins.str, provisioning_state: _builtins.str, vrs_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonType")
    def addon_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vrsCount")
    def vrs_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AvailabilityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secondary_zone: Optional[_builtins.int] = ..., strategy: Optional[_builtins.str] = ..., zone: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryZone")
    def secondary_zone(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CircuitResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, express_route_id: _builtins.str, express_route_private_peering_id: _builtins.str, primary_subnet: _builtins.str, secondary_subnet: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteID")
    def express_route_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRoutePrivatePeeringID")
    def express_route_private_peering_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primarySubnet")
    def primary_subnet(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondarySubnet")
    def secondary_subnet(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterZoneResponse(dict):
    
    def __init__(__self__, *, hosts: Sequence[_builtins.str], zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DiskPoolVolumeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lun_name: _builtins.str, path: _builtins.str, target_id: _builtins.str, mount_option: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lunName")
    def lun_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOption")
    def mount_option(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ElasticSanVolumeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionKeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_detected_key_version: _builtins.str, key_state: _builtins.str, version_type: _builtins.str, key_name: Optional[_builtins.str] = ..., key_vault_url: Optional[_builtins.str] = ..., key_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDetectedKeyVersion")
    def auto_detected_key_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyState")
    def key_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionType")
    def version_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_vault_properties: Optional[outputs.EncryptionKeyVaultPropertiesResponse] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.EncryptionKeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hcx_cloud_manager: _builtins.str, hcx_cloud_manager_ip: _builtins.str, nsxt_manager: _builtins.str, nsxt_manager_ip: _builtins.str, vcenter_ip: _builtins.str, vcsa: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hcxCloudManager")
    def hcx_cloud_manager(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hcxCloudManagerIp")
    def hcx_cloud_manager_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nsxtManager")
    def nsxt_manager(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nsxtManagerIp")
    def nsxt_manager_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcenterIp")
    def vcenter_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vcsa(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IdentitySourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alias: Optional[_builtins.str] = ..., base_group_dn: Optional[_builtins.str] = ..., base_user_dn: Optional[_builtins.str] = ..., domain: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., password: Optional[_builtins.str] = ..., primary_server: Optional[_builtins.str] = ..., secondary_server: Optional[_builtins.str] = ..., ssl: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseGroupDN")
    def base_group_dn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseUserDN")
    def base_user_dn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryServer")
    def primary_server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryServer")
    def secondary_server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LabelResponse(dict):
    
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagementClusterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_id: _builtins.int, provisioning_state: _builtins.str, cluster_size: Optional[_builtins.int] = ..., hosts: Optional[Sequence[_builtins.str]] = ..., vsan_datastore_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSize")
    def cluster_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vsanDatastoreName")
    def vsan_datastore_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetAppVolumeResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PSCredentialExecutionParameterResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str, password: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScriptSecureStringExecutionParameterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str, secure_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureValue")
    def secure_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScriptStringExecutionParameterResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemAssignedServiceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmHostPlacementPolicyPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, affinity_type: _builtins.str, host_members: Sequence[_builtins.str], provisioning_state: _builtins.str, type: _builtins.str, vm_members: Sequence[_builtins.str], affinity_strength: Optional[_builtins.str] = ..., azure_hybrid_benefit_type: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="affinityType")
    def affinity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostMembers")
    def host_members(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmMembers")
    def vm_members(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="affinityStrength")
    def affinity_strength(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridBenefitType")
    def azure_hybrid_benefit_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmVmPlacementPolicyPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, affinity_type: _builtins.str, provisioning_state: _builtins.str, type: _builtins.str, vm_members: Sequence[_builtins.str], display_name: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="affinityType")
    def affinity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmMembers")
    def vm_members(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareFirewallLicensePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cores: _builtins.int, end_date: _builtins.str, kind: _builtins.str, provisioning_state: _builtins.str, broadcom_contract_number: Optional[_builtins.str] = ..., broadcom_site_id: Optional[_builtins.str] = ..., labels: Optional[Sequence[outputs.LabelResponse]] = ..., license_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cores(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="broadcomContractNumber")
    def broadcom_contract_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="broadcomSiteId")
    def broadcom_site_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[outputs.LabelResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadNetworkDhcpRelayResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dhcp_type: _builtins.str, provisioning_state: _builtins.str, segments: Sequence[_builtins.str], display_name: Optional[_builtins.str] = ..., revision: Optional[_builtins.float] = ..., server_addresses: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dhcpType")
    def dhcp_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverAddresses")
    def server_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkloadNetworkDhcpServerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dhcp_type: _builtins.str, provisioning_state: _builtins.str, segments: Sequence[_builtins.str], display_name: Optional[_builtins.str] = ..., lease_time: Optional[_builtins.float] = ..., revision: Optional[_builtins.float] = ..., server_address: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dhcpType")
    def dhcp_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="leaseTime")
    def lease_time(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverAddress")
    def server_address(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadNetworkSegmentPortVifResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadNetworkSegmentSubnetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dhcp_ranges: Optional[Sequence[_builtins.str]] = ..., gateway_address: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dhcpRanges")
    def dhcp_ranges(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayAddress")
    def gateway_address(self) -> Optional[_builtins.str]:
        
        ...
    


