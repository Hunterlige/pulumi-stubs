import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDirectoryResult",
    "AwaitableGetDirectoryResult",
    "get_directory",
    "get_directory_output",
]

@pulumi.output_type
class GetDirectoryResult:
    def __init__(
        __self__,
        active_directory_configs=...,
        alias=...,
        certificate_based_auth_properties=...,
        customer_user_name=...,
        directory_id=...,
        directory_name=...,
        directory_type=...,
        dns_ip_addresses=...,
        iam_role_id=...,
        id=...,
        ip_group_ids=...,
        region=...,
        registration_code=...,
        saml_properties=...,
        self_service_permissions=...,
        subnet_ids=...,
        tags=...,
        tenancy=...,
        user_identity_type=...,
        workspace_access_properties=...,
        workspace_creation_properties=...,
        workspace_directory_description=...,
        workspace_directory_name=...,
        workspace_security_group_id=...,
        workspace_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfigs")
    def active_directory_configs(
        self,
    ) -> Sequence[outputs.GetDirectoryActiveDirectoryConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateBasedAuthProperties")
    def certificate_based_auth_properties(
        self,
    ) -> Sequence[outputs.GetDirectoryCertificateBasedAuthPropertyResult]: ...
    @_builtins.property
    @pulumi.getter(name="customerUserName")
    def customer_user_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="directoryType")
    def directory_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipGroupIds")
    def ip_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registrationCode")
    def registration_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="samlProperties")
    def saml_properties(self) -> Sequence[outputs.GetDirectorySamlPropertyResult]: ...
    @_builtins.property
    @pulumi.getter(name="selfServicePermissions")
    def self_service_permissions(
        self,
    ) -> Sequence[outputs.GetDirectorySelfServicePermissionResult]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userIdentityType")
    def user_identity_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceAccessProperties")
    def workspace_access_properties(
        self,
    ) -> Sequence[outputs.GetDirectoryWorkspaceAccessPropertyResult]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceCreationProperties")
    def workspace_creation_properties(
        self,
    ) -> Sequence[outputs.GetDirectoryWorkspaceCreationPropertyResult]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceDirectoryDescription")
    def workspace_directory_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceDirectoryName")
    def workspace_directory_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceType")
    def workspace_type(self) -> _builtins.str: ...

class AwaitableGetDirectoryResult(GetDirectoryResult):
    def __await__(self): ...

def get_directory(
    directory_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDirectoryResult: ...
def get_directory_output(
    directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDirectoryResult]: ...
