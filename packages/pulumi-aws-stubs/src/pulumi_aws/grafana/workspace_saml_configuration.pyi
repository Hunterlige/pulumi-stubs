import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceSamlConfigurationArgs", "WorkspaceSamlConfiguration"]

@pulumi.input_type
class WorkspaceSamlConfigurationArgs:
    def __init__(
        __self__,
        *,
        editor_role_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        workspace_id: pulumi.Input[_builtins.str],
        admin_role_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_organizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        email_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        groups_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_metadata_url: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_metadata_xml: Optional[pulumi.Input[_builtins.str]] = ...,
        login_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        login_validity_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        name_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        org_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="editorRoleValues")
    def editor_role_values(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @editor_role_values.setter
    def editor_role_values(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="adminRoleValues")
    def admin_role_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @admin_role_values.setter
    def admin_role_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedOrganizations")
    def allowed_organizations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_organizations.setter
    def allowed_organizations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailAssertion")
    def email_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_assertion.setter
    def email_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupsAssertion")
    def groups_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @groups_assertion.setter
    def groups_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idpMetadataUrl")
    def idp_metadata_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_metadata_url.setter
    def idp_metadata_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idpMetadataXml")
    def idp_metadata_xml(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_metadata_xml.setter
    def idp_metadata_xml(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loginAssertion")
    def login_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login_assertion.setter
    def login_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loginValidityDuration")
    def login_validity_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @login_validity_duration.setter
    def login_validity_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nameAssertion")
    def name_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_assertion.setter
    def name_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgAssertion")
    def org_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_assertion.setter
    def org_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleAssertion")
    def role_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_assertion.setter
    def role_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _WorkspaceSamlConfigurationState:
    def __init__(
        __self__,
        *,
        admin_role_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_organizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        editor_role_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        email_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        groups_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_metadata_url: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_metadata_xml: Optional[pulumi.Input[_builtins.str]] = ...,
        login_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        login_validity_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        name_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        org_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminRoleValues")
    def admin_role_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @admin_role_values.setter
    def admin_role_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedOrganizations")
    def allowed_organizations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_organizations.setter
    def allowed_organizations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="editorRoleValues")
    def editor_role_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @editor_role_values.setter
    def editor_role_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailAssertion")
    def email_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_assertion.setter
    def email_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupsAssertion")
    def groups_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @groups_assertion.setter
    def groups_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idpMetadataUrl")
    def idp_metadata_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_metadata_url.setter
    def idp_metadata_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idpMetadataXml")
    def idp_metadata_xml(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_metadata_xml.setter
    def idp_metadata_xml(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loginAssertion")
    def login_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login_assertion.setter
    def login_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loginValidityDuration")
    def login_validity_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @login_validity_duration.setter
    def login_validity_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nameAssertion")
    def name_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_assertion.setter
    def name_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgAssertion")
    def org_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_assertion.setter
    def org_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleAssertion")
    def role_assertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_assertion.setter
    def role_assertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class WorkspaceSamlConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_role_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_organizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        editor_role_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        email_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        groups_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_metadata_url: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_metadata_xml: Optional[pulumi.Input[_builtins.str]] = ...,
        login_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        login_validity_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        name_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        org_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceSamlConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_role_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_organizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        editor_role_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        email_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        groups_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_metadata_url: Optional[pulumi.Input[_builtins.str]] = ...,
        idp_metadata_xml: Optional[pulumi.Input[_builtins.str]] = ...,
        login_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        login_validity_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        name_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        org_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_assertion: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> WorkspaceSamlConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="adminRoleValues")
    def admin_role_values(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedOrganizations")
    def allowed_organizations(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="editorRoleValues")
    def editor_role_values(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emailAssertion")
    def email_assertion(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupsAssertion")
    def groups_assertion(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="idpMetadataUrl")
    def idp_metadata_url(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="idpMetadataXml")
    def idp_metadata_xml(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="loginAssertion")
    def login_assertion(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loginValidityDuration")
    def login_validity_duration(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nameAssertion")
    def name_assertion(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgAssertion")
    def org_assertion(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleAssertion")
    def role_assertion(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[_builtins.str]: ...
