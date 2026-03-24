

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
__all__ = ['ApplicationArgs', 'Application']
@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *, runtime_environment: pulumi.Input[_builtins.str], service_execution_role: pulumi.Input[_builtins.str], application_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationArgs]] = ..., application_mode: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[ApplicationCloudwatchLoggingOptionsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., force_stop: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., start_application: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironment")
    def runtime_environment(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @runtime_environment.setter
    def runtime_environment(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRole")
    def service_execution_role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_execution_role.setter
    def service_execution_role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationConfiguration")
    def application_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationArgs]]:
        
        ...
    
    @application_configuration.setter
    def application_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationMode")
    def application_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_mode.setter
    def application_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[ApplicationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[ApplicationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceStop")
    def force_stop(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_stop.setter
    def force_stop(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="startApplication")
    def start_application(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_application.setter
    def start_application(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ApplicationState:
    def __init__(__self__, *, application_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationArgs]] = ..., application_mode: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[ApplicationCloudwatchLoggingOptionsArgs]] = ..., create_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., force_stop: Optional[pulumi.Input[_builtins.bool]] = ..., last_update_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime_environment: Optional[pulumi.Input[_builtins.str]] = ..., service_execution_role: Optional[pulumi.Input[_builtins.str]] = ..., start_application: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version_id: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationConfiguration")
    def application_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationArgs]]:
        
        ...
    
    @application_configuration.setter
    def application_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationMode")
    def application_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_mode.setter
    def application_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[ApplicationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[ApplicationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTimestamp")
    def create_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_timestamp.setter
    def create_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceStop")
    def force_stop(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_stop.setter
    def force_stop(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateTimestamp")
    def last_update_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_update_timestamp.setter
    def last_update_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="runtimeEnvironment")
    def runtime_environment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_environment.setter
    def runtime_environment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRole")
    def service_execution_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_execution_role.setter
    def service_execution_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startApplication")
    def start_application(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_application.setter
    def start_application(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:kinesisanalyticsv2/application:Application")
class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_configuration: Optional[pulumi.Input[Union[ApplicationApplicationConfigurationArgs, ApplicationApplicationConfigurationArgsDict]]] = ..., application_mode: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[Union[ApplicationCloudwatchLoggingOptionsArgs, ApplicationCloudwatchLoggingOptionsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., force_stop: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime_environment: Optional[pulumi.Input[_builtins.str]] = ..., service_execution_role: Optional[pulumi.Input[_builtins.str]] = ..., start_application: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_configuration: Optional[pulumi.Input[Union[ApplicationApplicationConfigurationArgs, ApplicationApplicationConfigurationArgsDict]]] = ..., application_mode: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[Union[ApplicationCloudwatchLoggingOptionsArgs, ApplicationCloudwatchLoggingOptionsArgsDict]]] = ..., create_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., force_stop: Optional[pulumi.Input[_builtins.bool]] = ..., last_update_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime_environment: Optional[pulumi.Input[_builtins.str]] = ..., service_execution_role: Optional[pulumi.Input[_builtins.str]] = ..., start_application: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version_id: Optional[pulumi.Input[_builtins.int]] = ...) -> Application:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationConfiguration")
    def application_configuration(self) -> pulumi.Output[outputs.ApplicationApplicationConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationMode")
    def application_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> pulumi.Output[Optional[outputs.ApplicationCloudwatchLoggingOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTimestamp")
    def create_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceStop")
    def force_stop(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateTimestamp")
    def last_update_timestamp(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="runtimeEnvironment")
    def runtime_environment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRole")
    def service_execution_role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startApplication")
    def start_application(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


