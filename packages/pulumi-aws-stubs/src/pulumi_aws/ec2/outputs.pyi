

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AllowedImagesSettingsImageCriterion', ..., ..., 'AmiCopyEbsBlockDevice', 'AmiCopyEphemeralBlockDevice', 'AmiEbsBlockDevice', 'AmiEphemeralBlockDevice', 'AmiFromInstanceEbsBlockDevice', 'AmiFromInstanceEphemeralBlockDevice', 'CapacityBlockReservationTimeouts', 'DefaultCreditSpecificationTimeouts', 'DefaultNetworkAclEgress', 'DefaultNetworkAclIngress', 'DefaultRouteTableRoute', 'DefaultSecurityGroupEgress', 'DefaultSecurityGroupIngress', 'EipDomainNameTimeouts', 'EncryptionControlResourceExclusions', ..., ..., 'EncryptionControlResourceExclusionsInternetGateway', 'EncryptionControlResourceExclusionsLambda', 'EncryptionControlResourceExclusionsNatGateway', ..., 'EncryptionControlResourceExclusionsVpcLattice', 'EncryptionControlResourceExclusionsVpcPeering', 'EncryptionControlTimeouts', 'FleetFleetInstanceSet', 'FleetLaunchTemplateConfig', ..., 'FleetLaunchTemplateConfigOverride', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FleetOnDemandOptions', 'FleetOnDemandOptionsCapacityReservationOptions', 'FleetSpotOptions', 'FleetSpotOptionsMaintenanceStrategies', ..., 'FleetTargetCapacitySpecification', 'FlowLogDestinationOptions', 'InstanceCapacityReservationSpecification', ..., 'InstanceCpuOptions', 'InstanceCreditSpecification', 'InstanceEbsBlockDevice', 'InstanceEnclaveOptions', 'InstanceEphemeralBlockDevice', 'InstanceInstanceMarketOptions', 'InstanceInstanceMarketOptionsSpotOptions', 'InstanceLaunchTemplate', 'InstanceMaintenanceOptions', 'InstanceMetadataOptions', 'InstanceNetworkInterface', 'InstancePrimaryNetworkInterface', 'InstancePrivateDnsNameOptions', 'InstanceRootBlockDevice', 'InstanceSecondaryNetworkInterface', 'LaunchConfigurationEbsBlockDevice', 'LaunchConfigurationEphemeralBlockDevice', 'LaunchConfigurationMetadataOptions', 'LaunchConfigurationRootBlockDevice', 'LaunchTemplateBlockDeviceMapping', 'LaunchTemplateBlockDeviceMappingEbs', 'LaunchTemplateCapacityReservationSpecification', ..., 'LaunchTemplateCpuOptions', 'LaunchTemplateCreditSpecification', 'LaunchTemplateEnclaveOptions', 'LaunchTemplateHibernationOptions', 'LaunchTemplateIamInstanceProfile', 'LaunchTemplateInstanceMarketOptions', 'LaunchTemplateInstanceMarketOptionsSpotOptions', 'LaunchTemplateInstanceRequirements', 'LaunchTemplateInstanceRequirementsAcceleratorCount', ..., ..., 'LaunchTemplateInstanceRequirementsMemoryGibPerVcpu', 'LaunchTemplateInstanceRequirementsMemoryMib', ..., ..., ..., 'LaunchTemplateInstanceRequirementsVcpuCount', 'LaunchTemplateLicenseSpecification', 'LaunchTemplateMaintenanceOptions', 'LaunchTemplateMetadataOptions', 'LaunchTemplateMonitoring', 'LaunchTemplateNetworkInterface', ..., 'LaunchTemplateNetworkInterfaceEnaSrdSpecification', ..., 'LaunchTemplateNetworkPerformanceOptions', 'LaunchTemplatePlacement', 'LaunchTemplatePrivateDnsNameOptions', 'LaunchTemplateSecondaryInterface', 'LaunchTemplateTagSpecification', 'ManagedPrefixListEntry', 'NatGatewayAvailabilityZoneAddress', 'NatGatewayEipAssociationTimeouts', 'NatGatewayRegionalNatGatewayAddress', 'NetworkAclEgress', 'NetworkAclIngress', 'NetworkInsightsAnalysisAlternatePathHint', 'NetworkInsightsAnalysisExplanation', 'NetworkInsightsAnalysisExplanationAcl', 'NetworkInsightsAnalysisExplanationAclRule', 'NetworkInsightsAnalysisExplanationAclRulePortRange', 'NetworkInsightsAnalysisExplanationAttachedTo', ..., 'NetworkInsightsAnalysisExplanationComponent', 'NetworkInsightsAnalysisExplanationCustomerGateway', 'NetworkInsightsAnalysisExplanationDestination', 'NetworkInsightsAnalysisExplanationDestinationVpc', ..., ..., 'NetworkInsightsAnalysisExplanationInternetGateway', ..., 'NetworkInsightsAnalysisExplanationNatGateway', 'NetworkInsightsAnalysisExplanationNetworkInterface', 'NetworkInsightsAnalysisExplanationPortRange', 'NetworkInsightsAnalysisExplanationPrefixList', 'NetworkInsightsAnalysisExplanationRouteTable', 'NetworkInsightsAnalysisExplanationRouteTableRoute', 'NetworkInsightsAnalysisExplanationSecurityGroup', ..., ..., 'NetworkInsightsAnalysisExplanationSourceVpc', 'NetworkInsightsAnalysisExplanationSubnet', 'NetworkInsightsAnalysisExplanationSubnetRouteTable', 'NetworkInsightsAnalysisExplanationTransitGateway', ..., ..., ..., 'NetworkInsightsAnalysisExplanationVpc', 'NetworkInsightsAnalysisExplanationVpcEndpoint', ..., 'NetworkInsightsAnalysisExplanationVpnConnection', 'NetworkInsightsAnalysisExplanationVpnGateway', 'NetworkInsightsAnalysisForwardPathComponent', 'NetworkInsightsAnalysisForwardPathComponentAclRule', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'NetworkInsightsAnalysisForwardPathComponentSubnet', ..., ..., 'NetworkInsightsAnalysisForwardPathComponentVpc', 'NetworkInsightsAnalysisReturnPathComponent', 'NetworkInsightsAnalysisReturnPathComponentAclRule', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'NetworkInsightsAnalysisReturnPathComponentSubnet', ..., ..., 'NetworkInsightsAnalysisReturnPathComponentVpc', 'NetworkInsightsPathFilterAtDestination', ..., ..., 'NetworkInsightsPathFilterAtSource', ..., 'NetworkInsightsPathFilterAtSourceSourcePortRange', 'NetworkInterfaceAttachment', 'NetworkInterfacePermissionTimeouts', 'PeeringConnectionOptionsAccepter', 'PeeringConnectionOptionsRequester', 'RouteTableRoute', 'SecondaryNetworkIpv4CidrBlockAssociation', 'SecondaryNetworkTimeouts', 'SecondarySubnetIpv4CidrBlockAssociation', 'SecondarySubnetTimeouts', 'SecurityGroupEgress', 'SecurityGroupIngress', 'SpotFleetRequestLaunchSpecification', 'SpotFleetRequestLaunchSpecificationEbsBlockDevice', ..., 'SpotFleetRequestLaunchSpecificationRootBlockDevice', 'SpotFleetRequestLaunchTemplateConfig', ..., 'SpotFleetRequestLaunchTemplateConfigOverride', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'SpotFleetRequestSpotMaintenanceStrategies', ..., ..., ..., 'SpotInstanceRequestCpuOptions', 'SpotInstanceRequestCreditSpecification', 'SpotInstanceRequestEbsBlockDevice', 'SpotInstanceRequestEnclaveOptions', 'SpotInstanceRequestEphemeralBlockDevice', 'SpotInstanceRequestLaunchTemplate', 'SpotInstanceRequestMaintenanceOptions', 'SpotInstanceRequestMetadataOptions', 'SpotInstanceRequestNetworkInterface', 'SpotInstanceRequestPrimaryNetworkInterface', 'SpotInstanceRequestPrivateDnsNameOptions', 'SpotInstanceRequestRootBlockDevice', 'SpotInstanceRequestSecondaryNetworkInterface', 'TrafficMirrorFilterRuleDestinationPortRange', 'TrafficMirrorFilterRuleSourcePortRange', 'VpcBlockPublicAccessExclusionTimeouts', 'VpcBlockPublicAccessOptionsTimeouts', 'VpcEncryptionControlResourceExclusions', ..., ..., ..., 'VpcEncryptionControlResourceExclusionsLambda', 'VpcEncryptionControlResourceExclusionsNatGateway', ..., 'VpcEncryptionControlResourceExclusionsVpcLattice', 'VpcEncryptionControlResourceExclusionsVpcPeering', 'VpcEncryptionControlTimeouts', 'VpcEndpointDnsEntry', 'VpcEndpointDnsOptions', 'VpcEndpointServicePrivateDnsNameConfiguration', 'VpcEndpointSubnetConfiguration', 'VpcIpamOperatingRegion', 'VpcIpamPoolCidrCidrAuthorizationContext', 'VpcIpamPoolSourceResource', 'VpcIpamResourceDiscoveryOperatingRegion', ..., 'VpcPeeringConnectionAccepter', 'VpcPeeringConnectionAccepterAccepter', 'VpcPeeringConnectionAccepterRequester', 'VpcPeeringConnectionRequester', 'VpnConnectionRoute', 'VpnConnectionTunnel1LogOptions', 'VpnConnectionTunnel1LogOptionsCloudwatchLogOptions', 'VpnConnectionTunnel2LogOptions', 'VpnConnectionTunnel2LogOptionsCloudwatchLogOptions', 'VpnConnectionVgwTelemetry', 'GetAmiBlockDeviceMappingResult', 'GetAmiFilterResult', 'GetAmiIdsFilterResult', 'GetAmiProductCodeResult', 'GetCoipPoolFilterResult', 'GetCoipPoolsFilterResult', 'GetCustomerGatewayFilterResult', 'GetDedicatedHostFilterResult', 'GetEipsFilterResult', 'GetElasticIpFilterResult', 'GetInstanceCreditSpecificationResult', 'GetInstanceEbsBlockDeviceResult', 'GetInstanceEnclaveOptionResult', 'GetInstanceEphemeralBlockDeviceResult', 'GetInstanceFilterResult', 'GetInstanceMaintenanceOptionResult', 'GetInstanceMetadataOptionResult', 'GetInstancePrivateDnsNameOptionResult', 'GetInstanceRootBlockDeviceResult', 'GetInstanceTypeFpgaResult', 'GetInstanceTypeGpusResult', 'GetInstanceTypeInferenceAcceleratorResult', 'GetInstanceTypeInstanceDiskResult', 'GetInstanceTypeMediaAcceleratorResult', 'GetInstanceTypeNetworkCardResult', 'GetInstanceTypeNeuronDeviceResult', 'GetInstanceTypeOfferingFilterResult', 'GetInstanceTypeOfferingsFilterResult', 'GetInstanceTypesFilterResult', 'GetInstancesFilterResult', 'GetInternetGatewayAttachmentResult', 'GetInternetGatewayFilterResult', 'GetKeyPairFilterResult', 'GetLaunchConfigurationEbsBlockDeviceResult', 'GetLaunchConfigurationEphemeralBlockDeviceResult', 'GetLaunchConfigurationMetadataOptionResult', 'GetLaunchConfigurationRootBlockDeviceResult', 'GetLaunchTemplateBlockDeviceMappingResult', 'GetLaunchTemplateBlockDeviceMappingEbResult', ..., ..., 'GetLaunchTemplateCpuOptionResult', 'GetLaunchTemplateCreditSpecificationResult', 'GetLaunchTemplateEnclaveOptionResult', 'GetLaunchTemplateFilterResult', 'GetLaunchTemplateHibernationOptionResult', 'GetLaunchTemplateIamInstanceProfileResult', 'GetLaunchTemplateInstanceMarketOptionResult', ..., 'GetLaunchTemplateInstanceRequirementResult', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetLaunchTemplateLicenseSpecificationResult', 'GetLaunchTemplateMaintenanceOptionResult', 'GetLaunchTemplateMetadataOptionResult', 'GetLaunchTemplateMonitoringResult', 'GetLaunchTemplateNetworkInterfaceResult', ..., 'GetLaunchTemplateNetworkPerformanceOptionResult', 'GetLaunchTemplatePlacementResult', 'GetLaunchTemplatePrivateDnsNameOptionResult', 'GetLaunchTemplateSecondaryInterfaceResult', 'GetLaunchTemplateTagSpecificationResult', 'GetLocalGatewayFilterResult', 'GetLocalGatewayRouteTableFilterResult', 'GetLocalGatewayRouteTablesFilterResult', 'GetLocalGatewayVirtualInterfaceFilterResult', 'GetLocalGatewayVirtualInterfaceGroupFilterResult', 'GetLocalGatewayVirtualInterfaceGroupsFilterResult', 'GetLocalGatewaysFilterResult', 'GetManagedPrefixListEntryResult', 'GetManagedPrefixListFilterResult', 'GetManagedPrefixListsFilterResult', 'GetNatGatewayAvailabilityZoneAddressResult', 'GetNatGatewayFilterResult', 'GetNatGatewayRegionalNatGatewayAddressResult', 'GetNatGatewaysFilterResult', 'GetNetworkAclsFilterResult', 'GetNetworkInsightsAnalysisAlternatePathHintResult', 'GetNetworkInsightsAnalysisExplanationResult', 'GetNetworkInsightsAnalysisExplanationAclResult', 'GetNetworkInsightsAnalysisExplanationAclRuleResult', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetNetworkInsightsAnalysisExplanationSubnetResult', ..., ..., ..., ..., ..., 'GetNetworkInsightsAnalysisExplanationVpcResult', ..., ..., ..., ..., 'GetNetworkInsightsAnalysisFilterResult', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetNetworkInsightsPathFilterResult', 'GetNetworkInsightsPathFilterAtDestinationResult', ..., ..., 'GetNetworkInsightsPathFilterAtSourceResult', ..., ..., 'GetNetworkInterfaceAssociationResult', 'GetNetworkInterfaceAttachmentResult', 'GetNetworkInterfaceFilterResult', 'GetNetworkInterfacesFilterResult', 'GetPrefixListFilterResult', 'GetPublicIpv4PoolPoolAddressRangeResult', 'GetPublicIpv4PoolsFilterResult', 'GetRouteTableAssociationResult', 'GetRouteTableFilterResult', 'GetRouteTableRouteResult', 'GetRouteTablesFilterResult', 'GetSecurityGroupFilterResult', 'GetSecurityGroupsFilterResult', 'GetSpotPriceFilterResult', 'GetSubnetFilterResult', 'GetSubnetsFilterResult', 'GetTransitGatewayRouteTablesFilterResult', 'GetVpcCidrBlockAssociationResult', 'GetVpcDhcpOptionsFilterResult', 'GetVpcEndpointDnsEntryResult', 'GetVpcEndpointDnsOptionResult', 'GetVpcEndpointFilterResult', 'GetVpcEndpointServiceFilterResult', 'GetVpcFilterResult', 'GetVpcIpamOperatingRegionResult', 'GetVpcIpamPoolCidrsFilterResult', 'GetVpcIpamPoolCidrsIpamPoolCidrResult', 'GetVpcIpamPoolFilterResult', 'GetVpcIpamPoolSourceResourceResult', 'GetVpcIpamPoolsFilterResult', 'GetVpcIpamPoolsIpamPoolResult', 'GetVpcIpamsFilterResult', 'GetVpcIpamsIpamResult', 'GetVpcIpamsIpamOperatingRegionResult', 'GetVpcPeeringConnectionCidrBlockSetResult', 'GetVpcPeeringConnectionFilterResult', 'GetVpcPeeringConnectionIpv6CidrBlockSetResult', 'GetVpcPeeringConnectionPeerCidrBlockSetResult', 'GetVpcPeeringConnectionPeerIpv6CidrBlockSetResult', 'GetVpcPeeringConnectionsFilterResult', 'GetVpcsFilterResult', 'GetVpnConnectionFilterResult', 'GetVpnConnectionRouteResult', 'GetVpnConnectionVgwTelemetryResult', 'GetVpnGatewayFilterResult']
@pulumi.output_type
class AllowedImagesSettingsImageCriterion(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_date_condition: Optional[outputs.AllowedImagesSettingsImageCriterionCreationDateCondition] = ..., deprecation_time_condition: Optional[outputs.AllowedImagesSettingsImageCriterionDeprecationTimeCondition] = ..., image_names: Optional[Sequence[_builtins.str]] = ..., image_providers: Optional[Sequence[_builtins.str]] = ..., marketplace_product_codes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDateCondition")
    def creation_date_condition(self) -> Optional[outputs.AllowedImagesSettingsImageCriterionCreationDateCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deprecationTimeCondition")
    def deprecation_time_condition(self) -> Optional[outputs.AllowedImagesSettingsImageCriterionDeprecationTimeCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageNames")
    def image_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageProviders")
    def image_providers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceProductCodes")
    def marketplace_product_codes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AllowedImagesSettingsImageCriterionCreationDateCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, maximum_days_since_created: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumDaysSinceCreated")
    def maximum_days_since_created(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AllowedImagesSettingsImageCriterionDeprecationTimeCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, maximum_days_since_deprecated: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumDaysSinceDeprecated")
    def maximum_days_since_deprecated(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AmiCopyEbsBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.bool] = ..., device_name: Optional[_builtins.str] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., outpost_arn: Optional[_builtins.str] = ..., snapshot_id: Optional[_builtins.str] = ..., throughput: Optional[_builtins.int] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AmiCopyEphemeralBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: Optional[_builtins.str] = ..., virtual_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AmiEbsBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., outpost_arn: Optional[_builtins.str] = ..., snapshot_id: Optional[_builtins.str] = ..., throughput: Optional[_builtins.int] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AmiEphemeralBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, virtual_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AmiFromInstanceEbsBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.bool] = ..., device_name: Optional[_builtins.str] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., outpost_arn: Optional[_builtins.str] = ..., snapshot_id: Optional[_builtins.str] = ..., throughput: Optional[_builtins.int] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AmiFromInstanceEphemeralBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: Optional[_builtins.str] = ..., virtual_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CapacityBlockReservationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DefaultCreditSpecificationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DefaultNetworkAclEgress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: _builtins.str, from_port: _builtins.int, protocol: _builtins.str, rule_no: _builtins.int, to_port: _builtins.int, cidr_block: Optional[_builtins.str] = ..., icmp_code: Optional[_builtins.int] = ..., icmp_type: Optional[_builtins.int] = ..., ipv6_cidr_block: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNo")
    def rule_no(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DefaultNetworkAclIngress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: _builtins.str, from_port: _builtins.int, protocol: _builtins.str, rule_no: _builtins.int, to_port: _builtins.int, cidr_block: Optional[_builtins.str] = ..., icmp_code: Optional[_builtins.int] = ..., icmp_type: Optional[_builtins.int] = ..., ipv6_cidr_block: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNo")
    def rule_no(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DefaultRouteTableRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidr_block: Optional[_builtins.str] = ..., core_network_arn: Optional[_builtins.str] = ..., destination_prefix_list_id: Optional[_builtins.str] = ..., egress_only_gateway_id: Optional[_builtins.str] = ..., gateway_id: Optional[_builtins.str] = ..., instance_id: Optional[_builtins.str] = ..., ipv6_cidr_block: Optional[_builtins.str] = ..., nat_gateway_id: Optional[_builtins.str] = ..., network_interface_id: Optional[_builtins.str] = ..., transit_gateway_id: Optional[_builtins.str] = ..., vpc_endpoint_id: Optional[_builtins.str] = ..., vpc_peering_connection_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DefaultSecurityGroupEgress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, protocol: _builtins.str, to_port: _builtins.int, cidr_blocks: Optional[Sequence[_builtins.str]] = ..., description: Optional[_builtins.str] = ..., ipv6_cidr_blocks: Optional[Sequence[_builtins.str]] = ..., prefix_list_ids: Optional[Sequence[_builtins.str]] = ..., security_groups: Optional[Sequence[_builtins.str]] = ..., self: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DefaultSecurityGroupIngress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, protocol: _builtins.str, to_port: _builtins.int, cidr_blocks: Optional[Sequence[_builtins.str]] = ..., description: Optional[_builtins.str] = ..., ipv6_cidr_blocks: Optional[Sequence[_builtins.str]] = ..., prefix_list_ids: Optional[Sequence[_builtins.str]] = ..., security_groups: Optional[Sequence[_builtins.str]] = ..., self: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class EipDomainNameTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, egress_only_internet_gateway: outputs.EncryptionControlResourceExclusionsEgressOnlyInternetGateway, elastic_file_system: outputs.EncryptionControlResourceExclusionsElasticFileSystem, internet_gateway: outputs.EncryptionControlResourceExclusionsInternetGateway, lambda_: outputs.EncryptionControlResourceExclusionsLambda, nat_gateway: outputs.EncryptionControlResourceExclusionsNatGateway, virtual_private_gateway: outputs.EncryptionControlResourceExclusionsVirtualPrivateGateway, vpc_lattice: outputs.EncryptionControlResourceExclusionsVpcLattice, vpc_peering: outputs.EncryptionControlResourceExclusionsVpcPeering) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGateway")
    def egress_only_internet_gateway(self) -> outputs.EncryptionControlResourceExclusionsEgressOnlyInternetGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticFileSystem")
    def elastic_file_system(self) -> outputs.EncryptionControlResourceExclusionsElasticFileSystem:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateway")
    def internet_gateway(self) -> outputs.EncryptionControlResourceExclusionsInternetGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> outputs.EncryptionControlResourceExclusionsLambda:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> outputs.EncryptionControlResourceExclusionsNatGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualPrivateGateway")
    def virtual_private_gateway(self) -> outputs.EncryptionControlResourceExclusionsVirtualPrivateGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLattice")
    def vpc_lattice(self) -> outputs.EncryptionControlResourceExclusionsVpcLattice:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeering")
    def vpc_peering(self) -> outputs.EncryptionControlResourceExclusionsVpcPeering:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusionsEgressOnlyInternetGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusionsElasticFileSystem(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusionsInternetGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusionsLambda(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusionsNatGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusionsVirtualPrivateGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusionsVpcLattice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionControlResourceExclusionsVpcPeering(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionControlTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FleetFleetInstanceSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_ids: Optional[Sequence[_builtins.str]] = ..., instance_type: Optional[_builtins.str] = ..., lifecycle: Optional[_builtins.str] = ..., platform: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, launch_template_specification: Optional[outputs.FleetLaunchTemplateConfigLaunchTemplateSpecification] = ..., overrides: Optional[Sequence[outputs.FleetLaunchTemplateConfigOverride]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecification")
    def launch_template_specification(self) -> Optional[outputs.FleetLaunchTemplateConfigLaunchTemplateSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Optional[Sequence[outputs.FleetLaunchTemplateConfigOverride]]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigLaunchTemplateSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, version: _builtins.str, launch_template_id: Optional[_builtins.str] = ..., launch_template_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_zone: Optional[_builtins.str] = ..., instance_requirements: Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirements] = ..., instance_type: Optional[_builtins.str] = ..., max_price: Optional[_builtins.str] = ..., priority: Optional[_builtins.float] = ..., subnet_id: Optional[_builtins.str] = ..., weighted_capacity: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirements]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrice")
    def max_price(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirements(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, memory_mib: outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMib, vcpu_count: outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCount, accelerator_count: Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCount] = ..., accelerator_manufacturers: Optional[Sequence[_builtins.str]] = ..., accelerator_names: Optional[Sequence[_builtins.str]] = ..., accelerator_total_memory_mib: Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMib] = ..., accelerator_types: Optional[Sequence[_builtins.str]] = ..., allowed_instance_types: Optional[Sequence[_builtins.str]] = ..., bare_metal: Optional[_builtins.str] = ..., baseline_ebs_bandwidth_mbps: Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbps] = ..., burstable_performance: Optional[_builtins.str] = ..., cpu_manufacturers: Optional[Sequence[_builtins.str]] = ..., excluded_instance_types: Optional[Sequence[_builtins.str]] = ..., instance_generations: Optional[Sequence[_builtins.str]] = ..., local_storage: Optional[_builtins.str] = ..., local_storage_types: Optional[Sequence[_builtins.str]] = ..., max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[_builtins.int] = ..., memory_gib_per_vcpu: Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpu] = ..., network_bandwidth_gbps: Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbps] = ..., network_interface_count: Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCount] = ..., on_demand_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., require_hibernate_support: Optional[_builtins.bool] = ..., spot_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., total_local_storage_gb: Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGb] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(self) -> outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMib:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCount:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(self) -> Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMib]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSpotPriceAsPercentageOfOptimalOnDemandPrice")
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(self) -> Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpu]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGb")
    def total_local_storage_gb(self) -> Optional[outputs.FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGb]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMib(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbps(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpu(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMib(dict):
    def __init__(__self__, *, min: _builtins.int, max: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbps(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGb(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCount(dict):
    def __init__(__self__, *, min: _builtins.int, max: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FleetOnDemandOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocation_strategy: Optional[_builtins.str] = ..., capacity_reservation_options: Optional[outputs.FleetOnDemandOptionsCapacityReservationOptions] = ..., max_total_price: Optional[_builtins.str] = ..., min_target_capacity: Optional[_builtins.int] = ..., single_availability_zone: Optional[_builtins.bool] = ..., single_instance_type: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationOptions")
    def capacity_reservation_options(self) -> Optional[outputs.FleetOnDemandOptionsCapacityReservationOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTotalPrice")
    def max_total_price(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTargetCapacity")
    def min_target_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleAvailabilityZone")
    def single_availability_zone(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleInstanceType")
    def single_instance_type(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class FleetOnDemandOptionsCapacityReservationOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, usage_strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageStrategy")
    def usage_strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FleetSpotOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocation_strategy: Optional[_builtins.str] = ..., instance_interruption_behavior: Optional[_builtins.str] = ..., instance_pools_to_use_count: Optional[_builtins.int] = ..., maintenance_strategies: Optional[outputs.FleetSpotOptionsMaintenanceStrategies] = ..., max_total_price: Optional[_builtins.str] = ..., min_target_capacity: Optional[_builtins.int] = ..., single_availability_zone: Optional[_builtins.bool] = ..., single_instance_type: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceStrategies")
    def maintenance_strategies(self) -> Optional[outputs.FleetSpotOptionsMaintenanceStrategies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTotalPrice")
    def max_total_price(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTargetCapacity")
    def min_target_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleAvailabilityZone")
    def single_availability_zone(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleInstanceType")
    def single_instance_type(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class FleetSpotOptionsMaintenanceStrategies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_rebalance: Optional[outputs.FleetSpotOptionsMaintenanceStrategiesCapacityRebalance] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityRebalance")
    def capacity_rebalance(self) -> Optional[outputs.FleetSpotOptionsMaintenanceStrategiesCapacityRebalance]:
        
        ...
    


@pulumi.output_type
class FleetSpotOptionsMaintenanceStrategiesCapacityRebalance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replacement_strategy: Optional[_builtins.str] = ..., termination_delay: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementStrategy")
    def replacement_strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationDelay")
    def termination_delay(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class FleetTargetCapacitySpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_target_capacity_type: _builtins.str, total_target_capacity: _builtins.int, on_demand_target_capacity: Optional[_builtins.int] = ..., spot_target_capacity: Optional[_builtins.int] = ..., target_capacity_unit_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTargetCapacityType")
    def default_target_capacity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalTargetCapacity")
    def total_target_capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandTargetCapacity")
    def on_demand_target_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotTargetCapacity")
    def spot_target_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCapacityUnitType")
    def target_capacity_unit_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlowLogDestinationOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_format: Optional[_builtins.str] = ..., hive_compatible_partitions: Optional[_builtins.bool] = ..., per_hour_partition: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveCompatiblePartitions")
    def hive_compatible_partitions(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perHourPartition")
    def per_hour_partition(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InstanceCapacityReservationSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_preference: Optional[_builtins.str] = ..., capacity_reservation_target: Optional[outputs.InstanceCapacityReservationSpecificationCapacityReservationTarget] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationTarget")
    def capacity_reservation_target(self) -> Optional[outputs.InstanceCapacityReservationSpecificationCapacityReservationTarget]:
        
        ...
    


@pulumi.output_type
class InstanceCapacityReservationSpecificationCapacityReservationTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_id: Optional[_builtins.str] = ..., capacity_reservation_resource_group_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationId")
    def capacity_reservation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceCpuOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amd_sev_snp: Optional[_builtins.str] = ..., core_count: Optional[_builtins.int] = ..., nested_virtualization: Optional[_builtins.str] = ..., threads_per_core: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amdSevSnp")
    def amd_sev_snp(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestedVirtualization")
    def nested_virtualization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceCreditSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_credits: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceEbsBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., snapshot_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., tags_all: Optional[Mapping[str, _builtins.str]] = ..., throughput: Optional[_builtins.int] = ..., volume_id: Optional[_builtins.str] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceEnclaveOptions(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InstanceEphemeralBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, no_device: Optional[_builtins.bool] = ..., virtual_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceInstanceMarketOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, market_type: Optional[_builtins.str] = ..., spot_options: Optional[outputs.InstanceInstanceMarketOptionsSpotOptions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketType")
    def market_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[outputs.InstanceInstanceMarketOptionsSpotOptions]:
        
        ...
    


@pulumi.output_type
class InstanceInstanceMarketOptionsSpotOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_interruption_behavior: Optional[_builtins.str] = ..., max_price: Optional[_builtins.str] = ..., spot_instance_type: Optional[_builtins.str] = ..., valid_until: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrice")
    def max_price(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstanceType")
    def spot_instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceLaunchTemplate(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceMaintenanceOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_recovery: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRecovery")
    def auto_recovery(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceMetadataOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_endpoint: Optional[_builtins.str] = ..., http_protocol_ipv6: Optional[_builtins.str] = ..., http_put_response_hop_limit: Optional[_builtins.int] = ..., http_tokens: Optional[_builtins.str] = ..., instance_metadata_tags: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_index: _builtins.int, network_interface_id: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., network_card_index: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstancePrimaryNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_interface_id: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InstancePrivateDnsNameOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_resource_name_dns_a_record: Optional[_builtins.bool] = ..., enable_resource_name_dns_aaaa_record: Optional[_builtins.bool] = ..., hostname_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameType")
    def hostname_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceRootBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.bool] = ..., device_name: Optional[_builtins.str] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., tags_all: Optional[Mapping[str, _builtins.str]] = ..., throughput: Optional[_builtins.int] = ..., volume_id: Optional[_builtins.str] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceSecondaryNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_card_index: _builtins.int, secondary_subnet_id: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., device_index: Optional[_builtins.int] = ..., interface_type: Optional[_builtins.str] = ..., mac_address: Optional[_builtins.str] = ..., private_ip_address_count: Optional[_builtins.int] = ..., private_ip_addresses: Optional[Sequence[_builtins.str]] = ..., secondary_interface_id: Optional[_builtins.str] = ..., secondary_network_id: Optional[_builtins.str] = ..., source_dest_check: Optional[_builtins.bool] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondarySubnetId")
    def secondary_subnet_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddressCount")
    def private_ip_address_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInterfaceId")
    def secondary_interface_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkId")
    def secondary_network_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class LaunchConfigurationEbsBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., no_device: Optional[_builtins.bool] = ..., snapshot_id: Optional[_builtins.str] = ..., throughput: Optional[_builtins.int] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class LaunchConfigurationEphemeralBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, no_device: Optional[_builtins.bool] = ..., virtual_name: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class LaunchConfigurationMetadataOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_endpoint: Optional[_builtins.str] = ..., http_put_response_hop_limit: Optional[_builtins.int] = ..., http_tokens: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchConfigurationRootBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.bool] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., throughput: Optional[_builtins.int] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class LaunchTemplateBlockDeviceMapping(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: Optional[_builtins.str] = ..., ebs: Optional[outputs.LaunchTemplateBlockDeviceMappingEbs] = ..., no_device: Optional[_builtins.str] = ..., virtual_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ebs(self) -> Optional[outputs.LaunchTemplateBlockDeviceMappingEbs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateBlockDeviceMappingEbs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.str] = ..., encrypted: Optional[_builtins.str] = ..., iops: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., snapshot_id: Optional[_builtins.str] = ..., throughput: Optional[_builtins.int] = ..., volume_initialization_rate: Optional[_builtins.int] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeInitializationRate")
    def volume_initialization_rate(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateCapacityReservationSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_preference: Optional[_builtins.str] = ..., capacity_reservation_target: Optional[outputs.LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationTarget")
    def capacity_reservation_target(self) -> Optional[outputs.LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_id: Optional[_builtins.str] = ..., capacity_reservation_resource_group_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationId")
    def capacity_reservation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateCpuOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amd_sev_snp: Optional[_builtins.str] = ..., core_count: Optional[_builtins.int] = ..., nested_virtualization: Optional[_builtins.str] = ..., threads_per_core: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amdSevSnp")
    def amd_sev_snp(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestedVirtualization")
    def nested_virtualization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateCreditSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_credits: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateEnclaveOptions(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateHibernationOptions(dict):
    def __init__(__self__, *, configured: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configured(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class LaunchTemplateIamInstanceProfile(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceMarketOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, market_type: Optional[_builtins.str] = ..., spot_options: Optional[outputs.LaunchTemplateInstanceMarketOptionsSpotOptions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketType")
    def market_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[outputs.LaunchTemplateInstanceMarketOptionsSpotOptions]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceMarketOptionsSpotOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, block_duration_minutes: Optional[_builtins.int] = ..., instance_interruption_behavior: Optional[_builtins.str] = ..., max_price: Optional[_builtins.str] = ..., spot_instance_type: Optional[_builtins.str] = ..., valid_until: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrice")
    def max_price(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstanceType")
    def spot_instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirements(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, memory_mib: outputs.LaunchTemplateInstanceRequirementsMemoryMib, vcpu_count: outputs.LaunchTemplateInstanceRequirementsVcpuCount, accelerator_count: Optional[outputs.LaunchTemplateInstanceRequirementsAcceleratorCount] = ..., accelerator_manufacturers: Optional[Sequence[_builtins.str]] = ..., accelerator_names: Optional[Sequence[_builtins.str]] = ..., accelerator_total_memory_mib: Optional[outputs.LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib] = ..., accelerator_types: Optional[Sequence[_builtins.str]] = ..., allowed_instance_types: Optional[Sequence[_builtins.str]] = ..., bare_metal: Optional[_builtins.str] = ..., baseline_ebs_bandwidth_mbps: Optional[outputs.LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps] = ..., burstable_performance: Optional[_builtins.str] = ..., cpu_manufacturers: Optional[Sequence[_builtins.str]] = ..., excluded_instance_types: Optional[Sequence[_builtins.str]] = ..., instance_generations: Optional[Sequence[_builtins.str]] = ..., local_storage: Optional[_builtins.str] = ..., local_storage_types: Optional[Sequence[_builtins.str]] = ..., max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[_builtins.int] = ..., memory_gib_per_vcpu: Optional[outputs.LaunchTemplateInstanceRequirementsMemoryGibPerVcpu] = ..., network_bandwidth_gbps: Optional[outputs.LaunchTemplateInstanceRequirementsNetworkBandwidthGbps] = ..., network_interface_count: Optional[outputs.LaunchTemplateInstanceRequirementsNetworkInterfaceCount] = ..., on_demand_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., require_hibernate_support: Optional[_builtins.bool] = ..., spot_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., total_local_storage_gb: Optional[outputs.LaunchTemplateInstanceRequirementsTotalLocalStorageGb] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(self) -> outputs.LaunchTemplateInstanceRequirementsMemoryMib:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> outputs.LaunchTemplateInstanceRequirementsVcpuCount:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[outputs.LaunchTemplateInstanceRequirementsAcceleratorCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(self) -> Optional[outputs.LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Optional[outputs.LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSpotPriceAsPercentageOfOptimalOnDemandPrice")
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(self) -> Optional[outputs.LaunchTemplateInstanceRequirementsMemoryGibPerVcpu]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Optional[outputs.LaunchTemplateInstanceRequirementsNetworkBandwidthGbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[outputs.LaunchTemplateInstanceRequirementsNetworkInterfaceCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGb")
    def total_local_storage_gb(self) -> Optional[outputs.LaunchTemplateInstanceRequirementsTotalLocalStorageGb]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsAcceleratorCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsMemoryGibPerVcpu(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsMemoryMib(dict):
    def __init__(__self__, *, min: _builtins.int, max: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsNetworkBandwidthGbps(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsNetworkInterfaceCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsTotalLocalStorageGb(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateInstanceRequirementsVcpuCount(dict):
    def __init__(__self__, *, min: _builtins.int, max: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateLicenseSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, license_configuration_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseConfigurationArn")
    def license_configuration_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LaunchTemplateMaintenanceOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_recovery: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRecovery")
    def auto_recovery(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateMetadataOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_endpoint: Optional[_builtins.str] = ..., http_protocol_ipv6: Optional[_builtins.str] = ..., http_put_response_hop_limit: Optional[_builtins.int] = ..., http_tokens: Optional[_builtins.str] = ..., instance_metadata_tags: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateMonitoring(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, associate_carrier_ip_address: Optional[_builtins.str] = ..., associate_public_ip_address: Optional[_builtins.str] = ..., connection_tracking_specification: Optional[outputs.LaunchTemplateNetworkInterfaceConnectionTrackingSpecification] = ..., delete_on_termination: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., device_index: Optional[_builtins.int] = ..., ena_srd_specification: Optional[outputs.LaunchTemplateNetworkInterfaceEnaSrdSpecification] = ..., interface_type: Optional[_builtins.str] = ..., ipv4_address_count: Optional[_builtins.int] = ..., ipv4_addresses: Optional[Sequence[_builtins.str]] = ..., ipv4_prefix_count: Optional[_builtins.int] = ..., ipv4_prefixes: Optional[Sequence[_builtins.str]] = ..., ipv6_address_count: Optional[_builtins.int] = ..., ipv6_addresses: Optional[Sequence[_builtins.str]] = ..., ipv6_prefix_count: Optional[_builtins.int] = ..., ipv6_prefixes: Optional[Sequence[_builtins.str]] = ..., network_card_index: Optional[_builtins.int] = ..., network_interface_id: Optional[_builtins.str] = ..., primary_ipv6: Optional[_builtins.str] = ..., private_ip_address: Optional[_builtins.str] = ..., security_groups: Optional[Sequence[_builtins.str]] = ..., subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateCarrierIpAddress")
    def associate_carrier_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTrackingSpecification")
    def connection_tracking_specification(self) -> Optional[outputs.LaunchTemplateNetworkInterfaceConnectionTrackingSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enaSrdSpecification")
    def ena_srd_specification(self) -> Optional[outputs.LaunchTemplateNetworkInterfaceEnaSrdSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4AddressCount")
    def ipv4_address_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4PrefixCount")
    def ipv4_prefix_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Prefixes")
    def ipv4_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6PrefixCount")
    def ipv6_prefix_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Prefixes")
    def ipv6_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv6")
    def primary_ipv6(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateNetworkInterfaceConnectionTrackingSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tcp_established_timeout: Optional[_builtins.int] = ..., udp_stream_timeout: Optional[_builtins.int] = ..., udp_timeout: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpEstablishedTimeout")
    def tcp_established_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpStreamTimeout")
    def udp_stream_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpTimeout")
    def udp_timeout(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateNetworkInterfaceEnaSrdSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ena_srd_enabled: Optional[_builtins.bool] = ..., ena_srd_udp_specification: Optional[outputs.LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enaSrdEnabled")
    def ena_srd_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enaSrdUdpSpecification")
    def ena_srd_udp_specification(self) -> Optional[outputs.LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecification]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ena_srd_udp_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enaSrdUdpEnabled")
    def ena_srd_udp_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateNetworkPerformanceOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bandwidth_weighting: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthWeighting")
    def bandwidth_weighting(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplatePlacement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, affinity: Optional[_builtins.str] = ..., availability_zone: Optional[_builtins.str] = ..., group_id: Optional[_builtins.str] = ..., group_name: Optional[_builtins.str] = ..., host_id: Optional[_builtins.str] = ..., host_resource_group_arn: Optional[_builtins.str] = ..., partition_number: Optional[_builtins.int] = ..., spread_domain: Optional[_builtins.str] = ..., tenancy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def affinity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionNumber")
    def partition_number(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spreadDomain")
    def spread_domain(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplatePrivateDnsNameOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_resource_name_dns_a_record: Optional[_builtins.bool] = ..., enable_resource_name_dns_aaaa_record: Optional[_builtins.bool] = ..., hostname_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameType")
    def hostname_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateSecondaryInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.bool] = ..., device_index: Optional[_builtins.int] = ..., interface_type: Optional[_builtins.str] = ..., network_card_index: Optional[_builtins.int] = ..., private_ip_address_count: Optional[_builtins.int] = ..., private_ip_addresses: Optional[Sequence[_builtins.str]] = ..., secondary_subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddressCount")
    def private_ip_address_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondarySubnetId")
    def secondary_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LaunchTemplateTagSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ManagedPrefixListEntry(dict):
    def __init__(__self__, *, cidr: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NatGatewayAvailabilityZoneAddress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocation_ids: Optional[Sequence[_builtins.str]] = ..., availability_zone: Optional[_builtins.str] = ..., availability_zone_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationIds")
    def allocation_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NatGatewayEipAssociationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NatGatewayRegionalNatGatewayAddress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocation_id: Optional[_builtins.str] = ..., association_id: Optional[_builtins.str] = ..., availability_zone: Optional[_builtins.str] = ..., availability_zone_id: Optional[_builtins.str] = ..., network_interface_id: Optional[_builtins.str] = ..., public_ip: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkAclEgress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: _builtins.str, from_port: _builtins.int, protocol: _builtins.str, rule_no: _builtins.int, to_port: _builtins.int, cidr_block: Optional[_builtins.str] = ..., icmp_code: Optional[_builtins.int] = ..., icmp_type: Optional[_builtins.int] = ..., ipv6_cidr_block: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNo")
    def rule_no(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkAclIngress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: _builtins.str, from_port: _builtins.int, protocol: _builtins.str, rule_no: _builtins.int, to_port: _builtins.int, cidr_block: Optional[_builtins.str] = ..., icmp_code: Optional[_builtins.int] = ..., icmp_type: Optional[_builtins.int] = ..., ipv6_cidr_block: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNo")
    def rule_no(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisAlternatePathHint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_arn: Optional[_builtins.str] = ..., component_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, acl_rules: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationAclRule]] = ..., acls: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationAcl]] = ..., address: Optional[_builtins.str] = ..., addresses: Optional[Sequence[_builtins.str]] = ..., attached_tos: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationAttachedTo]] = ..., availability_zones: Optional[Sequence[_builtins.str]] = ..., cidrs: Optional[Sequence[_builtins.str]] = ..., classic_load_balancer_listeners: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationClassicLoadBalancerListener]] = ..., components: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationComponent]] = ..., customer_gateways: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationCustomerGateway]] = ..., destination_vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationDestinationVpc]] = ..., destinations: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationDestination]] = ..., direction: Optional[_builtins.str] = ..., elastic_load_balancer_listeners: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationElasticLoadBalancerListener]] = ..., explanation_code: Optional[_builtins.str] = ..., ingress_route_tables: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationIngressRouteTable]] = ..., internet_gateways: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationInternetGateway]] = ..., load_balancer_arn: Optional[_builtins.str] = ..., load_balancer_listener_port: Optional[_builtins.int] = ..., load_balancer_target_group: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationLoadBalancerTargetGroup]] = ..., load_balancer_target_groups: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationLoadBalancerTargetGroup]] = ..., load_balancer_target_port: Optional[_builtins.int] = ..., missing_component: Optional[_builtins.str] = ..., nat_gateways: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationNatGateway]] = ..., network_interfaces: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationNetworkInterface]] = ..., packet_field: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationPortRange]] = ..., prefix_lists: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationPrefixList]] = ..., protocols: Optional[Sequence[_builtins.str]] = ..., route_table_routes: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationRouteTableRoute]] = ..., route_tables: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationRouteTable]] = ..., security_group: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSecurityGroup]] = ..., security_group_rules: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSecurityGroupRule]] = ..., security_groups: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSecurityGroup]] = ..., source_vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSourceVpc]] = ..., state: Optional[_builtins.str] = ..., subnet_route_tables: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSubnetRouteTable]] = ..., subnets: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSubnet]] = ..., transit_gateway_attachments: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationTransitGatewayAttachment]] = ..., transit_gateway_route_table_routes: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRoute]] = ..., transit_gateway_route_tables: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationTransitGatewayRouteTable]] = ..., transit_gateways: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationTransitGateway]] = ..., vpc_endpoints: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpcEndpoint]] = ..., vpc_peering_connections: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpcPeeringConnection]] = ..., vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpc]] = ..., vpn_connections: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpnConnection]] = ..., vpn_gateways: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpnGateway]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationAclRule]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def acls(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationAcl]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationAttachedTo]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classicLoadBalancerListeners")
    def classic_load_balancer_listeners(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationClassicLoadBalancerListener]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationComponent]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerGateways")
    def customer_gateways(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationCustomerGateway]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationDestinationVpc]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationDestination]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticLoadBalancerListeners")
    def elastic_load_balancer_listeners(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationElasticLoadBalancerListener]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="explanationCode")
    def explanation_code(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressRouteTables")
    def ingress_route_tables(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationIngressRouteTable]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateways")
    def internet_gateways(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationInternetGateway]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerListenerPort")
    def load_balancer_listener_port(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetGroup")
    def load_balancer_target_group(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationLoadBalancerTargetGroup]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetGroups")
    def load_balancer_target_groups(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationLoadBalancerTargetGroup]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetPort")
    def load_balancer_target_port(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="missingComponent")
    def missing_component(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateways")
    def nat_gateways(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationNatGateway]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationNetworkInterface]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packetField")
    def packet_field(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationPortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationPrefixList]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationRouteTableRoute]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTables")
    def route_tables(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationRouteTable]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSecurityGroup]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSecurityGroupRule]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSecurityGroup]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSourceVpc]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetRouteTables")
    def subnet_route_tables(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSubnetRouteTable]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSubnet]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachments")
    def transit_gateway_attachments(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationTransitGatewayAttachment]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRoute]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTables")
    def transit_gateway_route_tables(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationTransitGatewayRouteTable]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationTransitGateway]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpcEndpoint]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnections")
    def vpc_peering_connections(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpcPeeringConnection]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpc]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnConnections")
    def vpn_connections(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpnConnection]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnGateways")
    def vpn_gateways(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationVpnGateway]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationAcl(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationAclRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidr: Optional[_builtins.str] = ..., egress: Optional[_builtins.bool] = ..., port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationAclRulePortRange]] = ..., protocol: Optional[_builtins.str] = ..., rule_action: Optional[_builtins.str] = ..., rule_number: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationAclRulePortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationAclRulePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationAttachedTo(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationClassicLoadBalancerListener(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_port: Optional[_builtins.int] = ..., load_balancer_port: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerPort")
    def load_balancer_port(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationComponent(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationCustomerGateway(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationDestination(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationDestinationVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationElasticLoadBalancerListener(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationIngressRouteTable(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationInternetGateway(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationLoadBalancerTargetGroup(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationNatGateway(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationNetworkInterface(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationPrefixList(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationRouteTable(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationRouteTableRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_cidr: Optional[_builtins.str] = ..., destination_prefix_list_id: Optional[_builtins.str] = ..., egress_only_internet_gateway_id: Optional[_builtins.str] = ..., gateway_id: Optional[_builtins.str] = ..., instance_id: Optional[_builtins.str] = ..., nat_gateway_id: Optional[_builtins.str] = ..., network_interface_id: Optional[_builtins.str] = ..., origin: Optional[_builtins.str] = ..., transit_gateway_id: Optional[_builtins.str] = ..., vpc_peering_connection_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationSecurityGroup(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationSecurityGroupRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidr: Optional[_builtins.str] = ..., direction: Optional[_builtins.str] = ..., port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSecurityGroupRulePortRange]] = ..., prefix_list_id: Optional[_builtins.str] = ..., protocol: Optional[_builtins.str] = ..., security_group_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisExplanationSecurityGroupRulePortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationSecurityGroupRulePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationSourceVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationSubnet(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationSubnetRouteTable(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationTransitGateway(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationTransitGatewayAttachment(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationTransitGatewayRouteTable(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attachment_id: Optional[_builtins.str] = ..., destination_cidr: Optional[_builtins.str] = ..., prefix_list_id: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ..., route_origin: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationVpcEndpoint(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationVpcPeeringConnection(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationVpnConnection(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisExplanationVpnGateway(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponent(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, acl_rules: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAclRule]] = ..., additional_details: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAdditionalDetail]] = ..., attached_tos: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAttachedTo]] = ..., components: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentComponent]] = ..., destination_vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentDestinationVpc]] = ..., inbound_headers: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentInboundHeader]] = ..., outbound_headers: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentOutboundHeader]] = ..., route_table_routes: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentRouteTableRoute]] = ..., security_group_rules: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentSecurityGroupRule]] = ..., sequence_number: Optional[_builtins.int] = ..., source_vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentSourceVpc]] = ..., subnets: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentSubnet]] = ..., transit_gateway_route_table_routes: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRoute]] = ..., transit_gateways: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentTransitGateway]] = ..., vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentVpc]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAclRule]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAdditionalDetail]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAttachedTo]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentComponent]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentDestinationVpc]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundHeaders")
    def inbound_headers(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentInboundHeader]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundHeaders")
    def outbound_headers(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentOutboundHeader]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentRouteTableRoute]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentSecurityGroupRule]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentSourceVpc]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentSubnet]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRoute]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentTransitGateway]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentVpc]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentAclRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidr: Optional[_builtins.str] = ..., egress: Optional[_builtins.bool] = ..., port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAclRulePortRange]] = ..., protocol: Optional[_builtins.str] = ..., rule_action: Optional[_builtins.str] = ..., rule_number: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAclRulePortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentAclRulePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentAdditionalDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_detail_type: Optional[_builtins.str] = ..., components: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponent]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetailType")
    def additional_detail_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponent]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponent(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentAttachedTo(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentComponent(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentDestinationVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentInboundHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_addresses: Optional[Sequence[_builtins.str]] = ..., destination_port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRange]] = ..., protocol: Optional[_builtins.str] = ..., source_addresses: Optional[Sequence[_builtins.str]] = ..., source_port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRange]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRange]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentOutboundHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_addresses: Optional[Sequence[_builtins.str]] = ..., destination_port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRange]] = ..., protocol: Optional[_builtins.str] = ..., source_addresses: Optional[Sequence[_builtins.str]] = ..., source_port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRange]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRange]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentRouteTableRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_cidr: Optional[_builtins.str] = ..., destination_prefix_list_id: Optional[_builtins.str] = ..., egress_only_internet_gateway_id: Optional[_builtins.str] = ..., gateway_id: Optional[_builtins.str] = ..., instance_id: Optional[_builtins.str] = ..., nat_gateway_id: Optional[_builtins.str] = ..., network_interface_id: Optional[_builtins.str] = ..., origin: Optional[_builtins.str] = ..., transit_gateway_id: Optional[_builtins.str] = ..., vpc_peering_connection_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentSecurityGroupRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidr: Optional[_builtins.str] = ..., direction: Optional[_builtins.str] = ..., port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRange]] = ..., prefix_list_id: Optional[_builtins.str] = ..., protocol: Optional[_builtins.str] = ..., security_group_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentSourceVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentSubnet(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentTransitGateway(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attachment_id: Optional[_builtins.str] = ..., destination_cidr: Optional[_builtins.str] = ..., prefix_list_id: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ..., route_origin: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisForwardPathComponentVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponent(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, acl_rules: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAclRule]] = ..., additional_details: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAdditionalDetail]] = ..., attached_tos: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAttachedTo]] = ..., components: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentComponent]] = ..., destination_vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentDestinationVpc]] = ..., inbound_headers: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentInboundHeader]] = ..., outbound_headers: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentOutboundHeader]] = ..., route_table_routes: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentRouteTableRoute]] = ..., security_group_rules: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentSecurityGroupRule]] = ..., sequence_number: Optional[_builtins.int] = ..., source_vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentSourceVpc]] = ..., subnets: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentSubnet]] = ..., transit_gateway_route_table_routes: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRoute]] = ..., transit_gateways: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentTransitGateway]] = ..., vpcs: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentVpc]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAclRule]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAdditionalDetail]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAttachedTo]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentComponent]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentDestinationVpc]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundHeaders")
    def inbound_headers(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentInboundHeader]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundHeaders")
    def outbound_headers(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentOutboundHeader]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentRouteTableRoute]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentSecurityGroupRule]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentSourceVpc]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentSubnet]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRoute]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentTransitGateway]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentVpc]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentAclRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidr: Optional[_builtins.str] = ..., egress: Optional[_builtins.bool] = ..., port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAclRulePortRange]] = ..., protocol: Optional[_builtins.str] = ..., rule_action: Optional[_builtins.str] = ..., rule_number: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAclRulePortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentAclRulePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentAdditionalDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_detail_type: Optional[_builtins.str] = ..., components: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponent]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetailType")
    def additional_detail_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponent]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponent(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentAttachedTo(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentComponent(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentDestinationVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentInboundHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_addresses: Optional[Sequence[_builtins.str]] = ..., destination_port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRange]] = ..., protocol: Optional[_builtins.str] = ..., source_addresses: Optional[Sequence[_builtins.str]] = ..., source_port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRange]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRange]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentOutboundHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_addresses: Optional[Sequence[_builtins.str]] = ..., destination_port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRange]] = ..., protocol: Optional[_builtins.str] = ..., source_addresses: Optional[Sequence[_builtins.str]] = ..., source_port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRange]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRange]]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentRouteTableRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_cidr: Optional[_builtins.str] = ..., destination_prefix_list_id: Optional[_builtins.str] = ..., egress_only_internet_gateway_id: Optional[_builtins.str] = ..., gateway_id: Optional[_builtins.str] = ..., instance_id: Optional[_builtins.str] = ..., nat_gateway_id: Optional[_builtins.str] = ..., network_interface_id: Optional[_builtins.str] = ..., origin: Optional[_builtins.str] = ..., transit_gateway_id: Optional[_builtins.str] = ..., vpc_peering_connection_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentSecurityGroupRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidr: Optional[_builtins.str] = ..., direction: Optional[_builtins.str] = ..., port_ranges: Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRange]] = ..., prefix_list_id: Optional[_builtins.str] = ..., protocol: Optional[_builtins.str] = ..., security_group_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRange]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentSourceVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentSubnet(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentTransitGateway(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attachment_id: Optional[_builtins.str] = ..., destination_cidr: Optional[_builtins.str] = ..., prefix_list_id: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ..., route_origin: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsAnalysisReturnPathComponentVpc(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkInsightsPathFilterAtDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_address: Optional[_builtins.str] = ..., destination_port_range: Optional[outputs.NetworkInsightsPathFilterAtDestinationDestinationPortRange] = ..., source_address: Optional[_builtins.str] = ..., source_port_range: Optional[outputs.NetworkInsightsPathFilterAtDestinationSourcePortRange] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[outputs.NetworkInsightsPathFilterAtDestinationDestinationPortRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddress")
    def source_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[outputs.NetworkInsightsPathFilterAtDestinationSourcePortRange]:
        
        ...
    


@pulumi.output_type
class NetworkInsightsPathFilterAtDestinationDestinationPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: Optional[_builtins.int] = ..., to_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class NetworkInsightsPathFilterAtDestinationSourcePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: Optional[_builtins.int] = ..., to_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class NetworkInsightsPathFilterAtSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_address: Optional[_builtins.str] = ..., destination_port_range: Optional[outputs.NetworkInsightsPathFilterAtSourceDestinationPortRange] = ..., source_address: Optional[_builtins.str] = ..., source_port_range: Optional[outputs.NetworkInsightsPathFilterAtSourceSourcePortRange] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[outputs.NetworkInsightsPathFilterAtSourceDestinationPortRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddress")
    def source_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[outputs.NetworkInsightsPathFilterAtSourceSourcePortRange]:
        
        ...
    


@pulumi.output_type
class NetworkInsightsPathFilterAtSourceDestinationPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: Optional[_builtins.int] = ..., to_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class NetworkInsightsPathFilterAtSourceSourcePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: Optional[_builtins.int] = ..., to_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class NetworkInterfaceAttachment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_index: _builtins.int, instance: _builtins.str, attachment_id: Optional[_builtins.str] = ..., network_card_index: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class NetworkInterfacePermissionTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PeeringConnectionOptionsAccepter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PeeringConnectionOptionsRequester(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RouteTableRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, carrier_gateway_id: Optional[_builtins.str] = ..., cidr_block: Optional[_builtins.str] = ..., core_network_arn: Optional[_builtins.str] = ..., destination_prefix_list_id: Optional[_builtins.str] = ..., egress_only_gateway_id: Optional[_builtins.str] = ..., gateway_id: Optional[_builtins.str] = ..., ipv6_cidr_block: Optional[_builtins.str] = ..., local_gateway_id: Optional[_builtins.str] = ..., nat_gateway_id: Optional[_builtins.str] = ..., network_interface_id: Optional[_builtins.str] = ..., transit_gateway_id: Optional[_builtins.str] = ..., vpc_endpoint_id: Optional[_builtins.str] = ..., vpc_peering_connection_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierGatewayId")
    def carrier_gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecondaryNetworkIpv4CidrBlockAssociation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, association_id: _builtins.str, cidr_block: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecondaryNetworkTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecondarySubnetIpv4CidrBlockAssociation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, association_id: _builtins.str, cidr_block: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecondarySubnetTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGroupEgress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, protocol: _builtins.str, to_port: _builtins.int, cidr_blocks: Optional[Sequence[_builtins.str]] = ..., description: Optional[_builtins.str] = ..., ipv6_cidr_blocks: Optional[Sequence[_builtins.str]] = ..., prefix_list_ids: Optional[Sequence[_builtins.str]] = ..., security_groups: Optional[Sequence[_builtins.str]] = ..., self: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SecurityGroupIngress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, protocol: _builtins.str, to_port: _builtins.int, cidr_blocks: Optional[Sequence[_builtins.str]] = ..., description: Optional[_builtins.str] = ..., ipv6_cidr_blocks: Optional[Sequence[_builtins.str]] = ..., prefix_list_ids: Optional[Sequence[_builtins.str]] = ..., security_groups: Optional[Sequence[_builtins.str]] = ..., self: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ami: _builtins.str, instance_type: _builtins.str, associate_public_ip_address: Optional[_builtins.bool] = ..., availability_zone: Optional[_builtins.str] = ..., ebs_block_devices: Optional[Sequence[outputs.SpotFleetRequestLaunchSpecificationEbsBlockDevice]] = ..., ebs_optimized: Optional[_builtins.bool] = ..., ephemeral_block_devices: Optional[Sequence[outputs.SpotFleetRequestLaunchSpecificationEphemeralBlockDevice]] = ..., iam_instance_profile: Optional[_builtins.str] = ..., iam_instance_profile_arn: Optional[_builtins.str] = ..., key_name: Optional[_builtins.str] = ..., monitoring: Optional[_builtins.bool] = ..., placement_group: Optional[_builtins.str] = ..., placement_tenancy: Optional[_builtins.str] = ..., root_block_devices: Optional[Sequence[outputs.SpotFleetRequestLaunchSpecificationRootBlockDevice]] = ..., spot_price: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., user_data: Optional[_builtins.str] = ..., vpc_security_group_ids: Optional[Sequence[_builtins.str]] = ..., weighted_capacity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ami(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> Optional[Sequence[outputs.SpotFleetRequestLaunchSpecificationEbsBlockDevice]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> Optional[Sequence[outputs.SpotFleetRequestLaunchSpecificationEphemeralBlockDevice]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfileArn")
    def iam_instance_profile_arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementTenancy")
    def placement_tenancy(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootBlockDevices")
    def root_block_devices(self) -> Optional[Sequence[outputs.SpotFleetRequestLaunchSpecificationRootBlockDevice]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchSpecificationEbsBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., snapshot_id: Optional[_builtins.str] = ..., throughput: Optional[_builtins.int] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchSpecificationEphemeralBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, virtual_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchSpecificationRootBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.bool] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., throughput: Optional[_builtins.int] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, launch_template_specification: outputs.SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecification, overrides: Optional[Sequence[outputs.SpotFleetRequestLaunchTemplateConfigOverride]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecification")
    def launch_template_specification(self) -> outputs.SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecification:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Optional[Sequence[outputs.SpotFleetRequestLaunchTemplateConfigOverride]]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecification(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_zone: Optional[_builtins.str] = ..., instance_requirements: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirements] = ..., instance_type: Optional[_builtins.str] = ..., priority: Optional[_builtins.float] = ..., spot_price: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ..., weighted_capacity: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirements]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirements(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCount] = ..., accelerator_manufacturers: Optional[Sequence[_builtins.str]] = ..., accelerator_names: Optional[Sequence[_builtins.str]] = ..., accelerator_total_memory_mib: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMib] = ..., accelerator_types: Optional[Sequence[_builtins.str]] = ..., allowed_instance_types: Optional[Sequence[_builtins.str]] = ..., bare_metal: Optional[_builtins.str] = ..., baseline_ebs_bandwidth_mbps: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbps] = ..., burstable_performance: Optional[_builtins.str] = ..., cpu_manufacturers: Optional[Sequence[_builtins.str]] = ..., excluded_instance_types: Optional[Sequence[_builtins.str]] = ..., instance_generations: Optional[Sequence[_builtins.str]] = ..., local_storage: Optional[_builtins.str] = ..., local_storage_types: Optional[Sequence[_builtins.str]] = ..., memory_gib_per_vcpu: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpu] = ..., memory_mib: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMib] = ..., network_bandwidth_gbps: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbps] = ..., network_interface_count: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCount] = ..., on_demand_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., require_hibernate_support: Optional[_builtins.bool] = ..., spot_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., total_local_storage_gb: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGb] = ..., vcpu_count: Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCount] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMib]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpu]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMib]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGb")
    def total_local_storage_gb(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGb]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> Optional[outputs.SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCount]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMib(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbps(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpu(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMib(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbps(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGb(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestSpotMaintenanceStrategies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_rebalance: Optional[outputs.SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalance] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityRebalance")
    def capacity_rebalance(self) -> Optional[outputs.SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalance]:
        
        ...
    


@pulumi.output_type
class SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replacement_strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementStrategy")
    def replacement_strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestCapacityReservationSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_preference: Optional[_builtins.str] = ..., capacity_reservation_target: Optional[outputs.SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationTarget")
    def capacity_reservation_target(self) -> Optional[outputs.SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_id: Optional[_builtins.str] = ..., capacity_reservation_resource_group_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationId")
    def capacity_reservation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestCpuOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amd_sev_snp: Optional[_builtins.str] = ..., core_count: Optional[_builtins.int] = ..., nested_virtualization: Optional[_builtins.str] = ..., threads_per_core: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amdSevSnp")
    def amd_sev_snp(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestedVirtualization")
    def nested_virtualization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestCreditSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_credits: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestEbsBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., snapshot_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., tags_all: Optional[Mapping[str, _builtins.str]] = ..., throughput: Optional[_builtins.int] = ..., volume_id: Optional[_builtins.str] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestEnclaveOptions(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestEphemeralBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: _builtins.str, no_device: Optional[_builtins.bool] = ..., virtual_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestLaunchTemplate(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestMaintenanceOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_recovery: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRecovery")
    def auto_recovery(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestMetadataOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_endpoint: Optional[_builtins.str] = ..., http_protocol_ipv6: Optional[_builtins.str] = ..., http_put_response_hop_limit: Optional[_builtins.int] = ..., http_tokens: Optional[_builtins.str] = ..., instance_metadata_tags: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_index: _builtins.int, network_interface_id: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., network_card_index: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestPrimaryNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.bool] = ..., network_interface_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestPrivateDnsNameOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_resource_name_dns_a_record: Optional[_builtins.bool] = ..., enable_resource_name_dns_aaaa_record: Optional[_builtins.bool] = ..., hostname_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameType")
    def hostname_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestRootBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_on_termination: Optional[_builtins.bool] = ..., device_name: Optional[_builtins.str] = ..., encrypted: Optional[_builtins.bool] = ..., iops: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., tags_all: Optional[Mapping[str, _builtins.str]] = ..., throughput: Optional[_builtins.int] = ..., volume_id: Optional[_builtins.str] = ..., volume_size: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpotInstanceRequestSecondaryNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_card_index: _builtins.int, secondary_subnet_id: _builtins.str, delete_on_termination: Optional[_builtins.bool] = ..., device_index: Optional[_builtins.int] = ..., interface_type: Optional[_builtins.str] = ..., mac_address: Optional[_builtins.str] = ..., private_ip_address_count: Optional[_builtins.int] = ..., private_ip_addresses: Optional[Sequence[_builtins.str]] = ..., secondary_interface_id: Optional[_builtins.str] = ..., secondary_network_id: Optional[_builtins.str] = ..., source_dest_check: Optional[_builtins.bool] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondarySubnetId")
    def secondary_subnet_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddressCount")
    def private_ip_address_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInterfaceId")
    def secondary_interface_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkId")
    def secondary_network_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class TrafficMirrorFilterRuleDestinationPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: Optional[_builtins.int] = ..., to_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TrafficMirrorFilterRuleSourcePortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: Optional[_builtins.int] = ..., to_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VpcBlockPublicAccessExclusionTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcBlockPublicAccessOptionsTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, egress_only_internet_gateway: outputs.VpcEncryptionControlResourceExclusionsEgressOnlyInternetGateway, elastic_file_system: outputs.VpcEncryptionControlResourceExclusionsElasticFileSystem, internet_gateway: outputs.VpcEncryptionControlResourceExclusionsInternetGateway, lambda_: outputs.VpcEncryptionControlResourceExclusionsLambda, nat_gateway: outputs.VpcEncryptionControlResourceExclusionsNatGateway, virtual_private_gateway: outputs.VpcEncryptionControlResourceExclusionsVirtualPrivateGateway, vpc_lattice: outputs.VpcEncryptionControlResourceExclusionsVpcLattice, vpc_peering: outputs.VpcEncryptionControlResourceExclusionsVpcPeering) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGateway")
    def egress_only_internet_gateway(self) -> outputs.VpcEncryptionControlResourceExclusionsEgressOnlyInternetGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticFileSystem")
    def elastic_file_system(self) -> outputs.VpcEncryptionControlResourceExclusionsElasticFileSystem:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateway")
    def internet_gateway(self) -> outputs.VpcEncryptionControlResourceExclusionsInternetGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> outputs.VpcEncryptionControlResourceExclusionsLambda:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> outputs.VpcEncryptionControlResourceExclusionsNatGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualPrivateGateway")
    def virtual_private_gateway(self) -> outputs.VpcEncryptionControlResourceExclusionsVirtualPrivateGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLattice")
    def vpc_lattice(self) -> outputs.VpcEncryptionControlResourceExclusionsVpcLattice:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeering")
    def vpc_peering(self) -> outputs.VpcEncryptionControlResourceExclusionsVpcPeering:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusionsEgressOnlyInternetGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusionsElasticFileSystem(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusionsInternetGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusionsLambda(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusionsNatGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusionsVirtualPrivateGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusionsVpcLattice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlResourceExclusionsVpcPeering(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, state_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEncryptionControlTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcEndpointDnsEntry(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_name: Optional[_builtins.str] = ..., hosted_zone_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcEndpointDnsOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_record_ip_type: Optional[_builtins.str] = ..., private_dns_only_for_inbound_resolver_endpoint: Optional[_builtins.bool] = ..., private_dns_preference: Optional[_builtins.str] = ..., private_dns_specified_domains: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsRecordIpType")
    def dns_record_ip_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsOnlyForInboundResolverEndpoint")
    def private_dns_only_for_inbound_resolver_endpoint(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsPreference")
    def private_dns_preference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsSpecifiedDomains")
    def private_dns_specified_domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VpcEndpointServicePrivateDnsNameConfiguration(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcEndpointSubnetConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ipv4: Optional[_builtins.str] = ..., ipv6: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ipv4(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ipv6(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcIpamOperatingRegion(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, region_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcIpamPoolCidrCidrAuthorizationContext(dict):
    def __init__(__self__, *, message: Optional[_builtins.str] = ..., signature: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def signature(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcIpamPoolSourceResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_id: _builtins.str, resource_owner: _builtins.str, resource_region: _builtins.str, resource_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRegion")
    def resource_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcIpamResourceDiscoveryOperatingRegion(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, region_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcIpamResourceDiscoveryOrganizationalUnitExclusion(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, organizations_entity_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationsEntityPath")
    def organizations_entity_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcPeeringConnectionAccepter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VpcPeeringConnectionAccepterAccepter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VpcPeeringConnectionAccepterRequester(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VpcPeeringConnectionRequester(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VpnConnectionRoute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_cidr_block: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpnConnectionTunnel1LogOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_log_options: Optional[outputs.VpnConnectionTunnel1LogOptionsCloudwatchLogOptions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogOptions")
    def cloudwatch_log_options(self) -> Optional[outputs.VpnConnectionTunnel1LogOptionsCloudwatchLogOptions]:
        
        ...
    


@pulumi.output_type
class VpnConnectionTunnel1LogOptionsCloudwatchLogOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bgp_log_enabled: Optional[_builtins.bool] = ..., bgp_log_group_arn: Optional[_builtins.str] = ..., bgp_log_output_format: Optional[_builtins.str] = ..., log_enabled: Optional[_builtins.bool] = ..., log_group_arn: Optional[_builtins.str] = ..., log_output_format: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogEnabled")
    def bgp_log_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogGroupArn")
    def bgp_log_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogOutputFormat")
    def bgp_log_output_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logEnabled")
    def log_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logOutputFormat")
    def log_output_format(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpnConnectionTunnel2LogOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_log_options: Optional[outputs.VpnConnectionTunnel2LogOptionsCloudwatchLogOptions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogOptions")
    def cloudwatch_log_options(self) -> Optional[outputs.VpnConnectionTunnel2LogOptionsCloudwatchLogOptions]:
        
        ...
    


@pulumi.output_type
class VpnConnectionTunnel2LogOptionsCloudwatchLogOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bgp_log_enabled: Optional[_builtins.bool] = ..., bgp_log_group_arn: Optional[_builtins.str] = ..., bgp_log_output_format: Optional[_builtins.str] = ..., log_enabled: Optional[_builtins.bool] = ..., log_group_arn: Optional[_builtins.str] = ..., log_output_format: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogEnabled")
    def bgp_log_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogGroupArn")
    def bgp_log_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogOutputFormat")
    def bgp_log_output_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logEnabled")
    def log_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logOutputFormat")
    def log_output_format(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpnConnectionVgwTelemetry(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accepted_route_count: Optional[_builtins.int] = ..., certificate_arn: Optional[_builtins.str] = ..., last_status_change: Optional[_builtins.str] = ..., outside_ip_address: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., status_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptedRouteCount")
    def accepted_route_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStatusChange")
    def last_status_change(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outsideIpAddress")
    def outside_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetAmiBlockDeviceMappingResult(dict):
    def __init__(__self__, *, device_name: _builtins.str, ebs: Mapping[str, _builtins.str], no_device: _builtins.str, virtual_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ebs(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetAmiFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetAmiIdsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetAmiProductCodeResult(dict):
    def __init__(__self__, *, product_code_id: _builtins.str, product_code_type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCodeId")
    def product_code_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCodeType")
    def product_code_type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetCoipPoolFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetCoipPoolsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetCustomerGatewayFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetDedicatedHostFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetEipsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetElasticIpFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetInstanceCreditSpecificationResult(dict):
    def __init__(__self__, *, cpu_credits: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetInstanceEbsBlockDeviceResult(dict):
    def __init__(__self__, *, delete_on_termination: _builtins.bool, device_name: _builtins.str, encrypted: _builtins.bool, iops: _builtins.int, kms_key_id: _builtins.str, snapshot_id: _builtins.str, tags: Mapping[str, _builtins.str], throughput: _builtins.int, volume_id: _builtins.str, volume_size: _builtins.int, volume_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceEnclaveOptionResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetInstanceEphemeralBlockDeviceResult(dict):
    def __init__(__self__, *, device_name: _builtins.str, no_device: Optional[_builtins.bool] = ..., virtual_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInstanceFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInstanceMaintenanceOptionResult(dict):
    def __init__(__self__, *, auto_recovery: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRecovery")
    def auto_recovery(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceMetadataOptionResult(dict):
    def __init__(__self__, *, http_endpoint: _builtins.str, http_protocol_ipv6: _builtins.str, http_put_response_hop_limit: _builtins.int, http_tokens: _builtins.str, instance_metadata_tags: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstancePrivateDnsNameOptionResult(dict):
    def __init__(__self__, *, enable_resource_name_dns_a_record: _builtins.bool, enable_resource_name_dns_aaaa_record: _builtins.bool, hostname_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameType")
    def hostname_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceRootBlockDeviceResult(dict):
    def __init__(__self__, *, delete_on_termination: _builtins.bool, device_name: _builtins.str, encrypted: _builtins.bool, iops: _builtins.int, kms_key_id: _builtins.str, tags: Mapping[str, _builtins.str], throughput: _builtins.int, volume_id: _builtins.str, volume_size: _builtins.int, volume_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceTypeFpgaResult(dict):
    def __init__(__self__, *, count: _builtins.int, manufacturer: _builtins.str, memory_size: _builtins.int, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def manufacturer(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetInstanceTypeGpusResult(dict):
    def __init__(__self__, *, count: _builtins.int, manufacturer: _builtins.str, memory_size: _builtins.int, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def manufacturer(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetInstanceTypeInferenceAcceleratorResult(dict):
    def __init__(__self__, *, count: _builtins.int, manufacturer: _builtins.str, memory_size: _builtins.int, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def manufacturer(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetInstanceTypeInstanceDiskResult(dict):
    def __init__(__self__, *, count: _builtins.int, size: _builtins.int, type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetInstanceTypeMediaAcceleratorResult(dict):
    def __init__(__self__, *, count: _builtins.int, manufacturer: _builtins.str, memory_size: _builtins.int, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def manufacturer(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetInstanceTypeNetworkCardResult(dict):
    def __init__(__self__, *, baseline_bandwidth: _builtins.float, index: _builtins.int, maximum_interfaces: _builtins.int, peak_bandwidth: _builtins.float, performance: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineBandwidth")
    def baseline_bandwidth(self) -> _builtins.float:
        ...
    
    @_builtins.property
    @pulumi.getter
    def index(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumInterfaces")
    def maximum_interfaces(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakBandwidth")
    def peak_bandwidth(self) -> _builtins.float:
        ...
    
    @_builtins.property
    @pulumi.getter
    def performance(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetInstanceTypeNeuronDeviceResult(dict):
    def __init__(__self__, *, core_count: _builtins.int, core_version: _builtins.int, count: _builtins.int, memory_size: _builtins.int, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreVersion")
    def core_version(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetInstanceTypeOfferingFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInstanceTypeOfferingsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInstanceTypesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInstancesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInternetGatewayAttachmentResult(dict):
    def __init__(__self__, *, state: _builtins.str, vpc_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInternetGatewayFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetKeyPairFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLaunchConfigurationEbsBlockDeviceResult(dict):
    def __init__(__self__, *, delete_on_termination: _builtins.bool, device_name: _builtins.str, encrypted: _builtins.bool, iops: _builtins.int, no_device: _builtins.bool, snapshot_id: _builtins.str, throughput: _builtins.int, volume_size: _builtins.int, volume_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetLaunchConfigurationEphemeralBlockDeviceResult(dict):
    def __init__(__self__, *, device_name: _builtins.str, virtual_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetLaunchConfigurationMetadataOptionResult(dict):
    def __init__(__self__, *, http_endpoint: _builtins.str, http_put_response_hop_limit: _builtins.int, http_tokens: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetLaunchConfigurationRootBlockDeviceResult(dict):
    def __init__(__self__, *, delete_on_termination: _builtins.bool, encrypted: _builtins.bool, iops: _builtins.int, throughput: _builtins.int, volume_size: _builtins.int, volume_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetLaunchTemplateBlockDeviceMappingResult(dict):
    def __init__(__self__, *, device_name: _builtins.str, ebs: Sequence[outputs.GetLaunchTemplateBlockDeviceMappingEbResult], no_device: _builtins.str, virtual_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ebs(self) -> Sequence[outputs.GetLaunchTemplateBlockDeviceMappingEbResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateBlockDeviceMappingEbResult(dict):
    def __init__(__self__, *, delete_on_termination: _builtins.str, encrypted: _builtins.str, iops: _builtins.int, kms_key_id: _builtins.str, snapshot_id: _builtins.str, throughput: _builtins.int, volume_initialization_rate: _builtins.int, volume_size: _builtins.int, volume_type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeInitializationRate")
    def volume_initialization_rate(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateCapacityReservationSpecificationResult(dict):
    def __init__(__self__, *, capacity_reservation_preference: _builtins.str, capacity_reservation_targets: Sequence[outputs.GetLaunchTemplateCapacityReservationSpecificationCapacityReservationTargetResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationTargets")
    def capacity_reservation_targets(self) -> Sequence[outputs.GetLaunchTemplateCapacityReservationSpecificationCapacityReservationTargetResult]:
        ...
    


@pulumi.output_type
class GetLaunchTemplateCapacityReservationSpecificationCapacityReservationTargetResult(dict):
    def __init__(__self__, *, capacity_reservation_id: _builtins.str, capacity_reservation_resource_group_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationId")
    def capacity_reservation_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateCpuOptionResult(dict):
    def __init__(__self__, *, amd_sev_snp: _builtins.str, core_count: _builtins.int, nested_virtualization: _builtins.str, threads_per_core: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amdSevSnp")
    def amd_sev_snp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestedVirtualization")
    def nested_virtualization(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetLaunchTemplateCreditSpecificationResult(dict):
    def __init__(__self__, *, cpu_credits: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateEnclaveOptionResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetLaunchTemplateFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLaunchTemplateHibernationOptionResult(dict):
    def __init__(__self__, *, configured: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configured(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetLaunchTemplateIamInstanceProfileResult(dict):
    def __init__(__self__, *, arn: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceMarketOptionResult(dict):
    def __init__(__self__, *, market_type: _builtins.str, spot_options: Sequence[outputs.GetLaunchTemplateInstanceMarketOptionSpotOptionResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketType")
    def market_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Sequence[outputs.GetLaunchTemplateInstanceMarketOptionSpotOptionResult]:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceMarketOptionSpotOptionResult(dict):
    def __init__(__self__, *, block_duration_minutes: _builtins.int, instance_interruption_behavior: _builtins.str, max_price: _builtins.str, spot_instance_type: _builtins.str, valid_until: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrice")
    def max_price(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstanceType")
    def spot_instance_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementResult(dict):
    def __init__(__self__, *, accelerator_counts: Sequence[outputs.GetLaunchTemplateInstanceRequirementAcceleratorCountResult], accelerator_manufacturers: Sequence[_builtins.str], accelerator_names: Sequence[_builtins.str], accelerator_total_memory_mibs: Sequence[outputs.GetLaunchTemplateInstanceRequirementAcceleratorTotalMemoryMibResult], accelerator_types: Sequence[_builtins.str], allowed_instance_types: Sequence[_builtins.str], bare_metal: _builtins.str, baseline_ebs_bandwidth_mbps: Sequence[outputs.GetLaunchTemplateInstanceRequirementBaselineEbsBandwidthMbpResult], burstable_performance: _builtins.str, cpu_manufacturers: Sequence[_builtins.str], excluded_instance_types: Sequence[_builtins.str], instance_generations: Sequence[_builtins.str], local_storage: _builtins.str, local_storage_types: Sequence[_builtins.str], max_spot_price_as_percentage_of_optimal_on_demand_price: _builtins.int, memory_gib_per_vcpus: Sequence[outputs.GetLaunchTemplateInstanceRequirementMemoryGibPerVcpusResult], memory_mibs: Sequence[outputs.GetLaunchTemplateInstanceRequirementMemoryMibResult], network_bandwidth_gbps: Sequence[outputs.GetLaunchTemplateInstanceRequirementNetworkBandwidthGbpResult], network_interface_counts: Sequence[outputs.GetLaunchTemplateInstanceRequirementNetworkInterfaceCountResult], on_demand_max_price_percentage_over_lowest_price: _builtins.int, require_hibernate_support: _builtins.bool, spot_max_price_percentage_over_lowest_price: _builtins.int, total_local_storage_gbs: Sequence[outputs.GetLaunchTemplateInstanceRequirementTotalLocalStorageGbResult], vcpu_counts: Sequence[outputs.GetLaunchTemplateInstanceRequirementVcpuCountResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCounts")
    def accelerator_counts(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementAcceleratorCountResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMibs")
    def accelerator_total_memory_mibs(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementAcceleratorTotalMemoryMibResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementBaselineEbsBandwidthMbpResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSpotPriceAsPercentageOfOptimalOnDemandPrice")
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpus")
    def memory_gib_per_vcpus(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementMemoryGibPerVcpusResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMibs")
    def memory_mibs(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementMemoryMibResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementNetworkBandwidthGbpResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCounts")
    def network_interface_counts(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementNetworkInterfaceCountResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGbs")
    def total_local_storage_gbs(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementTotalLocalStorageGbResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCounts")
    def vcpu_counts(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementVcpuCountResult]:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementAcceleratorCountResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementAcceleratorTotalMemoryMibResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementBaselineEbsBandwidthMbpResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementMemoryGibPerVcpusResult(dict):
    def __init__(__self__, *, max: _builtins.float, min: _builtins.float) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.float:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.float:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementMemoryMibResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementNetworkBandwidthGbpResult(dict):
    def __init__(__self__, *, max: _builtins.float, min: _builtins.float) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.float:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.float:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementNetworkInterfaceCountResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementTotalLocalStorageGbResult(dict):
    def __init__(__self__, *, max: _builtins.float, min: _builtins.float) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.float:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.float:
        ...
    


@pulumi.output_type
class GetLaunchTemplateInstanceRequirementVcpuCountResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetLaunchTemplateLicenseSpecificationResult(dict):
    def __init__(__self__, *, license_configuration_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseConfigurationArn")
    def license_configuration_arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateMaintenanceOptionResult(dict):
    def __init__(__self__, *, auto_recovery: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRecovery")
    def auto_recovery(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateMetadataOptionResult(dict):
    def __init__(__self__, *, http_endpoint: _builtins.str, http_protocol_ipv6: _builtins.str, http_put_response_hop_limit: _builtins.int, http_tokens: _builtins.str, instance_metadata_tags: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateMonitoringResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetLaunchTemplateNetworkInterfaceResult(dict):
    def __init__(__self__, *, associate_carrier_ip_address: _builtins.str, connection_tracking_specifications: Sequence[outputs.GetLaunchTemplateNetworkInterfaceConnectionTrackingSpecificationResult], description: _builtins.str, device_index: _builtins.int, interface_type: _builtins.str, ipv4_address_count: _builtins.int, ipv4_addresses: Sequence[_builtins.str], ipv4_prefix_count: _builtins.int, ipv4_prefixes: Sequence[_builtins.str], ipv6_address_count: _builtins.int, ipv6_addresses: Sequence[_builtins.str], ipv6_prefix_count: _builtins.int, ipv6_prefixes: Sequence[_builtins.str], network_card_index: _builtins.int, network_interface_id: _builtins.str, primary_ipv6: _builtins.str, private_ip_address: _builtins.str, security_groups: Sequence[_builtins.str], subnet_id: _builtins.str, associate_public_ip_address: Optional[_builtins.bool] = ..., delete_on_termination: Optional[_builtins.bool] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateCarrierIpAddress")
    def associate_carrier_ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTrackingSpecifications")
    def connection_tracking_specifications(self) -> Sequence[outputs.GetLaunchTemplateNetworkInterfaceConnectionTrackingSpecificationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4AddressCount")
    def ipv4_address_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4PrefixCount")
    def ipv4_prefix_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Prefixes")
    def ipv4_prefixes(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6PrefixCount")
    def ipv6_prefix_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Prefixes")
    def ipv6_prefixes(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv6")
    def primary_ipv6(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class GetLaunchTemplateNetworkInterfaceConnectionTrackingSpecificationResult(dict):
    def __init__(__self__, *, tcp_established_timeout: _builtins.int, udp_stream_timeout: _builtins.int, udp_timeout: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpEstablishedTimeout")
    def tcp_established_timeout(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpStreamTimeout")
    def udp_stream_timeout(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpTimeout")
    def udp_timeout(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetLaunchTemplateNetworkPerformanceOptionResult(dict):
    def __init__(__self__, *, bandwidth_weighting: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthWeighting")
    def bandwidth_weighting(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplatePlacementResult(dict):
    def __init__(__self__, *, affinity: _builtins.str, availability_zone: _builtins.str, group_id: _builtins.str, group_name: _builtins.str, host_id: _builtins.str, host_resource_group_arn: _builtins.str, partition_number: _builtins.int, spread_domain: _builtins.str, tenancy: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def affinity(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionNumber")
    def partition_number(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spreadDomain")
    def spread_domain(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplatePrivateDnsNameOptionResult(dict):
    def __init__(__self__, *, enable_resource_name_dns_a_record: _builtins.bool, enable_resource_name_dns_aaaa_record: _builtins.bool, hostname_type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameType")
    def hostname_type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateSecondaryInterfaceResult(dict):
    def __init__(__self__, *, delete_on_termination: _builtins.bool, device_index: _builtins.int, interface_type: _builtins.str, network_card_index: _builtins.int, private_ip_address_count: _builtins.int, private_ip_addresses: Sequence[_builtins.str], secondary_subnet_id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddressCount")
    def private_ip_address_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondarySubnetId")
    def secondary_subnet_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetLaunchTemplateTagSpecificationResult(dict):
    def __init__(__self__, *, resource_type: _builtins.str, tags: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLocalGatewayFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLocalGatewayRouteTableFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLocalGatewayRouteTablesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLocalGatewayVirtualInterfaceFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLocalGatewayVirtualInterfaceGroupFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLocalGatewayVirtualInterfaceGroupsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetLocalGatewaysFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetManagedPrefixListEntryResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, description: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetManagedPrefixListFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetManagedPrefixListsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetNatGatewayAvailabilityZoneAddressResult(dict):
    def __init__(__self__, *, allocation_ids: Sequence[_builtins.str], availability_zone: _builtins.str, availability_zone_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationIds")
    def allocation_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNatGatewayFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetNatGatewayRegionalNatGatewayAddressResult(dict):
    def __init__(__self__, *, allocation_id: _builtins.str, association_id: _builtins.str, availability_zone: _builtins.str, availability_zone_id: _builtins.str, network_interface_id: _builtins.str, public_ip: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNatGatewaysFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetNetworkAclsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisAlternatePathHintResult(dict):
    def __init__(__self__, *, component_arn: _builtins.str, component_id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationResult(dict):
    def __init__(__self__, *, acl_rules: Sequence[outputs.GetNetworkInsightsAnalysisExplanationAclRuleResult], acls: Sequence[outputs.GetNetworkInsightsAnalysisExplanationAclResult], address: _builtins.str, addresses: Sequence[_builtins.str], attached_tos: Sequence[outputs.GetNetworkInsightsAnalysisExplanationAttachedToResult], availability_zones: Sequence[_builtins.str], cidrs: Sequence[_builtins.str], classic_load_balancer_listeners: Sequence[outputs.GetNetworkInsightsAnalysisExplanationClassicLoadBalancerListenerResult], components: Sequence[outputs.GetNetworkInsightsAnalysisExplanationComponentResult], customer_gateways: Sequence[outputs.GetNetworkInsightsAnalysisExplanationCustomerGatewayResult], destination_vpcs: Sequence[outputs.GetNetworkInsightsAnalysisExplanationDestinationVpcResult], destinations: Sequence[outputs.GetNetworkInsightsAnalysisExplanationDestinationResult], direction: _builtins.str, elastic_load_balancer_listeners: Sequence[outputs.GetNetworkInsightsAnalysisExplanationElasticLoadBalancerListenerResult], explanation_code: _builtins.str, ingress_route_tables: Sequence[outputs.GetNetworkInsightsAnalysisExplanationIngressRouteTableResult], internet_gateways: Sequence[outputs.GetNetworkInsightsAnalysisExplanationInternetGatewayResult], load_balancer_arn: _builtins.str, load_balancer_listener_port: _builtins.int, load_balancer_target_group: Sequence[outputs.GetNetworkInsightsAnalysisExplanationLoadBalancerTargetGroupResult], load_balancer_target_groups: Sequence[outputs.GetNetworkInsightsAnalysisExplanationLoadBalancerTargetGroupResult], load_balancer_target_port: _builtins.int, missing_component: _builtins.str, nat_gateways: Sequence[outputs.GetNetworkInsightsAnalysisExplanationNatGatewayResult], network_interfaces: Sequence[outputs.GetNetworkInsightsAnalysisExplanationNetworkInterfaceResult], packet_field: _builtins.str, port: _builtins.int, port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisExplanationPortRangeResult], prefix_lists: Sequence[outputs.GetNetworkInsightsAnalysisExplanationPrefixListResult], protocols: Sequence[_builtins.str], route_table_routes: Sequence[outputs.GetNetworkInsightsAnalysisExplanationRouteTableRouteResult], route_tables: Sequence[outputs.GetNetworkInsightsAnalysisExplanationRouteTableResult], security_group: Sequence[outputs.GetNetworkInsightsAnalysisExplanationSecurityGroupResult], security_group_rules: Sequence[outputs.GetNetworkInsightsAnalysisExplanationSecurityGroupRuleResult], security_groups: Sequence[outputs.GetNetworkInsightsAnalysisExplanationSecurityGroupResult], source_vpcs: Sequence[outputs.GetNetworkInsightsAnalysisExplanationSourceVpcResult], state: _builtins.str, subnet_route_tables: Sequence[outputs.GetNetworkInsightsAnalysisExplanationSubnetRouteTableResult], subnets: Sequence[outputs.GetNetworkInsightsAnalysisExplanationSubnetResult], transit_gateway_attachments: Sequence[outputs.GetNetworkInsightsAnalysisExplanationTransitGatewayAttachmentResult], transit_gateway_route_table_routes: Sequence[outputs.GetNetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteResult], transit_gateway_route_tables: Sequence[outputs.GetNetworkInsightsAnalysisExplanationTransitGatewayRouteTableResult], transit_gateways: Sequence[outputs.GetNetworkInsightsAnalysisExplanationTransitGatewayResult], vpc_endpoints: Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpcEndpointResult], vpc_peering_connections: Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpcPeeringConnectionResult], vpcs: Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpcResult], vpn_connections: Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpnConnectionResult], vpn_gateways: Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpnGatewayResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationAclRuleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def acls(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationAclResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationAttachedToResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classicLoadBalancerListeners")
    def classic_load_balancer_listeners(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationClassicLoadBalancerListenerResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationComponentResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerGateways")
    def customer_gateways(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationCustomerGatewayResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationDestinationVpcResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationDestinationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticLoadBalancerListeners")
    def elastic_load_balancer_listeners(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationElasticLoadBalancerListenerResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="explanationCode")
    def explanation_code(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressRouteTables")
    def ingress_route_tables(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationIngressRouteTableResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateways")
    def internet_gateways(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationInternetGatewayResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerListenerPort")
    def load_balancer_listener_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetGroup")
    def load_balancer_target_group(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationLoadBalancerTargetGroupResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetGroups")
    def load_balancer_target_groups(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationLoadBalancerTargetGroupResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetPort")
    def load_balancer_target_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="missingComponent")
    def missing_component(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateways")
    def nat_gateways(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationNatGatewayResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationNetworkInterfaceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packetField")
    def packet_field(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationPortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationPrefixListResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationRouteTableRouteResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTables")
    def route_tables(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationRouteTableResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationSecurityGroupResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationSecurityGroupRuleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationSecurityGroupResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationSourceVpcResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetRouteTables")
    def subnet_route_tables(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationSubnetRouteTableResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationSubnetResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachments")
    def transit_gateway_attachments(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationTransitGatewayAttachmentResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTables")
    def transit_gateway_route_tables(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationTransitGatewayRouteTableResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationTransitGatewayResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpcEndpointResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnections")
    def vpc_peering_connections(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpcPeeringConnectionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpcResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnConnections")
    def vpn_connections(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpnConnectionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnGateways")
    def vpn_gateways(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationVpnGatewayResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationAclResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationAclRuleResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, egress: _builtins.bool, port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisExplanationAclRulePortRangeResult], protocol: _builtins.str, rule_action: _builtins.str, rule_number: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationAclRulePortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationAclRulePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationAttachedToResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationClassicLoadBalancerListenerResult(dict):
    def __init__(__self__, *, instance_port: _builtins.int, load_balancer_port: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerPort")
    def load_balancer_port(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationComponentResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationCustomerGatewayResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationDestinationResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationDestinationVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationElasticLoadBalancerListenerResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationIngressRouteTableResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationInternetGatewayResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationLoadBalancerTargetGroupResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationNatGatewayResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationNetworkInterfaceResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationPortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationPrefixListResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationRouteTableResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationRouteTableRouteResult(dict):
    def __init__(__self__, *, destination_cidr: _builtins.str, destination_prefix_list_id: _builtins.str, egress_only_internet_gateway_id: _builtins.str, gateway_id: _builtins.str, instance_id: _builtins.str, nat_gateway_id: _builtins.str, network_interface_id: _builtins.str, origin: _builtins.str, transit_gateway_id: _builtins.str, vpc_peering_connection_id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationSecurityGroupResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationSecurityGroupRuleResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, direction: _builtins.str, port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeResult], prefix_list_id: _builtins.str, protocol: _builtins.str, security_group_id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationSourceVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationSubnetResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationSubnetRouteTableResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationTransitGatewayResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationTransitGatewayAttachmentResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationTransitGatewayRouteTableResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteResult(dict):
    def __init__(__self__, *, attachment_id: _builtins.str, destination_cidr: _builtins.str, prefix_list_id: _builtins.str, resource_id: _builtins.str, resource_type: _builtins.str, route_origin: _builtins.str, state: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationVpcEndpointResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationVpcPeeringConnectionResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationVpnConnectionResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisExplanationVpnGatewayResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentResult(dict):
    def __init__(__self__, *, acl_rules: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAclRuleResult], additional_details: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAdditionalDetailResult], attached_tos: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAttachedToResult], components: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentComponentResult], destination_vpcs: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentDestinationVpcResult], inbound_headers: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderResult], outbound_headers: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderResult], route_table_routes: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentRouteTableRouteResult], security_group_rules: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleResult], sequence_number: _builtins.int, source_vpcs: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentSourceVpcResult], subnets: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentSubnetResult], transit_gateway_route_table_routes: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteResult], transit_gateways: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentTransitGatewayResult], vpcs: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentVpcResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAclRuleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAdditionalDetailResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAttachedToResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentComponentResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentDestinationVpcResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundHeaders")
    def inbound_headers(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundHeaders")
    def outbound_headers(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentRouteTableRouteResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentSourceVpcResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentSubnetResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentTransitGatewayResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentVpcResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentAclRuleResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, egress: _builtins.bool, port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAclRulePortRangeResult], protocol: _builtins.str, rule_action: _builtins.str, rule_number: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAclRulePortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentAclRulePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentAdditionalDetailResult(dict):
    def __init__(__self__, *, additional_detail_type: _builtins.str, components: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetailType")
    def additional_detail_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentAttachedToResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentComponentResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentDestinationVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderResult(dict):
    def __init__(__self__, *, destination_addresses: Sequence[_builtins.str], destination_port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeResult], protocol: _builtins.str, source_addresses: Sequence[_builtins.str], source_port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderResult(dict):
    def __init__(__self__, *, destination_addresses: Sequence[_builtins.str], destination_port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeResult], protocol: _builtins.str, source_addresses: Sequence[_builtins.str], source_port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentRouteTableRouteResult(dict):
    def __init__(__self__, *, destination_cidr: _builtins.str, destination_prefix_list_id: _builtins.str, egress_only_internet_gateway_id: _builtins.str, gateway_id: _builtins.str, instance_id: _builtins.str, nat_gateway_id: _builtins.str, network_interface_id: _builtins.str, origin: _builtins.str, transit_gateway_id: _builtins.str, vpc_peering_connection_id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, direction: _builtins.str, port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeResult], prefix_list_id: _builtins.str, protocol: _builtins.str, security_group_id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentSourceVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentSubnetResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentTransitGatewayResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteResult(dict):
    def __init__(__self__, *, attachment_id: _builtins.str, destination_cidr: _builtins.str, prefix_list_id: _builtins.str, resource_id: _builtins.str, resource_type: _builtins.str, route_origin: _builtins.str, state: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisForwardPathComponentVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentResult(dict):
    def __init__(__self__, *, acl_rules: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAclRuleResult], additional_details: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAdditionalDetailResult], attached_tos: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAttachedToResult], components: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentComponentResult], destination_vpcs: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentDestinationVpcResult], inbound_headers: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderResult], outbound_headers: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderResult], route_table_routes: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentRouteTableRouteResult], security_group_rules: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleResult], sequence_number: _builtins.int, source_vpcs: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentSourceVpcResult], subnets: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentSubnetResult], transit_gateway_route_table_routes: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteResult], transit_gateways: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentTransitGatewayResult], vpcs: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentVpcResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAclRuleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAdditionalDetailResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAttachedToResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentComponentResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentDestinationVpcResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundHeaders")
    def inbound_headers(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundHeaders")
    def outbound_headers(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentRouteTableRouteResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentSourceVpcResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentSubnetResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentTransitGatewayResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentVpcResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentAclRuleResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, egress: _builtins.bool, port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAclRulePortRangeResult], protocol: _builtins.str, rule_action: _builtins.str, rule_number: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAclRulePortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentAclRulePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentAdditionalDetailResult(dict):
    def __init__(__self__, *, additional_detail_type: _builtins.str, components: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetailType")
    def additional_detail_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentAttachedToResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentComponentResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentDestinationVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderResult(dict):
    def __init__(__self__, *, destination_addresses: Sequence[_builtins.str], destination_port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeResult], protocol: _builtins.str, source_addresses: Sequence[_builtins.str], source_port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderResult(dict):
    def __init__(__self__, *, destination_addresses: Sequence[_builtins.str], destination_port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeResult], protocol: _builtins.str, source_addresses: Sequence[_builtins.str], source_port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentRouteTableRouteResult(dict):
    def __init__(__self__, *, destination_cidr: _builtins.str, destination_prefix_list_id: _builtins.str, egress_only_internet_gateway_id: _builtins.str, gateway_id: _builtins.str, instance_id: _builtins.str, nat_gateway_id: _builtins.str, network_interface_id: _builtins.str, origin: _builtins.str, transit_gateway_id: _builtins.str, vpc_peering_connection_id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, direction: _builtins.str, port_ranges: Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeResult], prefix_list_id: _builtins.str, protocol: _builtins.str, security_group_id: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeResult(dict):
    def __init__(__self__, *, from_: _builtins.int, to: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentSourceVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentSubnetResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentTransitGatewayResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteResult(dict):
    def __init__(__self__, *, attachment_id: _builtins.str, destination_cidr: _builtins.str, prefix_list_id: _builtins.str, resource_id: _builtins.str, resource_type: _builtins.str, route_origin: _builtins.str, state: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetNetworkInsightsAnalysisReturnPathComponentVpcResult(dict):
    def __init__(__self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsPathFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetNetworkInsightsPathFilterAtDestinationResult(dict):
    def __init__(__self__, *, destination_address: _builtins.str, destination_port_ranges: Sequence[outputs.GetNetworkInsightsPathFilterAtDestinationDestinationPortRangeResult], source_address: _builtins.str, source_port_ranges: Sequence[outputs.GetNetworkInsightsPathFilterAtDestinationSourcePortRangeResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsPathFilterAtDestinationDestinationPortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddress")
    def source_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsPathFilterAtDestinationSourcePortRangeResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsPathFilterAtDestinationDestinationPortRangeResult(dict):
    def __init__(__self__, *, from_port: _builtins.int, to_port: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsPathFilterAtDestinationSourcePortRangeResult(dict):
    def __init__(__self__, *, from_port: _builtins.int, to_port: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsPathFilterAtSourceResult(dict):
    def __init__(__self__, *, destination_address: _builtins.str, destination_port_ranges: Sequence[outputs.GetNetworkInsightsPathFilterAtSourceDestinationPortRangeResult], source_address: _builtins.str, source_port_ranges: Sequence[outputs.GetNetworkInsightsPathFilterAtSourceSourcePortRangeResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsPathFilterAtSourceDestinationPortRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddress")
    def source_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Sequence[outputs.GetNetworkInsightsPathFilterAtSourceSourcePortRangeResult]:
        ...
    


@pulumi.output_type
class GetNetworkInsightsPathFilterAtSourceDestinationPortRangeResult(dict):
    def __init__(__self__, *, from_port: _builtins.int, to_port: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInsightsPathFilterAtSourceSourcePortRangeResult(dict):
    def __init__(__self__, *, from_port: _builtins.int, to_port: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetNetworkInterfaceAssociationResult(dict):
    def __init__(__self__, *, allocation_id: _builtins.str, association_id: _builtins.str, carrier_ip: _builtins.str, customer_owned_ip: _builtins.str, ip_owner_id: _builtins.str, public_dns_name: _builtins.str, public_ip: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierIp")
    def carrier_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIp")
    def customer_owned_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipOwnerId")
    def ip_owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDnsName")
    def public_dns_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkInterfaceAttachmentResult(dict):
    def __init__(__self__, *, attachment_id: _builtins.str, device_index: _builtins.int, instance_id: _builtins.str, instance_owner_id: _builtins.str, network_card_index: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceOwnerId")
    def instance_owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetNetworkInterfaceFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetNetworkInterfacesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetPrefixListFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetPublicIpv4PoolPoolAddressRangeResult(dict):
    def __init__(__self__, *, address_count: _builtins.int, available_address_count: _builtins.int, first_address: _builtins.str, last_address: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressCount")
    def address_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableAddressCount")
    def available_address_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstAddress")
    def first_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAddress")
    def last_address(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPublicIpv4PoolsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetRouteTableAssociationResult(dict):
    def __init__(__self__, *, gateway_id: _builtins.str, main: _builtins.bool, route_table_association_id: _builtins.str, route_table_id: _builtins.str, subnet_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def main(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableAssociationId")
    def route_table_association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRouteTableFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetRouteTableRouteResult(dict):
    def __init__(__self__, *, carrier_gateway_id: _builtins.str, cidr_block: _builtins.str, core_network_arn: _builtins.str, destination_prefix_list_id: _builtins.str, egress_only_gateway_id: _builtins.str, gateway_id: _builtins.str, instance_id: _builtins.str, ipv6_cidr_block: _builtins.str, local_gateway_id: _builtins.str, nat_gateway_id: _builtins.str, network_interface_id: _builtins.str, transit_gateway_id: _builtins.str, vpc_endpoint_id: _builtins.str, vpc_peering_connection_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierGatewayId")
    def carrier_gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRouteTablesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSecurityGroupFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSecurityGroupsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetSpotPriceFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSubnetFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSubnetsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetTransitGatewayRouteTablesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcCidrBlockAssociationResult(dict):
    def __init__(__self__, *, association_id: _builtins.str, cidr_block: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVpcDhcpOptionsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcEndpointDnsEntryResult(dict):
    def __init__(__self__, *, dns_name: _builtins.str, hosted_zone_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVpcEndpointDnsOptionResult(dict):
    def __init__(__self__, *, dns_record_ip_type: _builtins.str, private_dns_only_for_inbound_resolver_endpoint: _builtins.bool, private_dns_preference: _builtins.str, private_dns_specified_domains: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsRecordIpType")
    def dns_record_ip_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsOnlyForInboundResolverEndpoint")
    def private_dns_only_for_inbound_resolver_endpoint(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsPreference")
    def private_dns_preference(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsSpecifiedDomains")
    def private_dns_specified_domains(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcEndpointFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcEndpointServiceFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcIpamOperatingRegionResult(dict):
    def __init__(__self__, *, region_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetVpcIpamPoolCidrsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcIpamPoolCidrsIpamPoolCidrResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVpcIpamPoolFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcIpamPoolSourceResourceResult(dict):
    def __init__(__self__, *, resource_id: _builtins.str, resource_owner: _builtins.str, resource_region: _builtins.str, resource_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRegion")
    def resource_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVpcIpamPoolsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcIpamPoolsIpamPoolResult(dict):
    def __init__(__self__, *, address_family: _builtins.str, allocation_default_netmask_length: _builtins.int, allocation_max_netmask_length: _builtins.int, allocation_min_netmask_length: _builtins.int, allocation_resource_tags: Mapping[str, _builtins.str], arn: _builtins.str, auto_import: _builtins.bool, aws_service: _builtins.str, description: _builtins.str, id: _builtins.str, ipam_scope_id: _builtins.str, ipam_scope_type: _builtins.str, locale: _builtins.str, pool_depth: _builtins.int, publicly_advertisable: _builtins.bool, source_ipam_pool_id: _builtins.str, state: _builtins.str, tags: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationDefaultNetmaskLength")
    def allocation_default_netmask_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationMaxNetmaskLength")
    def allocation_max_netmask_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationMinNetmaskLength")
    def allocation_min_netmask_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationResourceTags")
    def allocation_resource_tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoImport")
    def auto_import(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsService")
    def aws_service(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamScopeId")
    def ipam_scope_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamScopeType")
    def ipam_scope_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolDepth")
    def pool_depth(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAdvertisable")
    def publicly_advertisable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIpamPoolId")
    def source_ipam_pool_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcIpamsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcIpamsIpamResult(dict):
    def __init__(__self__, *, arn: _builtins.str, default_resource_discovery_association_id: _builtins.str, default_resource_discovery_id: _builtins.str, description: _builtins.str, enable_private_gua: _builtins.bool, id: _builtins.str, ipam_region: _builtins.str, metered_account: _builtins.str, operating_regions: Sequence[outputs.GetVpcIpamsIpamOperatingRegionResult], owner_id: _builtins.str, private_default_scope_id: _builtins.str, public_default_scope_id: _builtins.str, resource_discovery_association_count: _builtins.int, scope_count: _builtins.int, state: _builtins.str, state_message: _builtins.str, tier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceDiscoveryAssociationId")
    def default_resource_discovery_association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceDiscoveryId")
    def default_resource_discovery_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateGua")
    def enable_private_gua(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamRegion")
    def ipam_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="meteredAccount")
    def metered_account(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> Sequence[outputs.GetVpcIpamsIpamOperatingRegionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDefaultScopeId")
    def private_default_scope_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDefaultScopeId")
    def public_default_scope_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceDiscoveryAssociationCount")
    def resource_discovery_association_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeCount")
    def scope_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVpcIpamsIpamOperatingRegionResult(dict):
    def __init__(__self__, *, region_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetVpcPeeringConnectionCidrBlockSetResult(dict):
    def __init__(__self__, *, cidr_block: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVpcPeeringConnectionFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcPeeringConnectionIpv6CidrBlockSetResult(dict):
    def __init__(__self__, *, ipv6_cidr_block: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetVpcPeeringConnectionPeerCidrBlockSetResult(dict):
    def __init__(__self__, *, cidr_block: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVpcPeeringConnectionPeerIpv6CidrBlockSetResult(dict):
    def __init__(__self__, *, ipv6_cidr_block: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetVpcPeeringConnectionsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpcsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpnConnectionFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetVpnConnectionRouteResult(dict):
    def __init__(__self__, *, destination_cidr_block: _builtins.str, source: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVpnConnectionVgwTelemetryResult(dict):
    def __init__(__self__, *, accepted_route_count: _builtins.int, last_status_change: _builtins.str, outside_ip_address: _builtins.str, status: _builtins.str, status_message: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptedRouteCount")
    def accepted_route_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStatusChange")
    def last_status_change(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outsideIpAddress")
    def outside_ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetVpnGatewayFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


