

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AddressGroupIamBindingConditionArgs', 'AddressGroupIamBindingConditionArgsDict', 'AddressGroupIamMemberConditionArgs', 'AddressGroupIamMemberConditionArgsDict', 'AuthorizationPolicyRuleArgs', 'AuthorizationPolicyRuleArgsDict', 'AuthorizationPolicyRuleDestinationArgs', 'AuthorizationPolicyRuleDestinationArgsDict', ..., ..., 'AuthorizationPolicyRuleSourceArgs', 'AuthorizationPolicyRuleSourceArgsDict', 'AuthzPolicyCustomProviderArgs', 'AuthzPolicyCustomProviderArgsDict', 'AuthzPolicyCustomProviderAuthzExtensionArgs', 'AuthzPolicyCustomProviderAuthzExtensionArgsDict', 'AuthzPolicyCustomProviderCloudIapArgs', 'AuthzPolicyCustomProviderCloudIapArgsDict', 'AuthzPolicyHttpRuleArgs', 'AuthzPolicyHttpRuleArgsDict', 'AuthzPolicyHttpRuleFromArgs', 'AuthzPolicyHttpRuleFromArgsDict', 'AuthzPolicyHttpRuleFromNotSourceArgs', 'AuthzPolicyHttpRuleFromNotSourceArgsDict', 'AuthzPolicyHttpRuleFromNotSourceIpBlockArgs', 'AuthzPolicyHttpRuleFromNotSourceIpBlockArgsDict', 'AuthzPolicyHttpRuleFromNotSourcePrincipalArgs', 'AuthzPolicyHttpRuleFromNotSourcePrincipalArgsDict', ..., ..., 'AuthzPolicyHttpRuleFromNotSourceResourceArgs', 'AuthzPolicyHttpRuleFromNotSourceResourceArgsDict', ..., ..., ..., ..., 'AuthzPolicyHttpRuleFromSourceArgs', 'AuthzPolicyHttpRuleFromSourceArgsDict', 'AuthzPolicyHttpRuleFromSourceIpBlockArgs', 'AuthzPolicyHttpRuleFromSourceIpBlockArgsDict', 'AuthzPolicyHttpRuleFromSourcePrincipalArgs', 'AuthzPolicyHttpRuleFromSourcePrincipalArgsDict', ..., ..., 'AuthzPolicyHttpRuleFromSourceResourceArgs', 'AuthzPolicyHttpRuleFromSourceResourceArgsDict', ..., ..., ..., ..., 'AuthzPolicyHttpRuleToArgs', 'AuthzPolicyHttpRuleToArgsDict', 'AuthzPolicyHttpRuleToNotOperationArgs', 'AuthzPolicyHttpRuleToNotOperationArgsDict', 'AuthzPolicyHttpRuleToNotOperationHeaderSetArgs', 'AuthzPolicyHttpRuleToNotOperationHeaderSetArgsDict', ..., ..., ..., ..., 'AuthzPolicyHttpRuleToNotOperationHostArgs', 'AuthzPolicyHttpRuleToNotOperationHostArgsDict', 'AuthzPolicyHttpRuleToNotOperationPathArgs', 'AuthzPolicyHttpRuleToNotOperationPathArgsDict', 'AuthzPolicyHttpRuleToOperationArgs', 'AuthzPolicyHttpRuleToOperationArgsDict', 'AuthzPolicyHttpRuleToOperationHeaderSetArgs', 'AuthzPolicyHttpRuleToOperationHeaderSetArgsDict', 'AuthzPolicyHttpRuleToOperationHeaderSetHeaderArgs', ..., ..., ..., 'AuthzPolicyHttpRuleToOperationHostArgs', 'AuthzPolicyHttpRuleToOperationHostArgsDict', 'AuthzPolicyHttpRuleToOperationMcpArgs', 'AuthzPolicyHttpRuleToOperationMcpArgsDict', 'AuthzPolicyHttpRuleToOperationMcpMethodArgs', 'AuthzPolicyHttpRuleToOperationMcpMethodArgsDict', 'AuthzPolicyHttpRuleToOperationMcpMethodParamArgs', ..., 'AuthzPolicyHttpRuleToOperationPathArgs', 'AuthzPolicyHttpRuleToOperationPathArgsDict', 'AuthzPolicyTargetArgs', 'AuthzPolicyTargetArgsDict', 'ClientTlsPolicyClientCertificateArgs', 'ClientTlsPolicyClientCertificateArgsDict', ..., ..., 'ClientTlsPolicyClientCertificateGrpcEndpointArgs', ..., 'ClientTlsPolicyServerValidationCaArgs', 'ClientTlsPolicyServerValidationCaArgsDict', ..., ..., 'ClientTlsPolicyServerValidationCaGrpcEndpointArgs', ..., 'FirewallEndpointEndpointSettingsArgs', 'FirewallEndpointEndpointSettingsArgsDict', 'InterceptDeploymentGroupConnectedEndpointGroupArgs', ..., 'InterceptDeploymentGroupLocationArgs', 'InterceptDeploymentGroupLocationArgsDict', 'InterceptEndpointGroupAssociationArgs', 'InterceptEndpointGroupAssociationArgsDict', 'InterceptEndpointGroupAssociationLocationArgs', 'InterceptEndpointGroupAssociationLocationArgsDict', ..., ..., 'InterceptEndpointGroupConnectedDeploymentGroupArgs', ..., ..., ..., 'MirroringDeploymentGroupConnectedEndpointGroupArgs', ..., 'MirroringDeploymentGroupLocationArgs', 'MirroringDeploymentGroupLocationArgsDict', 'MirroringEndpointGroupAssociationArgs', 'MirroringEndpointGroupAssociationArgsDict', 'MirroringEndpointGroupAssociationLocationArgs', 'MirroringEndpointGroupAssociationLocationArgsDict', ..., ..., 'MirroringEndpointGroupConnectedDeploymentGroupArgs', ..., ..., ..., 'SacAttachmentSymantecOptionsArgs', 'SacAttachmentSymantecOptionsArgsDict', 'SacRealmPairingKeyArgs', 'SacRealmPairingKeyArgsDict', 'SacRealmSymantecOptionsArgs', 'SacRealmSymantecOptionsArgsDict', 'SecurityProfileCustomInterceptProfileArgs', 'SecurityProfileCustomInterceptProfileArgsDict', 'SecurityProfileCustomMirroringProfileArgs', 'SecurityProfileCustomMirroringProfileArgsDict', 'SecurityProfileThreatPreventionProfileArgs', 'SecurityProfileThreatPreventionProfileArgsDict', ..., ..., ..., ..., ..., ..., 'SecurityProfileUrlFilteringProfileArgs', 'SecurityProfileUrlFilteringProfileArgsDict', 'SecurityProfileUrlFilteringProfileUrlFilterArgs', ..., 'ServerTlsPolicyMtlsPolicyArgs', 'ServerTlsPolicyMtlsPolicyArgsDict', 'ServerTlsPolicyMtlsPolicyClientValidationCaArgs', ..., ..., ..., ..., ..., 'ServerTlsPolicyServerCertificateArgs', 'ServerTlsPolicyServerCertificateArgsDict', ..., ..., 'ServerTlsPolicyServerCertificateGrpcEndpointArgs', ...]
class AddressGroupIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AddressGroupIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AddressGroupIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AddressGroupIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthorizationPolicyRuleArgsDict(TypedDict):
    destinations: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthorizationPolicyRuleDestinationArgsDict]]]]
    sources: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthorizationPolicyRuleSourceArgsDict]]]]


