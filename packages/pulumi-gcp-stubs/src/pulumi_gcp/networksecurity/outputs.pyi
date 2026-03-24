

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AddressGroupIamBindingCondition', 'AddressGroupIamMemberCondition', 'AuthorizationPolicyRule', 'AuthorizationPolicyRuleDestination', 'AuthorizationPolicyRuleDestinationHttpHeaderMatch', 'AuthorizationPolicyRuleSource', 'AuthzPolicyCustomProvider', 'AuthzPolicyCustomProviderAuthzExtension', 'AuthzPolicyCustomProviderCloudIap', 'AuthzPolicyHttpRule', 'AuthzPolicyHttpRuleFrom', 'AuthzPolicyHttpRuleFromNotSource', 'AuthzPolicyHttpRuleFromNotSourceIpBlock', 'AuthzPolicyHttpRuleFromNotSourcePrincipal', 'AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipal', 'AuthzPolicyHttpRuleFromNotSourceResource', ..., ..., 'AuthzPolicyHttpRuleFromSource', 'AuthzPolicyHttpRuleFromSourceIpBlock', 'AuthzPolicyHttpRuleFromSourcePrincipal', 'AuthzPolicyHttpRuleFromSourcePrincipalPrincipal', 'AuthzPolicyHttpRuleFromSourceResource', ..., 'AuthzPolicyHttpRuleFromSourceResourceTagValueIdSet', 'AuthzPolicyHttpRuleTo', 'AuthzPolicyHttpRuleToNotOperation', 'AuthzPolicyHttpRuleToNotOperationHeaderSet', 'AuthzPolicyHttpRuleToNotOperationHeaderSetHeader', ..., 'AuthzPolicyHttpRuleToNotOperationHost', 'AuthzPolicyHttpRuleToNotOperationPath', 'AuthzPolicyHttpRuleToOperation', 'AuthzPolicyHttpRuleToOperationHeaderSet', 'AuthzPolicyHttpRuleToOperationHeaderSetHeader', 'AuthzPolicyHttpRuleToOperationHeaderSetHeaderValue', 'AuthzPolicyHttpRuleToOperationHost', 'AuthzPolicyHttpRuleToOperationMcp', 'AuthzPolicyHttpRuleToOperationMcpMethod', 'AuthzPolicyHttpRuleToOperationMcpMethodParam', 'AuthzPolicyHttpRuleToOperationPath', 'AuthzPolicyTarget', 'ClientTlsPolicyClientCertificate', ..., 'ClientTlsPolicyClientCertificateGrpcEndpoint', 'ClientTlsPolicyServerValidationCa', ..., 'ClientTlsPolicyServerValidationCaGrpcEndpoint', 'FirewallEndpointEndpointSettings', 'InterceptDeploymentGroupConnectedEndpointGroup', 'InterceptDeploymentGroupLocation', 'InterceptEndpointGroupAssociation', 'InterceptEndpointGroupAssociationLocation', 'InterceptEndpointGroupAssociationLocationsDetail', 'InterceptEndpointGroupConnectedDeploymentGroup', ..., 'MirroringDeploymentGroupConnectedEndpointGroup', 'MirroringDeploymentGroupLocation', 'MirroringEndpointGroupAssociation', 'MirroringEndpointGroupAssociationLocation', 'MirroringEndpointGroupAssociationLocationsDetail', 'MirroringEndpointGroupConnectedDeploymentGroup', ..., 'SacAttachmentSymantecOptions', 'SacRealmPairingKey', 'SacRealmSymantecOptions', 'SecurityProfileCustomInterceptProfile', 'SecurityProfileCustomMirroringProfile', 'SecurityProfileThreatPreventionProfile', ..., ..., ..., 'SecurityProfileUrlFilteringProfile', 'SecurityProfileUrlFilteringProfileUrlFilter', 'ServerTlsPolicyMtlsPolicy', 'ServerTlsPolicyMtlsPolicyClientValidationCa', ..., ..., 'ServerTlsPolicyServerCertificate', ..., 'ServerTlsPolicyServerCertificateGrpcEndpoint']
@pulumi.output_type
class AddressGroupIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class AddressGroupIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class AuthorizationPolicyRule(dict):
    def __init__(__self__, *, destinations: Optional[Sequence[outputs.AuthorizationPolicyRuleDestination]] = ..., sources: Optional[Sequence[outputs.AuthorizationPolicyRuleSource]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[outputs.AuthorizationPolicyRuleDestination]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[Sequence[outputs.AuthorizationPolicyRuleSource]]:
        
        ...
    


@pulumi.output_type
class AuthorizationPolicyRuleDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hosts: Sequence[_builtins.str], methods: Sequence[_builtins.str], ports: Sequence[_builtins.int], http_header_match: Optional[outputs.AuthorizationPolicyRuleDestinationHttpHeaderMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaderMatch")
    def http_header_match(self) -> Optional[outputs.AuthorizationPolicyRuleDestinationHttpHeaderMatch]:
        
        ...
    


@pulumi.output_type
class AuthorizationPolicyRuleDestinationHttpHeaderMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_name: _builtins.str, regex_match: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AuthorizationPolicyRuleSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_blocks: Optional[Sequence[_builtins.str]] = ..., principals: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyCustomProvider(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authz_extension: Optional[outputs.AuthzPolicyCustomProviderAuthzExtension] = ..., cloud_iap: Optional[outputs.AuthzPolicyCustomProviderCloudIap] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authzExtension")
    def authz_extension(self) -> Optional[outputs.AuthzPolicyCustomProviderAuthzExtension]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudIap")
    def cloud_iap(self) -> Optional[outputs.AuthzPolicyCustomProviderCloudIap]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyCustomProviderAuthzExtension(dict):
    def __init__(__self__, *, resources: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyCustomProviderCloudIap(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[outputs.AuthzPolicyHttpRuleFrom] = ..., to: Optional[outputs.AuthzPolicyHttpRuleTo] = ..., when: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[outputs.AuthzPolicyHttpRuleFrom]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[outputs.AuthzPolicyHttpRuleTo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def when(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFrom(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, not_sources: Optional[Sequence[outputs.AuthzPolicyHttpRuleFromNotSource]] = ..., sources: Optional[Sequence[outputs.AuthzPolicyHttpRuleFromSource]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notSources")
    def not_sources(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleFromNotSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleFromSource]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromNotSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_blocks: Optional[Sequence[outputs.AuthzPolicyHttpRuleFromNotSourceIpBlock]] = ..., principals: Optional[Sequence[outputs.AuthzPolicyHttpRuleFromNotSourcePrincipal]] = ..., resources: Optional[Sequence[outputs.AuthzPolicyHttpRuleFromNotSourceResource]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleFromNotSourceIpBlock]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleFromNotSourcePrincipal]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleFromNotSourceResource]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromNotSourceIpBlock(dict):
    def __init__(__self__, *, length: _builtins.int, prefix: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromNotSourcePrincipal(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., principal: Optional[outputs.AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipal] = ..., principal_selector: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    @_utilities.deprecated(...)
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[outputs.AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipal]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalSelector")
    def principal_selector(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromNotSourcePrincipalPrincipal(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromNotSourceResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, iam_service_account: Optional[outputs.AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccount] = ..., tag_value_id_set: Optional[outputs.AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSet] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamServiceAccount")
    def iam_service_account(self) -> Optional[outputs.AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValueIdSet")
    def tag_value_id_set(self) -> Optional[outputs.AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSet]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromNotSourceResourceIamServiceAccount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromNotSourceResourceTagValueIdSet(dict):
    def __init__(__self__, *, ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_blocks: Optional[Sequence[outputs.AuthzPolicyHttpRuleFromSourceIpBlock]] = ..., principals: Optional[Sequence[outputs.AuthzPolicyHttpRuleFromSourcePrincipal]] = ..., resources: Optional[Sequence[outputs.AuthzPolicyHttpRuleFromSourceResource]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleFromSourceIpBlock]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleFromSourcePrincipal]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleFromSourceResource]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromSourceIpBlock(dict):
    def __init__(__self__, *, length: _builtins.int, prefix: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromSourcePrincipal(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., principal: Optional[outputs.AuthzPolicyHttpRuleFromSourcePrincipalPrincipal] = ..., principal_selector: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    @_utilities.deprecated(...)
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[outputs.AuthzPolicyHttpRuleFromSourcePrincipalPrincipal]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalSelector")
    def principal_selector(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromSourcePrincipalPrincipal(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromSourceResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, iam_service_account: Optional[outputs.AuthzPolicyHttpRuleFromSourceResourceIamServiceAccount] = ..., tag_value_id_set: Optional[outputs.AuthzPolicyHttpRuleFromSourceResourceTagValueIdSet] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamServiceAccount")
    def iam_service_account(self) -> Optional[outputs.AuthzPolicyHttpRuleFromSourceResourceIamServiceAccount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValueIdSet")
    def tag_value_id_set(self) -> Optional[outputs.AuthzPolicyHttpRuleFromSourceResourceTagValueIdSet]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromSourceResourceIamServiceAccount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleFromSourceResourceTagValueIdSet(dict):
    def __init__(__self__, *, ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleTo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, not_operations: Optional[Sequence[outputs.AuthzPolicyHttpRuleToNotOperation]] = ..., operations: Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notOperations")
    def not_operations(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToNotOperation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operations(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperation]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToNotOperation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_set: Optional[outputs.AuthzPolicyHttpRuleToNotOperationHeaderSet] = ..., hosts: Optional[Sequence[outputs.AuthzPolicyHttpRuleToNotOperationHost]] = ..., methods: Optional[Sequence[_builtins.str]] = ..., paths: Optional[Sequence[outputs.AuthzPolicyHttpRuleToNotOperationPath]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerSet")
    def header_set(self) -> Optional[outputs.AuthzPolicyHttpRuleToNotOperationHeaderSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToNotOperationHost]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToNotOperationPath]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToNotOperationHeaderSet(dict):
    def __init__(__self__, *, headers: Optional[Sequence[outputs.AuthzPolicyHttpRuleToNotOperationHeaderSetHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToNotOperationHeaderSetHeader]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToNotOperationHeaderSetHeader(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[outputs.AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValue]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToNotOperationHeaderSetHeaderValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToNotOperationHost(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToNotOperationPath(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_set: Optional[outputs.AuthzPolicyHttpRuleToOperationHeaderSet] = ..., hosts: Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationHost]] = ..., mcp: Optional[outputs.AuthzPolicyHttpRuleToOperationMcp] = ..., methods: Optional[Sequence[_builtins.str]] = ..., paths: Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationPath]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerSet")
    def header_set(self) -> Optional[outputs.AuthzPolicyHttpRuleToOperationHeaderSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationHost]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mcp(self) -> Optional[outputs.AuthzPolicyHttpRuleToOperationMcp]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationPath]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperationHeaderSet(dict):
    def __init__(__self__, *, headers: Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationHeaderSetHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationHeaderSetHeader]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperationHeaderSetHeader(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[outputs.AuthzPolicyHttpRuleToOperationHeaderSetHeaderValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.AuthzPolicyHttpRuleToOperationHeaderSetHeaderValue]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperationHeaderSetHeaderValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperationHost(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperationMcp(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, base_protocol_methods_option: Optional[_builtins.str] = ..., methods: Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationMcpMethod]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseProtocolMethodsOption")
    def base_protocol_methods_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationMcpMethod]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperationMcpMethod(dict):
    def __init__(__self__, *, name: _builtins.str, params: Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationMcpMethodParam]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[Sequence[outputs.AuthzPolicyHttpRuleToOperationMcpMethodParam]]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperationMcpMethodParam(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyHttpRuleToOperationPath(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contains: Optional[_builtins.str] = ..., exact: Optional[_builtins.str] = ..., ignore_case: Optional[_builtins.bool] = ..., prefix: Optional[_builtins.str] = ..., suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthzPolicyTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, load_balancing_scheme: Optional[_builtins.str] = ..., resources: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClientTlsPolicyClientCertificate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_provider_instance: Optional[outputs.ClientTlsPolicyClientCertificateCertificateProviderInstance] = ..., grpc_endpoint: Optional[outputs.ClientTlsPolicyClientCertificateGrpcEndpoint] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateProviderInstance")
    def certificate_provider_instance(self) -> Optional[outputs.ClientTlsPolicyClientCertificateCertificateProviderInstance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcEndpoint")
    def grpc_endpoint(self) -> Optional[outputs.ClientTlsPolicyClientCertificateGrpcEndpoint]:
        
        ...
    


@pulumi.output_type
class ClientTlsPolicyClientCertificateCertificateProviderInstance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, plugin_instance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClientTlsPolicyClientCertificateGrpcEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClientTlsPolicyServerValidationCa(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_provider_instance: Optional[outputs.ClientTlsPolicyServerValidationCaCertificateProviderInstance] = ..., grpc_endpoint: Optional[outputs.ClientTlsPolicyServerValidationCaGrpcEndpoint] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateProviderInstance")
    def certificate_provider_instance(self) -> Optional[outputs.ClientTlsPolicyServerValidationCaCertificateProviderInstance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcEndpoint")
    def grpc_endpoint(self) -> Optional[outputs.ClientTlsPolicyServerValidationCaGrpcEndpoint]:
        
        ...
    


@pulumi.output_type
class ClientTlsPolicyServerValidationCaCertificateProviderInstance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, plugin_instance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClientTlsPolicyServerValidationCaGrpcEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FirewallEndpointEndpointSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, jumbo_frames_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jumboFramesEnabled")
    def jumbo_frames_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InterceptDeploymentGroupConnectedEndpointGroup(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InterceptDeploymentGroupLocation(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InterceptEndpointGroupAssociation(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InterceptEndpointGroupAssociationLocation(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InterceptEndpointGroupAssociationLocationsDetail(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InterceptEndpointGroupConnectedDeploymentGroup(dict):
    def __init__(__self__, *, locations: Optional[Sequence[outputs.InterceptEndpointGroupConnectedDeploymentGroupLocation]] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[outputs.InterceptEndpointGroupConnectedDeploymentGroupLocation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InterceptEndpointGroupConnectedDeploymentGroupLocation(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MirroringDeploymentGroupConnectedEndpointGroup(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MirroringDeploymentGroupLocation(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MirroringEndpointGroupAssociation(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MirroringEndpointGroupAssociationLocation(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MirroringEndpointGroupAssociationLocationsDetail(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MirroringEndpointGroupConnectedDeploymentGroup(dict):
    def __init__(__self__, *, locations: Optional[Sequence[outputs.MirroringEndpointGroupConnectedDeploymentGroupLocation]] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[outputs.MirroringEndpointGroupConnectedDeploymentGroupLocation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MirroringEndpointGroupConnectedDeploymentGroupLocation(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SacAttachmentSymantecOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, symantec_location_name: Optional[_builtins.str] = ..., symantec_site: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="symantecLocationName")
    def symantec_location_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="symantecSite")
    def symantec_site(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SacRealmPairingKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expire_time: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SacRealmSymantecOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, available_symantec_sites: Optional[Sequence[_builtins.str]] = ..., secret_path: Optional[_builtins.str] = ..., symantec_connection_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableSymantecSites")
    def available_symantec_sites(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretPath")
    def secret_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="symantecConnectionState")
    def symantec_connection_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityProfileCustomInterceptProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, intercept_endpoint_group: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptEndpointGroup")
    def intercept_endpoint_group(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecurityProfileCustomMirroringProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mirroring_endpoint_group: _builtins.str, mirroring_deployment_groups: Optional[Sequence[_builtins.str]] = ..., mirroring_endpoint_group_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroup")
    def mirroring_endpoint_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mirroringDeploymentGroups")
    def mirroring_deployment_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroupType")
    def mirroring_endpoint_group_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityProfileThreatPreventionProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, antivirus_overrides: Optional[Sequence[outputs.SecurityProfileThreatPreventionProfileAntivirusOverride]] = ..., severity_overrides: Optional[Sequence[outputs.SecurityProfileThreatPreventionProfileSeverityOverride]] = ..., threat_overrides: Optional[Sequence[outputs.SecurityProfileThreatPreventionProfileThreatOverride]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="antivirusOverrides")
    def antivirus_overrides(self) -> Optional[Sequence[outputs.SecurityProfileThreatPreventionProfileAntivirusOverride]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="severityOverrides")
    def severity_overrides(self) -> Optional[Sequence[outputs.SecurityProfileThreatPreventionProfileSeverityOverride]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatOverrides")
    def threat_overrides(self) -> Optional[Sequence[outputs.SecurityProfileThreatPreventionProfileThreatOverride]]:
        
        ...
    


@pulumi.output_type
class SecurityProfileThreatPreventionProfileAntivirusOverride(dict):
    def __init__(__self__, *, action: _builtins.str, protocol: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecurityProfileThreatPreventionProfileSeverityOverride(dict):
    def __init__(__self__, *, action: _builtins.str, severity: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecurityProfileThreatPreventionProfileThreatOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: _builtins.str, threat_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatId")
    def threat_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityProfileUrlFilteringProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, url_filters: Optional[Sequence[outputs.SecurityProfileUrlFilteringProfileUrlFilter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlFilters")
    def url_filters(self) -> Optional[Sequence[outputs.SecurityProfileUrlFilteringProfileUrlFilter]]:
        
        ...
    


@pulumi.output_type
class SecurityProfileUrlFilteringProfileUrlFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filtering_action: _builtins.str, priority: _builtins.int, urls: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filteringAction")
    def filtering_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def urls(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ServerTlsPolicyMtlsPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_validation_cas: Optional[Sequence[outputs.ServerTlsPolicyMtlsPolicyClientValidationCa]] = ..., client_validation_mode: Optional[_builtins.str] = ..., client_validation_trust_config: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientValidationCas")
    def client_validation_cas(self) -> Optional[Sequence[outputs.ServerTlsPolicyMtlsPolicyClientValidationCa]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientValidationMode")
    def client_validation_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientValidationTrustConfig")
    def client_validation_trust_config(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerTlsPolicyMtlsPolicyClientValidationCa(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_provider_instance: Optional[outputs.ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstance] = ..., grpc_endpoint: Optional[outputs.ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpoint] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateProviderInstance")
    def certificate_provider_instance(self) -> Optional[outputs.ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcEndpoint")
    def grpc_endpoint(self) -> Optional[outputs.ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpoint]:
        
        ...
    


@pulumi.output_type
class ServerTlsPolicyMtlsPolicyClientValidationCaCertificateProviderInstance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, plugin_instance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerTlsPolicyMtlsPolicyClientValidationCaGrpcEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerTlsPolicyServerCertificate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_provider_instance: Optional[outputs.ServerTlsPolicyServerCertificateCertificateProviderInstance] = ..., grpc_endpoint: Optional[outputs.ServerTlsPolicyServerCertificateGrpcEndpoint] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateProviderInstance")
    def certificate_provider_instance(self) -> Optional[outputs.ServerTlsPolicyServerCertificateCertificateProviderInstance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcEndpoint")
    def grpc_endpoint(self) -> Optional[outputs.ServerTlsPolicyServerCertificateGrpcEndpoint]:
        
        ...
    


@pulumi.output_type
class ServerTlsPolicyServerCertificateCertificateProviderInstance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, plugin_instance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerTlsPolicyServerCertificateGrpcEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> _builtins.str:
        
        ...
    


