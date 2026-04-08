import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AgentDeploymentArgs", "AgentDeployment"]

@pulumi.input_type
class AgentDeploymentArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        app_name: pulumi.Input[_builtins.str],
        project_name: pulumi.Input[_builtins.str],
        properties: pulumi.Input[
            Union[HostedAgentDeploymentArgs, ManagedAgentDeploymentArgs]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Input[_builtins.str]: ...
    @app_name.setter
    def app_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]: ...
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Input[Union[HostedAgentDeploymentArgs, ManagedAgentDeploymentArgs]]: ...
    @properties.setter
    def properties(
        self,
        value: pulumi.Input[
            Union[HostedAgentDeploymentArgs, ManagedAgentDeploymentArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:cognitiveservices:AgentDeployment")
class AgentDeployment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    Union[HostedAgentDeploymentArgs, HostedAgentDeploymentArgsDict],
                    Union[ManagedAgentDeploymentArgs, ManagedAgentDeploymentArgsDict],
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AgentDeploymentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AgentDeployment: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
