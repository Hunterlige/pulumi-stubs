

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
__all__ = ['DefaultSecurityGroupArgs', 'DefaultSecurityGroup']
@pulumi.input_type
class DefaultSecurityGroupArgs:
    def __init__(__self__, *, egress: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupEgressArgs]]]] = ..., ingress: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupIngressArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revoke_rules_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupEgressArgs]]]]:
        
        ...
    
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupEgressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupIngressArgs]]]]:
        
        ...
    
    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupIngressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revokeRulesOnDelete")
    def revoke_rules_on_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @revoke_rules_on_delete.setter
    def revoke_rules_on_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DefaultSecurityGroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., egress: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupEgressArgs]]]] = ..., ingress: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupIngressArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revoke_rules_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def egress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupEgressArgs]]]]:
        
        ...
    
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupEgressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupIngressArgs]]]]:
        
        ...
    
    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DefaultSecurityGroupIngressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="revokeRulesOnDelete")
    def revoke_rules_on_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @revoke_rules_on_delete.setter
    def revoke_rules_on_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    


@pulumi.type_token("aws:ec2/defaultSecurityGroup:DefaultSecurityGroup")
class DefaultSecurityGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., egress: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DefaultSecurityGroupEgressArgs, DefaultSecurityGroupEgressArgsDict]]]]] = ..., ingress: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DefaultSecurityGroupIngressArgs, DefaultSecurityGroupIngressArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revoke_rules_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[DefaultSecurityGroupArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., egress: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DefaultSecurityGroupEgressArgs, DefaultSecurityGroupEgressArgsDict]]]]] = ..., ingress: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DefaultSecurityGroupIngressArgs, DefaultSecurityGroupIngressArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revoke_rules_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> DefaultSecurityGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> pulumi.Output[Sequence[outputs.DefaultSecurityGroupEgress]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> pulumi.Output[Sequence[outputs.DefaultSecurityGroupIngress]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
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
    @pulumi.getter(name="revokeRulesOnDelete")
    def revoke_rules_on_delete(self) -> pulumi.Output[Optional[_builtins.bool]]:
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
    


