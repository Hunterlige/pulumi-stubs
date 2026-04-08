import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSchemaRegistryResult",
    "AwaitableGetSchemaRegistryResult",
    "get_schema_registry",
    "get_schema_registry_output",
]

@pulumi.output_type
class GetSchemaRegistryResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        display_name=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        namespace=...,
        provisioning_state=...,
        storage_account_container_url=...,
        system_data=...,
        tags=...,
        type=...,
        uuid=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.SystemAssignedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountContainerUrl")
    def storage_account_container_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str: ...

class AwaitableGetSchemaRegistryResult(GetSchemaRegistryResult):
    def __await__(self): ...

def get_schema_registry(
    resource_group_name: Optional[_builtins.str] = ...,
    schema_registry_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSchemaRegistryResult: ...
def get_schema_registry_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    schema_registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSchemaRegistryResult]: ...
