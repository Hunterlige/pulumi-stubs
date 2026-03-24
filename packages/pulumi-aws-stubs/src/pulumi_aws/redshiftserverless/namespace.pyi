

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NamespaceArgs', 'Namespace']
@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], admin_password_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., admin_username: Optional[pulumi.Input[_builtins.str]] = ..., db_name: Optional[pulumi.Input[_builtins.str]] = ..., default_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., manage_admin_password: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPasswordSecretKmsKeyId")
    def admin_password_secret_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_password_secret_kms_key_id.setter
    def admin_password_secret_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_user_password.setter
    def admin_user_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPasswordWo")
    def admin_user_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_user_password_wo.setter
    def admin_user_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPasswordWoVersion")
    def admin_user_password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @admin_user_password_wo_version.setter
    def admin_user_password_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_name.setter
    def db_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @iam_roles.setter
    def iam_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @log_exports.setter
    def log_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageAdminPassword")
    def manage_admin_password(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @manage_admin_password.setter
    def manage_admin_password(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _NamespaceState:
    def __init__(__self__, *, admin_password_secret_arn: Optional[pulumi.Input[_builtins.str]] = ..., admin_password_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., admin_username: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., db_name: Optional[pulumi.Input[_builtins.str]] = ..., default_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., manage_admin_password: Optional[pulumi.Input[_builtins.bool]] = ..., namespace_id: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPasswordSecretArn")
    def admin_password_secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_password_secret_arn.setter
    def admin_password_secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPasswordSecretKmsKeyId")
    def admin_password_secret_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_password_secret_kms_key_id.setter
    def admin_password_secret_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_user_password.setter
    def admin_user_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPasswordWo")
    def admin_user_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_user_password_wo.setter
    def admin_user_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPasswordWoVersion")
    def admin_user_password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @admin_user_password_wo_version.setter
    def admin_user_password_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_name.setter
    def db_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @iam_roles.setter
    def iam_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @log_exports.setter
    def log_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageAdminPassword")
    def manage_admin_password(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @manage_admin_password.setter
    def manage_admin_password(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:redshiftserverless/namespace:Namespace")
class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., admin_password_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., admin_username: Optional[pulumi.Input[_builtins.str]] = ..., db_name: Optional[pulumi.Input[_builtins.str]] = ..., default_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., manage_admin_password: Optional[pulumi.Input[_builtins.bool]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NamespaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., admin_password_secret_arn: Optional[pulumi.Input[_builtins.str]] = ..., admin_password_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., admin_user_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., admin_username: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., db_name: Optional[pulumi.Input[_builtins.str]] = ..., default_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., manage_admin_password: Optional[pulumi.Input[_builtins.bool]] = ..., namespace_id: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Namespace:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPasswordSecretArn")
    def admin_password_secret_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPasswordSecretKmsKeyId")
    def admin_password_secret_kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPasswordWo")
    def admin_user_password_wo(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUserPasswordWoVersion")
    def admin_user_password_wo_version(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageAdminPassword")
    def manage_admin_password(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


