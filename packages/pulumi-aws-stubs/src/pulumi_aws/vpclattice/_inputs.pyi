

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListenerDefaultActionArgs', 'ListenerDefaultActionArgsDict', 'ListenerDefaultActionFixedResponseArgs', 'ListenerDefaultActionFixedResponseArgsDict', 'ListenerDefaultActionForwardArgs', 'ListenerDefaultActionForwardArgsDict', 'ListenerDefaultActionForwardTargetGroupArgs', 'ListenerDefaultActionForwardTargetGroupArgsDict', 'ListenerRuleActionArgs', 'ListenerRuleActionArgsDict', 'ListenerRuleActionFixedResponseArgs', 'ListenerRuleActionFixedResponseArgsDict', 'ListenerRuleActionForwardArgs', 'ListenerRuleActionForwardArgsDict', 'ListenerRuleActionForwardTargetGroupArgs', 'ListenerRuleActionForwardTargetGroupArgsDict', 'ListenerRuleMatchArgs', 'ListenerRuleMatchArgsDict', 'ListenerRuleMatchHttpMatchArgs', 'ListenerRuleMatchHttpMatchArgsDict', 'ListenerRuleMatchHttpMatchHeaderMatchArgs', 'ListenerRuleMatchHttpMatchHeaderMatchArgsDict', 'ListenerRuleMatchHttpMatchHeaderMatchMatchArgs', 'ListenerRuleMatchHttpMatchHeaderMatchMatchArgsDict', 'ListenerRuleMatchHttpMatchPathMatchArgs', 'ListenerRuleMatchHttpMatchPathMatchArgsDict', 'ListenerRuleMatchHttpMatchPathMatchMatchArgs', 'ListenerRuleMatchHttpMatchPathMatchMatchArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'ResourceConfigurationTimeoutsArgs', 'ResourceConfigurationTimeoutsArgsDict', 'ResourceGatewayTimeoutsArgs', 'ResourceGatewayTimeoutsArgsDict', 'ServiceDnsEntryArgs', 'ServiceDnsEntryArgsDict', 'ServiceNetworkResourceAssociationDnsEntryArgs', 'ServiceNetworkResourceAssociationDnsEntryArgsDict', 'ServiceNetworkResourceAssociationTimeoutsArgs', 'ServiceNetworkResourceAssociationTimeoutsArgsDict', 'ServiceNetworkServiceAssociationDnsEntryArgs', 'ServiceNetworkServiceAssociationDnsEntryArgsDict', 'ServiceNetworkVpcAssociationDnsOptionsArgs', 'ServiceNetworkVpcAssociationDnsOptionsArgsDict', 'TargetGroupAttachmentTargetArgs', 'TargetGroupAttachmentTargetArgsDict', 'TargetGroupConfigArgs', 'TargetGroupConfigArgsDict', 'TargetGroupConfigHealthCheckArgs', 'TargetGroupConfigHealthCheckArgsDict', 'TargetGroupConfigHealthCheckMatcherArgs', 'TargetGroupConfigHealthCheckMatcherArgsDict']
class ListenerDefaultActionArgsDict(TypedDict):
    fixed_response: NotRequired[pulumi.Input[ListenerDefaultActionFixedResponseArgsDict]]
    forwards: NotRequired[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardArgsDict]]]]


@pulumi.input_type
class ListenerDefaultActionArgs:
    def __init__(__self__, *, fixed_response: Optional[pulumi.Input[ListenerDefaultActionFixedResponseArgs]] = ..., forwards: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(self) -> Optional[pulumi.Input[ListenerDefaultActionFixedResponseArgs]]:
        ...
    
    @fixed_response.setter
    def fixed_response(self, value: Optional[pulumi.Input[ListenerDefaultActionFixedResponseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def forwards(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardArgs]]]]:
        
        ...
    
    @forwards.setter
    def forwards(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardArgs]]]]): # -> None:
        ...
    


class ListenerDefaultActionFixedResponseArgsDict(TypedDict):
    status_code: pulumi.Input[_builtins.int]


