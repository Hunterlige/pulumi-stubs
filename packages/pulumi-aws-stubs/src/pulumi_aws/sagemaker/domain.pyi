import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainArgs", "Domain"]

@pulumi.input_type
class DomainArgs:
    def __init__(
        __self__,
        *,
        auth_mode: pulumi.Input[_builtins.str],
        default_user_settings: pulumi.Input[DomainDefaultUserSettingsArgs],
        domain_name: pulumi.Input[_builtins.str],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
        app_network_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        app_security_group_management: Optional[pulumi.Input[_builtins.str]] = ...,
        default_space_settings: Optional[
            pulumi.Input[DomainDefaultSpaceSettingsArgs]
        ] = ...,
        domain_settings: Optional[pulumi.Input[DomainDomainSettingsArgs]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_policy: Optional[pulumi.Input[DomainRetentionPolicyArgs]] = ...,
        tag_propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Input[_builtins.str]: ...
    @auth_mode.setter
    def auth_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultUserSettings")
    def default_user_settings(self) -> pulumi.Input[DomainDefaultUserSettingsArgs]: ...
    @default_user_settings.setter
    def default_user_settings(
        self, value: pulumi.Input[DomainDefaultUserSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appNetworkAccessType")
    def app_network_access_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_network_access_type.setter
    def app_network_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appSecurityGroupManagement")
    def app_security_group_management(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_security_group_management.setter
    def app_security_group_management(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSpaceSettings")
    def default_space_settings(
        self,
    ) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsArgs]]: ...
    @default_space_settings.setter
    def default_space_settings(
        self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainSettings")
    def domain_settings(self) -> Optional[pulumi.Input[DomainDomainSettingsArgs]]: ...
    @domain_settings.setter
    def domain_settings(
        self, value: Optional[pulumi.Input[DomainDomainSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[DomainRetentionPolicyArgs]]: ...
    @retention_policy.setter
    def retention_policy(
        self, value: Optional[pulumi.Input[DomainRetentionPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagPropagation")
    def tag_propagation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_propagation.setter
    def tag_propagation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _DomainState:
    def __init__(
        __self__,
        *,
        app_network_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        app_security_group_management: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        default_space_settings: Optional[
            pulumi.Input[DomainDefaultSpaceSettingsArgs]
        ] = ...,
        default_user_settings: Optional[
            pulumi.Input[DomainDefaultUserSettingsArgs]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_settings: Optional[pulumi.Input[DomainDomainSettingsArgs]] = ...,
        home_efs_file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_policy: Optional[pulumi.Input[DomainRetentionPolicyArgs]] = ...,
        security_group_id_for_domain_boundary: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        single_sign_on_application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_managed_application_instance_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tag_propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appNetworkAccessType")
    def app_network_access_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_network_access_type.setter
    def app_network_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appSecurityGroupManagement")
    def app_security_group_management(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_security_group_management.setter
    def app_security_group_management(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_mode.setter
    def auth_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultSpaceSettings")
    def default_space_settings(
        self,
    ) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsArgs]]: ...
    @default_space_settings.setter
    def default_space_settings(
        self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultUserSettings")
    def default_user_settings(
        self,
    ) -> Optional[pulumi.Input[DomainDefaultUserSettingsArgs]]: ...
    @default_user_settings.setter
    def default_user_settings(
        self, value: Optional[pulumi.Input[DomainDefaultUserSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainSettings")
    def domain_settings(self) -> Optional[pulumi.Input[DomainDomainSettingsArgs]]: ...
    @domain_settings.setter
    def domain_settings(
        self, value: Optional[pulumi.Input[DomainDomainSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="homeEfsFileSystemId")
    def home_efs_file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @home_efs_file_system_id.setter
    def home_efs_file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[DomainRetentionPolicyArgs]]: ...
    @retention_policy.setter
    def retention_policy(
        self, value: Optional[pulumi.Input[DomainRetentionPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIdForDomainBoundary")
    def security_group_id_for_domain_boundary(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_group_id_for_domain_boundary.setter
    def security_group_id_for_domain_boundary(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnApplicationArn")
    def single_sign_on_application_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @single_sign_on_application_arn.setter
    def single_sign_on_application_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnManagedApplicationInstanceId")
    def single_sign_on_managed_application_instance_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @single_sign_on_managed_application_instance_id.setter
    def single_sign_on_managed_application_instance_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagPropagation")
    def tag_propagation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_propagation.setter
    def tag_propagation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:sagemaker/domain:Domain")
class Domain(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_network_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        app_security_group_management: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        default_space_settings: Optional[
            pulumi.Input[
                Union[
                    DomainDefaultSpaceSettingsArgs, DomainDefaultSpaceSettingsArgsDict
                ]
            ]
        ] = ...,
        default_user_settings: Optional[
            pulumi.Input[
                Union[DomainDefaultUserSettingsArgs, DomainDefaultUserSettingsArgsDict]
            ]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_settings: Optional[
            pulumi.Input[Union[DomainDomainSettingsArgs, DomainDomainSettingsArgsDict]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_policy: Optional[
            pulumi.Input[
                Union[DomainRetentionPolicyArgs, DomainRetentionPolicyArgsDict]
            ]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tag_propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_network_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        app_security_group_management: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        default_space_settings: Optional[
            pulumi.Input[
                Union[
                    DomainDefaultSpaceSettingsArgs, DomainDefaultSpaceSettingsArgsDict
                ]
            ]
        ] = ...,
        default_user_settings: Optional[
            pulumi.Input[
                Union[DomainDefaultUserSettingsArgs, DomainDefaultUserSettingsArgsDict]
            ]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_settings: Optional[
            pulumi.Input[Union[DomainDomainSettingsArgs, DomainDomainSettingsArgsDict]]
        ] = ...,
        home_efs_file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_policy: Optional[
            pulumi.Input[
                Union[DomainRetentionPolicyArgs, DomainRetentionPolicyArgsDict]
            ]
        ] = ...,
        security_group_id_for_domain_boundary: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        single_sign_on_application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_managed_application_instance_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tag_propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Domain: ...
    @_builtins.property
    @pulumi.getter(name="appNetworkAccessType")
    def app_network_access_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="appSecurityGroupManagement")
    def app_security_group_management(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultSpaceSettings")
    def default_space_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.DomainDefaultSpaceSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultUserSettings")
    def default_user_settings(
        self,
    ) -> pulumi.Output[outputs.DomainDefaultUserSettings]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainSettings")
    def domain_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.DomainDomainSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="homeEfsFileSystemId")
    def home_efs_file_system_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.DomainRetentionPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIdForDomainBoundary")
    def security_group_id_for_domain_boundary(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnApplicationArn")
    def single_sign_on_application_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnManagedApplicationInstanceId")
    def single_sign_on_managed_application_instance_id(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tagPropagation")
    def tag_propagation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
