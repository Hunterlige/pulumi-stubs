import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceArgs", "Workspace"]

@pulumi.input_type
class WorkspaceArgs:
    def __init__(
        __self__,
        *,
        account_access_type: pulumi.Input[_builtins.str],
        authentication_providers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        permission_type: pulumi.Input[_builtins.str],
        configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        data_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        grafana_version: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_access_control: Optional[
            pulumi.Input[WorkspaceNetworkAccessControlArgs]
        ] = ...,
        notification_destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        organization_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_units: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_configuration: Optional[pulumi.Input[WorkspaceVpcConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAccessType")
    def account_access_type(self) -> pulumi.Input[_builtins.str]: ...
    @account_access_type.setter
    def account_access_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationProviders")
    def authentication_providers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @authentication_providers.setter
    def authentication_providers(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> pulumi.Input[_builtins.str]: ...
    @permission_type.setter
    def permission_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @data_sources.setter
    def data_sources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grafanaVersion")
    def grafana_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grafana_version.setter
    def grafana_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkAccessControl")
    def network_access_control(
        self,
    ) -> Optional[pulumi.Input[WorkspaceNetworkAccessControlArgs]]: ...
    @network_access_control.setter
    def network_access_control(
        self, value: Optional[pulumi.Input[WorkspaceNetworkAccessControlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationDestinations")
    def notification_destinations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_destinations.setter
    def notification_destinations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="organizationRoleName")
    def organization_role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization_role_name.setter
    def organization_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnits")
    def organizational_units(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @organizational_units.setter
    def organizational_units(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stack_set_name.setter
    def stack_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> Optional[pulumi.Input[WorkspaceVpcConfigurationArgs]]: ...
    @vpc_configuration.setter
    def vpc_configuration(
        self, value: Optional[pulumi.Input[WorkspaceVpcConfigurationArgs]]
    ): ...

@pulumi.input_type
class _WorkspaceState:
    def __init__(
        __self__,
        *,
        account_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_providers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        data_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        grafana_version: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_access_control: Optional[
            pulumi.Input[WorkspaceNetworkAccessControlArgs]
        ] = ...,
        notification_destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        organization_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_units: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permission_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_configuration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_configuration: Optional[pulumi.Input[WorkspaceVpcConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAccessType")
    def account_access_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_access_type.setter
    def account_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationProviders")
    def authentication_providers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @authentication_providers.setter
    def authentication_providers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @data_sources.setter
    def data_sources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grafanaVersion")
    def grafana_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grafana_version.setter
    def grafana_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkAccessControl")
    def network_access_control(
        self,
    ) -> Optional[pulumi.Input[WorkspaceNetworkAccessControlArgs]]: ...
    @network_access_control.setter
    def network_access_control(
        self, value: Optional[pulumi.Input[WorkspaceNetworkAccessControlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationDestinations")
    def notification_destinations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_destinations.setter
    def notification_destinations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="organizationRoleName")
    def organization_role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization_role_name.setter
    def organization_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnits")
    def organizational_units(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @organizational_units.setter
    def organizational_units(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission_type.setter
    def permission_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samlConfigurationStatus")
    def saml_configuration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @saml_configuration_status.setter
    def saml_configuration_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stack_set_name.setter
    def stack_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> Optional[pulumi.Input[WorkspaceVpcConfigurationArgs]]: ...
    @vpc_configuration.setter
    def vpc_configuration(
        self, value: Optional[pulumi.Input[WorkspaceVpcConfigurationArgs]]
    ): ...

@pulumi.type_token("aws:grafana/workspace:Workspace")
class Workspace(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_providers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        data_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        grafana_version: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_access_control: Optional[
            pulumi.Input[
                Union[
                    WorkspaceNetworkAccessControlArgs,
                    WorkspaceNetworkAccessControlArgsDict,
                ]
            ]
        ] = ...,
        notification_destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        organization_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_units: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permission_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_configuration: Optional[
            pulumi.Input[
                Union[WorkspaceVpcConfigurationArgs, WorkspaceVpcConfigurationArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_providers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        data_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        grafana_version: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_access_control: Optional[
            pulumi.Input[
                Union[
                    WorkspaceNetworkAccessControlArgs,
                    WorkspaceNetworkAccessControlArgsDict,
                ]
            ]
        ] = ...,
        notification_destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        organization_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_units: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permission_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_configuration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_configuration: Optional[
            pulumi.Input[
                Union[WorkspaceVpcConfigurationArgs, WorkspaceVpcConfigurationArgsDict]
            ]
        ] = ...,
    ) -> Workspace: ...
    @_builtins.property
    @pulumi.getter(name="accountAccessType")
    def account_access_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationProviders")
    def authentication_providers(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grafanaVersion")
    def grafana_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkAccessControl")
    def network_access_control(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkspaceNetworkAccessControl]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationDestinations")
    def notification_destinations(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="organizationRoleName")
    def organization_role_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnits")
    def organizational_units(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="samlConfigurationStatus")
    def saml_configuration_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkspaceVpcConfiguration]]: ...
