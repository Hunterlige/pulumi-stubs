

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
__all__ = ['AgentcoreGatewayArgs', 'AgentcoreGateway']
@pulumi.input_type
class AgentcoreGatewayArgs:
    def __init__(__self__, *, authorizer_type: pulumi.Input[_builtins.str], protocol_type: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], authorizer_configuration: Optional[pulumi.Input[AgentcoreGatewayAuthorizerConfigurationArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exception_level: Optional[pulumi.Input[_builtins.str]] = ..., interceptor_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayInterceptorConfigurationArgs]]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., protocol_configuration: Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AgentcoreGatewayTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerType")
    def authorizer_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorizer_type.setter
    def authorizer_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol_type.setter
    def protocol_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerConfiguration")
    def authorizer_configuration(self) -> Optional[pulumi.Input[AgentcoreGatewayAuthorizerConfigurationArgs]]:
        
        ...
    
    @authorizer_configuration.setter
    def authorizer_configuration(self, value: Optional[pulumi.Input[AgentcoreGatewayAuthorizerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionLevel")
    def exception_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exception_level.setter
    def exception_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptorConfigurations")
    def interceptor_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayInterceptorConfigurationArgs]]]]:
        
        ...
    
    @interceptor_configurations.setter
    def interceptor_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayInterceptorConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolConfiguration")
    def protocol_configuration(self) -> Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationArgs]]:
        
        ...
    
    @protocol_configuration.setter
    def protocol_configuration(self, value: Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationArgs]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[AgentcoreGatewayTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentcoreGatewayTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentcoreGatewayState:
    def __init__(__self__, *, authorizer_configuration: Optional[pulumi.Input[AgentcoreGatewayAuthorizerConfigurationArgs]] = ..., authorizer_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exception_level: Optional[pulumi.Input[_builtins.str]] = ..., gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_url: Optional[pulumi.Input[_builtins.str]] = ..., interceptor_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayInterceptorConfigurationArgs]]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., protocol_configuration: Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationArgs]] = ..., protocol_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AgentcoreGatewayTimeoutsArgs]] = ..., workload_identity_details: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayWorkloadIdentityDetailArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerConfiguration")
    def authorizer_configuration(self) -> Optional[pulumi.Input[AgentcoreGatewayAuthorizerConfigurationArgs]]:
        
        ...
    
    @authorizer_configuration.setter
    def authorizer_configuration(self, value: Optional[pulumi.Input[AgentcoreGatewayAuthorizerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerType")
    def authorizer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_type.setter
    def authorizer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionLevel")
    def exception_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exception_level.setter
    def exception_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_arn.setter
    def gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayUrl")
    def gateway_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_url.setter
    def gateway_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptorConfigurations")
    def interceptor_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayInterceptorConfigurationArgs]]]]:
        
        ...
    
    @interceptor_configurations.setter
    def interceptor_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayInterceptorConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolConfiguration")
    def protocol_configuration(self) -> Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationArgs]]:
        
        ...
    
    @protocol_configuration.setter
    def protocol_configuration(self, value: Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol_type.setter
    def protocol_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[AgentcoreGatewayTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentcoreGatewayTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityDetails")
    def workload_identity_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayWorkloadIdentityDetailArgs]]]]:
        
        ...
    
    @workload_identity_details.setter
    def workload_identity_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreGatewayWorkloadIdentityDetailArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:bedrock/agentcoreGateway:AgentcoreGateway")
class AgentcoreGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorizer_configuration: Optional[pulumi.Input[Union[AgentcoreGatewayAuthorizerConfigurationArgs, AgentcoreGatewayAuthorizerConfigurationArgsDict]]] = ..., authorizer_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exception_level: Optional[pulumi.Input[_builtins.str]] = ..., interceptor_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentcoreGatewayInterceptorConfigurationArgs, AgentcoreGatewayInterceptorConfigurationArgsDict]]]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., protocol_configuration: Optional[pulumi.Input[Union[AgentcoreGatewayProtocolConfigurationArgs, AgentcoreGatewayProtocolConfigurationArgsDict]]] = ..., protocol_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentcoreGatewayTimeoutsArgs, AgentcoreGatewayTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentcoreGatewayArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., authorizer_configuration: Optional[pulumi.Input[Union[AgentcoreGatewayAuthorizerConfigurationArgs, AgentcoreGatewayAuthorizerConfigurationArgsDict]]] = ..., authorizer_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exception_level: Optional[pulumi.Input[_builtins.str]] = ..., gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_url: Optional[pulumi.Input[_builtins.str]] = ..., interceptor_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentcoreGatewayInterceptorConfigurationArgs, AgentcoreGatewayInterceptorConfigurationArgsDict]]]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., protocol_configuration: Optional[pulumi.Input[Union[AgentcoreGatewayProtocolConfigurationArgs, AgentcoreGatewayProtocolConfigurationArgsDict]]] = ..., protocol_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentcoreGatewayTimeoutsArgs, AgentcoreGatewayTimeoutsArgsDict]]] = ..., workload_identity_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentcoreGatewayWorkloadIdentityDetailArgs, AgentcoreGatewayWorkloadIdentityDetailArgsDict]]]]] = ...) -> AgentcoreGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerConfiguration")
    def authorizer_configuration(self) -> pulumi.Output[Optional[outputs.AgentcoreGatewayAuthorizerConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerType")
    def authorizer_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionLevel")
    def exception_level(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayUrl")
    def gateway_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptorConfigurations")
    def interceptor_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.AgentcoreGatewayInterceptorConfiguration]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolConfiguration")
    def protocol_configuration(self) -> pulumi.Output[Optional[outputs.AgentcoreGatewayProtocolConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentcoreGatewayTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityDetails")
    def workload_identity_details(self) -> pulumi.Output[Sequence[outputs.AgentcoreGatewayWorkloadIdentityDetail]]:
        
        ...
    


