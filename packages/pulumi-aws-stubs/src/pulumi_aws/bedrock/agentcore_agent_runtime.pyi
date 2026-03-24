

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
__all__ = ['AgentcoreAgentRuntimeArgs', 'AgentcoreAgentRuntime']
@pulumi.input_type
class AgentcoreAgentRuntimeArgs:
    def __init__(__self__, *, agent_runtime_artifact: pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactArgs], agent_runtime_name: pulumi.Input[_builtins.str], network_configuration: pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationArgs], role_arn: pulumi.Input[_builtins.str], authorizer_configuration: Optional[pulumi.Input[AgentcoreAgentRuntimeAuthorizerConfigurationArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifecycle_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeLifecycleConfigurationArgs]]]] = ..., protocol_configuration: Optional[pulumi.Input[AgentcoreAgentRuntimeProtocolConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_header_configuration: Optional[pulumi.Input[AgentcoreAgentRuntimeRequestHeaderConfigurationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AgentcoreAgentRuntimeTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeArtifact")
    def agent_runtime_artifact(self) -> pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactArgs]:
        
        ...
    
    @agent_runtime_artifact.setter
    def agent_runtime_artifact(self, value: pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeName")
    def agent_runtime_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent_runtime_name.setter
    def agent_runtime_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationArgs]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationArgs]): # -> None:
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
    def authorizer_configuration(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeAuthorizerConfigurationArgs]]:
        
        ...
    
    @authorizer_configuration.setter
    def authorizer_configuration(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeAuthorizerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigurations")
    def lifecycle_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeLifecycleConfigurationArgs]]]]:
        
        ...
    
    @lifecycle_configurations.setter
    def lifecycle_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeLifecycleConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolConfiguration")
    def protocol_configuration(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeProtocolConfigurationArgs]]:
        
        ...
    
    @protocol_configuration.setter
    def protocol_configuration(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeProtocolConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestHeaderConfiguration")
    def request_header_configuration(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeRequestHeaderConfigurationArgs]]:
        
        ...
    
    @request_header_configuration.setter
    def request_header_configuration(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeRequestHeaderConfigurationArgs]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentcoreAgentRuntimeState:
    def __init__(__self__, *, agent_runtime_arn: Optional[pulumi.Input[_builtins.str]] = ..., agent_runtime_artifact: Optional[pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactArgs]] = ..., agent_runtime_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_runtime_name: Optional[pulumi.Input[_builtins.str]] = ..., agent_runtime_version: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_configuration: Optional[pulumi.Input[AgentcoreAgentRuntimeAuthorizerConfigurationArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifecycle_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeLifecycleConfigurationArgs]]]] = ..., network_configuration: Optional[pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationArgs]] = ..., protocol_configuration: Optional[pulumi.Input[AgentcoreAgentRuntimeProtocolConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_header_configuration: Optional[pulumi.Input[AgentcoreAgentRuntimeRequestHeaderConfigurationArgs]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AgentcoreAgentRuntimeTimeoutsArgs]] = ..., workload_identity_details: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeWorkloadIdentityDetailArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeArn")
    def agent_runtime_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_runtime_arn.setter
    def agent_runtime_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeArtifact")
    def agent_runtime_artifact(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactArgs]]:
        
        ...
    
    @agent_runtime_artifact.setter
    def agent_runtime_artifact(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeId")
    def agent_runtime_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_runtime_id.setter
    def agent_runtime_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeName")
    def agent_runtime_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_runtime_name.setter
    def agent_runtime_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeVersion")
    def agent_runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_runtime_version.setter
    def agent_runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerConfiguration")
    def authorizer_configuration(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeAuthorizerConfigurationArgs]]:
        
        ...
    
    @authorizer_configuration.setter
    def authorizer_configuration(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeAuthorizerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigurations")
    def lifecycle_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeLifecycleConfigurationArgs]]]]:
        
        ...
    
    @lifecycle_configurations.setter
    def lifecycle_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeLifecycleConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationArgs]]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolConfiguration")
    def protocol_configuration(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeProtocolConfigurationArgs]]:
        
        ...
    
    @protocol_configuration.setter
    def protocol_configuration(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeProtocolConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestHeaderConfiguration")
    def request_header_configuration(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeRequestHeaderConfigurationArgs]]:
        
        ...
    
    @request_header_configuration.setter
    def request_header_configuration(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeRequestHeaderConfigurationArgs]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[AgentcoreAgentRuntimeTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentcoreAgentRuntimeTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityDetails")
    def workload_identity_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeWorkloadIdentityDetailArgs]]]]:
        
        ...
    
    @workload_identity_details.setter
    def workload_identity_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentcoreAgentRuntimeWorkloadIdentityDetailArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AgentcoreAgentRuntime(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., agent_runtime_artifact: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeAgentRuntimeArtifactArgs, AgentcoreAgentRuntimeAgentRuntimeArtifactArgsDict]]] = ..., agent_runtime_name: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_configuration: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeAuthorizerConfigurationArgs, AgentcoreAgentRuntimeAuthorizerConfigurationArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifecycle_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentcoreAgentRuntimeLifecycleConfigurationArgs, AgentcoreAgentRuntimeLifecycleConfigurationArgsDict]]]]] = ..., network_configuration: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeNetworkConfigurationArgs, AgentcoreAgentRuntimeNetworkConfigurationArgsDict]]] = ..., protocol_configuration: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeProtocolConfigurationArgs, AgentcoreAgentRuntimeProtocolConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_header_configuration: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeRequestHeaderConfigurationArgs, AgentcoreAgentRuntimeRequestHeaderConfigurationArgsDict]]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeTimeoutsArgs, AgentcoreAgentRuntimeTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentcoreAgentRuntimeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., agent_runtime_arn: Optional[pulumi.Input[_builtins.str]] = ..., agent_runtime_artifact: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeAgentRuntimeArtifactArgs, AgentcoreAgentRuntimeAgentRuntimeArtifactArgsDict]]] = ..., agent_runtime_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_runtime_name: Optional[pulumi.Input[_builtins.str]] = ..., agent_runtime_version: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_configuration: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeAuthorizerConfigurationArgs, AgentcoreAgentRuntimeAuthorizerConfigurationArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., lifecycle_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentcoreAgentRuntimeLifecycleConfigurationArgs, AgentcoreAgentRuntimeLifecycleConfigurationArgsDict]]]]] = ..., network_configuration: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeNetworkConfigurationArgs, AgentcoreAgentRuntimeNetworkConfigurationArgsDict]]] = ..., protocol_configuration: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeProtocolConfigurationArgs, AgentcoreAgentRuntimeProtocolConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_header_configuration: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeRequestHeaderConfigurationArgs, AgentcoreAgentRuntimeRequestHeaderConfigurationArgsDict]]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentcoreAgentRuntimeTimeoutsArgs, AgentcoreAgentRuntimeTimeoutsArgsDict]]] = ..., workload_identity_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentcoreAgentRuntimeWorkloadIdentityDetailArgs, AgentcoreAgentRuntimeWorkloadIdentityDetailArgsDict]]]]] = ...) -> AgentcoreAgentRuntime:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeArn")
    def agent_runtime_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeArtifact")
    def agent_runtime_artifact(self) -> pulumi.Output[outputs.AgentcoreAgentRuntimeAgentRuntimeArtifact]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeId")
    def agent_runtime_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeName")
    def agent_runtime_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentRuntimeVersion")
    def agent_runtime_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerConfiguration")
    def authorizer_configuration(self) -> pulumi.Output[Optional[outputs.AgentcoreAgentRuntimeAuthorizerConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigurations")
    def lifecycle_configurations(self) -> pulumi.Output[Sequence[outputs.AgentcoreAgentRuntimeLifecycleConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output[outputs.AgentcoreAgentRuntimeNetworkConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolConfiguration")
    def protocol_configuration(self) -> pulumi.Output[Optional[outputs.AgentcoreAgentRuntimeProtocolConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestHeaderConfiguration")
    def request_header_configuration(self) -> pulumi.Output[Optional[outputs.AgentcoreAgentRuntimeRequestHeaderConfiguration]]:
        
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentcoreAgentRuntimeTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityDetails")
    def workload_identity_details(self) -> pulumi.Output[Sequence[outputs.AgentcoreAgentRuntimeWorkloadIdentityDetail]]:
        
        ...
    


