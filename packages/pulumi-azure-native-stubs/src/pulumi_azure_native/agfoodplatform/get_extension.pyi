import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExtensionResult",
    "AwaitableGetExtensionResult",
    "get_extension",
    "get_extension_output",
]

@pulumi.output_type
class GetExtensionResult:
    def __init__(
        __self__,
        additional_api_properties=...,
        azure_api_version=...,
        e_tag=...,
        extension_api_docs_link=...,
        extension_auth_link=...,
        extension_category=...,
        extension_id=...,
        id=...,
        installed_extension_version=...,
        name=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalApiProperties")
    def additional_api_properties(
        self,
    ) -> Mapping[str, outputs.ApiPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extensionApiDocsLink")
    def extension_api_docs_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extensionAuthLink")
    def extension_auth_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extensionCategory")
    def extension_category(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extensionId")
    def extension_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="installedExtensionVersion")
    def installed_extension_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetExtensionResult(GetExtensionResult):
    def __await__(self): ...

def get_extension(
    data_manager_for_agriculture_resource_name: Optional[_builtins.str] = ...,
    extension_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExtensionResult: ...
def get_extension_output(
    data_manager_for_agriculture_resource_name: Optional[
        pulumi.Input[_builtins.str]
    ] = ...,
    extension_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExtensionResult]: ...
