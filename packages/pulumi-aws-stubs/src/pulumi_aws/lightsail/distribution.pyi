

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
__all__ = ['DistributionArgs', 'Distribution']
@pulumi.input_type
class DistributionArgs:
    def __init__(__self__, *, bundle_id: pulumi.Input[_builtins.str], default_cache_behavior: pulumi.Input[DistributionDefaultCacheBehaviorArgs], origin: pulumi.Input[DistributionOriginArgs], cache_behavior_settings: Optional[pulumi.Input[DistributionCacheBehaviorSettingsArgs]] = ..., cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCacheBehaviorArgs]]]] = ..., certificate_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(self) -> pulumi.Input[DistributionDefaultCacheBehaviorArgs]:
        
        ...
    
    @default_cache_behavior.setter
    def default_cache_behavior(self, value: pulumi.Input[DistributionDefaultCacheBehaviorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> pulumi.Input[DistributionOriginArgs]:
        
        ...
    
    @origin.setter
    def origin(self, value: pulumi.Input[DistributionOriginArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheBehaviorSettings")
    def cache_behavior_settings(self) -> Optional[pulumi.Input[DistributionCacheBehaviorSettingsArgs]]:
        
        ...
    
    @cache_behavior_settings.setter
    def cache_behavior_settings(self, value: Optional[pulumi.Input[DistributionCacheBehaviorSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheBehaviors")
    def cache_behaviors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCacheBehaviorArgs]]]]:
        
        ...
    
    @cache_behaviors.setter
    def cache_behaviors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCacheBehaviorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.input_type
class _DistributionState:
    def __init__(__self__, *, alternative_domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., cache_behavior_settings: Optional[pulumi.Input[DistributionCacheBehaviorSettingsArgs]] = ..., cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCacheBehaviorArgs]]]] = ..., certificate_name: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., default_cache_behavior: Optional[pulumi.Input[DistributionDefaultCacheBehaviorArgs]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., locations: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionLocationArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., origin: Optional[pulumi.Input[DistributionOriginArgs]] = ..., origin_public_dns: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., support_code: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternativeDomainNames")
    def alternative_domain_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @alternative_domain_names.setter
    def alternative_domain_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheBehaviorSettings")
    def cache_behavior_settings(self) -> Optional[pulumi.Input[DistributionCacheBehaviorSettingsArgs]]:
        
        ...
    
    @cache_behavior_settings.setter
    def cache_behavior_settings(self, value: Optional[pulumi.Input[DistributionCacheBehaviorSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheBehaviors")
    def cache_behaviors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCacheBehaviorArgs]]]]:
        
        ...
    
    @cache_behaviors.setter
    def cache_behaviors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionCacheBehaviorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(self) -> Optional[pulumi.Input[DistributionDefaultCacheBehaviorArgs]]:
        
        ...
    
    @default_cache_behavior.setter
    def default_cache_behavior(self, value: Optional[pulumi.Input[DistributionDefaultCacheBehaviorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionLocationArgs]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionLocationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[DistributionOriginArgs]]:
        
        ...
    
    @origin.setter
    def origin(self, value: Optional[pulumi.Input[DistributionOriginArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originPublicDns")
    def origin_public_dns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_public_dns.setter
    def origin_public_dns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportCode")
    def support_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @support_code.setter
    def support_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:lightsail/distribution:Distribution")
class Distribution(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., cache_behavior_settings: Optional[pulumi.Input[Union[DistributionCacheBehaviorSettingsArgs, DistributionCacheBehaviorSettingsArgsDict]]] = ..., cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionCacheBehaviorArgs, DistributionCacheBehaviorArgsDict]]]]] = ..., certificate_name: Optional[pulumi.Input[_builtins.str]] = ..., default_cache_behavior: Optional[pulumi.Input[Union[DistributionDefaultCacheBehaviorArgs, DistributionDefaultCacheBehaviorArgsDict]]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., origin: Optional[pulumi.Input[Union[DistributionOriginArgs, DistributionOriginArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DistributionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., alternative_domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., cache_behavior_settings: Optional[pulumi.Input[Union[DistributionCacheBehaviorSettingsArgs, DistributionCacheBehaviorSettingsArgsDict]]] = ..., cache_behaviors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionCacheBehaviorArgs, DistributionCacheBehaviorArgsDict]]]]] = ..., certificate_name: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., default_cache_behavior: Optional[pulumi.Input[Union[DistributionDefaultCacheBehaviorArgs, DistributionDefaultCacheBehaviorArgsDict]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., locations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DistributionLocationArgs, DistributionLocationArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., origin: Optional[pulumi.Input[Union[DistributionOriginArgs, DistributionOriginArgsDict]]] = ..., origin_public_dns: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., support_code: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Distribution:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternativeDomainNames")
    def alternative_domain_names(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheBehaviorSettings")
    def cache_behavior_settings(self) -> pulumi.Output[Optional[outputs.DistributionCacheBehaviorSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheBehaviors")
    def cache_behaviors(self) -> pulumi.Output[Optional[Sequence[outputs.DistributionCacheBehavior]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCacheBehavior")
    def default_cache_behavior(self) -> pulumi.Output[outputs.DistributionDefaultCacheBehavior]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Output[Sequence[outputs.DistributionLocation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origin(self) -> pulumi.Output[outputs.DistributionOrigin]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originPublicDns")
    def origin_public_dns(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportCode")
    def support_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


