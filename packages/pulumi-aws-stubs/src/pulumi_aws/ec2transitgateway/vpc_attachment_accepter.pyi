

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpcAttachmentAccepterArgs', 'VpcAttachmentAccepter']
@pulumi.input_type
class VpcAttachmentAccepterArgs:
    def __init__(__self__, *, transit_gateway_attachment_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_default_route_table_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_default_route_table_propagation: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="transitGatewayDefaultRouteTableAssociation")
    def transit_gateway_default_route_table_association(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transit_gateway_default_route_table_association.setter
    def transit_gateway_default_route_table_association(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayDefaultRouteTablePropagation")
    def transit_gateway_default_route_table_propagation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transit_gateway_default_route_table_propagation.setter
    def transit_gateway_default_route_table_propagation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcAttachmentAccepterState:
    def __init__(__self__, *, appliance_mode_support: Optional[pulumi.Input[_builtins.str]] = ..., dns_support: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_support: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_referencing_support: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_default_route_table_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_default_route_table_propagation: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_owner_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applianceModeSupport")
    def appliance_mode_support(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @appliance_mode_support.setter
    def appliance_mode_support(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_support.setter
    def dns_support(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_support.setter
    def ipv6_support(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_group_referencing_support.setter
    def security_group_referencing_support(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayDefaultRouteTableAssociation")
    def transit_gateway_default_route_table_association(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transit_gateway_default_route_table_association.setter
    def transit_gateway_default_route_table_association(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayDefaultRouteTablePropagation")
    def transit_gateway_default_route_table_propagation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @transit_gateway_default_route_table_propagation.setter
    def transit_gateway_default_route_table_propagation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOwnerId")
    def vpc_owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_owner_id.setter
    def vpc_owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VpcAttachmentAccepter(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_default_route_table_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_default_route_table_propagation: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcAttachmentAccepterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., appliance_mode_support: Optional[pulumi.Input[_builtins.str]] = ..., dns_support: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_support: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_referencing_support: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_default_route_table_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_default_route_table_propagation: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_owner_id: Optional[pulumi.Input[_builtins.str]] = ...) -> VpcAttachmentAccepter:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applianceModeSupport")
    def appliance_mode_support(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayDefaultRouteTableAssociation")
    def transit_gateway_default_route_table_association(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayDefaultRouteTablePropagation")
    def transit_gateway_default_route_table_propagation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOwnerId")
    def vpc_owner_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


