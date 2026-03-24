

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
__all__ = ['VpcIpamArgs', 'VpcIpam']
@pulumi.input_type
class VpcIpamArgs:
    def __init__(__self__, *, operating_regions: pulumi.Input[Sequence[pulumi.Input[VpcIpamOperatingRegionArgs]]], cascade: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_private_gua: Optional[pulumi.Input[_builtins.bool]] = ..., metered_account: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> pulumi.Input[Sequence[pulumi.Input[VpcIpamOperatingRegionArgs]]]:
        
        ...
    
    @operating_regions.setter
    def operating_regions(self, value: pulumi.Input[Sequence[pulumi.Input[VpcIpamOperatingRegionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cascade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cascade.setter
    def cascade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateGua")
    def enable_private_gua(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_private_gua.setter
    def enable_private_gua(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="meteredAccount")
    def metered_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metered_account.setter
    def metered_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcIpamState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., cascade: Optional[pulumi.Input[_builtins.bool]] = ..., default_resource_discovery_association_id: Optional[pulumi.Input[_builtins.str]] = ..., default_resource_discovery_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_private_gua: Optional[pulumi.Input[_builtins.bool]] = ..., metered_account: Optional[pulumi.Input[_builtins.str]] = ..., operating_regions: Optional[pulumi.Input[Sequence[pulumi.Input[VpcIpamOperatingRegionArgs]]]] = ..., private_default_scope_id: Optional[pulumi.Input[_builtins.str]] = ..., public_default_scope_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scope_count: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def cascade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cascade.setter
    def cascade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceDiscoveryAssociationId")
    def default_resource_discovery_association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_resource_discovery_association_id.setter
    def default_resource_discovery_association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceDiscoveryId")
    def default_resource_discovery_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_resource_discovery_id.setter
    def default_resource_discovery_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateGua")
    def enable_private_gua(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_private_gua.setter
    def enable_private_gua(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="meteredAccount")
    def metered_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metered_account.setter
    def metered_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VpcIpamOperatingRegionArgs]]]]:
        
        ...
    
    @operating_regions.setter
    def operating_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VpcIpamOperatingRegionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDefaultScopeId")
    def private_default_scope_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_default_scope_id.setter
    def private_default_scope_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDefaultScopeId")
    def public_default_scope_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_default_scope_id.setter
    def public_default_scope_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeCount")
    def scope_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scope_count.setter
    def scope_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/vpcIpam:VpcIpam")
class VpcIpam(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cascade: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_private_gua: Optional[pulumi.Input[_builtins.bool]] = ..., metered_account: Optional[pulumi.Input[_builtins.str]] = ..., operating_regions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VpcIpamOperatingRegionArgs, VpcIpamOperatingRegionArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcIpamArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cascade: Optional[pulumi.Input[_builtins.bool]] = ..., default_resource_discovery_association_id: Optional[pulumi.Input[_builtins.str]] = ..., default_resource_discovery_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_private_gua: Optional[pulumi.Input[_builtins.bool]] = ..., metered_account: Optional[pulumi.Input[_builtins.str]] = ..., operating_regions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VpcIpamOperatingRegionArgs, VpcIpamOperatingRegionArgsDict]]]]] = ..., private_default_scope_id: Optional[pulumi.Input[_builtins.str]] = ..., public_default_scope_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scope_count: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> VpcIpam:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cascade(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceDiscoveryAssociationId")
    def default_resource_discovery_association_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceDiscoveryId")
    def default_resource_discovery_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateGua")
    def enable_private_gua(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="meteredAccount")
    def metered_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> pulumi.Output[Sequence[outputs.VpcIpamOperatingRegion]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDefaultScopeId")
    def private_default_scope_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDefaultScopeId")
    def public_default_scope_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeCount")
    def scope_count(self) -> pulumi.Output[_builtins.int]:
        
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
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