@pulumi.input_type
class AuthorizationPolicyRuleArgs:
    def __init__(__self__, *, destinations: Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizationPolicyRuleDestinationArgs]]]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizationPolicyRuleSourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizationPolicyRuleDestinationArgs]]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizationPolicyRuleDestinationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizationPolicyRuleSourceArgs]]]]:
        
        ...
    
    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizationPolicyRuleSourceArgs]]]]): # -> None:
        ...
    


class AuthorizationPolicyRuleDestinationArgsDict(TypedDict):
    hosts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ports: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    http_header_match: NotRequired[pulumi.Input[AuthorizationPolicyRuleDestinationHttpHeaderMatchArgsDict]]


@pulumi.input_type
class AuthorizationPolicyRuleDestinationArgs:
    def __init__(__self__, *, hosts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], ports: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]], http_header_match: Optional[pulumi.Input[AuthorizationPolicyRuleDestinationHttpHeaderMatchArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @hosts.setter
    def hosts(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]:
        
        ...
    
    @ports.setter
    def ports(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaderMatch")
    def http_header_match(self) -> Optional[pulumi.Input[AuthorizationPolicyRuleDestinationHttpHeaderMatchArgs]]:
        
        ...
    
    @http_header_match.setter
    def http_header_match(self, value: Optional[pulumi.Input[AuthorizationPolicyRuleDestinationHttpHeaderMatchArgs]]): # -> None:
        ...
    


class AuthorizationPolicyRuleDestinationHttpHeaderMatchArgsDict(TypedDict):
    header_name: pulumi.Input[_builtins.str]
    regex_match: pulumi.Input[_builtins.str]


@pulumi.input_type
class AuthorizationPolicyRuleDestinationHttpHeaderMatchArgs:
    def __init__(__self__, *, header_name: pulumi.Input[_builtins.str], regex_match: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @regex_match.setter
    def regex_match(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AuthorizationPolicyRuleSourceArgsDict(TypedDict):
    ip_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AuthorizationPolicyRuleSourceArgs:
    def __init__(__self__, *, ip_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_blocks.setter
    def ip_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @principals.setter
    def principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AuthzPolicyCustomProviderArgsDict(TypedDict):
    authz_extension: NotRequired[pulumi.Input[AuthzPolicyCustomProviderAuthzExtensionArgsDict]]
    cloud_iap: NotRequired[pulumi.Input[AuthzPolicyCustomProviderCloudIapArgsDict]]


@pulumi.input_type
class AuthzPolicyCustomProviderArgs:
    def __init__(__self__, *, authz_extension: Optional[pulumi.Input[AuthzPolicyCustomProviderAuthzExtensionArgs]] = ..., cloud_iap: Optional[pulumi.Input[AuthzPolicyCustomProviderCloudIapArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authzExtension")
    def authz_extension(self) -> Optional[pulumi.Input[AuthzPolicyCustomProviderAuthzExtensionArgs]]:
        
        ...
    
    @authz_extension.setter
    def authz_extension(self, value: Optional[pulumi.Input[AuthzPolicyCustomProviderAuthzExtensionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudIap")
    def cloud_iap(self) -> Optional[pulumi.Input[AuthzPolicyCustomProviderCloudIapArgs]]:
        
        ...
    
    @cloud_iap.setter
    def cloud_iap(self, value: Optional[pulumi.Input[AuthzPolicyCustomProviderCloudIapArgs]]): # -> None:
        ...
    


class AuthzPolicyCustomProviderAuthzExtensionArgsDict(TypedDict):
    resources: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class AuthzPolicyCustomProviderAuthzExtensionArgs:
    def __init__(__self__, *, resources: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class AuthzPolicyCustomProviderCloudIapArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class AuthzPolicyCustomProviderCloudIapArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class AuthzPolicyHttpRuleArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[AuthzPolicyHttpRuleFromArgsDict]]
    to: NotRequired[pulumi.Input[AuthzPolicyHttpRuleToArgsDict]]
    when: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[AuthzPolicyHttpRuleFromArgs]] = ..., to: Optional[pulumi.Input[AuthzPolicyHttpRuleToArgs]] = ..., when: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleFromArgs]]:
        
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleFromArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleToArgs]]:
        
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleToArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def when(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @when.setter
    def when(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromArgsDict(TypedDict):
    not_sources: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceArgsDict]]]]
    sources: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromArgs:
    def __init__(__self__, *, not_sources: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceArgs]]]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notSources")
    def not_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceArgs]]]]:
        
        ...
    
    @not_sources.setter
    def not_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceArgs]]]]:
        
        ...
    
    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromNotSourceArgsDict(TypedDict):
    ip_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceIpBlockArgsDict]]]]
    principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourcePrincipalArgsDict]]]]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromNotSourceArgs:
    def __init__(__self__, *, ip_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceIpBlockArgs]]]] = ..., principals: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourcePrincipalArgs]]]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceIpBlockArgs]]]]:
        
        ...
    
    @ip_blocks.setter
    def ip_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceIpBlockArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourcePrincipalArgs]]]]:
        
        ...
    
    @principals.setter
    def principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourcePrincipalArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceArgs]]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromNotSourceIpBlockArgsDict(TypedDict):
    length: pulumi.Input[_builtins.int]
    prefix: pulumi.Input[_builtins.str]


