

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccountResult', 'AwaitableGetAccountResult', 'get_account', 'get_account_output']
@pulumi.output_type
class GetAccountResult:
    
    def __init__(__self__, account_id=..., azure_api_version=..., creation_time=..., current_tier=..., default_group=..., encryption_config=..., encryption_provisioning_state=..., encryption_state=..., endpoint=..., firewall_allow_azure_ips=..., firewall_rules=..., firewall_state=..., id=..., identity=..., last_modified_time=..., location=..., name=..., new_tier=..., provisioning_state=..., state=..., tags=..., trusted_id_provider_state=..., trusted_id_providers=..., type=..., virtual_network_rules=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentTier")
    def current_tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultGroup")
    def default_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> outputs.EncryptionConfigResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionProvisioningState")
    def encryption_provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionState")
    def encryption_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallAllowAzureIps")
    def firewall_allow_azure_ips(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Sequence[outputs.FirewallRuleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallState")
    def firewall_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> outputs.EncryptionIdentityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newTier")
    def new_tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedIdProviderState")
    def trusted_id_provider_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedIdProviders")
    def trusted_id_providers(self) -> Sequence[outputs.TrustedIdProviderResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Sequence[outputs.VirtualNetworkRuleResponse]:
        
        ...
    


class AwaitableGetAccountResult(GetAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetAccountResult]:
        ...
    


def get_account(account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccountResult:
    
    ...

def get_account_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccountResult]:
    
    ...

