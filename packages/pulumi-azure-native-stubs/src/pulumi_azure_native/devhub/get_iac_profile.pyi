import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIacProfileResult",
    "AwaitableGetIacProfileResult",
    "get_iac_profile",
    "get_iac_profile_output",
]

@pulumi.output_type
class GetIacProfileResult:
    def __init__(
        __self__,
        auth_status=...,
        azure_api_version=...,
        branch_name=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        pr_status=...,
        pull_number=...,
        repository_main_branch=...,
        repository_name=...,
        repository_owner=...,
        stages=...,
        storage_account_name=...,
        storage_account_resource_group=...,
        storage_account_subscription=...,
        storage_container_name=...,
        system_data=...,
        tags=...,
        templates=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authStatus")
    def auth_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="prStatus")
    def pr_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pullNumber")
    def pull_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="repositoryMainBranch")
    def repository_main_branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryOwner")
    def repository_owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def stages(self) -> Optional[Sequence[outputs.StagePropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceGroup")
    def storage_account_resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSubscription")
    def storage_account_subscription(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def templates(
        self,
    ) -> Optional[Sequence[outputs.IacTemplatePropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetIacProfileResult(GetIacProfileResult):
    def __await__(self): ...

def get_iac_profile(
    iac_profile_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIacProfileResult: ...
def get_iac_profile_output(
    iac_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIacProfileResult]: ...
