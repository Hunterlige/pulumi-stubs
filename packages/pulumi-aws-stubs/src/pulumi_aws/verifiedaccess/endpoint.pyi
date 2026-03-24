

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
__all__ = ['EndpointArgs', 'Endpoint']
@pulumi.input_type
class EndpointArgs:
    def __init__(__self__, *, attachment_type: pulumi.Input[_builtins.str], endpoint_type: pulumi.Input[_builtins.str], verified_access_group_id: pulumi.Input[_builtins.str], application_domain: Optional[pulumi.Input[_builtins.str]] = ..., cidr_options: Optional[pulumi.Input[EndpointCidrOptionsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_domain_prefix: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer_options: Optional[pulumi.Input[EndpointLoadBalancerOptionsArgs]] = ..., network_interface_options: Optional[pulumi.Input[EndpointNetworkInterfaceOptionsArgs]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., rds_options: Optional[pulumi.Input[EndpointRdsOptionsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sse_specification: Optional[pulumi.Input[EndpointSseSpecificationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @attachment_type.setter
    def attachment_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedAccessGroupId")
    def verified_access_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @verified_access_group_id.setter
    def verified_access_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationDomain")
    def application_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_domain.setter
    def application_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrOptions")
    def cidr_options(self) -> Optional[pulumi.Input[EndpointCidrOptionsArgs]]:
        
        ...
    
    @cidr_options.setter
    def cidr_options(self, value: Optional[pulumi.Input[EndpointCidrOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainCertificateArn")
    def domain_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_certificate_arn.setter
    def domain_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointDomainPrefix")
    def endpoint_domain_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_domain_prefix.setter
    def endpoint_domain_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerOptions")
    def load_balancer_options(self) -> Optional[pulumi.Input[EndpointLoadBalancerOptionsArgs]]:
        
        ...
    
    @load_balancer_options.setter
    def load_balancer_options(self, value: Optional[pulumi.Input[EndpointLoadBalancerOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceOptions")
    def network_interface_options(self) -> Optional[pulumi.Input[EndpointNetworkInterfaceOptionsArgs]]:
        
        ...
    
    @network_interface_options.setter
    def network_interface_options(self, value: Optional[pulumi.Input[EndpointNetworkInterfaceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdsOptions")
    def rds_options(self) -> Optional[pulumi.Input[EndpointRdsOptionsArgs]]:
        ...
    
    @rds_options.setter
    def rds_options(self, value: Optional[pulumi.Input[EndpointRdsOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> Optional[pulumi.Input[EndpointSseSpecificationArgs]]:
        
        ...
    
    @sse_specification.setter
    def sse_specification(self, value: Optional[pulumi.Input[EndpointSseSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _EndpointState:
    def __init__(__self__, *, application_domain: Optional[pulumi.Input[_builtins.str]] = ..., attachment_type: Optional[pulumi.Input[_builtins.str]] = ..., cidr_options: Optional[pulumi.Input[EndpointCidrOptionsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., device_validation_domain: Optional[pulumi.Input[_builtins.str]] = ..., domain_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_domain: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_domain_prefix: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer_options: Optional[pulumi.Input[EndpointLoadBalancerOptionsArgs]] = ..., network_interface_options: Optional[pulumi.Input[EndpointNetworkInterfaceOptionsArgs]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., rds_options: Optional[pulumi.Input[EndpointRdsOptionsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sse_specification: Optional[pulumi.Input[EndpointSseSpecificationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., verified_access_group_id: Optional[pulumi.Input[_builtins.str]] = ..., verified_access_instance_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationDomain")
    def application_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_domain.setter
    def application_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attachment_type.setter
    def attachment_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrOptions")
    def cidr_options(self) -> Optional[pulumi.Input[EndpointCidrOptionsArgs]]:
        
        ...
    
    @cidr_options.setter
    def cidr_options(self, value: Optional[pulumi.Input[EndpointCidrOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceValidationDomain")
    def device_validation_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_validation_domain.setter
    def device_validation_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainCertificateArn")
    def domain_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_certificate_arn.setter
    def domain_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointDomain")
    def endpoint_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_domain.setter
    def endpoint_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointDomainPrefix")
    def endpoint_domain_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_domain_prefix.setter
    def endpoint_domain_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerOptions")
    def load_balancer_options(self) -> Optional[pulumi.Input[EndpointLoadBalancerOptionsArgs]]:
        
        ...
    
    @load_balancer_options.setter
    def load_balancer_options(self, value: Optional[pulumi.Input[EndpointLoadBalancerOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceOptions")
    def network_interface_options(self) -> Optional[pulumi.Input[EndpointNetworkInterfaceOptionsArgs]]:
        
        ...
    
    @network_interface_options.setter
    def network_interface_options(self, value: Optional[pulumi.Input[EndpointNetworkInterfaceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdsOptions")
    def rds_options(self) -> Optional[pulumi.Input[EndpointRdsOptionsArgs]]:
        ...
    
    @rds_options.setter
    def rds_options(self, value: Optional[pulumi.Input[EndpointRdsOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> Optional[pulumi.Input[EndpointSseSpecificationArgs]]:
        
        ...
    
    @sse_specification.setter
    def sse_specification(self, value: Optional[pulumi.Input[EndpointSseSpecificationArgs]]): # -> None:
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
    @pulumi.getter(name="verifiedAccessGroupId")
    def verified_access_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @verified_access_group_id.setter
    def verified_access_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedAccessInstanceId")
    def verified_access_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @verified_access_instance_id.setter
    def verified_access_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:verifiedaccess/endpoint:Endpoint")
class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_domain: Optional[pulumi.Input[_builtins.str]] = ..., attachment_type: Optional[pulumi.Input[_builtins.str]] = ..., cidr_options: Optional[pulumi.Input[Union[EndpointCidrOptionsArgs, EndpointCidrOptionsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_domain_prefix: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer_options: Optional[pulumi.Input[Union[EndpointLoadBalancerOptionsArgs, EndpointLoadBalancerOptionsArgsDict]]] = ..., network_interface_options: Optional[pulumi.Input[Union[EndpointNetworkInterfaceOptionsArgs, EndpointNetworkInterfaceOptionsArgsDict]]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., rds_options: Optional[pulumi.Input[Union[EndpointRdsOptionsArgs, EndpointRdsOptionsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sse_specification: Optional[pulumi.Input[Union[EndpointSseSpecificationArgs, EndpointSseSpecificationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., verified_access_group_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_domain: Optional[pulumi.Input[_builtins.str]] = ..., attachment_type: Optional[pulumi.Input[_builtins.str]] = ..., cidr_options: Optional[pulumi.Input[Union[EndpointCidrOptionsArgs, EndpointCidrOptionsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., device_validation_domain: Optional[pulumi.Input[_builtins.str]] = ..., domain_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_domain: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_domain_prefix: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer_options: Optional[pulumi.Input[Union[EndpointLoadBalancerOptionsArgs, EndpointLoadBalancerOptionsArgsDict]]] = ..., network_interface_options: Optional[pulumi.Input[Union[EndpointNetworkInterfaceOptionsArgs, EndpointNetworkInterfaceOptionsArgsDict]]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., rds_options: Optional[pulumi.Input[Union[EndpointRdsOptionsArgs, EndpointRdsOptionsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sse_specification: Optional[pulumi.Input[Union[EndpointSseSpecificationArgs, EndpointSseSpecificationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., verified_access_group_id: Optional[pulumi.Input[_builtins.str]] = ..., verified_access_instance_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Endpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationDomain")
    def application_domain(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrOptions")
    def cidr_options(self) -> pulumi.Output[Optional[outputs.EndpointCidrOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceValidationDomain")
    def device_validation_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainCertificateArn")
    def domain_certificate_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointDomain")
    def endpoint_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointDomainPrefix")
    def endpoint_domain_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerOptions")
    def load_balancer_options(self) -> pulumi.Output[Optional[outputs.EndpointLoadBalancerOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceOptions")
    def network_interface_options(self) -> pulumi.Output[Optional[outputs.EndpointNetworkInterfaceOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdsOptions")
    def rds_options(self) -> pulumi.Output[Optional[outputs.EndpointRdsOptions]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> pulumi.Output[outputs.EndpointSseSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedAccessGroupId")
    def verified_access_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedAccessInstanceId")
    def verified_access_instance_id(self) -> pulumi.Output[_builtins.str]:
        ...
    


