

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AllowedImagesSettingsImageCriterionArgs', 'AllowedImagesSettingsImageCriterionArgsDict', ..., ..., ..., ..., 'AmiCopyEbsBlockDeviceArgs', 'AmiCopyEbsBlockDeviceArgsDict', 'AmiCopyEphemeralBlockDeviceArgs', 'AmiCopyEphemeralBlockDeviceArgsDict', 'AmiEbsBlockDeviceArgs', 'AmiEbsBlockDeviceArgsDict', 'AmiEphemeralBlockDeviceArgs', 'AmiEphemeralBlockDeviceArgsDict', 'AmiFromInstanceEbsBlockDeviceArgs', 'AmiFromInstanceEbsBlockDeviceArgsDict', 'AmiFromInstanceEphemeralBlockDeviceArgs', 'AmiFromInstanceEphemeralBlockDeviceArgsDict', 'CapacityBlockReservationTimeoutsArgs', 'CapacityBlockReservationTimeoutsArgsDict', 'DefaultCreditSpecificationTimeoutsArgs', 'DefaultCreditSpecificationTimeoutsArgsDict', 'DefaultNetworkAclEgressArgs', 'DefaultNetworkAclEgressArgsDict', 'DefaultNetworkAclIngressArgs', 'DefaultNetworkAclIngressArgsDict', 'DefaultRouteTableRouteArgs', 'DefaultRouteTableRouteArgsDict', 'DefaultSecurityGroupEgressArgs', 'DefaultSecurityGroupEgressArgsDict', 'DefaultSecurityGroupIngressArgs', 'DefaultSecurityGroupIngressArgsDict', 'EipDomainNameTimeoutsArgs', 'EipDomainNameTimeoutsArgsDict', 'EncryptionControlResourceExclusionsArgs', 'EncryptionControlResourceExclusionsArgsDict', ..., ..., ..., ..., ..., ..., 'EncryptionControlResourceExclusionsLambdaArgs', 'EncryptionControlResourceExclusionsLambdaArgsDict', 'EncryptionControlResourceExclusionsNatGatewayArgs', ..., ..., ..., 'EncryptionControlResourceExclusionsVpcLatticeArgs', ..., 'EncryptionControlResourceExclusionsVpcPeeringArgs', ..., 'EncryptionControlTimeoutsArgs', 'EncryptionControlTimeoutsArgsDict', 'FleetFleetInstanceSetArgs', 'FleetFleetInstanceSetArgsDict', 'FleetLaunchTemplateConfigArgs', 'FleetLaunchTemplateConfigArgsDict', ..., ..., 'FleetLaunchTemplateConfigOverrideArgs', 'FleetLaunchTemplateConfigOverrideArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FleetOnDemandOptionsArgs', 'FleetOnDemandOptionsArgsDict', 'FleetOnDemandOptionsCapacityReservationOptionsArgs', ..., 'FleetSpotOptionsArgs', 'FleetSpotOptionsArgsDict', 'FleetSpotOptionsMaintenanceStrategiesArgs', 'FleetSpotOptionsMaintenanceStrategiesArgsDict', ..., ..., 'FleetTargetCapacitySpecificationArgs', 'FleetTargetCapacitySpecificationArgsDict', 'FlowLogDestinationOptionsArgs', 'FlowLogDestinationOptionsArgsDict', 'InstanceCapacityReservationSpecificationArgs', 'InstanceCapacityReservationSpecificationArgsDict', ..., ..., 'InstanceCpuOptionsArgs', 'InstanceCpuOptionsArgsDict', 'InstanceCreditSpecificationArgs', 'InstanceCreditSpecificationArgsDict', 'InstanceEbsBlockDeviceArgs', 'InstanceEbsBlockDeviceArgsDict', 'InstanceEnclaveOptionsArgs', 'InstanceEnclaveOptionsArgsDict', 'InstanceEphemeralBlockDeviceArgs', 'InstanceEphemeralBlockDeviceArgsDict', 'InstanceInstanceMarketOptionsArgs', 'InstanceInstanceMarketOptionsArgsDict', 'InstanceInstanceMarketOptionsSpotOptionsArgs', 'InstanceInstanceMarketOptionsSpotOptionsArgsDict', 'InstanceLaunchTemplateArgs', 'InstanceLaunchTemplateArgsDict', 'InstanceMaintenanceOptionsArgs', 'InstanceMaintenanceOptionsArgsDict', 'InstanceMetadataOptionsArgs', 'InstanceMetadataOptionsArgsDict', 'InstanceNetworkInterfaceArgs', 'InstanceNetworkInterfaceArgsDict', 'InstancePrimaryNetworkInterfaceArgs', 'InstancePrimaryNetworkInterfaceArgsDict', 'InstancePrivateDnsNameOptionsArgs', 'InstancePrivateDnsNameOptionsArgsDict', 'InstanceRootBlockDeviceArgs', 'InstanceRootBlockDeviceArgsDict', 'InstanceSecondaryNetworkInterfaceArgs', 'InstanceSecondaryNetworkInterfaceArgsDict', 'LaunchConfigurationEbsBlockDeviceArgs', 'LaunchConfigurationEbsBlockDeviceArgsDict', 'LaunchConfigurationEphemeralBlockDeviceArgs', 'LaunchConfigurationEphemeralBlockDeviceArgsDict', 'LaunchConfigurationMetadataOptionsArgs', 'LaunchConfigurationMetadataOptionsArgsDict', 'LaunchConfigurationRootBlockDeviceArgs', 'LaunchConfigurationRootBlockDeviceArgsDict', 'LaunchTemplateBlockDeviceMappingArgs', 'LaunchTemplateBlockDeviceMappingArgsDict', 'LaunchTemplateBlockDeviceMappingEbsArgs', 'LaunchTemplateBlockDeviceMappingEbsArgsDict', 'LaunchTemplateCapacityReservationSpecificationArgs', ..., ..., ..., 'LaunchTemplateCpuOptionsArgs', 'LaunchTemplateCpuOptionsArgsDict', 'LaunchTemplateCreditSpecificationArgs', 'LaunchTemplateCreditSpecificationArgsDict', 'LaunchTemplateEnclaveOptionsArgs', 'LaunchTemplateEnclaveOptionsArgsDict', 'LaunchTemplateHibernationOptionsArgs', 'LaunchTemplateHibernationOptionsArgsDict', 'LaunchTemplateIamInstanceProfileArgs', 'LaunchTemplateIamInstanceProfileArgsDict', 'LaunchTemplateInstanceMarketOptionsArgs', 'LaunchTemplateInstanceMarketOptionsArgsDict', 'LaunchTemplateInstanceMarketOptionsSpotOptionsArgs', ..., 'LaunchTemplateInstanceRequirementsArgs', 'LaunchTemplateInstanceRequirementsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'LaunchTemplateInstanceRequirementsMemoryMibArgs', ..., ..., ..., ..., ..., ..., ..., 'LaunchTemplateInstanceRequirementsVcpuCountArgs', ..., 'LaunchTemplateLicenseSpecificationArgs', 'LaunchTemplateLicenseSpecificationArgsDict', 'LaunchTemplateMaintenanceOptionsArgs', 'LaunchTemplateMaintenanceOptionsArgsDict', 'LaunchTemplateMetadataOptionsArgs', 'LaunchTemplateMetadataOptionsArgsDict', 'LaunchTemplateMonitoringArgs', 'LaunchTemplateMonitoringArgsDict', 'LaunchTemplateNetworkInterfaceArgs', 'LaunchTemplateNetworkInterfaceArgsDict', ..., ..., ..., ..., ..., ..., 'LaunchTemplateNetworkPerformanceOptionsArgs', 'LaunchTemplateNetworkPerformanceOptionsArgsDict', 'LaunchTemplatePlacementArgs', 'LaunchTemplatePlacementArgsDict', 'LaunchTemplatePrivateDnsNameOptionsArgs', 'LaunchTemplatePrivateDnsNameOptionsArgsDict', 'LaunchTemplateSecondaryInterfaceArgs', 'LaunchTemplateSecondaryInterfaceArgsDict', 'LaunchTemplateTagSpecificationArgs', 'LaunchTemplateTagSpecificationArgsDict', 'ManagedPrefixListEntryArgs', 'ManagedPrefixListEntryArgsDict', 'NatGatewayAvailabilityZoneAddressArgs', 'NatGatewayAvailabilityZoneAddressArgsDict', 'NatGatewayEipAssociationTimeoutsArgs', 'NatGatewayEipAssociationTimeoutsArgsDict', 'NatGatewayRegionalNatGatewayAddressArgs', 'NatGatewayRegionalNatGatewayAddressArgsDict', 'NetworkAclEgressArgs', 'NetworkAclEgressArgsDict', 'NetworkAclIngressArgs', 'NetworkAclIngressArgsDict', 'NetworkInsightsAnalysisAlternatePathHintArgs', 'NetworkInsightsAnalysisAlternatePathHintArgsDict', 'NetworkInsightsAnalysisExplanationArgs', 'NetworkInsightsAnalysisExplanationArgsDict', 'NetworkInsightsAnalysisExplanationAclArgs', 'NetworkInsightsAnalysisExplanationAclArgsDict', 'NetworkInsightsAnalysisExplanationAclRuleArgs', 'NetworkInsightsAnalysisExplanationAclRuleArgsDict', ..., ..., 'NetworkInsightsAnalysisExplanationAttachedToArgs', ..., ..., ..., 'NetworkInsightsAnalysisExplanationComponentArgs', ..., ..., ..., 'NetworkInsightsAnalysisExplanationDestinationArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'NetworkInsightsAnalysisExplanationNatGatewayArgs', ..., ..., ..., 'NetworkInsightsAnalysisExplanationPortRangeArgs', ..., 'NetworkInsightsAnalysisExplanationPrefixListArgs', ..., 'NetworkInsightsAnalysisExplanationRouteTableArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'NetworkInsightsAnalysisExplanationSourceVpcArgs', ..., 'NetworkInsightsAnalysisExplanationSubnetArgs', 'NetworkInsightsAnalysisExplanationSubnetArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'NetworkInsightsAnalysisExplanationVpcArgs', 'NetworkInsightsAnalysisExplanationVpcArgsDict', 'NetworkInsightsAnalysisExplanationVpcEndpointArgs', ..., ..., ..., ..., ..., 'NetworkInsightsAnalysisExplanationVpnGatewayArgs', ..., 'NetworkInsightsAnalysisForwardPathComponentArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'NetworkInsightsAnalysisForwardPathComponentVpcArgs', ..., 'NetworkInsightsAnalysisReturnPathComponentArgs', 'NetworkInsightsAnalysisReturnPathComponentArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'NetworkInsightsAnalysisReturnPathComponentVpcArgs', ..., 'NetworkInsightsPathFilterAtDestinationArgs', 'NetworkInsightsPathFilterAtDestinationArgsDict', ..., ..., ..., ..., 'NetworkInsightsPathFilterAtSourceArgs', 'NetworkInsightsPathFilterAtSourceArgsDict', ..., ..., ..., ..., 'NetworkInterfaceAttachmentArgs', 'NetworkInterfaceAttachmentArgsDict', 'NetworkInterfacePermissionTimeoutsArgs', 'NetworkInterfacePermissionTimeoutsArgsDict', 'PeeringConnectionOptionsAccepterArgs', 'PeeringConnectionOptionsAccepterArgsDict', 'PeeringConnectionOptionsRequesterArgs', 'PeeringConnectionOptionsRequesterArgsDict', 'RouteTableRouteArgs', 'RouteTableRouteArgsDict', 'SecondaryNetworkIpv4CidrBlockAssociationArgs', 'SecondaryNetworkIpv4CidrBlockAssociationArgsDict', 'SecondaryNetworkTimeoutsArgs', 'SecondaryNetworkTimeoutsArgsDict', 'SecondarySubnetIpv4CidrBlockAssociationArgs', 'SecondarySubnetIpv4CidrBlockAssociationArgsDict', 'SecondarySubnetTimeoutsArgs', 'SecondarySubnetTimeoutsArgsDict', 'SecurityGroupEgressArgs', 'SecurityGroupEgressArgsDict', 'SecurityGroupIngressArgs', 'SecurityGroupIngressArgsDict', 'SpotFleetRequestLaunchSpecificationArgs', 'SpotFleetRequestLaunchSpecificationArgsDict', ..., ..., ..., ..., ..., ..., 'SpotFleetRequestLaunchTemplateConfigArgs', 'SpotFleetRequestLaunchTemplateConfigArgsDict', ..., ..., 'SpotFleetRequestLaunchTemplateConfigOverrideArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'SpotFleetRequestSpotMaintenanceStrategiesArgs', 'SpotFleetRequestSpotMaintenanceStrategiesArgsDict', ..., ..., ..., ..., ..., ..., 'SpotInstanceRequestCpuOptionsArgs', 'SpotInstanceRequestCpuOptionsArgsDict', 'SpotInstanceRequestCreditSpecificationArgs', 'SpotInstanceRequestCreditSpecificationArgsDict', 'SpotInstanceRequestEbsBlockDeviceArgs', 'SpotInstanceRequestEbsBlockDeviceArgsDict', 'SpotInstanceRequestEnclaveOptionsArgs', 'SpotInstanceRequestEnclaveOptionsArgsDict', 'SpotInstanceRequestEphemeralBlockDeviceArgs', 'SpotInstanceRequestEphemeralBlockDeviceArgsDict', 'SpotInstanceRequestLaunchTemplateArgs', 'SpotInstanceRequestLaunchTemplateArgsDict', 'SpotInstanceRequestMaintenanceOptionsArgs', 'SpotInstanceRequestMaintenanceOptionsArgsDict', 'SpotInstanceRequestMetadataOptionsArgs', 'SpotInstanceRequestMetadataOptionsArgsDict', 'SpotInstanceRequestNetworkInterfaceArgs', 'SpotInstanceRequestNetworkInterfaceArgsDict', 'SpotInstanceRequestPrimaryNetworkInterfaceArgs', 'SpotInstanceRequestPrimaryNetworkInterfaceArgsDict', 'SpotInstanceRequestPrivateDnsNameOptionsArgs', 'SpotInstanceRequestPrivateDnsNameOptionsArgsDict', 'SpotInstanceRequestRootBlockDeviceArgs', 'SpotInstanceRequestRootBlockDeviceArgsDict', 'SpotInstanceRequestSecondaryNetworkInterfaceArgs', ..., 'TrafficMirrorFilterRuleDestinationPortRangeArgs', ..., 'TrafficMirrorFilterRuleSourcePortRangeArgs', 'TrafficMirrorFilterRuleSourcePortRangeArgsDict', 'VpcBlockPublicAccessExclusionTimeoutsArgs', 'VpcBlockPublicAccessExclusionTimeoutsArgsDict', 'VpcBlockPublicAccessOptionsTimeoutsArgs', 'VpcBlockPublicAccessOptionsTimeoutsArgsDict', 'VpcEncryptionControlResourceExclusionsArgs', 'VpcEncryptionControlResourceExclusionsArgsDict', ..., ..., ..., ..., ..., ..., 'VpcEncryptionControlResourceExclusionsLambdaArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'VpcEncryptionControlTimeoutsArgs', 'VpcEncryptionControlTimeoutsArgsDict', 'VpcEndpointDnsEntryArgs', 'VpcEndpointDnsEntryArgsDict', 'VpcEndpointDnsOptionsArgs', 'VpcEndpointDnsOptionsArgsDict', 'VpcEndpointServicePrivateDnsNameConfigurationArgs', ..., 'VpcEndpointSubnetConfigurationArgs', 'VpcEndpointSubnetConfigurationArgsDict', 'VpcIpamOperatingRegionArgs', 'VpcIpamOperatingRegionArgsDict', 'VpcIpamPoolCidrCidrAuthorizationContextArgs', 'VpcIpamPoolCidrCidrAuthorizationContextArgsDict', 'VpcIpamPoolSourceResourceArgs', 'VpcIpamPoolSourceResourceArgsDict', 'VpcIpamResourceDiscoveryOperatingRegionArgs', 'VpcIpamResourceDiscoveryOperatingRegionArgsDict', ..., ..., 'VpcPeeringConnectionAccepterArgs', 'VpcPeeringConnectionAccepterArgsDict', 'VpcPeeringConnectionAccepterAccepterArgs', 'VpcPeeringConnectionAccepterAccepterArgsDict', 'VpcPeeringConnectionAccepterRequesterArgs', 'VpcPeeringConnectionAccepterRequesterArgsDict', 'VpcPeeringConnectionRequesterArgs', 'VpcPeeringConnectionRequesterArgsDict', 'VpnConnectionRouteArgs', 'VpnConnectionRouteArgsDict', 'VpnConnectionTunnel1LogOptionsArgs', 'VpnConnectionTunnel1LogOptionsArgsDict', ..., ..., 'VpnConnectionTunnel2LogOptionsArgs', 'VpnConnectionTunnel2LogOptionsArgsDict', ..., ..., 'VpnConnectionVgwTelemetryArgs', 'VpnConnectionVgwTelemetryArgsDict', 'GetAmiFilterArgs', 'GetAmiFilterArgsDict', 'GetAmiIdsFilterArgs', 'GetAmiIdsFilterArgsDict', 'GetCoipPoolFilterArgs', 'GetCoipPoolFilterArgsDict', 'GetCoipPoolsFilterArgs', 'GetCoipPoolsFilterArgsDict', 'GetCustomerGatewayFilterArgs', 'GetCustomerGatewayFilterArgsDict', 'GetDedicatedHostFilterArgs', 'GetDedicatedHostFilterArgsDict', 'GetEipsFilterArgs', 'GetEipsFilterArgsDict', 'GetElasticIpFilterArgs', 'GetElasticIpFilterArgsDict', 'GetInstanceFilterArgs', 'GetInstanceFilterArgsDict', 'GetInstanceTypeOfferingFilterArgs', 'GetInstanceTypeOfferingFilterArgsDict', 'GetInstanceTypeOfferingsFilterArgs', 'GetInstanceTypeOfferingsFilterArgsDict', 'GetInstanceTypesFilterArgs', 'GetInstanceTypesFilterArgsDict', 'GetInstancesFilterArgs', 'GetInstancesFilterArgsDict', 'GetInternetGatewayFilterArgs', 'GetInternetGatewayFilterArgsDict', 'GetKeyPairFilterArgs', 'GetKeyPairFilterArgsDict', 'GetLaunchTemplateFilterArgs', 'GetLaunchTemplateFilterArgsDict', 'GetLocalGatewayFilterArgs', 'GetLocalGatewayFilterArgsDict', 'GetLocalGatewayRouteTableFilterArgs', 'GetLocalGatewayRouteTableFilterArgsDict', 'GetLocalGatewayRouteTablesFilterArgs', 'GetLocalGatewayRouteTablesFilterArgsDict', 'GetLocalGatewayVirtualInterfaceFilterArgs', 'GetLocalGatewayVirtualInterfaceFilterArgsDict', 'GetLocalGatewayVirtualInterfaceGroupFilterArgs', 'GetLocalGatewayVirtualInterfaceGroupFilterArgsDict', 'GetLocalGatewayVirtualInterfaceGroupsFilterArgs', ..., 'GetLocalGatewaysFilterArgs', 'GetLocalGatewaysFilterArgsDict', 'GetManagedPrefixListFilterArgs', 'GetManagedPrefixListFilterArgsDict', 'GetManagedPrefixListsFilterArgs', 'GetManagedPrefixListsFilterArgsDict', 'GetNatGatewayFilterArgs', 'GetNatGatewayFilterArgsDict', 'GetNatGatewaysFilterArgs', 'GetNatGatewaysFilterArgsDict', 'GetNetworkAclsFilterArgs', 'GetNetworkAclsFilterArgsDict', 'GetNetworkInsightsAnalysisFilterArgs', 'GetNetworkInsightsAnalysisFilterArgsDict', 'GetNetworkInsightsPathFilterArgs', 'GetNetworkInsightsPathFilterArgsDict', 'GetNetworkInterfaceFilterArgs', 'GetNetworkInterfaceFilterArgsDict', 'GetNetworkInterfacesFilterArgs', 'GetNetworkInterfacesFilterArgsDict', 'GetPrefixListFilterArgs', 'GetPrefixListFilterArgsDict', 'GetPublicIpv4PoolsFilterArgs', 'GetPublicIpv4PoolsFilterArgsDict', 'GetRouteTableFilterArgs', 'GetRouteTableFilterArgsDict', 'GetRouteTablesFilterArgs', 'GetRouteTablesFilterArgsDict', 'GetSecurityGroupFilterArgs', 'GetSecurityGroupFilterArgsDict', 'GetSecurityGroupsFilterArgs', 'GetSecurityGroupsFilterArgsDict', 'GetSpotPriceFilterArgs', 'GetSpotPriceFilterArgsDict', 'GetSubnetFilterArgs', 'GetSubnetFilterArgsDict', 'GetSubnetsFilterArgs', 'GetSubnetsFilterArgsDict', 'GetTransitGatewayRouteTablesFilterArgs', 'GetTransitGatewayRouteTablesFilterArgsDict', 'GetVpcDhcpOptionsFilterArgs', 'GetVpcDhcpOptionsFilterArgsDict', 'GetVpcEndpointFilterArgs', 'GetVpcEndpointFilterArgsDict', 'GetVpcEndpointServiceFilterArgs', 'GetVpcEndpointServiceFilterArgsDict', 'GetVpcFilterArgs', 'GetVpcFilterArgsDict', 'GetVpcIpamPoolCidrsFilterArgs', 'GetVpcIpamPoolCidrsFilterArgsDict', 'GetVpcIpamPoolFilterArgs', 'GetVpcIpamPoolFilterArgsDict', 'GetVpcIpamPoolsFilterArgs', 'GetVpcIpamPoolsFilterArgsDict', 'GetVpcIpamsFilterArgs', 'GetVpcIpamsFilterArgsDict', 'GetVpcPeeringConnectionFilterArgs', 'GetVpcPeeringConnectionFilterArgsDict', 'GetVpcPeeringConnectionsFilterArgs', 'GetVpcPeeringConnectionsFilterArgsDict', 'GetVpcsFilterArgs', 'GetVpcsFilterArgsDict', 'GetVpnConnectionFilterArgs', 'GetVpnConnectionFilterArgsDict', 'GetVpnGatewayFilterArgs', 'GetVpnGatewayFilterArgsDict']
class AllowedImagesSettingsImageCriterionArgsDict(TypedDict):
    creation_date_condition: NotRequired[pulumi.Input[AllowedImagesSettingsImageCriterionCreationDateConditionArgsDict]]
    deprecation_time_condition: NotRequired[pulumi.Input[AllowedImagesSettingsImageCriterionDeprecationTimeConditionArgsDict]]
    image_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    image_providers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    marketplace_product_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AllowedImagesSettingsImageCriterionArgs:
    def __init__(__self__, *, creation_date_condition: Optional[pulumi.Input[AllowedImagesSettingsImageCriterionCreationDateConditionArgs]] = ..., deprecation_time_condition: Optional[pulumi.Input[AllowedImagesSettingsImageCriterionDeprecationTimeConditionArgs]] = ..., image_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., image_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., marketplace_product_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDateCondition")
    def creation_date_condition(self) -> Optional[pulumi.Input[AllowedImagesSettingsImageCriterionCreationDateConditionArgs]]:
        
        ...
    
    @creation_date_condition.setter
    def creation_date_condition(self, value: Optional[pulumi.Input[AllowedImagesSettingsImageCriterionCreationDateConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deprecationTimeCondition")
    def deprecation_time_condition(self) -> Optional[pulumi.Input[AllowedImagesSettingsImageCriterionDeprecationTimeConditionArgs]]:
        
        ...
    
    @deprecation_time_condition.setter
    def deprecation_time_condition(self, value: Optional[pulumi.Input[AllowedImagesSettingsImageCriterionDeprecationTimeConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageNames")
    def image_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @image_names.setter
    def image_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageProviders")
    def image_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @image_providers.setter
    def image_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceProductCodes")
    def marketplace_product_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @marketplace_product_codes.setter
    def marketplace_product_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AllowedImagesSettingsImageCriterionCreationDateConditionArgsDict(TypedDict):
    maximum_days_since_created: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AllowedImagesSettingsImageCriterionCreationDateConditionArgs:
    def __init__(__self__, *, maximum_days_since_created: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumDaysSinceCreated")
    def maximum_days_since_created(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_days_since_created.setter
    def maximum_days_since_created(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class AllowedImagesSettingsImageCriterionDeprecationTimeConditionArgsDict(TypedDict):
    maximum_days_since_deprecated: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AllowedImagesSettingsImageCriterionDeprecationTimeConditionArgs:
    def __init__(__self__, *, maximum_days_since_deprecated: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumDaysSinceDeprecated")
    def maximum_days_since_deprecated(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_days_since_deprecated.setter
    def maximum_days_since_deprecated(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class AmiCopyEbsBlockDeviceArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    outpost_arn: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AmiCopyEbsBlockDeviceArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AmiCopyEphemeralBlockDeviceArgsDict(TypedDict):
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    virtual_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AmiCopyEphemeralBlockDeviceArgs:
    def __init__(__self__, *, device_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_name.setter
    def virtual_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AmiEbsBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    outpost_arn: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AmiEbsBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AmiEphemeralBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    virtual_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class AmiEphemeralBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], virtual_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @virtual_name.setter
    def virtual_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AmiFromInstanceEbsBlockDeviceArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    outpost_arn: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AmiFromInstanceEbsBlockDeviceArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AmiFromInstanceEphemeralBlockDeviceArgsDict(TypedDict):
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    virtual_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AmiFromInstanceEphemeralBlockDeviceArgs:
    def __init__(__self__, *, device_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_name.setter
    def virtual_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CapacityBlockReservationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CapacityBlockReservationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DefaultCreditSpecificationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DefaultCreditSpecificationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DefaultNetworkAclEgressArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    rule_no: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    icmp_code: NotRequired[pulumi.Input[_builtins.int]]
    icmp_type: NotRequired[pulumi.Input[_builtins.int]]
    ipv6_cidr_block: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DefaultNetworkAclEgressArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], rule_no: pulumi.Input[_builtins.int], to_port: pulumi.Input[_builtins.int], cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., icmp_code: Optional[pulumi.Input[_builtins.int]] = ..., icmp_type: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNo")
    def rule_no(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @rule_no.setter
    def rule_no(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_code.setter
    def icmp_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_type.setter
    def icmp_type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DefaultNetworkAclIngressArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    rule_no: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    icmp_code: NotRequired[pulumi.Input[_builtins.int]]
    icmp_type: NotRequired[pulumi.Input[_builtins.int]]
    ipv6_cidr_block: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DefaultNetworkAclIngressArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], rule_no: pulumi.Input[_builtins.int], to_port: pulumi.Input[_builtins.int], cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., icmp_code: Optional[pulumi.Input[_builtins.int]] = ..., icmp_type: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNo")
    def rule_no(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @rule_no.setter
    def rule_no(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_code.setter
    def icmp_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_type.setter
    def icmp_type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DefaultRouteTableRouteArgsDict(TypedDict):
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    core_network_arn: NotRequired[pulumi.Input[_builtins.str]]
    destination_prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    egress_only_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    instance_id: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    nat_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    transit_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_peering_connection_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DefaultRouteTableRouteArgs:
    def __init__(__self__, *, cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., core_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_only_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_arn.setter
    def core_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_prefix_list_id.setter
    def destination_prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @egress_only_gateway_id.setter
    def egress_only_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DefaultSecurityGroupEgressArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    to_port: pulumi.Input[_builtins.int]
    cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix_list_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    self: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DefaultSecurityGroupEgressArgs:
    def __init__(__self__, *, from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], to_port: pulumi.Input[_builtins.int], cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., prefix_list_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., self: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cidr_blocks.setter
    def cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @prefix_list_ids.setter
    def prefix_list_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @self.setter
    def self(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DefaultSecurityGroupIngressArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    to_port: pulumi.Input[_builtins.int]
    cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix_list_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    self: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DefaultSecurityGroupIngressArgs:
    def __init__(__self__, *, from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], to_port: pulumi.Input[_builtins.int], cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., prefix_list_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., self: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cidr_blocks.setter
    def cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @prefix_list_ids.setter
    def prefix_list_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @self.setter
    def self(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class EipDomainNameTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EipDomainNameTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsArgsDict(TypedDict):
    egress_only_internet_gateway: pulumi.Input[EncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgsDict]
    elastic_file_system: pulumi.Input[EncryptionControlResourceExclusionsElasticFileSystemArgsDict]
    internet_gateway: pulumi.Input[EncryptionControlResourceExclusionsInternetGatewayArgsDict]
    lambda_: pulumi.Input[EncryptionControlResourceExclusionsLambdaArgsDict]
    nat_gateway: pulumi.Input[EncryptionControlResourceExclusionsNatGatewayArgsDict]
    virtual_private_gateway: pulumi.Input[EncryptionControlResourceExclusionsVirtualPrivateGatewayArgsDict]
    vpc_lattice: pulumi.Input[EncryptionControlResourceExclusionsVpcLatticeArgsDict]
    vpc_peering: pulumi.Input[EncryptionControlResourceExclusionsVpcPeeringArgsDict]


@pulumi.input_type
class EncryptionControlResourceExclusionsArgs:
    def __init__(__self__, *, egress_only_internet_gateway: pulumi.Input[EncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgs], elastic_file_system: pulumi.Input[EncryptionControlResourceExclusionsElasticFileSystemArgs], internet_gateway: pulumi.Input[EncryptionControlResourceExclusionsInternetGatewayArgs], lambda_: pulumi.Input[EncryptionControlResourceExclusionsLambdaArgs], nat_gateway: pulumi.Input[EncryptionControlResourceExclusionsNatGatewayArgs], virtual_private_gateway: pulumi.Input[EncryptionControlResourceExclusionsVirtualPrivateGatewayArgs], vpc_lattice: pulumi.Input[EncryptionControlResourceExclusionsVpcLatticeArgs], vpc_peering: pulumi.Input[EncryptionControlResourceExclusionsVpcPeeringArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGateway")
    def egress_only_internet_gateway(self) -> pulumi.Input[EncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgs]:
        
        ...
    
    @egress_only_internet_gateway.setter
    def egress_only_internet_gateway(self, value: pulumi.Input[EncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticFileSystem")
    def elastic_file_system(self) -> pulumi.Input[EncryptionControlResourceExclusionsElasticFileSystemArgs]:
        
        ...
    
    @elastic_file_system.setter
    def elastic_file_system(self, value: pulumi.Input[EncryptionControlResourceExclusionsElasticFileSystemArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateway")
    def internet_gateway(self) -> pulumi.Input[EncryptionControlResourceExclusionsInternetGatewayArgs]:
        
        ...
    
    @internet_gateway.setter
    def internet_gateway(self, value: pulumi.Input[EncryptionControlResourceExclusionsInternetGatewayArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> pulumi.Input[EncryptionControlResourceExclusionsLambdaArgs]:
        
        ...
    
    @lambda_.setter
    def lambda_(self, value: pulumi.Input[EncryptionControlResourceExclusionsLambdaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> pulumi.Input[EncryptionControlResourceExclusionsNatGatewayArgs]:
        
        ...
    
    @nat_gateway.setter
    def nat_gateway(self, value: pulumi.Input[EncryptionControlResourceExclusionsNatGatewayArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualPrivateGateway")
    def virtual_private_gateway(self) -> pulumi.Input[EncryptionControlResourceExclusionsVirtualPrivateGatewayArgs]:
        
        ...
    
    @virtual_private_gateway.setter
    def virtual_private_gateway(self, value: pulumi.Input[EncryptionControlResourceExclusionsVirtualPrivateGatewayArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLattice")
    def vpc_lattice(self) -> pulumi.Input[EncryptionControlResourceExclusionsVpcLatticeArgs]:
        
        ...
    
    @vpc_lattice.setter
    def vpc_lattice(self, value: pulumi.Input[EncryptionControlResourceExclusionsVpcLatticeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeering")
    def vpc_peering(self) -> pulumi.Input[EncryptionControlResourceExclusionsVpcPeeringArgs]:
        
        ...
    
    @vpc_peering.setter
    def vpc_peering(self, value: pulumi.Input[EncryptionControlResourceExclusionsVpcPeeringArgs]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsElasticFileSystemArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionControlResourceExclusionsElasticFileSystemArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsInternetGatewayArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionControlResourceExclusionsInternetGatewayArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsLambdaArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionControlResourceExclusionsLambdaArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsNatGatewayArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionControlResourceExclusionsNatGatewayArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsVirtualPrivateGatewayArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionControlResourceExclusionsVirtualPrivateGatewayArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsVpcLatticeArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionControlResourceExclusionsVpcLatticeArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionControlResourceExclusionsVpcPeeringArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionControlResourceExclusionsVpcPeeringArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionControlTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EncryptionControlTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetFleetInstanceSetArgsDict(TypedDict):
    instance_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle: NotRequired[pulumi.Input[_builtins.str]]
    platform: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FleetFleetInstanceSetArgs:
    def __init__(__self__, *, instance_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_ids.setter
    def instance_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle.setter
    def lifecycle(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigArgsDict(TypedDict):
    launch_template_specification: NotRequired[pulumi.Input[FleetLaunchTemplateConfigLaunchTemplateSpecificationArgsDict]]
    overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigOverrideArgsDict]]]]


@pulumi.input_type
class FleetLaunchTemplateConfigArgs:
    def __init__(__self__, *, launch_template_specification: Optional[pulumi.Input[FleetLaunchTemplateConfigLaunchTemplateSpecificationArgs]] = ..., overrides: Optional[pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigOverrideArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecification")
    def launch_template_specification(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigLaunchTemplateSpecificationArgs]]:
        
        ...
    
    @launch_template_specification.setter
    def launch_template_specification(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigLaunchTemplateSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigOverrideArgs]]]]:
        
        ...
    
    @overrides.setter
    def overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigOverrideArgs]]]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigLaunchTemplateSpecificationArgsDict(TypedDict):
    version: pulumi.Input[_builtins.str]
    launch_template_id: NotRequired[pulumi.Input[_builtins.str]]
    launch_template_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FleetLaunchTemplateConfigLaunchTemplateSpecificationArgs:
    def __init__(__self__, *, version: pulumi.Input[_builtins.str], launch_template_id: Optional[pulumi.Input[_builtins.str]] = ..., launch_template_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_template_id.setter
    def launch_template_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_template_name.setter
    def launch_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideArgsDict(TypedDict):
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    instance_requirements: NotRequired[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsArgsDict]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    max_price: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.float]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    weighted_capacity: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideArgs:
    def __init__(__self__, *, availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., instance_requirements: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsArgs]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., max_price: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.float]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., weighted_capacity: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsArgs]]:
        
        ...
    
    @instance_requirements.setter
    def instance_requirements(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrice")
    def max_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_price.setter
    def max_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @weighted_capacity.setter
    def weighted_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsArgsDict(TypedDict):
    memory_mib: pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgsDict]
    vcpu_count: pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgsDict]
    accelerator_count: NotRequired[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgsDict]]
    accelerator_manufacturers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accelerator_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accelerator_total_memory_mib: NotRequired[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgsDict]]
    accelerator_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bare_metal: NotRequired[pulumi.Input[_builtins.str]]
    baseline_ebs_bandwidth_mbps: NotRequired[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict]]
    burstable_performance: NotRequired[pulumi.Input[_builtins.str]]
    cpu_manufacturers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    instance_generations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    local_storage: NotRequired[pulumi.Input[_builtins.str]]
    local_storage_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_spot_price_as_percentage_of_optimal_on_demand_price: NotRequired[pulumi.Input[_builtins.int]]
    memory_gib_per_vcpu: NotRequired[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgsDict]]
    network_bandwidth_gbps: NotRequired[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgsDict]]
    network_interface_count: NotRequired[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgsDict]]
    on_demand_max_price_percentage_over_lowest_price: NotRequired[pulumi.Input[_builtins.int]]
    require_hibernate_support: NotRequired[pulumi.Input[_builtins.bool]]
    spot_max_price_percentage_over_lowest_price: NotRequired[pulumi.Input[_builtins.int]]
    total_local_storage_gb: NotRequired[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgsDict]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsArgs:
    def __init__(__self__, *, memory_mib: pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgs], vcpu_count: pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgs], accelerator_count: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgs]] = ..., accelerator_manufacturers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accelerator_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accelerator_total_memory_mib: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs]] = ..., accelerator_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bare_metal: Optional[pulumi.Input[_builtins.str]] = ..., baseline_ebs_bandwidth_mbps: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs]] = ..., burstable_performance: Optional[pulumi.Input[_builtins.str]] = ..., cpu_manufacturers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., excluded_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_generations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., local_storage: Optional[pulumi.Input[_builtins.str]] = ..., local_storage_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[pulumi.Input[_builtins.int]] = ..., memory_gib_per_vcpu: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgs]] = ..., network_bandwidth_gbps: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgs]] = ..., network_interface_count: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgs]] = ..., on_demand_max_price_percentage_over_lowest_price: Optional[pulumi.Input[_builtins.int]] = ..., require_hibernate_support: Optional[pulumi.Input[_builtins.bool]] = ..., spot_max_price_percentage_over_lowest_price: Optional[pulumi.Input[_builtins.int]] = ..., total_local_storage_gb: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(self) -> pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgs]:
        
        ...
    
    @memory_mib.setter
    def memory_mib(self, value: pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgs]:
        
        ...
    
    @vcpu_count.setter
    def vcpu_count(self, value: pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgs]]:
        
        ...
    
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_manufacturers.setter
    def accelerator_manufacturers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_names.setter
    def accelerator_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs]]:
        
        ...
    
    @accelerator_total_memory_mib.setter
    def accelerator_total_memory_mib(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_types.setter
    def accelerator_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_instance_types.setter
    def allowed_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bare_metal.setter
    def bare_metal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs]]:
        
        ...
    
    @baseline_ebs_bandwidth_mbps.setter
    def baseline_ebs_bandwidth_mbps(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @burstable_performance.setter
    def burstable_performance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cpu_manufacturers.setter
    def cpu_manufacturers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_instance_types.setter
    def excluded_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_generations.setter
    def instance_generations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @local_storage.setter
    def local_storage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @local_storage_types.setter
    def local_storage_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSpotPriceAsPercentageOfOptimalOnDemandPrice")
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_spot_price_as_percentage_of_optimal_on_demand_price.setter
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgs]]:
        
        ...
    
    @memory_gib_per_vcpu.setter
    def memory_gib_per_vcpu(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgs]]:
        
        ...
    
    @network_bandwidth_gbps.setter
    def network_bandwidth_gbps(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgs]]:
        
        ...
    
    @network_interface_count.setter
    def network_interface_count(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @on_demand_max_price_percentage_over_lowest_price.setter
    def on_demand_max_price_percentage_over_lowest_price(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_hibernate_support.setter
    def require_hibernate_support(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @spot_max_price_percentage_over_lowest_price.setter
    def spot_max_price_percentage_over_lowest_price(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGb")
    def total_local_storage_gb(self) -> Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgs]]:
        
        ...
    
    @total_local_storage_gb.setter
    def total_local_storage_gb(self, value: Optional[pulumi.Input[FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgs]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgsDict(TypedDict):
    min: pulumi.Input[_builtins.int]
    max: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgs:
    def __init__(__self__, *, min: pulumi.Input[_builtins.int], max: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min.setter
    def min(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgsDict(TypedDict):
    min: pulumi.Input[_builtins.int]
    max: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FleetLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgs:
    def __init__(__self__, *, min: pulumi.Input[_builtins.int], max: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min.setter
    def min(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FleetOnDemandOptionsArgsDict(TypedDict):
    allocation_strategy: NotRequired[pulumi.Input[_builtins.str]]
    capacity_reservation_options: NotRequired[pulumi.Input[FleetOnDemandOptionsCapacityReservationOptionsArgsDict]]
    max_total_price: NotRequired[pulumi.Input[_builtins.str]]
    min_target_capacity: NotRequired[pulumi.Input[_builtins.int]]
    single_availability_zone: NotRequired[pulumi.Input[_builtins.bool]]
    single_instance_type: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FleetOnDemandOptionsArgs:
    def __init__(__self__, *, allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_options: Optional[pulumi.Input[FleetOnDemandOptionsCapacityReservationOptionsArgs]] = ..., max_total_price: Optional[pulumi.Input[_builtins.str]] = ..., min_target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., single_availability_zone: Optional[pulumi.Input[_builtins.bool]] = ..., single_instance_type: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_strategy.setter
    def allocation_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationOptions")
    def capacity_reservation_options(self) -> Optional[pulumi.Input[FleetOnDemandOptionsCapacityReservationOptionsArgs]]:
        
        ...
    
    @capacity_reservation_options.setter
    def capacity_reservation_options(self, value: Optional[pulumi.Input[FleetOnDemandOptionsCapacityReservationOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTotalPrice")
    def max_total_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_total_price.setter
    def max_total_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTargetCapacity")
    def min_target_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_target_capacity.setter
    def min_target_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleAvailabilityZone")
    def single_availability_zone(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @single_availability_zone.setter
    def single_availability_zone(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleInstanceType")
    def single_instance_type(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @single_instance_type.setter
    def single_instance_type(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FleetOnDemandOptionsCapacityReservationOptionsArgsDict(TypedDict):
    usage_strategy: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FleetOnDemandOptionsCapacityReservationOptionsArgs:
    def __init__(__self__, *, usage_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageStrategy")
    def usage_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @usage_strategy.setter
    def usage_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetSpotOptionsArgsDict(TypedDict):
    allocation_strategy: NotRequired[pulumi.Input[_builtins.str]]
    instance_interruption_behavior: NotRequired[pulumi.Input[_builtins.str]]
    instance_pools_to_use_count: NotRequired[pulumi.Input[_builtins.int]]
    maintenance_strategies: NotRequired[pulumi.Input[FleetSpotOptionsMaintenanceStrategiesArgsDict]]
    max_total_price: NotRequired[pulumi.Input[_builtins.str]]
    min_target_capacity: NotRequired[pulumi.Input[_builtins.int]]
    single_availability_zone: NotRequired[pulumi.Input[_builtins.bool]]
    single_instance_type: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FleetSpotOptionsArgs:
    def __init__(__self__, *, allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., instance_interruption_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_pools_to_use_count: Optional[pulumi.Input[_builtins.int]] = ..., maintenance_strategies: Optional[pulumi.Input[FleetSpotOptionsMaintenanceStrategiesArgs]] = ..., max_total_price: Optional[pulumi.Input[_builtins.str]] = ..., min_target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., single_availability_zone: Optional[pulumi.Input[_builtins.bool]] = ..., single_instance_type: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_strategy.setter
    def allocation_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_interruption_behavior.setter
    def instance_interruption_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_pools_to_use_count.setter
    def instance_pools_to_use_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceStrategies")
    def maintenance_strategies(self) -> Optional[pulumi.Input[FleetSpotOptionsMaintenanceStrategiesArgs]]:
        
        ...
    
    @maintenance_strategies.setter
    def maintenance_strategies(self, value: Optional[pulumi.Input[FleetSpotOptionsMaintenanceStrategiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTotalPrice")
    def max_total_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_total_price.setter
    def max_total_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTargetCapacity")
    def min_target_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_target_capacity.setter
    def min_target_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleAvailabilityZone")
    def single_availability_zone(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @single_availability_zone.setter
    def single_availability_zone(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleInstanceType")
    def single_instance_type(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @single_instance_type.setter
    def single_instance_type(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FleetSpotOptionsMaintenanceStrategiesArgsDict(TypedDict):
    capacity_rebalance: NotRequired[pulumi.Input[FleetSpotOptionsMaintenanceStrategiesCapacityRebalanceArgsDict]]


@pulumi.input_type
class FleetSpotOptionsMaintenanceStrategiesArgs:
    def __init__(__self__, *, capacity_rebalance: Optional[pulumi.Input[FleetSpotOptionsMaintenanceStrategiesCapacityRebalanceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityRebalance")
    def capacity_rebalance(self) -> Optional[pulumi.Input[FleetSpotOptionsMaintenanceStrategiesCapacityRebalanceArgs]]:
        
        ...
    
    @capacity_rebalance.setter
    def capacity_rebalance(self, value: Optional[pulumi.Input[FleetSpotOptionsMaintenanceStrategiesCapacityRebalanceArgs]]): # -> None:
        ...
    


class FleetSpotOptionsMaintenanceStrategiesCapacityRebalanceArgsDict(TypedDict):
    replacement_strategy: NotRequired[pulumi.Input[_builtins.str]]
    termination_delay: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FleetSpotOptionsMaintenanceStrategiesCapacityRebalanceArgs:
    def __init__(__self__, *, replacement_strategy: Optional[pulumi.Input[_builtins.str]] = ..., termination_delay: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementStrategy")
    def replacement_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replacement_strategy.setter
    def replacement_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationDelay")
    def termination_delay(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @termination_delay.setter
    def termination_delay(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FleetTargetCapacitySpecificationArgsDict(TypedDict):
    default_target_capacity_type: pulumi.Input[_builtins.str]
    total_target_capacity: pulumi.Input[_builtins.int]
    on_demand_target_capacity: NotRequired[pulumi.Input[_builtins.int]]
    spot_target_capacity: NotRequired[pulumi.Input[_builtins.int]]
    target_capacity_unit_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FleetTargetCapacitySpecificationArgs:
    def __init__(__self__, *, default_target_capacity_type: pulumi.Input[_builtins.str], total_target_capacity: pulumi.Input[_builtins.int], on_demand_target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., spot_target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., target_capacity_unit_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTargetCapacityType")
    def default_target_capacity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @default_target_capacity_type.setter
    def default_target_capacity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalTargetCapacity")
    def total_target_capacity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @total_target_capacity.setter
    def total_target_capacity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandTargetCapacity")
    def on_demand_target_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @on_demand_target_capacity.setter
    def on_demand_target_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotTargetCapacity")
    def spot_target_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @spot_target_capacity.setter
    def spot_target_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCapacityUnitType")
    def target_capacity_unit_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_capacity_unit_type.setter
    def target_capacity_unit_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowLogDestinationOptionsArgsDict(TypedDict):
    file_format: NotRequired[pulumi.Input[_builtins.str]]
    hive_compatible_partitions: NotRequired[pulumi.Input[_builtins.bool]]
    per_hour_partition: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowLogDestinationOptionsArgs:
    def __init__(__self__, *, file_format: Optional[pulumi.Input[_builtins.str]] = ..., hive_compatible_partitions: Optional[pulumi.Input[_builtins.bool]] = ..., per_hour_partition: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_format.setter
    def file_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveCompatiblePartitions")
    def hive_compatible_partitions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hive_compatible_partitions.setter
    def hive_compatible_partitions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perHourPartition")
    def per_hour_partition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @per_hour_partition.setter
    def per_hour_partition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class InstanceCapacityReservationSpecificationArgsDict(TypedDict):
    capacity_reservation_preference: NotRequired[pulumi.Input[_builtins.str]]
    capacity_reservation_target: NotRequired[pulumi.Input[InstanceCapacityReservationSpecificationCapacityReservationTargetArgsDict]]


@pulumi.input_type
class InstanceCapacityReservationSpecificationArgs:
    def __init__(__self__, *, capacity_reservation_preference: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_target: Optional[pulumi.Input[InstanceCapacityReservationSpecificationCapacityReservationTargetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_preference.setter
    def capacity_reservation_preference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationTarget")
    def capacity_reservation_target(self) -> Optional[pulumi.Input[InstanceCapacityReservationSpecificationCapacityReservationTargetArgs]]:
        
        ...
    
    @capacity_reservation_target.setter
    def capacity_reservation_target(self, value: Optional[pulumi.Input[InstanceCapacityReservationSpecificationCapacityReservationTargetArgs]]): # -> None:
        ...
    


class InstanceCapacityReservationSpecificationCapacityReservationTargetArgsDict(TypedDict):
    capacity_reservation_id: NotRequired[pulumi.Input[_builtins.str]]
    capacity_reservation_resource_group_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceCapacityReservationSpecificationCapacityReservationTargetArgs:
    def __init__(__self__, *, capacity_reservation_id: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationId")
    def capacity_reservation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_id.setter
    def capacity_reservation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_resource_group_arn.setter
    def capacity_reservation_resource_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceCpuOptionsArgsDict(TypedDict):
    amd_sev_snp: NotRequired[pulumi.Input[_builtins.str]]
    core_count: NotRequired[pulumi.Input[_builtins.int]]
    nested_virtualization: NotRequired[pulumi.Input[_builtins.str]]
    threads_per_core: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class InstanceCpuOptionsArgs:
    def __init__(__self__, *, amd_sev_snp: Optional[pulumi.Input[_builtins.str]] = ..., core_count: Optional[pulumi.Input[_builtins.int]] = ..., nested_virtualization: Optional[pulumi.Input[_builtins.str]] = ..., threads_per_core: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amdSevSnp")
    def amd_sev_snp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amd_sev_snp.setter
    def amd_sev_snp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @core_count.setter
    def core_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestedVirtualization")
    def nested_virtualization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nested_virtualization.setter
    def nested_virtualization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @threads_per_core.setter
    def threads_per_core(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class InstanceCreditSpecificationArgsDict(TypedDict):
    cpu_credits: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceCreditSpecificationArgs:
    def __init__(__self__, *, cpu_credits: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu_credits.setter
    def cpu_credits(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceEbsBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags_all: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_id: NotRequired[pulumi.Input[_builtins.str]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceEbsBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_id: Optional[pulumi.Input[_builtins.str]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceEnclaveOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class InstanceEnclaveOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class InstanceEphemeralBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    no_device: NotRequired[pulumi.Input[_builtins.bool]]
    virtual_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceEphemeralBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], no_device: Optional[pulumi.Input[_builtins.bool]] = ..., virtual_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @no_device.setter
    def no_device(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_name.setter
    def virtual_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceInstanceMarketOptionsArgsDict(TypedDict):
    market_type: NotRequired[pulumi.Input[_builtins.str]]
    spot_options: NotRequired[pulumi.Input[InstanceInstanceMarketOptionsSpotOptionsArgsDict]]


@pulumi.input_type
class InstanceInstanceMarketOptionsArgs:
    def __init__(__self__, *, market_type: Optional[pulumi.Input[_builtins.str]] = ..., spot_options: Optional[pulumi.Input[InstanceInstanceMarketOptionsSpotOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketType")
    def market_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @market_type.setter
    def market_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[pulumi.Input[InstanceInstanceMarketOptionsSpotOptionsArgs]]:
        
        ...
    
    @spot_options.setter
    def spot_options(self, value: Optional[pulumi.Input[InstanceInstanceMarketOptionsSpotOptionsArgs]]): # -> None:
        ...
    


class InstanceInstanceMarketOptionsSpotOptionsArgsDict(TypedDict):
    instance_interruption_behavior: NotRequired[pulumi.Input[_builtins.str]]
    max_price: NotRequired[pulumi.Input[_builtins.str]]
    spot_instance_type: NotRequired[pulumi.Input[_builtins.str]]
    valid_until: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceInstanceMarketOptionsSpotOptionsArgs:
    def __init__(__self__, *, instance_interruption_behavior: Optional[pulumi.Input[_builtins.str]] = ..., max_price: Optional[pulumi.Input[_builtins.str]] = ..., spot_instance_type: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_interruption_behavior.setter
    def instance_interruption_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrice")
    def max_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_price.setter
    def max_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstanceType")
    def spot_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_instance_type.setter
    def spot_instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_until.setter
    def valid_until(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceLaunchTemplateArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceLaunchTemplateArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceMaintenanceOptionsArgsDict(TypedDict):
    auto_recovery: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceMaintenanceOptionsArgs:
    def __init__(__self__, *, auto_recovery: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRecovery")
    def auto_recovery(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_recovery.setter
    def auto_recovery(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceMetadataOptionsArgsDict(TypedDict):
    http_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    http_protocol_ipv6: NotRequired[pulumi.Input[_builtins.str]]
    http_put_response_hop_limit: NotRequired[pulumi.Input[_builtins.int]]
    http_tokens: NotRequired[pulumi.Input[_builtins.str]]
    instance_metadata_tags: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceMetadataOptionsArgs:
    def __init__(__self__, *, http_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., http_protocol_ipv6: Optional[pulumi.Input[_builtins.str]] = ..., http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ..., http_tokens: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_tags: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_endpoint.setter
    def http_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_protocol_ipv6.setter
    def http_protocol_ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_tokens.setter
    def http_tokens(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_metadata_tags.setter
    def instance_metadata_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceNetworkInterfaceArgsDict(TypedDict):
    device_index: pulumi.Input[_builtins.int]
    network_interface_id: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    network_card_index: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class InstanceNetworkInterfaceArgs:
    def __init__(__self__, *, device_index: pulumi.Input[_builtins.int], network_interface_id: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., network_card_index: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @device_index.setter
    def device_index(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @network_card_index.setter
    def network_card_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class InstancePrimaryNetworkInterfaceArgsDict(TypedDict):
    network_interface_id: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class InstancePrimaryNetworkInterfaceArgs:
    def __init__(__self__, *, network_interface_id: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class InstancePrivateDnsNameOptionsArgsDict(TypedDict):
    enable_resource_name_dns_a_record: NotRequired[pulumi.Input[_builtins.bool]]
    enable_resource_name_dns_aaaa_record: NotRequired[pulumi.Input[_builtins.bool]]
    hostname_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstancePrivateDnsNameOptionsArgs:
    def __init__(__self__, *, enable_resource_name_dns_a_record: Optional[pulumi.Input[_builtins.bool]] = ..., enable_resource_name_dns_aaaa_record: Optional[pulumi.Input[_builtins.bool]] = ..., hostname_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_a_record.setter
    def enable_resource_name_dns_a_record(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_aaaa_record.setter
    def enable_resource_name_dns_aaaa_record(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameType")
    def hostname_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hostname_type.setter
    def hostname_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceRootBlockDeviceArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags_all: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_id: NotRequired[pulumi.Input[_builtins.str]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceRootBlockDeviceArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_id: Optional[pulumi.Input[_builtins.str]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceSecondaryNetworkInterfaceArgsDict(TypedDict):
    network_card_index: pulumi.Input[_builtins.int]
    secondary_subnet_id: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    device_index: NotRequired[pulumi.Input[_builtins.int]]
    interface_type: NotRequired[pulumi.Input[_builtins.str]]
    mac_address: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address_count: NotRequired[pulumi.Input[_builtins.int]]
    private_ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secondary_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    secondary_network_id: NotRequired[pulumi.Input[_builtins.str]]
    source_dest_check: NotRequired[pulumi.Input[_builtins.bool]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceSecondaryNetworkInterfaceArgs:
    def __init__(__self__, *, network_card_index: pulumi.Input[_builtins.int], secondary_subnet_id: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., device_index: Optional[pulumi.Input[_builtins.int]] = ..., interface_type: Optional[pulumi.Input[_builtins.str]] = ..., mac_address: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address_count: Optional[pulumi.Input[_builtins.int]] = ..., private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secondary_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., secondary_network_id: Optional[pulumi.Input[_builtins.str]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @network_card_index.setter
    def network_card_index(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondarySubnetId")
    def secondary_subnet_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secondary_subnet_id.setter
    def secondary_subnet_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @device_index.setter
    def device_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface_type.setter
    def interface_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddressCount")
    def private_ip_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @private_ip_address_count.setter
    def private_ip_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_ip_addresses.setter
    def private_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInterfaceId")
    def secondary_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secondary_interface_id.setter
    def secondary_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkId")
    def secondary_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secondary_network_id.setter
    def secondary_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @source_dest_check.setter
    def source_dest_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchConfigurationEbsBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    no_device: NotRequired[pulumi.Input[_builtins.bool]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchConfigurationEbsBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., no_device: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @no_device.setter
    def no_device(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchConfigurationEphemeralBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    no_device: NotRequired[pulumi.Input[_builtins.bool]]
    virtual_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchConfigurationEphemeralBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], no_device: Optional[pulumi.Input[_builtins.bool]] = ..., virtual_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @no_device.setter
    def no_device(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @virtual_name.setter
    def virtual_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchConfigurationMetadataOptionsArgsDict(TypedDict):
    http_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    http_put_response_hop_limit: NotRequired[pulumi.Input[_builtins.int]]
    http_tokens: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchConfigurationMetadataOptionsArgs:
    def __init__(__self__, *, http_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ..., http_tokens: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_endpoint.setter
    def http_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_tokens.setter
    def http_tokens(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchConfigurationRootBlockDeviceArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchConfigurationRootBlockDeviceArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateBlockDeviceMappingArgsDict(TypedDict):
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    ebs: NotRequired[pulumi.Input[LaunchTemplateBlockDeviceMappingEbsArgsDict]]
    no_device: NotRequired[pulumi.Input[_builtins.str]]
    virtual_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateBlockDeviceMappingArgs:
    def __init__(__self__, *, device_name: Optional[pulumi.Input[_builtins.str]] = ..., ebs: Optional[pulumi.Input[LaunchTemplateBlockDeviceMappingEbsArgs]] = ..., no_device: Optional[pulumi.Input[_builtins.str]] = ..., virtual_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ebs(self) -> Optional[pulumi.Input[LaunchTemplateBlockDeviceMappingEbsArgs]]:
        
        ...
    
    @ebs.setter
    def ebs(self, value: Optional[pulumi.Input[LaunchTemplateBlockDeviceMappingEbsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @no_device.setter
    def no_device(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_name.setter
    def virtual_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateBlockDeviceMappingEbsArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.str]]
    encrypted: NotRequired[pulumi.Input[_builtins.str]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_initialization_rate: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateBlockDeviceMappingEbsArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.str]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_initialization_rate: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeInitializationRate")
    def volume_initialization_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_initialization_rate.setter
    def volume_initialization_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateCapacityReservationSpecificationArgsDict(TypedDict):
    capacity_reservation_preference: NotRequired[pulumi.Input[_builtins.str]]
    capacity_reservation_target: NotRequired[pulumi.Input[LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetArgsDict]]


@pulumi.input_type
class LaunchTemplateCapacityReservationSpecificationArgs:
    def __init__(__self__, *, capacity_reservation_preference: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_target: Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_preference.setter
    def capacity_reservation_preference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationTarget")
    def capacity_reservation_target(self) -> Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetArgs]]:
        
        ...
    
    @capacity_reservation_target.setter
    def capacity_reservation_target(self, value: Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetArgs]]): # -> None:
        ...
    


class LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetArgsDict(TypedDict):
    capacity_reservation_id: NotRequired[pulumi.Input[_builtins.str]]
    capacity_reservation_resource_group_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetArgs:
    def __init__(__self__, *, capacity_reservation_id: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationId")
    def capacity_reservation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_id.setter
    def capacity_reservation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_resource_group_arn.setter
    def capacity_reservation_resource_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateCpuOptionsArgsDict(TypedDict):
    amd_sev_snp: NotRequired[pulumi.Input[_builtins.str]]
    core_count: NotRequired[pulumi.Input[_builtins.int]]
    nested_virtualization: NotRequired[pulumi.Input[_builtins.str]]
    threads_per_core: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LaunchTemplateCpuOptionsArgs:
    def __init__(__self__, *, amd_sev_snp: Optional[pulumi.Input[_builtins.str]] = ..., core_count: Optional[pulumi.Input[_builtins.int]] = ..., nested_virtualization: Optional[pulumi.Input[_builtins.str]] = ..., threads_per_core: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amdSevSnp")
    def amd_sev_snp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amd_sev_snp.setter
    def amd_sev_snp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @core_count.setter
    def core_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestedVirtualization")
    def nested_virtualization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nested_virtualization.setter
    def nested_virtualization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @threads_per_core.setter
    def threads_per_core(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LaunchTemplateCreditSpecificationArgsDict(TypedDict):
    cpu_credits: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateCreditSpecificationArgs:
    def __init__(__self__, *, cpu_credits: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu_credits.setter
    def cpu_credits(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateEnclaveOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class LaunchTemplateEnclaveOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class LaunchTemplateHibernationOptionsArgsDict(TypedDict):
    configured: pulumi.Input[_builtins.bool]


@pulumi.input_type
class LaunchTemplateHibernationOptionsArgs:
    def __init__(__self__, *, configured: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configured(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @configured.setter
    def configured(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class LaunchTemplateIamInstanceProfileArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateIamInstanceProfileArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateInstanceMarketOptionsArgsDict(TypedDict):
    market_type: NotRequired[pulumi.Input[_builtins.str]]
    spot_options: NotRequired[pulumi.Input[LaunchTemplateInstanceMarketOptionsSpotOptionsArgsDict]]


@pulumi.input_type
class LaunchTemplateInstanceMarketOptionsArgs:
    def __init__(__self__, *, market_type: Optional[pulumi.Input[_builtins.str]] = ..., spot_options: Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsSpotOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketType")
    def market_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @market_type.setter
    def market_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsSpotOptionsArgs]]:
        
        ...
    
    @spot_options.setter
    def spot_options(self, value: Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsSpotOptionsArgs]]): # -> None:
        ...
    


class LaunchTemplateInstanceMarketOptionsSpotOptionsArgsDict(TypedDict):
    block_duration_minutes: NotRequired[pulumi.Input[_builtins.int]]
    instance_interruption_behavior: NotRequired[pulumi.Input[_builtins.str]]
    max_price: NotRequired[pulumi.Input[_builtins.str]]
    spot_instance_type: NotRequired[pulumi.Input[_builtins.str]]
    valid_until: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateInstanceMarketOptionsSpotOptionsArgs:
    def __init__(__self__, *, block_duration_minutes: Optional[pulumi.Input[_builtins.int]] = ..., instance_interruption_behavior: Optional[pulumi.Input[_builtins.str]] = ..., max_price: Optional[pulumi.Input[_builtins.str]] = ..., spot_instance_type: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @block_duration_minutes.setter
    def block_duration_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehavior")
    def instance_interruption_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_interruption_behavior.setter
    def instance_interruption_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrice")
    def max_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_price.setter
    def max_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstanceType")
    def spot_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_instance_type.setter
    def spot_instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_until.setter
    def valid_until(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsArgsDict(TypedDict):
    memory_mib: pulumi.Input[LaunchTemplateInstanceRequirementsMemoryMibArgsDict]
    vcpu_count: pulumi.Input[LaunchTemplateInstanceRequirementsVcpuCountArgsDict]
    accelerator_count: NotRequired[pulumi.Input[LaunchTemplateInstanceRequirementsAcceleratorCountArgsDict]]
    accelerator_manufacturers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accelerator_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accelerator_total_memory_mib: NotRequired[pulumi.Input[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgsDict]]
    accelerator_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bare_metal: NotRequired[pulumi.Input[_builtins.str]]
    baseline_ebs_bandwidth_mbps: NotRequired[pulumi.Input[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict]]
    burstable_performance: NotRequired[pulumi.Input[_builtins.str]]
    cpu_manufacturers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    instance_generations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    local_storage: NotRequired[pulumi.Input[_builtins.str]]
    local_storage_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_spot_price_as_percentage_of_optimal_on_demand_price: NotRequired[pulumi.Input[_builtins.int]]
    memory_gib_per_vcpu: NotRequired[pulumi.Input[LaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgsDict]]
    network_bandwidth_gbps: NotRequired[pulumi.Input[LaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgsDict]]
    network_interface_count: NotRequired[pulumi.Input[LaunchTemplateInstanceRequirementsNetworkInterfaceCountArgsDict]]
    on_demand_max_price_percentage_over_lowest_price: NotRequired[pulumi.Input[_builtins.int]]
    require_hibernate_support: NotRequired[pulumi.Input[_builtins.bool]]
    spot_max_price_percentage_over_lowest_price: NotRequired[pulumi.Input[_builtins.int]]
    total_local_storage_gb: NotRequired[pulumi.Input[LaunchTemplateInstanceRequirementsTotalLocalStorageGbArgsDict]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsArgs:
    def __init__(__self__, *, memory_mib: pulumi.Input[LaunchTemplateInstanceRequirementsMemoryMibArgs], vcpu_count: pulumi.Input[LaunchTemplateInstanceRequirementsVcpuCountArgs], accelerator_count: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsAcceleratorCountArgs]] = ..., accelerator_manufacturers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accelerator_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accelerator_total_memory_mib: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgs]] = ..., accelerator_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bare_metal: Optional[pulumi.Input[_builtins.str]] = ..., baseline_ebs_bandwidth_mbps: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgs]] = ..., burstable_performance: Optional[pulumi.Input[_builtins.str]] = ..., cpu_manufacturers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., excluded_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_generations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., local_storage: Optional[pulumi.Input[_builtins.str]] = ..., local_storage_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[pulumi.Input[_builtins.int]] = ..., memory_gib_per_vcpu: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgs]] = ..., network_bandwidth_gbps: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgs]] = ..., network_interface_count: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsNetworkInterfaceCountArgs]] = ..., on_demand_max_price_percentage_over_lowest_price: Optional[pulumi.Input[_builtins.int]] = ..., require_hibernate_support: Optional[pulumi.Input[_builtins.bool]] = ..., spot_max_price_percentage_over_lowest_price: Optional[pulumi.Input[_builtins.int]] = ..., total_local_storage_gb: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsTotalLocalStorageGbArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(self) -> pulumi.Input[LaunchTemplateInstanceRequirementsMemoryMibArgs]:
        
        ...
    
    @memory_mib.setter
    def memory_mib(self, value: pulumi.Input[LaunchTemplateInstanceRequirementsMemoryMibArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> pulumi.Input[LaunchTemplateInstanceRequirementsVcpuCountArgs]:
        
        ...
    
    @vcpu_count.setter
    def vcpu_count(self, value: pulumi.Input[LaunchTemplateInstanceRequirementsVcpuCountArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsAcceleratorCountArgs]]:
        
        ...
    
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsAcceleratorCountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_manufacturers.setter
    def accelerator_manufacturers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_names.setter
    def accelerator_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgs]]:
        
        ...
    
    @accelerator_total_memory_mib.setter
    def accelerator_total_memory_mib(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_types.setter
    def accelerator_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_instance_types.setter
    def allowed_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bare_metal.setter
    def bare_metal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgs]]:
        
        ...
    
    @baseline_ebs_bandwidth_mbps.setter
    def baseline_ebs_bandwidth_mbps(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @burstable_performance.setter
    def burstable_performance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cpu_manufacturers.setter
    def cpu_manufacturers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_instance_types.setter
    def excluded_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_generations.setter
    def instance_generations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @local_storage.setter
    def local_storage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @local_storage_types.setter
    def local_storage_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSpotPriceAsPercentageOfOptimalOnDemandPrice")
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_spot_price_as_percentage_of_optimal_on_demand_price.setter
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgs]]:
        
        ...
    
    @memory_gib_per_vcpu.setter
    def memory_gib_per_vcpu(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgs]]:
        
        ...
    
    @network_bandwidth_gbps.setter
    def network_bandwidth_gbps(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsNetworkInterfaceCountArgs]]:
        
        ...
    
    @network_interface_count.setter
    def network_interface_count(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsNetworkInterfaceCountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @on_demand_max_price_percentage_over_lowest_price.setter
    def on_demand_max_price_percentage_over_lowest_price(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_hibernate_support.setter
    def require_hibernate_support(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @spot_max_price_percentage_over_lowest_price.setter
    def spot_max_price_percentage_over_lowest_price(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGb")
    def total_local_storage_gb(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsTotalLocalStorageGbArgs]]:
        
        ...
    
    @total_local_storage_gb.setter
    def total_local_storage_gb(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsTotalLocalStorageGbArgs]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsAcceleratorCountArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsAcceleratorCountArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsMemoryMibArgsDict(TypedDict):
    min: pulumi.Input[_builtins.int]
    max: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsMemoryMibArgs:
    def __init__(__self__, *, min: pulumi.Input[_builtins.int], max: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min.setter
    def min(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsNetworkInterfaceCountArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsNetworkInterfaceCountArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsTotalLocalStorageGbArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsTotalLocalStorageGbArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class LaunchTemplateInstanceRequirementsVcpuCountArgsDict(TypedDict):
    min: pulumi.Input[_builtins.int]
    max: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LaunchTemplateInstanceRequirementsVcpuCountArgs:
    def __init__(__self__, *, min: pulumi.Input[_builtins.int], max: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min.setter
    def min(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LaunchTemplateLicenseSpecificationArgsDict(TypedDict):
    license_configuration_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class LaunchTemplateLicenseSpecificationArgs:
    def __init__(__self__, *, license_configuration_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseConfigurationArn")
    def license_configuration_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @license_configuration_arn.setter
    def license_configuration_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LaunchTemplateMaintenanceOptionsArgsDict(TypedDict):
    auto_recovery: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateMaintenanceOptionsArgs:
    def __init__(__self__, *, auto_recovery: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRecovery")
    def auto_recovery(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_recovery.setter
    def auto_recovery(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateMetadataOptionsArgsDict(TypedDict):
    http_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    http_protocol_ipv6: NotRequired[pulumi.Input[_builtins.str]]
    http_put_response_hop_limit: NotRequired[pulumi.Input[_builtins.int]]
    http_tokens: NotRequired[pulumi.Input[_builtins.str]]
    instance_metadata_tags: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateMetadataOptionsArgs:
    def __init__(__self__, *, http_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., http_protocol_ipv6: Optional[pulumi.Input[_builtins.str]] = ..., http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ..., http_tokens: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_tags: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_endpoint.setter
    def http_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_protocol_ipv6.setter
    def http_protocol_ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_tokens.setter
    def http_tokens(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_metadata_tags.setter
    def instance_metadata_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateMonitoringArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class LaunchTemplateMonitoringArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class LaunchTemplateNetworkInterfaceArgsDict(TypedDict):
    associate_carrier_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    associate_public_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    connection_tracking_specification: NotRequired[pulumi.Input[LaunchTemplateNetworkInterfaceConnectionTrackingSpecificationArgsDict]]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    device_index: NotRequired[pulumi.Input[_builtins.int]]
    ena_srd_specification: NotRequired[pulumi.Input[LaunchTemplateNetworkInterfaceEnaSrdSpecificationArgsDict]]
    interface_type: NotRequired[pulumi.Input[_builtins.str]]
    ipv4_address_count: NotRequired[pulumi.Input[_builtins.int]]
    ipv4_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ipv4_prefix_count: NotRequired[pulumi.Input[_builtins.int]]
    ipv4_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ipv6_address_count: NotRequired[pulumi.Input[_builtins.int]]
    ipv6_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ipv6_prefix_count: NotRequired[pulumi.Input[_builtins.int]]
    ipv6_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    network_card_index: NotRequired[pulumi.Input[_builtins.int]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    primary_ipv6: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateNetworkInterfaceArgs:
    def __init__(__self__, *, associate_carrier_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., associate_public_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., connection_tracking_specification: Optional[pulumi.Input[LaunchTemplateNetworkInterfaceConnectionTrackingSpecificationArgs]] = ..., delete_on_termination: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., device_index: Optional[pulumi.Input[_builtins.int]] = ..., ena_srd_specification: Optional[pulumi.Input[LaunchTemplateNetworkInterfaceEnaSrdSpecificationArgs]] = ..., interface_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv4_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv4_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv4_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., network_card_index: Optional[pulumi.Input[_builtins.int]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., primary_ipv6: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateCarrierIpAddress")
    def associate_carrier_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @associate_carrier_ip_address.setter
    def associate_carrier_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTrackingSpecification")
    def connection_tracking_specification(self) -> Optional[pulumi.Input[LaunchTemplateNetworkInterfaceConnectionTrackingSpecificationArgs]]:
        
        ...
    
    @connection_tracking_specification.setter
    def connection_tracking_specification(self, value: Optional[pulumi.Input[LaunchTemplateNetworkInterfaceConnectionTrackingSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @device_index.setter
    def device_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enaSrdSpecification")
    def ena_srd_specification(self) -> Optional[pulumi.Input[LaunchTemplateNetworkInterfaceEnaSrdSpecificationArgs]]:
        
        ...
    
    @ena_srd_specification.setter
    def ena_srd_specification(self, value: Optional[pulumi.Input[LaunchTemplateNetworkInterfaceEnaSrdSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface_type.setter
    def interface_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4AddressCount")
    def ipv4_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv4_address_count.setter
    def ipv4_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv4_addresses.setter
    def ipv4_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4PrefixCount")
    def ipv4_prefix_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv4_prefix_count.setter
    def ipv4_prefix_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Prefixes")
    def ipv4_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv4_prefixes.setter
    def ipv4_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_address_count.setter
    def ipv6_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6PrefixCount")
    def ipv6_prefix_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_prefix_count.setter
    def ipv6_prefix_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Prefixes")
    def ipv6_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_prefixes.setter
    def ipv6_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @network_card_index.setter
    def network_card_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv6")
    def primary_ipv6(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_ipv6.setter
    def primary_ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateNetworkInterfaceConnectionTrackingSpecificationArgsDict(TypedDict):
    tcp_established_timeout: NotRequired[pulumi.Input[_builtins.int]]
    udp_stream_timeout: NotRequired[pulumi.Input[_builtins.int]]
    udp_timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LaunchTemplateNetworkInterfaceConnectionTrackingSpecificationArgs:
    def __init__(__self__, *, tcp_established_timeout: Optional[pulumi.Input[_builtins.int]] = ..., udp_stream_timeout: Optional[pulumi.Input[_builtins.int]] = ..., udp_timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpEstablishedTimeout")
    def tcp_established_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tcp_established_timeout.setter
    def tcp_established_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpStreamTimeout")
    def udp_stream_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @udp_stream_timeout.setter
    def udp_stream_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpTimeout")
    def udp_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @udp_timeout.setter
    def udp_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LaunchTemplateNetworkInterfaceEnaSrdSpecificationArgsDict(TypedDict):
    ena_srd_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ena_srd_udp_specification: NotRequired[pulumi.Input[LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecificationArgsDict]]


@pulumi.input_type
class LaunchTemplateNetworkInterfaceEnaSrdSpecificationArgs:
    def __init__(__self__, *, ena_srd_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ena_srd_udp_specification: Optional[pulumi.Input[LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecificationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enaSrdEnabled")
    def ena_srd_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ena_srd_enabled.setter
    def ena_srd_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enaSrdUdpSpecification")
    def ena_srd_udp_specification(self) -> Optional[pulumi.Input[LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecificationArgs]]:
        
        ...
    
    @ena_srd_udp_specification.setter
    def ena_srd_udp_specification(self, value: Optional[pulumi.Input[LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecificationArgs]]): # -> None:
        ...
    


class LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecificationArgsDict(TypedDict):
    ena_srd_udp_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class LaunchTemplateNetworkInterfaceEnaSrdSpecificationEnaSrdUdpSpecificationArgs:
    def __init__(__self__, *, ena_srd_udp_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enaSrdUdpEnabled")
    def ena_srd_udp_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ena_srd_udp_enabled.setter
    def ena_srd_udp_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class LaunchTemplateNetworkPerformanceOptionsArgsDict(TypedDict):
    bandwidth_weighting: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateNetworkPerformanceOptionsArgs:
    def __init__(__self__, *, bandwidth_weighting: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthWeighting")
    def bandwidth_weighting(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bandwidth_weighting.setter
    def bandwidth_weighting(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplatePlacementArgsDict(TypedDict):
    affinity: NotRequired[pulumi.Input[_builtins.str]]
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    group_name: NotRequired[pulumi.Input[_builtins.str]]
    host_id: NotRequired[pulumi.Input[_builtins.str]]
    host_resource_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    partition_number: NotRequired[pulumi.Input[_builtins.int]]
    spread_domain: NotRequired[pulumi.Input[_builtins.str]]
    tenancy: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplatePlacementArgs:
    def __init__(__self__, *, affinity: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., group_id: Optional[pulumi.Input[_builtins.str]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., host_id: Optional[pulumi.Input[_builtins.str]] = ..., host_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., partition_number: Optional[pulumi.Input[_builtins.int]] = ..., spread_domain: Optional[pulumi.Input[_builtins.str]] = ..., tenancy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def affinity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @affinity.setter
    def affinity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_id.setter
    def host_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_resource_group_arn.setter
    def host_resource_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionNumber")
    def partition_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @partition_number.setter
    def partition_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spreadDomain")
    def spread_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spread_domain.setter
    def spread_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplatePrivateDnsNameOptionsArgsDict(TypedDict):
    enable_resource_name_dns_a_record: NotRequired[pulumi.Input[_builtins.bool]]
    enable_resource_name_dns_aaaa_record: NotRequired[pulumi.Input[_builtins.bool]]
    hostname_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplatePrivateDnsNameOptionsArgs:
    def __init__(__self__, *, enable_resource_name_dns_a_record: Optional[pulumi.Input[_builtins.bool]] = ..., enable_resource_name_dns_aaaa_record: Optional[pulumi.Input[_builtins.bool]] = ..., hostname_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_a_record.setter
    def enable_resource_name_dns_a_record(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_aaaa_record.setter
    def enable_resource_name_dns_aaaa_record(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameType")
    def hostname_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hostname_type.setter
    def hostname_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateSecondaryInterfaceArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    device_index: NotRequired[pulumi.Input[_builtins.int]]
    interface_type: NotRequired[pulumi.Input[_builtins.str]]
    network_card_index: NotRequired[pulumi.Input[_builtins.int]]
    private_ip_address_count: NotRequired[pulumi.Input[_builtins.int]]
    private_ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secondary_subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LaunchTemplateSecondaryInterfaceArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., device_index: Optional[pulumi.Input[_builtins.int]] = ..., interface_type: Optional[pulumi.Input[_builtins.str]] = ..., network_card_index: Optional[pulumi.Input[_builtins.int]] = ..., private_ip_address_count: Optional[pulumi.Input[_builtins.int]] = ..., private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secondary_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @device_index.setter
    def device_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface_type.setter
    def interface_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @network_card_index.setter
    def network_card_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddressCount")
    def private_ip_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @private_ip_address_count.setter
    def private_ip_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_ip_addresses.setter
    def private_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondarySubnetId")
    def secondary_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_subnet_id.setter
    def secondary_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LaunchTemplateTagSpecificationArgsDict(TypedDict):
    resource_type: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class LaunchTemplateTagSpecificationArgs:
    def __init__(__self__, *, resource_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ManagedPrefixListEntryArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedPrefixListEntryArgs:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NatGatewayAvailabilityZoneAddressArgsDict(TypedDict):
    allocation_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    availability_zone_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NatGatewayAvailabilityZoneAddressArgs:
    def __init__(__self__, *, allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationIds")
    def allocation_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allocation_ids.setter
    def allocation_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NatGatewayEipAssociationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NatGatewayEipAssociationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NatGatewayRegionalNatGatewayAddressArgsDict(TypedDict):
    allocation_id: NotRequired[pulumi.Input[_builtins.str]]
    association_id: NotRequired[pulumi.Input[_builtins.str]]
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    availability_zone_id: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    public_ip: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NatGatewayRegionalNatGatewayAddressArgs:
    def __init__(__self__, *, allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., association_id: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., public_ip: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkAclEgressArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    rule_no: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    icmp_code: NotRequired[pulumi.Input[_builtins.int]]
    icmp_type: NotRequired[pulumi.Input[_builtins.int]]
    ipv6_cidr_block: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkAclEgressArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], rule_no: pulumi.Input[_builtins.int], to_port: pulumi.Input[_builtins.int], cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., icmp_code: Optional[pulumi.Input[_builtins.int]] = ..., icmp_type: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNo")
    def rule_no(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @rule_no.setter
    def rule_no(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_code.setter
    def icmp_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_type.setter
    def icmp_type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkAclIngressArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    rule_no: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    icmp_code: NotRequired[pulumi.Input[_builtins.int]]
    icmp_type: NotRequired[pulumi.Input[_builtins.int]]
    ipv6_cidr_block: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkAclIngressArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], rule_no: pulumi.Input[_builtins.int], to_port: pulumi.Input[_builtins.int], cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., icmp_code: Optional[pulumi.Input[_builtins.int]] = ..., icmp_type: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNo")
    def rule_no(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @rule_no.setter
    def rule_no(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_code.setter
    def icmp_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_type.setter
    def icmp_type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisAlternatePathHintArgsDict(TypedDict):
    component_arn: NotRequired[pulumi.Input[_builtins.str]]
    component_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisAlternatePathHintArgs:
    def __init__(__self__, *, component_arn: Optional[pulumi.Input[_builtins.str]] = ..., component_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @component_arn.setter
    def component_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationArgsDict(TypedDict):
    acl_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclRuleArgsDict]]]]
    acls: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclArgsDict]]]]
    address: NotRequired[pulumi.Input[_builtins.str]]
    addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    attached_tos: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAttachedToArgsDict]]]]
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    classic_load_balancer_listeners: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationClassicLoadBalancerListenerArgsDict]]]]
    components: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationComponentArgsDict]]]]
    customer_gateways: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationCustomerGatewayArgsDict]]]]
    destination_vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationDestinationVpcArgsDict]]]]
    destinations: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationDestinationArgsDict]]]]
    direction: NotRequired[pulumi.Input[_builtins.str]]
    elastic_load_balancer_listeners: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationElasticLoadBalancerListenerArgsDict]]]]
    explanation_code: NotRequired[pulumi.Input[_builtins.str]]
    ingress_route_tables: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationIngressRouteTableArgsDict]]]]
    internet_gateways: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationInternetGatewayArgsDict]]]]
    load_balancer_arn: NotRequired[pulumi.Input[_builtins.str]]
    load_balancer_listener_port: NotRequired[pulumi.Input[_builtins.int]]
    load_balancer_target_group: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgsDict]]]]
    load_balancer_target_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgsDict]]]]
    load_balancer_target_port: NotRequired[pulumi.Input[_builtins.int]]
    missing_component: NotRequired[pulumi.Input[_builtins.str]]
    nat_gateways: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationNatGatewayArgsDict]]]]
    network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationNetworkInterfaceArgsDict]]]]
    packet_field: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationPortRangeArgsDict]]]]
    prefix_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationPrefixListArgsDict]]]]
    protocols: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    route_table_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationRouteTableRouteArgsDict]]]]
    route_tables: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationRouteTableArgsDict]]]]
    security_group: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupArgsDict]]]]
    security_group_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupRuleArgsDict]]]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupArgsDict]]]]
    source_vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSourceVpcArgsDict]]]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    subnet_route_tables: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSubnetRouteTableArgsDict]]]]
    subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSubnetArgsDict]]]]
    transit_gateway_attachments: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayAttachmentArgsDict]]]]
    transit_gateway_route_table_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteArgsDict]]]]
    transit_gateway_route_tables: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayRouteTableArgsDict]]]]
    transit_gateways: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayArgsDict]]]]
    vpc_endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcEndpointArgsDict]]]]
    vpc_peering_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcPeeringConnectionArgsDict]]]]
    vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcArgsDict]]]]
    vpn_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpnConnectionArgsDict]]]]
    vpn_gateways: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpnGatewayArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationArgs:
    def __init__(__self__, *, acl_rules: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclRuleArgs]]]] = ..., acls: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclArgs]]]] = ..., address: Optional[pulumi.Input[_builtins.str]] = ..., addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., attached_tos: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAttachedToArgs]]]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., classic_load_balancer_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationClassicLoadBalancerListenerArgs]]]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationComponentArgs]]]] = ..., customer_gateways: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationCustomerGatewayArgs]]]] = ..., destination_vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationDestinationVpcArgs]]]] = ..., destinations: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationDestinationArgs]]]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., elastic_load_balancer_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationElasticLoadBalancerListenerArgs]]]] = ..., explanation_code: Optional[pulumi.Input[_builtins.str]] = ..., ingress_route_tables: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationIngressRouteTableArgs]]]] = ..., internet_gateways: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationInternetGatewayArgs]]]] = ..., load_balancer_arn: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer_listener_port: Optional[pulumi.Input[_builtins.int]] = ..., load_balancer_target_group: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgs]]]] = ..., load_balancer_target_groups: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgs]]]] = ..., load_balancer_target_port: Optional[pulumi.Input[_builtins.int]] = ..., missing_component: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateways: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationNatGatewayArgs]]]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationNetworkInterfaceArgs]]]] = ..., packet_field: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationPortRangeArgs]]]] = ..., prefix_lists: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationPrefixListArgs]]]] = ..., protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., route_table_routes: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationRouteTableRouteArgs]]]] = ..., route_tables: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationRouteTableArgs]]]] = ..., security_group: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupArgs]]]] = ..., security_group_rules: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupRuleArgs]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupArgs]]]] = ..., source_vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSourceVpcArgs]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnet_route_tables: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSubnetRouteTableArgs]]]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSubnetArgs]]]] = ..., transit_gateway_attachments: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayAttachmentArgs]]]] = ..., transit_gateway_route_table_routes: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteArgs]]]] = ..., transit_gateway_route_tables: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayRouteTableArgs]]]] = ..., transit_gateways: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayArgs]]]] = ..., vpc_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcEndpointArgs]]]] = ..., vpc_peering_connections: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcPeeringConnectionArgs]]]] = ..., vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcArgs]]]] = ..., vpn_connections: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpnConnectionArgs]]]] = ..., vpn_gateways: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpnGatewayArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclRuleArgs]]]]:
        ...
    
    @acl_rules.setter
    def acl_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def acls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclArgs]]]]:
        ...
    
    @acls.setter
    def acls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @addresses.setter
    def addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAttachedToArgs]]]]:
        ...
    
    @attached_tos.setter
    def attached_tos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAttachedToArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @cidrs.setter
    def cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classicLoadBalancerListeners")
    def classic_load_balancer_listeners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationClassicLoadBalancerListenerArgs]]]]:
        ...
    
    @classic_load_balancer_listeners.setter
    def classic_load_balancer_listeners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationClassicLoadBalancerListenerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationComponentArgs]]]]:
        ...
    
    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationComponentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerGateways")
    def customer_gateways(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationCustomerGatewayArgs]]]]:
        ...
    
    @customer_gateways.setter
    def customer_gateways(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationCustomerGatewayArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationDestinationVpcArgs]]]]:
        ...
    
    @destination_vpcs.setter
    def destination_vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationDestinationVpcArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationDestinationArgs]]]]:
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationDestinationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticLoadBalancerListeners")
    def elastic_load_balancer_listeners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationElasticLoadBalancerListenerArgs]]]]:
        ...
    
    @elastic_load_balancer_listeners.setter
    def elastic_load_balancer_listeners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationElasticLoadBalancerListenerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="explanationCode")
    def explanation_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @explanation_code.setter
    def explanation_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressRouteTables")
    def ingress_route_tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationIngressRouteTableArgs]]]]:
        ...
    
    @ingress_route_tables.setter
    def ingress_route_tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationIngressRouteTableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateways")
    def internet_gateways(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationInternetGatewayArgs]]]]:
        ...
    
    @internet_gateways.setter
    def internet_gateways(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationInternetGatewayArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @load_balancer_arn.setter
    def load_balancer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerListenerPort")
    def load_balancer_listener_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @load_balancer_listener_port.setter
    def load_balancer_listener_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetGroup")
    def load_balancer_target_group(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgs]]]]:
        ...
    
    @load_balancer_target_group.setter
    def load_balancer_target_group(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetGroups")
    def load_balancer_target_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgs]]]]:
        ...
    
    @load_balancer_target_groups.setter
    def load_balancer_target_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerTargetPort")
    def load_balancer_target_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @load_balancer_target_port.setter
    def load_balancer_target_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="missingComponent")
    def missing_component(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @missing_component.setter
    def missing_component(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateways")
    def nat_gateways(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationNatGatewayArgs]]]]:
        ...
    
    @nat_gateways.setter
    def nat_gateways(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationNatGatewayArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationNetworkInterfaceArgs]]]]:
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packetField")
    def packet_field(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @packet_field.setter
    def packet_field(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationPortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationPrefixListArgs]]]]:
        ...
    
    @prefix_lists.setter
    def prefix_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationPrefixListArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @protocols.setter
    def protocols(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationRouteTableRouteArgs]]]]:
        ...
    
    @route_table_routes.setter
    def route_table_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationRouteTableRouteArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTables")
    def route_tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationRouteTableArgs]]]]:
        ...
    
    @route_tables.setter
    def route_tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationRouteTableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupArgs]]]]:
        ...
    
    @security_group.setter
    def security_group(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupRuleArgs]]]]:
        ...
    
    @security_group_rules.setter
    def security_group_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupArgs]]]]:
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSourceVpcArgs]]]]:
        ...
    
    @source_vpcs.setter
    def source_vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSourceVpcArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetRouteTables")
    def subnet_route_tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSubnetRouteTableArgs]]]]:
        ...
    
    @subnet_route_tables.setter
    def subnet_route_tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSubnetRouteTableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSubnetArgs]]]]:
        ...
    
    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSubnetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachments")
    def transit_gateway_attachments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayAttachmentArgs]]]]:
        ...
    
    @transit_gateway_attachments.setter
    def transit_gateway_attachments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayAttachmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteArgs]]]]:
        ...
    
    @transit_gateway_route_table_routes.setter
    def transit_gateway_route_table_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTables")
    def transit_gateway_route_tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayRouteTableArgs]]]]:
        ...
    
    @transit_gateway_route_tables.setter
    def transit_gateway_route_tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayRouteTableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayArgs]]]]:
        ...
    
    @transit_gateways.setter
    def transit_gateways(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationTransitGatewayArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcEndpointArgs]]]]:
        ...
    
    @vpc_endpoints.setter
    def vpc_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnections")
    def vpc_peering_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcPeeringConnectionArgs]]]]:
        ...
    
    @vpc_peering_connections.setter
    def vpc_peering_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcPeeringConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcArgs]]]]:
        ...
    
    @vpcs.setter
    def vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpcArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnConnections")
    def vpn_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpnConnectionArgs]]]]:
        ...
    
    @vpn_connections.setter
    def vpn_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpnConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnGateways")
    def vpn_gateways(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpnGatewayArgs]]]]:
        ...
    
    @vpn_gateways.setter
    def vpn_gateways(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationVpnGatewayArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationAclArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationAclArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationAclRuleArgsDict(TypedDict):
    cidr: NotRequired[pulumi.Input[_builtins.str]]
    egress: NotRequired[pulumi.Input[_builtins.bool]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclRulePortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    rule_action: NotRequired[pulumi.Input[_builtins.str]]
    rule_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationAclRuleArgs:
    def __init__(__self__, *, cidr: Optional[pulumi.Input[_builtins.str]] = ..., egress: Optional[pulumi.Input[_builtins.bool]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclRulePortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., rule_action: Optional[pulumi.Input[_builtins.str]] = ..., rule_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclRulePortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationAclRulePortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @rule_action.setter
    def rule_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @rule_number.setter
    def rule_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationAclRulePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationAclRulePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationAttachedToArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationAttachedToArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationClassicLoadBalancerListenerArgsDict(TypedDict):
    instance_port: NotRequired[pulumi.Input[_builtins.int]]
    load_balancer_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationClassicLoadBalancerListenerArgs:
    def __init__(__self__, *, instance_port: Optional[pulumi.Input[_builtins.int]] = ..., load_balancer_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @instance_port.setter
    def instance_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerPort")
    def load_balancer_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @load_balancer_port.setter
    def load_balancer_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationComponentArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationComponentArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationCustomerGatewayArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationCustomerGatewayArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationDestinationArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationDestinationArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationDestinationVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationDestinationVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationElasticLoadBalancerListenerArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationElasticLoadBalancerListenerArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationIngressRouteTableArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationIngressRouteTableArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationInternetGatewayArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationInternetGatewayArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationLoadBalancerTargetGroupArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationNatGatewayArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationNatGatewayArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationNetworkInterfaceArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationNetworkInterfaceArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationPortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationPortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationPrefixListArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationPrefixListArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationRouteTableArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationRouteTableArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationRouteTableRouteArgsDict(TypedDict):
    destination_cidr: NotRequired[pulumi.Input[_builtins.str]]
    destination_prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    egress_only_internet_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    instance_id: NotRequired[pulumi.Input[_builtins.str]]
    nat_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    origin: NotRequired[pulumi.Input[_builtins.str]]
    transit_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_peering_connection_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationRouteTableRouteArgs:
    def __init__(__self__, *, destination_cidr: Optional[pulumi.Input[_builtins.str]] = ..., destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_only_internet_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., origin: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_cidr.setter
    def destination_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_prefix_list_id.setter
    def destination_prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @egress_only_internet_gateway_id.setter
    def egress_only_internet_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @origin.setter
    def origin(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationSecurityGroupArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationSecurityGroupArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationSecurityGroupRuleArgsDict(TypedDict):
    cidr: NotRequired[pulumi.Input[_builtins.str]]
    direction: NotRequired[pulumi.Input[_builtins.str]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeArgsDict]]]]
    prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    security_group_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationSecurityGroupRuleArgs:
    def __init__(__self__, *, cidr: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeArgs]]]] = ..., prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationSecurityGroupRulePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationSourceVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationSourceVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationSubnetArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationSubnetArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationSubnetRouteTableArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationSubnetRouteTableArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationTransitGatewayArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationTransitGatewayArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationTransitGatewayAttachmentArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationTransitGatewayAttachmentArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationTransitGatewayRouteTableArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationTransitGatewayRouteTableArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteArgsDict(TypedDict):
    attachment_id: NotRequired[pulumi.Input[_builtins.str]]
    destination_cidr: NotRequired[pulumi.Input[_builtins.str]]
    prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]
    route_origin: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationTransitGatewayRouteTableRouteArgs:
    def __init__(__self__, *, attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_cidr: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., route_origin: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_cidr.setter
    def destination_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @route_origin.setter
    def route_origin(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationVpcEndpointArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationVpcEndpointArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationVpcPeeringConnectionArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationVpcPeeringConnectionArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationVpnConnectionArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationVpnConnectionArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisExplanationVpnGatewayArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisExplanationVpnGatewayArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentArgsDict(TypedDict):
    acl_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAclRuleArgsDict]]]]
    additional_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAdditionalDetailArgsDict]]]]
    attached_tos: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAttachedToArgsDict]]]]
    components: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentComponentArgsDict]]]]
    destination_vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentDestinationVpcArgsDict]]]]
    inbound_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderArgsDict]]]]
    outbound_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderArgsDict]]]]
    route_table_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentRouteTableRouteArgsDict]]]]
    security_group_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleArgsDict]]]]
    sequence_number: NotRequired[pulumi.Input[_builtins.int]]
    source_vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSourceVpcArgsDict]]]]
    subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSubnetArgsDict]]]]
    transit_gateway_route_table_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteArgsDict]]]]
    transit_gateways: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentTransitGatewayArgsDict]]]]
    vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentVpcArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentArgs:
    def __init__(__self__, *, acl_rules: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAclRuleArgs]]]] = ..., additional_details: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAdditionalDetailArgs]]]] = ..., attached_tos: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAttachedToArgs]]]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentComponentArgs]]]] = ..., destination_vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentDestinationVpcArgs]]]] = ..., inbound_headers: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderArgs]]]] = ..., outbound_headers: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderArgs]]]] = ..., route_table_routes: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentRouteTableRouteArgs]]]] = ..., security_group_rules: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleArgs]]]] = ..., sequence_number: Optional[pulumi.Input[_builtins.int]] = ..., source_vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSourceVpcArgs]]]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSubnetArgs]]]] = ..., transit_gateway_route_table_routes: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteArgs]]]] = ..., transit_gateways: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentTransitGatewayArgs]]]] = ..., vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentVpcArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAclRuleArgs]]]]:
        ...
    
    @acl_rules.setter
    def acl_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAclRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAdditionalDetailArgs]]]]:
        ...
    
    @additional_details.setter
    def additional_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAdditionalDetailArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAttachedToArgs]]]]:
        ...
    
    @attached_tos.setter
    def attached_tos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAttachedToArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentComponentArgs]]]]:
        ...
    
    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentComponentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentDestinationVpcArgs]]]]:
        ...
    
    @destination_vpcs.setter
    def destination_vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentDestinationVpcArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundHeaders")
    def inbound_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderArgs]]]]:
        ...
    
    @inbound_headers.setter
    def inbound_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundHeaders")
    def outbound_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderArgs]]]]:
        ...
    
    @outbound_headers.setter
    def outbound_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentRouteTableRouteArgs]]]]:
        ...
    
    @route_table_routes.setter
    def route_table_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentRouteTableRouteArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleArgs]]]]:
        ...
    
    @security_group_rules.setter
    def security_group_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @sequence_number.setter
    def sequence_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSourceVpcArgs]]]]:
        ...
    
    @source_vpcs.setter
    def source_vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSourceVpcArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSubnetArgs]]]]:
        ...
    
    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSubnetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteArgs]]]]:
        ...
    
    @transit_gateway_route_table_routes.setter
    def transit_gateway_route_table_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentTransitGatewayArgs]]]]:
        ...
    
    @transit_gateways.setter
    def transit_gateways(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentTransitGatewayArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentVpcArgs]]]]:
        ...
    
    @vpcs.setter
    def vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentVpcArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentAclRuleArgsDict(TypedDict):
    cidr: NotRequired[pulumi.Input[_builtins.str]]
    egress: NotRequired[pulumi.Input[_builtins.bool]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAclRulePortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    rule_action: NotRequired[pulumi.Input[_builtins.str]]
    rule_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentAclRuleArgs:
    def __init__(__self__, *, cidr: Optional[pulumi.Input[_builtins.str]] = ..., egress: Optional[pulumi.Input[_builtins.bool]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAclRulePortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., rule_action: Optional[pulumi.Input[_builtins.str]] = ..., rule_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAclRulePortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAclRulePortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @rule_action.setter
    def rule_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @rule_number.setter
    def rule_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentAclRulePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentAclRulePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentAdditionalDetailArgsDict(TypedDict):
    additional_detail_type: NotRequired[pulumi.Input[_builtins.str]]
    components: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentAdditionalDetailArgs:
    def __init__(__self__, *, additional_detail_type: Optional[pulumi.Input[_builtins.str]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetailType")
    def additional_detail_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @additional_detail_type.setter
    def additional_detail_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentArgs]]]]:
        ...
    
    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentAdditionalDetailComponentArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentAttachedToArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentAttachedToArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentComponentArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentComponentArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentDestinationVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentDestinationVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentInboundHeaderArgsDict(TypedDict):
    destination_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    destination_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    source_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    source_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentInboundHeaderArgs:
    def __init__(__self__, *, destination_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., source_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @destination_addresses.setter
    def destination_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeArgs]]]]:
        ...
    
    @destination_port_ranges.setter
    def destination_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @source_addresses.setter
    def source_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeArgs]]]]:
        ...
    
    @source_port_ranges.setter
    def source_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentInboundHeaderDestinationPortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentInboundHeaderSourcePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentOutboundHeaderArgsDict(TypedDict):
    destination_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    destination_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    source_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    source_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentOutboundHeaderArgs:
    def __init__(__self__, *, destination_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., source_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @destination_addresses.setter
    def destination_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeArgs]]]]:
        ...
    
    @destination_port_ranges.setter
    def destination_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @source_addresses.setter
    def source_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeArgs]]]]:
        ...
    
    @source_port_ranges.setter
    def source_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentOutboundHeaderDestinationPortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentOutboundHeaderSourcePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentRouteTableRouteArgsDict(TypedDict):
    destination_cidr: NotRequired[pulumi.Input[_builtins.str]]
    destination_prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    egress_only_internet_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    instance_id: NotRequired[pulumi.Input[_builtins.str]]
    nat_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    origin: NotRequired[pulumi.Input[_builtins.str]]
    transit_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_peering_connection_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentRouteTableRouteArgs:
    def __init__(__self__, *, destination_cidr: Optional[pulumi.Input[_builtins.str]] = ..., destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_only_internet_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., origin: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_cidr.setter
    def destination_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_prefix_list_id.setter
    def destination_prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @egress_only_internet_gateway_id.setter
    def egress_only_internet_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @origin.setter
    def origin(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleArgsDict(TypedDict):
    cidr: NotRequired[pulumi.Input[_builtins.str]]
    direction: NotRequired[pulumi.Input[_builtins.str]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeArgsDict]]]]
    prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    security_group_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentSecurityGroupRuleArgs:
    def __init__(__self__, *, cidr: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeArgs]]]] = ..., prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentSecurityGroupRulePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentSourceVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentSourceVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentSubnetArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentSubnetArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentTransitGatewayArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentTransitGatewayArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteArgsDict(TypedDict):
    attachment_id: NotRequired[pulumi.Input[_builtins.str]]
    destination_cidr: NotRequired[pulumi.Input[_builtins.str]]
    prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]
    route_origin: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentTransitGatewayRouteTableRouteArgs:
    def __init__(__self__, *, attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_cidr: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., route_origin: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_cidr.setter
    def destination_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @route_origin.setter
    def route_origin(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisForwardPathComponentVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisForwardPathComponentVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentArgsDict(TypedDict):
    acl_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAclRuleArgsDict]]]]
    additional_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAdditionalDetailArgsDict]]]]
    attached_tos: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAttachedToArgsDict]]]]
    components: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentComponentArgsDict]]]]
    destination_vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentDestinationVpcArgsDict]]]]
    inbound_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderArgsDict]]]]
    outbound_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderArgsDict]]]]
    route_table_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentRouteTableRouteArgsDict]]]]
    security_group_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleArgsDict]]]]
    sequence_number: NotRequired[pulumi.Input[_builtins.int]]
    source_vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSourceVpcArgsDict]]]]
    subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSubnetArgsDict]]]]
    transit_gateway_route_table_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteArgsDict]]]]
    transit_gateways: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentTransitGatewayArgsDict]]]]
    vpcs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentVpcArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentArgs:
    def __init__(__self__, *, acl_rules: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAclRuleArgs]]]] = ..., additional_details: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAdditionalDetailArgs]]]] = ..., attached_tos: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAttachedToArgs]]]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentComponentArgs]]]] = ..., destination_vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentDestinationVpcArgs]]]] = ..., inbound_headers: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderArgs]]]] = ..., outbound_headers: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderArgs]]]] = ..., route_table_routes: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentRouteTableRouteArgs]]]] = ..., security_group_rules: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleArgs]]]] = ..., sequence_number: Optional[pulumi.Input[_builtins.int]] = ..., source_vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSourceVpcArgs]]]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSubnetArgs]]]] = ..., transit_gateway_route_table_routes: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteArgs]]]] = ..., transit_gateways: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentTransitGatewayArgs]]]] = ..., vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentVpcArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclRules")
    def acl_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAclRuleArgs]]]]:
        ...
    
    @acl_rules.setter
    def acl_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAclRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAdditionalDetailArgs]]]]:
        ...
    
    @additional_details.setter
    def additional_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAdditionalDetailArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedTos")
    def attached_tos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAttachedToArgs]]]]:
        ...
    
    @attached_tos.setter
    def attached_tos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAttachedToArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentComponentArgs]]]]:
        ...
    
    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentComponentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationVpcs")
    def destination_vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentDestinationVpcArgs]]]]:
        ...
    
    @destination_vpcs.setter
    def destination_vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentDestinationVpcArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundHeaders")
    def inbound_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderArgs]]]]:
        ...
    
    @inbound_headers.setter
    def inbound_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundHeaders")
    def outbound_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderArgs]]]]:
        ...
    
    @outbound_headers.setter
    def outbound_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableRoutes")
    def route_table_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentRouteTableRouteArgs]]]]:
        ...
    
    @route_table_routes.setter
    def route_table_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentRouteTableRouteArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleArgs]]]]:
        ...
    
    @security_group_rules.setter
    def security_group_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @sequence_number.setter
    def sequence_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVpcs")
    def source_vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSourceVpcArgs]]]]:
        ...
    
    @source_vpcs.setter
    def source_vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSourceVpcArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSubnetArgs]]]]:
        ...
    
    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSubnetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableRoutes")
    def transit_gateway_route_table_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteArgs]]]]:
        ...
    
    @transit_gateway_route_table_routes.setter
    def transit_gateway_route_table_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGateways")
    def transit_gateways(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentTransitGatewayArgs]]]]:
        ...
    
    @transit_gateways.setter
    def transit_gateways(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentTransitGatewayArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentVpcArgs]]]]:
        ...
    
    @vpcs.setter
    def vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentVpcArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentAclRuleArgsDict(TypedDict):
    cidr: NotRequired[pulumi.Input[_builtins.str]]
    egress: NotRequired[pulumi.Input[_builtins.bool]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAclRulePortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    rule_action: NotRequired[pulumi.Input[_builtins.str]]
    rule_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentAclRuleArgs:
    def __init__(__self__, *, cidr: Optional[pulumi.Input[_builtins.str]] = ..., egress: Optional[pulumi.Input[_builtins.bool]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAclRulePortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., rule_action: Optional[pulumi.Input[_builtins.str]] = ..., rule_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAclRulePortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAclRulePortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @rule_action.setter
    def rule_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @rule_number.setter
    def rule_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentAclRulePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentAclRulePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentAdditionalDetailArgsDict(TypedDict):
    additional_detail_type: NotRequired[pulumi.Input[_builtins.str]]
    components: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentAdditionalDetailArgs:
    def __init__(__self__, *, additional_detail_type: Optional[pulumi.Input[_builtins.str]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetailType")
    def additional_detail_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @additional_detail_type.setter
    def additional_detail_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentArgs]]]]:
        ...
    
    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentAdditionalDetailComponentArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentAttachedToArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentAttachedToArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentComponentArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentComponentArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentDestinationVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentDestinationVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentInboundHeaderArgsDict(TypedDict):
    destination_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    destination_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    source_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    source_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentInboundHeaderArgs:
    def __init__(__self__, *, destination_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., source_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @destination_addresses.setter
    def destination_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeArgs]]]]:
        ...
    
    @destination_port_ranges.setter
    def destination_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @source_addresses.setter
    def source_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeArgs]]]]:
        ...
    
    @source_port_ranges.setter
    def source_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentInboundHeaderDestinationPortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentInboundHeaderSourcePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentOutboundHeaderArgsDict(TypedDict):
    destination_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    destination_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeArgsDict]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    source_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    source_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeArgsDict]]]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentOutboundHeaderArgs:
    def __init__(__self__, *, destination_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeArgs]]]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., source_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddresses")
    def destination_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @destination_addresses.setter
    def destination_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeArgs]]]]:
        ...
    
    @destination_port_ranges.setter
    def destination_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @source_addresses.setter
    def source_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeArgs]]]]:
        ...
    
    @source_port_ranges.setter
    def source_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeArgs]]]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentOutboundHeaderDestinationPortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentOutboundHeaderSourcePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentRouteTableRouteArgsDict(TypedDict):
    destination_cidr: NotRequired[pulumi.Input[_builtins.str]]
    destination_prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    egress_only_internet_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    instance_id: NotRequired[pulumi.Input[_builtins.str]]
    nat_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    origin: NotRequired[pulumi.Input[_builtins.str]]
    transit_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_peering_connection_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentRouteTableRouteArgs:
    def __init__(__self__, *, destination_cidr: Optional[pulumi.Input[_builtins.str]] = ..., destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_only_internet_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., origin: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_cidr.setter
    def destination_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_prefix_list_id.setter
    def destination_prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @egress_only_internet_gateway_id.setter
    def egress_only_internet_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @origin.setter
    def origin(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleArgsDict(TypedDict):
    cidr: NotRequired[pulumi.Input[_builtins.str]]
    direction: NotRequired[pulumi.Input[_builtins.str]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeArgsDict]]]]
    prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    security_group_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentSecurityGroupRuleArgs:
    def __init__(__self__, *, cidr: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeArgs]]]] = ..., prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeArgs]]]]:
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentSecurityGroupRulePortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentSourceVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentSourceVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentSubnetArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentSubnetArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentTransitGatewayArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentTransitGatewayArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteArgsDict(TypedDict):
    attachment_id: NotRequired[pulumi.Input[_builtins.str]]
    destination_cidr: NotRequired[pulumi.Input[_builtins.str]]
    prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]
    route_origin: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentTransitGatewayRouteTableRouteArgs:
    def __init__(__self__, *, attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_cidr: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., route_origin: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination_cidr.setter
    def destination_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeOrigin")
    def route_origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @route_origin.setter
    def route_origin(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsAnalysisReturnPathComponentVpcArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInsightsAnalysisReturnPathComponentVpcArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInsightsPathFilterAtDestinationArgsDict(TypedDict):
    destination_address: NotRequired[pulumi.Input[_builtins.str]]
    destination_port_range: NotRequired[pulumi.Input[NetworkInsightsPathFilterAtDestinationDestinationPortRangeArgsDict]]
    source_address: NotRequired[pulumi.Input[_builtins.str]]
    source_port_range: NotRequired[pulumi.Input[NetworkInsightsPathFilterAtDestinationSourcePortRangeArgsDict]]


@pulumi.input_type
class NetworkInsightsPathFilterAtDestinationArgs:
    def __init__(__self__, *, destination_address: Optional[pulumi.Input[_builtins.str]] = ..., destination_port_range: Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationDestinationPortRangeArgs]] = ..., source_address: Optional[pulumi.Input[_builtins.str]] = ..., source_port_range: Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationSourcePortRangeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_address.setter
    def destination_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationDestinationPortRangeArgs]]:
        
        ...
    
    @destination_port_range.setter
    def destination_port_range(self, value: Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationDestinationPortRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddress")
    def source_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_address.setter
    def source_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationSourcePortRangeArgs]]:
        
        ...
    
    @source_port_range.setter
    def source_port_range(self, value: Optional[pulumi.Input[NetworkInsightsPathFilterAtDestinationSourcePortRangeArgs]]): # -> None:
        ...
    


