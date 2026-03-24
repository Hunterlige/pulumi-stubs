import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetIndexResult", "AwaitableGetIndexResult", "get_index", "get_index_output"]

@pulumi.output_type
class GetIndexResult:
    def __init__(
        __self__,
        arn=...,
        capacity_units=...,
        created_at=...,
        description=...,
        document_metadata_configuration_updates=...,
        edition=...,
        error_message=...,
        id=...,
        index_statistics=...,
        name=...,
        region=...,
        role_arn=...,
        server_side_encryption_configurations=...,
        status=...,
        tags=...,
        updated_at=...,
        user_context_policy=...,
        user_group_resolution_configurations=...,
        user_token_configurations=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="capacityUnits")
    def capacity_units(self) -> Sequence[outputs.GetIndexCapacityUnitResult]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="documentMetadataConfigurationUpdates")
    def document_metadata_configuration_updates(
        self,
    ) -> Sequence[outputs.GetIndexDocumentMetadataConfigurationUpdateResult]: ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="indexStatistics")
    def index_statistics(self) -> Sequence[outputs.GetIndexIndexStatisticResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionConfigurations")
    def server_side_encryption_configurations(
        self,
    ) -> Sequence[outputs.GetIndexServerSideEncryptionConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userContextPolicy")
    def user_context_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userGroupResolutionConfigurations")
    def user_group_resolution_configurations(
        self,
    ) -> Sequence[outputs.GetIndexUserGroupResolutionConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="userTokenConfigurations")
    def user_token_configurations(
        self,
    ) -> Sequence[outputs.GetIndexUserTokenConfigurationResult]: ...

class AwaitableGetIndexResult(GetIndexResult):
    def __await__(self): ...

def get_index(
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIndexResult: ...
def get_index_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIndexResult]: ...
