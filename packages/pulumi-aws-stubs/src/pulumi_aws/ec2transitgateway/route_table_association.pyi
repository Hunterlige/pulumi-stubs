

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RouteTableAssociationArgs', 'RouteTableAssociation']
@pulumi.input_type
class RouteTableAssociationArgs:
    def __init__(__self__, *, transit_gateway_attachment_id: pulumi.Input[_builtins.str], transit_gateway_route_table_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., replace_existing_association: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transit_gateway_route_table_id.setter
    def transit_gateway_route_table_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceExistingAssociation")
    def replace_existing_association(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replace_existing_association.setter
    def replace_existing_association(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _RouteTableAssociationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., replace_existing_association: Optional[pulumi.Input[_builtins.bool]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceExistingAssociation")
    def replace_existing_association(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replace_existing_association.setter
    def replace_existing_association(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_route_table_id.setter
    def transit_gateway_route_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RouteTableAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_existing_association: Optional[pulumi.Input[_builtins.bool]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RouteTableAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_existing_association: Optional[pulumi.Input[_builtins.bool]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...) -> RouteTableAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceExistingAssociation")
    def replace_existing_association(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


