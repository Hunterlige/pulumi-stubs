

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SecurityProfileArgs', 'SecurityProfile']
@pulumi.input_type
class SecurityProfileArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], custom_intercept_profile: Optional[pulumi.Input[SecurityProfileCustomInterceptProfileArgs]] = ..., custom_mirroring_profile: Optional[pulumi.Input[SecurityProfileCustomMirroringProfileArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., threat_prevention_profile: Optional[pulumi.Input[SecurityProfileThreatPreventionProfileArgs]] = ..., url_filtering_profile: Optional[pulumi.Input[SecurityProfileUrlFilteringProfileArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customInterceptProfile")
    def custom_intercept_profile(self) -> Optional[pulumi.Input[SecurityProfileCustomInterceptProfileArgs]]:
        
        ...
    
    @custom_intercept_profile.setter
    def custom_intercept_profile(self, value: Optional[pulumi.Input[SecurityProfileCustomInterceptProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMirroringProfile")
    def custom_mirroring_profile(self) -> Optional[pulumi.Input[SecurityProfileCustomMirroringProfileArgs]]:
        
        ...
    
    @custom_mirroring_profile.setter
    def custom_mirroring_profile(self, value: Optional[pulumi.Input[SecurityProfileCustomMirroringProfileArgs]]): # -> None:
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
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatPreventionProfile")
    def threat_prevention_profile(self) -> Optional[pulumi.Input[SecurityProfileThreatPreventionProfileArgs]]:
        
        ...
    
    @threat_prevention_profile.setter
    def threat_prevention_profile(self, value: Optional[pulumi.Input[SecurityProfileThreatPreventionProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlFilteringProfile")
    def url_filtering_profile(self) -> Optional[pulumi.Input[SecurityProfileUrlFilteringProfileArgs]]:
        
        ...
    
    @url_filtering_profile.setter
    def url_filtering_profile(self, value: Optional[pulumi.Input[SecurityProfileUrlFilteringProfileArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _SecurityProfileState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., custom_intercept_profile: Optional[pulumi.Input[SecurityProfileCustomInterceptProfileArgs]] = ..., custom_mirroring_profile: Optional[pulumi.Input[SecurityProfileCustomMirroringProfileArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., threat_prevention_profile: Optional[pulumi.Input[SecurityProfileThreatPreventionProfileArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., url_filtering_profile: Optional[pulumi.Input[SecurityProfileUrlFilteringProfileArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customInterceptProfile")
    def custom_intercept_profile(self) -> Optional[pulumi.Input[SecurityProfileCustomInterceptProfileArgs]]:
        
        ...
    
    @custom_intercept_profile.setter
    def custom_intercept_profile(self, value: Optional[pulumi.Input[SecurityProfileCustomInterceptProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMirroringProfile")
    def custom_mirroring_profile(self) -> Optional[pulumi.Input[SecurityProfileCustomMirroringProfileArgs]]:
        
        ...
    
    @custom_mirroring_profile.setter
    def custom_mirroring_profile(self, value: Optional[pulumi.Input[SecurityProfileCustomMirroringProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatPreventionProfile")
    def threat_prevention_profile(self) -> Optional[pulumi.Input[SecurityProfileThreatPreventionProfileArgs]]:
        
        ...
    
    @threat_prevention_profile.setter
    def threat_prevention_profile(self, value: Optional[pulumi.Input[SecurityProfileThreatPreventionProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlFilteringProfile")
    def url_filtering_profile(self) -> Optional[pulumi.Input[SecurityProfileUrlFilteringProfileArgs]]:
        
        ...
    
    @url_filtering_profile.setter
    def url_filtering_profile(self, value: Optional[pulumi.Input[SecurityProfileUrlFilteringProfileArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SecurityProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_intercept_profile: Optional[pulumi.Input[Union[SecurityProfileCustomInterceptProfileArgs, SecurityProfileCustomInterceptProfileArgsDict]]] = ..., custom_mirroring_profile: Optional[pulumi.Input[Union[SecurityProfileCustomMirroringProfileArgs, SecurityProfileCustomMirroringProfileArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., threat_prevention_profile: Optional[pulumi.Input[Union[SecurityProfileThreatPreventionProfileArgs, SecurityProfileThreatPreventionProfileArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., url_filtering_profile: Optional[pulumi.Input[Union[SecurityProfileUrlFilteringProfileArgs, SecurityProfileUrlFilteringProfileArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecurityProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., custom_intercept_profile: Optional[pulumi.Input[Union[SecurityProfileCustomInterceptProfileArgs, SecurityProfileCustomInterceptProfileArgsDict]]] = ..., custom_mirroring_profile: Optional[pulumi.Input[Union[SecurityProfileCustomMirroringProfileArgs, SecurityProfileCustomMirroringProfileArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., threat_prevention_profile: Optional[pulumi.Input[Union[SecurityProfileThreatPreventionProfileArgs, SecurityProfileThreatPreventionProfileArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., url_filtering_profile: Optional[pulumi.Input[Union[SecurityProfileUrlFilteringProfileArgs, SecurityProfileUrlFilteringProfileArgsDict]]] = ...) -> SecurityProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customInterceptProfile")
    def custom_intercept_profile(self) -> pulumi.Output[Optional[outputs.SecurityProfileCustomInterceptProfile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMirroringProfile")
    def custom_mirroring_profile(self) -> pulumi.Output[Optional[outputs.SecurityProfileCustomMirroringProfile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatPreventionProfile")
    def threat_prevention_profile(self) -> pulumi.Output[Optional[outputs.SecurityProfileThreatPreventionProfile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlFilteringProfile")
    def url_filtering_profile(self) -> pulumi.Output[Optional[outputs.SecurityProfileUrlFilteringProfile]]:
        
        ...
    


