import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBrokerResult",
    "AwaitableGetBrokerResult",
    "get_broker",
    "get_broker_output",
]

@pulumi.output_type
class GetBrokerResult:
    def __init__(
        __self__,
        auth_image=...,
        azure_api_version=...,
        broker_image=...,
        broker_node_tolerations=...,
        cardinality=...,
        diagnostics=...,
        disk_backed_message_buffer_settings=...,
        encrypt_internal_traffic=...,
        extended_location=...,
        health_manager_image=...,
        health_manager_node_tolerations=...,
        id=...,
        internal_certs=...,
        location=...,
        memory_profile=...,
        mode=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authImage")
    def auth_image(self) -> outputs.ContainerImageResponse: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="brokerImage")
    def broker_image(self) -> outputs.ContainerImageResponse: ...
    @_builtins.property
    @pulumi.getter(name="brokerNodeTolerations")
    def broker_node_tolerations(self) -> Optional[outputs.NodeTolerationsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def cardinality(self) -> Optional[outputs.CardinalityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[outputs.BrokerDiagnosticsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="diskBackedMessageBufferSettings")
    def disk_backed_message_buffer_settings(
        self,
    ) -> Optional[outputs.DiskBackedMessageBufferSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="encryptInternalTraffic")
    def encrypt_internal_traffic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationPropertyResponse: ...
    @_builtins.property
    @pulumi.getter(name="healthManagerImage")
    def health_manager_image(self) -> outputs.ContainerImageResponse: ...
    @_builtins.property
    @pulumi.getter(name="healthManagerNodeTolerations")
    def health_manager_node_tolerations(
        self,
    ) -> Optional[outputs.NodeTolerationsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="internalCerts")
    def internal_certs(self) -> Optional[outputs.CertManagerCertOptionsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryProfile")
    def memory_profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
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

class AwaitableGetBrokerResult(GetBrokerResult):
    def __await__(self): ...

def get_broker(
    broker_name: Optional[_builtins.str] = ...,
    mq_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBrokerResult: ...
def get_broker_output(
    broker_name: Optional[pulumi.Input[_builtins.str]] = ...,
    mq_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBrokerResult]: ...
