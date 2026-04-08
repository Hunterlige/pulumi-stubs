import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AddressArgs",
    "AddressArgsDict",
    "AsymmetricEncryptedSecretArgs",
    "AsymmetricEncryptedSecretArgsDict",
    "AuthenticationArgs",
    "AuthenticationArgsDict",
    "AzureContainerInfoArgs",
    "AzureContainerInfoArgsDict",
    "ClientAccessRightArgs",
    "ClientAccessRightArgsDict",
    "ComputeResourceArgs",
    "ComputeResourceArgsDict",
    "ContactDetailsArgs",
    "ContactDetailsArgsDict",
    "DataResidencyArgs",
    "DataResidencyArgsDict",
    "FileSourceInfoArgs",
    "FileSourceInfoArgsDict",
    "ImageRepositoryCredentialArgs",
    "ImageRepositoryCredentialArgsDict",
    "IoTDeviceInfoArgs",
    "IoTDeviceInfoArgsDict",
    "IoTEdgeAgentInfoArgs",
    "IoTEdgeAgentInfoArgsDict",
    "KubernetesClusterInfoArgs",
    "KubernetesClusterInfoArgsDict",
    "KubernetesRoleComputeArgs",
    "KubernetesRoleComputeArgsDict",
    "KubernetesRoleResourcesArgs",
    "KubernetesRoleResourcesArgsDict",
    "KubernetesRoleStorageArgs",
    "KubernetesRoleStorageArgsDict",
    "MetricConfigurationArgs",
    "MetricConfigurationArgsDict",
    "MetricCounterSetArgs",
    "MetricCounterSetArgsDict",
    "MetricCounterArgs",
    "MetricCounterArgsDict",
    "MetricDimensionArgs",
    "MetricDimensionArgsDict",
    "MountPointMapArgs",
    "MountPointMapArgsDict",
    "PeriodicTimerSourceInfoArgs",
    "PeriodicTimerSourceInfoArgsDict",
    "RefreshDetailsArgs",
    "RefreshDetailsArgsDict",
    "ResourceIdentityArgs",
    "ResourceIdentityArgsDict",
    "RoleSinkInfoArgs",
    "RoleSinkInfoArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SymmetricKeyArgs",
    "SymmetricKeyArgsDict",
    "UserAccessRightArgs",
    "UserAccessRightArgsDict",
]

