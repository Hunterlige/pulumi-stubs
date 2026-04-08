import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContainerAppsSessionPoolResult",
    "AwaitableGetContainerAppsSessionPoolResult",
    "get_container_apps_session_pool",
    "get_container_apps_session_pool_output",
]

@pulumi.output_type
class GetContainerAppsSessionPoolResult:
    def __init__(
        __self__,
        azure_api_version=...,
        container_type=...,
        custom_container_template=...,
        dynamic_pool_configuration=...,
        environment_id=...,
        id=...,
        identity=...,
        location=...,
        managed_identity_settings=...,
        name=...,
        node_count=...,
        pool_management_endpoint=...,
        pool_management_type=...,
        provisioning_state=...,
        scale_configuration=...,
        secrets=...,
        session_network_configuration=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customContainerTemplate")
    def custom_container_template(
        self,
    ) -> Optional[outputs.CustomContainerTemplateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicPoolConfiguration")
    def dynamic_pool_configuration(
        self,
    ) -> Optional[outputs.DynamicPoolConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentitySettings")
    def managed_identity_settings(
        self,
    ) -> Optional[Sequence[outputs.ManagedIdentitySettingResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="poolManagementEndpoint")
    def pool_management_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="poolManagementType")
    def pool_management_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scaleConfiguration")
    def scale_configuration(self) -> Optional[outputs.ScaleConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.SessionPoolSecretResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sessionNetworkConfiguration")
    def session_network_configuration(
        self,
    ) -> Optional[outputs.SessionNetworkConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetContainerAppsSessionPoolResult(GetContainerAppsSessionPoolResult):
    def __await__(self): ...

def get_container_apps_session_pool(
    resource_group_name: Optional[_builtins.str] = ...,
    session_pool_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContainerAppsSessionPoolResult: ...
def get_container_apps_session_pool_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    session_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContainerAppsSessionPoolResult]: ...
