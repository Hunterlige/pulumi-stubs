import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AddressResponse",
    "AsymmetricEncryptedSecretResponse",
    "AuthenticationResponse",
    "AzureContainerInfoResponse",
    "ClientAccessRightResponse",
    "CniConfigResponse",
    "ComputeResourceResponse",
    "ContactDetailsResponse",
    "DataResidencyResponse",
    "EdgeProfileResponse",
    "EdgeProfileSubscriptionResponse",
    "EtcdInfoResponse",
    "FileSourceInfoResponse",
    "ImageRepositoryCredentialResponse",
    "IoTDeviceInfoResponse",
    "IoTEdgeAgentInfoResponse",
    "KubernetesClusterInfoResponse",
    "KubernetesIPConfigurationResponse",
    "KubernetesRoleComputeResponse",
    "KubernetesRoleNetworkResponse",
    "KubernetesRoleResourcesResponse",
    "KubernetesRoleStorageClassInfoResponse",
    "KubernetesRoleStorageResponse",
    "LoadBalancerConfigResponse",
    "MetricConfigurationResponse",
    "MetricCounterResponse",
    "MetricCounterSetResponse",
    "MetricDimensionResponse",
    "MountPointMapResponse",
    "NodeInfoResponse",
    "OrderStatusResponse",
    "PeriodicTimerSourceInfoResponse",
    "RefreshDetailsResponse",
    "ResourceIdentityResponse",
    "ResourceMoveDetailsResponse",
    "RoleSinkInfoResponse",
    "SecretResponse",
    "ShareAccessRightResponse",
    "SkuResponse",
    "SubscriptionRegisteredFeaturesResponse",
    "SymmetricKeyResponse",
    "SystemDataResponse",
    "TrackingInfoResponse",
    "UserAccessRightResponse",
]

@pulumi.output_type
class AddressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        country: _builtins.str,
        address_line1: Optional[_builtins.str] = ...,
        address_line2: Optional[_builtins.str] = ...,
        address_line3: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AsymmetricEncryptedSecretResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_algorithm: _builtins.str,
        value: _builtins.str,
        encryption_cert_thumbprint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionCertThumbprint")
    def encryption_cert_thumbprint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, symmetric_key: Optional[outputs.SymmetricKeyResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="symmetricKey")
    def symmetric_key(self) -> Optional[outputs.SymmetricKeyResponse]: ...

@pulumi.output_type
class AzureContainerInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_name: _builtins.str,
        data_format: _builtins.str,
        storage_account_credential_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> _builtins.str: ...

@pulumi.output_type
class ClientAccessRightResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, access_permission: _builtins.str, client: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPermission")
    def access_permission(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> _builtins.str: ...

@pulumi.output_type
class CniConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pod_subnet: _builtins.str,
        service_subnet: _builtins.str,
        type: _builtins.str,
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podSubnet")
    def pod_subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceSubnet")
    def service_subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class ComputeResourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, memory_in_gb: _builtins.float, processor_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryInGB")
    def memory_in_gb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="processorCount")
    def processor_count(self) -> _builtins.int: ...

