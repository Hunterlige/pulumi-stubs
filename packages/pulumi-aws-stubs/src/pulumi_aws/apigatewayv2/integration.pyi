

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
__all__ = ['IntegrationArgs', 'Integration']
@pulumi.input_type
class IntegrationArgs:
    def __init__(__self__, *, api_id: pulumi.Input[_builtins.str], integration_type: pulumi.Input[_builtins.str], connection_id: Optional[pulumi.Input[_builtins.str]] = ..., connection_type: Optional[pulumi.Input[_builtins.str]] = ..., content_handling_strategy: Optional[pulumi.Input[_builtins.str]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., integration_method: Optional[pulumi.Input[_builtins.str]] = ..., integration_subtype: Optional[pulumi.Input[_builtins.str]] = ..., integration_uri: Optional[pulumi.Input[_builtins.str]] = ..., passthrough_behavior: Optional[pulumi.Input[_builtins.str]] = ..., payload_format_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[IntegrationResponseParameterArgs]]]] = ..., template_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ..., tls_config: Optional[pulumi.Input[IntegrationTlsConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @integration_type.setter
    def integration_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentHandlingStrategy")
    def content_handling_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_handling_strategy.setter
    def content_handling_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @credentials_arn.setter
    def credentials_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationMethod")
    def integration_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_method.setter
    def integration_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationSubtype")
    def integration_subtype(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_subtype.setter
    def integration_subtype(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationUri")
    def integration_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_uri.setter
    def integration_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passthroughBehavior")
    def passthrough_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @passthrough_behavior.setter
    def passthrough_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadFormatVersion")
    def payload_format_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload_format_version.setter
    def payload_format_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_parameters.setter
    def request_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestTemplates")
    def request_templates(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_templates.setter
    def request_templates(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IntegrationResponseParameterArgs]]]]:
        
        ...
    
    @response_parameters.setter
    def response_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IntegrationResponseParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateSelectionExpression")
    def template_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_selection_expression.setter
    def template_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_milliseconds.setter
    def timeout_milliseconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[IntegrationTlsConfigArgs]]:
        
        ...
    
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[IntegrationTlsConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _IntegrationState:
    def __init__(__self__, *, api_id: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., connection_type: Optional[pulumi.Input[_builtins.str]] = ..., content_handling_strategy: Optional[pulumi.Input[_builtins.str]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., integration_method: Optional[pulumi.Input[_builtins.str]] = ..., integration_response_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., integration_subtype: Optional[pulumi.Input[_builtins.str]] = ..., integration_type: Optional[pulumi.Input[_builtins.str]] = ..., integration_uri: Optional[pulumi.Input[_builtins.str]] = ..., passthrough_behavior: Optional[pulumi.Input[_builtins.str]] = ..., payload_format_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[IntegrationResponseParameterArgs]]]] = ..., template_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ..., tls_config: Optional[pulumi.Input[IntegrationTlsConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentHandlingStrategy")
    def content_handling_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_handling_strategy.setter
    def content_handling_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @credentials_arn.setter
    def credentials_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationMethod")
    def integration_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_method.setter
    def integration_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationResponseSelectionExpression")
    def integration_response_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_response_selection_expression.setter
    def integration_response_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationSubtype")
    def integration_subtype(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_subtype.setter
    def integration_subtype(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_type.setter
    def integration_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationUri")
    def integration_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_uri.setter
    def integration_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passthroughBehavior")
    def passthrough_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @passthrough_behavior.setter
    def passthrough_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadFormatVersion")
    def payload_format_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload_format_version.setter
    def payload_format_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_parameters.setter
    def request_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestTemplates")
    def request_templates(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_templates.setter
    def request_templates(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IntegrationResponseParameterArgs]]]]:
        
        ...
    
    @response_parameters.setter
    def response_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IntegrationResponseParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateSelectionExpression")
    def template_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_selection_expression.setter
    def template_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_milliseconds.setter
    def timeout_milliseconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[IntegrationTlsConfigArgs]]:
        
        ...
    
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[IntegrationTlsConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigatewayv2/integration:Integration")
class Integration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., connection_type: Optional[pulumi.Input[_builtins.str]] = ..., content_handling_strategy: Optional[pulumi.Input[_builtins.str]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., integration_method: Optional[pulumi.Input[_builtins.str]] = ..., integration_subtype: Optional[pulumi.Input[_builtins.str]] = ..., integration_type: Optional[pulumi.Input[_builtins.str]] = ..., integration_uri: Optional[pulumi.Input[_builtins.str]] = ..., passthrough_behavior: Optional[pulumi.Input[_builtins.str]] = ..., payload_format_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IntegrationResponseParameterArgs, IntegrationResponseParameterArgsDict]]]]] = ..., template_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ..., tls_config: Optional[pulumi.Input[Union[IntegrationTlsConfigArgs, IntegrationTlsConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IntegrationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., connection_type: Optional[pulumi.Input[_builtins.str]] = ..., content_handling_strategy: Optional[pulumi.Input[_builtins.str]] = ..., credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., integration_method: Optional[pulumi.Input[_builtins.str]] = ..., integration_response_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., integration_subtype: Optional[pulumi.Input[_builtins.str]] = ..., integration_type: Optional[pulumi.Input[_builtins.str]] = ..., integration_uri: Optional[pulumi.Input[_builtins.str]] = ..., passthrough_behavior: Optional[pulumi.Input[_builtins.str]] = ..., payload_format_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IntegrationResponseParameterArgs, IntegrationResponseParameterArgsDict]]]]] = ..., template_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ..., tls_config: Optional[pulumi.Input[Union[IntegrationTlsConfigArgs, IntegrationTlsConfigArgsDict]]] = ...) -> Integration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentHandlingStrategy")
    def content_handling_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationMethod")
    def integration_method(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationResponseSelectionExpression")
    def integration_response_selection_expression(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationSubtype")
    def integration_subtype(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationUri")
    def integration_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passthroughBehavior")
    def passthrough_behavior(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadFormatVersion")
    def payload_format_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestTemplates")
    def request_templates(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> pulumi.Output[Optional[Sequence[outputs.IntegrationResponseParameter]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateSelectionExpression")
    def template_selection_expression(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> pulumi.Output[Optional[outputs.IntegrationTlsConfig]]:
        
        ...
    