class NetworkInsightsPathFilterAtDestinationDestinationPortRangeArgsDict(TypedDict):
    from_port: NotRequired[pulumi.Input[_builtins.int]]
    to_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsPathFilterAtDestinationDestinationPortRangeArgs:
    def __init__(__self__, *, from_port: Optional[pulumi.Input[_builtins.int]] = ..., to_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsPathFilterAtDestinationSourcePortRangeArgsDict(TypedDict):
    from_port: NotRequired[pulumi.Input[_builtins.int]]
    to_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsPathFilterAtDestinationSourcePortRangeArgs:
    def __init__(__self__, *, from_port: Optional[pulumi.Input[_builtins.int]] = ..., to_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsPathFilterAtSourceArgsDict(TypedDict):
    destination_address: NotRequired[pulumi.Input[_builtins.str]]
    destination_port_range: NotRequired[pulumi.Input[NetworkInsightsPathFilterAtSourceDestinationPortRangeArgsDict]]
    source_address: NotRequired[pulumi.Input[_builtins.str]]
    source_port_range: NotRequired[pulumi.Input[NetworkInsightsPathFilterAtSourceSourcePortRangeArgsDict]]


@pulumi.input_type
class NetworkInsightsPathFilterAtSourceArgs:
    def __init__(__self__, *, destination_address: Optional[pulumi.Input[_builtins.str]] = ..., destination_port_range: Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceDestinationPortRangeArgs]] = ..., source_address: Optional[pulumi.Input[_builtins.str]] = ..., source_port_range: Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceSourcePortRangeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_address.setter
    def destination_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceDestinationPortRangeArgs]]:
        
        ...
    
    @destination_port_range.setter
    def destination_port_range(self, value: Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceDestinationPortRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddress")
    def source_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_address.setter
    def source_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceSourcePortRangeArgs]]:
        
        ...
    
    @source_port_range.setter
    def source_port_range(self, value: Optional[pulumi.Input[NetworkInsightsPathFilterAtSourceSourcePortRangeArgs]]): # -> None:
        ...
    


