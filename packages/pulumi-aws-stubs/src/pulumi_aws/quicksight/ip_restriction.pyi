

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IpRestrictionArgs', 'IpRestriction']
@pulumi.input_type
class IpRestrictionArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., ip_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRestrictionRuleMap")
    def ip_restriction_rule_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_restriction_rule_map.setter
    def ip_restriction_rule_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointIdRestrictionRuleMap")
    def vpc_endpoint_id_restriction_rule_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_endpoint_id_restriction_rule_map.setter
    def vpc_endpoint_id_restriction_rule_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcIdRestrictionRuleMap")
    def vpc_id_restriction_rule_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_id_restriction_rule_map.setter
    def vpc_id_restriction_rule_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _IpRestrictionState:
    def __init__(__self__, *, aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ip_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRestrictionRuleMap")
    def ip_restriction_rule_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_restriction_rule_map.setter
    def ip_restriction_rule_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointIdRestrictionRuleMap")
    def vpc_endpoint_id_restriction_rule_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_endpoint_id_restriction_rule_map.setter
    def vpc_endpoint_id_restriction_rule_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcIdRestrictionRuleMap")
    def vpc_id_restriction_rule_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_id_restriction_rule_map.setter
    def vpc_id_restriction_rule_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:quicksight/ipRestriction:IpRestriction")
class IpRestriction(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ip_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IpRestrictionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ip_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id_restriction_rule_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> IpRestriction:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRestrictionRuleMap")
    def ip_restriction_rule_map(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointIdRestrictionRuleMap")
    def vpc_endpoint_id_restriction_rule_map(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcIdRestrictionRuleMap")
    def vpc_id_restriction_rule_map(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    


