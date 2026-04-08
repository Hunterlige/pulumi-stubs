import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFactoryResult",
    "AwaitableGetFactoryResult",
    "get_factory",
    "get_factory_output",
]

@pulumi.output_type
class GetFactoryResult:
    def __init__(
        __self__,
        azure_api_version=...,
        create_time=...,
        e_tag=...,
        encryption=...,
        global_parameters=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        provisioning_state=...,
        public_network_access=...,
        purview_configuration=...,
        repo_configuration=...,
        tags=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="globalParameters")
    def global_parameters(
        self,
    ) -> Optional[Mapping[str, outputs.GlobalParameterSpecificationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.FactoryIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(
        self,
    ) -> Optional[outputs.PurviewConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="repoConfiguration")
    def repo_configuration(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetFactoryResult(GetFactoryResult):
    def __await__(self): ...

def get_factory(
    factory_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFactoryResult: ...
def get_factory_output(
    factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFactoryResult]: ...
