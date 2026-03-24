

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CommunityTrainingArgs', 'CommunityTraining']
@pulumi.input_type
class CommunityTrainingArgs:
    def __init__(__self__, *, disaster_recovery_enabled: pulumi.Input[_builtins.bool], identity_configuration: pulumi.Input[IdentityConfigurationPropertiesArgs], portal_admin_email_address: pulumi.Input[_builtins.str], portal_name: pulumi.Input[_builtins.str], portal_owner_email_address: pulumi.Input[_builtins.str], portal_owner_organization_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], zone_redundancy_enabled: pulumi.Input[_builtins.bool], community_training_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[SkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryEnabled")
    def disaster_recovery_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @disaster_recovery_enabled.setter
    def disaster_recovery_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityConfiguration")
    def identity_configuration(self) -> pulumi.Input[IdentityConfigurationPropertiesArgs]:
        
        ...
    
    @identity_configuration.setter
    def identity_configuration(self, value: pulumi.Input[IdentityConfigurationPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalAdminEmailAddress")
    def portal_admin_email_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @portal_admin_email_address.setter
    def portal_admin_email_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalName")
    def portal_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @portal_name.setter
    def portal_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalOwnerEmailAddress")
    def portal_owner_email_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @portal_owner_email_address.setter
    def portal_owner_email_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalOwnerOrganizationName")
    def portal_owner_organization_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @portal_owner_organization_name.setter
    def portal_owner_organization_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundancyEnabled")
    def zone_redundancy_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @zone_redundancy_enabled.setter
    def zone_redundancy_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityTrainingName")
    def community_training_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @community_training_name.setter
    def community_training_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:community:CommunityTraining")
class CommunityTraining(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., community_training_name: Optional[pulumi.Input[_builtins.str]] = ..., disaster_recovery_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., identity_configuration: Optional[pulumi.Input[Union[IdentityConfigurationPropertiesArgs, IdentityConfigurationPropertiesArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., portal_admin_email_address: Optional[pulumi.Input[_builtins.str]] = ..., portal_name: Optional[pulumi.Input[_builtins.str]] = ..., portal_owner_email_address: Optional[pulumi.Input[_builtins.str]] = ..., portal_owner_organization_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zone_redundancy_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CommunityTrainingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> CommunityTraining:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryEnabled")
    def disaster_recovery_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityConfiguration")
    def identity_configuration(self) -> pulumi.Output[outputs.IdentityConfigurationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalAdminEmailAddress")
    def portal_admin_email_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalName")
    def portal_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalOwnerEmailAddress")
    def portal_owner_email_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalOwnerOrganizationName")
    def portal_owner_organization_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundancyEnabled")
    def zone_redundancy_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    


