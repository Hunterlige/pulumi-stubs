import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApiGatewayResult",
    "AwaitableGetApiGatewayResult",
    "get_api_gateway",
    "get_api_gateway_output",
]

@pulumi.output_type
class GetApiGatewayResult:
    def __init__(
        __self__,
        azure_api_version=...,
        backend=...,
        configuration_api=...,
        created_at_utc=...,
        etag=...,
        frontend=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        sku=...,
        system_data=...,
        tags=...,
        target_provisioning_state=...,
        type=...,
        virtual_network_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def backend(self) -> Optional[outputs.BackendConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="configurationApi")
    def configuration_api(
        self,
    ) -> Optional[outputs.GatewayConfigurationApiResponse]: ...
    @_builtins.property
    @pulumi.getter(name="createdAtUtc")
    def created_at_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def frontend(self) -> Optional[outputs.FrontendConfigurationResponse]: ...
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.ApiManagementGatewaySkuPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetProvisioningState")
    def target_provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetApiGatewayResult(GetApiGatewayResult):
    def __await__(self): ...

def get_api_gateway(
    gateway_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApiGatewayResult: ...
def get_api_gateway_output(
    gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApiGatewayResult]: ...