@pulumi.input_type
class AuthzPolicyHttpRuleFromNotSourceIpBlockArgs:
    def __init__(__self__, *, length: pulumi.Input[_builtins.int], prefix: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def length(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @length.setter
    def length(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromNotSourcePrincipalArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    principal: NotRequired[pulumi.Input[AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipalArgsDict]]
    principal_selector: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromNotSourcePrincipalArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., principal: Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipalArgs]] = ..., principal_selector: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    @_utilities.deprecated(...)
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipalArgs]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipalArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalSelector")
    def principal_selector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_selector.setter
    def principal_selector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipalArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipalArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromNotSourceResourceArgsDict(TypedDict):
    iam_service_account: NotRequired[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccountArgsDict]]
    tag_value_id_set: NotRequired[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSetArgsDict]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromNotSourceResourceArgs:
    def __init__(__self__, *, iam_service_account: Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccountArgs]] = ..., tag_value_id_set: Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamServiceAccount")
    def iam_service_account(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccountArgs]]:
        
        ...
    
    @iam_service_account.setter
    def iam_service_account(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValueIdSet")
    def tag_value_id_set(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSetArgs]]:
        
        ...
    
    @tag_value_id_set.setter
    def tag_value_id_set(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSetArgs]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccountArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccountArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSetArgsDict(TypedDict):
    ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSetArgs:
    def __init__(__self__, *, ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ids.setter
    def ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromSourceArgsDict(TypedDict):
    ip_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceIpBlockArgsDict]]]]
    principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourcePrincipalArgsDict]]]]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromSourceArgs:
    def __init__(__self__, *, ip_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceIpBlockArgs]]]] = ..., principals: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourcePrincipalArgs]]]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceIpBlockArgs]]]]:
        
        ...
    
    @ip_blocks.setter
    def ip_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceIpBlockArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourcePrincipalArgs]]]]:
        
        ...
    
    @principals.setter
    def principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourcePrincipalArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceArgs]]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromSourceIpBlockArgsDict(TypedDict):
    length: pulumi.Input[_builtins.int]
    prefix: pulumi.Input[_builtins.str]