@pulumi.input_type
class ListenerDefaultActionFixedResponseArgs:
    def __init__(__self__, *, status_code: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class ListenerDefaultActionForwardArgsDict(TypedDict):
    target_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardTargetGroupArgsDict]]]]


@pulumi.input_type
class ListenerDefaultActionForwardArgs:
    def __init__(__self__, *, target_groups: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardTargetGroupArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardTargetGroupArgs]]]]:
        
        ...
    
    @target_groups.setter
    def target_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardTargetGroupArgs]]]]): # -> None:
        ...
    


class ListenerDefaultActionForwardTargetGroupArgsDict(TypedDict):
    target_group_identifier: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ListenerDefaultActionForwardTargetGroupArgs:
    def __init__(__self__, *, target_group_identifier: Optional[pulumi.Input[_builtins.str]] = ..., weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_group_identifier.setter
    def target_group_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ListenerRuleActionArgsDict(TypedDict):
    fixed_response: NotRequired[pulumi.Input[ListenerRuleActionFixedResponseArgsDict]]
    forward: NotRequired[pulumi.Input[ListenerRuleActionForwardArgsDict]]


@pulumi.input_type
class ListenerRuleActionArgs:
    def __init__(__self__, *, fixed_response: Optional[pulumi.Input[ListenerRuleActionFixedResponseArgs]] = ..., forward: Optional[pulumi.Input[ListenerRuleActionForwardArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(self) -> Optional[pulumi.Input[ListenerRuleActionFixedResponseArgs]]:
        
        ...
    
    @fixed_response.setter
    def fixed_response(self, value: Optional[pulumi.Input[ListenerRuleActionFixedResponseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def forward(self) -> Optional[pulumi.Input[ListenerRuleActionForwardArgs]]:
        
        ...
    
    @forward.setter
    def forward(self, value: Optional[pulumi.Input[ListenerRuleActionForwardArgs]]): # -> None:
        ...
    


class ListenerRuleActionFixedResponseArgsDict(TypedDict):
    status_code: pulumi.Input[_builtins.int]


@pulumi.input_type
class ListenerRuleActionFixedResponseArgs:
    def __init__(__self__, *, status_code: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class ListenerRuleActionForwardArgsDict(TypedDict):
    target_groups: pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionForwardTargetGroupArgsDict]]]


@pulumi.input_type
class ListenerRuleActionForwardArgs:
    def __init__(__self__, *, target_groups: pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionForwardTargetGroupArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionForwardTargetGroupArgs]]]:
        
        ...
    
    @target_groups.setter
    def target_groups(self, value: pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionForwardTargetGroupArgs]]]): # -> None:
        ...
    


class ListenerRuleActionForwardTargetGroupArgsDict(TypedDict):
    target_group_identifier: pulumi.Input[_builtins.str]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ListenerRuleActionForwardTargetGroupArgs:
    def __init__(__self__, *, target_group_identifier: pulumi.Input[_builtins.str], weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @target_group_identifier.setter
    def target_group_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ListenerRuleMatchArgsDict(TypedDict):
    http_match: pulumi.Input[ListenerRuleMatchHttpMatchArgsDict]


@pulumi.input_type
class ListenerRuleMatchArgs:
    def __init__(__self__, *, http_match: pulumi.Input[ListenerRuleMatchHttpMatchArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMatch")
    def http_match(self) -> pulumi.Input[ListenerRuleMatchHttpMatchArgs]:
        
        ...
    
    @http_match.setter
    def http_match(self, value: pulumi.Input[ListenerRuleMatchHttpMatchArgs]): # -> None:
        ...
    


class ListenerRuleMatchHttpMatchArgsDict(TypedDict):
    header_matches: NotRequired[pulumi.Input[Sequence[pulumi.Input[ListenerRuleMatchHttpMatchHeaderMatchArgsDict]]]]
    method: NotRequired[pulumi.Input[_builtins.str]]
    path_match: NotRequired[pulumi.Input[ListenerRuleMatchHttpMatchPathMatchArgsDict]]


@pulumi.input_type
class ListenerRuleMatchHttpMatchArgs:
    def __init__(__self__, *, header_matches: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleMatchHttpMatchHeaderMatchArgs]]]] = ..., method: Optional[pulumi.Input[_builtins.str]] = ..., path_match: Optional[pulumi.Input[ListenerRuleMatchHttpMatchPathMatchArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerMatches")
    def header_matches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleMatchHttpMatchHeaderMatchArgs]]]]:
        
        ...
    
    @header_matches.setter
    def header_matches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleMatchHttpMatchHeaderMatchArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathMatch")
    def path_match(self) -> Optional[pulumi.Input[ListenerRuleMatchHttpMatchPathMatchArgs]]:
        
        ...
    
    @path_match.setter
    def path_match(self, value: Optional[pulumi.Input[ListenerRuleMatchHttpMatchPathMatchArgs]]): # -> None:
        ...
    