class AddressArgsDict(TypedDict):
    country: pulumi.Input[_builtins.str]
    address_line1: NotRequired[pulumi.Input[_builtins.str]]
    address_line2: NotRequired[pulumi.Input[_builtins.str]]
    address_line3: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AddressArgs:
    def __init__(
        __self__,
        *,
        country: pulumi.Input[_builtins.str],
        address_line1: Optional[pulumi.Input[_builtins.str]] = ...,
        address_line2: Optional[pulumi.Input[_builtins.str]] = ...,
        address_line3: Optional[pulumi.Input[_builtins.str]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> pulumi.Input[_builtins.str]: ...
    @country.setter
    def country(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_line3.setter
    def address_line3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AsymmetricEncryptedSecretArgsDict(TypedDict):
    encryption_algorithm: pulumi.Input[Union[_builtins.str, EncryptionAlgorithm]]
    value: pulumi.Input[_builtins.str]
    encryption_cert_thumbprint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AsymmetricEncryptedSecretArgs:
    def __init__(
        __self__,
        *,
        encryption_algorithm: pulumi.Input[Union[_builtins.str, EncryptionAlgorithm]],
        value: pulumi.Input[_builtins.str],
        encryption_cert_thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(
        self,
    ) -> pulumi.Input[Union[_builtins.str, EncryptionAlgorithm]]: ...
    @encryption_algorithm.setter
    def encryption_algorithm(
        self, value: pulumi.Input[Union[_builtins.str, EncryptionAlgorithm]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionCertThumbprint")
    def encryption_cert_thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_cert_thumbprint.setter
    def encryption_cert_thumbprint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class AuthenticationArgsDict(TypedDict):
    symmetric_key: NotRequired[pulumi.Input[SymmetricKeyArgsDict]]

@pulumi.input_type
class AuthenticationArgs:
    def __init__(
        __self__, *, symmetric_key: Optional[pulumi.Input[SymmetricKeyArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="symmetricKey")
    def symmetric_key(self) -> Optional[pulumi.Input[SymmetricKeyArgs]]: ...
    @symmetric_key.setter
    def symmetric_key(self, value: Optional[pulumi.Input[SymmetricKeyArgs]]): ...

class AzureContainerInfoArgsDict(TypedDict):
    container_name: pulumi.Input[_builtins.str]
    data_format: pulumi.Input[Union[_builtins.str, AzureContainerDataFormat]]
    storage_account_credential_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureContainerInfoArgs:
    def __init__(
        __self__,
        *,
        container_name: pulumi.Input[_builtins.str],
        data_format: pulumi.Input[Union[_builtins.str, AzureContainerDataFormat]],
        storage_account_credential_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]: ...
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AzureContainerDataFormat]]: ...
    @data_format.setter
    def data_format(
        self, value: pulumi.Input[Union[_builtins.str, AzureContainerDataFormat]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> pulumi.Input[_builtins.str]: ...
    @storage_account_credential_id.setter
    def storage_account_credential_id(self, value: pulumi.Input[_builtins.str]): ...

class ClientAccessRightArgsDict(TypedDict):
    access_permission: pulumi.Input[Union[_builtins.str, ClientPermissionType]]
    client: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClientAccessRightArgs:
    def __init__(
        __self__,
        *,
        access_permission: pulumi.Input[Union[_builtins.str, ClientPermissionType]],
        client: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPermission")
    def access_permission(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ClientPermissionType]]: ...
    @access_permission.setter
    def access_permission(
        self, value: pulumi.Input[Union[_builtins.str, ClientPermissionType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> pulumi.Input[_builtins.str]: ...
    @client.setter
    def client(self, value: pulumi.Input[_builtins.str]): ...

class ComputeResourceArgsDict(TypedDict):
    memory_in_gb: pulumi.Input[_builtins.float]
    processor_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class ComputeResourceArgs:
    def __init__(
        __self__,
        *,
        memory_in_gb: pulumi.Input[_builtins.float],
        processor_count: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryInGB")
    def memory_in_gb(self) -> pulumi.Input[_builtins.float]: ...
    @memory_in_gb.setter
    def memory_in_gb(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="processorCount")
    def processor_count(self) -> pulumi.Input[_builtins.int]: ...
    @processor_count.setter
    def processor_count(self, value: pulumi.Input[_builtins.int]): ...

class ContactDetailsArgsDict(TypedDict):
    company_name: pulumi.Input[_builtins.str]
    contact_person: pulumi.Input[_builtins.str]
    email_list: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    phone: pulumi.Input[_builtins.str]

@pulumi.input_type
class ContactDetailsArgs:
    def __init__(
        __self__,
        *,
        company_name: pulumi.Input[_builtins.str],
        contact_person: pulumi.Input[_builtins.str],
        email_list: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        phone: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> pulumi.Input[_builtins.str]: ...
    @company_name.setter
    def company_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contactPerson")
    def contact_person(self) -> pulumi.Input[_builtins.str]: ...
    @contact_person.setter
    def contact_person(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="emailList")
    def email_list(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @email_list.setter
    def email_list(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def phone(self) -> pulumi.Input[_builtins.str]: ...
    @phone.setter
    def phone(self, value: pulumi.Input[_builtins.str]): ...

class DataResidencyArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, DataResidencyType]]]

@pulumi.input_type
class DataResidencyArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, DataResidencyType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataResidencyType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataResidencyType]]]
    ): ...

class FileSourceInfoArgsDict(TypedDict):
    share_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class FileSourceInfoArgs:
    def __init__(__self__, *, share_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shareId")
    def share_id(self) -> pulumi.Input[_builtins.str]: ...
    @share_id.setter
    def share_id(self, value: pulumi.Input[_builtins.str]): ...

class ImageRepositoryCredentialArgsDict(TypedDict):
    image_repository_url: pulumi.Input[_builtins.str]
    user_name: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[AsymmetricEncryptedSecretArgsDict]]

@pulumi.input_type
class ImageRepositoryCredentialArgs:
    def __init__(
        __self__,
        *,
        image_repository_url: pulumi.Input[_builtins.str],
        user_name: pulumi.Input[_builtins.str],
        password: Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageRepositoryUrl")
    def image_repository_url(self) -> pulumi.Input[_builtins.str]: ...
    @image_repository_url.setter
    def image_repository_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]: ...
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]]: ...
    @password.setter
    def password(
        self, value: Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]]
    ): ...

class IoTDeviceInfoArgsDict(TypedDict):
    device_id: pulumi.Input[_builtins.str]
    io_t_host_hub: pulumi.Input[_builtins.str]
    authentication: NotRequired[pulumi.Input[AuthenticationArgsDict]]
    io_t_host_hub_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IoTDeviceInfoArgs:
    def __init__(
        __self__,
        *,
        device_id: pulumi.Input[_builtins.str],
        io_t_host_hub: pulumi.Input[_builtins.str],
        authentication: Optional[pulumi.Input[AuthenticationArgs]] = ...,
        io_t_host_hub_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Input[_builtins.str]: ...
    @device_id.setter
    def device_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ioTHostHub")
    def io_t_host_hub(self) -> pulumi.Input[_builtins.str]: ...
    @io_t_host_hub.setter
    def io_t_host_hub(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[AuthenticationArgs]]: ...
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[AuthenticationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ioTHostHubId")
    def io_t_host_hub_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @io_t_host_hub_id.setter
    def io_t_host_hub_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IoTEdgeAgentInfoArgsDict(TypedDict):
    image_name: pulumi.Input[_builtins.str]
    tag: pulumi.Input[_builtins.str]
    image_repository: NotRequired[pulumi.Input[ImageRepositoryCredentialArgsDict]]

@pulumi.input_type
class IoTEdgeAgentInfoArgs:
    def __init__(
        __self__,
        *,
        image_name: pulumi.Input[_builtins.str],
        tag: pulumi.Input[_builtins.str],
        image_repository: Optional[pulumi.Input[ImageRepositoryCredentialArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]: ...
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> pulumi.Input[_builtins.str]: ...
    @tag.setter
    def tag(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="imageRepository")
    def image_repository(
        self,
    ) -> Optional[pulumi.Input[ImageRepositoryCredentialArgs]]: ...
    @image_repository.setter
    def image_repository(
        self, value: Optional[pulumi.Input[ImageRepositoryCredentialArgs]]
    ): ...

class KubernetesClusterInfoArgsDict(TypedDict):
    version: pulumi.Input[_builtins.str]

@pulumi.input_type
class KubernetesClusterInfoArgs:
    def __init__(__self__, *, version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...

class KubernetesRoleComputeArgsDict(TypedDict):
    vm_profile: pulumi.Input[_builtins.str]

@pulumi.input_type
class KubernetesRoleComputeArgs:
    def __init__(__self__, *, vm_profile: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vmProfile")
    def vm_profile(self) -> pulumi.Input[_builtins.str]: ...
    @vm_profile.setter
    def vm_profile(self, value: pulumi.Input[_builtins.str]): ...

class KubernetesRoleResourcesArgsDict(TypedDict):
    compute: pulumi.Input[KubernetesRoleComputeArgsDict]
    storage: NotRequired[pulumi.Input[KubernetesRoleStorageArgsDict]]

@pulumi.input_type
class KubernetesRoleResourcesArgs:
    def __init__(
        __self__,
        *,
        compute: pulumi.Input[KubernetesRoleComputeArgs],
        storage: Optional[pulumi.Input[KubernetesRoleStorageArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def compute(self) -> pulumi.Input[KubernetesRoleComputeArgs]: ...
    @compute.setter
    def compute(self, value: pulumi.Input[KubernetesRoleComputeArgs]): ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[KubernetesRoleStorageArgs]]: ...
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[KubernetesRoleStorageArgs]]): ...

class KubernetesRoleStorageArgsDict(TypedDict):
    endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[MountPointMapArgsDict]]]]

@pulumi.input_type
class KubernetesRoleStorageArgs:
    def __init__(
        __self__,
        *,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[MountPointMapArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MountPointMapArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MountPointMapArgs]]]]
    ): ...

class MetricConfigurationArgsDict(TypedDict):
    counter_sets: pulumi.Input[Sequence[pulumi.Input[MetricCounterSetArgsDict]]]
    resource_id: pulumi.Input[_builtins.str]
    mdm_account: NotRequired[pulumi.Input[_builtins.str]]
    metric_name_space: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetricConfigurationArgs:
    def __init__(
        __self__,
        *,
        counter_sets: pulumi.Input[Sequence[pulumi.Input[MetricCounterSetArgs]]],
        resource_id: pulumi.Input[_builtins.str],
        mdm_account: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_name_space: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="counterSets")
    def counter_sets(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[MetricCounterSetArgs]]]: ...
    @counter_sets.setter
    def counter_sets(
        self, value: pulumi.Input[Sequence[pulumi.Input[MetricCounterSetArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mdmAccount")
    def mdm_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mdm_account.setter
    def mdm_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricNameSpace")
    def metric_name_space(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_name_space.setter
    def metric_name_space(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetricCounterSetArgsDict(TypedDict):
    counters: pulumi.Input[Sequence[pulumi.Input[MetricCounterArgsDict]]]

@pulumi.input_type
class MetricCounterSetArgs:
    def __init__(
        __self__, *, counters: pulumi.Input[Sequence[pulumi.Input[MetricCounterArgs]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def counters(self) -> pulumi.Input[Sequence[pulumi.Input[MetricCounterArgs]]]: ...
    @counters.setter
    def counters(
        self, value: pulumi.Input[Sequence[pulumi.Input[MetricCounterArgs]]]
    ): ...

class MetricCounterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    additional_dimensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgsDict]]]
    ]
    dimension_filter: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgsDict]]]
    ]
    instance: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetricCounterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        additional_dimensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]
        ] = ...,
        dimension_filter: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]
        ] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalDimensions")
    def additional_dimensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]]: ...
    @additional_dimensions.setter
    def additional_dimensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dimensionFilter")
    def dimension_filter(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]]: ...
    @dimension_filter.setter
    def dimension_filter(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetricDimensionArgsDict(TypedDict):
    source_name: pulumi.Input[_builtins.str]
    source_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class MetricDimensionArgs:
    def __init__(
        __self__,
        *,
        source_name: pulumi.Input[_builtins.str],
        source_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Input[_builtins.str]: ...
    @source_name.setter
    def source_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Input[_builtins.str]: ...
    @source_type.setter
    def source_type(self, value: pulumi.Input[_builtins.str]): ...

class MountPointMapArgsDict(TypedDict):
    share_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class MountPointMapArgs:
    def __init__(__self__, *, share_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shareId")
    def share_id(self) -> pulumi.Input[_builtins.str]: ...
    @share_id.setter
    def share_id(self, value: pulumi.Input[_builtins.str]): ...

class PeriodicTimerSourceInfoArgsDict(TypedDict):
    schedule: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[_builtins.str]
    topic: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PeriodicTimerSourceInfoArgs:
    def __init__(
        __self__,
        *,
        schedule: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[_builtins.str],
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[_builtins.str]: ...
    @schedule.setter
    def schedule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RefreshDetailsArgsDict(TypedDict):
    error_manifest_file: NotRequired[pulumi.Input[_builtins.str]]
    in_progress_refresh_job_id: NotRequired[pulumi.Input[_builtins.str]]
    last_completed_refresh_job_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    last_job: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RefreshDetailsArgs:
    def __init__(
        __self__,
        *,
        error_manifest_file: Optional[pulumi.Input[_builtins.str]] = ...,
        in_progress_refresh_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_completed_refresh_job_time_in_utc: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        last_job: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorManifestFile")
    def error_manifest_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_manifest_file.setter
    def error_manifest_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inProgressRefreshJobId")
    def in_progress_refresh_job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @in_progress_refresh_job_id.setter
    def in_progress_refresh_job_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastCompletedRefreshJobTimeInUTC")
    def last_completed_refresh_job_time_in_utc(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_completed_refresh_job_time_in_utc.setter
    def last_completed_refresh_job_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastJob")
    def last_job(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_job.setter
    def last_job(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, MsiIdentityType]]]

@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, MsiIdentityType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, MsiIdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MsiIdentityType]]]
    ): ...

class RoleSinkInfoArgsDict(TypedDict):
    role_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class RoleSinkInfoArgs:
    def __init__(__self__, *, role_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Input[_builtins.str]: ...
    @role_id.setter
    def role_id(self, value: pulumi.Input[_builtins.str]): ...

class SkuArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[Union[_builtins.str, SkuName]]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, SkuTier]]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[Union[_builtins.str, SkuName]]] = ...,
        tier: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuName]]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuName]]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]): ...

class SymmetricKeyArgsDict(TypedDict):
    connection_string: NotRequired[pulumi.Input[AsymmetricEncryptedSecretArgsDict]]

@pulumi.input_type
class SymmetricKeyArgs:
    def __init__(
        __self__,
        *,
        connection_string: Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(
        self,
    ) -> Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]]: ...
    @connection_string.setter
    def connection_string(
        self, value: Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]]
    ): ...

class UserAccessRightArgsDict(TypedDict):
    access_type: pulumi.Input[Union[_builtins.str, ShareAccessType]]
    user_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class UserAccessRightArgs:
    def __init__(
        __self__,
        *,
        access_type: pulumi.Input[Union[_builtins.str, ShareAccessType]],
        user_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> pulumi.Input[Union[_builtins.str, ShareAccessType]]: ...
    @access_type.setter
    def access_type(
        self, value: pulumi.Input[Union[_builtins.str, ShareAccessType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[_builtins.str]: ...
    @user_id.setter
    def user_id(self, value: pulumi.Input[_builtins.str]): ...