class NetworkInsightsPathFilterAtSourceDestinationPortRangeArgsDict(TypedDict):
    from_port: NotRequired[pulumi.Input[_builtins.int]]
    to_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsPathFilterAtSourceDestinationPortRangeArgs:
    def __init__(__self__, *, from_port: Optional[pulumi.Input[_builtins.int]] = ..., to_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInsightsPathFilterAtSourceSourcePortRangeArgsDict(TypedDict):
    from_port: NotRequired[pulumi.Input[_builtins.int]]
    to_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInsightsPathFilterAtSourceSourcePortRangeArgs:
    def __init__(__self__, *, from_port: Optional[pulumi.Input[_builtins.int]] = ..., to_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInterfaceAttachmentArgsDict(TypedDict):
    device_index: pulumi.Input[_builtins.int]
    instance: pulumi.Input[_builtins.str]
    attachment_id: NotRequired[pulumi.Input[_builtins.str]]
    network_card_index: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class NetworkInterfaceAttachmentArgs:
    def __init__(__self__, *, device_index: pulumi.Input[_builtins.int], instance: pulumi.Input[_builtins.str], attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., network_card_index: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @device_index.setter
    def device_index(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @network_card_index.setter
    def network_card_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class NetworkInterfacePermissionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInterfacePermissionTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PeeringConnectionOptionsAccepterArgsDict(TypedDict):
    allow_remote_vpc_dns_resolution: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class PeeringConnectionOptionsAccepterArgs:
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class PeeringConnectionOptionsRequesterArgsDict(TypedDict):
    allow_remote_vpc_dns_resolution: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class PeeringConnectionOptionsRequesterArgs:
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RouteTableRouteArgsDict(TypedDict):
    carrier_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    core_network_arn: NotRequired[pulumi.Input[_builtins.str]]
    destination_prefix_list_id: NotRequired[pulumi.Input[_builtins.str]]
    egress_only_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    local_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    nat_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    transit_gateway_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_peering_connection_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RouteTableRouteArgs:
    def __init__(__self__, *, carrier_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., core_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ..., egress_only_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., local_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierGatewayId")
    def carrier_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @carrier_gateway_id.setter
    def carrier_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_arn.setter
    def core_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_prefix_list_id.setter
    def destination_prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @egress_only_gateway_id.setter
    def egress_only_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @local_gateway_id.setter
    def local_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecondaryNetworkIpv4CidrBlockAssociationArgsDict(TypedDict):
    association_id: pulumi.Input[_builtins.str]
    cidr_block: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecondaryNetworkIpv4CidrBlockAssociationArgs:
    def __init__(__self__, *, association_id: pulumi.Input[_builtins.str], cidr_block: pulumi.Input[_builtins.str], state: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @association_id.setter
    def association_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecondaryNetworkTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecondaryNetworkTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecondarySubnetIpv4CidrBlockAssociationArgsDict(TypedDict):
    association_id: pulumi.Input[_builtins.str]
    cidr_block: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecondarySubnetIpv4CidrBlockAssociationArgs:
    def __init__(__self__, *, association_id: pulumi.Input[_builtins.str], cidr_block: pulumi.Input[_builtins.str], state: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @association_id.setter
    def association_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecondarySubnetTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecondarySubnetTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityGroupEgressArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    to_port: pulumi.Input[_builtins.int]
    cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix_list_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    self: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SecurityGroupEgressArgs:
    def __init__(__self__, *, from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], to_port: pulumi.Input[_builtins.int], cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., prefix_list_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., self: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cidr_blocks.setter
    def cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @prefix_list_ids.setter
    def prefix_list_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @self.setter
    def self(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SecurityGroupIngressArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    to_port: pulumi.Input[_builtins.int]
    cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix_list_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    self: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SecurityGroupIngressArgs:
    def __init__(__self__, *, from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], to_port: pulumi.Input[_builtins.int], cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., prefix_list_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., self: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cidr_blocks.setter
    def cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_cidr_blocks.setter
    def ipv6_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListIds")
    def prefix_list_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @prefix_list_ids.setter
    def prefix_list_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @self.setter
    def self(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SpotFleetRequestLaunchSpecificationArgsDict(TypedDict):
    ami: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    associate_public_ip_address: NotRequired[pulumi.Input[_builtins.bool]]
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    ebs_block_devices: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationEbsBlockDeviceArgsDict]]]]
    ebs_optimized: NotRequired[pulumi.Input[_builtins.bool]]
    ephemeral_block_devices: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationEphemeralBlockDeviceArgsDict]]]]
    iam_instance_profile: NotRequired[pulumi.Input[_builtins.str]]
    iam_instance_profile_arn: NotRequired[pulumi.Input[_builtins.str]]
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    placement_group: NotRequired[pulumi.Input[_builtins.str]]
    placement_tenancy: NotRequired[pulumi.Input[_builtins.str]]
    root_block_devices: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationRootBlockDeviceArgsDict]]]]
    spot_price: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    user_data: NotRequired[pulumi.Input[_builtins.str]]
    vpc_security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    weighted_capacity: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotFleetRequestLaunchSpecificationArgs:
    def __init__(__self__, *, ami: pulumi.Input[_builtins.str], instance_type: pulumi.Input[_builtins.str], associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationEbsBlockDeviceArgs]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationEphemeralBlockDeviceArgs]]]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., iam_instance_profile_arn: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., placement_tenancy: Optional[pulumi.Input[_builtins.str]] = ..., root_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationRootBlockDeviceArgs]]]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., weighted_capacity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ami(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @ami.setter
    def ami(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationEbsBlockDeviceArgs]]]]:
        ...
    
    @ebs_block_devices.setter
    def ebs_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationEbsBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationEphemeralBlockDeviceArgs]]]]:
        ...
    
    @ephemeral_block_devices.setter
    def ephemeral_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationEphemeralBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfileArn")
    def iam_instance_profile_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iam_instance_profile_arn.setter
    def iam_instance_profile_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @placement_group.setter
    def placement_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementTenancy")
    def placement_tenancy(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @placement_tenancy.setter
    def placement_tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootBlockDevices")
    def root_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationRootBlockDeviceArgs]]]]:
        ...
    
    @root_block_devices.setter
    def root_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationRootBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_price.setter
    def spot_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @weighted_capacity.setter
    def weighted_capacity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotFleetRequestLaunchSpecificationEbsBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotFleetRequestLaunchSpecificationEbsBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotFleetRequestLaunchSpecificationEphemeralBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    virtual_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class SpotFleetRequestLaunchSpecificationEphemeralBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], virtual_name: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @virtual_name.setter
    def virtual_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SpotFleetRequestLaunchSpecificationRootBlockDeviceArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotFleetRequestLaunchSpecificationRootBlockDeviceArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigArgsDict(TypedDict):
    launch_template_specification: pulumi.Input[SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecificationArgsDict]
    overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideArgsDict]]]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigArgs:
    def __init__(__self__, *, launch_template_specification: pulumi.Input[SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecificationArgs], overrides: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecification")
    def launch_template_specification(self) -> pulumi.Input[SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecificationArgs]:
        
        ...
    
    @launch_template_specification.setter
    def launch_template_specification(self, value: pulumi.Input[SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecificationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideArgs]]]]:
        
        ...
    
    @overrides.setter
    def overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideArgs]]]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecificationArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecificationArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideArgsDict(TypedDict):
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    instance_requirements: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsArgsDict]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.float]]
    spot_price: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    weighted_capacity: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideArgs:
    def __init__(__self__, *, availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., instance_requirements: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsArgs]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.float]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., weighted_capacity: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsArgs]]:
        
        ...
    
    @instance_requirements.setter
    def instance_requirements(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_price.setter
    def spot_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @weighted_capacity.setter
    def weighted_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsArgsDict(TypedDict):
    accelerator_count: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgsDict]]
    accelerator_manufacturers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accelerator_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accelerator_total_memory_mib: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgsDict]]
    accelerator_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bare_metal: NotRequired[pulumi.Input[_builtins.str]]
    baseline_ebs_bandwidth_mbps: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict]]
    burstable_performance: NotRequired[pulumi.Input[_builtins.str]]
    cpu_manufacturers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    instance_generations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    local_storage: NotRequired[pulumi.Input[_builtins.str]]
    local_storage_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    memory_gib_per_vcpu: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgsDict]]
    memory_mib: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgsDict]]
    network_bandwidth_gbps: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgsDict]]
    network_interface_count: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgsDict]]
    on_demand_max_price_percentage_over_lowest_price: NotRequired[pulumi.Input[_builtins.int]]
    require_hibernate_support: NotRequired[pulumi.Input[_builtins.bool]]
    spot_max_price_percentage_over_lowest_price: NotRequired[pulumi.Input[_builtins.int]]
    total_local_storage_gb: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgsDict]]
    vcpu_count: NotRequired[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgsDict]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsArgs:
    def __init__(__self__, *, accelerator_count: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgs]] = ..., accelerator_manufacturers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accelerator_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accelerator_total_memory_mib: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs]] = ..., accelerator_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bare_metal: Optional[pulumi.Input[_builtins.str]] = ..., baseline_ebs_bandwidth_mbps: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs]] = ..., burstable_performance: Optional[pulumi.Input[_builtins.str]] = ..., cpu_manufacturers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., excluded_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instance_generations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., local_storage: Optional[pulumi.Input[_builtins.str]] = ..., local_storage_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., memory_gib_per_vcpu: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgs]] = ..., memory_mib: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgs]] = ..., network_bandwidth_gbps: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgs]] = ..., network_interface_count: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgs]] = ..., on_demand_max_price_percentage_over_lowest_price: Optional[pulumi.Input[_builtins.int]] = ..., require_hibernate_support: Optional[pulumi.Input[_builtins.bool]] = ..., spot_max_price_percentage_over_lowest_price: Optional[pulumi.Input[_builtins.int]] = ..., total_local_storage_gb: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgs]] = ..., vcpu_count: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgs]]:
        
        ...
    
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_manufacturers.setter
    def accelerator_manufacturers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_names.setter
    def accelerator_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs]]:
        
        ...
    
    @accelerator_total_memory_mib.setter
    def accelerator_total_memory_mib(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accelerator_types.setter
    def accelerator_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_instance_types.setter
    def allowed_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bare_metal.setter
    def bare_metal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs]]:
        
        ...
    
    @baseline_ebs_bandwidth_mbps.setter
    def baseline_ebs_bandwidth_mbps(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @burstable_performance.setter
    def burstable_performance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cpu_manufacturers.setter
    def cpu_manufacturers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_instance_types.setter
    def excluded_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_generations.setter
    def instance_generations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @local_storage.setter
    def local_storage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @local_storage_types.setter
    def local_storage_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgs]]:
        
        ...
    
    @memory_gib_per_vcpu.setter
    def memory_gib_per_vcpu(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgs]]:
        
        ...
    
    @memory_mib.setter
    def memory_mib(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgs]]:
        
        ...
    
    @network_bandwidth_gbps.setter
    def network_bandwidth_gbps(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgs]]:
        
        ...
    
    @network_interface_count.setter
    def network_interface_count(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @on_demand_max_price_percentage_over_lowest_price.setter
    def on_demand_max_price_percentage_over_lowest_price(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_hibernate_support.setter
    def require_hibernate_support(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @spot_max_price_percentage_over_lowest_price.setter
    def spot_max_price_percentage_over_lowest_price(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGb")
    def total_local_storage_gb(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgs]]:
        
        ...
    
    @total_local_storage_gb.setter
    def total_local_storage_gb(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgs]]:
        
        ...
    
    @vcpu_count.setter
    def vcpu_count(self, value: Optional[pulumi.Input[SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgs]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorCountArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryGibPerVcpuArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsMemoryMibArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkBandwidthGbpsArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsNetworkInterfaceCountArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsTotalLocalStorageGbArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpotFleetRequestLaunchTemplateConfigOverrideInstanceRequirementsVcpuCountArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpotFleetRequestSpotMaintenanceStrategiesArgsDict(TypedDict):
    capacity_rebalance: NotRequired[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalanceArgsDict]]


@pulumi.input_type
class SpotFleetRequestSpotMaintenanceStrategiesArgs:
    def __init__(__self__, *, capacity_rebalance: Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalanceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityRebalance")
    def capacity_rebalance(self) -> Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalanceArgs]]:
        
        ...
    
    @capacity_rebalance.setter
    def capacity_rebalance(self, value: Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalanceArgs]]): # -> None:
        ...
    


class SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalanceArgsDict(TypedDict):
    replacement_strategy: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotFleetRequestSpotMaintenanceStrategiesCapacityRebalanceArgs:
    def __init__(__self__, *, replacement_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementStrategy")
    def replacement_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replacement_strategy.setter
    def replacement_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestCapacityReservationSpecificationArgsDict(TypedDict):
    capacity_reservation_preference: NotRequired[pulumi.Input[_builtins.str]]
    capacity_reservation_target: NotRequired[pulumi.Input[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetArgsDict]]


@pulumi.input_type
class SpotInstanceRequestCapacityReservationSpecificationArgs:
    def __init__(__self__, *, capacity_reservation_preference: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_target: Optional[pulumi.Input[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_preference.setter
    def capacity_reservation_preference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationTarget")
    def capacity_reservation_target(self) -> Optional[pulumi.Input[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetArgs]]:
        
        ...
    
    @capacity_reservation_target.setter
    def capacity_reservation_target(self, value: Optional[pulumi.Input[SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetArgs]]): # -> None:
        ...
    


class SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetArgsDict(TypedDict):
    capacity_reservation_id: NotRequired[pulumi.Input[_builtins.str]]
    capacity_reservation_resource_group_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestCapacityReservationSpecificationCapacityReservationTargetArgs:
    def __init__(__self__, *, capacity_reservation_id: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationId")
    def capacity_reservation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_id.setter
    def capacity_reservation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArn")
    def capacity_reservation_resource_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_resource_group_arn.setter
    def capacity_reservation_resource_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestCpuOptionsArgsDict(TypedDict):
    amd_sev_snp: NotRequired[pulumi.Input[_builtins.str]]
    core_count: NotRequired[pulumi.Input[_builtins.int]]
    nested_virtualization: NotRequired[pulumi.Input[_builtins.str]]
    threads_per_core: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpotInstanceRequestCpuOptionsArgs:
    def __init__(__self__, *, amd_sev_snp: Optional[pulumi.Input[_builtins.str]] = ..., core_count: Optional[pulumi.Input[_builtins.int]] = ..., nested_virtualization: Optional[pulumi.Input[_builtins.str]] = ..., threads_per_core: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amdSevSnp")
    def amd_sev_snp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amd_sev_snp.setter
    def amd_sev_snp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @core_count.setter
    def core_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestedVirtualization")
    def nested_virtualization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nested_virtualization.setter
    def nested_virtualization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @threads_per_core.setter
    def threads_per_core(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpotInstanceRequestCreditSpecificationArgsDict(TypedDict):
    cpu_credits: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestCreditSpecificationArgs:
    def __init__(__self__, *, cpu_credits: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu_credits.setter
    def cpu_credits(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestEbsBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags_all: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_id: NotRequired[pulumi.Input[_builtins.str]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestEbsBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_id: Optional[pulumi.Input[_builtins.str]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestEnclaveOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SpotInstanceRequestEnclaveOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SpotInstanceRequestEphemeralBlockDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    no_device: NotRequired[pulumi.Input[_builtins.bool]]
    virtual_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestEphemeralBlockDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], no_device: Optional[pulumi.Input[_builtins.bool]] = ..., virtual_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @no_device.setter
    def no_device(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_name.setter
    def virtual_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestLaunchTemplateArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestLaunchTemplateArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestMaintenanceOptionsArgsDict(TypedDict):
    auto_recovery: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestMaintenanceOptionsArgs:
    def __init__(__self__, *, auto_recovery: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRecovery")
    def auto_recovery(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_recovery.setter
    def auto_recovery(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestMetadataOptionsArgsDict(TypedDict):
    http_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    http_protocol_ipv6: NotRequired[pulumi.Input[_builtins.str]]
    http_put_response_hop_limit: NotRequired[pulumi.Input[_builtins.int]]
    http_tokens: NotRequired[pulumi.Input[_builtins.str]]
    instance_metadata_tags: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestMetadataOptionsArgs:
    def __init__(__self__, *, http_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., http_protocol_ipv6: Optional[pulumi.Input[_builtins.str]] = ..., http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ..., http_tokens: Optional[pulumi.Input[_builtins.str]] = ..., instance_metadata_tags: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_endpoint.setter
    def http_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProtocolIpv6")
    def http_protocol_ipv6(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_protocol_ipv6.setter
    def http_protocol_ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_tokens.setter
    def http_tokens(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMetadataTags")
    def instance_metadata_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_metadata_tags.setter
    def instance_metadata_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestNetworkInterfaceArgsDict(TypedDict):
    device_index: pulumi.Input[_builtins.int]
    network_interface_id: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    network_card_index: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpotInstanceRequestNetworkInterfaceArgs:
    def __init__(__self__, *, device_index: pulumi.Input[_builtins.int], network_interface_id: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., network_card_index: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @device_index.setter
    def device_index(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @network_card_index.setter
    def network_card_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpotInstanceRequestPrimaryNetworkInterfaceArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestPrimaryNetworkInterfaceArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestPrivateDnsNameOptionsArgsDict(TypedDict):
    enable_resource_name_dns_a_record: NotRequired[pulumi.Input[_builtins.bool]]
    enable_resource_name_dns_aaaa_record: NotRequired[pulumi.Input[_builtins.bool]]
    hostname_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestPrivateDnsNameOptionsArgs:
    def __init__(__self__, *, enable_resource_name_dns_a_record: Optional[pulumi.Input[_builtins.bool]] = ..., enable_resource_name_dns_aaaa_record: Optional[pulumi.Input[_builtins.bool]] = ..., hostname_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecord")
    def enable_resource_name_dns_a_record(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_a_record.setter
    def enable_resource_name_dns_a_record(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecord")
    def enable_resource_name_dns_aaaa_record(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_aaaa_record.setter
    def enable_resource_name_dns_aaaa_record(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameType")
    def hostname_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hostname_type.setter
    def hostname_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestRootBlockDeviceArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags_all: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_id: NotRequired[pulumi.Input[_builtins.str]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestRootBlockDeviceArgs:
    def __init__(__self__, *, delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_id: Optional[pulumi.Input[_builtins.str]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotInstanceRequestSecondaryNetworkInterfaceArgsDict(TypedDict):
    network_card_index: pulumi.Input[_builtins.int]
    secondary_subnet_id: pulumi.Input[_builtins.str]
    delete_on_termination: NotRequired[pulumi.Input[_builtins.bool]]
    device_index: NotRequired[pulumi.Input[_builtins.int]]
    interface_type: NotRequired[pulumi.Input[_builtins.str]]
    mac_address: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address_count: NotRequired[pulumi.Input[_builtins.int]]
    private_ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secondary_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    secondary_network_id: NotRequired[pulumi.Input[_builtins.str]]
    source_dest_check: NotRequired[pulumi.Input[_builtins.bool]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotInstanceRequestSecondaryNetworkInterfaceArgs:
    def __init__(__self__, *, network_card_index: pulumi.Input[_builtins.int], secondary_subnet_id: pulumi.Input[_builtins.str], delete_on_termination: Optional[pulumi.Input[_builtins.bool]] = ..., device_index: Optional[pulumi.Input[_builtins.int]] = ..., interface_type: Optional[pulumi.Input[_builtins.str]] = ..., mac_address: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address_count: Optional[pulumi.Input[_builtins.int]] = ..., private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secondary_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., secondary_network_id: Optional[pulumi.Input[_builtins.str]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @network_card_index.setter
    def network_card_index(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondarySubnetId")
    def secondary_subnet_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secondary_subnet_id.setter
    def secondary_subnet_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @device_index.setter
    def device_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface_type.setter
    def interface_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddressCount")
    def private_ip_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @private_ip_address_count.setter
    def private_ip_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_ip_addresses.setter
    def private_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInterfaceId")
    def secondary_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secondary_interface_id.setter
    def secondary_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkId")
    def secondary_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secondary_network_id.setter
    def secondary_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @source_dest_check.setter
    def source_dest_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TrafficMirrorFilterRuleDestinationPortRangeArgsDict(TypedDict):
    from_port: NotRequired[pulumi.Input[_builtins.int]]
    to_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TrafficMirrorFilterRuleDestinationPortRangeArgs:
    def __init__(__self__, *, from_port: Optional[pulumi.Input[_builtins.int]] = ..., to_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TrafficMirrorFilterRuleSourcePortRangeArgsDict(TypedDict):
    from_port: NotRequired[pulumi.Input[_builtins.int]]
    to_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TrafficMirrorFilterRuleSourcePortRangeArgs:
    def __init__(__self__, *, from_port: Optional[pulumi.Input[_builtins.int]] = ..., to_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VpcBlockPublicAccessExclusionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcBlockPublicAccessExclusionTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcBlockPublicAccessOptionsTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcBlockPublicAccessOptionsTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsArgsDict(TypedDict):
    egress_only_internet_gateway: pulumi.Input[VpcEncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgsDict]
    elastic_file_system: pulumi.Input[VpcEncryptionControlResourceExclusionsElasticFileSystemArgsDict]
    internet_gateway: pulumi.Input[VpcEncryptionControlResourceExclusionsInternetGatewayArgsDict]
    lambda_: pulumi.Input[VpcEncryptionControlResourceExclusionsLambdaArgsDict]
    nat_gateway: pulumi.Input[VpcEncryptionControlResourceExclusionsNatGatewayArgsDict]
    virtual_private_gateway: pulumi.Input[VpcEncryptionControlResourceExclusionsVirtualPrivateGatewayArgsDict]
    vpc_lattice: pulumi.Input[VpcEncryptionControlResourceExclusionsVpcLatticeArgsDict]
    vpc_peering: pulumi.Input[VpcEncryptionControlResourceExclusionsVpcPeeringArgsDict]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsArgs:
    def __init__(__self__, *, egress_only_internet_gateway: pulumi.Input[VpcEncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgs], elastic_file_system: pulumi.Input[VpcEncryptionControlResourceExclusionsElasticFileSystemArgs], internet_gateway: pulumi.Input[VpcEncryptionControlResourceExclusionsInternetGatewayArgs], lambda_: pulumi.Input[VpcEncryptionControlResourceExclusionsLambdaArgs], nat_gateway: pulumi.Input[VpcEncryptionControlResourceExclusionsNatGatewayArgs], virtual_private_gateway: pulumi.Input[VpcEncryptionControlResourceExclusionsVirtualPrivateGatewayArgs], vpc_lattice: pulumi.Input[VpcEncryptionControlResourceExclusionsVpcLatticeArgs], vpc_peering: pulumi.Input[VpcEncryptionControlResourceExclusionsVpcPeeringArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGateway")
    def egress_only_internet_gateway(self) -> pulumi.Input[VpcEncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgs]:
        
        ...
    
    @egress_only_internet_gateway.setter
    def egress_only_internet_gateway(self, value: pulumi.Input[VpcEncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticFileSystem")
    def elastic_file_system(self) -> pulumi.Input[VpcEncryptionControlResourceExclusionsElasticFileSystemArgs]:
        
        ...
    
    @elastic_file_system.setter
    def elastic_file_system(self, value: pulumi.Input[VpcEncryptionControlResourceExclusionsElasticFileSystemArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateway")
    def internet_gateway(self) -> pulumi.Input[VpcEncryptionControlResourceExclusionsInternetGatewayArgs]:
        
        ...
    
    @internet_gateway.setter
    def internet_gateway(self, value: pulumi.Input[VpcEncryptionControlResourceExclusionsInternetGatewayArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> pulumi.Input[VpcEncryptionControlResourceExclusionsLambdaArgs]:
        
        ...
    
    @lambda_.setter
    def lambda_(self, value: pulumi.Input[VpcEncryptionControlResourceExclusionsLambdaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> pulumi.Input[VpcEncryptionControlResourceExclusionsNatGatewayArgs]:
        
        ...
    
    @nat_gateway.setter
    def nat_gateway(self, value: pulumi.Input[VpcEncryptionControlResourceExclusionsNatGatewayArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualPrivateGateway")
    def virtual_private_gateway(self) -> pulumi.Input[VpcEncryptionControlResourceExclusionsVirtualPrivateGatewayArgs]:
        
        ...
    
    @virtual_private_gateway.setter
    def virtual_private_gateway(self, value: pulumi.Input[VpcEncryptionControlResourceExclusionsVirtualPrivateGatewayArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLattice")
    def vpc_lattice(self) -> pulumi.Input[VpcEncryptionControlResourceExclusionsVpcLatticeArgs]:
        
        ...
    
    @vpc_lattice.setter
    def vpc_lattice(self, value: pulumi.Input[VpcEncryptionControlResourceExclusionsVpcLatticeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeering")
    def vpc_peering(self) -> pulumi.Input[VpcEncryptionControlResourceExclusionsVpcPeeringArgs]:
        
        ...
    
    @vpc_peering.setter
    def vpc_peering(self, value: pulumi.Input[VpcEncryptionControlResourceExclusionsVpcPeeringArgs]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsEgressOnlyInternetGatewayArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsElasticFileSystemArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsElasticFileSystemArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsInternetGatewayArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsInternetGatewayArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsLambdaArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsLambdaArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsNatGatewayArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsNatGatewayArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsVirtualPrivateGatewayArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsVirtualPrivateGatewayArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsVpcLatticeArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsVpcLatticeArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcEncryptionControlResourceExclusionsVpcPeeringArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    state_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcEncryptionControlResourceExclusionsVpcPeeringArgs:
    def __init__(__self__, *, state: pulumi.Input[_builtins.str], state_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcEncryptionControlTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcEncryptionControlTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcEndpointDnsEntryArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    hosted_zone_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcEndpointDnsEntryArgs:
    def __init__(__self__, *, dns_name: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcEndpointDnsOptionsArgsDict(TypedDict):
    dns_record_ip_type: NotRequired[pulumi.Input[_builtins.str]]
    private_dns_only_for_inbound_resolver_endpoint: NotRequired[pulumi.Input[_builtins.bool]]
    private_dns_preference: NotRequired[pulumi.Input[_builtins.str]]
    private_dns_specified_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VpcEndpointDnsOptionsArgs:
    def __init__(__self__, *, dns_record_ip_type: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_only_for_inbound_resolver_endpoint: Optional[pulumi.Input[_builtins.bool]] = ..., private_dns_preference: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_specified_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsRecordIpType")
    def dns_record_ip_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_record_ip_type.setter
    def dns_record_ip_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsOnlyForInboundResolverEndpoint")
    def private_dns_only_for_inbound_resolver_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @private_dns_only_for_inbound_resolver_endpoint.setter
    def private_dns_only_for_inbound_resolver_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsPreference")
    def private_dns_preference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_preference.setter
    def private_dns_preference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsSpecifiedDomains")
    def private_dns_specified_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_dns_specified_domains.setter
    def private_dns_specified_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VpcEndpointServicePrivateDnsNameConfigurationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcEndpointServicePrivateDnsNameConfigurationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcEndpointSubnetConfigurationArgsDict(TypedDict):
    ipv4: NotRequired[pulumi.Input[_builtins.str]]
    ipv6: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcEndpointSubnetConfigurationArgs:
    def __init__(__self__, *, ipv4: Optional[pulumi.Input[_builtins.str]] = ..., ipv6: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ipv4(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv4.setter
    def ipv4(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ipv6(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6.setter
    def ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcIpamOperatingRegionArgsDict(TypedDict):
    region_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcIpamOperatingRegionArgs:
    def __init__(__self__, *, region_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcIpamPoolCidrCidrAuthorizationContextArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    signature: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcIpamPoolCidrCidrAuthorizationContextArgs:
    def __init__(__self__, *, message: Optional[pulumi.Input[_builtins.str]] = ..., signature: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def signature(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @signature.setter
    def signature(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcIpamPoolSourceResourceArgsDict(TypedDict):
    resource_id: pulumi.Input[_builtins.str]
    resource_owner: pulumi.Input[_builtins.str]
    resource_region: pulumi.Input[_builtins.str]
    resource_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcIpamPoolSourceResourceArgs:
    def __init__(__self__, *, resource_id: pulumi.Input[_builtins.str], resource_owner: pulumi.Input[_builtins.str], resource_region: pulumi.Input[_builtins.str], resource_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_owner.setter
    def resource_owner(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRegion")
    def resource_region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_region.setter
    def resource_region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcIpamResourceDiscoveryOperatingRegionArgsDict(TypedDict):
    region_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcIpamResourceDiscoveryOperatingRegionArgs:
    def __init__(__self__, *, region_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgsDict(TypedDict):
    organizations_entity_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs:
    def __init__(__self__, *, organizations_entity_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationsEntityPath")
    def organizations_entity_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @organizations_entity_path.setter
    def organizations_entity_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VpcPeeringConnectionAccepterArgsDict(TypedDict):
    allow_remote_vpc_dns_resolution: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VpcPeeringConnectionAccepterArgs:
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VpcPeeringConnectionAccepterAccepterArgsDict(TypedDict):
    allow_remote_vpc_dns_resolution: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VpcPeeringConnectionAccepterAccepterArgs:
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VpcPeeringConnectionAccepterRequesterArgsDict(TypedDict):
    allow_remote_vpc_dns_resolution: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VpcPeeringConnectionAccepterRequesterArgs:
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VpcPeeringConnectionRequesterArgsDict(TypedDict):
    allow_remote_vpc_dns_resolution: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VpcPeeringConnectionRequesterArgs:
    def __init__(__self__, *, allow_remote_vpc_dns_resolution: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VpnConnectionRouteArgsDict(TypedDict):
    destination_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpnConnectionRouteArgs:
    def __init__(__self__, *, destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_cidr_block.setter
    def destination_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpnConnectionTunnel1LogOptionsArgsDict(TypedDict):
    cloudwatch_log_options: NotRequired[pulumi.Input[VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsArgsDict]]


@pulumi.input_type
class VpnConnectionTunnel1LogOptionsArgs:
    def __init__(__self__, *, cloudwatch_log_options: Optional[pulumi.Input[VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogOptions")
    def cloudwatch_log_options(self) -> Optional[pulumi.Input[VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsArgs]]:
        
        ...
    
    @cloudwatch_log_options.setter
    def cloudwatch_log_options(self, value: Optional[pulumi.Input[VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsArgs]]): # -> None:
        ...
    


class VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsArgsDict(TypedDict):
    bgp_log_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    bgp_log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    bgp_log_output_format: NotRequired[pulumi.Input[_builtins.str]]
    log_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    log_output_format: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsArgs:
    def __init__(__self__, *, bgp_log_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., bgp_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., bgp_log_output_format: Optional[pulumi.Input[_builtins.str]] = ..., log_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., log_output_format: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogEnabled")
    def bgp_log_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bgp_log_enabled.setter
    def bgp_log_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogGroupArn")
    def bgp_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_log_group_arn.setter
    def bgp_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogOutputFormat")
    def bgp_log_output_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_log_output_format.setter
    def bgp_log_output_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logEnabled")
    def log_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_enabled.setter
    def log_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_arn.setter
    def log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logOutputFormat")
    def log_output_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_output_format.setter
    def log_output_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpnConnectionTunnel2LogOptionsArgsDict(TypedDict):
    cloudwatch_log_options: NotRequired[pulumi.Input[VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsArgsDict]]


@pulumi.input_type
class VpnConnectionTunnel2LogOptionsArgs:
    def __init__(__self__, *, cloudwatch_log_options: Optional[pulumi.Input[VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogOptions")
    def cloudwatch_log_options(self) -> Optional[pulumi.Input[VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsArgs]]:
        
        ...
    
    @cloudwatch_log_options.setter
    def cloudwatch_log_options(self, value: Optional[pulumi.Input[VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsArgs]]): # -> None:
        ...
    


class VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsArgsDict(TypedDict):
    bgp_log_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    bgp_log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    bgp_log_output_format: NotRequired[pulumi.Input[_builtins.str]]
    log_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    log_output_format: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsArgs:
    def __init__(__self__, *, bgp_log_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., bgp_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., bgp_log_output_format: Optional[pulumi.Input[_builtins.str]] = ..., log_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., log_output_format: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogEnabled")
    def bgp_log_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bgp_log_enabled.setter
    def bgp_log_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogGroupArn")
    def bgp_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_log_group_arn.setter
    def bgp_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLogOutputFormat")
    def bgp_log_output_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_log_output_format.setter
    def bgp_log_output_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logEnabled")
    def log_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_enabled.setter
    def log_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_arn.setter
    def log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logOutputFormat")
    def log_output_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_output_format.setter
    def log_output_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpnConnectionVgwTelemetryArgsDict(TypedDict):
    accepted_route_count: NotRequired[pulumi.Input[_builtins.int]]
    certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    last_status_change: NotRequired[pulumi.Input[_builtins.str]]
    outside_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    status_message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpnConnectionVgwTelemetryArgs:
    def __init__(__self__, *, accepted_route_count: Optional[pulumi.Input[_builtins.int]] = ..., certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_status_change: Optional[pulumi.Input[_builtins.str]] = ..., outside_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptedRouteCount")
    def accepted_route_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @accepted_route_count.setter
    def accepted_route_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStatusChange")
    def last_status_change(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_status_change.setter
    def last_status_change(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outsideIpAddress")
    def outside_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outside_ip_address.setter
    def outside_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_message.setter
    def status_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GetAmiFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetAmiFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetAmiIdsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetAmiIdsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetCoipPoolFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetCoipPoolFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetCoipPoolsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetCoipPoolsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetCustomerGatewayFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetCustomerGatewayFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetDedicatedHostFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetDedicatedHostFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetEipsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetEipsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetElasticIpFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetElasticIpFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetInstanceFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetInstanceFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetInstanceTypeOfferingFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetInstanceTypeOfferingFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetInstanceTypeOfferingsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetInstanceTypeOfferingsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetInstanceTypesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetInstanceTypesFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetInstancesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetInstancesFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetInternetGatewayFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetInternetGatewayFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetKeyPairFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetKeyPairFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetLaunchTemplateFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetLaunchTemplateFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetLocalGatewayFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetLocalGatewayFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetLocalGatewayRouteTableFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetLocalGatewayRouteTableFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetLocalGatewayRouteTablesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetLocalGatewayRouteTablesFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetLocalGatewayVirtualInterfaceFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetLocalGatewayVirtualInterfaceFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetLocalGatewayVirtualInterfaceGroupFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetLocalGatewayVirtualInterfaceGroupFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetLocalGatewayVirtualInterfaceGroupsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetLocalGatewayVirtualInterfaceGroupsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetLocalGatewaysFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetLocalGatewaysFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetManagedPrefixListFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetManagedPrefixListFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetManagedPrefixListsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetManagedPrefixListsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetNatGatewayFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetNatGatewayFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetNatGatewaysFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetNatGatewaysFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetNetworkAclsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetNetworkAclsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetNetworkInsightsAnalysisFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetNetworkInsightsAnalysisFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetNetworkInsightsPathFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetNetworkInsightsPathFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetNetworkInterfaceFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetNetworkInterfaceFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetNetworkInterfacesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetNetworkInterfacesFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetPrefixListFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetPrefixListFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetPublicIpv4PoolsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetPublicIpv4PoolsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetRouteTableFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetRouteTableFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetRouteTablesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetRouteTablesFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetSecurityGroupFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetSecurityGroupFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetSecurityGroupsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetSecurityGroupsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetSpotPriceFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetSpotPriceFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetSubnetFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetSubnetFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetSubnetsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetSubnetsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetTransitGatewayRouteTablesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetTransitGatewayRouteTablesFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcDhcpOptionsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcDhcpOptionsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcEndpointFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcEndpointFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcEndpointServiceFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcEndpointServiceFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcIpamPoolCidrsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcIpamPoolCidrsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcIpamPoolFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcIpamPoolFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcIpamPoolsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcIpamPoolsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcIpamsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcIpamsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcPeeringConnectionFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcPeeringConnectionFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcPeeringConnectionsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcPeeringConnectionsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpcsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpcsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpnConnectionFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpnConnectionFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVpnGatewayFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVpnGatewayFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


