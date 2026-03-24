import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkforcePoolProviderScimTenantArgs", "WorkforcePoolProviderScimTenant"]

@pulumi.input_type
class WorkforcePoolProviderScimTenantArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        provider_id: pulumi.Input[_builtins.str],
        scim_tenant_id: pulumi.Input[_builtins.str],
        workforce_pool_id: pulumi.Input[_builtins.str],
        claim_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hard_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Input[_builtins.str]: ...
    @provider_id.setter
    def provider_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scimTenantId")
    def scim_tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @scim_tenant_id.setter
    def scim_tenant_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="claimMapping")
    def claim_mapping(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @claim_mapping.setter
    def claim_mapping(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hardDelete")
    def hard_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @hard_delete.setter
    def hard_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _WorkforcePoolProviderScimTenantState:
    def __init__(
        __self__,
        *,
        base_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        claim_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hard_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
        purge_time: Optional[pulumi.Input[_builtins.str]] = ...,
        scim_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseUri")
    def base_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_uri.setter
    def base_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="claimMapping")
    def claim_mapping(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @claim_mapping.setter
    def claim_mapping(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hardDelete")
    def hard_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @hard_delete.setter
    def hard_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="purgeTime")
    def purge_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @purge_time.setter
    def purge_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scimTenantId")
    def scim_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scim_tenant_id.setter
    def scim_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAgent")
    def service_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_agent.setter
    def service_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class WorkforcePoolProviderScimTenant(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        claim_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hard_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scim_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkforcePoolProviderScimTenantArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        base_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        claim_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hard_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
        purge_time: Optional[pulumi.Input[_builtins.str]] = ...,
        scim_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> WorkforcePoolProviderScimTenant: ...
    @_builtins.property
    @pulumi.getter(name="baseUri")
    def base_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="claimMapping")
    def claim_mapping(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hardDelete")
    def hard_delete(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="purgeTime")
    def purge_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scimTenantId")
    def scim_tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAgent")
    def service_agent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Output[_builtins.str]: ...