@pulumi.output_type
class ContactDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        company_name: _builtins.str,
        contact_person: _builtins.str,
        email_list: Sequence[_builtins.str],
        phone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactPerson")
    def contact_person(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="emailList")
    def email_list(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def phone(self) -> _builtins.str: ...

@pulumi.output_type
class DataResidencyResponse(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeProfileResponse(dict):
    def __init__(
        __self__,
        *,
        subscription: Optional[outputs.EdgeProfileSubscriptionResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subscription(self) -> Optional[outputs.EdgeProfileSubscriptionResponse]: ...

@pulumi.output_type
class EdgeProfileSubscriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        location_placement_id: Optional[_builtins.str] = ...,
        quota_id: Optional[_builtins.str] = ...,
        registered_features: Optional[
            Sequence[outputs.SubscriptionRegisteredFeaturesResponse]
        ] = ...,
        registration_date: Optional[_builtins.str] = ...,
        registration_id: Optional[_builtins.str] = ...,
        serialized_details: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        subscription_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="locationPlacementId")
    def location_placement_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registeredFeatures")
    def registered_features(
        self,
    ) -> Optional[Sequence[outputs.SubscriptionRegisteredFeaturesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="registrationDate")
    def registration_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationId")
    def registration_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serializedDetails")
    def serialized_details(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EtcdInfoResponse(dict):
    def __init__(__self__, *, type: _builtins.str, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class FileSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, share_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shareId")
    def share_id(self) -> _builtins.str: ...

@pulumi.output_type
class ImageRepositoryCredentialResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_repository_url: _builtins.str,
        user_name: _builtins.str,
        password: Optional[outputs.AsymmetricEncryptedSecretResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageRepositoryUrl")
    def image_repository_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[outputs.AsymmetricEncryptedSecretResponse]: ...

@pulumi.output_type
class IoTDeviceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_id: _builtins.str,
        io_t_host_hub: _builtins.str,
        authentication: Optional[outputs.AuthenticationResponse] = ...,
        io_t_host_hub_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ioTHostHub")
    def io_t_host_hub(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.AuthenticationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="ioTHostHubId")
    def io_t_host_hub_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IoTEdgeAgentInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_name: _builtins.str,
        tag: _builtins.str,
        image_repository: Optional[outputs.ImageRepositoryCredentialResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageRepository")
    def image_repository(
        self,
    ) -> Optional[outputs.ImageRepositoryCredentialResponse]: ...

@pulumi.output_type
class KubernetesClusterInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        etcd_info: outputs.EtcdInfoResponse,
        nodes: Sequence[outputs.NodeInfoResponse],
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="etcdInfo")
    def etcd_info(self) -> outputs.EtcdInfoResponse: ...
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Sequence[outputs.NodeInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class KubernetesIPConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, port: _builtins.str, ip_address: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KubernetesRoleComputeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        memory_in_bytes: _builtins.float,
        processor_count: _builtins.int,
        vm_profile: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryInBytes")
    def memory_in_bytes(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="processorCount")
    def processor_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="vmProfile")
    def vm_profile(self) -> _builtins.str: ...

@pulumi.output_type
class KubernetesRoleNetworkResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cni_config: outputs.CniConfigResponse,
        load_balancer_config: outputs.LoadBalancerConfigResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cniConfig")
    def cni_config(self) -> outputs.CniConfigResponse: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerConfig")
    def load_balancer_config(self) -> outputs.LoadBalancerConfigResponse: ...

@pulumi.output_type
class KubernetesRoleResourcesResponse(dict):
    def __init__(
        __self__,
        *,
        compute: outputs.KubernetesRoleComputeResponse,
        network: outputs.KubernetesRoleNetworkResponse,
        storage: Optional[outputs.KubernetesRoleStorageResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def compute(self) -> outputs.KubernetesRoleComputeResponse: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> outputs.KubernetesRoleNetworkResponse: ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[outputs.KubernetesRoleStorageResponse]: ...

@pulumi.output_type
class KubernetesRoleStorageClassInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        posix_compliant: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="posixCompliant")
    def posix_compliant(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class KubernetesRoleStorageResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_classes: Sequence[outputs.KubernetesRoleStorageClassInfoResponse],
        endpoints: Optional[Sequence[outputs.MountPointMapResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageClasses")
    def storage_classes(
        self,
    ) -> Sequence[outputs.KubernetesRoleStorageClassInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[outputs.MountPointMapResponse]]: ...

@pulumi.output_type
class LoadBalancerConfigResponse(dict):
    def __init__(__self__, *, type: _builtins.str, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class MetricConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        counter_sets: Sequence[outputs.MetricCounterSetResponse],
        resource_id: _builtins.str,
        mdm_account: Optional[_builtins.str] = ...,
        metric_name_space: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="counterSets")
    def counter_sets(self) -> Sequence[outputs.MetricCounterSetResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mdmAccount")
    def mdm_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricNameSpace")
    def metric_name_space(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MetricCounterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        additional_dimensions: Optional[
            Sequence[outputs.MetricDimensionResponse]
        ] = ...,
        dimension_filter: Optional[Sequence[outputs.MetricDimensionResponse]] = ...,
        instance: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalDimensions")
    def additional_dimensions(
        self,
    ) -> Optional[Sequence[outputs.MetricDimensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dimensionFilter")
    def dimension_filter(
        self,
    ) -> Optional[Sequence[outputs.MetricDimensionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MetricCounterSetResponse(dict):
    def __init__(
        __self__, *, counters: Sequence[outputs.MetricCounterResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def counters(self) -> Sequence[outputs.MetricCounterResponse]: ...

@pulumi.output_type
class MetricDimensionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, source_name: _builtins.str, source_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str: ...

@pulumi.output_type
class MountPointMapResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mount_point: _builtins.str,
        mount_type: _builtins.str,
        role_id: _builtins.str,
        role_type: _builtins.str,
        share_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mountType")
    def mount_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareId")
    def share_id(self) -> _builtins.str: ...

@pulumi.output_type
class NodeInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        ip_configuration: Optional[
            Sequence[outputs.KubernetesIPConfigurationResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(
        self,
    ) -> Optional[Sequence[outputs.KubernetesIPConfigurationResponse]]: ...

@pulumi.output_type
class OrderStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_order_details: Mapping[str, _builtins.str],
        status: _builtins.str,
        tracking_information: outputs.TrackingInfoResponse,
        update_date_time: _builtins.str,
        comments: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalOrderDetails")
    def additional_order_details(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trackingInformation")
    def tracking_information(self) -> outputs.TrackingInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="updateDateTime")
    def update_date_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comments(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PeriodicTimerSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule: _builtins.str,
        start_time: _builtins.str,
        topic: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RefreshDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_manifest_file: Optional[_builtins.str] = ...,
        in_progress_refresh_job_id: Optional[_builtins.str] = ...,
        last_completed_refresh_job_time_in_utc: Optional[_builtins.str] = ...,
        last_job: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorManifestFile")
    def error_manifest_file(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inProgressRefreshJobId")
    def in_progress_refresh_job_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastCompletedRefreshJobTimeInUTC")
    def last_completed_refresh_job_time_in_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastJob")
    def last_job(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceMoveDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operation_in_progress: Optional[_builtins.str] = ...,
        operation_in_progress_lock_timeout_in_utc: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operationInProgress")
    def operation_in_progress(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationInProgressLockTimeoutInUTC")
    def operation_in_progress_lock_timeout_in_utc(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoleSinkInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, role_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> _builtins.str: ...

@pulumi.output_type
class SecretResponse(dict):
    def __init__(
        __self__,
        *,
        encrypted_secret: Optional[outputs.AsymmetricEncryptedSecretResponse] = ...,
        key_vault_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptedSecret")
    def encrypted_secret(
        self,
    ) -> Optional[outputs.AsymmetricEncryptedSecretResponse]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ShareAccessRightResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, access_type: _builtins.str, share_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareId")
    def share_id(self) -> _builtins.str: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubscriptionRegisteredFeaturesResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SymmetricKeyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_string: Optional[outputs.AsymmetricEncryptedSecretResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(
        self,
    ) -> Optional[outputs.AsymmetricEncryptedSecretResponse]: ...

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
class TrackingInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        carrier_name: Optional[_builtins.str] = ...,
        serial_number: Optional[_builtins.str] = ...,
        tracking_id: Optional[_builtins.str] = ...,
        tracking_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackingUrl")
    def tracking_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAccessRightResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, access_type: _builtins.str, user_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str: ...
