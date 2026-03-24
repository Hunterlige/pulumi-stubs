

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ContactProfileArgs', 'ContactProfile']
@pulumi.input_type
class ContactProfileArgs:
    def __init__(__self__, *, links: pulumi.Input[Sequence[pulumi.Input[ContactProfileLinkArgs]]], network_configuration: pulumi.Input[ContactProfilesPropertiesNetworkConfigurationArgs], resource_group_name: pulumi.Input[_builtins.str], auto_tracking_configuration: Optional[pulumi.Input[AutoTrackingConfiguration]] = ..., contact_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., event_hub_uri: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., minimum_elevation_degrees: Optional[pulumi.Input[_builtins.float]] = ..., minimum_viable_contact_duration: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., third_party_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ContactProfileThirdPartyConfigurationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> pulumi.Input[Sequence[pulumi.Input[ContactProfileLinkArgs]]]:
        
        ...
    
    @links.setter
    def links(self, value: pulumi.Input[Sequence[pulumi.Input[ContactProfileLinkArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Input[ContactProfilesPropertiesNetworkConfigurationArgs]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: pulumi.Input[ContactProfilesPropertiesNetworkConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoTrackingConfiguration")
    def auto_tracking_configuration(self) -> Optional[pulumi.Input[AutoTrackingConfiguration]]:
        
        ...
    
    @auto_tracking_configuration.setter
    def auto_tracking_configuration(self, value: Optional[pulumi.Input[AutoTrackingConfiguration]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactProfileName")
    def contact_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_profile_name.setter
    def contact_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubUri")
    def event_hub_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_hub_uri.setter
    def event_hub_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumElevationDegrees")
    def minimum_elevation_degrees(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @minimum_elevation_degrees.setter
    def minimum_elevation_degrees(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumViableContactDuration")
    def minimum_viable_contact_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimum_viable_contact_duration.setter
    def minimum_viable_contact_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thirdPartyConfigurations")
    def third_party_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContactProfileThirdPartyConfigurationArgs]]]]:
        
        ...
    
    @third_party_configurations.setter
    def third_party_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContactProfileThirdPartyConfigurationArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:orbital:ContactProfile")
class ContactProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_tracking_configuration: Optional[pulumi.Input[AutoTrackingConfiguration]] = ..., contact_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., event_hub_uri: Optional[pulumi.Input[_builtins.str]] = ..., links: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ContactProfileLinkArgs, ContactProfileLinkArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., minimum_elevation_degrees: Optional[pulumi.Input[_builtins.float]] = ..., minimum_viable_contact_duration: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[Union[ContactProfilesPropertiesNetworkConfigurationArgs, ContactProfilesPropertiesNetworkConfigurationArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., third_party_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ContactProfileThirdPartyConfigurationArgs, ContactProfileThirdPartyConfigurationArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ContactProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ContactProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoTrackingConfiguration")
    def auto_tracking_configuration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubUri")
    def event_hub_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> pulumi.Output[Sequence[outputs.ContactProfileLinkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumElevationDegrees")
    def minimum_elevation_degrees(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumViableContactDuration")
    def minimum_viable_contact_duration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output[outputs.ContactProfilesPropertiesResponseNetworkConfiguration]:
        
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
    @pulumi.getter(name="thirdPartyConfigurations")
    def third_party_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.ContactProfileThirdPartyConfigurationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


