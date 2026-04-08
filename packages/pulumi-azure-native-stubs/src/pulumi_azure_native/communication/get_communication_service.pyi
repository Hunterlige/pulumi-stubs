import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCommunicationServiceResult",
    "AwaitableGetCommunicationServiceResult",
    "get_communication_service",
    "get_communication_service_output",
]

@pulumi.output_type
class GetCommunicationServiceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_location=...,
        host_name=...,
        id=...,
        identity=...,
        immutable_resource_id=...,
        linked_domains=...,
        location=...,
        name=...,
        notification_hub_id=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="immutableResourceId")
    def immutable_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkedDomains")
    def linked_domains(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notificationHubId")
    def notification_hub_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
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
    def version(self) -> _builtins.str: ...

class AwaitableGetCommunicationServiceResult(GetCommunicationServiceResult):
    def __await__(self): ...

def get_communication_service(
    communication_service_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCommunicationServiceResult: ...
def get_communication_service_output(
    communication_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCommunicationServiceResult]: ...
