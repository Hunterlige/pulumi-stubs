

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointAuthorizationArgs', 'EndpointAuthorization']
@pulumi.input_type
class EndpointAuthorizationArgs:
    def __init__(__self__, *, account: pulumi.Input[_builtins.str], cluster_identifier: pulumi.Input[_builtins.str], force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account.setter
    def account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcIds")
    def vpc_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_ids.setter
    def vpc_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _EndpointAuthorizationState:
    def __init__(__self__, *, account: Optional[pulumi.Input[_builtins.str]] = ..., allowed_all_vpcs: Optional[pulumi.Input[_builtins.bool]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_count: Optional[pulumi.Input[_builtins.int]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., grantee: Optional[pulumi.Input[_builtins.str]] = ..., grantor: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account.setter
    def account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAllVpcs")
    def allowed_all_vpcs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allowed_all_vpcs.setter
    def allowed_all_vpcs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointCount")
    def endpoint_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @endpoint_count.setter
    def endpoint_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @grantee.setter
    def grantee(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @grantor.setter
    def grantor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcIds")
    def vpc_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_ids.setter
    def vpc_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class EndpointAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EndpointAuthorizationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account: Optional[pulumi.Input[_builtins.str]] = ..., allowed_all_vpcs: Optional[pulumi.Input[_builtins.bool]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_count: Optional[pulumi.Input[_builtins.int]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., grantee: Optional[pulumi.Input[_builtins.str]] = ..., grantor: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> EndpointAuthorization:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAllVpcs")
    def allowed_all_vpcs(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointCount")
    def endpoint_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantor(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcIds")
    def vpc_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


