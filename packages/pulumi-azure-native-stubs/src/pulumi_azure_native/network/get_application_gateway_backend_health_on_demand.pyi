import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationGatewayBackendHealthOnDemandResult",
    ...,
    "get_application_gateway_backend_health_on_demand",
    ...,
]

@pulumi.output_type
class GetApplicationGatewayBackendHealthOnDemandResult:
    def __init__(
        __self__, backend_address_pool=..., backend_health_http_settings=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPool")
    def backend_address_pool(
        self,
    ) -> Optional[outputs.ApplicationGatewayBackendAddressPoolResponse]: ...
    @_builtins.property
    @pulumi.getter(name="backendHealthHttpSettings")
    def backend_health_http_settings(
        self,
    ) -> Optional[outputs.ApplicationGatewayBackendHealthHttpSettingsResponse]: ...

class AwaitableGetApplicationGatewayBackendHealthOnDemandResult(
    GetApplicationGatewayBackendHealthOnDemandResult
):
    def __await__(self): ...

def get_application_gateway_backend_health_on_demand(
    application_gateway_name: Optional[_builtins.str] = ...,
    backend_address_pool: Optional[Union[SubResource, SubResourceDict]] = ...,
    backend_http_settings: Optional[Union[SubResource, SubResourceDict]] = ...,
    expand: Optional[_builtins.str] = ...,
    host: Optional[_builtins.str] = ...,
    match: Optional[
        Union[
            ApplicationGatewayProbeHealthResponseMatch,
            ApplicationGatewayProbeHealthResponseMatchDict,
        ]
    ] = ...,
    path: Optional[_builtins.str] = ...,
    pick_host_name_from_backend_http_settings: Optional[_builtins.bool] = ...,
    protocol: Optional[Union[_builtins.str, ApplicationGatewayProtocol]] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    timeout: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationGatewayBackendHealthOnDemandResult: ...
def get_application_gateway_backend_health_on_demand_output(
    application_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    backend_address_pool: Optional[
        pulumi.Input[Optional[Union[SubResource, SubResourceDict]]]
    ] = ...,
    backend_http_settings: Optional[
        pulumi.Input[Optional[Union[SubResource, SubResourceDict]]]
    ] = ...,
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    host: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    match: Optional[
        pulumi.Input[
            Optional[
                Union[
                    ApplicationGatewayProbeHealthResponseMatch,
                    ApplicationGatewayProbeHealthResponseMatchDict,
                ]
            ]
        ]
    ] = ...,
    path: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    pick_host_name_from_backend_http_settings: Optional[
        pulumi.Input[Optional[_builtins.bool]]
    ] = ...,
    protocol: Optional[
        pulumi.Input[Optional[Union[_builtins.str, ApplicationGatewayProtocol]]]
    ] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    timeout: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationGatewayBackendHealthOnDemandResult]: ...
