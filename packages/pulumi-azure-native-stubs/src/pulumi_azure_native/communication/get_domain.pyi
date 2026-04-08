import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDomainResult",
    "AwaitableGetDomainResult",
    "get_domain",
    "get_domain_output",
]

@pulumi.output_type
class GetDomainResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_location=...,
        domain_management=...,
        from_sender_domain=...,
        id=...,
        location=...,
        mail_from_sender_domain=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        user_engagement_tracking=...,
        verification_records=...,
        verification_states=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainManagement")
    def domain_management(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fromSenderDomain")
    def from_sender_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mailFromSenderDomain")
    def mail_from_sender_domain(self) -> _builtins.str: ...
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
    @_builtins.property
    @pulumi.getter(name="userEngagementTracking")
    def user_engagement_tracking(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="verificationRecords")
    def verification_records(
        self,
    ) -> outputs.DomainPropertiesResponseVerificationRecords: ...
    @_builtins.property
    @pulumi.getter(name="verificationStates")
    def verification_states(
        self,
    ) -> outputs.DomainPropertiesResponseVerificationStates: ...

class AwaitableGetDomainResult(GetDomainResult):
    def __await__(self): ...

def get_domain(
    domain_name: Optional[_builtins.str] = ...,
    email_service_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDomainResult: ...
def get_domain_output(
    domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
    email_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDomainResult]: ...