@pulumi.input_type
class AuthzPolicyHttpRuleFromSourceIpBlockArgs:
    def __init__(__self__, *, length: pulumi.Input[_builtins.int], prefix: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def length(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @length.setter
    def length(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromSourcePrincipalArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    principal: NotRequired[pulumi.Input[AuthzPolicyHttpRuleFromSourcePrincipalPrincipalArgsDict]]
    principal_selector: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromSourcePrincipalArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., principal: Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourcePrincipalPrincipalArgs]] = ..., principal_selector: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    @_utilities.deprecated(...)
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourcePrincipalPrincipalArgs]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourcePrincipalPrincipalArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalSelector")
    def principal_selector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_selector.setter
    def principal_selector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromSourcePrincipalPrincipalArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromSourcePrincipalPrincipalArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromSourceResourceArgsDict(TypedDict):
    iam_service_account: NotRequired[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceIamServiceAccountArgsDict]]
    tag_value_id_set: NotRequired[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceTagValueIdSetArgsDict]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromSourceResourceArgs:
    def __init__(__self__, *, iam_service_account: Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceIamServiceAccountArgs]] = ..., tag_value_id_set: Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceTagValueIdSetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamServiceAccount")
    def iam_service_account(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceIamServiceAccountArgs]]:
        
        ...
    
    @iam_service_account.setter
    def iam_service_account(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceIamServiceAccountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValueIdSet")
    def tag_value_id_set(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceTagValueIdSetArgs]]:
        
        ...
    
    @tag_value_id_set.setter
    def tag_value_id_set(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleFromSourceResourceTagValueIdSetArgs]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromSourceResourceIamServiceAccountArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromSourceResourceIamServiceAccountArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleFromSourceResourceTagValueIdSetArgsDict(TypedDict):
    ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleFromSourceResourceTagValueIdSetArgs:
    def __init__(__self__, *, ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ids.setter
    def ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToArgsDict(TypedDict):
    not_operations: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationArgsDict]]]]
    operations: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleToArgs:
    def __init__(__self__, *, not_operations: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationArgs]]]] = ..., operations: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notOperations")
    def not_operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationArgs]]]]:
        
        ...
    
    @not_operations.setter
    def not_operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationArgs]]]]:
        
        ...
    
    @operations.setter
    def operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToNotOperationArgsDict(TypedDict):
    header_set: NotRequired[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetArgsDict]]
    hosts: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHostArgsDict]]]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationPathArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleToNotOperationArgs:
    def __init__(__self__, *, header_set: Optional[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetArgs]] = ..., hosts: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHostArgs]]]] = ..., methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., paths: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationPathArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerSet")
    def header_set(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetArgs]]:
        
        ...
    
    @header_set.setter
    def header_set(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHostArgs]]]]:
        
        ...
    
    @hosts.setter
    def hosts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHostArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationPathArgs]]]]:
        
        ...
    
    @paths.setter
    def paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationPathArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToNotOperationHeaderSetArgsDict(TypedDict):
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleToNotOperationHeaderSetArgs:
    def __init__(__self__, *, headers: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderArgs]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValueArgsDict]]


