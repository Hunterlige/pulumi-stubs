

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
__all__ = ['StageArgs', 'Stage']
@pulumi.input_type
class StageArgs:
    def __init__(__self__, *, deployment: pulumi.Input[_builtins.str], rest_api: pulumi.Input[_builtins.str], stage_name: pulumi.Input[_builtins.str], access_log_settings: Optional[pulumi.Input[StageAccessLogSettingsArgs]] = ..., cache_cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_cluster_size: Optional[pulumi.Input[_builtins.str]] = ..., canary_settings: Optional[pulumi.Input[StageCanarySettingsArgs]] = ..., client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., documentation_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., xray_tracing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @deployment.setter
    def deployment(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stage_name.setter
    def stage_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogSettings")
    def access_log_settings(self) -> Optional[pulumi.Input[StageAccessLogSettingsArgs]]:
        
        ...
    
    @access_log_settings.setter
    def access_log_settings(self, value: Optional[pulumi.Input[StageAccessLogSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheClusterEnabled")
    def cache_cluster_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cache_cluster_enabled.setter
    def cache_cluster_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheClusterSize")
    def cache_cluster_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_cluster_size.setter
    def cache_cluster_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canarySettings")
    def canary_settings(self) -> Optional[pulumi.Input[StageCanarySettingsArgs]]:
        
        ...
    
    @canary_settings.setter
    def canary_settings(self, value: Optional[pulumi.Input[StageCanarySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate_id.setter
    def client_certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentationVersion")
    def documentation_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @documentation_version.setter
    def documentation_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @variables.setter
    def variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xrayTracingEnabled")
    def xray_tracing_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @xray_tracing_enabled.setter
    def xray_tracing_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _StageState:
    def __init__(__self__, *, access_log_settings: Optional[pulumi.Input[StageAccessLogSettingsArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cache_cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_cluster_size: Optional[pulumi.Input[_builtins.str]] = ..., canary_settings: Optional[pulumi.Input[StageCanarySettingsArgs]] = ..., client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., documentation_version: Optional[pulumi.Input[_builtins.str]] = ..., execution_arn: Optional[pulumi.Input[_builtins.str]] = ..., invoke_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., web_acl_arn: Optional[pulumi.Input[_builtins.str]] = ..., xray_tracing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogSettings")
    def access_log_settings(self) -> Optional[pulumi.Input[StageAccessLogSettingsArgs]]:
        
        ...
    
    @access_log_settings.setter
    def access_log_settings(self, value: Optional[pulumi.Input[StageAccessLogSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheClusterEnabled")
    def cache_cluster_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cache_cluster_enabled.setter
    def cache_cluster_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheClusterSize")
    def cache_cluster_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_cluster_size.setter
    def cache_cluster_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canarySettings")
    def canary_settings(self) -> Optional[pulumi.Input[StageCanarySettingsArgs]]:
        
        ...
    
    @canary_settings.setter
    def canary_settings(self, value: Optional[pulumi.Input[StageCanarySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate_id.setter
    def client_certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentationVersion")
    def documentation_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @documentation_version.setter
    def documentation_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionArn")
    def execution_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_arn.setter
    def execution_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeUrl")
    def invoke_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invoke_url.setter
    def invoke_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stage_name.setter
    def stage_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @variables.setter
    def variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAclArn")
    def web_acl_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_acl_arn.setter
    def web_acl_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xrayTracingEnabled")
    def xray_tracing_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @xray_tracing_enabled.setter
    def xray_tracing_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigateway/stage:Stage")
class Stage(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_log_settings: Optional[pulumi.Input[Union[StageAccessLogSettingsArgs, StageAccessLogSettingsArgsDict]]] = ..., cache_cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_cluster_size: Optional[pulumi.Input[_builtins.str]] = ..., canary_settings: Optional[pulumi.Input[Union[StageCanarySettingsArgs, StageCanarySettingsArgsDict]]] = ..., client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., documentation_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., xray_tracing_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StageArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_log_settings: Optional[pulumi.Input[Union[StageAccessLogSettingsArgs, StageAccessLogSettingsArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cache_cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_cluster_size: Optional[pulumi.Input[_builtins.str]] = ..., canary_settings: Optional[pulumi.Input[Union[StageCanarySettingsArgs, StageCanarySettingsArgsDict]]] = ..., client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., documentation_version: Optional[pulumi.Input[_builtins.str]] = ..., execution_arn: Optional[pulumi.Input[_builtins.str]] = ..., invoke_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., web_acl_arn: Optional[pulumi.Input[_builtins.str]] = ..., xray_tracing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> Stage:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogSettings")
    def access_log_settings(self) -> pulumi.Output[Optional[outputs.StageAccessLogSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheClusterEnabled")
    def cache_cluster_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheClusterSize")
    def cache_cluster_size(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canarySettings")
    def canary_settings(self) -> pulumi.Output[Optional[outputs.StageCanarySettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentationVersion")
    def documentation_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionArn")
    def execution_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeUrl")
    def invoke_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Output[_builtins.str]:
        
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
    def variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAclArn")
    def web_acl_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xrayTracingEnabled")
    def xray_tracing_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


