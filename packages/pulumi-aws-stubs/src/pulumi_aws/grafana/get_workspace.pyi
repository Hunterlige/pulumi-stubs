import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkspaceResult",
    "AwaitableGetWorkspaceResult",
    "get_workspace",
    "get_workspace_output",
]

@pulumi.output_type
class GetWorkspaceResult:
    def __init__(
        __self__,
        account_access_type=...,
        arn=...,
        authentication_providers=...,
        created_date=...,
        data_sources=...,
        description=...,
        endpoint=...,
        grafana_version=...,
        id=...,
        kms_key_id=...,
        last_updated_date=...,
        name=...,
        notification_destinations=...,
        organization_role_name=...,
        organizational_units=...,
        permission_type=...,
        region=...,
        role_arn=...,
        saml_configuration_status=...,
        stack_set_name=...,
        status=...,
        tags=...,
        workspace_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAccessType")
    def account_access_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationProviders")
    def authentication_providers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="grafanaVersion")
    def grafana_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notificationDestinations")
    def notification_destinations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationRoleName")
    def organization_role_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnits")
    def organizational_units(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="samlConfigurationStatus")
    def saml_configuration_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str: ...

class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    def __await__(self): ...

def get_workspace(
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    workspace_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkspaceResult: ...
def get_workspace_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkspaceResult]: ...
