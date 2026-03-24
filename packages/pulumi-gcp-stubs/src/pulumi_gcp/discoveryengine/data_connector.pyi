

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
__all__ = ['DataConnectorArgs', 'DataConnector']
@pulumi.input_type
class DataConnectorArgs:
    def __init__(__self__, *, collection_display_name: pulumi.Input[_builtins.str], collection_id: pulumi.Input[_builtins.str], data_source: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], refresh_interval: pulumi.Input[_builtins.str], action_config: Optional[pulumi.Input[DataConnectorActionConfigArgs]] = ..., auto_run_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., bap_config: Optional[pulumi.Input[DataConnectorBapConfigArgs]] = ..., connector_modes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., data_source_version: Optional[pulumi.Input[_builtins.int]] = ..., destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorDestinationConfigArgs]]]] = ..., entities: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorEntityArgs]]]] = ..., incremental_refresh_interval: Optional[pulumi.Input[_builtins.str]] = ..., incremental_sync_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., json_params: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., sync_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionDisplayName")
    def collection_display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @collection_display_name.setter
    def collection_display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @collection_id.setter
    def collection_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @refresh_interval.setter
    def refresh_interval(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfig")
    def action_config(self) -> Optional[pulumi.Input[DataConnectorActionConfigArgs]]:
        
        ...
    
    @action_config.setter
    def action_config(self, value: Optional[pulumi.Input[DataConnectorActionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRunDisabled")
    def auto_run_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_run_disabled.setter
    def auto_run_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bapConfig")
    def bap_config(self) -> Optional[pulumi.Input[DataConnectorBapConfigArgs]]:
        
        ...
    
    @bap_config.setter
    def bap_config(self, value: Optional[pulumi.Input[DataConnectorBapConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorModes")
    def connector_modes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @connector_modes.setter
    def connector_modes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceVersion")
    def data_source_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_source_version.setter
    def data_source_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfigs")
    def destination_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorDestinationConfigArgs]]]]:
        
        ...
    
    @destination_configs.setter
    def destination_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorDestinationConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorEntityArgs]]]]:
        
        ...
    
    @entities.setter
    def entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorEntityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalRefreshInterval")
    def incremental_refresh_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @incremental_refresh_interval.setter
    def incremental_refresh_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalSyncDisabled")
    def incremental_sync_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @incremental_sync_disabled.setter
    def incremental_sync_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonParams")
    def json_params(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @json_params.setter
    def json_params(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpEnabled")
    def static_ip_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @static_ip_enabled.setter
    def static_ip_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncMode")
    def sync_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_mode.setter
    def sync_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DataConnectorState:
    def __init__(__self__, *, action_config: Optional[pulumi.Input[DataConnectorActionConfigArgs]] = ..., action_state: Optional[pulumi.Input[_builtins.str]] = ..., auto_run_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., bap_config: Optional[pulumi.Input[DataConnectorBapConfigArgs]] = ..., blocking_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., collection_display_name: Optional[pulumi.Input[_builtins.str]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., connector_modes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., connector_type: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., data_source_version: Optional[pulumi.Input[_builtins.int]] = ..., destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorDestinationConfigArgs]]]] = ..., entities: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorEntityArgs]]]] = ..., errors: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorErrorArgs]]]] = ..., incremental_refresh_interval: Optional[pulumi.Input[_builtins.str]] = ..., incremental_sync_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., json_params: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., last_sync_time: Optional[pulumi.Input[_builtins.str]] = ..., latest_pause_time: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., private_connectivity_project_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., realtime_state: Optional[pulumi.Input[_builtins.str]] = ..., refresh_interval: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., static_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., sync_mode: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfig")
    def action_config(self) -> Optional[pulumi.Input[DataConnectorActionConfigArgs]]:
        
        ...
    
    @action_config.setter
    def action_config(self, value: Optional[pulumi.Input[DataConnectorActionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionState")
    def action_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_state.setter
    def action_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRunDisabled")
    def auto_run_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_run_disabled.setter
    def auto_run_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bapConfig")
    def bap_config(self) -> Optional[pulumi.Input[DataConnectorBapConfigArgs]]:
        
        ...
    
    @bap_config.setter
    def bap_config(self, value: Optional[pulumi.Input[DataConnectorBapConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockingReasons")
    def blocking_reasons(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @blocking_reasons.setter
    def blocking_reasons(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionDisplayName")
    def collection_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection_display_name.setter
    def collection_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorModes")
    def connector_modes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @connector_modes.setter
    def connector_modes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_type.setter
    def connector_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceVersion")
    def data_source_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_source_version.setter
    def data_source_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfigs")
    def destination_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorDestinationConfigArgs]]]]:
        
        ...
    
    @destination_configs.setter
    def destination_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorDestinationConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorEntityArgs]]]]:
        
        ...
    
    @entities.setter
    def entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorEntityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorErrorArgs]]]]:
        
        ...
    
    @errors.setter
    def errors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataConnectorErrorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalRefreshInterval")
    def incremental_refresh_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @incremental_refresh_interval.setter
    def incremental_refresh_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalSyncDisabled")
    def incremental_sync_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @incremental_sync_disabled.setter
    def incremental_sync_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonParams")
    def json_params(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @json_params.setter
    def json_params(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_sync_time.setter
    def last_sync_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestPauseTime")
    def latest_pause_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @latest_pause_time.setter
    def latest_pause_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateConnectivityProjectId")
    def private_connectivity_project_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_connectivity_project_id.setter
    def private_connectivity_project_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeState")
    def realtime_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realtime_state.setter
    def realtime_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @refresh_interval.setter
    def refresh_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpAddresses")
    def static_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @static_ip_addresses.setter
    def static_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpEnabled")
    def static_ip_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @static_ip_enabled.setter
    def static_ip_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncMode")
    def sync_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_mode.setter
    def sync_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:discoveryengine/dataConnector:DataConnector")
class DataConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action_config: Optional[pulumi.Input[Union[DataConnectorActionConfigArgs, DataConnectorActionConfigArgsDict]]] = ..., auto_run_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., bap_config: Optional[pulumi.Input[Union[DataConnectorBapConfigArgs, DataConnectorBapConfigArgsDict]]] = ..., collection_display_name: Optional[pulumi.Input[_builtins.str]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., connector_modes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., data_source_version: Optional[pulumi.Input[_builtins.int]] = ..., destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataConnectorDestinationConfigArgs, DataConnectorDestinationConfigArgsDict]]]]] = ..., entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataConnectorEntityArgs, DataConnectorEntityArgsDict]]]]] = ..., incremental_refresh_interval: Optional[pulumi.Input[_builtins.str]] = ..., incremental_sync_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., json_params: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., refresh_interval: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., sync_mode: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action_config: Optional[pulumi.Input[Union[DataConnectorActionConfigArgs, DataConnectorActionConfigArgsDict]]] = ..., action_state: Optional[pulumi.Input[_builtins.str]] = ..., auto_run_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., bap_config: Optional[pulumi.Input[Union[DataConnectorBapConfigArgs, DataConnectorBapConfigArgsDict]]] = ..., blocking_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., collection_display_name: Optional[pulumi.Input[_builtins.str]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., connector_modes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., connector_type: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., data_source_version: Optional[pulumi.Input[_builtins.int]] = ..., destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataConnectorDestinationConfigArgs, DataConnectorDestinationConfigArgsDict]]]]] = ..., entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataConnectorEntityArgs, DataConnectorEntityArgsDict]]]]] = ..., errors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataConnectorErrorArgs, DataConnectorErrorArgsDict]]]]] = ..., incremental_refresh_interval: Optional[pulumi.Input[_builtins.str]] = ..., incremental_sync_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., json_params: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., last_sync_time: Optional[pulumi.Input[_builtins.str]] = ..., latest_pause_time: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., private_connectivity_project_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., realtime_state: Optional[pulumi.Input[_builtins.str]] = ..., refresh_interval: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., static_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., sync_mode: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> DataConnector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfig")
    def action_config(self) -> pulumi.Output[Optional[outputs.DataConnectorActionConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionState")
    def action_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRunDisabled")
    def auto_run_disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bapConfig")
    def bap_config(self) -> pulumi.Output[Optional[outputs.DataConnectorBapConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockingReasons")
    def blocking_reasons(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionDisplayName")
    def collection_display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorModes")
    def connector_modes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceVersion")
    def data_source_version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfigs")
    def destination_configs(self) -> pulumi.Output[Optional[Sequence[outputs.DataConnectorDestinationConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entities(self) -> pulumi.Output[Optional[Sequence[outputs.DataConnectorEntity]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[outputs.DataConnectorError]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalRefreshInterval")
    def incremental_refresh_interval(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalSyncDisabled")
    def incremental_sync_disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonParams")
    def json_params(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestPauseTime")
    def latest_pause_time(self) -> pulumi.Output[_builtins.str]:
        
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
    def params(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateConnectivityProjectId")
    def private_connectivity_project_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeState")
    def realtime_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpAddresses")
    def static_ip_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpEnabled")
    def static_ip_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncMode")
    def sync_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


