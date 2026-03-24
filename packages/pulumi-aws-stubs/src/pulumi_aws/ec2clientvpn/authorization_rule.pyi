

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthorizationRuleArgs', 'AuthorizationRule']
@pulumi.input_type
class AuthorizationRuleArgs:
    def __init__(__self__, *, client_vpn_endpoint_id: pulumi.Input[_builtins.str], target_network_cidr: pulumi.Input[_builtins.str], access_group_id: Optional[pulumi.Input[_builtins.str]] = ..., authorize_all_groups: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_vpn_endpoint_id.setter
    def client_vpn_endpoint_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkCidr")
    def target_network_cidr(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_network_cidr.setter
    def target_network_cidr(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_group_id.setter
    def access_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizeAllGroups")
    def authorize_all_groups(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @authorize_all_groups.setter
    def authorize_all_groups(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    


@pulumi.input_type
class _AuthorizationRuleState:
    def __init__(__self__, *, access_group_id: Optional[pulumi.Input[_builtins.str]] = ..., authorize_all_groups: Optional[pulumi.Input[_builtins.bool]] = ..., client_vpn_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_group_id.setter
    def access_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizeAllGroups")
    def authorize_all_groups(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @authorize_all_groups.setter
    def authorize_all_groups(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_vpn_endpoint_id.setter
    def client_vpn_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="targetNetworkCidr")
    def target_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_network_cidr.setter
    def target_network_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AuthorizationRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_group_id: Optional[pulumi.Input[_builtins.str]] = ..., authorize_all_groups: Optional[pulumi.Input[_builtins.bool]] = ..., client_vpn_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_network_cidr: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AuthorizationRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_group_id: Optional[pulumi.Input[_builtins.str]] = ..., authorize_all_groups: Optional[pulumi.Input[_builtins.bool]] = ..., client_vpn_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...) -> AuthorizationRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizeAllGroups")
    def authorize_all_groups(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkCidr")
    def target_network_cidr(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


