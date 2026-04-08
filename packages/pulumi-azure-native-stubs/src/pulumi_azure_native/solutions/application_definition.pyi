import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationDefinitionArgs", "ApplicationDefinition"]

@pulumi.input_type
class ApplicationDefinitionArgs:
    def __init__(
        __self__,
        *,
        lock_level: pulumi.Input[ApplicationLockLevel],
        resource_group_name: pulumi.Input[_builtins.str],
        application_definition_name: Optional[pulumi.Input[_builtins.str]] = ...,
        artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationDefinitionArtifactArgs]]]
        ] = ...,
        authorizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationAuthorizationArgs]]]
        ] = ...,
        create_ui_definition: Optional[Any] = ...,
        deployment_policy: Optional[
            pulumi.Input[ApplicationDeploymentPolicyArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        locking_policy: Optional[
            pulumi.Input[ApplicationPackageLockingPolicyDefinitionArgs]
        ] = ...,
        main_template: Optional[Any] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        management_policy: Optional[
            pulumi.Input[ApplicationManagementPolicyArgs]
        ] = ...,
        notification_policy: Optional[
            pulumi.Input[ApplicationNotificationPolicyArgs]
        ] = ...,
        package_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationPolicyArgs]]]
        ] = ...,
        sku: Optional[pulumi.Input[SkuArgs]] = ...,
        storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lockLevel")
    def lock_level(self) -> pulumi.Input[ApplicationLockLevel]: ...
    @lock_level.setter
    def lock_level(self, value: pulumi.Input[ApplicationLockLevel]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationDefinitionName")
    def application_definition_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_definition_name.setter
    def application_definition_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationDefinitionArtifactArgs]]]
    ]: ...
    @artifacts.setter
    def artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationDefinitionArtifactArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def authorizations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationAuthorizationArgs]]]
    ]: ...
    @authorizations.setter
    def authorizations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationAuthorizationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createUiDefinition")
    def create_ui_definition(self) -> Optional[Any]: ...
    @create_ui_definition.setter
    def create_ui_definition(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentPolicy")
    def deployment_policy(
        self,
    ) -> Optional[pulumi.Input[ApplicationDeploymentPolicyArgs]]: ...
    @deployment_policy.setter
    def deployment_policy(
        self, value: Optional[pulumi.Input[ApplicationDeploymentPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lockingPolicy")
    def locking_policy(
        self,
    ) -> Optional[pulumi.Input[ApplicationPackageLockingPolicyDefinitionArgs]]: ...
    @locking_policy.setter
    def locking_policy(
        self,
        value: Optional[pulumi.Input[ApplicationPackageLockingPolicyDefinitionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> Optional[Any]: ...
    @main_template.setter
    def main_template(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managementPolicy")
    def management_policy(
        self,
    ) -> Optional[pulumi.Input[ApplicationManagementPolicyArgs]]: ...
    @management_policy.setter
    def management_policy(
        self, value: Optional[pulumi.Input[ApplicationManagementPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(
        self,
    ) -> Optional[pulumi.Input[ApplicationNotificationPolicyArgs]]: ...
    @notification_policy.setter
    def notification_policy(
        self, value: Optional[pulumi.Input[ApplicationNotificationPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="packageFileUri")
    def package_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_file_uri.setter
    def package_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationPolicyArgs]]]]: ...
    @policies.setter
    def policies(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationPolicyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:solutions:ApplicationDefinition")
class ApplicationDefinition(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_definition_name: Optional[pulumi.Input[_builtins.str]] = ...,
        artifacts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationDefinitionArtifactArgs,
                            ApplicationDefinitionArtifactArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        authorizations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationAuthorizationArgs,
                            ApplicationAuthorizationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        create_ui_definition: Optional[Any] = ...,
        deployment_policy: Optional[
            pulumi.Input[
                Union[
                    ApplicationDeploymentPolicyArgs, ApplicationDeploymentPolicyArgsDict
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        lock_level: Optional[pulumi.Input[ApplicationLockLevel]] = ...,
        locking_policy: Optional[
            pulumi.Input[
                Union[
                    ApplicationPackageLockingPolicyDefinitionArgs,
                    ApplicationPackageLockingPolicyDefinitionArgsDict,
                ]
            ]
        ] = ...,
        main_template: Optional[Any] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        management_policy: Optional[
            pulumi.Input[
                Union[
                    ApplicationManagementPolicyArgs, ApplicationManagementPolicyArgsDict
                ]
            ]
        ] = ...,
        notification_policy: Optional[
            pulumi.Input[
                Union[
                    ApplicationNotificationPolicyArgs,
                    ApplicationNotificationPolicyArgsDict,
                ]
            ]
        ] = ...,
        package_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ApplicationPolicyArgs, ApplicationPolicyArgsDict]
                    ]
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationDefinitionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ApplicationDefinition: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationDefinitionArtifactResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def authorizations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationAuthorizationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createUiDefinition")
    def create_ui_definition(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentPolicy")
    def deployment_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationDeploymentPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lockLevel")
    def lock_level(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lockingPolicy")
    def locking_policy(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ApplicationPackageLockingPolicyDefinitionResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managementPolicy")
    def management_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationManagementPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationNotificationPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="packageFileUri")
    def package_file_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def policies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ApplicationPolicyResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
