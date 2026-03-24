

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResourceSetResourceArgs', 'ResourceSetResourceArgsDict', 'ResourceSetResourceDnsTargetResourceArgs', 'ResourceSetResourceDnsTargetResourceArgsDict', ..., ..., ..., ..., ..., ...]
class ResourceSetResourceArgsDict(TypedDict):
    component_id: NotRequired[pulumi.Input[_builtins.str]]
    dns_target_resource: NotRequired[pulumi.Input[ResourceSetResourceDnsTargetResourceArgsDict]]
    readiness_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceSetResourceArgs:
    def __init__(__self__, *, component_id: Optional[pulumi.Input[_builtins.str]] = ..., dns_target_resource: Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceArgs]] = ..., readiness_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsTargetResource")
    def dns_target_resource(self) -> Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceArgs]]:
        
        ...
    
    @dns_target_resource.setter
    def dns_target_resource(self, value: Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readinessScopes")
    def readiness_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @readiness_scopes.setter
    def readiness_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceSetResourceDnsTargetResourceArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    hosted_zone_arn: NotRequired[pulumi.Input[_builtins.str]]
    record_set_id: NotRequired[pulumi.Input[_builtins.str]]
    record_type: NotRequired[pulumi.Input[_builtins.str]]
    target_resource: NotRequired[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceArgsDict]]


@pulumi.input_type
class ResourceSetResourceDnsTargetResourceArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], hosted_zone_arn: Optional[pulumi.Input[_builtins.str]] = ..., record_set_id: Optional[pulumi.Input[_builtins.str]] = ..., record_type: Optional[pulumi.Input[_builtins.str]] = ..., target_resource: Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneArn")
    def hosted_zone_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_arn.setter
    def hosted_zone_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSetId")
    def record_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_set_id.setter
    def record_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordType")
    def record_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_type.setter
    def record_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResource")
    def target_resource(self) -> Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceArgs]]:
        
        ...
    
    @target_resource.setter
    def target_resource(self, value: Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceArgs]]): # -> None:
        ...
    


class ResourceSetResourceDnsTargetResourceTargetResourceArgsDict(TypedDict):
    nlb_resource: NotRequired[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgsDict]]
    r53_resource: NotRequired[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgsDict]]


@pulumi.input_type
class ResourceSetResourceDnsTargetResourceTargetResourceArgs:
    def __init__(__self__, *, nlb_resource: Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs]] = ..., r53_resource: Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nlbResource")
    def nlb_resource(self) -> Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs]]:
        
        ...
    
    @nlb_resource.setter
    def nlb_resource(self, value: Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="r53Resource")
    def r53_resource(self) -> Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs]]:
        
        ...
    
    @r53_resource.setter
    def r53_resource(self, value: Optional[pulumi.Input[ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs]]): # -> None:
        ...
    


class ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceSetResourceDnsTargetResourceTargetResourceNlbResourceArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    record_set_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceSetResourceDnsTargetResourceTargetResourceR53ResourceArgs:
    def __init__(__self__, *, domain_name: Optional[pulumi.Input[_builtins.str]] = ..., record_set_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSetId")
    def record_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_set_id.setter
    def record_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


