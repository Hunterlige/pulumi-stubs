import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetJobResult", "AwaitableGetJobResult", "get_job", "get_job_output"]

@pulumi.output_type
class GetJobResult:
    def __init__(
        __self__,
        azure_api_version=...,
        configuration=...,
        environment_id=...,
        event_stream_endpoint=...,
        extended_location=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        outbound_ip_addresses=...,
        provisioning_state=...,
        running_state=...,
        system_data=...,
        tags=...,
        template=...,
        type=...,
        workload_profile_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[outputs.JobConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventStreamEndpoint")
    def event_stream_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
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
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outboundIpAddresses")
    def outbound_ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runningState")
    def running_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> Optional[outputs.JobTemplateResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workloadProfileName")
    def workload_profile_name(self) -> Optional[_builtins.str]: ...

class AwaitableGetJobResult(GetJobResult):
    def __await__(self): ...

def get_job(
    job_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetJobResult: ...
def get_job_output(
    job_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetJobResult]: ...
