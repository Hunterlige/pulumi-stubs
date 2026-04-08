import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkflowArgs", "Workflow"]

@pulumi.input_type
class WorkflowArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        access_control: Optional[
            pulumi.Input[FlowAccessControlConfigurationArgs]
        ] = ...,
        definition: Optional[Any] = ...,
        endpoints_configuration: Optional[
            pulumi.Input[FlowEndpointsConfigurationArgs]
        ] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        integration_account: Optional[pulumi.Input[ResourceReferenceArgs]] = ...,
        integration_service_environment: Optional[
            pulumi.Input[ResourceReferenceArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[WorkflowParameterArgs]]]
        ] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessControl")
    def access_control(
        self,
    ) -> Optional[pulumi.Input[FlowAccessControlConfigurationArgs]]: ...
    @access_control.setter
    def access_control(
        self, value: Optional[pulumi.Input[FlowAccessControlConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[Any]: ...
    @definition.setter
    def definition(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="endpointsConfiguration")
    def endpoints_configuration(
        self,
    ) -> Optional[pulumi.Input[FlowEndpointsConfigurationArgs]]: ...
    @endpoints_configuration.setter
    def endpoints_configuration(
        self, value: Optional[pulumi.Input[FlowEndpointsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationAccount")
    def integration_account(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]: ...
    @integration_account.setter
    def integration_account(
        self, value: Optional[pulumi.Input[ResourceReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(
        self,
    ) -> Optional[pulumi.Input[ResourceReferenceArgs]]: ...
    @integration_service_environment.setter
    def integration_service_environment(
        self, value: Optional[pulumi.Input[ResourceReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[WorkflowParameterArgs]]]]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[WorkflowParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]]: ...
    @state.setter
    def state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workflow_name.setter
    def workflow_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:logic:Workflow")
class Workflow(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_control: Optional[
            pulumi.Input[
                Union[
                    FlowAccessControlConfigurationArgs,
                    FlowAccessControlConfigurationArgsDict,
                ]
            ]
        ] = ...,
        definition: Optional[Any] = ...,
        endpoints_configuration: Optional[
            pulumi.Input[
                Union[
                    FlowEndpointsConfigurationArgs, FlowEndpointsConfigurationArgsDict
                ]
            ]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        integration_account: Optional[
            pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]
        ] = ...,
        integration_service_environment: Optional[
            pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[WorkflowParameterArgs, WorkflowParameterArgsDict]
                    ],
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkflowArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Workflow: ...
    @_builtins.property
    @pulumi.getter(name="accessControl")
    def access_control(
        self,
    ) -> pulumi.Output[Optional[outputs.FlowAccessControlConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="accessEndpoint")
    def access_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointsConfiguration")
    def endpoints_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.FlowEndpointsConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="integrationAccount")
    def integration_account(
        self,
    ) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(
        self,
    ) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, outputs.WorkflowParameterResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
