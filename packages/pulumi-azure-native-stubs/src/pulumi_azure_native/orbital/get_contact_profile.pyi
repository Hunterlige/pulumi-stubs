import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContactProfileResult",
    "AwaitableGetContactProfileResult",
    "get_contact_profile",
    "get_contact_profile_output",
]

@pulumi.output_type
class GetContactProfileResult:
    def __init__(
        __self__,
        auto_tracking_configuration=...,
        azure_api_version=...,
        event_hub_uri=...,
        id=...,
        links=...,
        location=...,
        minimum_elevation_degrees=...,
        minimum_viable_contact_duration=...,
        name=...,
        network_configuration=...,
        system_data=...,
        tags=...,
        third_party_configurations=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoTrackingConfiguration")
    def auto_tracking_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventHubUri")
    def event_hub_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def links(self) -> Sequence[outputs.ContactProfileLinkResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumElevationDegrees")
    def minimum_elevation_degrees(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="minimumViableContactDuration")
    def minimum_viable_contact_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> outputs.ContactProfilesPropertiesResponseNetworkConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="thirdPartyConfigurations")
    def third_party_configurations(
        self,
    ) -> Optional[Sequence[outputs.ContactProfileThirdPartyConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetContactProfileResult(GetContactProfileResult):
    def __await__(self): ...

def get_contact_profile(
    contact_profile_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContactProfileResult: ...
def get_contact_profile_output(
    contact_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContactProfileResult]: ...
