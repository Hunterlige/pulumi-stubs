import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PoolArgs", "Pool"]

@pulumi.input_type
class PoolArgs:
    def __init__(
        __self__,
        *,
        agent_profile: pulumi.Input[Union[StatefulArgs, StatelessAgentProfileArgs]],
        dev_center_project_resource_id: pulumi.Input[_builtins.str],
        fabric_profile: pulumi.Input[VmssFabricProfileArgs],
        maximum_concurrency: pulumi.Input[_builtins.int],
        organization_profile: pulumi.Input[
            Union[AzureDevOpsOrganizationProfileArgs, GitHubOrganizationProfileArgs]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentProfile")
    def agent_profile(
        self,
    ) -> pulumi.Input[Union[StatefulArgs, StatelessAgentProfileArgs]]: ...
    @agent_profile.setter
    def agent_profile(
        self, value: pulumi.Input[Union[StatefulArgs, StatelessAgentProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="devCenterProjectResourceId")
    def dev_center_project_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @dev_center_project_resource_id.setter
    def dev_center_project_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fabricProfile")
    def fabric_profile(self) -> pulumi.Input[VmssFabricProfileArgs]: ...
    @fabric_profile.setter
    def fabric_profile(self, value: pulumi.Input[VmssFabricProfileArgs]): ...
    @_builtins.property
    @pulumi.getter(name="maximumConcurrency")
    def maximum_concurrency(self) -> pulumi.Input[_builtins.int]: ...
    @maximum_concurrency.setter
    def maximum_concurrency(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="organizationProfile")
    def organization_profile(
        self,
    ) -> pulumi.Input[
        Union[AzureDevOpsOrganizationProfileArgs, GitHubOrganizationProfileArgs]
    ]: ...
    @organization_profile.setter
    def organization_profile(
        self,
        value: pulumi.Input[
            Union[AzureDevOpsOrganizationProfileArgs, GitHubOrganizationProfileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]: ...
    @provisioning_state.setter
    def provisioning_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]
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

@pulumi.type_token("azure-native:devopsinfrastructure:Pool")
class Pool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_profile: Optional[
            pulumi.Input[
                Union[
                    Union[StatefulArgs, StatefulArgsDict],
                    Union[StatelessAgentProfileArgs, StatelessAgentProfileArgsDict],
                ]
            ]
        ] = ...,
        dev_center_project_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        fabric_profile: Optional[
            pulumi.Input[Union[VmssFabricProfileArgs, VmssFabricProfileArgsDict]]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maximum_concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        organization_profile: Optional[
            pulumi.Input[
                Union[
                    Union[
                        AzureDevOpsOrganizationProfileArgs,
                        AzureDevOpsOrganizationProfileArgsDict,
                    ],
                    Union[
                        GitHubOrganizationProfileArgs, GitHubOrganizationProfileArgsDict
                    ],
                ]
            ]
        ] = ...,
        pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Pool: ...
    @_builtins.property
    @pulumi.getter(name="agentProfile")
    def agent_profile(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="devCenterProjectResourceId")
    def dev_center_project_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fabricProfile")
    def fabric_profile(self) -> pulumi.Output[outputs.VmssFabricProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maximumConcurrency")
    def maximum_concurrency(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationProfile")
    def organization_profile(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
