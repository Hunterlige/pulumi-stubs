import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DirectoryArgs", "Directory"]

@pulumi.input_type
class DirectoryArgs:
    def __init__(
        __self__,
        *,
        active_directory_config: Optional[
            pulumi.Input[DirectoryActiveDirectoryConfigArgs]
        ] = ...,
        certificate_based_auth_properties: Optional[
            pulumi.Input[DirectoryCertificateBasedAuthPropertiesArgs]
        ] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_properties: Optional[pulumi.Input[DirectorySamlPropertiesArgs]] = ...,
        self_service_permissions: Optional[
            pulumi.Input[DirectorySelfServicePermissionsArgs]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tenancy: Optional[pulumi.Input[_builtins.str]] = ...,
        user_identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_access_properties: Optional[
            pulumi.Input[DirectoryWorkspaceAccessPropertiesArgs]
        ] = ...,
        workspace_creation_properties: Optional[
            pulumi.Input[DirectoryWorkspaceCreationPropertiesArgs]
        ] = ...,
        workspace_directory_description: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfig")
    def active_directory_config(
        self,
    ) -> Optional[pulumi.Input[DirectoryActiveDirectoryConfigArgs]]: ...
    @active_directory_config.setter
    def active_directory_config(
        self, value: Optional[pulumi.Input[DirectoryActiveDirectoryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateBasedAuthProperties")
    def certificate_based_auth_properties(
        self,
    ) -> Optional[pulumi.Input[DirectoryCertificateBasedAuthPropertiesArgs]]: ...
    @certificate_based_auth_properties.setter
    def certificate_based_auth_properties(
        self, value: Optional[pulumi.Input[DirectoryCertificateBasedAuthPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipGroupIds")
    def ip_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_group_ids.setter
    def ip_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samlProperties")
    def saml_properties(
        self,
    ) -> Optional[pulumi.Input[DirectorySamlPropertiesArgs]]: ...
    @saml_properties.setter
    def saml_properties(
        self, value: Optional[pulumi.Input[DirectorySamlPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfServicePermissions")
    def self_service_permissions(
        self,
    ) -> Optional[pulumi.Input[DirectorySelfServicePermissionsArgs]]: ...
    @self_service_permissions.setter
    def self_service_permissions(
        self, value: Optional[pulumi.Input[DirectorySelfServicePermissionsArgs]]
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
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userIdentityType")
    def user_identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_identity_type.setter
    def user_identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceAccessProperties")
    def workspace_access_properties(
        self,
    ) -> Optional[pulumi.Input[DirectoryWorkspaceAccessPropertiesArgs]]: ...
    @workspace_access_properties.setter
    def workspace_access_properties(
        self, value: Optional[pulumi.Input[DirectoryWorkspaceAccessPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceCreationProperties")
    def workspace_creation_properties(
        self,
    ) -> Optional[pulumi.Input[DirectoryWorkspaceCreationPropertiesArgs]]: ...
    @workspace_creation_properties.setter
    def workspace_creation_properties(
        self, value: Optional[pulumi.Input[DirectoryWorkspaceCreationPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceDirectoryDescription")
    def workspace_directory_description(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_directory_description.setter
    def workspace_directory_description(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceDirectoryName")
    def workspace_directory_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_directory_name.setter
    def workspace_directory_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceType")
    def workspace_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_type.setter
    def workspace_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DirectoryState:
    def __init__(
        __self__,
        *,
        active_directory_config: Optional[
            pulumi.Input[DirectoryActiveDirectoryConfigArgs]
        ] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_based_auth_properties: Optional[
            pulumi.Input[DirectoryCertificateBasedAuthPropertiesArgs]
        ] = ...,
        customer_user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_type: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        iam_role_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_code: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_properties: Optional[pulumi.Input[DirectorySamlPropertiesArgs]] = ...,
        self_service_permissions: Optional[
            pulumi.Input[DirectorySelfServicePermissionsArgs]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tenancy: Optional[pulumi.Input[_builtins.str]] = ...,
        user_identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_access_properties: Optional[
            pulumi.Input[DirectoryWorkspaceAccessPropertiesArgs]
        ] = ...,
        workspace_creation_properties: Optional[
            pulumi.Input[DirectoryWorkspaceCreationPropertiesArgs]
        ] = ...,
        workspace_directory_description: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfig")
    def active_directory_config(
        self,
    ) -> Optional[pulumi.Input[DirectoryActiveDirectoryConfigArgs]]: ...
    @active_directory_config.setter
    def active_directory_config(
        self, value: Optional[pulumi.Input[DirectoryActiveDirectoryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateBasedAuthProperties")
    def certificate_based_auth_properties(
        self,
    ) -> Optional[pulumi.Input[DirectoryCertificateBasedAuthPropertiesArgs]]: ...
    @certificate_based_auth_properties.setter
    def certificate_based_auth_properties(
        self, value: Optional[pulumi.Input[DirectoryCertificateBasedAuthPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerUserName")
    def customer_user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_user_name.setter
    def customer_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_name.setter
    def directory_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryType")
    def directory_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_type.setter
    def directory_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_ip_addresses.setter
    def dns_ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_role_id.setter
    def iam_role_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipGroupIds")
    def ip_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_group_ids.setter
    def ip_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationCode")
    def registration_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_code.setter
    def registration_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samlProperties")
    def saml_properties(
        self,
    ) -> Optional[pulumi.Input[DirectorySamlPropertiesArgs]]: ...
    @saml_properties.setter
    def saml_properties(
        self, value: Optional[pulumi.Input[DirectorySamlPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfServicePermissions")
    def self_service_permissions(
        self,
    ) -> Optional[pulumi.Input[DirectorySelfServicePermissionsArgs]]: ...
    @self_service_permissions.setter
    def self_service_permissions(
        self, value: Optional[pulumi.Input[DirectorySelfServicePermissionsArgs]]
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
    def tenancy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userIdentityType")
    def user_identity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_identity_type.setter
    def user_identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceAccessProperties")
    def workspace_access_properties(
        self,
    ) -> Optional[pulumi.Input[DirectoryWorkspaceAccessPropertiesArgs]]: ...
    @workspace_access_properties.setter
    def workspace_access_properties(
        self, value: Optional[pulumi.Input[DirectoryWorkspaceAccessPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceCreationProperties")
    def workspace_creation_properties(
        self,
    ) -> Optional[pulumi.Input[DirectoryWorkspaceCreationPropertiesArgs]]: ...
    @workspace_creation_properties.setter
    def workspace_creation_properties(
        self, value: Optional[pulumi.Input[DirectoryWorkspaceCreationPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceDirectoryDescription")
    def workspace_directory_description(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_directory_description.setter
    def workspace_directory_description(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceDirectoryName")
    def workspace_directory_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_directory_name.setter
    def workspace_directory_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_security_group_id.setter
    def workspace_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceType")
    def workspace_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_type.setter
    def workspace_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:workspaces/directory:Directory")
class Directory(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        active_directory_config: Optional[
            pulumi.Input[
                Union[
                    DirectoryActiveDirectoryConfigArgs,
                    DirectoryActiveDirectoryConfigArgsDict,
                ]
            ]
        ] = ...,
        certificate_based_auth_properties: Optional[
            pulumi.Input[
                Union[
                    DirectoryCertificateBasedAuthPropertiesArgs,
                    DirectoryCertificateBasedAuthPropertiesArgsDict,
                ]
            ]
        ] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_properties: Optional[
            pulumi.Input[
                Union[DirectorySamlPropertiesArgs, DirectorySamlPropertiesArgsDict]
            ]
        ] = ...,
        self_service_permissions: Optional[
            pulumi.Input[
                Union[
                    DirectorySelfServicePermissionsArgs,
                    DirectorySelfServicePermissionsArgsDict,
                ]
            ]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tenancy: Optional[pulumi.Input[_builtins.str]] = ...,
        user_identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_access_properties: Optional[
            pulumi.Input[
                Union[
                    DirectoryWorkspaceAccessPropertiesArgs,
                    DirectoryWorkspaceAccessPropertiesArgsDict,
                ]
            ]
        ] = ...,
        workspace_creation_properties: Optional[
            pulumi.Input[
                Union[
                    DirectoryWorkspaceCreationPropertiesArgs,
                    DirectoryWorkspaceCreationPropertiesArgsDict,
                ]
            ]
        ] = ...,
        workspace_directory_description: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[DirectoryArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        active_directory_config: Optional[
            pulumi.Input[
                Union[
                    DirectoryActiveDirectoryConfigArgs,
                    DirectoryActiveDirectoryConfigArgsDict,
                ]
            ]
        ] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_based_auth_properties: Optional[
            pulumi.Input[
                Union[
                    DirectoryCertificateBasedAuthPropertiesArgs,
                    DirectoryCertificateBasedAuthPropertiesArgsDict,
                ]
            ]
        ] = ...,
        customer_user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_type: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        iam_role_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_code: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_properties: Optional[
            pulumi.Input[
                Union[DirectorySamlPropertiesArgs, DirectorySamlPropertiesArgsDict]
            ]
        ] = ...,
        self_service_permissions: Optional[
            pulumi.Input[
                Union[
                    DirectorySelfServicePermissionsArgs,
                    DirectorySelfServicePermissionsArgsDict,
                ]
            ]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tenancy: Optional[pulumi.Input[_builtins.str]] = ...,
        user_identity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_access_properties: Optional[
            pulumi.Input[
                Union[
                    DirectoryWorkspaceAccessPropertiesArgs,
                    DirectoryWorkspaceAccessPropertiesArgsDict,
                ]
            ]
        ] = ...,
        workspace_creation_properties: Optional[
            pulumi.Input[
                Union[
                    DirectoryWorkspaceCreationPropertiesArgs,
                    DirectoryWorkspaceCreationPropertiesArgsDict,
                ]
            ]
        ] = ...,
        workspace_directory_description: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Directory: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfig")
    def active_directory_config(
        self,
    ) -> pulumi.Output[Optional[outputs.DirectoryActiveDirectoryConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateBasedAuthProperties")
    def certificate_based_auth_properties(
        self,
    ) -> pulumi.Output[outputs.DirectoryCertificateBasedAuthProperties]: ...
    @_builtins.property
    @pulumi.getter(name="customerUserName")
    def customer_user_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="directoryType")
    def directory_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipGroupIds")
    def ip_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationCode")
    def registration_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="samlProperties")
    def saml_properties(self) -> pulumi.Output[outputs.DirectorySamlProperties]: ...
    @_builtins.property
    @pulumi.getter(name="selfServicePermissions")
    def self_service_permissions(
        self,
    ) -> pulumi.Output[outputs.DirectorySelfServicePermissions]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userIdentityType")
    def user_identity_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceAccessProperties")
    def workspace_access_properties(
        self,
    ) -> pulumi.Output[outputs.DirectoryWorkspaceAccessProperties]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceCreationProperties")
    def workspace_creation_properties(
        self,
    ) -> pulumi.Output[outputs.DirectoryWorkspaceCreationProperties]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceDirectoryDescription")
    def workspace_directory_description(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceDirectoryName")
    def workspace_directory_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceType")
    def workspace_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
