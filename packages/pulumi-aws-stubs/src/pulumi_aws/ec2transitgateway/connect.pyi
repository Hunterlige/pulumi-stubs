

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectArgs', 'Connect']
@pulumi.input_type
class ConnectArgs:
    def __init__(__self__, *, transit_gateway_id: pulumi.Input[_builtins.str], transport_attachment_id: pulumi.Input[_builtins.str], protocol: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_default_route_table_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_default_route_table_propagation: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportAttachmentId")
    def transport_attachment_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transport_attachment_id.setter
    def transport_attachment_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class _ConnectState:
    def __init__(__self__, *, protocol: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_default_route_table_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_default_route_table_propagation: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., transport_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="transportAttachmentId")
    def transport_attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transport_attachment_id.setter
    def transport_attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2transitgateway/connect:Connect")
class Connect(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_default_route_table_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_default_route_table_propagation: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., transport_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_default_route_table_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_default_route_table_propagation: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., transport_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Connect:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="transportAttachmentId")
    def transport_attachment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


