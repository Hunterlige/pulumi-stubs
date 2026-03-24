

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointAccessArgs', 'EndpointAccess']
@pulumi.input_type
class EndpointAccessArgs:
    def __init__(__self__, *, endpoint_name: pulumi.Input[_builtins.str], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], workgroup_name: pulumi.Input[_builtins.str], owner_account: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workgroup_name.setter
    def workgroup_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_account.setter
    def owner_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _EndpointAccessState:
    def __init__(__self__, *, address: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., owner_account: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointArgs]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_name.setter
    def endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_account.setter
    def owner_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointArgs]]]]:
        
        ...
    
    @vpc_endpoints.setter
    def vpc_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workgroup_name.setter
    def workgroup_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class EndpointAccess(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., owner_account: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EndpointAccessArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., address: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., owner_account: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EndpointAccessVpcEndpointArgs, EndpointAccessVpcEndpointArgsDict]]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> EndpointAccess:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> pulumi.Output[Sequence[outputs.EndpointAccessVpcEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


