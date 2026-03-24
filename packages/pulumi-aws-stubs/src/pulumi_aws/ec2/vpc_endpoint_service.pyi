

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpcEndpointServiceArgs', 'VpcEndpointService']
@pulumi.input_type
class VpcEndpointServiceArgs:
    def __init__(__self__, *, acceptance_required: pulumi.Input[_builtins.bool], allowed_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., gateway_load_balancer_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., network_load_balancer_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., supported_ip_address_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., supported_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptanceRequired")
    def acceptance_required(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @acceptance_required.setter
    def acceptance_required(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPrincipals")
    def allowed_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_principals.setter
    def allowed_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayLoadBalancerArns")
    def gateway_load_balancer_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @gateway_load_balancer_arns.setter
    def gateway_load_balancer_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkLoadBalancerArns")
    def network_load_balancer_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @network_load_balancer_arns.setter
    def network_load_balancer_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsName")
    def private_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_name.setter
    def private_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedIpAddressTypes")
    def supported_ip_address_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_ip_address_types.setter
    def supported_ip_address_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedRegions")
    def supported_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_regions.setter
    def supported_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcEndpointServiceState:
    def __init__(__self__, *, acceptance_required: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., base_endpoint_dns_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., gateway_load_balancer_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., manages_vpc_endpoints: Optional[pulumi.Input[_builtins.bool]] = ..., network_load_balancer_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_name_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[VpcEndpointServicePrivateDnsNameConfigurationArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., supported_ip_address_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., supported_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptanceRequired")
    def acceptance_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @acceptance_required.setter
    def acceptance_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPrincipals")
    def allowed_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_principals.setter
    def allowed_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseEndpointDnsNames")
    def base_endpoint_dns_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @base_endpoint_dns_names.setter
    def base_endpoint_dns_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayLoadBalancerArns")
    def gateway_load_balancer_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @gateway_load_balancer_arns.setter
    def gateway_load_balancer_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managesVpcEndpoints")
    def manages_vpc_endpoints(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @manages_vpc_endpoints.setter
    def manages_vpc_endpoints(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkLoadBalancerArns")
    def network_load_balancer_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @network_load_balancer_arns.setter
    def network_load_balancer_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsName")
    def private_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_name.setter
    def private_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameConfigurations")
    def private_dns_name_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VpcEndpointServicePrivateDnsNameConfigurationArgs]]]]:
        
        ...
    
    @private_dns_name_configurations.setter
    def private_dns_name_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VpcEndpointServicePrivateDnsNameConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedIpAddressTypes")
    def supported_ip_address_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_ip_address_types.setter
    def supported_ip_address_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedRegions")
    def supported_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_regions.setter
    def supported_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    


@pulumi.type_token("aws:ec2/vpcEndpointService:VpcEndpointService")
class VpcEndpointService(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., acceptance_required: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., gateway_load_balancer_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., network_load_balancer_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., supported_ip_address_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., supported_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcEndpointServiceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., acceptance_required: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., base_endpoint_dns_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., gateway_load_balancer_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., manages_vpc_endpoints: Optional[pulumi.Input[_builtins.bool]] = ..., network_load_balancer_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_name_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VpcEndpointServicePrivateDnsNameConfigurationArgs, VpcEndpointServicePrivateDnsNameConfigurationArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., service_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., supported_ip_address_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., supported_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> VpcEndpointService:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptanceRequired")
    def acceptance_required(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPrincipals")
    def allowed_principals(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseEndpointDnsNames")
    def base_endpoint_dns_names(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayLoadBalancerArns")
    def gateway_load_balancer_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managesVpcEndpoints")
    def manages_vpc_endpoints(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkLoadBalancerArns")
    def network_load_balancer_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsName")
    def private_dns_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameConfigurations")
    def private_dns_name_configurations(self) -> pulumi.Output[Sequence[outputs.VpcEndpointServicePrivateDnsNameConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedIpAddressTypes")
    def supported_ip_address_types(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedRegions")
    def supported_regions(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


