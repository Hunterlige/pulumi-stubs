

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgentArgs', 'Agent']
@pulumi.input_type
class AgentArgs:
    def __init__(__self__, *, default_language_code: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], time_zone: pulumi.Input[_builtins.str], api_version: Optional[pulumi.Input[_builtins.str]] = ..., avatar_uri: Optional[pulumi.Input[_builtins.str]] = ..., classification_threshold: Optional[pulumi.Input[_builtins.float]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., match_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @default_language_code.setter
    def default_language_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @avatar_uri.setter
    def avatar_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationThreshold")
    def classification_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @classification_threshold.setter
    def classification_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchMode")
    def match_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @match_mode.setter
    def match_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_language_codes.setter
    def supported_language_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentState:
    def __init__(__self__, *, api_version: Optional[pulumi.Input[_builtins.str]] = ..., avatar_uri: Optional[pulumi.Input[_builtins.str]] = ..., avatar_uri_backend: Optional[pulumi.Input[_builtins.str]] = ..., classification_threshold: Optional[pulumi.Input[_builtins.float]] = ..., default_language_code: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., match_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @avatar_uri.setter
    def avatar_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="avatarUriBackend")
    def avatar_uri_backend(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @avatar_uri_backend.setter
    def avatar_uri_backend(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationThreshold")
    def classification_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @classification_threshold.setter
    def classification_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_language_code.setter
    def default_language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchMode")
    def match_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @match_mode.setter
    def match_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_language_codes.setter
    def supported_language_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:diagflow/agent:Agent")
class Agent(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_version: Optional[pulumi.Input[_builtins.str]] = ..., avatar_uri: Optional[pulumi.Input[_builtins.str]] = ..., classification_threshold: Optional[pulumi.Input[_builtins.float]] = ..., default_language_code: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., match_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_version: Optional[pulumi.Input[_builtins.str]] = ..., avatar_uri: Optional[pulumi.Input[_builtins.str]] = ..., avatar_uri_backend: Optional[pulumi.Input[_builtins.str]] = ..., classification_threshold: Optional[pulumi.Input[_builtins.float]] = ..., default_language_code: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., match_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> Agent:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avatarUriBackend")
    def avatar_uri_backend(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationThreshold")
    def classification_threshold(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchMode")
    def match_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


