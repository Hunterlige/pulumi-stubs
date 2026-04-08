import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountArgs", "Account"]

@pulumi.input_type
class AccountArgs:
    def __init__(
        __self__,
        *,
        data_lake_store_accounts: pulumi.Input[
            Sequence[pulumi.Input[AddDataLakeStoreWithAccountParametersArgs]]
        ],
        default_data_lake_store_account: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_policies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CreateComputePolicyWithAccountParametersArgs]]
            ]
        ] = ...,
        firewall_allow_azure_ips: Optional[
            pulumi.Input[FirewallAllowAzureIpsState]
        ] = ...,
        firewall_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CreateFirewallRuleWithAccountParametersArgs]]
            ]
        ] = ...,
        firewall_state: Optional[pulumi.Input[FirewallState]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_degree_of_parallelism: Optional[pulumi.Input[_builtins.int]] = ...,
        max_degree_of_parallelism_per_job: Optional[pulumi.Input[_builtins.int]] = ...,
        max_job_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_priority_per_job: Optional[pulumi.Input[_builtins.int]] = ...,
        new_tier: Optional[pulumi.Input[TierType]] = ...,
        query_store_retention: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_accounts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AddStorageAccountWithAccountParametersArgs]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataLakeStoreAccounts")
    def data_lake_store_accounts(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[AddDataLakeStoreWithAccountParametersArgs]]
    ]: ...
    @data_lake_store_accounts.setter
    def data_lake_store_accounts(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[AddDataLakeStoreWithAccountParametersArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultDataLakeStoreAccount")
    def default_data_lake_store_account(self) -> pulumi.Input[_builtins.str]: ...
    @default_data_lake_store_account.setter
    def default_data_lake_store_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computePolicies")
    def compute_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CreateComputePolicyWithAccountParametersArgs]]
        ]
    ]: ...
    @compute_policies.setter
    def compute_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CreateComputePolicyWithAccountParametersArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallAllowAzureIps")
    def firewall_allow_azure_ips(
        self,
    ) -> Optional[pulumi.Input[FirewallAllowAzureIpsState]]: ...
    @firewall_allow_azure_ips.setter
    def firewall_allow_azure_ips(
        self, value: Optional[pulumi.Input[FirewallAllowAzureIpsState]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CreateFirewallRuleWithAccountParametersArgs]]
        ]
    ]: ...
    @firewall_rules.setter
    def firewall_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CreateFirewallRuleWithAccountParametersArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallState")
    def firewall_state(self) -> Optional[pulumi.Input[FirewallState]]: ...
    @firewall_state.setter
    def firewall_state(self, value: Optional[pulumi.Input[FirewallState]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelism")
    def max_degree_of_parallelism(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_degree_of_parallelism.setter
    def max_degree_of_parallelism(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_degree_of_parallelism_per_job.setter
    def max_degree_of_parallelism_per_job(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxJobCount")
    def max_job_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_job_count.setter
    def max_job_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_priority_per_job.setter
    def min_priority_per_job(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="newTier")
    def new_tier(self) -> Optional[pulumi.Input[TierType]]: ...
    @new_tier.setter
    def new_tier(self, value: Optional[pulumi.Input[TierType]]): ...
    @_builtins.property
    @pulumi.getter(name="queryStoreRetention")
    def query_store_retention(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_store_retention.setter
    def query_store_retention(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AddStorageAccountWithAccountParametersArgs]]]
    ]: ...
    @storage_accounts.setter
    def storage_accounts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AddStorageAccountWithAccountParametersArgs]]
            ]
        ],
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

@pulumi.type_token("azure-native:datalakeanalytics:Account")
class Account(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CreateComputePolicyWithAccountParametersArgs,
                            CreateComputePolicyWithAccountParametersArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        data_lake_store_accounts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AddDataLakeStoreWithAccountParametersArgs,
                            AddDataLakeStoreWithAccountParametersArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        default_data_lake_store_account: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_allow_azure_ips: Optional[
            pulumi.Input[FirewallAllowAzureIpsState]
        ] = ...,
        firewall_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CreateFirewallRuleWithAccountParametersArgs,
                            CreateFirewallRuleWithAccountParametersArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        firewall_state: Optional[pulumi.Input[FirewallState]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_degree_of_parallelism: Optional[pulumi.Input[_builtins.int]] = ...,
        max_degree_of_parallelism_per_job: Optional[pulumi.Input[_builtins.int]] = ...,
        max_job_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_priority_per_job: Optional[pulumi.Input[_builtins.int]] = ...,
        new_tier: Optional[pulumi.Input[TierType]] = ...,
        query_store_retention: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_accounts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AddStorageAccountWithAccountParametersArgs,
                            AddStorageAccountWithAccountParametersArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccountArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Account: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computePolicies")
    def compute_policies(
        self,
    ) -> pulumi.Output[Sequence[outputs.ComputePolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentTier")
    def current_tier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataLakeStoreAccounts")
    def data_lake_store_accounts(
        self,
    ) -> pulumi.Output[Sequence[outputs.DataLakeStoreAccountInformationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="debugDataAccessLevel")
    def debug_data_access_level(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDataLakeStoreAccount")
    def default_data_lake_store_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDataLakeStoreAccountType")
    def default_data_lake_store_account_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firewallAllowAzureIps")
    def firewall_allow_azure_ips(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(
        self,
    ) -> pulumi.Output[Sequence[outputs.FirewallRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="firewallState")
    def firewall_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hiveMetastores")
    def hive_metastores(
        self,
    ) -> pulumi.Output[Sequence[outputs.HiveMetastoreResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxActiveJobCountPerUser")
    def max_active_job_count_per_user(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelism")
    def max_degree_of_parallelism(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="maxJobCount")
    def max_job_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="maxJobRunningTimeInMin")
    def max_job_running_time_in_min(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxQueuedJobCountPerUser")
    def max_queued_job_count_per_user(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="newTier")
    def new_tier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicDataLakeStoreAccounts")
    def public_data_lake_store_accounts(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.DataLakeStoreAccountInformationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="queryStoreRetention")
    def query_store_retention(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(
        self,
    ) -> pulumi.Output[Sequence[outputs.StorageAccountInformationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemMaxDegreeOfParallelism")
    def system_max_degree_of_parallelism(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="systemMaxJobCount")
    def system_max_job_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(
        self,
    ) -> pulumi.Output[Sequence[outputs.VirtualNetworkRuleResponse]]: ...
