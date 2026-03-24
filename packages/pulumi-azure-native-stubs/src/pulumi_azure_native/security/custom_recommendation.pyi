

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CustomRecommendationArgs', 'CustomRecommendation']
@pulumi.input_type
class CustomRecommendationArgs:
    def __init__(__self__, *, scope: pulumi.Input[_builtins.str], cloud_providers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RecommendationSupportedClouds]]]]] = ..., custom_recommendation_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., query: Optional[pulumi.Input[_builtins.str]] = ..., remediation_description: Optional[pulumi.Input[_builtins.str]] = ..., security_issue: Optional[pulumi.Input[Union[_builtins.str, SecurityIssue]]] = ..., severity: Optional[pulumi.Input[Union[_builtins.str, SeverityEnum]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudProviders")
    def cloud_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RecommendationSupportedClouds]]]]]:
        
        ...
    
    @cloud_providers.setter
    def cloud_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RecommendationSupportedClouds]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRecommendationName")
    def custom_recommendation_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_recommendation_name.setter
    def custom_recommendation_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remediation_description.setter
    def remediation_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityIssue")
    def security_issue(self) -> Optional[pulumi.Input[Union[_builtins.str, SecurityIssue]]]:
        
        ...
    
    @security_issue.setter
    def security_issue(self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityIssue]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[Union[_builtins.str, SeverityEnum]]]:
        
        ...
    
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[Union[_builtins.str, SeverityEnum]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:security:CustomRecommendation")
class CustomRecommendation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloud_providers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RecommendationSupportedClouds]]]]] = ..., custom_recommendation_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., query: Optional[pulumi.Input[_builtins.str]] = ..., remediation_description: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., security_issue: Optional[pulumi.Input[Union[_builtins.str, SecurityIssue]]] = ..., severity: Optional[pulumi.Input[Union[_builtins.str, SeverityEnum]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CustomRecommendationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> CustomRecommendation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentKey")
    def assessment_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudProviders")
    def cloud_providers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityIssue")
    def security_issue(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


