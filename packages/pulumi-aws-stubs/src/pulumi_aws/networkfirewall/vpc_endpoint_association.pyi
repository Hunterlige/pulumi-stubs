

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
__all__ = ['VpcEndpointAssociationArgs', 'VpcEndpointAssociation']
@pulumi.input_type
class VpcEndpointAssociationArgs:
    def __init__(__self__, *, firewall_arn: pulumi.Input[_builtins.str], subnet_mapping: pulumi.Input[VpcEndpointAssociationSubnetMappingArgs], vpc_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[VpcEndpointAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallArn")
    def firewall_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @firewall_arn.setter
    def firewall_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMapping")
    def subnet_mapping(self) -> pulumi.Input[VpcEndpointAssociationSubnetMappingArgs]:
        
        ...
    
    @subnet_mapping.setter
    def subnet_mapping(self, value: pulumi.Input[VpcEndpointAssociationSubnetMappingArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[VpcEndpointAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[VpcEndpointAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcEndpointAssociationState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., firewall_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_mapping: Optional[pulumi.Input[VpcEndpointAssociationSubnetMappingArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[VpcEndpointAssociationTimeoutsArgs]] = ..., vpc_endpoint_association_arn: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_association_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_association_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[VpcEndpointAssociationVpcEndpointAssociationStatusArgs]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallArn")
    def firewall_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firewall_arn.setter
    def firewall_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMapping")
    def subnet_mapping(self) -> Optional[pulumi.Input[VpcEndpointAssociationSubnetMappingArgs]]:
        
        ...
    
    @subnet_mapping.setter
    def subnet_mapping(self, value: Optional[pulumi.Input[VpcEndpointAssociationSubnetMappingArgs]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[VpcEndpointAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[VpcEndpointAssociationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointAssociationArn")
    def vpc_endpoint_association_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_association_arn.setter
    def vpc_endpoint_association_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointAssociationId")
    def vpc_endpoint_association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_association_id.setter
    def vpc_endpoint_association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointAssociationStatuses")
    def vpc_endpoint_association_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VpcEndpointAssociationVpcEndpointAssociationStatusArgs]]]]:
        
        ...
    
    @vpc_endpoint_association_statuses.setter
    def vpc_endpoint_association_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VpcEndpointAssociationVpcEndpointAssociationStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VpcEndpointAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., firewall_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_mapping: Optional[pulumi.Input[Union[VpcEndpointAssociationSubnetMappingArgs, VpcEndpointAssociationSubnetMappingArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[VpcEndpointAssociationTimeoutsArgs, VpcEndpointAssociationTimeoutsArgsDict]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcEndpointAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., firewall_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_mapping: Optional[pulumi.Input[Union[VpcEndpointAssociationSubnetMappingArgs, VpcEndpointAssociationSubnetMappingArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[VpcEndpointAssociationTimeoutsArgs, VpcEndpointAssociationTimeoutsArgsDict]]] = ..., vpc_endpoint_association_arn: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_association_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_association_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VpcEndpointAssociationVpcEndpointAssociationStatusArgs, VpcEndpointAssociationVpcEndpointAssociationStatusArgsDict]]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> VpcEndpointAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallArn")
    def firewall_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMapping")
    def subnet_mapping(self) -> pulumi.Output[outputs.VpcEndpointAssociationSubnetMapping]:
        
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
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.VpcEndpointAssociationTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointAssociationArn")
    def vpc_endpoint_association_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointAssociationId")
    def vpc_endpoint_association_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointAssociationStatuses")
    def vpc_endpoint_association_statuses(self) -> pulumi.Output[Sequence[outputs.VpcEndpointAssociationVpcEndpointAssociationStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


