

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
    
    def __init__(__self__, account_id=..., azure_api_version=..., compute_policies=..., creation_time=..., current_tier=..., data_lake_store_accounts=..., debug_data_access_level=..., default_data_lake_store_account=..., default_data_lake_store_account_type=..., endpoint=..., firewall_allow_azure_ips=..., firewall_rules=..., firewall_state=..., hive_metastores=..., id=..., last_modified_time=..., location=..., max_active_job_count_per_user=..., max_degree_of_parallelism=..., max_degree_of_parallelism_per_job=..., max_job_count=..., max_job_running_time_in_min=..., max_queued_job_count_per_user=..., min_priority_per_job=..., name=..., new_tier=..., provisioning_state=..., public_data_lake_store_accounts=..., query_store_retention=..., state=..., storage_accounts=..., system_max_degree_of_parallelism=..., system_max_job_count=..., tags=..., type=..., virtual_network_rules=...) -> None:
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
    @pulumi.getter(name="computePolicies")
    def compute_policies(self) -> Sequence[outputs.ComputePolicyResponse]:
        
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
    @pulumi.getter(name="dataLakeStoreAccounts")
    def data_lake_store_accounts(self) -> Sequence[outputs.DataLakeStoreAccountInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="debugDataAccessLevel")
    def debug_data_access_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDataLakeStoreAccount")
    def default_data_lake_store_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDataLakeStoreAccountType")
    def default_data_lake_store_account_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallAllowAzureIps")
    def firewall_allow_azure_ips(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Sequence[outputs.FirewallRuleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallState")
    def firewall_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveMetastores")
    def hive_metastores(self) -> Sequence[outputs.HiveMetastoreResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="maxActiveJobCountPerUser")
    def max_active_job_count_per_user(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelism")
    def max_degree_of_parallelism(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxJobCount")
    def max_job_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxJobRunningTimeInMin")
    def max_job_running_time_in_min(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxQueuedJobCountPerUser")
    def max_queued_job_count_per_user(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newTier")
    def new_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDataLakeStoreAccounts")
    def public_data_lake_store_accounts(self) -> Optional[Sequence[outputs.DataLakeStoreAccountInformationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStoreRetention")
    def query_store_retention(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> Sequence[outputs.StorageAccountInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemMaxDegreeOfParallelism")
    def system_max_degree_of_parallelism(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemMaxJobCount")
    def system_max_job_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
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

