import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPartnerDestinationResult",
    "AwaitableGetPartnerDestinationResult",
    "get_partner_destination",
    "get_partner_destination_output",
]

@pulumi.output_type
class GetPartnerDestinationResult:
    def __init__(
        __self__,
        activation_state=...,
        azure_api_version=...,
        endpoint_base_url=...,
        endpoint_service_context=...,
        expiration_time_if_not_activated_utc=...,
        id=...,
        location=...,
        message_for_activation=...,
        name=...,
        partner_registration_immutable_id=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointBaseUrl")
    def endpoint_base_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointServiceContext")
    def endpoint_service_context(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(self) -> Optional[_builtins.str]: ...
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

class AwaitableGetPartnerDestinationResult(GetPartnerDestinationResult):
    def __await__(self): ...

def get_partner_destination(
    partner_destination_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPartnerDestinationResult: ...
def get_partner_destination_output(
    partner_destination_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPartnerDestinationResult]: ...
