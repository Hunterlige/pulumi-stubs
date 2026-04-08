import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgriServiceConfigResponse",
    "AgriServiceResourcePropertiesResponse",
    "DataConnectorCredentialMapResponse",
    "DataConnectorCredentialsResponse",
    "DataManagerForAgricultureSolutionResponse",
    "InstalledSolutionMapResponse",
    "ManagedOnBehalfOfConfigurationResponse",
    "ManagedServiceIdentityResponse",
    "MarketPlaceOfferDetailsResponse",
    "MoboBrokerResourceResponse",
    "SkuResponse",
    "SolutionResponse",
    "SystemDataResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class AgriServiceConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_service_resource_id: _builtins.str,
        cosmos_db_resource_id: _builtins.str,
        instance_uri: _builtins.str,
        key_vault_resource_id: _builtins.str,
        redis_cache_resource_id: _builtins.str,
        storage_account_resource_id: _builtins.str,
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appServiceResourceId")
    def app_service_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cosmosDbResourceId")
    def cosmos_db_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceUri")
    def instance_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redisCacheResourceId")
    def redis_cache_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class AgriServiceResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        managed_on_behalf_of_configuration: outputs.ManagedOnBehalfOfConfigurationResponse,
        provisioning_state: _builtins.str,
        config: Optional[outputs.AgriServiceConfigResponse] = ...,
        data_connector_credentials: Optional[
            Sequence[outputs.DataConnectorCredentialMapResponse]
        ] = ...,
        installed_solutions: Optional[
            Sequence[outputs.InstalledSolutionMapResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedOnBehalfOfConfiguration")
    def managed_on_behalf_of_configuration(
        self,
    ) -> outputs.ManagedOnBehalfOfConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[outputs.AgriServiceConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dataConnectorCredentials")
    def data_connector_credentials(
        self,
    ) -> Optional[Sequence[outputs.DataConnectorCredentialMapResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="installedSolutions")
    def installed_solutions(
        self,
    ) -> Optional[Sequence[outputs.InstalledSolutionMapResponse]]: ...

@pulumi.output_type
class DataConnectorCredentialMapResponse(dict):
    def __init__(
        __self__, *, key: _builtins.str, value: outputs.DataConnectorCredentialsResponse
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> outputs.DataConnectorCredentialsResponse: ...

@pulumi.output_type
class DataConnectorCredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        key_name: Optional[_builtins.str] = ...,
        key_vault_uri: Optional[_builtins.str] = ...,
        key_version: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataManagerForAgricultureSolutionResponse(dict):
    def __init__(
        __self__,
        *,
        access_azure_data_manager_for_agriculture_application_id: _builtins.str,
        access_azure_data_manager_for_agriculture_application_name: _builtins.str,
        data_access_scopes: Sequence[_builtins.str],
        is_validate_input: _builtins.bool,
        market_place_offer_details: outputs.MarketPlaceOfferDetailsResponse,
        partner_id: _builtins.str,
        partner_tenant_id: _builtins.str,
        saas_application_id: _builtins.str,
        solution_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessAzureDataManagerForAgricultureApplicationId")
    def access_azure_data_manager_for_agriculture_application_id(
        self,
    ) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def access_azure_data_manager_for_agriculture_application_name(
        self,
    ) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessScopes")
    def data_access_scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isValidateInput")
    def is_validate_input(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="marketPlaceOfferDetails")
    def market_place_offer_details(self) -> outputs.MarketPlaceOfferDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerTenantId")
    def partner_tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="saasApplicationId")
    def saas_application_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="solutionId")
    def solution_id(self) -> _builtins.str: ...

@pulumi.output_type
class InstalledSolutionMapResponse(dict):
    def __init__(
        __self__, *, key: _builtins.str, value: outputs.SolutionResponse
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> outputs.SolutionResponse: ...

@pulumi.output_type
class ManagedOnBehalfOfConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, mobo_broker_resources: Sequence[outputs.MoboBrokerResourceResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="moboBrokerResources")
    def mobo_broker_resources(self) -> Sequence[outputs.MoboBrokerResourceResponse]: ...

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
class MarketPlaceOfferDetailsResponse(dict):
    def __init__(
        __self__, *, publisher_id: _builtins.str, saas_offer_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="saasOfferId")
    def saas_offer_id(self) -> _builtins.str: ...

@pulumi.output_type
class MoboBrokerResourceResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        capacity: Optional[_builtins.int] = ...,
        family: Optional[_builtins.str] = ...,
        size: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SolutionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_name: Optional[_builtins.str] = ...,
        market_place_publisher_id: Optional[_builtins.str] = ...,
        partner_id: Optional[_builtins.str] = ...,
        plan_id: Optional[_builtins.str] = ...,
        saas_subscription_id: Optional[_builtins.str] = ...,
        saas_subscription_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="marketPlacePublisherId")
    def market_place_publisher_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionId")
    def saas_subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionName")
    def saas_subscription_name(self) -> Optional[_builtins.str]: ...

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
