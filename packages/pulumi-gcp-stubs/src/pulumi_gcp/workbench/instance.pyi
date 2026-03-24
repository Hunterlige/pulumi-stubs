

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], desired_state: Optional[pulumi.Input[_builtins.str]] = ..., disable_proxy_access: Optional[pulumi.Input[_builtins.bool]] = ..., enable_managed_euc: Optional[pulumi.Input[_builtins.bool]] = ..., enable_third_party_identity: Optional[pulumi.Input[_builtins.bool]] = ..., gce_setup: Optional[pulumi.Input[InstanceGceSetupArgs]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableProxyAccess")
    def disable_proxy_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_proxy_access.setter
    def disable_proxy_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableManagedEuc")
    def enable_managed_euc(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_managed_euc.setter
    def enable_managed_euc(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableThirdPartyIdentity")
    def enable_third_party_identity(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_third_party_identity.setter
    def enable_third_party_identity(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceSetup")
    def gce_setup(self) -> Optional[pulumi.Input[InstanceGceSetupArgs]]:
        
        ...
    
    @gce_setup.setter
    def gce_setup(self, value: Optional[pulumi.Input[InstanceGceSetupArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_owners.setter
    def instance_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., creator: Optional[pulumi.Input[_builtins.str]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., disable_proxy_access: Optional[pulumi.Input[_builtins.bool]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_managed_euc: Optional[pulumi.Input[_builtins.bool]] = ..., enable_third_party_identity: Optional[pulumi.Input[_builtins.bool]] = ..., gce_setup: Optional[pulumi.Input[InstanceGceSetupArgs]] = ..., health_infos: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceHealthInfoArgs]]]] = ..., health_state: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy_uri: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., upgrade_histories: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceUpgradeHistoryArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def creator(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creator.setter
    def creator(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableProxyAccess")
    def disable_proxy_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_proxy_access.setter
    def disable_proxy_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableManagedEuc")
    def enable_managed_euc(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_managed_euc.setter
    def enable_managed_euc(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableThirdPartyIdentity")
    def enable_third_party_identity(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_third_party_identity.setter
    def enable_third_party_identity(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceSetup")
    def gce_setup(self) -> Optional[pulumi.Input[InstanceGceSetupArgs]]:
        
        ...
    
    @gce_setup.setter
    def gce_setup(self, value: Optional[pulumi.Input[InstanceGceSetupArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthInfos")
    def health_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceHealthInfoArgs]]]]:
        
        ...
    
    @health_infos.setter
    def health_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceHealthInfoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @health_state.setter
    def health_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_owners.setter
    def instance_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyUri")
    def proxy_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @proxy_uri.setter
    def proxy_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeHistories")
    def upgrade_histories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceUpgradeHistoryArgs]]]]:
        
        ...
    
    @upgrade_histories.setter
    def upgrade_histories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceUpgradeHistoryArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:workbench/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., disable_proxy_access: Optional[pulumi.Input[_builtins.bool]] = ..., enable_managed_euc: Optional[pulumi.Input[_builtins.bool]] = ..., enable_third_party_identity: Optional[pulumi.Input[_builtins.bool]] = ..., gce_setup: Optional[pulumi.Input[Union[InstanceGceSetupArgs, InstanceGceSetupArgsDict]]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., creator: Optional[pulumi.Input[_builtins.str]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., disable_proxy_access: Optional[pulumi.Input[_builtins.bool]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_managed_euc: Optional[pulumi.Input[_builtins.bool]] = ..., enable_third_party_identity: Optional[pulumi.Input[_builtins.bool]] = ..., gce_setup: Optional[pulumi.Input[Union[InstanceGceSetupArgs, InstanceGceSetupArgsDict]]] = ..., health_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceHealthInfoArgs, InstanceHealthInfoArgsDict]]]]] = ..., health_state: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy_uri: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., upgrade_histories: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceUpgradeHistoryArgs, InstanceUpgradeHistoryArgsDict]]]]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def creator(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableProxyAccess")
    def disable_proxy_access(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableManagedEuc")
    def enable_managed_euc(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableThirdPartyIdentity")
    def enable_third_party_identity(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceSetup")
    def gce_setup(self) -> pulumi.Output[outputs.InstanceGceSetup]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthInfos")
    def health_infos(self) -> pulumi.Output[Sequence[outputs.InstanceHealthInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyUri")
    def proxy_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeHistories")
    def upgrade_histories(self) -> pulumi.Output[Sequence[outputs.InstanceUpgradeHistory]]:
        
        ...
    