class ListenerRuleMatchHttpMatchHeaderMatchArgsDict(TypedDict):
    match: pulumi.Input[ListenerRuleMatchHttpMatchHeaderMatchMatchArgsDict]
    name: pulumi.Input[_builtins.str]
    case_sensitive: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ListenerRuleMatchHttpMatchHeaderMatchArgs:
    def __init__(__self__, *, match: pulumi.Input[ListenerRuleMatchHttpMatchHeaderMatchMatchArgs], name: pulumi.Input[_builtins.str], case_sensitive: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[ListenerRuleMatchHttpMatchHeaderMatchMatchArgs]:
        
        ...
    
    @match.setter
    def match(self, value: pulumi.Input[ListenerRuleMatchHttpMatchHeaderMatchMatchArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @case_sensitive.setter
    def case_sensitive(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ListenerRuleMatchHttpMatchHeaderMatchMatchArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerRuleMatchHttpMatchHeaderMatchMatchArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerRuleMatchHttpMatchPathMatchArgsDict(TypedDict):
    match: pulumi.Input[ListenerRuleMatchHttpMatchPathMatchMatchArgsDict]
    case_sensitive: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ListenerRuleMatchHttpMatchPathMatchArgs:
    def __init__(__self__, *, match: pulumi.Input[ListenerRuleMatchHttpMatchPathMatchMatchArgs], case_sensitive: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[ListenerRuleMatchHttpMatchPathMatchMatchArgs]:
        
        ...
    
    @match.setter
    def match(self, value: pulumi.Input[ListenerRuleMatchHttpMatchPathMatchMatchArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @case_sensitive.setter
    def case_sensitive(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ListenerRuleMatchHttpMatchPathMatchMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerRuleMatchHttpMatchPathMatchMatchArgs:
    def __init__(__self__, *, exact: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceConfigurationResourceConfigurationDefinitionArgsDict(TypedDict):
    arn_resource: NotRequired[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArnResourceArgsDict]]
    dns_resource: NotRequired[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionDnsResourceArgsDict]]
    ip_resource: NotRequired[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionIpResourceArgsDict]]


@pulumi.input_type
class ResourceConfigurationResourceConfigurationDefinitionArgs:
    def __init__(__self__, *, arn_resource: Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArnResourceArgs]] = ..., dns_resource: Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionDnsResourceArgs]] = ..., ip_resource: Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionIpResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arnResource")
    def arn_resource(self) -> Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArnResourceArgs]]:
        
        ...
    
    @arn_resource.setter
    def arn_resource(self, value: Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArnResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsResource")
    def dns_resource(self) -> Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionDnsResourceArgs]]:
        
        ...
    
    @dns_resource.setter
    def dns_resource(self, value: Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionDnsResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipResource")
    def ip_resource(self) -> Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionIpResourceArgs]]:
        
        ...
    
    @ip_resource.setter
    def ip_resource(self, value: Optional[pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionIpResourceArgs]]): # -> None:
        ...
    