@pulumi.input_type
class AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValueArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValueArgs]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValueArgs]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValueArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValueArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToNotOperationHostArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleToNotOperationHostArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToNotOperationPathArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleToNotOperationPathArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationArgsDict(TypedDict):
    header_set: NotRequired[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetArgsDict]]
    hosts: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationHostArgsDict]]]]
    mcp: NotRequired[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpArgsDict]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationPathArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationArgs:
    def __init__(__self__, *, header_set: Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetArgs]] = ..., hosts: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationHostArgs]]]] = ..., mcp: Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpArgs]] = ..., methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., paths: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationPathArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerSet")
    def header_set(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetArgs]]:
        
        ...
    
    @header_set.setter
    def header_set(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationHostArgs]]]]:
        
        ...
    
    @hosts.setter
    def hosts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationHostArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mcp(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpArgs]]:
        
        ...
    
    @mcp.setter
    def mcp(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationPathArgs]]]]:
        
        ...
    
    @paths.setter
    def paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationPathArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationHeaderSetArgsDict(TypedDict):
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetHeaderArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationHeaderSetArgs:
    def __init__(__self__, *, headers: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetHeaderArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetHeaderArgs]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetHeaderArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationHeaderSetHeaderArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetHeaderValueArgsDict]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationHeaderSetHeaderArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetHeaderValueArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetHeaderValueArgs]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[AuthzPolicyHttpRuleToOperationHeaderSetHeaderValueArgs]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationHeaderSetHeaderValueArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationHeaderSetHeaderValueArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationHostArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationHostArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationMcpArgsDict(TypedDict):
    base_protocol_methods_option: NotRequired[pulumi.Input[_builtins.str]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpMethodArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationMcpArgs:
    def __init__(__self__, *, base_protocol_methods_option: Optional[pulumi.Input[_builtins.str]] = ..., methods: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpMethodArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseProtocolMethodsOption")
    def base_protocol_methods_option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_protocol_methods_option.setter
    def base_protocol_methods_option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpMethodArgs]]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpMethodArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationMcpMethodArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    params: NotRequired[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpMethodParamArgsDict]]]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationMcpMethodArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], params: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpMethodParamArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpMethodParamArgs]]]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthzPolicyHttpRuleToOperationMcpMethodParamArgs]]]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationMcpMethodParamArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationMcpMethodParamArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyHttpRuleToOperationPathArgsDict(TypedDict):
    contains: NotRequired[pulumi.Input[_builtins.str]]
    exact: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthzPolicyHttpRuleToOperationPathArgs:
    def __init__(__self__, *, contains: Optional[pulumi.Input[_builtins.str]] = ..., exact: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AuthzPolicyTargetArgsDict(TypedDict):
    load_balancing_scheme: NotRequired[pulumi.Input[_builtins.str]]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AuthzPolicyTargetArgs:
    def __init__(__self__, *, load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ClientTlsPolicyClientCertificateArgsDict(TypedDict):
    certificate_provider_instance: NotRequired[pulumi.Input[ClientTlsPolicyClientCertificateCertificateProviderInstanceArgsDict]]
    grpc_endpoint: NotRequired[pulumi.Input[ClientTlsPolicyClientCertificateGrpcEndpointArgsDict]]


@pulumi.input_type
class ClientTlsPolicyClientCertificateArgs:
    def __init__(__self__, *, certificate_provider_instance: Optional[pulumi.Input[ClientTlsPolicyClientCertificateCertificateProviderInstanceArgs]] = ..., grpc_endpoint: Optional[pulumi.Input[ClientTlsPolicyClientCertificateGrpcEndpointArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateProviderInstance")
    def certificate_provider_instance(self) -> Optional[pulumi.Input[ClientTlsPolicyClientCertificateCertificateProviderInstanceArgs]]:
        
        ...
    
    @certificate_provider_instance.setter
    def certificate_provider_instance(self, value: Optional[pulumi.Input[ClientTlsPolicyClientCertificateCertificateProviderInstanceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcEndpoint")
    def grpc_endpoint(self) -> Optional[pulumi.Input[ClientTlsPolicyClientCertificateGrpcEndpointArgs]]:
        
        ...
    
    @grpc_endpoint.setter
    def grpc_endpoint(self, value: Optional[pulumi.Input[ClientTlsPolicyClientCertificateGrpcEndpointArgs]]): # -> None:
        ...
    


class ClientTlsPolicyClientCertificateCertificateProviderInstanceArgsDict(TypedDict):
    plugin_instance: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClientTlsPolicyClientCertificateCertificateProviderInstanceArgs:
    def __init__(__self__, *, plugin_instance: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @plugin_instance.setter
    def plugin_instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClientTlsPolicyClientCertificateGrpcEndpointArgsDict(TypedDict):
    target_uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClientTlsPolicyClientCertificateGrpcEndpointArgs:
    def __init__(__self__, *, target_uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_uri.setter
    def target_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClientTlsPolicyServerValidationCaArgsDict(TypedDict):
    certificate_provider_instance: NotRequired[pulumi.Input[ClientTlsPolicyServerValidationCaCertificateProviderInstanceArgsDict]]
    grpc_endpoint: NotRequired[pulumi.Input[ClientTlsPolicyServerValidationCaGrpcEndpointArgsDict]]


@pulumi.input_type
class ClientTlsPolicyServerValidationCaArgs:
    def __init__(__self__, *, certificate_provider_instance: Optional[pulumi.Input[ClientTlsPolicyServerValidationCaCertificateProviderInstanceArgs]] = ..., grpc_endpoint: Optional[pulumi.Input[ClientTlsPolicyServerValidationCaGrpcEndpointArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateProviderInstance")
    def certificate_provider_instance(self) -> Optional[pulumi.Input[ClientTlsPolicyServerValidationCaCertificateProviderInstanceArgs]]:
        
        ...
    
    @certificate_provider_instance.setter
    def certificate_provider_instance(self, value: Optional[pulumi.Input[ClientTlsPolicyServerValidationCaCertificateProviderInstanceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcEndpoint")
    def grpc_endpoint(self) -> Optional[pulumi.Input[ClientTlsPolicyServerValidationCaGrpcEndpointArgs]]:
        
        ...
    
    @grpc_endpoint.setter
    def grpc_endpoint(self, value: Optional[pulumi.Input[ClientTlsPolicyServerValidationCaGrpcEndpointArgs]]): # -> None:
        ...
    


class ClientTlsPolicyServerValidationCaCertificateProviderInstanceArgsDict(TypedDict):
    plugin_instance: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClientTlsPolicyServerValidationCaCertificateProviderInstanceArgs:
    def __init__(__self__, *, plugin_instance: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @plugin_instance.setter
    def plugin_instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClientTlsPolicyServerValidationCaGrpcEndpointArgsDict(TypedDict):
    target_uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClientTlsPolicyServerValidationCaGrpcEndpointArgs:
    def __init__(__self__, *, target_uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_uri.setter
    def target_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirewallEndpointEndpointSettingsArgsDict(TypedDict):
    jumbo_frames_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FirewallEndpointEndpointSettingsArgs:
    def __init__(__self__, *, jumbo_frames_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jumboFramesEnabled")
    def jumbo_frames_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @jumbo_frames_enabled.setter
    def jumbo_frames_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class InterceptDeploymentGroupConnectedEndpointGroupArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InterceptDeploymentGroupConnectedEndpointGroupArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InterceptDeploymentGroupLocationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InterceptDeploymentGroupLocationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InterceptEndpointGroupAssociationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InterceptEndpointGroupAssociationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InterceptEndpointGroupAssociationLocationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InterceptEndpointGroupAssociationLocationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InterceptEndpointGroupAssociationLocationsDetailArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InterceptEndpointGroupAssociationLocationsDetailArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InterceptEndpointGroupConnectedDeploymentGroupArgsDict(TypedDict):
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[InterceptEndpointGroupConnectedDeploymentGroupLocationArgsDict]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InterceptEndpointGroupConnectedDeploymentGroupArgs:
    def __init__(__self__, *, locations: Optional[pulumi.Input[Sequence[pulumi.Input[InterceptEndpointGroupConnectedDeploymentGroupLocationArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterceptEndpointGroupConnectedDeploymentGroupLocationArgs]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterceptEndpointGroupConnectedDeploymentGroupLocationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InterceptEndpointGroupConnectedDeploymentGroupLocationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InterceptEndpointGroupConnectedDeploymentGroupLocationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MirroringDeploymentGroupConnectedEndpointGroupArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MirroringDeploymentGroupConnectedEndpointGroupArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MirroringDeploymentGroupLocationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MirroringDeploymentGroupLocationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MirroringEndpointGroupAssociationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MirroringEndpointGroupAssociationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MirroringEndpointGroupAssociationLocationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MirroringEndpointGroupAssociationLocationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MirroringEndpointGroupAssociationLocationsDetailArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MirroringEndpointGroupAssociationLocationsDetailArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MirroringEndpointGroupConnectedDeploymentGroupArgsDict(TypedDict):
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[MirroringEndpointGroupConnectedDeploymentGroupLocationArgsDict]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MirroringEndpointGroupConnectedDeploymentGroupArgs:
    def __init__(__self__, *, locations: Optional[pulumi.Input[Sequence[pulumi.Input[MirroringEndpointGroupConnectedDeploymentGroupLocationArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MirroringEndpointGroupConnectedDeploymentGroupLocationArgs]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MirroringEndpointGroupConnectedDeploymentGroupLocationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MirroringEndpointGroupConnectedDeploymentGroupLocationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MirroringEndpointGroupConnectedDeploymentGroupLocationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SacAttachmentSymantecOptionsArgsDict(TypedDict):
    symantec_location_name: NotRequired[pulumi.Input[_builtins.str]]
    symantec_site: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SacAttachmentSymantecOptionsArgs:
    def __init__(__self__, *, symantec_location_name: Optional[pulumi.Input[_builtins.str]] = ..., symantec_site: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="symantecLocationName")
    def symantec_location_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @symantec_location_name.setter
    def symantec_location_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="symantecSite")
    def symantec_site(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @symantec_site.setter
    def symantec_site(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SacRealmPairingKeyArgsDict(TypedDict):
    expire_time: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SacRealmPairingKeyArgs:
    def __init__(__self__, *, expire_time: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SacRealmSymantecOptionsArgsDict(TypedDict):
    available_symantec_sites: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secret_path: NotRequired[pulumi.Input[_builtins.str]]
    symantec_connection_state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SacRealmSymantecOptionsArgs:
    def __init__(__self__, *, available_symantec_sites: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secret_path: Optional[pulumi.Input[_builtins.str]] = ..., symantec_connection_state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableSymantecSites")
    def available_symantec_sites(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @available_symantec_sites.setter
    def available_symantec_sites(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretPath")
    def secret_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_path.setter
    def secret_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="symantecConnectionState")
    def symantec_connection_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @symantec_connection_state.setter
    def symantec_connection_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityProfileCustomInterceptProfileArgsDict(TypedDict):
    intercept_endpoint_group: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecurityProfileCustomInterceptProfileArgs:
    def __init__(__self__, *, intercept_endpoint_group: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptEndpointGroup")
    def intercept_endpoint_group(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @intercept_endpoint_group.setter
    def intercept_endpoint_group(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecurityProfileCustomMirroringProfileArgsDict(TypedDict):
    mirroring_endpoint_group: pulumi.Input[_builtins.str]
    mirroring_deployment_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    mirroring_endpoint_group_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecurityProfileCustomMirroringProfileArgs:
    def __init__(__self__, *, mirroring_endpoint_group: pulumi.Input[_builtins.str], mirroring_deployment_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., mirroring_endpoint_group_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroup")
    def mirroring_endpoint_group(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mirroring_endpoint_group.setter
    def mirroring_endpoint_group(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mirroringDeploymentGroups")
    def mirroring_deployment_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @mirroring_deployment_groups.setter
    def mirroring_deployment_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroupType")
    def mirroring_endpoint_group_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mirroring_endpoint_group_type.setter
    def mirroring_endpoint_group_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityProfileThreatPreventionProfileArgsDict(TypedDict):
    antivirus_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileAntivirusOverrideArgsDict]]]]
    severity_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileSeverityOverrideArgsDict]]]]
    threat_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileThreatOverrideArgsDict]]]]


@pulumi.input_type
class SecurityProfileThreatPreventionProfileArgs:
    def __init__(__self__, *, antivirus_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileAntivirusOverrideArgs]]]] = ..., severity_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileSeverityOverrideArgs]]]] = ..., threat_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileThreatOverrideArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="antivirusOverrides")
    def antivirus_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileAntivirusOverrideArgs]]]]:
        
        ...
    
    @antivirus_overrides.setter
    def antivirus_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileAntivirusOverrideArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="severityOverrides")
    def severity_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileSeverityOverrideArgs]]]]:
        
        ...
    
    @severity_overrides.setter
    def severity_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileSeverityOverrideArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatOverrides")
    def threat_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileThreatOverrideArgs]]]]:
        
        ...
    
    @threat_overrides.setter
    def threat_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileThreatPreventionProfileThreatOverrideArgs]]]]): # -> None:
        ...
    


