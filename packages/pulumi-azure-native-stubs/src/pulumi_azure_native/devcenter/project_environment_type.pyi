import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProjectEnvironmentTypeArgs", "ProjectEnvironmentType"]

@pulumi.input_type
class ProjectEnvironmentTypeArgs:
    def __init__(
        __self__,
        *,
        project_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        creator_role_assignment: Optional[
            pulumi.Input[
                ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs
            ]
        ] = ...,
        deployment_target_id: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, EnvironmentTypeEnableStatus]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_role_assignments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserRoleAssignmentArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]: ...
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="creatorRoleAssignment")
    def creator_role_assignment(
        self,
    ) -> Optional[
        pulumi.Input[ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs]
    ]: ...
    @creator_role_assignment.setter
    def creator_role_assignment(
        self,
        value: Optional[
            pulumi.Input[
                ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentTargetId")
    def deployment_target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_target_id.setter
    def deployment_target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentTypeName")
    def environment_type_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_type_name.setter
    def environment_type_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnvironmentTypeEnableStatus]]]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, EnvironmentTypeEnableStatus]]
        ],
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
    @pulumi.getter(name="userRoleAssignments")
    def user_role_assignments(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[UserRoleAssignmentArgs]]]]: ...
    @user_role_assignments.setter
    def user_role_assignments(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserRoleAssignmentArgs]]]
        ],
    ): ...

@pulumi.type_token("azure-native:devcenter:ProjectEnvironmentType")
class ProjectEnvironmentType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        creator_role_assignment: Optional[
            pulumi.Input[
                Union[
                    ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs,
                    ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgsDict,
                ]
            ]
        ] = ...,
        deployment_target_id: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, EnvironmentTypeEnableStatus]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_role_assignments: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[UserRoleAssignmentArgs, UserRoleAssignmentArgsDict]
                    ],
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProjectEnvironmentTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ProjectEnvironmentType: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creatorRoleAssignment")
    def creator_role_assignment(
        self,
    ) -> pulumi.Output[
        Optional[
            outputs.ProjectEnvironmentTypeUpdatePropertiesResponseCreatorRoleAssignment
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentTargetId")
    def deployment_target_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="environmentCount")
    def environment_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userRoleAssignments")
    def user_role_assignments(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, outputs.UserRoleAssignmentResponse]]]: ...
