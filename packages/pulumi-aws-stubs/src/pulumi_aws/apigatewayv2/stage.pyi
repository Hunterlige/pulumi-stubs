

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
__all__ = ['StageArgs', 'Stage']
@pulumi.input_type
class StageArgs:
    def __init__(__self__, *, api_id: pulumi.Input[_builtins.str], access_log_settings: Optional[pulumi.Input[StageAccessLogSettingsArgs]] = ..., auto_deploy: Optional[pulumi.Input[_builtins.bool]] = ..., client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., default_route_settings: Optional[pulumi.Input[StageDefaultRouteSettingsArgs]] = ..., deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_settings: Optional[pulumi.Input[Sequence[pulumi.Input[StageRouteSettingArgs]]]] = ..., stage_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogSettings")
    def access_log_settings(self) -> Optional[pulumi.Input[StageAccessLogSettingsArgs]]:
        
        ...
    
    @access_log_settings.setter
    def access_log_settings(self, value: Optional[pulumi.Input[StageAccessLogSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeploy")
    def auto_deploy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_deploy.setter
    def auto_deploy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate_id.setter
    def client_certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteSettings")
    def default_route_settings(self) -> Optional[pulumi.Input[StageDefaultRouteSettingsArgs]]:
        
        ...
    
    @default_route_settings.setter
    def default_route_settings(self, value: Optional[pulumi.Input[StageDefaultRouteSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="routeSettings")
    def route_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StageRouteSettingArgs]]]]:
        
        ...
    
    @route_settings.setter
    def route_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StageRouteSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageVariables")
    def stage_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @stage_variables.setter
    def stage_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _StageState:
    def __init__(__self__, *, access_log_settings: Optional[pulumi.Input[StageAccessLogSettingsArgs]] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_deploy: Optional[pulumi.Input[_builtins.bool]] = ..., client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., default_route_settings: Optional[pulumi.Input[StageDefaultRouteSettingsArgs]] = ..., deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_arn: Optional[pulumi.Input[_builtins.str]] = ..., invoke_url: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_settings: Optional[pulumi.Input[Sequence[pulumi.Input[StageRouteSettingArgs]]]] = ..., stage_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogSettings")
    def access_log_settings(self) -> Optional[pulumi.Input[StageAccessLogSettingsArgs]]:
        
        ...
    
    @access_log_settings.setter
    def access_log_settings(self, value: Optional[pulumi.Input[StageAccessLogSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeploy")
    def auto_deploy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_deploy.setter
    def auto_deploy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate_id.setter
    def client_certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteSettings")
    def default_route_settings(self) -> Optional[pulumi.Input[StageDefaultRouteSettingsArgs]]:
        
        ...
    
    @default_route_settings.setter
    def default_route_settings(self, value: Optional[pulumi.Input[StageDefaultRouteSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="routeSettings")
    def route_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StageRouteSettingArgs]]]]:
        
        ...
    
    @route_settings.setter
    def route_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StageRouteSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageVariables")
    def stage_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @stage_variables.setter
    def stage_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    


@pulumi.type_token("aws:apigatewayv2/stage:Stage")
class Stage(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_log_settings: Optional[pulumi.Input[Union[StageAccessLogSettingsArgs, StageAccessLogSettingsArgsDict]]] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., auto_deploy: Optional[pulumi.Input[_builtins.bool]] = ..., client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., default_route_settings: Optional[pulumi.Input[Union[StageDefaultRouteSettingsArgs, StageDefaultRouteSettingsArgsDict]]] = ..., deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StageRouteSettingArgs, StageRouteSettingArgsDict]]]]] = ..., stage_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StageArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_log_settings: Optional[pulumi.Input[Union[StageAccessLogSettingsArgs, StageAccessLogSettingsArgsDict]]] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_deploy: Optional[pulumi.Input[_builtins.bool]] = ..., client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., default_route_settings: Optional[pulumi.Input[Union[StageDefaultRouteSettingsArgs, StageDefaultRouteSettingsArgsDict]]] = ..., deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_arn: Optional[pulumi.Input[_builtins.str]] = ..., invoke_url: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StageRouteSettingArgs, StageRouteSettingArgsDict]]]]] = ..., stage_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Stage:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogSettings")
    def access_log_settings(self) -> pulumi.Output[Optional[outputs.StageAccessLogSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeploy")
    def auto_deploy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteSettings")
    def default_route_settings(self) -> pulumi.Output[Optional[outputs.StageDefaultRouteSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeSettings")
    def route_settings(self) -> pulumi.Output[Optional[Sequence[outputs.StageRouteSetting]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageVariables")
    def stage_variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


