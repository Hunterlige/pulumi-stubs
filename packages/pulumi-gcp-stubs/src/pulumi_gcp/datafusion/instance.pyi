

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceAcceleratorArgs]]]] = ..., crypto_key_config: Optional[pulumi.Input[InstanceCryptoKeyConfigArgs]] = ..., dataproc_service_account: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_rbac: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., event_publish_config: Optional[pulumi.Input[InstanceEventPublishConfigArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[InstanceNetworkConfigArgs]] = ..., options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., patch_revision: Optional[pulumi.Input[_builtins.str]] = ..., private_instance: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceAcceleratorArgs]]]]:
        
        ...
    
    @accelerators.setter
    def accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceAcceleratorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyConfig")
    def crypto_key_config(self) -> Optional[pulumi.Input[InstanceCryptoKeyConfigArgs]]:
        
        ...
    
    @crypto_key_config.setter
    def crypto_key_config(self, value: Optional[pulumi.Input[InstanceCryptoKeyConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocServiceAccount")
    def dataproc_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataproc_service_account.setter
    def dataproc_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRbac")
    def enable_rbac(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_rbac.setter
    def enable_rbac(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverMonitoring")
    def enable_stackdriver_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_monitoring.setter
    def enable_stackdriver_monitoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventPublishConfig")
    def event_publish_config(self) -> Optional[pulumi.Input[InstanceEventPublishConfigArgs]]:
        
        ...
    
    @event_publish_config.setter
    def event_publish_config(self, value: Optional[pulumi.Input[InstanceEventPublishConfigArgs]]): # -> None:
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
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[InstanceNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[InstanceNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchRevision")
    def patch_revision(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @patch_revision.setter
    def patch_revision(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateInstance")
    def private_instance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @private_instance.setter
    def private_instance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceAcceleratorArgs]]]] = ..., api_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., crypto_key_config: Optional[pulumi.Input[InstanceCryptoKeyConfigArgs]] = ..., dataproc_service_account: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_rbac: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., event_publish_config: Optional[pulumi.Input[InstanceEventPublishConfigArgs]] = ..., gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[InstanceNetworkConfigArgs]] = ..., options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., p4_service_account: Optional[pulumi.Input[_builtins.str]] = ..., patch_revision: Optional[pulumi.Input[_builtins.str]] = ..., private_instance: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., service_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_message: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenant_project_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceAcceleratorArgs]]]]:
        
        ...
    
    @accelerators.setter
    def accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceAcceleratorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_endpoint.setter
    def api_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyConfig")
    def crypto_key_config(self) -> Optional[pulumi.Input[InstanceCryptoKeyConfigArgs]]:
        
        ...
    
    @crypto_key_config.setter
    def crypto_key_config(self, value: Optional[pulumi.Input[InstanceCryptoKeyConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocServiceAccount")
    def dataproc_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataproc_service_account.setter
    def dataproc_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRbac")
    def enable_rbac(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_rbac.setter
    def enable_rbac(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverMonitoring")
    def enable_stackdriver_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_monitoring.setter
    def enable_stackdriver_monitoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventPublishConfig")
    def event_publish_config(self) -> Optional[pulumi.Input[InstanceEventPublishConfigArgs]]:
        
        ...
    
    @event_publish_config.setter
    def event_publish_config(self, value: Optional[pulumi.Input[InstanceEventPublishConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcs_bucket.setter
    def gcs_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[InstanceNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[InstanceNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="p4ServiceAccount")
    def p4_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @p4_service_account.setter
    def p4_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchRevision")
    def patch_revision(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @patch_revision.setter
    def patch_revision(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateInstance")
    def private_instance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @private_instance.setter
    def private_instance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    @_utilities.deprecated(...)
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_endpoint.setter
    def service_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantProjectId")
    def tenant_project_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_project_id.setter
    def tenant_project_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:datafusion/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceAcceleratorArgs, InstanceAcceleratorArgsDict]]]]] = ..., crypto_key_config: Optional[pulumi.Input[Union[InstanceCryptoKeyConfigArgs, InstanceCryptoKeyConfigArgsDict]]] = ..., dataproc_service_account: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_rbac: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., event_publish_config: Optional[pulumi.Input[Union[InstanceEventPublishConfigArgs, InstanceEventPublishConfigArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[InstanceNetworkConfigArgs, InstanceNetworkConfigArgsDict]]] = ..., options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., patch_revision: Optional[pulumi.Input[_builtins.str]] = ..., private_instance: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceAcceleratorArgs, InstanceAcceleratorArgsDict]]]]] = ..., api_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., crypto_key_config: Optional[pulumi.Input[Union[InstanceCryptoKeyConfigArgs, InstanceCryptoKeyConfigArgsDict]]] = ..., dataproc_service_account: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_rbac: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., event_publish_config: Optional[pulumi.Input[Union[InstanceEventPublishConfigArgs, InstanceEventPublishConfigArgsDict]]] = ..., gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[InstanceNetworkConfigArgs, InstanceNetworkConfigArgsDict]]] = ..., options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., p4_service_account: Optional[pulumi.Input[_builtins.str]] = ..., patch_revision: Optional[pulumi.Input[_builtins.str]] = ..., private_instance: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., service_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_message: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenant_project_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> pulumi.Output[Optional[Sequence[outputs.InstanceAccelerator]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyConfig")
    def crypto_key_config(self) -> pulumi.Output[Optional[outputs.InstanceCryptoKeyConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocServiceAccount")
    def dataproc_service_account(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRbac")
    def enable_rbac(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverMonitoring")
    def enable_stackdriver_monitoring(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventPublishConfig")
    def event_publish_config(self) -> pulumi.Output[Optional[outputs.InstanceEventPublishConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[Optional[outputs.InstanceNetworkConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="p4ServiceAccount")
    def p4_service_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchRevision")
    def patch_revision(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateInstance")
    def private_instance(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    @_utilities.deprecated(...)
    def service_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantProjectId")
    def tenant_project_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