class SecurityProfileThreatPreventionProfileAntivirusOverrideArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    protocol: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecurityProfileThreatPreventionProfileAntivirusOverrideArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], protocol: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecurityProfileThreatPreventionProfileSeverityOverrideArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    severity: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecurityProfileThreatPreventionProfileSeverityOverrideArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], severity: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecurityProfileThreatPreventionProfileThreatOverrideArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    threat_id: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecurityProfileThreatPreventionProfileThreatOverrideArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], threat_id: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatId")
    def threat_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @threat_id.setter
    def threat_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityProfileUrlFilteringProfileArgsDict(TypedDict):
    url_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecurityProfileUrlFilteringProfileUrlFilterArgsDict]]]]


@pulumi.input_type
class SecurityProfileUrlFilteringProfileArgs:
    def __init__(__self__, *, url_filters: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileUrlFilteringProfileUrlFilterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlFilters")
    def url_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileUrlFilteringProfileUrlFilterArgs]]]]:
        
        ...
    
    @url_filters.setter
    def url_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityProfileUrlFilteringProfileUrlFilterArgs]]]]): # -> None:
        ...
    


class SecurityProfileUrlFilteringProfileUrlFilterArgsDict(TypedDict):
    filtering_action: pulumi.Input[_builtins.str]
    priority: pulumi.Input[_builtins.int]
    urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SecurityProfileUrlFilteringProfileUrlFilterArgs:
    def __init__(__self__, *, filtering_action: pulumi.Input[_builtins.str], priority: pulumi.Input[_builtins.int], urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filteringAction")
    def filtering_action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filtering_action.setter
    def filtering_action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @urls.setter
    def urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ServerTlsPolicyMtlsPolicyArgsDict(TypedDict):
    client_validation_cas: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaArgsDict]]]]
    client_validation_mode: NotRequired[pulumi.Input[_builtins.str]]
    client_validation_trust_config: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServerTlsPolicyMtlsPolicyArgs:
    def __init__(__self__, *, client_validation_cas: Optional[pulumi.Input[Sequence[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaArgs]]]] = ..., client_validation_mode: Optional[pulumi.Input[_builtins.str]] = ..., client_validation_trust_config: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientValidationCas")
    def client_validation_cas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaArgs]]]]:
        
        ...
    
    @client_validation_cas.setter
    def client_validation_cas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientValidationMode")
    def client_validation_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_validation_mode.setter
    def client_validation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientValidationTrustConfig")
    def client_validation_trust_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_validation_trust_config.setter
    def client_validation_trust_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServerTlsPolicyMtlsPolicyClientValidationCaArgsDict(TypedDict):
    certificate_provider_instance: NotRequired[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstanceArgsDict]]
    grpc_endpoint: NotRequired[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpointArgsDict]]


