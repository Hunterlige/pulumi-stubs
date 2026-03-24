

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
__all__ = ['DefaultNetworkAclArgs', 'DefaultNetworkAcl']
@pulumi.input_type
class DefaultNetworkAclArgs:
    def __init__(__self__, *, default_network_acl_id: pulumi.Input[_builtins.str], egress: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclEgressArgs]]]] = ..., ingress: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclIngressArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNetworkAclId")
    def default_network_acl_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @default_network_acl_id.setter
    def default_network_acl_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclEgressArgs]]]]:
        
        ...
    
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclEgressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclIngressArgs]]]]:
        
        ...
    
    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclIngressArgs]]]]): # -> None:
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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _DefaultNetworkAclState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., default_network_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., egress: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclEgressArgs]]]] = ..., ingress: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclIngressArgs]]]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNetworkAclId")
    def default_network_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_network_acl_id.setter
    def default_network_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclEgressArgs]]]]:
        
        ...
    
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclEgressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclIngressArgs]]]]:
        
        ...
    
    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultNetworkAclIngressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/defaultNetworkAcl:DefaultNetworkAcl")
class DefaultNetworkAcl(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_network_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., egress: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DefaultNetworkAclEgressArgs, DefaultNetworkAclEgressArgsDict]]]]] = ..., ingress: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DefaultNetworkAclIngressArgs, DefaultNetworkAclIngressArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DefaultNetworkAclArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., default_network_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., egress: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DefaultNetworkAclEgressArgs, DefaultNetworkAclEgressArgsDict]]]]] = ..., ingress: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DefaultNetworkAclIngressArgs, DefaultNetworkAclIngressArgsDict]]]]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> DefaultNetworkAcl:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNetworkAclId")
    def default_network_acl_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> pulumi.Output[Optional[Sequence[outputs.DefaultNetworkAclEgress]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> pulumi.Output[Optional[Sequence[outputs.DefaultNetworkAclIngress]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


