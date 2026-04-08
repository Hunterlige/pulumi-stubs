import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EndpointArgs", "Endpoint"]

@pulumi.input_type
class EndpointArgs:
    def __init__(
        __self__,
        *,
        origins: pulumi.Input[Sequence[pulumi.Input[DeepCreatedOriginArgs]]],
        profile_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        content_types_to_compress: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_origin_group: Optional[pulumi.Input[ResourceReferenceArgs]] = ...,
        delivery_policy: Optional[
            pulumi.Input[EndpointPropertiesUpdateParametersDeliveryPolicyArgs]
        ] = ...,
        endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        geo_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[GeoFilterArgs]]]
        ] = ...,
        is_compression_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_http_allowed: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_https_allowed: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        optimization_type: Optional[
            pulumi.Input[Union[_builtins.str, OptimizationType]]
        ] = ...,
        origin_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[DeepCreatedOriginGroupArgs]]]
        ] = ...,
        origin_host_header: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_path: Optional[pulumi.Input[_builtins.str]] = ...,
        probe_path: Optional[pulumi.Input[_builtins.str]] = ...,
        query_string_caching_behavior: Optional[
            pulumi.Input[QueryStringCachingBehavior]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        url_signing_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[UrlSigningKeyArgs]]]
        ] = ...,
        web_application_firewall_policy_link: Optional[
            pulumi.Input[
                EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def origins(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[DeepCreatedOriginArgs]]]: ...
    @origins.setter
    def origins(
        self, value: pulumi.Input[Sequence[pulumi.Input[DeepCreatedOriginArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contentTypesToCompress")
    def content_types_to_compress(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @content_types_to_compress.setter
    def content_types_to_compress(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultOriginGroup")
    def default_origin_group(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]: ...
    @default_origin_group.setter
    def default_origin_group(
        self, value: Optional[pulumi.Input[ResourceReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(
        self,
    ) -> Optional[
        pulumi.Input[EndpointPropertiesUpdateParametersDeliveryPolicyArgs]
    ]: ...
    @delivery_policy.setter
    def delivery_policy(
        self,
        value: Optional[
            pulumi.Input[EndpointPropertiesUpdateParametersDeliveryPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_name.setter
    def endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="geoFilters")
    def geo_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GeoFilterArgs]]]]: ...
    @geo_filters.setter
    def geo_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GeoFilterArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_compression_enabled.setter
    def is_compression_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isHttpAllowed")
    def is_http_allowed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_http_allowed.setter
    def is_http_allowed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isHttpsAllowed")
    def is_https_allowed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_https_allowed.setter
    def is_https_allowed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="optimizationType")
    def optimization_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OptimizationType]]]: ...
    @optimization_type.setter
    def optimization_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OptimizationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeepCreatedOriginGroupArgs]]]]: ...
    @origin_groups.setter
    def origin_groups(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DeepCreatedOriginGroupArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_host_header.setter
    def origin_host_header(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_path.setter
    def origin_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="probePath")
    def probe_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @probe_path.setter
    def probe_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryStringCachingBehavior")
    def query_string_caching_behavior(
        self,
    ) -> Optional[pulumi.Input[QueryStringCachingBehavior]]: ...
    @query_string_caching_behavior.setter
    def query_string_caching_behavior(
        self, value: Optional[pulumi.Input[QueryStringCachingBehavior]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlSigningKeys")
    def url_signing_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UrlSigningKeyArgs]]]]: ...
    @url_signing_keys.setter
    def url_signing_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UrlSigningKeyArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallPolicyLink")
    def web_application_firewall_policy_link(
        self,
    ) -> Optional[
        pulumi.Input[
            EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkArgs
        ]
    ]: ...
    @web_application_firewall_policy_link.setter
    def web_application_firewall_policy_link(
        self,
        value: Optional[
            pulumi.Input[
                EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkArgs
            ]
        ],
    ): ...

@pulumi.type_token("azure-native:cdn:Endpoint")
class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        content_types_to_compress: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_origin_group: Optional[
            pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]
        ] = ...,
        delivery_policy: Optional[
            pulumi.Input[
                Union[
                    EndpointPropertiesUpdateParametersDeliveryPolicyArgs,
                    EndpointPropertiesUpdateParametersDeliveryPolicyArgsDict,
                ]
            ]
        ] = ...,
        endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        geo_filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[GeoFilterArgs, GeoFilterArgsDict]]]
            ]
        ] = ...,
        is_compression_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_http_allowed: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_https_allowed: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        optimization_type: Optional[
            pulumi.Input[Union[_builtins.str, OptimizationType]]
        ] = ...,
        origin_groups: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DeepCreatedOriginGroupArgs, DeepCreatedOriginGroupArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        origin_host_header: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_path: Optional[pulumi.Input[_builtins.str]] = ...,
        origins: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DeepCreatedOriginArgs, DeepCreatedOriginArgsDict]
                    ]
                ]
            ]
        ] = ...,
        probe_path: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        query_string_caching_behavior: Optional[
            pulumi.Input[QueryStringCachingBehavior]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        url_signing_keys: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[UrlSigningKeyArgs, UrlSigningKeyArgsDict]]]
            ]
        ] = ...,
        web_application_firewall_policy_link: Optional[
            pulumi.Input[
                Union[
                    EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkArgs,
                    EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Endpoint: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentTypesToCompress")
    def content_types_to_compress(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(
        self,
    ) -> pulumi.Output[Sequence[outputs.DeepCreatedCustomDomainResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultOriginGroup")
    def default_origin_group(
        self,
    ) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(
        self,
    ) -> pulumi.Output[
        Optional[outputs.EndpointPropertiesUpdateParametersDeliveryPolicyResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="geoFilters")
    def geo_filters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.GeoFilterResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isHttpAllowed")
    def is_http_allowed(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isHttpsAllowed")
    def is_https_allowed(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="optimizationType")
    def optimization_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DeepCreatedOriginGroupResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def origins(self) -> pulumi.Output[Sequence[outputs.DeepCreatedOriginResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="probePath")
    def probe_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryStringCachingBehavior")
    def query_string_caching_behavior(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="urlSigningKeys")
    def url_signing_keys(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.UrlSigningKeyResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallPolicyLink")
    def web_application_firewall_policy_link(
        self,
    ) -> pulumi.Output[
        Optional[
            outputs.EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkResponse
        ]
    ]: ...