@pulumi.input_type
class ServerTlsPolicyMtlsPolicyClientValidationCaArgs:
    def __init__(__self__, *, certificate_provider_instance: Optional[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstanceArgs]] = ..., grpc_endpoint: Optional[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpointArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateProviderInstance")
    def certificate_provider_instance(self) -> Optional[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstanceArgs]]:
        
        ...
    
    @certificate_provider_instance.setter
    def certificate_provider_instance(self, value: Optional[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstanceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcEndpoint")
    def grpc_endpoint(self) -> Optional[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpointArgs]]:
        
        ...
    
    @grpc_endpoint.setter
    def grpc_endpoint(self, value: Optional[pulumi.Input[ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpointArgs]]): # -> None:
        ...
    


class ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstanceArgsDict(TypedDict):
    plugin_instance: pulumi.Input[_builtins.str]


@pulumi.input_type
class ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstanceArgs:
    def __init__(__self__, *, plugin_instance: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @plugin_instance.setter
    def plugin_instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpointArgsDict(TypedDict):
    target_uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpointArgs:
    def __init__(__self__, *, target_uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_uri.setter
    def target_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServerTlsPolicyServerCertificateArgsDict(TypedDict):
    certificate_provider_instance: NotRequired[pulumi.Input[ServerTlsPolicyServerCertificateCertificateProviderInstanceArgsDict]]
    grpc_endpoint: NotRequired[pulumi.Input[ServerTlsPolicyServerCertificateGrpcEndpointArgsDict]]


@pulumi.input_type
class ServerTlsPolicyServerCertificateArgs:
    def __init__(__self__, *, certificate_provider_instance: Optional[pulumi.Input[ServerTlsPolicyServerCertificateCertificateProviderInstanceArgs]] = ..., grpc_endpoint: Optional[pulumi.Input[ServerTlsPolicyServerCertificateGrpcEndpointArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateProviderInstance")
    def certificate_provider_instance(self) -> Optional[pulumi.Input[ServerTlsPolicyServerCertificateCertificateProviderInstanceArgs]]:
        
        ...
    
    @certificate_provider_instance.setter
    def certificate_provider_instance(self, value: Optional[pulumi.Input[ServerTlsPolicyServerCertificateCertificateProviderInstanceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcEndpoint")
    def grpc_endpoint(self) -> Optional[pulumi.Input[ServerTlsPolicyServerCertificateGrpcEndpointArgs]]:
        
        ...
    
    @grpc_endpoint.setter
    def grpc_endpoint(self, value: Optional[pulumi.Input[ServerTlsPolicyServerCertificateGrpcEndpointArgs]]): # -> None:
        ...
    


class ServerTlsPolicyServerCertificateCertificateProviderInstanceArgsDict(TypedDict):
    plugin_instance: pulumi.Input[_builtins.str]


@pulumi.input_type
class ServerTlsPolicyServerCertificateCertificateProviderInstanceArgs:
    def __init__(__self__, *, plugin_instance: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @plugin_instance.setter
    def plugin_instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServerTlsPolicyServerCertificateGrpcEndpointArgsDict(TypedDict):
    target_uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class ServerTlsPolicyServerCertificateGrpcEndpointArgs:
    def __init__(__self__, *, target_uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_uri.setter
    def target_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


