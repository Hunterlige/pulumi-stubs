

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WebAclLoggingConfigurationArgs', 'WebAclLoggingConfiguration']
@pulumi.input_type
class WebAclLoggingConfigurationArgs:
    def __init__(__self__, *, log_destination_configs: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], resource_arn: pulumi.Input[_builtins.str], logging_filter: Optional[pulumi.Input[WebAclLoggingConfigurationLoggingFilterArgs]] = ..., redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @log_destination_configs.setter
    def log_destination_configs(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingFilter")
    def logging_filter(self) -> Optional[pulumi.Input[WebAclLoggingConfigurationLoggingFilterArgs]]:
        
        ...
    
    @logging_filter.setter
    def logging_filter(self, value: Optional[pulumi.Input[WebAclLoggingConfigurationLoggingFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldArgs]]]]:
        
        ...
    
    @redacted_fields.setter
    def redacted_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WebAclLoggingConfigurationState:
    def __init__(__self__, *, log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., logging_filter: Optional[pulumi.Input[WebAclLoggingConfigurationLoggingFilterArgs]] = ..., redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @log_destination_configs.setter
    def log_destination_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingFilter")
    def logging_filter(self) -> Optional[pulumi.Input[WebAclLoggingConfigurationLoggingFilterArgs]]:
        
        ...
    
    @logging_filter.setter
    def logging_filter(self, value: Optional[pulumi.Input[WebAclLoggingConfigurationLoggingFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldArgs]]]]:
        
        ...
    
    @redacted_fields.setter
    def redacted_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WebAclLoggingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., logging_filter: Optional[pulumi.Input[Union[WebAclLoggingConfigurationLoggingFilterArgs, WebAclLoggingConfigurationLoggingFilterArgsDict]]] = ..., redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WebAclLoggingConfigurationRedactedFieldArgs, WebAclLoggingConfigurationRedactedFieldArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebAclLoggingConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., log_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., logging_filter: Optional[pulumi.Input[Union[WebAclLoggingConfigurationLoggingFilterArgs, WebAclLoggingConfigurationLoggingFilterArgsDict]]] = ..., redacted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WebAclLoggingConfigurationRedactedFieldArgs, WebAclLoggingConfigurationRedactedFieldArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> WebAclLoggingConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingFilter")
    def logging_filter(self) -> pulumi.Output[Optional[outputs.WebAclLoggingConfigurationLoggingFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> pulumi.Output[Optional[Sequence[outputs.WebAclLoggingConfigurationRedactedField]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