class ResourceConfigurationResourceConfigurationDefinitionArnResourceArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResourceConfigurationResourceConfigurationDefinitionArnResourceArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResourceConfigurationResourceConfigurationDefinitionDnsResourceArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    ip_address_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResourceConfigurationResourceConfigurationDefinitionDnsResourceArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], ip_address_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResourceConfigurationResourceConfigurationDefinitionIpResourceArgsDict(TypedDict):
    ip_address: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResourceConfigurationResourceConfigurationDefinitionIpResourceArgs:
    def __init__(__self__, *, ip_address: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResourceConfigurationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceConfigurationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceGatewayTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceGatewayTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceDnsEntryArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    hosted_zone_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceDnsEntryArgs:
    def __init__(__self__, *, domain_name: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceNetworkResourceAssociationDnsEntryArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    hosted_zone_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class ServiceNetworkResourceAssociationDnsEntryArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], hosted_zone_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServiceNetworkResourceAssociationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceNetworkResourceAssociationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceNetworkServiceAssociationDnsEntryArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    hosted_zone_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceNetworkServiceAssociationDnsEntryArgs:
    def __init__(__self__, *, domain_name: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceNetworkVpcAssociationDnsOptionsArgsDict(TypedDict):
    private_dns_preference: NotRequired[pulumi.Input[_builtins.str]]
    private_dns_specified_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ServiceNetworkVpcAssociationDnsOptionsArgs:
    def __init__(__self__, *, private_dns_preference: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_specified_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsPreference")
    def private_dns_preference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_preference.setter
    def private_dns_preference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsSpecifiedDomains")
    def private_dns_specified_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_dns_specified_domains.setter
    def private_dns_specified_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class TargetGroupAttachmentTargetArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TargetGroupAttachmentTargetArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TargetGroupConfigArgsDict(TypedDict):
    health_check: NotRequired[pulumi.Input[TargetGroupConfigHealthCheckArgsDict]]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]
    lambda_event_structure_version: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    protocol_version: NotRequired[pulumi.Input[_builtins.str]]
    vpc_identifier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TargetGroupConfigArgs:
    def __init__(__self__, *, health_check: Optional[pulumi.Input[TargetGroupConfigHealthCheckArgs]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., lambda_event_structure_version: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., protocol_version: Optional[pulumi.Input[_builtins.str]] = ..., vpc_identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[TargetGroupConfigHealthCheckArgs]]:
        
        ...
    
    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input[TargetGroupConfigHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaEventStructureVersion")
    def lambda_event_structure_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lambda_event_structure_version.setter
    def lambda_event_structure_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol_version.setter
    def protocol_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcIdentifier")
    def vpc_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_identifier.setter
    def vpc_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TargetGroupConfigHealthCheckArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    health_check_interval_seconds: NotRequired[pulumi.Input[_builtins.int]]
    health_check_timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    healthy_threshold_count: NotRequired[pulumi.Input[_builtins.int]]
    matcher: NotRequired[pulumi.Input[TargetGroupConfigHealthCheckMatcherArgsDict]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    protocol_version: NotRequired[pulumi.Input[_builtins.str]]
    unhealthy_threshold_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TargetGroupConfigHealthCheckArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ..., health_check_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ..., healthy_threshold_count: Optional[pulumi.Input[_builtins.int]] = ..., matcher: Optional[pulumi.Input[TargetGroupConfigHealthCheckMatcherArgs]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., protocol_version: Optional[pulumi.Input[_builtins.str]] = ..., unhealthy_threshold_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckIntervalSeconds")
    def health_check_interval_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @health_check_interval_seconds.setter
    def health_check_interval_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckTimeoutSeconds")
    def health_check_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @health_check_timeout_seconds.setter
    def health_check_timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThresholdCount")
    def healthy_threshold_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @healthy_threshold_count.setter
    def healthy_threshold_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def matcher(self) -> Optional[pulumi.Input[TargetGroupConfigHealthCheckMatcherArgs]]:
        
        ...
    
    @matcher.setter
    def matcher(self, value: Optional[pulumi.Input[TargetGroupConfigHealthCheckMatcherArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol_version.setter
    def protocol_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThresholdCount")
    def unhealthy_threshold_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @unhealthy_threshold_count.setter
    def unhealthy_threshold_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TargetGroupConfigHealthCheckMatcherArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TargetGroupConfigHealthCheckMatcherArgs:
    def __init__(__self__, *, value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


