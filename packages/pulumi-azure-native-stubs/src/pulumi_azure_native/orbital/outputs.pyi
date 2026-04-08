import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AuthorizedGroundstationResponse",
    "AvailableContactsResponse",
    "AvailableContactsResponseSpacecraft",
    "ContactProfileLinkChannelResponse",
    "ContactProfileLinkResponse",
    "ContactProfileThirdPartyConfigurationResponse",
    ...,
    "ContactsPropertiesResponseAntennaConfiguration",
    "ContactsPropertiesResponseContactProfile",
    ...,
    "EndPointResponse",
    "GeoCatalogPropertiesResponse",
    ...,
    "L2ConnectionsPropertiesResponseEdgeSite",
    "L2ConnectionsPropertiesResponseGroundStation",
    ...,
    "ManagedServiceIdentityResponse",
    "ResourceIdListResultResponseValue",
    "SpacecraftLinkResponse",
    "SystemDataResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class AuthorizedGroundstationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, expiration_date: _builtins.str, ground_station: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groundStation")
    def ground_station(self) -> _builtins.str: ...

@pulumi.output_type
class AvailableContactsResponse(dict):
    def __init__(
        __self__,
        *,
        end_azimuth_degrees: _builtins.float,
        end_elevation_degrees: _builtins.float,
        ground_station_name: _builtins.str,
        maximum_elevation_degrees: _builtins.float,
        rx_end_time: _builtins.str,
        rx_start_time: _builtins.str,
        start_azimuth_degrees: _builtins.float,
        start_elevation_degrees: _builtins.float,
        tx_end_time: _builtins.str,
        tx_start_time: _builtins.str,
        spacecraft: Optional[outputs.AvailableContactsResponseSpacecraft] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endAzimuthDegrees")
    def end_azimuth_degrees(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="endElevationDegrees")
    def end_elevation_degrees(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="groundStationName")
    def ground_station_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maximumElevationDegrees")
    def maximum_elevation_degrees(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="rxEndTime")
    def rx_end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rxStartTime")
    def rx_start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startAzimuthDegrees")
    def start_azimuth_degrees(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="startElevationDegrees")
    def start_elevation_degrees(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="txEndTime")
    def tx_end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="txStartTime")
    def tx_start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def spacecraft(self) -> Optional[outputs.AvailableContactsResponseSpacecraft]: ...

@pulumi.output_type
class AvailableContactsResponseSpacecraft(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ContactProfileLinkChannelResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bandwidth_m_hz: _builtins.float,
        center_frequency_m_hz: _builtins.float,
        end_point: outputs.EndPointResponse,
        name: _builtins.str,
        decoding_configuration: Optional[_builtins.str] = ...,
        demodulation_configuration: Optional[_builtins.str] = ...,
        encoding_configuration: Optional[_builtins.str] = ...,
        modulation_configuration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bandwidthMHz")
    def bandwidth_m_hz(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="centerFrequencyMHz")
    def center_frequency_m_hz(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="endPoint")
    def end_point(self) -> outputs.EndPointResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="decodingConfiguration")
    def decoding_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="demodulationConfiguration")
    def demodulation_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encodingConfiguration")
    def encoding_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modulationConfiguration")
    def modulation_configuration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContactProfileLinkResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channels: Sequence[outputs.ContactProfileLinkChannelResponse],
        direction: _builtins.str,
        name: _builtins.str,
        polarization: _builtins.str,
        eirpd_bw: Optional[_builtins.float] = ...,
        gain_over_temperature: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channels(self) -> Sequence[outputs.ContactProfileLinkChannelResponse]: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def polarization(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eirpdBW")
    def eirpd_bw(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="gainOverTemperature")
    def gain_over_temperature(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ContactProfileThirdPartyConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, mission_configuration: _builtins.str, provider_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="missionConfiguration")
    def mission_configuration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> _builtins.str: ...

@pulumi.output_type
class ContactProfilesPropertiesResponseNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, subnet_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...

@pulumi.output_type
class ContactsPropertiesResponseAntennaConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_ip: Optional[_builtins.str] = ...,
        source_ips: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIps")
    def source_ips(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ContactsPropertiesResponseContactProfile(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class EdgeSitesPropertiesResponseGlobalCommunicationsSite(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class EndPointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_point_name: _builtins.str,
        ip_address: _builtins.str,
        port: _builtins.str,
        protocol: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endPointName")
    def end_point_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class GeoCatalogPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog_uri: _builtins.str,
        provisioning_state: _builtins.str,
        auto_generated_domain_name_label_scope: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogUri")
    def catalog_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GroundStationsPropertiesResponseGlobalCommunicationsSite(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class L2ConnectionsPropertiesResponseEdgeSite(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class L2ConnectionsPropertiesResponseGroundStation(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class L2ConnectionsPropertiesResponseGroundStationPartnerRouter(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class ResourceIdListResultResponseValue(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpacecraftLinkResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorizations: Sequence[outputs.AuthorizedGroundstationResponse],
        bandwidth_m_hz: _builtins.float,
        center_frequency_m_hz: _builtins.float,
        direction: _builtins.str,
        name: _builtins.str,
        polarization: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorizations(self) -> Sequence[outputs.AuthorizedGroundstationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="bandwidthMHz")
    def bandwidth_m_hz(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="centerFrequencyMHz")
    def center_frequency_m_hz(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def polarization(self) -> _builtins.str: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
